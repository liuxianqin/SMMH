import java.util.*;
import java.util.LinkedList;

public class Main {

    public static void main(String[] args) {
	// write your code here

        BST<Integer> bst = new BST<>();
        Random random = new Random();
        int n = 1000;

        for(int i=1;i<n;i++)
            bst.add(random.nextInt(10000));
        ArrayList<Integer> nums = new ArrayList<>();

        System.out.println(bst.getSize());

        while(!bst.isEmpty())
            nums.add(bst.removeMin());

        System.out.println(nums);

        for(int i = 1;i<nums.size();i++)
            if(nums.get(i-1)> nums.get(i))
                throw new IllegalArgumentException("ERROR");


        System.out.println(bst.getSize());
//        bst.preTraverse();
//
////        System.out.println(bst.contains(6));
//        bst.inOrder();
//        System.out.println();
//        bst.postOrder();
//        bst.PreOrder_notre();
//        bst.levelOrder();
//        System.out.println(bst.maximum());
//        System.out.println(bst.minimum());

    }



}
