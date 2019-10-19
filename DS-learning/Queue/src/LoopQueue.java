import java.util.Objects;

public class LoopQueue<E> implements Queue<E>{

    private E[] data;
    private int front ,tail;
    private int size;

    public LoopQueue(int capacity){
        data =(E[]) new Object[capacity + 1];
        front = 0;
        tail = 0;
        size =0;
    }
    public LoopQueue(){
        this(10);
    }

    public int getCapaticy(){
        return data.length -1;
    }

    @Override
    public boolean isEmpty(){
        return front == tail;
    }

    @Override
    public int getSize(){
        return size;
    }

    @Override
    public void enqueue(E e){

        if( (tail + 1)% data.length == front )
            resize(getCapaticy()*2);

        data[tail] = e;
        tail = (tail +1 )% data.length;
        size ++;
    }

    @Override
    public E dequeue(){
        if(isEmpty())
            throw new IllegalArgumentException("Queue is empty");
        E ret = data[front];
        data[front] = null;
        front = (front + 1) % data.length;
        if(size == getCapaticy()/4  && getCapaticy()/2 !=0)
            resize(getCapaticy()/2);

        return ret;
    }

    private void resize(int newCapacity){
        E[] newData = (E[])new  Object[newCapacity+1];
        for(int i=0;i<size  ;i++)
            newData[i] = data[(i+front) % data.length];
        data = newData;
        front = 0;
        tail = size;
    }

    @Override
    public E getFront(){
        if(isEmpty())
            throw new IllegalArgumentException("Queue is Empty");
        return data[front];
    }

    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();
        res.append(String.format("Queue: size = %d , capaticy = %d\n", size, getCapaticy())) ;
        res.append("front [");
        for(int i = front; i != tail; i=(i+1)%data.length){
            res.append(data[i]);
            if((i+1)%data.length != tail )
                res.append(", ");
        }
        res.append("] tail");
        return res.toString();
    }

    public static void main(String[] args){
        ArrayQueue<Integer> queue = new ArrayQueue<>();
        for(int i=0;i<20;i++){
            queue.enqueue(i);
            System.out.println(queue);
        }

        queue.dequeue();
        queue.dequeue();
        System.out.println(queue);
    }
}
