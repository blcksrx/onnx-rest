import unittest

from api.model.main import model_existence_checker


class TestApiModel(unittest.TestCase):

    def test_model_existence_checker(self):
        self.assertEqual(model_existence_checker("foo.onnx"), False)
