public class StringBuilderDemo {
    // This file serves 2 purposes: 1) showing how to use string builder by example
    // 2) pointing out that string builder is essential for speed in this problem.
    // you WILL NOT actually need this code in your project, it's just here to help
    // with some "required" learning.
    public static void main(String[] args) {
        int N = 158291; // character count of the SHORTEST book we need to decode
        // WARNING -- this test takes about 11 seconds on my computer. That's not monsterously slow, but it's slow enough
        // to make you worried it's frozen.
        char c = 'a';

        // get the time.
        long start = System.currentTimeMillis();


        String result1 = "";
        // This loop runs in O(N^2)
        for(int i = 0; i < N; i++) {
            // this operation is O(n) (where n is the number of letters in result1)
            // because strings are immutable -- it has to copy the whole string (O(n))
            // each time we do this.
            result1 += c;
        }

        // midpoint time
        long mid = System.currentTimeMillis();

        c = 'a';
        // step 1: use constructor to get new string builder
        // a string builder is almost a custom-purpose List of chars
        // it provides really efficient tools to manipulate a string.
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < N; i++) {
            // Step 2: use append, or other StringBuilder methods to build a string.
            // this operation is O(1) because a StringBuilder is mutable
            sb.append(c);
        }

        // Step 3, use toString method to get a String at the end.
        String result2 = sb.toString();

        long end = System.currentTimeMillis();

        double stringSeconds = (mid-start)/1000.0;
        System.out.println("Using the String class and + to build the string took: "+stringSeconds+" seconds");
        double builderSeconds = (end-mid)/1000.0;
        System.out.println("Using the StringBuilder to build the string took: "+builderSeconds+" seconds");
        System.out.println("Using the String builder is "+(stringSeconds-builderSeconds)+" faster than the string loop");


    }
}
