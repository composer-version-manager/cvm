package cmd

import (
	"cvm-go/internal/shell"
	"fmt"
	"log"
	"os"

	"github.com/spf13/cobra"
)

var (
	hookCmd = &cobra.Command{
		Use:       "hook [bash|zsh]",
		Short:     "hook cvm to a shell",
		Args:      cobra.ExactValidArgs(1),
		ValidArgs: []string{"bash", "zsh"},
		Run: func(cmd *cobra.Command, args []string) {
			shell, err := shell.GetShell(args[0])
			if err != nil {
				log.Fatal(err)
				os.Exit(1)
			}
			fmt.Println(shell.Hook())
		},
	}
)
