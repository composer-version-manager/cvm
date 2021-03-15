package cmd

import (
	"cvm-go/internal/composer"
	"cvm-go/internal/config"
	"cvm-go/internal/env"
	"fmt"
	"log"
	"os"

	"github.com/spf13/cobra"
)

const (
	cvm_set       = "CVM_SET"
	composer_home = "COMPOSER_HOME"
	path          = "PATH"
)

var (
	searchPath string
	scanCmd    = &cobra.Command{
		Use:       "scan [bash|zsh]",
		Short:     "If present use .cvm_config from the current or specified directory",
		Args:      cobra.ExactValidArgs(1),
		ValidArgs: []string{"bash", "zsh"},
		Run: func(cmd *cobra.Command, args []string) {

			cfgClient := config.New()
			compClient := composer.New()

			cfgFile, cfgScanOK := cfgClient.Scan(searchPath)
			setTag, hasTagOK := hasCMVSet()

			if hasTagOK && !cfgScanOK {
				unset(setTag, compClient)
			}

			if !cfgScanOK {
				os.Exit(0)
			}

			cfg, err := cfgClient.Read(cfgFile)
			if err != nil {
				log.Fatal(err)
				os.Exit(1)
			}

			if cfg.Version == setTag {
				os.Exit(1)
			}

			if hasTagOK {
				unset(setTag, compClient)
			}

			if !composer.IsInstalled(cfg.Version) {
				err = compClient.Install(cfg.Version, false)
				if err != nil {
					log.Fatal(err)
					os.Exit(1)
				}
			}

			set(cfg.Version, compClient)
		},
	}
)

func init() {
	defaultPath, err := os.Getwd()
	if err != nil {
		log.Println(err)
	}

	scanCmd.Flags().StringVar(&searchPath, "path", defaultPath, "Path to search for a .cvm_config file")
}

func hasCMVSet() (string, bool) {
	value := env.Get(cvm_set, "-1")
	if value == "-1" {
		return "", false
	}
	return value, true
}

func set(tag string, compClient composer.Composer) {
	composerPath, err := compClient.GetPath(tag)
	venderBinPath := compClient.GetVendorBinDir(tag)
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}

	msg := fmt.Sprintf("echo \"\033[0;33mSetting composer version: \033[0m%s\"", tag)
	setPaths := fmt.Sprintf("export PATH=%s:%s:$PATH; export COMPOSER_HOME=%s; export CVM_SET=%s;", composerPath, venderBinPath, composerPath, tag)
	fmt.Println(setPaths)
	fmt.Println(msg)

}

func unset(tag string, compClient composer.Composer) {
	composerPath, err := compClient.GetPath(tag)
	venderBinPath := compClient.GetVendorBinDir(tag)
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}

	oldPath := os.Getenv("PATH")
	newPath := env.Remove(oldPath, composerPath)
	newPath = env.Remove(newPath, venderBinPath)

	msg := fmt.Sprintf("echo \"\033[0;31mUnsetting composer version: \033[0m%s\"", tag)
	envs := fmt.Sprintf("export PATH=%s; export COMPOSER_HOME=; export CVM_SET=-1;", newPath)
	fmt.Println(envs)
	fmt.Println(msg)
}
