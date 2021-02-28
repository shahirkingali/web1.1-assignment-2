from flask import Flask, request, render_template
import random

app = Flask(__name__)


def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')


@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        <input type="submit" value="Submit!">
    </form>
    """


@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    context = {
        'users_froyo_flavor': request.args.get('flavor'),
        'users_froyo_toppings': request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)


@ app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
        <form action="/favorites_results" method="GET">
            What is your favorite animal? <br/>
            <input type="text" name="animal"><br/>
            What color are they? <br/>
            <input type="text" name="color"><br/>
            Where do they live? <br/>
            <input type="text" name="city">
            <input type="submit" value="Submit">
        </form>
    """


@ app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    favorite_animal = request.args.get('animal')
    animal_color = request.args.get('color')
    animal_city = request.args.get('city')

    return f"Wow, I didn't know {animal_color} {favorite_animal}'s live in {animal_city}!"


@ app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
        <form action="/message_results" method="POST">
        Type a secret message
        <input type="text" name="message"><br/>
        <input type="submit" name="Submit!">
        </form>
    """


@ app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    message = request.form['message']
    return sort_letters(message)


@ app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')


@ app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    context = {
        'operation': request.args.get('operation'),
        'first_num': request.args.get('operand1'),
        'second_num': request.args.get('operand2')
    }

    return render_template('calculator_results.html', **context)


HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}


@ app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')


@ app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = request.args.get('horoscope_sign')

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = HOROSCOPE_PERSONALITIES.get(horoscope_sign)

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randit(1, 99)

    context = {
        'horoscope_sign': horoscope_sign,
        'personality': users_personality,
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
