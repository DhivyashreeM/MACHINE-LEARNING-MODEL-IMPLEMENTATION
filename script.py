import pandas as pd
import urllib.request
import io
import os

try:
    if os.path.exists('spam.csv'):
        df = pd.read_csv('spam.csv', encoding='latin-1')
        
        if all(col in df.columns for col in ['v1', 'v2']):
            df = df[['v1', 'v2']].rename(columns={'v1': 'label', 'v2': 'text'})
        else:
            df = df.rename(columns={df.columns[0]: 'label', df.columns[1]: 'text'})
    else:
        url = "https://raw.githubusercontent.com/commit-live-students/Spam_SMS_Detection/master/data/spam.csv"
        response = urllib.request.urlopen(url)
        df = pd.read_csv(io.StringIO(response.read().decode('utf-8')), encoding='latin-1')
        df = df[['v1', 'v2']].rename(columns={'v1': 'label', 'v2': 'text'})

except Exception as e:
    print(f"Couldn't load dataset: {e}")
    print("Using sample data instead...")
    data = {
        'text': [
            'Free money!!! Click here to claim your prize',
            'Hi John, how about a meeting tomorrow?',
            'You won a free iPhone! Claim now!',
            'Meeting reminder: Project discussion at 3pm',
            'Limited time offer! 50% off all products'
        ],
        'label': ['spam', 'ham', 'spam', 'ham', 'spam']
    }
    df = pd.DataFrame(data)

print(df.head())
