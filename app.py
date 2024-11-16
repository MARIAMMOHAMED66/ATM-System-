from flask import Flask, render_template, request
from ATM_system import ATM  # استيراد الكود البرمجي الخاص بك هنا

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('atm_withdrawal.html')  # صفحة HTML الخاصة بالسحب

@app.route('/withdraw', methods=['POST'])
def withdraw():
    amount = request.form['amount']
    # قم بتطبيق المنطق الخاص بك من ATM_system هنا
    atm = ATM()
    message = atm.withdraw_cash(amount)
    return render_template('atm_withdrawal.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
55