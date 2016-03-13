# NLP

Paper reference : http://www.dai-labor.de/fileadmin/files/publications/narr-twittersentiment-KDML-LWA-2012.pdf

### How it works
 * Data scraped from various Twitter accoutns (mostly Hindi based)
 * Ground truth obtained by using Google Translate
 * Classifier trained using a [Naive Bayes Classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
 * Tweets are analyzed as they are
 * Tweets are scanned for emoticons (to give higher score to certain sentiments)

### Running it
 * `pip install -r requirements`
 * `python BayesClassifier/eval.py` , takes `file_name` as input, where `file_name` is the file stored in the Input folder. Output is stored in the Output folder.
 * To run the classifier for yourself, run `python  BayesClassifier/SentiAPI.py` to give custom input.
