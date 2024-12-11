import provided.BinarySequence;
import student.HuffmanCodeTree;
import student.HuffmanNode;

/**
 * Due to the task-focused design of the HuffmanCodeTree
 * it's pretty much impossible to test any one function in isolation
 * As such, the tests in this file are not split up method
 * by method. This is common with datastructures, you may
 * only be able to say conclusively "it all passes tests"
 * or "none of it passes any tests".
 */
public class HuffmanCodeTreeTester {

    public static void main(String[] args) {
        /////////////////////////////////////////////////
        // Test 1 (Build Tree Test Valid) (3 points)
        /////////////////////////////////////////////////

        // we'll start with an empty node.
        HuffmanCodeTree tree = new HuffmanCodeTree(new HuffmanNode(null, null));

        // the tree should just be the 1 node, so definitely not valid.
        boolean b = tree.isValid();                      // false
        System.out.println(b);
        // since it's not valid it's not reasonable to decode anything.
        // let's add a few nodes shall we?

        //           *
        tree.put(new BinarySequence("1"), 'o');
        System.out.println(tree.isValid());              // false
        //           *
        //            \
        //            [o]
        tree.put(new BinarySequence("011"), 'g');
        System.out.println(tree.isValid());              // false
        //           *
        //         /  \
        //        *   [o]
        //          \
        //            *
        //             \
        //             [g]
        tree.put(new BinarySequence("0100"), 'y');
        System.out.println(tree.isValid());              // false
        //           *
        //         /  \
        //        *   [o]
        //          \
        //            *
        //           / \
        //          *  [g]
        //        /
        //      [y]
        tree.put(new BinarySequence("0101"), '!');
        System.out.println(tree.isValid());              // false
        //           *
        //         /  \
        //        *   [o]
        //          \
        //            *
        //           / \
        //          *  [g]
        //        /  \
        //      [y]  [!]
        tree.put(new BinarySequence("000"), 'v');
        System.out.println(tree.isValid());              // false
        //           *
        //         /  \
        //        *   [o]
        //      /   \
        //    *      *
        //   /      / \
        // [v]     *  [g]
        //        / \
        //      [y] [!]
        tree.put(new BinarySequence("001"), 'r');
        System.out.println(tree.isValid());              // true

        /////////////////////////////////////////////////
        // Test 2 (Test Build And Decode) (2 points)
        // runs test 1 code before starting
        /////////////////////////////////////////////////
        // test encode (will start from where the past test finished)
        // hey that's a full tre with data only in the leafs!
        // (that's finally valid!)
        BinarySequence encoded = new BinarySequence("01100111000010001010101");
        String decoded = tree.decode(encoded);
        System.out.println(decoded);                     // groovy!!

        /////////////////////////////////////////////////
        // Test 3 (test overbuild) (2 points)
        // runs test 1 code before starting
        /////////////////////////////////////////////////

        // OH NO -- that can't go there! the tree was perfect
        tree.put(new BinarySequence("11"), '"');
        System.out.println(tree.isValid());              // false


        /////////////////////////////////////////////////
        // Test 4 (pre-built tree) (2 points)
        /////////////////////////////////////////////////
        HuffmanNode n1 = new HuffmanNode('a');
        HuffmanNode n2 = new HuffmanNode('b');
        HuffmanNode n3 = new HuffmanNode('c');
        HuffmanNode n4 = new HuffmanNode('d');
        HuffmanNode temp1 = new HuffmanNode(n1, n2);
        HuffmanNode temp2 = new HuffmanNode(n3, n4);
        HuffmanNode temp = new HuffmanNode(temp1, temp2);
        tree = new HuffmanCodeTree(temp);
        System.out.println(tree.isValid());              // true
        encoded = new BinarySequence("11011000");
        System.out.println(tree.decode(encoded));        // dbca

        /////////////////////////////////////////////////
        // Test 5 (Provided CodeBook Tests) (3 points)
        // I have just the one in mind. This should be
        // more than enough of a test just making this work!
        /////////////////////////////////////////////////
        tree = new HuffmanCodeTree(ProvidedHuffmanCodeBook.getEbookHuffmanCodebook());
        System.out.println(tree.isValid());              // true
        // and with a beefy tree, we have a beefy binary sequence to go with it.

        encoded = new BinarySequence("1001111001010111100000011011111011111110111010111010001101110010010101100101001010011001001010110101101111000010001111001101001100111010111001000010100100001101001111111011111110111010110110000111100001011001100111010111000010001111110111010000101101101101011100001000111100110100110011110101001111001011011000011110110111001100001010110101101000110011000000011111010000010010110101101000010110110110111000111110111100010011111111000111100110110011110010111110111001000110011110111111010111101111111010011001111010101000001011101001001111111000010011110110111010110110110110111011001001000010100100001101001111111001010111101101011000010110011001110010100010001111010010011010110010110001111111111111100100101100110011001110001111111010110101100000101100100110101101010010000011110000110111000100011100100011010001101010100011111111111111001001011001100110011110100110111100011110011110111111000110111111001000110011101010001101001100000101101010010011010110111101000111111111111110010010110011001100111011110100011111111111111001001011001101101000101011011100101101011011100001001000111001111011100011110110101100111011111110100111011101010011110101100111101000111111001001000111100011011111100100011001101100010001100101010011111110011001100111101011101001111111011100111111010101010000111100001011001100111010011110101101010001111111111111100100101100110110100010101101110010110101101110000100100011100111101110001111011010110011101111111010011110110111010110110110110110110110110110110110110100111100101011001001101011010100100001000111101000010110110110010101111010010000100101100110110111001011111110000100111010011110101");
        System.out.println(tree.decode(encoded));
        /*
        should output the following, newlines, spaces, quotes and everything.
        Make sure to look for that last quote in particular -- it's easy to have
        issues at the end of this string.
    
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
"'Tis some visitor," I muttered, "tapping at my chamber door—
            Only this and nothing more."
    
         */
    }


}
/*
false
false
false
false
false
false
true
groovy!!
false
true
dbca
true
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
"'Tis some visitor," I muttered, "tapping at my chamber door—
            Only this and nothing more."

 */