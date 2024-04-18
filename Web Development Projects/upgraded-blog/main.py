from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    url = requests.get("https://api.npoint.io/c74eba9692e63b9264c2")
    blog_post = url.json()
    return render_template('index.html', post = blog_post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def blog(id):
    journals = requests.get("https://api.npoint.io/c74eba9692e63b9264c2").json()
    thisJournal = None
    for journal in journals:
        if journal['id'] == id:
            thisJournal = journal
    return render_template('post.html', thisJournal = thisJournal)






if __name__ == '__main__':
    app.run(debug=True)