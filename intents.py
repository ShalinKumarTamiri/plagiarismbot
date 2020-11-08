#importing packages
from .welcomegreet import *
from .plagcheck import *

#creating global variables 
name = ''
content1 = ""
content2 = ""
isplagactive = False
plagcount = 0

#function to get the intent
def get_intent(data):
    global name,isplagactive,plagcount,content1,content2
    m = data['message'].lower()
    #check if message key is name
    if data['key']=="name":
        name =  m
        # returning next
        return "next"
    #checking if user asks to check the similarity
    elif isplagactive == True:
        plagcount = plagcount + 1
        if plagcount == 1:
            content1 = m
            return "plag"
        elif plagcount == 2:
            content2 = m
            return "plagcheck"
        #We need to take contents for two times to reseting the values
        else:
            plagcount = 0
            isplagactive = False
    #getting the main intent of the user
    m = m.split(" ")
    #different ways of user inputs
    plagstems = ["plag","yes","Yes","Plag","plagiarism","Plagiarism","similarity","Similarity","similar","Similar","common","Common","commonwords","Commonwords","Commoncount","commoncount","Similaritychecck","smilaritycheck"]
    for wrd in m:
        if wrd in plagstems:
            m = "plag"
    #if he wants to check
    if "plag" in m and isplagactive == False:
        isplagactive = True
        return "plag"
    #if user dont wants to do it 
    byestems = ["Bye","no","No","bye"]
    for wrd in m:
        if wrd in byestems:
            m = "bye"
    if m == "bye":
        return "bye"
    #if user doesn't give the right response
    else:
        return "unknown"    


def handle(data):
    global name,content1,content2
    from flask import render_template
    
    #Getting the intent 
    intent = get_intent(data)
    if intent == "next":
        #rendering the next related template
        return render_template("messages/greet.html",data={'greet':welcome_greeting()},name=name,question={'key':'Request','text':'what would you like to do'})
    elif intent == "plag":
        #rendering the plag related template
        return render_template("messages/content.html", question={'key':'Request','text':'Enter content to check'})
    elif intent == "plagcheck":
        #rendering the plagchecker related template
        return render_template("messages/plagchecker.html",data=plagiarismChecker(content1,content2),question={'key':'Request','text':'Do you like to do it again !!!'})
    elif intent == "unknown":
        #rendering the unknown related template
        return render_template("messages/unknown.html", question={'key':'Request','text':"I can't understand!!!"})
    elif intent == "bye":
        #rendering the bye related template
        return render_template("messages/bye.html",data = data,question={'key':'Request','text':'Bye!!! Have a nice day'})