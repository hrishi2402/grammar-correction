from flask import Flask,request,render_template,redirect
from gramformer import Gramformer

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def hello_world():
    if request.method == "GET":
        output = None
        return render_template('home.html',output=output)
    elif request.method == "POST":
        try:
            text = request.form.get('text')        
        except:
            raise IOError()    
        if text:   
            output = remove_errors(text)
            for i in output:
                output = {"output":i,"original":text} 
            return render_template('home.html',output=output)
        else:
            redirect('hello_world')

def remove_errors(input):
    gf = Gramformer(models=1, use_gpu=False)
    a = gf.correct(input)
    return a
