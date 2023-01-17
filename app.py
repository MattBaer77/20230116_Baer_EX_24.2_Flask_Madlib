# First we must import Flask
# and by importing a flask object called request 
from flask import Flask, request, render_template

#  Importing the debug toolbar
from flask_debugtoolbar import DebugToolbarExtension

import stories

# This command initiates server - tells flask to do it's thing in the file.
app = Flask(__name__)

# Secret key for some reason
app.config['SECRET_KEY'] = "secret_key"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():

    story_prompts = stories.story.prompts

    return render_template("home-form.html", story_prompts=story_prompts )

@app.route('/stories')
def story_page():

    args = request.args

    text = stories.story.generate(args)

    return render_template("story.html", story=text)

