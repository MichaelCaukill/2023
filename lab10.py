def count(sequence, item):
    y = 0
    for n in sequence:
        if n == item:
            y += 1
    return y

#printcount)

def test_count(): 
    assert count ([1,2,2,2,2,6], 2) == 4