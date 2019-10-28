import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class BST<E extends Comparable<E>> {
    private class Node{
        public E e;
        public Node left,right;

        public Node(E e){
            this.e = e;
            left = null;
            right = null;
        }
    }

    private Node root;
    private int size;

    public BST(){
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
       root =  add(root,e);
    }


    private Node add(Node node, E e){
        if(node==null) {
            size ++;
            node =new  Node(e);
        }
        if(e.compareTo(node.e)<0){
            node.left = add(node.left,e);
        }
        else if(e.compareTo(node.e)>0){
            node.right = add(node.right,e);
        }
        return node;
    }

//    private Node add(Node root, E e){
//        if(root==null) {
//            size ++;
//            root =new  Node(e);
//        }
//        if(e.compareTo(root.e)<0){
//            root.left = add(root.left,e);
//        }
//        else if(e.compareTo(root.e)>0){
//            root.right = add(root.right,e);
//        }
//        return root;
//    }

    //查询元素
    public boolean contains(E e){
        return     contains(root,e);
    }
    private  boolean contains(Node node,E e){
        if(node == null)
            return false;
        if(e.compareTo(node.e)==0)
            return true;
        else if(e.compareTo(node.e)<0)
            return contains(node.left,e);
        else
            return contains(node.right,e);
    }

    //前序遍历
    public void preTraverse(){
        preTraverse(root);
    }
    private void preTraverse(Node node){
//        if(root == null) return;
        if(node != null) {
            System.out.println(node.e);
            preTraverse(node.left);
            preTraverse(node.right);
        }
    }

    public void inOrder(){
        inOrder(root);
    }

    private void inOrder(Node node){
        if(node==null)
            return;
        inOrder(node.left);
        System.out.println(node.e);
        inOrder(node.right);
    }

    public void postOrder(){
        postOrder(root);
    }
    private void postOrder(Node node){
        if(node == null)
            return;

        postOrder(node.left);
        postOrder(node.right);
        System.out.println(node.e);
    }

    public void PreOrder_notre(){
        Stack<Node> stack = new Stack<>();
        stack.push(root);
        while(!stack.isEmpty()){
            Node cur = stack.pop();
            System.out.println(cur.e);

            if(cur.right != null)
                stack.push(cur.right);
            if(cur.left != null)
                stack.push(cur.left);
        }
    }

    public void levelOrder(){
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        while(!queue.isEmpty()){
            Node cur = queue.remove();
            System.out.println(cur.e);
            if(cur.left!=null)
                queue.add(cur.left);
            if(cur.right!=null)
                queue.add(cur.right);
        }

    }

    public E minimum(){
        if(size==0)
            throw new IllegalArgumentException("BST is empty");
        return minimun(root).e;

    }
    private Node minimun(Node node){
       if(node.left == null)
           return node;
       return minimun(node.left);
    }

    public E maximum(){
        if(size==0)
            throw new IllegalArgumentException("BST is empty");
        return maximum(root).e;
    }
    private Node maximum(Node node){
        if(node.right == null)
            return node;
        return maximum(node.right);
    }

    //删除最小元素
    public E removeMin(){
        E min = minimum();
        root = removeMin(root);
        return min;
    }
    private Node removeMin(Node node){
        if(node.left == null){
         Node rightNode = node.right;
         node.right = null;
         size --;
         return rightNode;
        }
        node.left = removeMin(node.left);
        return node;
    }

    //删除最大元素
    public E removeMax(){
        E max = maximum();
        root = removeMax(root);
        return max;
    }
    private Node removeMax(Node node){
        if(node.right == null){
            Node leftNode = node.left;
            node.left = null;
            size --;
            return leftNode;
        }
        node.right = removeMax(node.right);
        return node;
    }

    //移除一个已知的元素
    public void remove(E e){
        root = remove(root,e);
    }
    private Node remove(Node node,E e){
        if(node == null)
            return null;
        if(e.compareTo(node.e)<0){
            node.left = remove(node.left,e);
            return node;
        }
        else if(e.compareTo(node.e)>0){
            node.right = remove(node.right,e);
            return node;
        }
//        if(node.left!=null && node.right!=null)
        else //e == node.e
        {
            if(node.left == null){
                Node rightNode = node.right;
                node.right = null;
                size --;
                return rightNode;
            }
            if(node.right == null){
                Node leftNode = node.left;
                node.left = null;
                size --;
                return leftNode;
            }
            Node successor = minimun(node.right);
            successor.right = removeMin(node.right);
            size -=1;
            successor.left = node.left;
            node.right = null;
            node.left = null;
            size +=1;
            return successor;
        }


    }

}
