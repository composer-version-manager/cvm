package config

import (
	"os"
)

var fs fileSystem = osFS{}

//go:generate go run github.com/maxbrunsfeld/counterfeiter/v6 . fileSystem

type fileSystem interface {
	Stat(name string) (os.FileInfo, error)
}

type osFS struct{}

func (osFS) Stat(name string) (os.FileInfo, error) { return os.Stat(name) }
