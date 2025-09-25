from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # prints to console
    return param  # displays in browser

@app.route('/count/<int:param>')
def count(param):
    numbers = "\n".join(str(i) for i in range(param))
    return numbers + "\n"

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        # division by zero check
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        result = f"Error: Unsupported operation '{operation}'"
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
