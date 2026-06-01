class Solution {
    private List<Integer> res = new ArrayList<>();
    public List<Integer> topologicalSort(int n, int[][] edges) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for(int[] edge : edges) {
            graph.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(edge[0]);
        }
        int[] visited = new int[n];
        for(int i = 0; i < n; i++) {
            if(visited[i] == 0) {
                if(dfs(i, graph, visited)) {
                    return List.of();
                }
            }
        }
        return res;
    }

    private boolean dfs(int node, Map<Integer, List<Integer>> graph, int[] visited) {
        visited[node] = 1;
        for(int nei : graph.getOrDefault(node, List.of())) {
            if(visited[nei] == 1) {
                return true;
            }
            if(visited[nei] == 0 && dfs(nei, graph, visited)) {
                return true;
            }
        }
        visited[node] = 2;
        res.add(node);
        return false;
    }
}
