package cache

import (
	"log"
	"os"
	"path/filepath"
)

var (
	FS       fileSystem
	rootDir  string
	cacheDir string
	setupDir string
)

func performInit() {
	h, err := os.UserHomeDir()
	if err != nil {
		log.Fatal(err)
	}
	rootDir = filepath.Join(h, ".cvm")
	if _, err := FS.Stat(rootDir); os.IsNotExist(err) {
		os.Mkdir(rootDir, 0755)
	}
	cacheDir = filepath.Join(rootDir, "cache")
	if _, err := FS.Stat(cacheDir); os.IsNotExist(err) {
		FS.Mkdir(cacheDir, 0755)
	}
	setupDir = filepath.Join(rootDir, "setup")
	if _, err := FS.Stat(setupDir); os.IsNotExist(err) {
		FS.Mkdir(setupDir, 0755)
	}
}

func init() {
	FS = fs
	performInit()
}

// GetRootDir returns the path to the root cache directory
func GetRootDir() string { return rootDir }

// GetCacheDir returns the path to the composer cache directory
func GetCacheDir() string { return cacheDir }

// GetCacheDir returns the path to the composer setup directory
func GetSetupDir() string { return setupDir }

// GetInstallDir returns the path to the install directory of the given tag
func GetInstallDir(tag string) string {
	installDir := filepath.Join(cacheDir, tag)
	if _, err := FS.Stat(installDir); os.IsNotExist(err) {
		FS.Mkdir(installDir, 0755)
	}
	return installDir
}
