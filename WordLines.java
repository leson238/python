import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.TreeSet ;
import java.io.File;
import java.io.FileNotFoundException;

/**
 For each word in a given java file, prints all line numbers where the word occurs.
 NOTE: You must use a map!!

 HINT: use a map where the key is the word and the value
 is a string containing all the line numbers. Don't forget to check the map
 before adding a new key word to see if it already in the map.

 Assume the first line in the file is line number 1.
 ----------------------------------------------
 The input file is: Simple.java
 ----------------------------------
 public class Simple
 {
 public static void main(String[] args)
 {
 System.out.println("-------------------------") ;
 System.out.println("Simple Simon met a pieman going to the fair.") ;
 System.out.println("Said Simple Simon to the pieman...") ;
 System.out.println("-------------------------") ;
 }
 }
 ----------------------------------
 Expected output is (without the dashed line):
 ----------------------------------
 Said: 7
 Simon: 6 7
 Simple: 1 6 7
 String: 3
 System: 5 6 7 8
 a: 6
 args: 3
 class: 1
 fair: 6
 going: 6
 main: 3
 met: 6
 out: 5 6 7 8
 pieman: 6 7
 println: 5 6 7 8
 public: 1 3
 static: 3
 the: 6 7
 to: 6 7
 void: 3
 */
public class WordLines
{
    public static void main(String[] args) throws FileNotFoundException
    {
        //-----------Start below here. To do: approximate lines of code = 15
        //
        //NOTE: you do not need to use try...catch.. in this question
        // Create a Map called lines

        // Create a scanner, the input file is "Simple.java"
        Map<String, String> lines = new TreeMap<String, String>();
        Scanner sc = new Scanner(new File("Simple.java"));

        // HINT: while a scanner has another line, read the line and then get all words from each line,
        // create another scanner to scan words from each line
        // set the delimiter for this line scanner to read only alphabetic characters from the line
        // using the Scanner method: useDelimiter("[^A-Za-z_]+");
        // look at the documentation of Map for names of methods if you have forgotten
        int l = 0;
        while (sc.hasNextLine())
        {
            l += 1;
            String line = sc.nextLine();
            Scanner lineScanner = new Scanner(line);
            lineScanner.useDelimiter("[^A-Za-z_]+");
            while (lineScanner.hasNext())
            {
                String word = lineScanner.next();
                if (lines.containsKey(word))
                {
                    String v = lines.get(word);
                    v += (" " + l);
                }
                else
                {
                    lines.put(word, Integer.toString(l));
                }
            }
        }
        //
        //-----------------End here. Please do not remove this comment. Reminder: no changes outside the todo regions.

        // Print all words and currentLines
        TreeSet<String> treeSet = new TreeSet<String>() ;
        treeSet.addAll(lines.keySet()) ;
        for (String key : treeSet) {
            System.out.println(key + ": " + lines.get(key)) ;
        }
    }
}
