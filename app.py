from flask import Flask, request, jsonify

app = Flask(__name__)

# Helper function to extract user information (Modify with actual user data)
def get_user_info():
    return {
        "user_id": "john_doe_17091999",  # Replace with actual user data
        "email": "john@xyz.com",  # Replace with actual user data
        "roll_number": "ABCD123"  # Replace with actual user data
    }

# POST /bfhl
@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        # Get the data from the JSON request
        data = request.json.get('data')
        
        # Validate if 'data' exists and is a list
        if not isinstance(data, list):
            raise ValueError("Invalid input: 'data' should be a list")
        
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
        return jsonify(response), 200

    except Exception as e:
        # Handle exceptions and construct an error response
        response = {
            "is_success": False,
            "error": f"400 Bad Request: {str(e)}"
        }
        return jsonify(response), 400

# GET /bfhl
@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

# Entry point
if __name__ == '__main__':
    app.run(debug=True)
