'''EN-FR translation service powered by IBM Watson'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-08-05',
    authenticator=authenticator
)

language_translator.set_service_url(url)



def english_to_french(english_text):
    '''EN-FR Translate'''
    french_text = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    return french_text


def french_to_english(french_text):
    '''FR-EN Translate'''
    english_text = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    return english_text
