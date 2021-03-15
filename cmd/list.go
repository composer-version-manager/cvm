package cmd

import (
	"cvm-go/internal/composer"
	"cvm-go/internal/github"
	"fmt"

	"github.com/fatih/color"
	"github.com/spf13/cobra"
)

var (
	clearCache bool
	allCache   bool
	listCmd    = &cobra.Command{
		Use:   "list",
		Short: "print a list of composer versions",
		Run: func(cmd *cobra.Command, args []string) {

			c := github.New("composer", "composer")
			tags, err := c.Tags(clearCache)
			if err != nil {
				fmt.Printf("Could not list tags: %v\n", err)
			}

			if allCache {
				showAllTags(tags)
			} else {
				showInstalledTags(tags)
			}
		},
	}
)

func init() {
	listCmd.Flags().BoolVar(&clearCache, "clear-cache", false, "Clear the local cache")
	listCmd.Flags().BoolVar(&allCache, "all", false, "Shows all composer versions")
}

func showAllTags(tags []string) {
	b := color.New(color.FgBlue)
	for _, tag := range tags {
		fmt.Printf(" *  %s", tag)
		if composer.IsInstalled(tag) {
			b.Println(" (Installed)")
		} else {
			fmt.Println()
		}
	}
}

func showInstalledTags(tags []string) {
	for _, tag := range tags {
		if composer.IsInstalled(tag) {
			fmt.Printf(" *  %s\n", tag)
		}
	}
}
