import provided.BinarySequence;
import student.HuffmanCodeBook;
import student.HuffmanCodeTree;

public class DecodeEncodeTester {
    public static void main(String[] args) {
        HuffmanCodeBook book = ProvidedHuffmanCodeBook.getEbookHuffmanCodebook();
        HuffmanCodeTree tree = new HuffmanCodeTree(book);

        /////////////////////////////////////////////////
        // TEST 1: Simple DecodeEncode (2 points)
        /////////////////////////////////////////////////
        String original = "Once upon a midnight dreary, while I pondered, weak and weary,\n" +
                "Over many a quaint and curious volume of forgotten lore—\n" +
                "    While I nodded, nearly napping, suddenly there came a tapping,\n" +
                "As of some one gently rapping, rapping at my chamber door.\n" +
                "\"'Tis some visitor,\" I muttered, \"tapping at my chamber door—\n" +
                "            Only this and nothing more.\"";
        BinarySequence encoded = book.encode(original);
        System.out.println(encoded);
        String decoded = tree.decode(encoded);
        System.out.println(original.equals(decoded));
        System.out.println(decoded);

        /////////////////////////////////////////////////
        // Test 2: DecodeEncode real file (2 points)
        // this will assume that you've got the right test files in the right folder.
        // see the FileIOAssistance to get that setup. If you can't get it setup don't sweat it too much
        // the autograder will be setup right, and if you past test 1 you probably pass test 2.
        /////////////////////////////////////////////////
        String bookFileID = "16-0";
        String bookFile = bookFileID + ".txt";
        // read the book
        String bookText = FileIOAssistance.readFile(bookFile);
        // encode it
        BinarySequence studentEncode = book.encode(bookText);

        // check that it's good.
        BinarySequence expectedEncode = BinarySequence.readFromFile(bookFile + ".enc");
        System.out.println(expectedEncode.equals(studentEncode));

        // store it to a file.
        studentEncode.writeToFile(bookFile + ".student.enc");

        // read it back and decode it!
        studentEncode = BinarySequence.readFromFile(bookFile + ".student.enc");
        System.out.println(expectedEncode.equals(studentEncode));
        decoded = tree.decode(studentEncode);
        FileIOAssistance.writeFile(bookFileID + ".student.txt", decoded);
        System.out.println("Go check " + bookFileID + ".student.txt it should be peter pan.");

        /////////////////////////////////////////////////
        // Test 3 (not in autograder -- this one's just for you)
        // This should run pretty quickly -- a second or two depending on computer.
        // decode the other test files.
        /////////////////////////////////////////////////
        String[] files = {
                "23-0.txt",
                "36-0.txt",
                "43-0.txt",
                "84-0.txt",
                "345-0.txt",
                "829-0.txt",
                "1661-0.txt",
                "4300-0.txt",
                "6130-0.txt",
                "pg46.txt",
                "pg996.txt",
                "pg64317.txt"};
        for(String file : files) {
            BinarySequence code = BinarySequence.readFromFile(file+".enc");
            String text = tree.decode(code);
            FileIOAssistance.writeFile(file, text);
        }
        // for extra fun -- go check out the file size of the encoded and not encoded files!








    }
}
/*
1001111001010111100000011011111011111110111010111010001101110010010101100101001010011001001010110101101111000010001111001101001100111010111001000010100100001101001111111011111110111010110110000111100001011001100111010111000010001111110111010000101101101101011100001000111100110100110011110101001111001011011000011110110111001100001010110101101000110011000000011111010000010010110101101000010110110110111000111110111100010011111111000111100110110011110010111110111001000110011110111111010111101111111010011001111010101000001011101001001111111000010011110110111010110110110110111011001001000010100100001101001111111001010111101101011000010110011001110010100010001111010010011010110010110001111111111111100100101100110011001110001111111010110101100000101100100110101101010010000011110000110111000100011100100011010001101010100011111111111111001001011001100110011110100110111100011110011110111111000110111111001000110011101010001101001100000101101010010011010110111101000111111111111110010010110011001100111011110100011111111111111001001011001101101000101011011100101101011011100001001000111001111011100011110110101100111011111110100111011101010011110101100111101000111111001001000111100011011111100100011001101100010001100101010011111110011001100111101011101001111111011100111111010101010000111100001011001100111010011110101101010001111111111111100100101100110110100010101101110010110101101110000100100011100111101110001111011010110011101111111010011110110111010110110110110110110110110110110110110100111100101011001001101011010100100001000111101000010110110110010101111010010000100101100110110111001011111110000100111010011110101
true
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore—
    While I nodded, nearly napping, suddenly there came a tapping,
As of some one gently rapping, rapping at my chamber door.
"'Tis some visitor," I muttered, "tapping at my chamber door—
            Only this and nothing more."
true
true
Go check 16-0.student.txt it should be peter pan.
 */
