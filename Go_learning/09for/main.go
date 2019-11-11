package main

import "fmt"

func main() {

	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}
	fmt.Println()

	//省略初始语句
	var i = 5
	for ; i < 10; i++ {
		fmt.Println(i)
	}

	//省略结束语句
	// var j = 8
	// for j < 10 {
	// 	fmt.Println(j)
	// }

	//无限循环
	// for {
	// 	fmt.Println(123)
	// }

	//for range 键值循环
	//可以遍历　　数组　切片　字符串　ｍａｐ　通道
	s := "Hello沙河"
	for i, v := range s {
		// fmt.Println(i, v)
		fmt.Printf("%d,%c\n", i, v)
	}

}
