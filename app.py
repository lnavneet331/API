from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        # Get the data from the JSON request
        data = request.json.get('data')
        if data is None:
            raise ValueError("Invalid input data")

        # Separate numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        # Find the highest lowercase alphabet
        lowercases = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = [max(lowercases)] if lowercases else []

        # Construct the response
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }

    except Exception as e:
        # Handle exceptions and construct an error response
        response = {
            "is_success": False,
            "error": str(e)
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
