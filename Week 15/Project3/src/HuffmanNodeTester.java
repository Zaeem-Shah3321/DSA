import student.HuffmanNode;

public class HuffmanNodeTester {
    public static void main(String[] args) {
        // Test Huffman Node isValid #1 max_score = 2
        HuffmanNode emptyNode = new HuffmanNode('c');
        boolean b = emptyNode.isValidTree();
        System.out.println(b);                           // True
        b = emptyNode.isValidNode();
        System.out.println(b);                           // True

        // This should be null for all 3 data variables by the way
        HuffmanNode otherNode = new HuffmanNode(null, null);
        System.out.println(emptyNode.isValidTree());         // true
        System.out.println(otherNode.isValidTree());         // false
        System.out.println(otherNode.isValidNode());         // false
        otherNode.setOne(emptyNode);
        System.out.println(emptyNode.isValidTree());         // true
        System.out.println(emptyNode.isValidNode());         // true
        System.out.println(otherNode.isValidTree());         // false
        System.out.println(otherNode.isValidNode());         // false
        HuffmanNode emptyNode2 = new HuffmanNode('d');
        otherNode.setZero(emptyNode2);
        System.out.println(emptyNode.isValidTree());         // true
        System.out.println(emptyNode.isValidNode());         // true
        System.out.println(emptyNode2.isValidTree());        // true
        System.out.println(emptyNode2.isValidNode());        // true
        System.out.println(otherNode.isValidTree());         // true
        System.out.println(otherNode.isValidNode());         // true

        // Test Huffman Node isValid #2 max_score = 2
        HuffmanNode n1 = new HuffmanNode('a');
        HuffmanNode n2 = new HuffmanNode('b');
        HuffmanNode n3 = new HuffmanNode('c');
        HuffmanNode n4 = new HuffmanNode('d');
        HuffmanNode temp1 = new HuffmanNode(n1, n2);
        HuffmanNode temp2 = new HuffmanNode(n3, n4);
        HuffmanNode temp = new HuffmanNode(temp1, temp2);
        System.out.println(n1.isValidTree());                // true
        System.out.println(n1.isValidNode());                // true
        System.out.println(n2.isValidTree());                // true
        System.out.println(n2.isValidNode());                // true
        System.out.println(n3.isValidTree());                // true
        System.out.println(n3.isValidNode());                // true
        System.out.println(n4.isValidTree());                // true
        System.out.println(n4.isValidNode());                // true
        System.out.println(temp1.isValidTree());             // true
        System.out.println(temp1.isValidNode());             // true
        System.out.println(temp2.isValidTree());             // true
        System.out.println(temp2.isValidNode());             // true
        System.out.println(temp.isValidTree());              // true
        System.out.println(temp.isValidNode());              // true

        // Test Huffman Node isValid #3 max_score = 2
        n1 = new HuffmanNode('a');
        n2 = new HuffmanNode('b');
        n3 = new HuffmanNode('c');
        temp1 = new HuffmanNode(n1, n2);
        temp2 = new HuffmanNode(n3, null);
        temp = new HuffmanNode(temp1, temp2);
        System.out.println(n1.isValidTree());                // true
        System.out.println(n1.isValidNode());                // true
        System.out.println(n2.isValidTree());                // true
        System.out.println(n2.isValidNode());                // true
        System.out.println(n3.isValidTree());                // true
        System.out.println(n3.isValidNode());                // true
        System.out.println(temp1.isValidTree());             // true
        System.out.println(temp1.isValidNode());             // true
        System.out.println(temp2.isValidTree());             // false
        System.out.println(temp2.isValidNode());             // false
        System.out.println(temp.isValidTree());              // false
        System.out.println(temp.isValidNode());              // true

        // Test Huffman Node isLeaf max_score = 1
        n1 = new HuffmanNode('a');
        n2 = new HuffmanNode('b');
        n3 = new HuffmanNode(n1, n2);
        System.out.println(n1.isLeaf());                 // true
        System.out.println(n2.isLeaf());                 // true
        System.out.println(n3.isLeaf());                 // false

        // Test Huffman Node getters/setters #1 max_score = 0.5
        n1 = new HuffmanNode('a');
        n2 = new HuffmanNode('b');
        n2.setData('c');
        n1.setZero(n2);
        System.out.println(n1.getZero().getData());      // c


        // Test Huffman Node getters/setters #2 max_score = 0.5
        n1 = new HuffmanNode('a');
        n2 = new HuffmanNode('c');
        n1.setData('b');
        n1.setOne(n2);
        System.out.println(n1.getOne().getData());       // c

    }
}

/*
true
true
true
false
false
true
true
false
false
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
true
false
false
false
true
true
true
false
c
c

 */