# /src/history.py

class BrowserHistory:
    def __init__(self, start="home"):
        self._start = start      # store start page
        self._cur = start        # current page
        self._back = []          # stack for back navigation
        self._fwd = []           # stack for forward navigation

    def visit(self, url: str) -> None:
        """Visit a new URL: push current (if not start page) to back,
        set new current, and clear forward history."""
        if self._cur != self._start or self._back:  # don't push 'home' as a history item
            self._back.append(self._cur)
        self._cur = url
        self._fwd.clear()

    def back(self) -> str:
        """Go back to the previous page. Raise IndexError if no history."""
        if not self._back:
            raise IndexError("No pages in back history")
        self._fwd.append(self._cur)
        self._cur = self._back.pop()
        return self._cur

    def forward(self) -> str:
        """Go forward to the next page. Raise IndexError if no forward history."""
        if not self._fwd:
            raise IndexError("No pages in forward history")
        self._back.append(self._cur)
        self._cur = self._fwd.pop()
        return self._cur

    def current(self) -> str:
        """Return the current page."""
        return self._cur
