public class Array {
    private int[] data;
    private int size;

    //构造函数
    public Array(int capacity){
        data = new int[capacity];
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
    public void addLast(int e){
//        if(size == data.length)
//            throw new IllegalArgumentException("Array is full.");
//        data[size] = e;
//        size ++;
        add(size, e);
    }

    //向第一个位置添加元素
    public void addFirst(int e){
        add(0,e);
    }

    //向制定位置添加元素
    public void add(int index, int e){
        if(size == data.length)
            throw new IllegalArgumentException("Array is full.");
        if(index < 0 || index > size)
            throw new IllegalArgumentException("Array is full.");
        for (int i = size -1 ; i >=index ; i--)
            data[i+1] = data[i];
        data[index] = e;
        size ++;
    }

    //得到索引为index的元素
    public int  get(int index){
        if(index<0 || index >= size)
            throw new IllegalArgumentException("Index is illegal");
        return data[index];
    }

    // 修改index索引位置的元素为e
    void set(int index ,int e){
        if(index<0 || index >= size)
            throw new IllegalArgumentException("Index is illegal");
        data[index]=e;
    }


    public boolean contains(int e){
        for(int i=0;i<size;i++){
            if(data[i] == e)
                return true;
        }
        return false;
    }

    public int find(int e){
        for(int i=0;i<size;i++) {
            if (data[i] == e)
                return i;
        }

        return -1;
    }


    //从指定位置删除元素

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
}
