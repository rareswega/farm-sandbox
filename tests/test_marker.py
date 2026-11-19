import unittest

class TestMarkerFile(unittest.TestCase):
    def test_marker_content(self):
        with open('marker.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'farm-m4\n')

if __name__ == '__main__':
    unittest.main()
