class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        node = Node(url)
        self.current.next = node
        node.prev = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.current.prev != None:
            self.current = self.current.prev
            i += 1
        return self.current.value

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.current.next != None:
            self.current = self.current.next
            i += 1
        return self.current.value
            


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)