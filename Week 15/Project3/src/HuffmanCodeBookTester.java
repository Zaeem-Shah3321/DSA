import provided.BinarySequence;
import student.HuffmanCodeBook;

public class HuffmanCodeBookTester {
    public static void main(String[] args) {
        testAll();

        // comment above and uncomment below to run each of the autograder's tests individually.
        //containsTest();
        //containsAllTest();
        //getTestOne();
        //getTestTwo();
        //testEncode();
    }

    /**
     * Runs all tests in one big series, this isn't how the
     * autograder runs tests, but it's easier for humans to use
     * ALSO IMPORTANT: this version has comments explaining the
     * tests design.
     */
    public static void testAll() {
        // make an empty huffman codebook. nothing should
        // be in it.
        HuffmanCodeBook book = new HuffmanCodeBook();

        // contains should be false for any letter at
        // this point
        System.out.println(book.contains('a'));            // false
        System.out.println(book.contains('B'));            // false
        System.out.println(book.contains(' '));            // false
        // we're testing this char '\0' on purpose. This
        // is the default char value -- so if you're
        // using an array, or unininitalized instance
        // variables it would be easy to accidentally
        // treat this letter as included if you're not
        // keeping track of what parts of the data are
        // "in-use"
        System.out.println(book.contains('\0'));           // false

        // OK. Let's add some things and check if the
        // contains method now shows "contains"
        book.addSequence('a', new BinarySequence("0000"));
        book.addSequence(' ', new BinarySequence("0001"));
        System.out.println(book.contains('a'));            // true
        System.out.println(book.contains('B'));            // false
        System.out.println(book.contains(' '));            // true
        System.out.println(book.contains('\0'));           // false


        // Your data structures should work for ANY char
        book.addSequence('\0', new BinarySequence("0010"));
        book.addSequence('!', new BinarySequence("0011"));
        book.addSequence('œ', new BinarySequence("0100"));
        System.out.println(book.contains('a'));            // true
        System.out.println(book.contains('B'));            // false
        System.out.println(book.contains(' '));            // true
        System.out.println(book.contains('\0'));           // true

        // check if get returns the correct values now.
        // some of these should be null -- the return
        // value for "never added"
        BinarySequence bs;
        bs = book.getSequence('a');
        System.out.println(bs);                            // 0000
        bs = book.getSequence('b');
        System.out.println(bs);                            // null
        bs = book.getSequence('A');
        System.out.println(bs);                            // null
        bs = book.getSequence('B');
        System.out.println(bs);                            // null
        bs = book.getSequence(' ');
        System.out.println(bs);                            // 0001
        bs = book.getSequence('!');
        System.out.println(bs);                            // 0011
        bs = book.getSequence('œ');
        System.out.println(bs);                            // 0100

        book.addSequence('A', new BinarySequence("0101"));
        bs = book.getSequence('a');
        System.out.println(bs);                            // 0000
        bs = book.getSequence('b');
        System.out.println(bs);                            // null
        bs = book.getSequence('A');
        System.out.println(bs);                            // 0101

        System.out.println(book.containsAll("apple"));     // false
        System.out.println(book.containsAll(""));          // true
        System.out.println(book.containsAll("  a!"));      // true
        book.addSequence('e', new BinarySequence("0110"));
        book.addSequence('l', new BinarySequence("0111"));
        book.addSequence('p', new BinarySequence("1000"));

        System.out.println(book.containsAll("apple"));     // true
        System.out.println(book.containsAll(""));          // true
        System.out.println(book.containsAll("  a!"));      // true

        // test encode for a specific codebook.
        bs = book.encode("");
        System.out.println("size: "+bs.size());            // size: 0
        bs = book.encode("  a!");
        System.out.println(bs);                            // 0001000100000011
        // key for the last one (split up by letter) // 0001  0001  0000  0011
        book.addSequence('?', new BinarySequence("11"));
        // Kluver's favorite simple letter
        // the interrobang
        book.addSequence('‽', new BinarySequence("101"));
        bs = book.encode("A!p?p!le‽");
        System.out.println(bs);                            // 010100111000111000001101110110101
        // key for the last one (split up by letter)  0101  0011  1000  11  1000  0011  0111  0110  101
    }
/* expected output
false
false
false
false
true
false
true
false
true
false
true
true
0000
null
null
null
0001
0011
0100
0000
null
0101
false
true
true
true
true
true
size: 0
0001000100000011
010100111000111000001101110110101
 */


    public static void containsTest() {
        HuffmanCodeBook book = new HuffmanCodeBook();
        System.out.println(book.contains('a'));            // false
        System.out.println(book.contains('B'));            // false
        System.out.println(book.contains(' '));            // false
        System.out.println(book.contains('\0'));           // false
        book.addSequence('a', new BinarySequence("0000"));
        book.addSequence(' ', new BinarySequence("0001"));
        System.out.println(book.contains('a'));            // true
        System.out.println(book.contains('B'));            // false
        System.out.println(book.contains(' '));            // true
        System.out.println(book.contains('\0'));           // false
        book.addSequence('\0', new BinarySequence("0010"));
        book.addSequence('!', new BinarySequence("0011"));
        book.addSequence('œ', new BinarySequence("0100"));
        System.out.println(book.contains('a'));            // true
        System.out.println(book.contains('B'));            // false
        System.out.println(book.contains(' '));            // true
        System.out.println(book.contains('\0'));           // true
    }
/* expected output
false
false
false
false
true
false
true
false
true
false
true
true
 */

    public static void containsAllTest() {
        HuffmanCodeBook book = new HuffmanCodeBook();
        book.addSequence('a', new BinarySequence("0000"));
        book.addSequence(' ', new BinarySequence("0001"));
        book.addSequence('!', new BinarySequence("0011"));
        System.out.println(book.containsAll("apple"));     // false
        System.out.println(book.containsAll(""));          // true
        System.out.println(book.containsAll("  a!"));      // true
        book.addSequence('e', new BinarySequence("0110"));
        book.addSequence('l', new BinarySequence("0111"));
        book.addSequence('p', new BinarySequence("1000"));
        System.out.println(book.containsAll("apple"));     // true
        System.out.println(book.containsAll(""));          // true
        System.out.println(book.containsAll("  a!"));      // true
    }
/* expected output
false
true
true
true
true
true
 */

    public static void getTestOne() {
        HuffmanCodeBook book = new HuffmanCodeBook();
        book.addSequence('a', new BinarySequence("0000"));
        book.addSequence(' ', new BinarySequence("0001"));
        book.addSequence('\0', new BinarySequence("0010"));
        book.addSequence('!', new BinarySequence("0011"));
        book.addSequence('œ', new BinarySequence("0100"));
        BinarySequence bs;
        bs = book.getSequence('a');
        System.out.println(bs);                            // 0000
        bs = book.getSequence(' ');
        System.out.println(bs);                            // 0001
        bs = book.getSequence('!');
        System.out.println(bs);                            // 0011
        bs = book.getSequence('œ');
        System.out.println(bs);                            // 0100
    }
/* expected output:
0000
0001
0011
0100
 */

    public static void getTestTwo() {
        // test two is a continuation / extention of test one
        // it checks mainly for null, but also makes sure values don't change on add.
        HuffmanCodeBook book = new HuffmanCodeBook();
        book.addSequence('a', new BinarySequence("0000"));
        book.addSequence(' ', new BinarySequence("0001"));
        book.addSequence('\0', new BinarySequence("0010"));
        book.addSequence('!', new BinarySequence("0011"));
        book.addSequence('œ', new BinarySequence("0100"));
        BinarySequence bs;
        bs = book.getSequence('a');
        System.out.println(bs);                            // 0000
        bs = book.getSequence('b');
        System.out.println(bs);                            // null
        bs = book.getSequence('A');
        System.out.println(bs);                            // null
        bs = book.getSequence('B');
        System.out.println(bs);                            // null
        bs = book.getSequence(' ');
        System.out.println(bs);                            // 0001
        bs = book.getSequence('!');
        System.out.println(bs);                            // 0011
        bs = book.getSequence('œ');
        System.out.println(bs);                            // 0100

        book.addSequence('A', new BinarySequence("0101"));
        bs = book.getSequence('a');
        System.out.println(bs);                            // 0000
        bs = book.getSequence('b');
        System.out.println(bs);                            // null
        bs = book.getSequence('A');
        System.out.println(bs);                            // 0101
    }
/* expected output
0000
null
null
null
0001
0011
0100
0000
null
0101
 */

    public static void testEncode() {
        HuffmanCodeBook book = new HuffmanCodeBook();
        book.addSequence('a', new BinarySequence("0000"));
        book.addSequence(' ', new BinarySequence("0001"));
        book.addSequence('\0', new BinarySequence("0010"));
        book.addSequence('!', new BinarySequence("0011"));
        book.addSequence('œ', new BinarySequence("0100"));
        BinarySequence bs;
        book.addSequence('A', new BinarySequence("0101"));
        book.addSequence('e', new BinarySequence("0110"));
        book.addSequence('l', new BinarySequence("0111"));
        book.addSequence('p', new BinarySequence("1000"));
        bs = book.encode("");
        System.out.println("size: "+bs.size());            // size: 0
        bs = book.encode("  a!");
        System.out.println(bs);                            // 0001000100000011
        // key for the last one (split up by letter) // 0001  0001  0000  0011
        book.addSequence('?', new BinarySequence("11"));
        // Kluver's favorite simple letter:
        // the interrobang (a mix of ! and ?)
        book.addSequence('‽', new BinarySequence("101"));
        bs = book.encode("A!p?p!le‽");
        System.out.println(bs);                            // 010100111000111000001101110110101
        // key for the last one (split up by letter)  0101  0011  1000  11  1000  0011  0111  0110  101
    }
/* expected output
size: 0
0001000100000011
010100111000111000001101110110101
 */
}


