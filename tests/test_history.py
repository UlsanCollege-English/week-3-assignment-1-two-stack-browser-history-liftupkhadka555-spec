import pytest
from src.history import BrowserHistory

def test_visit_and_current():
    h = BrowserHistory()
    assert h.current() == "home"
    h.visit("a"); h.visit("b")
    assert h.current() == "b"

def test_back_forward_flow():
    h = BrowserHistory()
    h.visit("a"); h.visit("b"); h.visit("c")
    assert h.back() == "b"
    assert h.back() == "a"
    assert h.forward() == "b"
    h.visit("x")
    with pytest.raises(IndexError):
        h.forward()
    assert h.current() == "x"

def test_back_underflow():
    h = BrowserHistory()
    with pytest.raises(IndexError):
        h.back()

# --- Edge Cases ---
def test_edge_back_at_start_raises():
    h = BrowserHistory()
    # no pages visited yet beyond "home"
    with pytest.raises(IndexError):
        h.back()
    assert h.current() == "home"

def test_edge_forward_when_empty_raises():
    h = BrowserHistory()
    h.visit("a")
    with pytest.raises(IndexError):
        h.forward()  # no forward history after a fresh visit

# --- Longer Scenario ---
def test_long_navigation_session():
    h = BrowserHistory()
    h.visit("a"); h.visit("b"); h.visit("c")
    assert h.back() == "b"      # c -> b
    h.visit("x")                # clears forward stack
    with pytest.raises(IndexError):
        h.forward()
    h.visit("y"); h.visit("z")
    assert h.back() == "y"
    assert h.back() == "x"
    assert h.back() == "b"
    assert h.back() == "a"
    with pytest.raises(IndexError):
        h.back()
    assert h.current() == "a"