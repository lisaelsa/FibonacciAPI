from flask import Flask, request, jsonify

app = Flask(__name__)

def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series[:n]

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    try:
        n = int(request.args.get('n'))
        if n < 0:
            return jsonify({'error': 'Negative input is not allowed'}), 400
        fib_series = fibonacci(n)
        return jsonify({'fibonacci_series': fib_series})
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide a positive integer'}), 400

if __name__ == '__main__':
    app.run(debug=True)
