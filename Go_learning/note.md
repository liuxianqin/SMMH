# Go

编译型语言
关键字少　２５个
２１世纪的Ｃ语言

百度　腾讯蓝鲸　知乎之前用Ｐｙｔｈｏｎ　后来用Ｇｏ重构　节约８０％的服务器
协作开发效率高　
天生支持并发　语言层面支持　
企业级编程语言　　　业务的事情都能做



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



### iota

计数器

```go
const (
	n1 = iota //0
    n2 		  //1
    n3        //2
    n4        //4
)
```

定义数量级

```go
//定义数量级

const (
	_  = iota
    KB = 1 << (10 * iota)
    MB = 1 << (10 * iota)
    GB = 1 << (10 * iota)
    TB = 1 << (10 * iota)
    PB = 1 << (10 * iota)
    
)
```

### 　整型

## 整型

整型分为以下两个大类： 按长度分为：int8、int16、int32、int64 对应的无符号整型：uint8、uint16、uint32、uint64

其中，`uint8`就是我们熟知的`byte`型，`int16`对应C语言中的`short`型，`int64`对应C语言中的`long`型。

|  类型  | 描述                                                         |
| :----: | :----------------------------------------------------------- |
| uint8  | 无符号 8位整型 (0 到 255)                                    |
| uint16 | 无符号 16位整型 (0 到 65535)                                 |
| uint32 | 无符号 32位整型 (0 到 4294967295)                            |
| uint64 | 无符号 64位整型 (0 到 18446744073709551615)                  |
|  int8  | 有符号 8位整型 (-128 到 127)                                 |
| int16  | 有符号 16位整型 (-32768 到 32767)                            |
| int32  | 有符号 32位整型 (-2147483648 到 2147483647)                  |
| int64  | 有符号 64位整型 (-9223372036854775808 到 9223372036854775807) |



### 八进制数

在Linux表示权限　　0644 是一个八进制数

### 查看变量类型

`%T`

### 声明int8类型的变量

`i := int8(9)`

`%v` 打印所有类型的ｖａｌｕｅ的值

`%#v`　明显的的方式打印值　　字符串加上了双引号



### ｓｔｒｉｎｇ

用反引号　打印多行话

用反引号的时候可以避免　转义字符的麻烦



### 字符串拼接  分割

```go
name := "LLP"
adj := "OK"
ss2 := fmt.Sprintf("%s%s",name,adj)

path := "/usr/local/go"
ret := strings.Split(path,"/") 
// ret   [ usr local go]
```



### 前后缀　子串

`strings.HasPrefix`

`strings.HasSuffix`

`strings.index()`

`strings.LastIndex()`

