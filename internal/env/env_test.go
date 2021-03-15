package env_test

import (
	"cvm-go/internal/env"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

var _ = Describe("Env", func() {

	Context("Has test", func() {

		var (
			isSet  bool
			values string
			toFind string
		)

		BeforeEach(func() {
			toFind = "a/path/to/set"
			values = "a/path/to/set:another/path/to/set"
		})

		JustBeforeEach(func() {
			isSet = env.Has(values, toFind)
		})

		It("is set", func() {
			Expect(isSet).To(BeTrue())
		})

		When("the path is not set", func() {
			BeforeEach(func() {
				values = "not/a/set/path"
			})

			It("is set", func() {
				Expect(isSet).To(BeFalse())
			})
		})
	})

	Context("Remove test", func() {
		var (
			resultVal   string
			expectedVal string
			values      string
			toRemove    string
		)

		BeforeEach(func() {
			toRemove = "a/path/to/remove"
			values = "a/path/to/remove:another/path/to/remove"
			expectedVal = "another/path/to/remove"
		})

		JustBeforeEach(func() {
			resultVal = env.Remove(values, toRemove)
		})

		It("removes the value", func() {
			Expect(resultVal).To(Equal(expectedVal))
		})

		When("there is more than one value in the path", func() {

			BeforeEach(func() {
				values = "a/path/to/remove:another/path/to/remove:a/third/path"
				expectedVal = "another/path/to/remove:a/third/path"
			})

			It("removes the value", func() {
				Expect(resultVal).To(Equal(expectedVal))
			})
		})

		When("it is not the first value in the list", func() {

			BeforeEach(func() {
				values = "i/am/first:a/path/to/remove:another/path/to/remove:a/third/path"
				expectedVal = "i/am/first:another/path/to/remove:a/third/path"
			})

			It("removes the value", func() {
				Expect(resultVal).To(Equal(expectedVal))
			})
		})

		When("it is already removed from the list", func() {
			BeforeEach(func() {
				values = "i/am/first:a/path/to/removeNOT:another/path/to/remove:a/third/path"
				expectedVal = "i/am/first:a/path/to/removeNOT:another/path/to/remove:a/third/path"
			})

			It("does not change the result", func() {
				Expect(resultVal).To(Equal(expectedVal))
			})

		})
	})
})
