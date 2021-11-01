
"""
    Turkish Document Topic Prediction Library    
    @author: Emre YAVUZ
    Github: github.com/emreyvz
    Site:  emreyavuz.co
"""

class TurkishTopicPredict:
    
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from nltk.corpus import stopwords
    from sklearn.naive_bayes import MultinomialNB
    
    textContent = ""
    data = pd.read_csv("news.txt", sep='&', engine='python')
    newsData = [doc for doc in data.iloc[:,0]]
    categoryData = [doc for doc in data.iloc[:,1]]
    dateData = [doc for doc in data.iloc[:,2]]
    sourceData = [doc for doc in data.iloc[:,3]]
    stopWords = list(stopwords.words('turkish'))
    vectorizer = TfidfVectorizer(analyzer='word', lowercase = True, stop_words=set(stopWords))
    sen_train_vector = vectorizer.fit_transform(newsData)
    clf = MultinomialNB()
    model = clf.fit(X=sen_train_vector.toarray(), y=categoryData)
    
    def __init__(self):
        pass
        
    def getPredict(self, _textContent):
        self.textContent = _textContent     
        sen_test_vector = self.vectorizer.transform([self.textContent])
        y_pred = self.model.predict_proba(sen_test_vector.toarray()) 
        return y_pred[0];

    def getTopics(self):
        return self.categoryData.unique().tolist()
    
    
        