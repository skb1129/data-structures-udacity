# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, data=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(data)

    def insert(self, routes, data):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        head = self.root
        for route in routes:
            head = head.insert(route)
        head.data = data

    def find(self, routes):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        head = self.root
        for route in routes:
            head = head.children.get(route)
            if not head:
                return None
        return head
        pass


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, data=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.data = data

    def insert(self, route):
        # Insert the node as before
        if not self.children.get(route):
            self.children[route] = RouteTrieNode()
        return self.children.get(route)


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, data, error=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(data)
        self.error = error

    def add_handler(self, string, data):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        routes = self.split_path(string)
        self.router.insert(routes, data)

    def lookup(self, string):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        routes = self.split_path(string)
        node = self.router.find(routes)
        if (not node) or (not node.data):
            return self.error
        return node.data

    @staticmethod
    def split_path(route):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return list(filter(None, route.split('/')))


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
