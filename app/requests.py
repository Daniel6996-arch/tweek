import urllib.request,json
from .models import Quote


# Getting the base URL
#base_url = None

#def configure_request(app):
    #global base_url
    #base_url = app.config['RANDOM_QUOTES_BASE_URL']
    

def get_quote():
    '''
    Function that gets the json response to our url request
    '''
    
    get_quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = None  #replacable with []

        if get_quote_response:
            quote_results_list = get_quote_response
            quote_results = process_quote(quote_results_list)


    return quote_results

def process_quote(quote_list): #quote_url
    '''
    Function  that processes the quote result and transform them to a list of Objects

    Args:
        quote_list: A list of dictionaries that contain quote details

    Returns :
        quote_results: A list of quote objects
    '''
   
    quote_results = [] 
    for quote_item in quote_list:
       
        author = quote_item.get('author')
        id = quote_item.get('id')
        quote = quote_item.get('quote')
        permalink = quote_item.get('permalink')

        quote_object = Quote(author,id,quote,permalink)
        quote_results.append(quote_object)

    return quote_results    