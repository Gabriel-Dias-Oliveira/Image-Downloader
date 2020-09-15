# IMAGE DOWNLOADER

The code for this repository consists of a program that aims to automate the downloading of images (using Selenium). The program is able to search for any information that the user wants and at the end of the process it generates a .txt file with all links of the downloaded images for reference purposes.
However, it is worth mentioning that the number of images downloaded is variable.

## HOW TO USE

* Run the code through a program like VS Code or PyCharm.
* Run the code through the terminal by the code: `python image_downloader.py`.

## ATTENTION

* Make sure the Driver version your code needs. This code uses the Driver for Chrome version 85.
  * [Chrome Driver](https://chromedriver.chromium.org/), [Firefox](https://github.com/mozilla/geckodriver/releases), [Microsoft Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/), etc.
    
* Check that the Web Driver is in the same path as the code and check that the used libraries are [installed](https://selenium-python.readthedocs.io/). 
* The code does not have a fixed number of images to be downloaded, this number may vary according to the search and / or download difficulties, however these exceptions are handled by the code.
* Feel free to use the code and change it as you wish.