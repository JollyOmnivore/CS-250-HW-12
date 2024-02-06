from flask import Flask,render_template,request

app = Flask(__name__,static_url_path='/static')

@app.route('/factor', methods=['GET','POST'])
def factor():
    if request.method == "POST":

        N = request.form["number"]
        N = int(N)
        factors = []
        factors = getFactors(N)
        return render_template('factor.html', factors=factors)

    return render_template('factor.html')

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/wordcount', methods=['GET','POST'])
def wordcount():
    words = []
    if request.method == "POST":
        text = request.form["text"]
        for line in text:
            word =line.split(" ")
            words.append(word)
            worddict= {}
            worddict = countwords(words)
        return render_template('wordcount.html', worddict=worddict)



def getFactors(numb):
    factors = []
    for i in range(1, numb + 1):
        if numb % i == 0:
            factors.append(i)
    return factors

def countwords(words):
    worddict = {}

    for word in words:
        if word in worddict:
            freq = worddict[word]
            freq += 1
            worddict[word] = freq
        else:
            worddict[word] = 1
    return worddict

app.run()