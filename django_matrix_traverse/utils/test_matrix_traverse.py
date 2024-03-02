import unittest
import asyncio
from matrix_traverse import parse_matrix, clockwise_matrix_traverse, get_matrix

class ParseMatrixTestcase(unittest.TestCase):
    """Tests for parse_matrix function"""

    def test_parse_matrix(self):
        """Parsing test for matrix"""
        input_matrix = """
+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
"""
        output_matrix = [[10, 20, 30, 40],
                        [50, 60, 70, 80],
                        [90, 100, 110, 120],
                        [130, 140, 150, 160]]
        
        formatted_matrix = parse_matrix(input_matrix)
        self.assertEqual(formatted_matrix, output_matrix)

    def test_parse_matrix_amended(self):
        """Parsing test for amended matrix"""
        input_matrix = """
+-----+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |  50 |
+-----+-----+-----+-----+-----+
|  60 |  70 |  80 |  90 |  100 |
+-----+-----+-----+-----+-----+
|  110 | 120 | 130 | 140 | 150 |
+-----+-----+-----+-----+-----+
| 160 | 170 | 180 | 190 |  200 |
+-----+-----+-----+-----+-----+
| 210 | 220 | 230 | 240 |  250 |
+-----+-----+-----+-----+-----+
"""
        output_matrix = [[10, 20, 30, 40, 50],
                        [60, 70, 80, 90, 100],
                        [110, 120, 130, 140, 150],
                        [160, 170, 180, 190, 200],
                        [210, 220, 230, 240, 250]]
        
        formatted_matrix = parse_matrix(input_matrix)
        self.assertEqual(formatted_matrix, output_matrix) 


class ClockwiseMatrixTraverseTestCase(unittest.TestCase):
    """Tests for clockwise_matrix_traverse function"""

    def test_clockwise_matrix_traverse(self):
        """Matrix traverse test"""
        input_matrix = [[10, 20, 30, 40],
                        [50, 60, 70, 80],
                        [90, 100, 110, 120],
                        [130, 140, 150, 160]]
        
        output = [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]
        
        traversed_matrix = clockwise_matrix_traverse(input_matrix)
        self.assertEqual(traversed_matrix, output)

    def test_clockwise_matrix_traverse_amended(self):
        """Matrix traverse test for amended matrix"""
        input_matrix = [[10, 20, 30, 40, 50],
                        [60, 70, 80, 90, 100],
                        [110, 120, 130, 140, 150],
                        [160, 170, 180, 190, 200],
                        [210, 220, 230, 240, 250]]
        
        output = [10, 60, 110, 160, 210, 220, 230, 240, 250, 200, 150, 100, 50, 40, 30, 20, 70, 120, 170, 180, 190, 140, 90, 80, 130]
        
        traversed_matrix = clockwise_matrix_traverse(input_matrix)
        self.assertEqual(traversed_matrix, output)


class GetMatrixTestCase(unittest.TestCase):
    """Tests for get_matrix function"""

    def test_get_matrix(self):
        """Test for correct receiving from URL and traverse matrix"""
        SOURCE_URL = 'https://raw.githubusercontent.com/Real-Estate-THE-Capital/python-assignment/main/matrix.txt'
        TRAVERSAL = [
        10, 50, 90, 130,
        140, 150, 160, 120,
        80, 40, 30, 20,
        60, 100, 110, 70,
    ]
        result = asyncio.run(get_matrix(SOURCE_URL))
        self.assertEqual(result, TRAVERSAL)


if __name__ == '__main__':
    unittest.main()
