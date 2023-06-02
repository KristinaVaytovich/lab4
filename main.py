from flask import Flask, render_template, request
import unittest

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    loan_amount = float(request.form['loan_amount'])
    interest_rate = float(request.form['interest_rate']) / 100
    loan_term = int(request.form['loan_term'])

    monthly_interest_rate = interest_rate / 12
    total_payments = loan_term * 12

    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-total_payments))
    total_cost = monthly_payment * total_payments
    total_interest = total_cost - loan_amount

    return render_template('result.html', monthly_payment=monthly_payment, total_cost=total_cost,
                           total_interest=total_interest)

def calc(loan_amount, interest_rate, loan_term):
    try:
        loan_amount = float(loan_amount)
        interest_rate = float(interest_rate)
        loan_term = float(loan_term)
    except ValueError:
        return 'ValueError: не является числом'
    except TypeError:
        return "TypeError: недопустимое значение"
    if (loan_amount < 0 or interest_rate < 0 or loan_term < 0):
        return "Одно или все значения меньше нуля"
    else:
        return render_template

class test_Converter(unittest.TestCase):
    def test_values(self):
        self.assertEqual(calc(100000, 5, 12))
        self.assertEqual(calc(-100000, -1, -2), "Одно или все значения меньше нуля")

    def test_types(self):
        self.assertEqual(calc(100000, 1, "пять"), 'ValueError: не является числом')
        self.assertEqual(calc(100000, 1, [1, 2, 3]), 'TypeError: недопустимое значение')
        self.assertEqual(calc(100000, 1, (1, 2, 3)), 'TypeError: недопустимое значение')

if __name__ == '__main__':
    app.run(debug=True)
