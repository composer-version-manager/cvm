package github

import (
	"cvm-go/internal/cache"
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"path/filepath"
)

var (
	cacheFileName = "tags.json"
	baseURL       = "https://api.github.com/repos"
)

type tag struct {
	Name string `json:"name"`
}

type githubErrorMsg struct {
	Message string `json:"message"`
}

type client struct {
	OwnerID string
	RepoID  string
}

type Github interface {
	Tags(clearCache bool) ([]string, error)
}

func New(ownerID, repoID string) Github {
	c := client{
		OwnerID: ownerID,
		RepoID:  repoID,
	}
	return &c
}

func getTags(page int, ownerID, repoID string) ([]tag, error) {
	url := fmt.Sprintf("%s/%s/%s/tags?page=%d", baseURL, ownerID, repoID, page)
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	respBody, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}
	if resp.StatusCode != http.StatusOK {
		var eMsg githubErrorMsg
		err = json.Unmarshal(respBody, &eMsg)
		if err != nil {
			return nil, err
		}
		return nil, errors.New(eMsg.Message)
	}

	var tags []tag
	err = json.Unmarshal(respBody, &tags)
	if err != nil {
		return nil, err
	}
	return tags, err
}

func fromCache() ([]string, error) {
	cacheFilePath := filepath.Join(cache.GetRootDir(), cacheFileName)
	if _, err := os.Stat(cacheFilePath); os.IsNotExist(err) {
		return []string{}, err
	}
	raw, err := ioutil.ReadFile(cacheFilePath)
	if err != nil {
		return []string{}, err
	}

	var tags []string
	err = json.Unmarshal(raw, &tags)
	if err != nil {
		return []string{}, err
	}

	return tags, nil
}

func fromGitlab(ownerID, repoID string) ([]string, error) {
	page := 1
	var s []string
	for {
		tags, err := getTags(page, ownerID, repoID)
		page++
		if err != nil {
			return nil, err
		}
		if len(tags) <= 0 {
			return s, nil
		}
		for _, tag := range tags {
			s = append(s, tag.Name)
		}
	}
}

func removeCache() error {
	cacheFilePath := filepath.Join(cache.GetRootDir(), cacheFileName)
	if _, err := os.Stat(cacheFilePath); os.IsNotExist(err) {
		return nil
	}
	err := os.Remove(cacheFilePath)
	if err != nil {
		return err
	}
	return nil
}

// Return a list of all the Composer version tags
func (c *client) Tags(clearCache bool) ([]string, error) {

	var tags []string
	var err error
	if !clearCache {
		tags, err = fromCache()
		if err != nil && !os.IsNotExist(err) {
			return []string{}, err
		}
		if err == nil {
			return tags, nil
		}
	}

	err = removeCache()
	if err != nil {
		return []string{}, nil
	}

	tags, err = fromGitlab(c.OwnerID, c.RepoID)
	if err != nil {
		return []string{}, err
	}

	data, err := json.MarshalIndent(tags, "", "")
	if err != nil {
		return []string{}, err
	}

	cacheFilePath := filepath.Join(cache.GetRootDir(), cacheFileName)
	err = ioutil.WriteFile(cacheFilePath, data, 0644)
	if err != nil {
		return []string{}, err
	}
	return tags, nil
}
