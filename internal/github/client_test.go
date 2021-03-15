package github_test

import (
	"cvm-go/internal/github"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"

	"github.com/jarcoal/httpmock"
	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

type tag struct {
	Name string `json:"name"`
}

var _ = Describe("Service", func() {

	var (
		gServer github.Github
		owner   = "owner"
		repo    = "repo"
		baseURL = "https://api.github.com/repos"
	)

	BeforeEach(func() {
		gServer = github.New(owner, repo)
	})

	Context("List Test", func() {
		var (
			tags         []string
			err          error
			tagsBody     string
			expectedTags []string
		)

		BeforeEach(func() {
			httpmock.Activate()
			content, err := ioutil.ReadFile("tags.json")
			Expect(err).ToNot(HaveOccurred())

			var tags []tag
			err = json.Unmarshal(content, &tags)
			Expect(err).ToNot(HaveOccurred())
			for _, tag := range tags {
				expectedTags = append(expectedTags, tag.Name)
			}

			tagsBody = string(content)
		})

		AfterEach(func() {
			httpmock.Deactivate()
			expectedTags = []string{}
		})

		JustBeforeEach(func() {
			url := fmt.Sprintf("%s/%s/%s/tags?page=1", baseURL, owner, repo)
			httpmock.RegisterResponder(
				http.MethodGet,
				url,
				httpmock.NewStringResponder(http.StatusOK, tagsBody),
			)
			url = fmt.Sprintf("%s/%s/%s/tags?page=2", baseURL, owner, repo)
			httpmock.RegisterResponder(
				http.MethodGet,
				url,
				httpmock.NewStringResponder(http.StatusOK, "[]"),
			)
			tags, err = gServer.Tags(true)
		})

		It("does not return an error", func() {
			Expect(err).ToNot(HaveOccurred())
		})

		It("returns an expected tag list", func() {
			Expect(tags).To(Equal(expectedTags))
		})
	})
})
