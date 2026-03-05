from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Renders the main page with the button
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    # This returns a snippet of HTML that HTMX will inject into the page
    return '<h1 class="text-4xl font-bold text-green-600">Welcome!</h1>'

if __name__ == '__main__':
    app.run(debug=True)