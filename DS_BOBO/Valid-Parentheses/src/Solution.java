//import java.util.Stack;


public class Solution {

    public boolean isValid(String s){
        ArrayStack<Character> stack = new ArrayStack<>();
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            if(c ==  '(' || c == '[' || c == '{')
                stack.push(c);
            else{
                if(stack.isEmpty())
                    return false;
                char topChar = stack.pop();
                if(c == ')' && topChar!='(')
                    return false;
                if(c == ']' && topChar!='[')
                    return false;
                if(c == '}' && topChar!='{')
                    return false;
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args){
       boolean a= (new Solution()).isValid("(){}{}[]");
       System.out.println(a);
    }
}

/*    util
执行结果：通过
显示详情
执行用时 :2 ms, 在所有 java 提交中击败了96.81%的用户
内存消耗 :34.1 MB, 在所有 java 提交中击败了87.62%的用户

 */

/*  自有类
执行用时 :3 ms, 在所有 java 提交中击败了87.72%的用户内存消耗 :34.3 MB, 在所有 java 提交中击败了85.22%的用户
 */