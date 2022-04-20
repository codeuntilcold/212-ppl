public class Hello {

    public int radius;

    Hello() {
        this.radius = 5;
    }

    public int circumference() {
        final double PI = 3.14;
        return this.radius * 2 * PI;
    }


    public static void main(String args[]) {
        System.out.println("Calculate circumference");
        System.out.println(circumference());
    }
}