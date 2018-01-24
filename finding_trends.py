import pickle
import Scraper as mus
import os
import twitter
import json

if not os.path.exists('secret_twitter_credentials.pkl'):
    Twitter={}
    Twitter['Consumer Key'] = ''
    Twitter['Consumer Secret'] = ''
    Twitter['Access Token'] = ''
    Twitter['Access Token Secret'] = ''
    with open('secret_twitter_credentials.pkl','wb') as f:
        pickle.dump(Twitter, f)
else:
    Twitter=pickle.load(open('secret_twitter_credentials.pkl','rb'))

auth = twitter.oauth.OAuth(Twitter['Access Token'],
                           Twitter['Access Token Secret'],
                           Twitter['Consumer Key'],
                           Twitter['Consumer Secret'])

twitter_api = twitter.Twitter(auth=auth)
print(twitter_api)
LOCAL_WOE_ID=int(mus.Scraping())
print(LOCAL_WOE_ID)
try:
	local_trends = twitter_api.trends.place(_id=LOCAL_WOE_ID)
except:
	print("No Trends available in twitter for given place")
	exit()
trends_set = set([trend['name'] for trend in local_trends[0]['trends']]) 
for trend in trends_set:
	print(trend)
