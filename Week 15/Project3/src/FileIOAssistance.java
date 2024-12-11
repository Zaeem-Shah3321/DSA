import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintStream;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

/**
 * @Author Daniel Kluver
 * This class helps read and write files as Strings.
 */
public class FileIOAssistance {
    /**
     * Read a text formatted file into a string.
     * @param filePath -- the filePath can just be the name of a text file, or it can be the full path of the text file.
     * @return the text of the file as a string.
     */
    public static String readFile(String filePath) {
        Path path = Paths.get(filePath);
        if (!path.toFile().exists()) {
            System.err.println("!!! The file you've asked me to read doesn't even exist!");
            System.err.println("You asked for the file: "+path.toAbsolutePath());
            throw new RuntimeException("The file you asked for doesn't exist!");
        }
        try {
            Scanner s = new Scanner(path);
            StringBuilder out = new StringBuilder();
            while (s.hasNextLine()) {
                out.append(s.nextLine());
                out.append("\n");
            }
            s.close();
            return out.toString();
        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    /**
     * create a text formatted file from a string.
     * @param filePath the filePath can just be the name of a text file, or it can be the full path of the text file.
     * @param contents
     * @return the text of the file as a string.
     */
    public static void writeFile(String filePath, String contents) {
        Path path = Paths.get(filePath);
        try {
            PrintStream fileOut = new PrintStream(path.toFile());
            fileOut.print(contents);
            fileOut.close();
        } catch (IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        // running this should create a file "TEST_FOR_LOCATION.txt" that you can use to figure out where
        // java is looking for files in your current programming environment.
        FileIOAssistance.writeFile("TEST_FOR_LOCATION.txt", "Groovy Groovy Groovy.");
        // In IntelliJ it tends to make the file outside of your src folder in my experience
        // IntelliJ doesn't always immediately notice this file BTW.

        // As a "part 2" -- read the file and print it's content. should be "groovy groovy groovy".
        System.out.println(FileIOAssistance.readFile("TEST_FOR_LOCATION.txt"));
    }
}
