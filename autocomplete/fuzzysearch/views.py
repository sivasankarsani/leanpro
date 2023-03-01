from django.shortcuts import render
import json
from django.http import JsonResponse
from django.template import loader
from .helper_methods import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    '''
    @param request
    @type dict
    Testng the Django Server
    '''

    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# write api to search the given word
def search_word(request):
    """
    @param: request
    @type: dict
    
    @rtype dict as json_format

    1. Get the require kwargs from request
    2. Validating given word
    3. Get the dataset data for searching word
    4. Apply default filter or given filter
    5. Extracted all matched_words(contains words)
    6. Filter best matched words based on given word
    7. Return response

    """
    #1. Get the require kwargs from request
    if request.method=='GET':
        word = request.GET.get('word','')
        limit= request.GET.get('limit',25)

    # if request.method=='POST':
    #     word = request.POST.get('word','')
    #     limit= request.POST.get('limit',25)

    default_json_resp = {
            "status": False,
            "err_msg": "Unable to find the fuzzysearch for given word: {}".format(word)
        }

    '''
    if given word is not valide_query, return failed response
    #2. Validating given word
    '''
    if validator_string(word):
        return JsonResponse(default_json_resp, safe=False)

    #3. Get the dataset data for searching word
    data = get_dataset()

    if not data.get('status'):
        return JsonResponse(data, safe=False)
    '''
    #4. Apply default filter or given filter
    fetch/ convert into query on demad
    '''
    query = apply_default_filters(word, limit)

    # to store the all matching words for given query
    matched_words = []

    # 5. Extracted all matched_words(contains words)
    for _word in data.get('all_possible_match_words',[]):
        if query['match_word'] in _word[0]:
            matched_words.append(_word)

    #if no single word matches
    if not matched_words or len(matched_words)==0:
        default_json_resp["is_not_found"] = "Yes"
        return JsonResponse(default_json_resp)

    #6. Filter best matched words based on given word
    best_words_list = filter_best_matched_words(matched_words, query['limit'])

    #7. return response
    return JsonResponse(best_words_list, safe=False)

