import unittest
from unittest.mock import patch
from io import StringIO
from LGT_canvas_esther import Canvas  # 假设类定义在 canvas.py 文件中

class TestCanvas(unittest.TestCase):

    def setUp(self):
        self.canvas = Canvas(15, 8)

    def test_canvas_creation(self):
        # the initial canvas should be blank
        expected_canvas = [[' ' for _ in range(15)] for _ in range(8)]
        self.assertEqual(self.canvas.canvas, expected_canvas)
    
    def test_hor_line(self):
        # horizontal line test
        self.canvas.line(2, 3, 10, 3, is_show=False)
        expected_canvas = [
            [' ' for _ in range(15)],
            [' ' for _ in range(15)],
            [' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x','x'] + [' '] * 5,
            [' ' for _ in range(15)],
            [' ' for _ in range(15)],
            [' ' for _ in range(15)],
            [' ' for _ in range(15)],
            [' ' for _ in range(15)],
        ]
        self.assertEqual(self.canvas.canvas, expected_canvas)

    def test_ver_line(self):
        # vertical line test
        self.canvas.line(6, 2, 6, 6, is_show=False)
        expected_canvas = [
            [' ' for _ in range(15)],
            [' ', ' ', ' ', ' ', ' ', 'x'] + [' '] * 9,
            [' ', ' ', ' ', ' ', ' ', 'x'] + [' '] * 9,
            [' ', ' ', ' ', ' ', ' ', 'x'] + [' '] * 9,
            [' ', ' ', ' ', ' ', ' ', 'x'] + [' '] * 9,
            [' ', ' ', ' ', ' ', ' ', 'x'] + [' '] * 9,
            [' ' for _ in range(15)],
            [' ' for _ in range(15)],
        ]
        self.assertEqual(self.canvas.canvas, expected_canvas)

    def test_rectangle(self):
        self.canvas.rectangle(3, 3, 8, 6)
        expected_canvas = [
            [' ' for _ in range(15)],
            [' ' for _ in range(15)],
            [' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' '] + [' '] * 6,
            [' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' '] + [' '] * 6,
            [' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' '] + [' '] * 6,
            [' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' '] + [' '] * 6,
            [' ' for _ in range(15)],
            [' ' for _ in range(15)],
        ]
        self.assertEqual(self.canvas.canvas, expected_canvas)

    def test_fill(self):
        self.canvas.rectangle(3, 3, 8, 6)
        self.canvas.fill(4, 4, 'p')
        expected_canvas = [
            [' ' for _ in range(15)],
            [' ' for _ in range(15)],
            [' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' '] + [' '] * 6,
            [' ', ' ', 'x', 'p', 'p', 'p', 'p', 'x', ' '] + [' '] * 6,
            [' ', ' ', 'x', 'p', 'p', 'p', 'p', 'x', ' '] + [' '] * 6,
            [' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' '] + [' '] * 6,
            [' ' for _ in range(15)],
            [' ' for _ in range(15)],
        ]
        self.assertEqual(self.canvas.canvas, expected_canvas)
    
    def test_check(self):
        # out of bound
        self.assertFalse(self.canvas.check(0, 0, 16, 9))
        # invalid oder
        self.assertFalse(self.canvas.check(5, 3, 4, 4))
    
    
    def test_line_special_case(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.canvas.line(1, 2, 3,4, is_show=False)
            # obtain printed error type
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Error: Only horizontal or vertical lines are supported.")


    def test_fill_invalid_coordinates(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.canvas.fill(16, 9, 'o')  
            # obtain printed error type
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Error: Coordinates are out of canvas bounds.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
