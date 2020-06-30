#Reads whatsapp logs and generates a word cloud. 
 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
import re
from collections import Counter

inputs = ["illuminati.txt"] #Whatsapp log file(s)
user = "+447923357686" #Either the contact name or phone number with spaces removed
          #leave blank for all of the chat

banned_words = ["https","say","the","didnt","dont","aaron","guido","don't","aint","yeah",'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us',"i'm","im","theres","thats","there's","that's","ain't","saying","done","didnt","didn't","wont","won't","got","much","does","wouldn't","wouldnt","going","though","need","on","what","what's","said","couldn't","could","couldnt","group","stop","groups","wrong","ok","maybe","really","i'll","ill","oh","guess","why","ok","cant","can't","thing","ah","doesn't","doesnt","another","still","thank","it","i't","it","i t","it","i","t","its","im","i'm","it's","Iâ€™m","und","da","message","deleted","anyone"]


#returns the text in a message for a particular user
def find_user(target,text):
    new_text = text.split(":")
    
    try:
        find_target = new_text[1].split("-")
        
        if find_target[1][1] == "+":
            
            find_new_target = find_target[1].replace(" ","")
            if find_new_target == target:
                return new_text[2]
        if find_target[1].strip() == target.strip():
            return new_text[2]
        
        return False
  
    except:
        return False
        
#Strips all messages
def strip_text(text):
    new_text = text.split(":")
    try: 
    
        return new_text[2]
    except:
        return False
    
        
    
for target in inputs:
    file = open(target, "rt", errors="ignore") 
    comment_words = ""
    
    for line in file: 
        
        if user == "":
            text = strip_text(line)
        else:
            text = find_user(user,line)
        
        if text:
            if not "<Media omitted>" in text:
                try:
                    text = text.split(" ")
                except:
                    continue
                for word in text:
                    word = re.sub(r'[^a-zA-Z]', "", word)
                    if len(word) > 3:
                        if not word.lower() in banned_words:
                            comment_words += " " + str(word) + " "

    file.close()
    
stopwords = set(STOPWORDS) 
  

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 
     
     
               
  
#plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()