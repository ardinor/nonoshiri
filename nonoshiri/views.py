from flask import render_template
from twython import Twython

from nonoshiri import app
from secret import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/q/<query>')
def query(query):
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                      ACCESS_TOKEN, ACCESS_SECRET)
    results = twitter.search(q=query)
    statuses = results['statuses']
    #results['search_metadata'].keys()
    #['since_id_str', 'max_id_str', 'count', 'completed_in',
    # 'refresh_url', 'query', 'max_id', 'since_id', 'next_results']
    return render_template('index.html',
                           statuses=statuses)