public class Model {
    public static void main(String [] args) {
        int r;
        Model m = new Model();

        r = m.sum(1,2);
        
        System.out.println("Result = " + r);
    }

    public int sum(int a, int b) {
        return a + b;
    }
}
