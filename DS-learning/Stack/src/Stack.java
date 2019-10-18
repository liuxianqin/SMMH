public interface Stack<E> {
    int getSize();
    boolean isEmpty();
    void push(E e);
    E pop();
    E peek();
}


//此处的接口是与栈的具体实现方式无关的、通用的方法。
