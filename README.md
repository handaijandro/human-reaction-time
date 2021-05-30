# Human reaction time

CLI App to measure human reaction time using 4 different tests.

## Description

You have 4 different tests, that use combinations of UPPER CASE LETTERS, lower case letters, and $ymb0ls.
- ### Simple reaction test: 
A single character is displayed at random, at random intervals. When the character is displayed, press the "SPACE" key. The time between the display and the
pressing of the key is measured 100 times. In this experiment, uppercase and lowercase alphabets were used.
- ### Physical matching test:
Two characters are displayed at random, at random intervals. When they are displayed, press the 'SPACE' key if the two letters are identical, or the 'ENTER' key if
they are different. This experiment is case-sensitive. The time between the display and the key being pressed is measured 100 times. 
In this experiment we used uppercase and lowercase alphabets. The probability of being the same and the probability of being different is set to 1:1.
- ### Name matching test:
Two characters are displayed at random, at random intervals. When they are displayed, press the 'SPACE' key if the two letters are identical, 
or the 'ENTER' key if they are different. This experiment is not case-sensitive. The time between the display and the key being pressed is measured 100 times.
In this experiment we used both upper and lower case letters. The probability of being the same and the probability of being different is set to 1:1.
- ### Category matching test:
Two characters are displayed at random, at random intervals. When they appear, press the "SPACE" key if the two letters are BOTH either upper case, lower case or 
symbolic, otherwise press the "ENTER" key. The time between the display and the key being pressed is measured 100 times. In this experiment, we used uppercase 
and lowercase alphabets and symbols. The probability of uppercase letters, lowercase letters and symbols being one to one and the probability of them not
being one to one was kept at 1:1.

## Getting Started

### Dependencies

* run ```pip install -r requirements.txt``` after cloning the repository.

### Installing 

* Run ```git clone https://github.com/handaijandro/human-reaction-time.git``` to clone the repository.
* After cloning, run (if possible in a virtual environment) ```pip3 install -r requirements.txt``` to install the necessary dependencies.

### Executing program

* After installing the dependencies, just run ```python3 hrtime.py```
* Select question type from (1-4)
* Follow the on-terminal instructions
* After you're done, csv files for each test type (1-4) with the test info are saved on the same directory.



## Author
Alejandro Ramos



## Acknowledgments
This is part of an experiment I did on a class called "人間情報工学”
