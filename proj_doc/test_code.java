public class Main {
    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 20;
        int result = sum(num1, num2);
    }

   // Returns the sum of two integers.
 public static int sum(int a , int b){
        int sum = a + b;
        return sum;
    }
// Multiply two integers.

// Multiply two integers.
public static int mul(int a , int b){
        int sum = a * b;
        return sum;
    }
}
public class StringUtils {

    // Reverses the given string
    
   
public static String reverse(String input) {
        if (input == null || input.isEmpty()) return input;
        return new StringBuilder(input).reverse().toString();
    }

    // Capitalizes the first letter of each word in a sentence
    
    // Capitalize words.
/** 
Capitalize words.

@param sentence the sentence
@return the capitalized sentence or {@code null} if sentence is empty.
@since 1.0.0
@see #capitalizeWords(String)
@see*/
public static String capitalizeWords(String sentence) {
        if (sentence == null || sentence.isEmpty()) return sentence;
        String[] words = sentence.split(regex:'');
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            if (word.length() > 0) {
                result.append(Character.toUpperCase(word.charAt(0)))
                      .append(word.substring(1).toLowerCase())
                      .append(str:'');
            }
        }

        return result.toString().trim();
    }
    public static String cleanAndLower(String input) { 
        return input.trim().toLowerCase().replaceAll('[^a-z0-9 ]', ''); 
    }

    public static void main(String[] args) {
        String original = "hello world from java";
        String reversed = reverse(original);
        String capitalized = capitalizeWords(original);

        System.out.println("Original: " + original);
        System.out.println("Reversed: " + reversed);
        System.out.println("Capitalized: " + capitalized);
    }
}
