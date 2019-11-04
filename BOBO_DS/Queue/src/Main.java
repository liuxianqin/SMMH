import java.net.Inet4Address;
import java.util.Random;

public class Main {

    private static double testQueue(Queue<Integer> q,int opCount){

        long startTime = System.nanoTime();

        Random random = new Random();
        for(int i=0;i<opCount;i++)
            q.enqueue(random.nextInt(Integer.MAX_VALUE));
        for(int i=0;i<opCount;i++)
            q.dequeue();

        long endTime = System.nanoTime();

        return (endTime-startTime)/1000000000.0;
    }

    public static void main(String[] args) {
	// write your code here
        int opCount = 100000;

        ArrayQueue<Integer>  arrayqueue = new ArrayQueue<>();
        double time1 = testQueue(arrayqueue,opCount);
        System.out.println(time1);

        LoopQueue<Integer> loopqueue = new LoopQueue<>();
        double time2 = testQueue(loopqueue,opCount);
        System.out.println(time2);
    }
}


//100万 300s和0.04s