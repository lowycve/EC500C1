import tweepy #https://github.com/tweepy/tweepy
import json
import wget
from subprocess import call

#Twitter API credentials
consumer_key = "X81uhAUxCUv5xFsqmmWY1Uytt"
consumer_secret = "oWvsm4D4SDke4mCSZ2fbmDeLAXkiQvWCcR7RPxDSWC1qcvQH8t"
access_key = "956288592686534656-rSUsibsc3wrljniaq9BjkveIJcfsTkQ"
access_secret = "vj8XH6UGG9Cm38vwv4V51ot39bwsFq9D50W7QuM4knJdO"


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))
       

    # file = open('tweet.json', 'w') 
    # print ("Writing tweet objects to JSON please wait...")
    # for status in alltweets:
    #     json.dump(status._json,file,sort_keys = True,indent = 4)
    media_files = set()

    for status in alltweets:
        media = status.extended_entities.get('media', [])
        if(len(media) > 0):
            for i in range(len(media)):
                media_files.add(media[i]['media_url'])
    for media_file in media_files:
        wget.download(media_file)
    #close the file
    print ("Done")
   

get_all_tweets("@LiyiCao")
call('cd Desktop/')
call('cd untitled\ folder/')
call('ffmpeg -framerate 1 -pattern_type glob -i "*.jpg" -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4')