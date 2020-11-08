#importing packages
import string
import nltk
##importing snltk.corpus for stopwords
from nltk.corpus import stopwords 
#importing snowballstrmmer for stemming words
from nltk.stem import SnowballStemmer

def plagiarismChecker(content1,content2):
    #Converting messages into string and spliting them
    content1 = str(content1)
    content1 = content1.split(" ")
    content2 = str(content2)
    content2 = content2.split(" ")
    #Removing stopwords in the contents
    stop_word = set(stopwords.words('english'))
    stop_words=list(stop_word)
    filtered_list1 = [wrd for wrd in content1 if not wrd in stop_words]
    filtered_list2 = [wrd for wrd in content2 if not wrd in stop_words]
    words1 = []
    words2 = []
    #removing punctuations in the remaining list
    for wrd in filtered_list1:
        if wrd not in string.punctuation:
            words1.append(wrd)
    for wrd in filtered_list2:
        if wrd not in string.punctuation:
            words2.append(wrd)
    #Stemming the words
    stemmer = SnowballStemmer('english')
    filtered_list1 = []
    for wrd in words1:
 		#adding every stemmed word into filtered list
        filtered_list1.append(stemmer.stem(wrd))
    filtered_list2 = []
    for wrd in words2:
 		#adding every stemmed word into filtered list
        filtered_list2.append(stemmer.stem(wrd))  
    words1 = filtered_list1
    words2 = filtered_list2
    #finding lengths and common words
    length1 = len(words1)
    length2 = len(words2)
    common_list = []
    for word in words1:
        if word in words2:
            common_list.append(word)
    common_length = len(common_list)
    #computing similarity
    unique_words1_length = length1 - common_length
    unique_words2_length = length2 - common_length
    uniqueness = ((unique_words1_length + unique_words2_length)/(length1+length2))*100
    return f"The contents are {100-uniqueness} similar"
 	
