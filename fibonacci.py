import unittest

def fibo(n = int):
    prev = 1
    fibonacci = 0
    most = 1
    for i in range(n-1):
        most = fibonacci
        fibonacci += prev
        prev = most
    print(fibonacci)

class TestfibMennyi(unittest.TestCase):
    def test_egy(self):
        elso = fibo(1)
        self.assertEqual(elso, 0)
    def test_nagyobb(self):
        nagy = fibo(50)
        self.assertGreaterEqual(nagy, 192168)
    def test_kicsi(self):
        torpiszorp = fibo(5)
        self.assertLessEqual(torpiszorp, 20)
    def test_kb(self):
        esetleg = fibo(4)
        self.assertAlmostEqual(esetleg, 1)
    def test_vane(self):
        letezik = fibo(192)
        self.assertIs(letezik)

    
unittest.main()