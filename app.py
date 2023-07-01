from flask import Flask, render_template, request
from bardapi import Bard

app = Flask(__name__)

token = 'YAhi70m7MPPMduUaCkgkJaN_wt4qrPWFi7iVZhWCqt7JMWSsuUly43Q296UtRM8cQcMskQ.'
bard = Bard(token=token)

# Define a function to generate tweets
def generate_tweet(prompt):
    response = bard.get_answer(prompt)
    tweet = response['content']
    return tweet

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form.get('content')
        mood_of_content = request.form.get('mood_of_content')
        platform = request.form.get('platform')
        length = int(request.form.get('length'))

        # Generate tweet
        fprompt = f"Write a {mood_of_content} {platform} post about {content} within {length} characters"
        tweet = generate_tweet(fprompt)

        return render_template('index.html', tweet=tweet)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

