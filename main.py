from __future__ import print_function
import ProWritingAidSDK
from ProWritingAidSDK.rest import ApiException
from pprint import pprint

configuration = ProWritingAidSDK.Configuration()
configuration.host = 'https://api.prowritingaid.com'
configuration.api_key['licenseCode'] = '05919403-4500-45EC-8BB8-BE60F1ED41AB'

# create an instance of the API class
api_instance = ProWritingAidSDK.TextApi(ProWritingAidSDK.ApiClient('https://api.prowritingaid.com'))
sentence="""Zain is very good boy"""
print(sentence)
try:
    api_request = ProWritingAidSDK.TextAnalysisRequest(sentence,
                                                       ["grammar"],
                                                       "General",
                                                       "en")

    api_response = api_instance.post(api_request)
    # print(api_response)
    # if api_response.result and api_response.result.summaries:
    #     a = []
    #     for summary in api_response.result.summaries:
    #         if summary.summary_items:
    #             for item in summary.summary_items:
    #                 if item.category_name == 'grammargrammar' and item.num_issues > 0:
    #                     for sub_item in item.sub_items:
    #                         a.append([sub_item.sub_category])
    #     print(a)  # This will print the entire list of search terms


    # pprint(api_response)
    tags = api_response.result.tags
    print(tags)
    suggestions_2d_array = []
    a=[]  # Initialize an empty 2D array
    for tag in tags:
        suggestions = tag.suggestions
        a.append([tag.subcategory])
        suggestions_2d_array.append([suggestions[0]])  # Append each suggestion as a list with one element

    print(suggestions_2d_array)
# Assuming 'a' contains the mistake words and 'suggestions_2d_array' contains the correct words
    for mistake_word, correct_word in zip(a, suggestions_2d_array):
        mistake_word_str = mistake_word[0]
        correct_word_str = correct_word[0]
        sentence = sentence.replace(mistake_word_str, correct_word_str)

    print(sentence)  # This will print the corrected sentence

except ApiException as e:
    print("Exception when calling API: %s\n" % e)