class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.history = [self.homepage]
        self.current = 0
        self.max_forward = 0

    def visit(self, url: str) -> None:
        if self.current + 1 >= len(self.history):
            self.history.append(url)
            self.current += 1
            self.max_forward = self.current
            return
        
        self.current += 1
        self.history[self.current] = url
        self.max_forward = self.current

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(self.max_forward, self.current + steps)
        return self.history[self.current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)