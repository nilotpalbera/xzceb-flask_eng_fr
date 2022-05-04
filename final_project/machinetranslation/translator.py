'''Code for machine language translation'''
import json
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

language_translator.set_service_url(url)

def englishToFrench(englishText):
    '''Function to convert english text to french'''
    #write the code here
    translation_response = language_translator.translate(text = englishText, model_id = 'en-fr').get_result()
    translation_str = json.dumps(translation_response)
    translation_dict = json.loads(translation_str)
    frenchText = translation_dict['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    '''Function to convert french text to english'''
    #write the code here
    translation_response = language_translator.translate(text = frenchText, model_id = 'fr-en').get_result()
    translation_str = json.dumps(translation_response)
    translation_dict = json.loads(translation_str)
    englishText = translation_dict['translations'][0]['translation']
    return englishText
