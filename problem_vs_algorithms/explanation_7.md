## Explanation

Router Trie implementation:
- **class RouteTrieNode**: Represents a single route, has a children dictionary which has the child routes mapped to another
RouteTrieNode, and has a `data` property to store the route's data.
- **class RouteTrie**: Uses RouteTrieNode to create a tree structure. Inserts routes by breaking each route from `/`.
Finds and returns the route's data by traversing the tree.
- **class Router**: Build on top of RouteTrie, sets the router using RouteTrie, and a default error for when a route
data is not found.

## Design

Trie class can be used to insert and find words for autocomplete.

## Big O

Route insert => **O(n)**
Route lookup => **O(log(n))**