from flask import Flask# Import Flask Class, and redirect
app = Flask(__name__) # Create an Instance

@app.route('/') # Route the Function
def main(): # Run the function
    return "Hello, World! This is Ian's first web app!"

app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)
