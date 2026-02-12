public class SecondLargest {
    public static void main(String[] args) {
        int[] a = {40, 10, 30, 70, 100, 90, 80};
        int max = a[0], temp = 0;
        for (int i = 1; i < a.length; i++) {
            if (a[i] > max) { 
                temp = max; max = a[i]; }
            else if (a[i] > temp && a[i] != max) temp = a[i];
        }
        System.out.println("Second Largest = " + temp);
    }
}
