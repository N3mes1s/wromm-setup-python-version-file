import sys
import unittest


class PythonVersionFileTest(unittest.TestCase):
    def test_version_file_selected_python(self):
        self.assertEqual(sys.version_info[:2], (3, 13))
        print(sys.version)


if __name__ == "__main__":
    unittest.main()
