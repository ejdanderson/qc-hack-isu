from flask import Flask, request, jsonify
from datetime import datetime
from qvm import vm
import program

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)


@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.json
    print (content['mytext'])
    p = content['mytext']
    wvf = program.run(p)
    return jsonify({"wavefunction":vm.wavefunction(wvf)})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)