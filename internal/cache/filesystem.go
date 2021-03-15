package cache

import (
	"os"
)

var fs fileSystem = osFS{}

//go:generate go run github.com/maxbrunsfeld/counterfeiter/v6 . fileSystem

type fileSystem interface {
	Stat(name string) (os.FileInfo, error)
	Mkdir(name string, perm os.FileMode) error
	Create(name string) (*os.File, error)
}

type osFS struct{}

func (osFS) Stat(name string) (os.FileInfo, error)     { return os.Stat(name) }
func (osFS) Mkdir(name string, perm os.FileMode) error { return os.Mkdir(name, perm) }
func (osFS) Create(name string) (*os.File, error)      { return os.Create(name) }
