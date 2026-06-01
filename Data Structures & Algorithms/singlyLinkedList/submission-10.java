class LinkedList {

    static class Node {
        int val;
        Node next;

        Node(int val) {
            this.val = val;
        }
    }

    private Node head = new Node(-1);
    private Node tail;


    public LinkedList() {
        tail = head;
    }

    public int get(int index) {
        int i = 0;
        Node cur = head.next;
        while (cur != null) {
            if(i == index) {
                return cur.val;
            }
            cur = cur.next;
            i += 1;
        }
        return -1;
    }

    public void insertHead(int val) {
        Node headNext = head.next;
        Node newNode = new Node(val);
        newNode.next = headNext;
        head.next = newNode;
        if(newNode.next == null) {
            tail = newNode;
        }
    }

    public void insertTail(int val) {
        Node newNode = new Node(val);
        tail.next = newNode;
        tail = newNode;
    }

    public boolean remove(int index) {
        int i = 0;
        Node cur = head;
        while(i < index && cur != null) {
            i += 1;
            cur = cur.next;
        }
        if(cur != null && cur.next != null) {
            if(cur.next == tail) {
                tail = cur;
            }
            cur.next = cur.next.next;
            return true;
        }
        return false;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> values = new ArrayList<>();
        Node cur = head.next;
        while(cur != null) {
            values.add(cur.val);
            cur = cur.next;
        }
        return values;
    }
}