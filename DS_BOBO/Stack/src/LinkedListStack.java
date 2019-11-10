public class LinkedListStack<E>  implements Stack<E> {
    private LinkedList<E> list;

    public LinkedListStack(){
        list = new LinkedList<>();
    }

    @Override
    public int getSize(){
        return list.getSize();
    }

    @Override
    public boolean isEmpty(){
        return list.isEmpty();
    }

    @Override
    public void push(E e){
        list.addFirst(e);
    }

    @Override
    public E pop(){
        E e = list.removeFirst();
        return e;
    }

    @Override
    public E peek(){
        return list.getFirst();
    }

    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();
        res.append("Stack : top ");
        res.append(list);
        res.append("|||");
        return res.toString();
    }


    public static void main(String[] args){
        LinkedListStack<Integer> stack = new LinkedListStack<>();
        for(int i=0;i<10;i++){
            stack.push(i);
            System.out.println(stack);
        }
    }

}
