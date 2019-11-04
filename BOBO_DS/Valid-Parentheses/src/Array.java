import java.util.Objects;

public class Array<E> {
    private E[] data;
    private int size;

    //构造函数
    public Array(int capacity){
        data =(E[]) new Object[capacity];
        size = 0;
    }

    //无参构造函数
    public Array(){
        this(10);
    }

    //获取元素个数
    public int getSize(){
        return size;
    }

    //获取元素容量
    public int getCapacity(){
        return data.length;
    }

    //返回数组是否为空
    public boolean isEmpty(){
        return size == 0;
    }

    //向末尾添加元素
    public void addLast(E e){
//        if(size == data.length)
//            throw new IllegalArgumentException("Array is full.");
//        data[size] = e;
//        size ++;
        add(size, e);
    }

    //向第一个位置添加元素
    public void addFirst(E e){
        add(0,e);
    }

    //向制定位置添加元素
    public void add(int index, E e){
        if(index < 0 || index > size)
            throw new IllegalArgumentException("Array is full.");
        if(size == data.length)
            resize(2*data.length);

        for (int i = size -1 ; i >=index ; i--)
            data[i+1] = data[i];
        data[index] = e;
        size ++;
    }

    //得到索引为index的元素
    public E  get(int index){
        if(index<0 || index >= size)
            throw new IllegalArgumentException("Index is illegal");
        return data[index];
    }

    public E getLast(){
        return get(size-1);
    }

    // 修改index索引位置的元素为e
    void set(int index ,E e){
        if(index<0 || index >= size)
            throw new IllegalArgumentException("Index is illegal");
        data[index]=e;
    }


    public boolean contains(E e){
        for(int i=0;i<size;i++){
            if(data[i].equals(e))
                return true;
        }
        return false;
    }

    public int find(E e){
        for(int i=0;i<size;i++) {
            if (data[i].equals(e))
                return i;
        }

        return -1;
    }


    //从指定位置删除元素 返回删除元素
    public E remove(int index){
        if(index<0 || index >= size)
            throw new IllegalArgumentException("Index is illegal");
        E ret = data[index];
        for(int i=index+1;i<size;i++){
            data[i-1] = data[i];
        }
        size --;
        data[size] = null;// loitering objects

        if (size == data.length/4  && data.length/2!=0)
            resize(data.length/2);

        return ret;
    }

    public E removeFirst(){
        return remove(0);
    }
    public E removeLast(){
        return remove(size-1);
    }

    public boolean removeElem(E elem){
        int index = find(elem);
        if (index != -1) {
            remove(index);
            return true;
        }
        return false;
    }

    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();
        res.append(String.format("Array: size = %d , capaticy = %d\n", size, data.length));
        res.append('[');
        for(int i = 0; i<size;i++){
            res.append(data[i]);
            if(i != size-1)
                res.append(", ");
        }
        res.append(']');
        return res.toString();
    }


    private void resize(int newCapacity){
        E[] newData =(E[]) new Object[newCapacity];
        for(int i=0;i<size;i++)
            newData[i]=data[i];
        data = newData;
    }
}
