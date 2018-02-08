import tweepy 
import json
import wget
import requests
import io
import os
from os import listdir
from google.cloud import vision
from google.cloud.vision import types
import sys

consumer_key = 'Enter your information here'
consumer_secret = 'Enter your information here'
access_key = 'Enter your information here'
access_secret = 'Enter your information here'


def get_all_tweets(screen_name):
    

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    alltweets = []    
    
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)
    if len(new_tweets) == 0:
        print('The user did not tweet anything.')
        sys.exit()

    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:

        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        
        alltweets.extend(new_tweets)
        
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            print('more that 15 tweets downloaded.')
            break
        print ("There are %s tweets downloaded so far" % (len(alltweets)))

    media_files = set()

    for status in alltweets:
        try:
            media = status.extended_entities.get('media', [])
        except:
            media = status.entities.get('media', [])
        if(len(media) > 0):
            for i in range(len(media)):
                media_files.add(media[i]['media_url'])
    if len(media_files) == 0:
        print('The user did not post any pictures.')
        sys.exit()
    for media_file in media_files:
        wget.download(media_file)
    
name = input('Please Enter the Twitter user name(DO NOT INCLUDE "@"):')
names = '@' + str(name)
# get_all_tweets("@lm19official")
try:
    # get_all_tweets("@8POrwwRMMS8gqkJ")
    # get_all_tweets("@dsarew")
    get_all_tweets(name)
except tweepy.error.TweepError:
    print('Sorry, the user is not exist')
    sys.exit()

GOOGLE_APPLICATION_CREDENTIALS = './service-account-file.json'
client = vision.ImageAnnotatorClient()

file = open('result.txt','w')
m = 1
OBJ = []
for pic in listdir():
    if pic.endswith('jpg') or pic.endswith('png'):
        OBJ.append(pic)
print(str(len(OBJ)) + ' Pictures Found.' + '\n')
file.write(str(len(OBJ)) + ' Pictures Found.' + '\n')
os.system('ffmpeg -framerate 1 -pattern_type glob -i "*.jpg"   -c:v libx264 -r 30 -pix_fmt yuv420p 1.mpg')
os.system('ffmpeg -framerate 1 -pattern_type glob -i "*.png"   -c:v libx264 -r 30 -pix_fmt yuv420p 2.mpg')
os.system('cat 1.mpg 2.mpg | ffmpeg -f mpeg -i - -qscale 0 -vcodec mpeg4 output.mp4')
for i in OBJ:
    file_name = os.path.join(os.path.dirname(__file__),i)
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations
    # writing Picutre names and  IDs to txt.file
    print('Picture Name: ' + i + ', ID: ' + str(m))
    print(str(len(labels)) + ' objects detected.')
    print('Labels:')
    file.write('Picture Name: ' + i + ', ID: ' + str(m) + '\n')
    file.write(str(len(labels)) + ' objects detected.' + '\n')
    file.write('Labels:' + '\n')
    m = m + 1
    for label in labels:
        file.write(label.description + '\n')
        print(label.description)
    print('')
    file.write('\n')
file.close()