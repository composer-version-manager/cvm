package shell

import (
	"fmt"
)

type Shell interface {
	Hook() string
}

func GetShell(name string) (Shell, error) {
	switch name {
	case "zsh":
		return Zsh, nil
	case "bash":
		return Bash, nil
	default:
		return nil, fmt.Errorf("unsupported shell: %s", name)
	}
}
