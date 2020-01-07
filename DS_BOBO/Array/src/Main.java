public class Main {

    public static void main(String[] args) {
	// write your code here
//        int[] arr = new int[10];
//        for (int i = 0; i < arr.length ; i ++) {
//            arr[i] = i;
//        }
//        int[] scores = new int[]{100,99,66};
//
//        for(int i = 0; i < scores.length; i ++)
//            System.out.println(scores[i]);
//
//        for(int score:scores)
//            System.out.println(score);

        ///usr/local/jdk1.8.0_221/bin/java
        // -javaagent:/home/user/sofrwares/idea-IC-192.6817.14/lib/idea_rt.jar=44085:/home/user/sofrwares/idea-IC-192.6817.14/bin -Dfile.encoding=UTF-8
        // -classpath
        // /usr/local/jdk1.8.0_221/jre/lib/charsets.jar:/usr/local/jdk1.8.0_221/jre/lib/deploy.jar:/usr/local/jdk1.8.0_221/jre/lib/ext/cldrdata.jar:/usr/local/jdk1.8.0_221/jre/lib/ext/dnsns.jar:/usr/local/jdk1.8.0_221/jre/lib/ext/jaccess.jar:/usr/local/jdk1.8.0_221/jre/lib/ext/jfxrt.jar:/usr/local/jdk1.8.0_221/jre/lib/ext/localedata.jar:/usr/local/jdk1.8.0_221/jre/lib/ext/nashorn.jar:/usr/local/jdk1.8.0_221/jre/lib/ext/sunec.jar:/usr/local/jdk1.8.0_221/jre/lib/ext/sunjce_provider.jar:/usr/local/jdk1.8.0_221/jre/lib/ext/sunpkcs11.jar:/usr/local/jdk1.8.0_221/jre/lib/ext/zipfs.jar:/usr/local/jdk1.8.0_221/jre/lib/javaws.jar:/usr/local/jdk1.8.0_221/jre/lib/jce.jar:/usr/local/jdk1.8.0_221/jre/lib/jfr.jar:/usr/local/jdk1.8.0_221/jre/lib/jfxswt.jar:/usr/local/jdk1.8.0_221/jre/lib/jsse.jar:/usr/local/jdk1.8.0_221/jre/lib/management-agent.jar:/usr/local/jdk1.8.0_221/jre/lib/plugin.jar:/usr/local/jdk1.8.0_221/jre/lib/resources.jar:/usr/local/jdk1.8.0_221/jre/lib/rt.jar:/home/user/IdeaProjects/Array/out/production/Array Main

        Array<Integer> arr = new Array<>();
        for(int i=0;i<10;i++)
            arr.addLast(i);
        System.out.println(arr);

        arr.add(1,100);

        arr.addFirst(-1);

        System.out.println(arr);

        arr.remove(3);
        arr.remove(1);
        arr.remove(5);
        System.out.println(arr);
    }
}
