public class Main {

    public static void main(String[] args) {
	// write your code here
        LinkedList<Integer> linkedlist = new LinkedList<>();
        for(int i = 0 ;i<10;i++) {
            linkedlist.addFirst(i);
            System.out.println(linkedlist);
        }
        System.out.println(linkedlist.getSize());

        linkedlist.remove(5);
        System.out.println(linkedlist);
    }
}
