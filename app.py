from flask import render_template, Flask
app=Flask("app")

#@app.route('/hello/')
@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)


app.run(port=5555)