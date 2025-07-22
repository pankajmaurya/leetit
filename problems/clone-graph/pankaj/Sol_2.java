/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }
        
        Map<Integer, Node> cloneMap = new HashMap<>();
        cloneGraphByDfsHelper(node, new HashMap<>(), cloneMap);

        return cloneMap.get(node.val);
        // return cloneGraphHelper(node).get(node.val);
    }

    // TODO: Change to a DFS implementation now.
    private void cloneGraphByDfsHelper(Node node, Map<Integer, Boolean> visitedMap, Map<Integer, Node> cloneMap) {
        // mark as discovered.
        visitedMap.put(node.val, true);

        Node clonedCur = cloneMap.get(node.val);            
        if (clonedCur == null) {
            clonedCur = new Node(node.val);
            cloneMap.put(node.val, clonedCur);
        }
        
        for (Node neighbor : node.neighbors) {

            // create new neighbor if needed.
            Node newNeighbor = cloneMap.get(neighbor.val);
            if (newNeighbor == null) {
                newNeighbor = new Node(neighbor.val);
                cloneMap.put(neighbor.val, newNeighbor);
            }

            if (!clonedCur.neighbors.contains(cloneMap.get(neighbor.val))) {
                clonedCur.neighbors.add(cloneMap.get(neighbor.val));
            }


            if (!visitedMap.containsKey(neighbor.val)) {
                cloneGraphByDfsHelper(neighbor, visitedMap, cloneMap);
            }
        }
    }


    private Map<Integer, Node> cloneGraphHelper(Node node) {
        Map<Integer, Node> nodeMap = new HashMap<>();
        Map<Integer, Boolean> statusMap = new HashMap<>();

        if (node == null) {
            return nodeMap;
        }
        Queue<Node> q = new ArrayDeque<>();

        q.add(node);

        while (!q.isEmpty()) {
            Node cur = q.poll();
            Node clonedCur = nodeMap.get(cur.val);
            
            if (clonedCur == null) {
                clonedCur = new Node(cur.val);
                nodeMap.put(cur.val, clonedCur);
            }
            
            for (Node neighbor : cur.neighbors) {

                // create new neighbor if needed.
                Node newNeighbor = nodeMap.get(neighbor.val);
                if (newNeighbor == null) {
                    newNeighbor = new Node(neighbor.val);
                    nodeMap.put(neighbor.val, newNeighbor);
                }

                if (!clonedCur.neighbors.contains(nodeMap.get(neighbor.val))) {
                    clonedCur.neighbors.add(nodeMap.get(neighbor.val));
                }

                // it may do duplicate work
                if (!statusMap.containsKey(neighbor.val)) {
                    q.offer(neighbor);
                }

                statusMap.put(cur.val, true);
            }
        }
        return nodeMap;
    }
}
