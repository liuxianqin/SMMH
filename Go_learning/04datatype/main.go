package main

import "fmt"

func main() {
	var a int = 10
	fmt.Printf("%d \n", a)
	fmt.Printf("%b \n", a)
	// %d 10 用println打印不出来%d

	var i1 = 101
	fmt.Printf("%d\n", i1)
	i2 := 077
	fmt.Printf("%d\n", i2)
	i3 := 0xff123
	fmt.Printf("%T\n", i3)
}
