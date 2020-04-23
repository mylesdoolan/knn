import unittest
import KNN

class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(11.999999999999998, KNN.euclidean_distance(1, 4, 4, 1))

    def test_k(self):
        self.assertEqual(35, KNN.k(1200))


if __name__ == '__main__':
    unittest.main()
