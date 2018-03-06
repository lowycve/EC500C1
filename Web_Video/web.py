import api
import os
import flask


app = flask.Flask(__name__)
@app.route('/')
def form():
	return flask.render_template('form.html')


@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = flask.request.form['name']
    api.get_all_tweets(name)
    api.writefile(name)
    return flask.render_template('submitted_form.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)