package cmd

import "github.com/spf13/cobra"

var (
	rootCmd = &cobra.Command{
		Use:   "cvm",
		Short: "Composer version manager",
		Long:  `A tool to manager your composer versions`,
	}
)

func Execute() error {
	return rootCmd.Execute()
}

func init() {
	rootCmd.AddCommand(listCmd)
	rootCmd.AddCommand(useCmd)
	rootCmd.AddCommand(scanCmd)
	rootCmd.AddCommand(hookCmd)
	rootCmd.AddCommand(cacheCmd)
}
