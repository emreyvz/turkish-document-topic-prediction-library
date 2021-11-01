
"""
    Turkish Document Topic Prediction Library    
    @author: Emre YAVUZ
    Github: github.com/emreyvz
    Site:  emreyavuz.co
    Mail: emreyavuz25@yandex.com
"""

class TurkishTopicPredict:
    
    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from nltk.corpus import stopwords
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.metrics import accuracy_score
    
    predictionScore = int()
        
    def __init__(self):
        self.predictionScore = 0
            
    def getAccuracyScore(self):
        return self.predictionScore    
    
    def setAccuracyScore(self, _value):
        self.predictionScore = _value       
       
    def getPrediction(self, _textContent):
        """
        Parameters
        ----------
        _textContent : String
            The data that will be classify by algorithm

        Raises
        ------
        ValueError
            An exception that thrown when _textContent parameters sends empty or null
            
        Returns
        -------
        String
            Predicted topic by algorithm

        """
        if not _textContent:
            raise ValueError('The data that will be analyse is empty. Set getPrediction(@_textContent) parameter to get proper output')
        data = self.pd.read_csv("dataset", sep='&', engine='python')
        newsData = [doc for doc in data.iloc[:,0]]
        categoryData = [doc for doc in data.iloc[:,1]]
        dateData = [doc for doc in data.iloc[:,2]]
        sourceData = [doc for doc in data.iloc[:,3]]
        stopWords = list(self.stopwords.words('turkish'))
        vectorizer = self.TfidfVectorizer(analyzer='word', lowercase = True, stop_words=set(stopWords))
        sen_train_vector = vectorizer.fit_transform(newsData)
        clf = self.MultinomialNB()
        model = clf.fit(X=sen_train_vector.toarray(), y=categoryData)
        textContent = _textContent 
        sen_test_vector = vectorizer.transform([textContent])
        y_pred = model.predict(sen_test_vector.toarray()) 
        self.setAccuracyScore(clf.score(X=sen_train_vector.toarray(), y=categoryData) * 100)
        return y_pred[0];

    def getTopics(self):
        """
        Returns
        -------
        Set
        Unique category values from dataset. Returns set.

        """
        data = self.pd.read_csv("dataset", sep='&', engine='python')
        categoryData = [doc for doc in data.iloc[:,1]]
        return set(categoryData)
    
    
        