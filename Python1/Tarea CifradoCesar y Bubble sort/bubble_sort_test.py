import bubble_sort

def test_bubble():
    
    assert bubble_sort.bubble_sort([5,4,2,7,1]) == [1,2,4,5,7]
if __name__ == "__main__":
    test_bubble()