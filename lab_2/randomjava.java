import java.util.Random;

public class RandomBinarySequenceGenerator {
    /**
     * the function generates a pseudo-random sequence
     */
    public static int random() {
        Random random = new Random();
        return random.nextInt(2);
    }
    public static void main(String[] args) {
        int len = 128;
        for(int i = 0; i < len; i++)
            System.out.print(random());

    }
}
 