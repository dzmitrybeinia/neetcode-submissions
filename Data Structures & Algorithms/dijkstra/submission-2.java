class Solution {
    class Node {
        int to;
        int weight;
        Node(int t, int w) {
            this.to = t;
            this.weight = w;
        }
    }
    public Map<Integer, Integer> shortestPath(int n, List<List<Integer>> edges, int src) {
        Map<Integer, List<Node>> graph = new HashMap<>();
        for(var edge : edges) {
            graph.computeIfAbsent(edge.get(0), k -> new ArrayList<>()).add(new Node(edge.get(1), edge.get(2)));
        }
        Map<Integer, Integer> visited = new HashMap<>();
        Queue<Node> minHeap = new PriorityQueue<>((a, b) -> a.weight - b.weight);
        minHeap.add(new Node(src, 0));
        while(!minHeap.isEmpty()) {
            Node node = minHeap.poll();
            int to = node.to;
            int weight = node.weight;
            if(visited.containsKey(to)) {
                continue;
            }
            visited.put(to, weight);
            for(Node nei : graph.getOrDefault(to, List.of())) {
                if(!visited.containsKey(nei)) {
                    minHeap.add(new Node(nei.to, nei.weight + weight));
                }
            }
        }
        for(int i = 0; i < n; i++) {
            if(!visited.containsKey(i)) {
                visited.put(i, -1);
            }
        }
        return visited;
    }  
}


