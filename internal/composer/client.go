package composer

import (
	"cvm-go/internal/cache"
	"fmt"
	"io"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
)

var (
	setupDownloadURL = "https://getcomposer.org/installer"
	setupFilename    = "composer-setup.php"
)

type client struct{}

type Composer interface {
	Install(tag string, verbose bool) error
	GetPath(tag string) (string, error)
	GetVendorBinDir(tag string) string
}

func New() Composer {
	c := client{}
	return &c
}

// Install the given composer version
func (c *client) Install(tag string, verbose bool) error {
	installDir := cache.GetInstallDir(tag)

	setupFilePath := filepath.Join(cache.GetSetupDir(), setupFilename)
	if _, err := os.Stat(setupFilePath); os.IsNotExist(err) {
		downloadFile(setupFilePath, setupDownloadURL)
	}
	installFlag := fmt.Sprintf("--install-dir=%s", installDir)
	fnameFlag := "--filename=composer"
	versionFlag := fmt.Sprintf("--version=%s", tag)

	out, err := exec.Command("php", setupFilePath, installFlag, fnameFlag, versionFlag).Output()
	if verbose {
		fmt.Println(string(out))
	}

	return err
}

// GetPath for the installed composer version
func (c *client) GetPath(tag string) (string, error) {
	if !IsInstalled(tag) {
		return "", os.ErrNotExist
	}
	return cache.GetInstallDir(tag), nil
}

func (c *client) GetVendorBinDir(tag string) string {
	return filepath.Join(cache.GetInstallDir(tag), "vendor", "bin")
}

// IsInstalled check if the given version is installed
func IsInstalled(tag string) bool {
	composerFile := filepath.Join(cache.GetCacheDir(), tag, "composer")
	if _, err := os.Stat(composerFile); os.IsNotExist(err) {
		return false
	}
	return true
}

func downloadFile(filepath string, url string) error {

	resp, err := http.Get(url)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	out, err := os.Create(filepath)
	if err != nil {
		return err
	}
	defer out.Close()

	_, err = io.Copy(out, resp.Body)
	return err
}
