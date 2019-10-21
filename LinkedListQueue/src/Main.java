public class Main {

    public static void main(String[] args) {
	// write your code here
        LinkedListQueue<Integer> queue = new LinkedListQueue<>();
        for(int i = 0 ; i<10;i++){
            queue.enqueue(i);
            System.out.println(queue);
        }

        queue.dequeue();
        queue.dequeue();
        queue.dequeue();
        System.out.println(queue);
    }
}
