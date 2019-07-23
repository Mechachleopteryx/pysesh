from flask import Flask, request, render_template, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# the secret key is used to encode the session. The session ()

TECHMODAL_MISSION_STATEMENT = """
The mission of Techmodal is to maintain its outstanding
reputation in delivering high quality tools that are key 
enablers in our customers operational and strategic
decisions Continuing to employ and develop high calibre
individuals that are capable of delivering a quality
service to our customers
"""


word_list = TECHMODAL_MISSION_STATEMENT.split()
word_list = [x.lower() for x in word_list if len(x) >= 4] # filter for words with 4 letters or more

def initilase(sesh):
    sesh["number_of_guesses"] = 0
    return sesh

@app.route("/", methods=['GET','POST'])
def hagnman():
    print(session)

    # if session is empty, initialise it
    # note: session is like a dictionary. An empty dictionary has a boolean value of False.
    if not session:
        initilase(session)

    # extract values from session
    number_of_guesses = session["number_of_guesses"]

    # if the request method is post, add 1 to num_guesses
    # the request is POST when the button is clicked. If you are just visiting the page,
    # then its just GET.
    if request.method == "POST":
        number_of_guesses += 1

    # update session
    session["number_of_guesses"] = number_of_guesses

    # render template from templates/home.html
    return render_template('home.html', number_of_guesses=number_of_guesses)

@app.route('/reset')
def reset():
    # this will delete everything from session.
    session.clear()
    # this redirects you to the url for the hangman() function above.
    return redirect(url_for('hagnman'))