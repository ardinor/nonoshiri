from flask import render_template, jsonify, Response
from twython import Twython
import json

from nonoshiri import app
from secret import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/q/<query>.json')
def query(query):
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                      ACCESS_TOKEN, ACCESS_SECRET)
    results = twitter.search(q=query)
    statuses = results['statuses']
    status_dict = {}
    status_list = []
    #maybe just take out the info we want? less data going back and forth...
    for index, i in enumerate(statuses):
        status_dict[index] = {'text': i['text'],
                              'name': i['user']['name']}
        status_list.append({'text': i['text'],
                            'name': i['user']['name']})
    #results['search_metadata'].keys()
    #['since_id_str', 'max_id_str', 'count', 'completed_in',
    # 'refresh_url', 'query', 'max_id', 'since_id', 'next_results']
    #return render_template('index.html',
    #                       statuses=statuses)
    return Response(json.dumps(status_list), mimetype='application/json')
    #same as below?
    #return jsonify(results=status_list)
