from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_number', methods=['GET'])
def check_number():
    try:
        number = int(request.args.get('number'))
        if number % 2 == 0:
            result = 'even'
        else:
            result = 'odd'
        return jsonify({'number': number, 'result': result})
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input. Please provide an integer.'}), 400

if __name__ == '__main__':
    app.run(debug=True)