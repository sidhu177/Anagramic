## Importing the library files
from flask import Flask, render_template, flash, request
from wtforms import Form,TextField, TextAreaField, StringField, SubmitField
from flask_bootstrap import Bootstrap
import sys

## Setting Flask Config 
DEBUG=False
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SuperSecretKey'
strnum=0

## Loading the dictionary file onto memory
file = '/opt/Anagramic/WordList.txt'
def load(file):
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e:
        print("{}\n Error opening {}. Terminating Program.".format(e,file),file=sys.stderr)
        sys.exit(1)

word_list = load(file)
anagram_list = []

## Core Flask Application
class NameForm(Form):
    name = TextField('Word: ')
    #name = name.lower()

@app.route("/", methods=['GET','POST'])
def Anagram():
    global anagram_list    
    form = NameForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        strnum = len(name)
        if strnum==0:
            anagram_list='O'
            flash('No Word Entered')
        else:
            name_sorted = sorted(name)
            anagram_list = []
            for word in word_list:
                word = word.lower()
                if word!=name:
                    if sorted(word)==name_sorted:
                        anagram_list.append(word)
            str1 = ''.join(anagram_list)
            strnum = len(anagram_list)
            str1 = str(strnum)
            flash('Total Anagrams found = ' +str1)
    
    return render_template('index.html', form=form, data=anagram_list)

@app.errorhandler(404)
def page_not_found(e):
    return "Not Found: " + request.path

if __name__=="__main__":
    app.run(host='0.0.0.0')
