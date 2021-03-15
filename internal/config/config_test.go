package config_test

import (
	"cvm-go/internal/config"
	"cvm-go/internal/config/configfakes"
	"os"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("Config", func() {

	Context("Scan tests", func() {
		var (
			configFile   string
			ok           bool
			configClient config.ConfigClient
			dir          string
			fakeFS       *configfakes.FakeFileSystem
		)

		BeforeEach(func() {
			fakeFS = &configfakes.FakeFileSystem{}
			config.FS = fakeFS
			configClient = config.New()
			dir = "."
			fakeFS.StatReturns(nil, nil)
		})

		JustBeforeEach(func() {
			configFile, ok = configClient.Scan(dir)
		})

		It("returns ok", func() {
			Expect(ok).To(BeTrue())
		})

		It("gets a config file", func() {
			Expect(configFile).To(Equal(".cvm_config"))
		})

		When("the config file is in the parent folder", func() {
			BeforeEach(func() {
				dir = "a/path/to/the/parent/directory"
				stub := func(s string) (os.FileInfo, error) {
					if s == "a/path/to/the/.cvm_config" {
						return nil, nil
					}
					return nil, os.ErrNotExist
				}
				fakeFS.StatCalls(stub)
			})

			It("returns ok", func() {
				Expect(ok).To(BeTrue())
			})

			It("does not gets a config file", func() {
				Expect(configFile).To(Equal("a/path/to/the/.cvm_config"))
			})
		})

		When("there is no config file", func() {
			BeforeEach(func() {
				fakeFS.StatReturns(nil, os.ErrNotExist)
			})

			It("does not return ok", func() {
				Expect(ok).To(BeFalse())
			})
			It("does not gets a config file", func() {
				Expect(configFile).To(Equal(""))
			})
		})

		When("there is no config even in the parent folder", func() {
			BeforeEach(func() {
				dir = "/a/path/to/the/parent/directory"
				stub := func(s string) (os.FileInfo, error) {
					return nil, os.ErrNotExist
				}
				fakeFS.StatCalls(stub)
			})

			It("returns ok", func() {
				Expect(ok).To(BeFalse())
			})

			It("does not gets a config file", func() {
				Expect(configFile).To(Equal(""))
			})
		})

		Context("Test different line endings", func() {
			BeforeEach(func() {
				stub := func(s string) (os.FileInfo, error) {
					return nil, os.ErrNotExist
				}
				fakeFS.StatCalls(stub)
			})

			When("the file path ends with .", func() {
				BeforeEach(func() {
					dir = "."
				})
				It("returns ok", func() {
					Expect(ok).To(BeFalse())
				})
			})

			When("the file path ends with /", func() {
				BeforeEach(func() {
					dir = "/"
				})
				It("returns ok", func() {
					Expect(ok).To(BeFalse())
				})
			})

			When("the file path ends with ", func() {
				BeforeEach(func() {
					dir = ""
				})
				It("returns ok", func() {
					Expect(ok).To(BeFalse())
				})
			})

			When("the file path ends with ", func() {
				BeforeEach(func() {
					dir = "./a/path"
				})
				It("returns ok", func() {
					Expect(ok).To(BeFalse())
				})
			})
		})
	})
})
