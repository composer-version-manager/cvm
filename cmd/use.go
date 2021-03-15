package cmd

import (
	"cvm-go/internal/composer"
	"cvm-go/internal/config"
	"log"
	"os"

	"github.com/spf13/cobra"
)

var (
	useVerbose bool
	useNoSave  bool
	useCmd     = &cobra.Command{
		Use:   "use [Composer version]",
		Short: "Downloads the composer version and set the current working directory to use it",
		Args:  cobra.ExactArgs(1),
		Run: func(cmd *cobra.Command, args []string) {
			c := composer.New()
			conf := config.New()
			err := c.Install(args[0], useVerbose)
			if err != nil {
				log.Fatal(err)
				os.Exit(1)
			}
			if useNoSave {
				os.Exit(0)
			}
			err = conf.Save(args[0])
			if err != nil {
				log.Fatal(err)
				os.Exit(1)
			}
		},
	}
)

func init() {
	useCmd.Flags().BoolVar(&useVerbose, "verbose", false, "show verbose output")
	useCmd.Flags().BoolVar(&useNoSave, "no-save", false, "download the version only. Do not save the cvm_config file")
}
