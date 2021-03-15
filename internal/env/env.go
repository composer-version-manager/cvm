package env

import (
	"os"
	"strings"
)

// Has checks if the given environment key has the given value
func Has(values, toFind string) bool {

	split := strings.Split(values, ":")
	for _, val := range split {
		if toFind == val {
			return true
		}
	}
	return false
}

// Remove a value from a given environment key
func Remove(values, toRemove string) string {
	var newValues []string
	split := strings.Split(values, ":")
	for _, v := range split {
		if toRemove != v {
			newValues = append(newValues, v)
		}
	}
	return strings.Join(newValues, ":")
}

// Get an env vairable, uses fallback if it is not set
func Get(key, fallback string) string {
	value := os.Getenv(key)
	if len(value) == 0 {
		return fallback
	}
	return value
}
