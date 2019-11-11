package main

import "fmt"
import "strings"

func main() {
	path := "/usr/local/go"
	ret := strings.Split(path, "/")
	fmt.Println(ret)


	// byte and rune
	s := "Hello123是１２３"
	n := len(s)
	fmt.Println(n)

	for _, c := range s{
		fmt.Printf("%c\n",c)
	}
}
