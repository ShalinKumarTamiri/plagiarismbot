#importing the packages required
from flask import Flask, request, render_template

app = Flask(__name__)

#creating route
@app.route("/")
def introduce(): 
    from .data.about import bot
    #rendering the template
    return render_template("index.html",
                            data=bot,
                            question ={"key" : "name" , "text" : "Can I have your name"}
                            )

#creating route
@app.route('/message', methods=['POST'])
def user_message():
    #checking whether it is post request
    if request.method == 'POST':
        from .intents import handle
        #caalling handle function
        return handle(request.form)
    else:
        return "INVALID"
    

if __name__ == '__main__':
    app.run(threaded=True,port=5000)
