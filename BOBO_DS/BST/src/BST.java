public class BST<E extends Comparable<E>> {
    private class Node{
        public E val;
        public Node left;
        public Node right;
        public Node(E e){
            this.val = e;
            left = null;
            right = null;
        }
    }


    private Node root;
    private int size;

    BST(){
        root = null;
        size = 0;
    }

    public int getSize(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public void add(E e){
        if(root == null) {
            root = new Node(e);
            size ++;
        }

        add(root,e);
    }

    private void add(Node root, E e){

        if(e.equals(root.val)) return;
        else if(e.compareTo(root.val)<0 && root.left == null){
            root.left = new Node(e);
            size ++;
        }
        else if (e.compareTo(root.val)>0 && root.right == null){
//            root.right =e;
            root.right = new Node(e);
            size ++;
        }
        if (e.compareTo(root.val)<0 )
            add(root.left,e);
        else
            add(root.right,e);

    }



}
