from autocorrect import spell
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot


#Tokenizing the sentence and then return a list of words
def tokens(sentence):
        return nltk.word_tokenize(sentence)

#Checks the spelling of words and returns the correct word
def SpellChecker(line):
    correctword_list=[]
    for i in tokens(line):
        correctword_list.append(spell(i))
    return correctword_list

#Removes any specail characters in the sentence and returns the string
def removePunct(sentence):
        return  "".join(i for i in sentence if i not in ('!','.',':',','))

#Removes the stop words('is','the','in'....) from the list of tokenized words and returns the list 
def stopword(tokenize_list):
        stop_words = set(stopwords.words('english'))
        filtered_list = [i for i in tokenize_list if not i in stop_words]
        filtered_list = []

        for i in tokenize_list:
                if i not in stop_words:
                        filtered_list.append(i)
        return filtered_list

      return lemit_list

#Creates a vector to the list of words and plots them as a scattered plot
def vector(keyword_list):
	vlist = [keyword_list]
	model = Word2Vec(vlist, min_count=1)
	X = model[model.wv.vocab]
	pca = PCA(n_components=2)
	result = pca.fit_transform(X)
        # create a scatter plot of the projection
	pyplot.scatter(result[:, 0], result[:, 1])
	words = list(model.wv.vocab)
	for i, word in enumerate(words):
        	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
	pyplot.show()

#Takes input of a string that is to be processed
string = input("Enter a String: ")

#Removing special characters
noPunct = removePunct(string.lower())
print("---------------------------------------------------------------------------------------------------------------")
string = noPunct
print(noPunct)

#Tokenizing
token_list = tokens(string)
print("----------------------------------------------------------------------------------------------------------------")
print(token_list)

#Spell Checker
correct_list = SpellChecker(string)
print("----------------------------------------------------------------------------------------------------------------")
print(correct_list)

#Removing Stop words
stopword_list = stopword(correct_list)
print("----------------------------------------------------------------------------------------------------------------")
print(stopword_list)

#Plotting words 
print("-----------------------------------------------------------------------------------------------------------------")
vector(stopword_list)

