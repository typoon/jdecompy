public class Example {
    private int n1;
    private int n2;

    public Example(int n1, int n2) {
        this.n1 = n1;
        this.n2 = n2;
    }

    public int getSum() {
        return this.n1 + this.n2;
    }

    public static void main(String [] args) {
        Example ex = new Example(10,20);
        int sum;

        sum = ex.getSum();
        System.out.println("Sum = " + sum);
    }
}
