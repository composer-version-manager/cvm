package main_test

import (
	"testing"

	. "github.com/onsi/ginkgo"
	. "github.com/onsi/gomega"
)

func TestCvmGo(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "CvmGo Suite")
}
