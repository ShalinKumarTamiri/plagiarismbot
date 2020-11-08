# Plagiarism-Bot
 
 ### Team Memebers:
 
    * Shalin Kumar - 18pa1a1242
    
    * Mydhili - 18pa1a1210
 
 ## Objective :
 
    * This is a plagiarism bot to check similarity between the content given by the end user.
    
    * We used HTML,CSS,BOOTSTRAP,JAVASCRIPT,FLASK to develop this.
    
    * Now, our main goal to check text only.
    
 ## Steps :
     
    1.Chatbot will greet the enduser and asks user name and bot will reply to the messages according to the input of the end user.
    
    2.It will greet the end user and asks whether he/she wants to check who similar the files are or wants to exit.
    
    3.If he/she wants to perform plagiarism check then bot will ask the end user to enter the content and bot will return the percentage of similarity.
    
    4.Then , it aks for the input whether he/she wants perform again or wants to exit.
    
    5.Finally , it greets the end user and quits.
    
 ## Approach :
 
    1.We initially splits the content into words 
    
    2.Then we will remove punctuations from the remaining words
    
    3.We will do this process for both the contents
    
    4.We will find how many words are common in both filtered words and we will calculate how similar they are.
    
 ## Functions and their use :
 
    1.Welcome_greeting : It will create a greeting to the enduser.
        
    2.PlagiarismChecker : It will split the text and  remove punctuation, stem the words and calculate similarity 
    
    3.user_meessage : It will create a user message and respond to the user input
    
    4.Handle : It will handle the intents by calling get-intents function
    
    5.Get_intents : It will return main intent of the user.
    
 ## Images of bot :
 
   ![chat](https://raw.githubusercontent.com/ShalinKumarTamiri/plagiarismbot/main/images/bandicam%202020-11-08%2017-46-53-674.jpg)
    
   ![chat2](https://raw.githubusercontent.com/ShalinKumarTamiri/plagiarismbot/main/images/bandicam%202020-11-08%2018-15-53-783.jpg)
    
 ## Heroku Link :
 
  https://plagbot.herokuapp.com/
 
 ## Demo video link :
    
  [![](http://img.youtube.com/vi/PoHRVWTtpzk/0.jpg)](http://www.youtube.com/watch?v=PoHRVWTtpzk "")
