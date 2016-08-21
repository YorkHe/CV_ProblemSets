# Problem Set 0: Images as Functions


1. Input images
- Find two interesting images to use. They should be color, rectangular in shape (NOT square). Pick one that is wide and one tall.
You might find some classic vision examples here. Or take your own. Make sure the image width or height do not exceed 512 pixels.
Output: Store the two images as ps0-1-a-1.png and ps0-1-a-2.png inside the output folder

![](https://github.com/YorkHe/CV_ProblemSets/blob/master/ps0_python/output/ps0-1-a-1.png?raw=true)
![](https://github.com/YorkHe/CV_ProblemSets/blob/master/ps0_python/output/ps0-1-a-2.png?raw=true)

2. Color planes
- Swap the red and blue pixels of image 1
    - Output: Store as ps0-2-a-1.png in the output folder

![](https://github.com/YorkHe/CV_ProblemSets/blob/master/ps0_python/output/ps0-2-a-1.png?raw=true)

- Create a monochrome image (img1_green) by selecting the green channel of image 1
    - Output: ps0-2-b-1.png

![](https://github.com/YorkHe/CV_ProblemSets/blob/master/ps0_python/output/ps0-2-b-1.png?raw=true)

- Create a monochrome image (img1_red) by selecting the red channel of image 1
    - Output: ps0-2-c-1.png

![](https://github.com/YorkHe/CV_ProblemSets/blob/master/ps0_python/output/ps0-2-c-1.png?raw=true)

- Which looks more like what you’d expect a monochrome image to look like? Would you expect a computer vision algorithm to work on one better than the other?

3. Replacement of pixels

- Take the inner center square region of 100x100 pixels of monochrome version of image 1 and insert them into the center of monochrome version of image 2
    - Output: Store the new image created as ps0-3-a-1.png


![](https://github.com/YorkHe/CV_ProblemSets/blob/master/ps0_python/output/ps0-3-a-1.png?raw=true)

4.Arithmetic and Geometric operations

- What is the min and max of the pixel values of img1_green? What is the mean? What is the standard deviation?  And how did you compute these?
    - Output: Text response, with code snippets


- Subtract the mean from all pixels, then divide by standard deviation, then multiply by 10 (if your image is 0 to 255) or by 0.05 (if your image ranges from 0.0 to 1.0). Now add the mean back in.
    - Output: ps0-4-b-1.png


![](https://github.com/YorkHe/CV_ProblemSets/blob/master/ps0_python/output/ps0-4-b-1.png?raw=true)

- Shift img1_green to the left by 2 pixels.
    - Output: ps0-4-c-1.png

![](https://github.com/YorkHe/CV_ProblemSets/blob/master/ps0_python/output/ps0-4-c-1.png?raw=true)

- Subtract the shifted version of img1_green from the original, and save the difference image.
    - Output: ps0-4-d-1.png (make sure that the values are legal when you write the image so that you can see all relative differences), text response: What do negative pixel values mean anyways?


![](https://github.com/YorkHe/CV_ProblemSets/blob/master/ps0_python/output/ps0-4-d-1.png?raw=true)

