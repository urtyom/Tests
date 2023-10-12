import unittest
from unittest import TestCase
from main import new_folder


class TestNew(TestCase):
  def test_new_f(self):
    name = '123123123'
    expected = 201
    result = new_folder(name)
    self.assertEqual(result, expected)

  @unittest.expectedFailure
  def test_failed(self):
    name = 'qwerty'
    expected = 409
    result = new_folder(name)
    self.assertEqual(result, expected)
