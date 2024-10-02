from flask import Flask, request, render_template

app = Flask(__name__)

# Route to display the greeting and prompt the user for their name
@app.route('/', methods=['GET', 'POST'])
def index():
    # Read the current content of the text file
    with open('hello.txt', 'r') as file:
        greeting = file.read()

    if request.method == 'POST':
        # Get the user's name from the form
        user_name = request.form['name']
        
        # Write the user's name to the text file
        with open('hello.txt', 'w') as file:
            file.write(f"Hello, {user_name}!")
        
        # Update the greeting with the user's name
        greeting = f"Hello, {user_name}!"

    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
