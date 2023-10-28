from flask import Flask, request, render_template, redirect
import random
import string

app = Flask(__name__)

# Dictionary to store URL mappings
url_mapping = {}

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    short_code = generate_short_code()

    # Store the mapping in the dictionary
    url_mapping[short_code] = long_url

    return short_code

@app.route('/<short_code>')
def redirect_to_long_url(short_code):
    if short_code in url_mapping:
        long_url = url_mapping[short_code]
        return redirect(long_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
