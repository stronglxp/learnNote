from my_add import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 2) == 1
    assert add(0, 0) == 0
    assert add(10, -5) == 5
