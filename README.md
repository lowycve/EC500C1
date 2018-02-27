# EC500C1
# General Idea
Basically, this API is the combination usage of tweepy, FFMPEG and Google Vision, which is able to download the pictures of a certain Twitter user, then convert them into video, and obtain the detected labels of objects in the picture by Google Vison.

# Navigator
The code folder contains the code that use to solve this problem, and result.txt is the result generated by the code. The Pictures folder contains the pictures downloaded from Twitter User'@Yuchen310', and there are 3 videoes in the video folder, the 2 .mpg file is the video generated at first by .jpg and .png file seperatly, and the .mp4 file is the final video generated whose framerate is 1 fps(can be changed). The API_Test folder contains 3 different test programs.

# How to run the code
To run the code, you need to fill in your twitter account information at the begining of the code, then install google cloud package, obtain a json file that contains your google account information and download google cloud sdk. Make sure include the json file in the same directory as your code.
When everything is done, type 'python api.py' in terminal, and type the twitter user name you want to search for. The pictures will atuomatically download to your folder and the result.txt will also been generated.

# Features
1. When the user name you typed is not exsit, or there is no tweet, picture for the user, the program will tell you which situation happened and shut down.

**No Tweet**:
<img width="569" alt="no tweet" src="https://user-images.githubusercontent.com/31743714/35995720-42cbed8a-0ce2-11e8-9dff-8fd06b9f1460.png">

**Not exist**:
<img width="567" alt="not exist" src="https://user-images.githubusercontent.com/31743714/35995775-64fb0ad0-0ce2-11e8-8e3e-d965e08e0ef3.png">

**No picture**:
<img width="570" alt="no picture" src="https://user-images.githubusercontent.com/31743714/35995794-724ae318-0ce2-11e8-827a-48dd696a822b.png">

2. The Twitter user may upload both png and jpg picture, we need to first create the video seperately and then combine the 2 videos together.

3. The api ask the user if they want to delete the photos or the videos after detection.

4. The api.py allows the user to input multiple Twitter username using a .txt file, after finishing running, it will generate a result.txt file starting with the username. However, the .txt file should contain a username which is 'quit' to stop the program.

# Test
**Test 1:**
This test is design to test the speed of retriving data. The requirement of passing the test is 15 seconds, below is the result of running the test program.
<img width="571" alt="screen shot 2018-02-26 at 3 20 12 pm" src="https://user-images.githubusercontent.com/31743714/36705586-f4716682-1b33-11e8-99aa-0e3785e8f6a4.png">
**Test 2:**
This test aims to test the error handler, more specfic, testing the wrong username. If the user enter an unvalid user name that is not exsit, testing program will check if the api program could raise the error and output the error information. Below is the result.
<img width="569" alt="screen shot 2018-02-26 at 7 59 10 pm" src="https://user-images.githubusercontent.com/31743714/36705691-783463d4-1b34-11e8-81ee-0ef31aa4d681.png">
**Test 3:**
This test aims to test if the program could generate the txt.file and mp4.file correctly, before running the program, test program will delete all the txt.file and mp4.file so that it could test only the file that the api program generates. Below is the result.
<img width="571" alt="screen shot 2018-02-26 at 3 49 03 pm" src="https://user-images.githubusercontent.com/31743714/36706004-e5dafcc6-1b35-11e8-9d3f-8db831d81b3b.png">
