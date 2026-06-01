class LinkedList {

    static class Node {
        private int val;
        private Node next;
        Node(int v) {
            this.val = v;
        }
    }

    private Node head;
    private int size;

    public LinkedList() {
        size = 0;
    }

    public int get(int index) {
        if(index > size - 1) {
            return -1;
        }
        int i = 0;
        Node cur = head;
        while(i != index) {
            cur = cur.next;
            i += 1;
        }
        return cur.val;
    }

    public void insertHead(int val) {
        Node newHead = new Node(val);
        newHead.next = head;
        head = newHead;
        size += 1;
    }

    public void insertTail(int val) {
        if(head == null) {
            insertHead(val);
            return;
        }
        Node cur = head;
        while(cur.next != null) {
            cur = cur.next;
        }
        Node newNode = new Node(val);
        cur.next = newNode;
        size += 1;
    }

    public boolean remove(int index) {
        if(index > size - 1) {
            return false;
        }
        if(index == 0) {
            head = head.next;
            size -= 1;
            return true;
        } 
        Node cur = head;
        int i = 0;
        while(i + 1 != index) {
            cur = cur.next;
            i += 1;
        }
        cur.next = cur.next.next;
        size -= 1;
        return true;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> values = new ArrayList<>();
        Node cur = head;
        while(cur != null) {
            values.add(cur.val);
            cur = cur.next;
        }
        return values;
    }
}
