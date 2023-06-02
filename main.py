import unittest
from main import calculate

class TestMortgageCalculator(unittest.TestCase):
    def setUp(self):
        self.calculate = calculate.test_client()
        self.calculate.testing = True

    def test_index(self):
        response = self.calculate.get('/')
        self.assertEqual(response.status_code, 200)

    def test_calculate(self):
        data = {'loan_amount': '100000', 'interest_rate': '5', 'loan_term': '12'}
        response = self.calculate.post('/calculate', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your monthly payment is', response.data)
        self.assertIn(b'Your total payment is', response.data)

    def test_calculate_invalid_input(self):
        data = {'loan_amount': 'invalid', 'interest_rate': '5', 'loan_term': '12'}
        response = self.calculate.post('/calculate', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid input', response.data)

if __name__ == '__main__':
    unittest.main()
