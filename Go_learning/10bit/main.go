package main

import "fmt"

func main() {

	//位运算
	// 5 101
	// 2  10

	//按位与
	fmt.Println(5 & 2)
	//按位或
	fmt.Println(5 | 2)
	// ^ 亦或
	fmt.Println(5 ^ 2)
	//左移
	fmt.Println(5 << 1)
	fmt.Println(1 << 10)

	//装不下
	var m = int8(1)
	fmt.Println(m << 10) //10000000000

	//应用
	//IP计算
	//权限计算
}
