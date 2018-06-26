import requests
import io
from bs4 import BeautifulSoup
from nltk.tokenize import  word_tokenize, sent_tokenize,wordpunct_tokenize
from nltk.stem import PorterStemmer, LancasterStemmer
from nltk import pos_tag, ne_chunk
from nltk.util import  ngrams
from collections import  Counter
from nltk.stem import WordNetLemmatizer

#URL link for the url_code
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# #Getting the requets from web page
html_page = requests.get(url)

# # using beautiful soup for html parser
soup = BeautifulSoup(html_page.text, "html.parser")

#extracting the tag information
[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
#converting tag into text
visible_text = soup.getText()

#Creating a file and wriing data into the fie
with io.open(r'C:\Users\mural\OneDrive\Desktop\ICP-7.txt', "w+", encoding="utf-8") as f:
    f.write(visible_text)
    f.close()

with io.open(r'C:\Users\mural\OneDrive\Desktop\ICP-7.txt', "r", encoding="utf-8") as fo:
    for i in fo.readlines():
        print("-----word tokenization---------")
        tokenization = word_tokenize(i)
        # print(tokenization)
        print("-----pos tag---------")
        # print(pos_tag(i))
        print("-----trigram---------")
        # print(Counter(ngrams(word_tokenize(i), 3)))
        print("-----Name Entity Recognition---------")
        # print(ne_chunk(pos_tag(wordpunct_tokenize(i))))
        print("-----Stemmer---------")
        stemmer = LancasterStemmer()
        print("-----Lemmetization---------")
        lemmetizer = WordNetLemmatizer()
        for data in tokenization:
            #print("Lemmetizer for word: ", data,": " ,lemmetizer.lemmatize(data))
            print("Stemmer for word: ", data, ": ", stemmer.stem(data))


