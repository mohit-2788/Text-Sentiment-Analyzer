import boto3

def do_sentiment(input):
    comprehend = boto3.client(service_name='comprehend',region_name='ca-central-1',use_ssl=True)
    response = comprehend.detect_sentiment(Text=input,LanguageCode="en")
    sentiment_type = response["Sentiment"]
    sentiment_scores = response["SentimentScore"]
    return sentiment_type,sentiment_scores
