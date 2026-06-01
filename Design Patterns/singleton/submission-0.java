static class Singleton {

    private static Singleton INSTANCE = new Singleton();
    private String value;

    private Singleton() {

    }

    public static Singleton getInstance() {
        return INSTANCE;
    }

    public String getValue() {
        return INSTANCE.value;
    }

    public void setValue(String value) {
        INSTANCE.value = value;
    }
    
}
