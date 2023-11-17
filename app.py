from flask import Flask, render_template, request
from calculator import fibonacci, factorial
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        n = int(request.form['number'])
    except ValueError:
        return render_template('error.html', message='Please enter a valid non-negative integer.')

    start_time_factorial = time.time_ns()
    factorial_result = factorial(n)
    
    # Commented out for demonstration purposes
    # Simulate a 5-second delay
    #time.sleep(5)

    end_time_factorial = time.time_ns()
    factorial_time_ns = end_time_factorial - start_time_factorial

    # Convert factorial_time_ns to seconds
    factorial_time_sec = factorial_time_ns / 1e9

    # Format time values for display
    factorial_time_sec = "{:.6f}".format(factorial_time_sec)
    factorial_time_ns = "{:.6f}".format(factorial_time_ns)

    # Provide feedback for long computations
    print("factorial_time_sec:", factorial_time_sec)
    if float(factorial_time_sec) >= 1.0:
        feedback_message = "Note: The factorial calculation took longer than 1 second."
    else:
        feedback_message = ""
    print("feedback_message:", feedback_message)

    return render_template('result.html', n=n, factorial_result=factorial_result, 
                           factorial_time_sec=factorial_time_sec, 
                           factorial_time_ns=factorial_time_ns, 
                           feedback_message=feedback_message)

if __name__ == '__main__':
    app.run(debug=True)