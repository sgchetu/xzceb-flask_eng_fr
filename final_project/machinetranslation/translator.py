import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)


language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/857beec2-b295-447e-87b5-d57e4f375b2a')

def english_to_french(english_text):
    """trnslate English to French"""
    frenchtranslation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return frenchtranslation.get("translations")[0].get("translation")
	

def french_to_english(french_text):
    """trnslate English to French"""
    englishranslation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return englishranslation.get("translations")[0].get("translation")
	
