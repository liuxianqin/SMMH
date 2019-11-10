### main包
可以得到可执行文件。
### main函数
没有参数也没有返回值

### 导入语句
双引号

### 函数外面只能放变量的声明　不能执行逻辑语句

```go
package main

import "fmt"

func main(){
	fmt.Println("Hello world")
}
```

### 标识符

25个关键字　37个保留字

### 变量

需要声明再使用

#### 声明变量 　　非全局			变量声明了就必须使用

`var s1 string`　声明的时候保存类型

### 格式化保存

`$ go fmt main.go`

### 短变量声明

`s3 := "hahaha"`

只能在函数体内使用

### anonymous variable

```go
func foo(int, string){
    return 10, "zhangsan"
}
func main(){
    x,_ = foo()
    _,y = foo()
}
```

用不到就报错。有些不想用：使用匿名变量　　匿名变量不会分配内存　

在函数外　语句必须以关键字开头

### const

```go
const pi = 3.1415

const (
	statusOK = 200
    notFound = 404
)

// 批量声明常量
const (
	n1 = 100
    n2
    n3
)
//n1 n2 n3 都是１００
```











