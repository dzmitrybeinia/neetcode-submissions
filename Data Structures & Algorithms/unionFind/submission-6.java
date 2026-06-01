class UnionFind {

    private int[] parents;
    private int[] ranks;
    private int components;

    public UnionFind(int n) {
        parents = new int[n];
        ranks = new int[n];
        for(int i = 0; i < n; i++) {
            parents[i] = i;
            ranks[i] = 1;
        }
        components = n;
    }

    public int find(int x) {
        int cur = x;
        while(cur != parents[cur]) {
            cur = parents[cur];
        }
        return parents[cur];
    }

    public boolean isSameComponent(int x, int y) {
        return find(x) == find(y);
    }

    public boolean union(int x, int y) {
        int xParent = find(x);
        int yParent = find(y);
        if(xParent == yParent) {
            return false;
        }
        if(ranks[xParent] > ranks[yParent]) {
            parents[yParent] = xParent;
            ranks[xParent] += 1;
        } else {
            parents[xParent] = yParent;
            ranks[yParent] += 1;
        }
        components -= 1;
        return true;
    }

    public int getNumComponents() {
        return this.components;
    }
}
