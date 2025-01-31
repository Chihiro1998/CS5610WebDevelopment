from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/waddayaknow')
def knowledge():
    return "Not much, you?\n"


@app.route('/post-demo', methods=['GET', 'POST'])
def post_demo():
    if request.method == 'POST':
        return jsonify(request.form)
    return "That wasn't a POST request\n"


@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    if request.method == 'POST':
        return jsonify(request.form)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
