# Import Package
import os as os
import time as time
import selenium as selenium
import random as random
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Set Browser Kernel
driver = webdriver.Chrome()

# Input web page address
url = 'https://udify.app/chat/iP0yw8HbPFeD6XzL'
driver.get( url )
time.sleep( 3 )
# driver.close()

# Input Prompt
def input_prompt():
    ## Ergodic file to search 'Prompt + *  .csv'
    filename = []
    for filenameTem in os.listdir():
        if filenameTem.startswith( 'Prompt' ) and filenameTem.endswith( '.csv' ):
            filename.append( filenameTem )

    promptList = dict()
    for i1 in filename:
        promptList[ i1.split( '.' )[0] ] = pd.read_csv( i1 )

    return promptList

promptList = input_prompt()

def game_loop(
        languageSet: str
):
    for i1 in promptList.keys():
        # Set OptionList
        optionList = {
            'language': (
                '中文',
                'English'
            )
        }
        # Set 'language'
        language = driver.find_element(
            By.XPATH,
            '//div[@class="flex mb-3 last-of-type:mb-0 text-sm text-gray-900 false"]'
        )
        language.click()

        if not languageSet in optionList[ 'language' ]:
            ## Set 'Language' by random
            XPATHtem = '//div[@title="' + optionList['language'][random.randint(0,1)] + '"]'

        else:
            ## Set 'language' by User inputing
            XPATHtem = '//div[@title="' + languageSet + '"]'

        language = driver.find_element(
            By.XPATH,
            XPATHtem
        )
        language.click()
        time.sleep( 3 )

        # Start Chat
        startChat = driver.find_element(
            By.XPATH,
            '//div[@class="btn btn-primary px-4 py-0 h-9 ml-[136px]"]'
        )
        startChat.click()
        time.sleep( 10 )

        for i2 in promptList[ i1 ].loc[ :, 'Prompt' ]:
            ## Input Prompt in inputBox and send the message
            inputBox = driver.find_element(
                By.XPATH,
                '//textarea[@style="resize: none; height: 34px;"]'
            )
            inputBox.send_keys( i2 )
            inputBox.send_keys( Keys.RETURN )
            time.sleep( 9 )

        # Go back to New Chat
        newChat = driver.find_element(
            By.XPATH,
            '//div[@class="btn btn-default justify-start px-3 py-0 w-full h-9 text-sm font-medium text-primary-600"]'
        )
        newChat.click()

game_loop( '中文' )