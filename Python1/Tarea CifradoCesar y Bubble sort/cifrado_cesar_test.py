import cifrado_cesar

def test_cifrar():
    assert cifrado_cesar.main(x="derek", Num= 3) == "ghuhn"
if __name__ == "__main__":
    test_cifrar()
    
    
# def test_decifrar():
#     assert cifrado_cesar.main(x="ghuhn", Num= 3) == "dereek"

# if __name__ == "__main__":
#     test_cifrar()


