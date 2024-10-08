# UI Frontend Automation Test

## Project Overview
This project is designed for the [digital.auto](https://autowrx.digital.auto/) web application, but anyone can use this repo and modify the test methods to test the UI of any web pages. 

By using the end-to-end test approach, the test starts from the end user's perspective and simulates a real-world scenario. Specifically, it will perfom user's actions such as clicking, scrolling, typing,... to see if the UI web elements appear on the screen as expected.

Written in Python, this project also use the Selenium Testing Framework, a popular testing framework for UI web application.

## Repository Structure

- **setup_methods/** : This folder contains files that set up the logs, evoke the browser used for testing, and some functions that are used in the test methods folder. All the libraries that get included will also be in the *util.py* in this folder.

- **test_methods/** : This is where all the test files are. The name of each test has to start with *test_*  so that the Pytest framework can recognize the test file. The file name also represents the functionality of that test file. For example, *test_signUp.py* means it will test the sign up/register functionality.

- **logs/** : Stores log files generated by each test method. This folder must exist even if it's initially empty.

- **images/** : Stores the images that will be used during the test methods.

- **critical_error.json** : A JSON file that stores the encoded URI for all the critical errors (remember that it's for critical errors only, not warnings or normal errors). Read the *Send Emails* section below to understand why do we need this.

- **info_sample.json** : You need to provide all the information in this file so that all tests work properly. Do not forget to change the file name to *info.json* before running the test. 

- **requirements.txt** : All the libraries you need to install before running the test. Type *pip install -r requirements.txt* to install everything in this file.

- **main.py** : The entry point for running the tests. This file controls which test method files are executed. To run the project, simply type *python main.py*

## Adding New Test Methods
- Place new test files in the test-methods folder. Follow the naming convention: **test_yourTestName.py** Otherwise, the Pytest framework won't recognize the test files. 

- You should think about how to split the test files according to their functionalities. You wouldn't want to have too long test files because that will be a pain to debug.

## Log Management
- Logs are automatically generated for each test file (file that has naming convention **yourTestName.test.js.**) and saved in the **logs/** folder.
- Each test file creates its own log to prevent overly long log files. The name of the log file represents the date and time that the log is generated.

## Send Emails
We use 4 log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL in this project. 
- The DEBUG and INFO are used mainly to explain what test cases we are performing, and no emails will be sent based on these 2 levels.
- The WARNING and ERROR are used to report errors that are not urgent and can be fixed later. At the end of the *main.py*, a function will scan through the logs folder, grab all the logs that have today's date (the date that the test gets executed). That function will then check if there is any WARNING or ERROR messages, group them in a HTML and encode it. This HTML will be the content of the email that is sent to the front-end developer.
- The CRITICAL is used to report errors that are urgent and need to be fixed as soon as possible. Right after each test method is run, if there is any critical error, an email will be sent immediately (not waiting until the end of every test methods like WARNING and ERROR). It will still use HTML and encode it to make the email's content.

You can write the message that you want to be sent with HTML, then use this [link](https://www.onlinewebtoolkit.com/url-encode-decode) to encode/decode it. The *error.json* file is a good example of how you can write the HTML.


## Set Up Webdriver
To understand how the webdriver works, you can refer to this [slideshow](https://www.canva.com/design/DAGKU4ulntc/tJKLkpbAPVf0ahNYFOTx_A/edit?utm_content=DAGKU4ulntc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) (slide no.8)

1. You can install the Chrome webdriver using this [link](https://getwebdriver.com/chromedriver). 
2. Unzip the file and copy the path to the *chromedriver.exe* file, paste it in the environment variables, also paste it in the *info_sample.json* (will be renamed to info.json). 
3. Restart the computer.

## Notes and Best Practices
- To use this repo, start with cloning this repo to your working directory. Next, create an empty folder called logs,  rename the info-sample.json to info-json and fill in the information (be careful with the paths, usernames, passwords). 

- When writing the test, try to start with your experience with the webpage first (what buttons do you click, in what order) to make sure that you are simulating a real-world scenario.

- All the test methods are independent so the order doesn't matter. You can decide which file to run first simply by modifying the *main.py*

- Make sure that the number of created vehicles of the testing user is 0 before running the test.

- This project can also be used for other instances (apart from autowrx instance) such as [etas.digital.auto](https://etas.digital.auto/) and [covesa.digital.auto](https://covesa.digital.auto/). You just need to replace the web_url link in the *info.json* to indicate the instance's website you want to test.

## Tips
- You'll see that selenium still has its limitations, sometimes it sees the element, sometimes it doesn't. You might want to add the *time.sleep()* or using wait methods because when the Selenium framework does everything too fast, there won't be enough time to load elements.

- Another problem is that the Selenium can usually grab elements that is not visible on the current viewport, for example it can grab a button at the bottom of the webpage without scrolling down the page. But sometimes it can't grab it, and you might want to add the scrolling page until see element so that the script works (refer to the *click_getting_started()* function in the *actions.py* to see how did I scroll until an element is visible).

## Contact Information
Please contact my.giangvu@gmail.com if you need further assistance.
