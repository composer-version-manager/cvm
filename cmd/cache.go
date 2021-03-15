package cmd

import (
	"bufio"
	"cvm-go/internal/cache"
	"cvm-go/internal/composer"
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/fatih/color"
	"github.com/spf13/cobra"
)

var (
	cacheWhere    bool
	cacheClearAll bool
	cacheClear    string
	cacheCmd      = &cobra.Command{
		Use:   "cache",
		Short: "manage the cvm cache",
		Run: func(cmd *cobra.Command, args []string) {

			if cacheWhere {
				root := cache.GetRootDir()
				fmt.Println(root)
			}

			if cacheClearAll {

				reader := bufio.NewReader(os.Stdin)
				color.Red("** [Warning] **")
				fmt.Println("-> This will remove all composer versions from your cache. Do you want to continue (y/N)")
				text, _ := reader.ReadString('\n')
				text = strings.Replace(text, "\n", "", -1)
				if strings.Compare("y", text) != 0 {
					fmt.Println("Aborting")
					os.Exit(0)
				}

				fmt.Print("Removing Cache dir ... ")
				cacheDir := cache.GetCacheDir()
				err := os.RemoveAll(cacheDir)
				if err != nil {
					log.Fatal(err)
					os.Exit(1)
				}
				fmt.Println("Done")
			}

			if strings.Compare(cacheClear, "") != 0 {
				if composer.IsInstalled(cacheClear) {

					reader := bufio.NewReader(os.Stdin)
					color.Red("** [Warning] **")
					msg := fmt.Sprintf("-> This will remove composer version %s from your cache. Do you want to continue (y/N)", cacheClear)
					fmt.Println(msg)
					text, _ := reader.ReadString('\n')
					text = strings.Replace(text, "\n", "", -1)
					if strings.Compare("y", text) != 0 {
						fmt.Println("Aborting")
						os.Exit(0)
					}

					fmt.Print("Removing Cache dir ... ")
					installDir := cache.GetInstallDir(cacheClear)
					err := os.RemoveAll(installDir)
					if err != nil {
						log.Fatal(err)
						os.Exit(1)
					}
					fmt.Println("Done")
				} else {
					msg := fmt.Sprintf("composer version %s is not installed", cacheClear)
					fmt.Println(msg)
				}
			}
		},
	}
)

func init() {
	cacheCmd.Flags().BoolVar(&cacheWhere, "where", false, "Show the location of the cache")
	cacheCmd.Flags().BoolVar(&cacheClearAll, "clear-all", false, "Clean the composer cache")
	cacheCmd.Flags().StringVar(&cacheClear, "clear", "", "remove a composer version from the cache")
}
