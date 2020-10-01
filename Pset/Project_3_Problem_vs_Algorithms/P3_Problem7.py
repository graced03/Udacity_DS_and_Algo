# A RouteTrie will store our routes and their associated handlers
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, path):
        # Insert the node as before
        if path not in self.children:
            self.children[path] = RouteTrieNode()

class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = root_handler

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root

        for current_path in paths:
            node.insert(current_path)
            node = node.children[current_path]

        node.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        node = self.root

        for current_path in paths:
            if current_path not in node.children:
                return None
            node = node.children[current_path]

        return node.handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, non_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler=root_handler)
        self.non_found_handler = non_found_handler

    def add_handler(self, ori_path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        paths = self.split_path(ori_path)
        self.router.insert(paths=paths, handler=handler)

    def lookup(self, ori_path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        paths = self.split_path(ori_path)

        if len(paths) == 0:
            return self.router.handler

        finding = self.router.find(paths=paths)

        if finding is None:
            return self.non_found_handler
        else:
            return finding

    def split_path(self, ori_path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        path_parts= ori_path.split('/')
        results = [i for i in path_parts if i != '']
        return results

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
# results: root handler

print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
# results: not found handler

print(router.lookup("/home/about")) # should print 'about handler'
# results: about handler

print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
# results: about handler

print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
# results: not found handler