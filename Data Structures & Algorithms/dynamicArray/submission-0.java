class DynamicArray {

    int[] arr;
    int size = 0;
    int capacity = 0;

    public DynamicArray(int capacity) {
        arr = new int[capacity];
        this.capacity = capacity;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if(size >= capacity) {
            resize();
        }
        arr[size] = n;
        size += 1;
    }

    public int popback() {
        int toDelete = arr[size - 1];
        System.arraycopy(arr, 0, arr, 0, arr.length - 1);
        size -= 1;
        return toDelete;
    }

    private void resize() {
        int newCapacity = capacity * 2;
        int[] newArr = new int[newCapacity];
        System.arraycopy(arr, 0, newArr, 0, arr.length);
        arr = newArr;
        capacity = newCapacity;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
