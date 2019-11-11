package main

import "fmt"
import "strings"


func count() {
	words := "hello沙河小王子123１２３"
	count := 0
	const startCode = 0x2E80
	const endCode = 0x9FFF
	for _, w := range words {
		if startCode < w && endCode > w {
			count++
		}
	}
	fmt.Println("中文字符数:", count)
}

func main() {
	path := "/usr/local/go"
	ret := strings.Split(path, "/")
	fmt.Println(ret)

	// byte and rune
	s := "Hello123是１２３"
	n := len(s)
	fmt.Println(n)

	// for _, c := range s {
	// 	fmt.Printf("%c\n", c)
	// }

	//修改字符串
	s2 := "白萝卜"
	s3 := []rune(s2) //构成一个rune切片
	s3[0] = '红'
	fmt.Println(string(s3))

	c1 := '宏'
	c2 := "红"
	fmt.Printf("%d\n",0x2e80)
	fmt.Printf("%T %#v\n", c1, c1) //int32  3*8=24位
	fmt.Printf("%d\n",0x9fff)
	fmt.Printf("%T %#v\n", c2, c2)

	c3 := 'd'
	c4 := "d"
	fmt.Printf("%T %#v\n", c3, c3) //int32  3*8=24位
	fmt.Printf("%T %#v\n", c4, c4)

	count()
}
