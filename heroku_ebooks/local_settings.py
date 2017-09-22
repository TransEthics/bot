'''
Local Settings for a heroku_ebooks account. TransEbooks
'''

#configuration
MY_CONSUMER_KEY = 'I6pSkDy9hAgGGiPBaQcXzeod6'
MY_CONSUMER_SECRET = 'BG6monvOpbCgcEVPXgsXGBLMmV52UViK5T7OASbLBj1ATqmCYo'
MY_ACCESS_TOKEN_KEY = '910910733730193409-KpWg2dynJSWRrx8z6yvKF3JDUlMU2Es'
MY_ACCESS_TOKEN_SECRET = '26CugSkJcirRkneJE1g7DlLLcidcc5DuNNWxqOtDQ9Ia8'

SOURCE_ACCOUNTS = ["ThatSabineGirl", "GuildingLilly", "cosmos_cookie", "lilylayer4", "SadieSatanas", "Mythic_Memory", "every_lesbian", "TransEthics"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 3 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = "testcorpus.txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "TransEbooks" #The name of the account you're tweeting to.
