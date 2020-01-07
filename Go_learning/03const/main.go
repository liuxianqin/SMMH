package main

import "fmt"

// const (
// 	n1 = iota
// 	n2 = iota
// 	n3 = iota
// )
const (
	n1 = iota
	n2
	n3 
)

const (
	c1 = iota
	c2 = 100
	c3 			//100
	c4 = iota + 100  
)

const (
	d1, d2 = iota + 1, iota + 2   // 1 2
	d3, d4 = iota + 1, iota + 2   // 2 3
)

const (
	_  = iota
    KB = 1 << (10 * iota)
    MB = 1 << (10 * iota)
    GB = 1 << (10 * iota)
    TB = 1 << (10 * iota)
    PB = 1 << (10 * iota)
    
)

func main() {
	fmt.Println("n1:", n1)
	fmt.Println("n2:", n2)
	fmt.Println("n3:", n3)

	fmt.Println("c1:", c1)
	fmt.Println("c2:", c2)
	fmt.Println("c3:", c3)
	fmt.Println("c4:", c4)

	fmt.Println("d1:", d1)
	fmt.Println("d2:", d2)
	fmt.Println("d3:", d3)
	fmt.Println("d4:", d4)

	
}
