package config

import (
	"encoding/json"
	"io/ioutil"
	"os"
	"path/filepath"
)

var (
	confFileName = ".cvm_config"
	FS           fileSystem
)

func init() {
	FS = fs
}

type Config struct {
	Version string `json:"version"`
}

type ConfigClient interface {
	Scan(dir string) (string, bool)
	Read(confFilePath string) (Config, error)
	Save(tag string) error
}

type conf struct {
}

func New() ConfigClient {
	c := conf{}
	return &c
}

// Scan the dir and parent dir for the .cvm_config file
func (c *conf) Scan(dir string) (string, bool) {
	for {
		confFile, ok := hasConf(dir)
		if ok {
			return confFile, true
		}
		dir = filepath.Dir(dir)
		if dir == "." || dir == "/" {
			return "", false
		}
	}
}

func hasConf(dir string) (string, bool) {
	confPath := filepath.Join(dir, confFileName)
	_, err := FS.Stat(confPath)
	if os.IsNotExist(err) {
		return "", false
	}
	return confPath, true
}

// Read the conf file
func (c *conf) Read(confFilePath string) (Config, error) {
	content, err := ioutil.ReadFile(confFilePath)
	if err != nil {
		return Config{}, err
	}

	var data Config
	err = json.Unmarshal(content, &data)
	if err != nil {
		return Config{}, err
	}
	return data, nil
}

// Save the config file
func (c *conf) Save(tag string) error {
	cnf := Config{
		Version: tag,
	}
	raw, err := json.Marshal(cnf)
	if err != nil {
		return err
	}

	ioutil.WriteFile(confFileName, raw, 0644)
	return nil
}
