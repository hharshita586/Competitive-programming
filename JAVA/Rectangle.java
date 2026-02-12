class Rectangle {
    int length, breadth;
    void read(int l, int b) {
        length = l;
        breadth = b;
    }
    void display() {
        System.out.println("Length: " + length);
        System.out.println("Breadth: " + breadth);
        System.out.println("Area: " + (length * breadth));
    }
}
class Rectangle {
    public static void main(String[] args) {
        Rectangle r = new Rectangle();
        r.read(10, 5);
        r.display();
    }
}
