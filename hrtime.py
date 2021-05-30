import datetime
import random
from time import sleep
from pynput import keyboard
import sys

#now 
def getQuestion(qType):
    if (qType == 0):
        s = "ABEFGHMPRTabefghmprt"
        question = s[random.randint(0,len(s)-1)]
        return question
    elif (qType == 1):
        sameOrNot = random.randint(1,2)
        s = "ABEFGHMPRTabefghmprt"
        if sameOrNot == 1:
            expectedAns = True
            char = s[random.randint(0,len(s)-1)]
            question = char + ' ' + char
            # return question, expectedAns
        elif sameOrNot == 2:
            expectedAns = False
            char1 = s[random.randint(0,len(s)-1)]
            char2 = s[random.randint(0,len(s)-1)]
            while char1 == char2:
                char2 = s[random.randint(0,len(s)-1)]
            question = char1 + ' ' + char2
            # return question, expectedAns
        return question, expectedAns
    elif (qType == 2):
        sameOrNot = random.randint(1,2)
        s = "ABEFGHMPRTabefghmprt"
        if sameOrNot == 1:
            expectedAns = True
            ranIdx = random.randint(0,len(s)-1)
            char1 = s[ranIdx]
            char2 = s[(ranIdx + len(s) // 2)%(len(s))]
            question =  char1 + ' ' + char2
            return question, expectedAns
        elif sameOrNot == 2:
            expectedAns = False
            ranIdx1 = random.randint(0,len(s)-1)
            ranIdx2 = random.randint(0,len(s)-1)
            char1 = s[ranIdx1]
            char2 = s[ranIdx2]
            while (char1 == char2 or char2 == s[(ranIdx1 + len(s) // 2)%(len(s))]):
                char2 = s[random.randint(0,len(s)-1)]
            question = char1 + ' ' + char2
            return question, expectedAns
    elif (qType == 3):
        sameOrNot = random.randint(1,2)
        if sameOrNot == 1:
            expectedAns = True
            ran1to3 = random.randin(1,3)
            if ran1to3 == 1:
                s = "ABEFGHMPRT"
                ranIdx = random.randint(0,len(s)-1)
                char1 = s[ranIdx]
                char2 = s[ranIdx]
                question =  char1 + ' ' + char2
                # return question, expectedAns
            if ran1to3 == 2:
                s = "abefghmprt"
                ranIdx = random.randint(0,len(s)-1)
                char1 = s[ranIdx]
                char2 = s[ranIdx]
                question =  char1 + ' ' + char2
                # return question, expectedAns
            if ran1to3 == 3:
                s = "!@#$%&*+=?"
                ranIdx = random.randint(0,len(s)-1)
                char1 = s[ranIdx]
                char2 = s[ranIdx]
                question =  char1 + ' ' + char2
            # return question, expectedAns
        elif sameOrNot == 2:
            s = "ABEFGHMPRTabefghmprt!@#$%&*+=?"
            expectedAns = False
            ranIdx1 = random.randint(0,len(s)-1)
            if (ranIdx1 < 10):
                ranIdx2 = 10 + random.randint(0,19)
            elif (ranIdx1 < 20):
                ranIdx2 = (20 + random.randint(0,19)) % len(s)
            else:
                ranIdx2 = random.randint(0,19)
            char1 = s[ranIdx1]
            char2 = s[ranIdx2]
            question = char1 + ' ' + char2
            # return question, expectedAns
        return question, expectedAns
def resultToCsvFormat(time, qType, question, expectedAns, qAns):
    if qType == 0:
        s = '' + str(time) + ',' + str(qType) + ',"' + question + '",,,'
    else:
        s = '' + str(time) + ',' + str(qType) + ',"' + question \
            + '",,,' + str(expectedAns) + ',' + str(qAns) + ',' + \
                str((expectedAns == qAns))
    return s

def writeToCsv(resultArr, qType):
    if qType == 0:
        nameOfFile = 'simpleReactionResult.csv'
    elif qType == 1:
        nameOfFile = 'physicalMatchingResult.csv'
    if qType == 2:
        nameOfFile = 'nameMatchingResult.csv'
    if qType == 3:
        nameOfFile = 'categoryMatchingResult.csv'
    with open(nameOfFile, 'w') as f:
        if qType == 0:
            f.write('time, qType, question, expectedAns, qAns')
            f.write('\n')
        else:
            f.write('time, qType, question, expectedAns, qAns')
            f.write('\n')
        for line in resultArr:
            f.write(line)
            f.write('\n')

def readKeyboardInput(qType, question):
    if qType == 0:
        sleep(random.randint(1,4))
        print(question)
        tic = datetime.datetime.now()
        with keyboard.Events() as events:
            event = events.get(1e6)
            #block as much as possible
            # if event.key == keyboard.KeyCode.from_char('f'):
            if event.key == keyboard.Key.space:
                toc = datetime.datetime.now()
                # print(f"key pressed was{event.key}")
                qAns = True
            else:
                print(f"ERROR, you pressed an invalid key, key pressed was {event.key}")
                sys.exit()
            print("#------------------------------------#")

    else:
        sleep(random.randint(1,4))
        print(question)
        tic = datetime.datetime.now()
        with keyboard.Events() as events:
            event = events.get(1e6)
            #block as much as possible
            # if event.key == keyboard.KeyCode.from_char('f'):
            if event.key == keyboard.Key.space:
                toc = datetime.datetime.now()
                # print(f"key pressed was{event.key}")
                qAns = True
            # elif event.key == keyboard.KeyCode.from_char('j'):
            if event.key == keyboard.Key.enter:
                toc = datetime.datetime.now()
                # print(f"key pressed was{event.key}")
                qAns = False
            else:
                print(f"ERROR, you pressed an invalid key, key pressed was {event.key}")
                sys.exit()

        print("#------------------------------------#")

    time = getTime(tic, toc)
    return time, qAns

def getTime(tic, toc):
    delta = toc - tic
    ti = int(delta.total_seconds() * 1000) # miliseconds
    me = str(ti) + "ms"
    return me

def printRules(qType):
    if qType == 0:
        print("Press SPACE when a letter shows up")
    if qType == 1:
        print("########CASE SENSITIVE########")
        sleep(1)
        print("Press SPACE if the two letters are the same , press ENTER if they're not")
        sleep(1)
        print("ready.....")
        sleep(1)
        print("START")
    if qType == 2:
        print("########NOT CASE SENSITIVE########")
        sleep(1)
        print("Press SPACE if the two letters are the same , press ENTER if they're not")
        sleep(1)
        print("ready.....")
        sleep(1)
        print("START")
    if qType == 3:
        print("########TYPE refers to if they're either UPPER CASE, lower case, or SYMBOLS(!@#$)########")
        sleep(2)
        print("Press SPACE if the two letters are the same TYPE , press ENTER if they're not")
        sleep(2)
        print("ready.....")
        sleep(1)
        print("START")
    pass

if __name__ == "__main__":
    qType = int(input("Select question type (from 1 to 4)")) - 1 #from 0 to 3 (Questions 1 to 4)
    resultCsvArr = []
    N = int(input("How many times do you want to repeat each test?")) #回数
    printRules(qType)
    for i in range(N):
        if qType == 0:
            question = getQuestion(qType)
            time, qAns = readKeyboardInput(qType, question)
            s = resultToCsvFormat(time, qType, question, ',,,',',,,')
            resultCsvArr.append(s)
        else:
            question, expectedAns = getQuestion(qType)
            time, qAns = readKeyboardInput(qType, question)
            s = resultToCsvFormat(time, qType, question, expectedAns, qAns)
            resultCsvArr.append(s)
    writeToCsv(resultCsvArr, qType)