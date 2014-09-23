__author__ = 'yalnazov'

try:
    import unittest2 as unittest
except ImportError:
    import unittest


from paymill.models.filter import Filter


class TestFilter(unittest.TestCase):
    """

    Testing all methods of the Filter abstraction

    """

    def setUp(self):
        self.filter = Filter('payment', values=('pay_2f82a672574647cd911d',), operator=Filter.OPERATOR['EQUAL'])

    def test_filter_init(self):
        f = Filter('test', values=('test_id', 'test_id'), operator=Filter.OPERATOR['INTERVAL'])
        self.assertIsInstance(f, Filter)

    def test_filter_init_sets_key(self):
        self.assertEqual('payment', self.filter.key)

    def test_filter_init_sets_values(self):
        self.assertEqual(('pay_2f82a672574647cd911d', ), self.filter.values)

    def test_filter_init_sets_operator(self):
        self.assertEqual(Filter.OPERATOR['EQUAL'], self.filter.operator)

    def test_filter_equal_to_dict(self):
        self.assertEqual(dict(payment='pay_2f82a672574647cd911d'), self.filter.to_dict())

    def test_filter_interval_to_dict(self):
        f = Filter('test_interval', values=('123456789', '98717171',), operator=Filter.OPERATOR['INTERVAL'])
        self.assertEqual(dict(test_interval='123456789-98717171'), f.to_dict())



