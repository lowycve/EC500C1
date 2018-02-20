Code Review:

This project is able to download a certain number of images from twitter by using tweepy api and put them all together to a video by using ffmpeg and also can get description of the images by using google vision api. The code really concerned of different kind of situations, such as searching non-exist user or try to download images from user who doesn't have uploaded any images. But it's not really easy to read, there doesn't have any description for any functions. This code passed most of the test, all the test cases are listed below.

Test Cases:

1. Non-exist username test: PASS
![alt tag](https://github.com/lowycve/EC500C1/blob/ChihWeiTung_Review/Review/nonuser_test.png)

2. No photo user test: PASS
![alt tag](https://github.com/lowycve/EC500C1/blob/ChihWeiTung_Review/Review/nonphoto_test.png)

3. Time spend test: FAILED (too slow)
![alt tag](https://github.com/lowycve/EC500C1/blob/ChihWeiTung_Review/Review/timetest.png)

4. Video create: PASS
![alt tag](https://github.com/lowycve/EC500C1/blob/ChihWeiTung_Review/Review/videotest.png)

5. Vision test: PASS![alt tag](https://github.com/lowycve/EC500C1/blob/ChihWeiTung_Review/Review/vision_test.png)

