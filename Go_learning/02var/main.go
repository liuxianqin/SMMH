package main

import "fmt"

// var name string
// var age int
// var isOk bool

//批量声明
var (
	name string
	age  int
	isOk bool
)

func main() {

	name = "张三"
	age = 16
	isOk = true
	var sex string = "male"
	fmt.Printf("name:%s", name)
	fmt.Println(age) //add a　换行符
	fmt.Print(isOk)
	fmt.Println(sex)
}

//  student_name
//  studentName
//  StudentName
