#Gianluca Benucci
#GTMSpider
#v. 1.0.0
#https://www.gianlucabenucci.com/#portfolio

#pyppeteer.errors.NetworkError: Protocol error Page.navigate: Target closed. Errore causato da vecchia versione di WebSocket
# Fix: From terminal pip3 install websockets==6.0 --force-reinstall

#ToDo Get Only the <head> tag from rendered page?

#Try-Except for avoid crash/error if modules are not avaible
try:
    from googlesearch import search
    from requests_html import HTMLSession
except ImportError:  
    print("Install all modules for use it")


def GTMSpider(query):
    session = HTMLSession() # Initialize HTMLSession

    #query : query string that we want to search for.
    #tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
    #lang : lang stands for language.
    #num : Number of results we want.
    #start : First result to retrieve.
    #stop : Last result to retrieve. Use None to keep searching forever.
    #pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
    #Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.

    for current_url in search(query, lang="en", num=10, start=0, stop=10, pause=15, only_standard=True):

        try:
            
            content_js = session.get(current_url) #Open session for current url
            content_js.html.render() #Render page

            rendered_html = content_js.html.html #Contenuto della pagina con js renderizzato 

            check_GTM_URL = rendered_html.find("www.googletagmanager.com/gtm.js") #Check for see if GTM url is in page
            check_GTM_ACRONYM = rendered_html.find("GTM-") #Check for see if GTM Acronym is in page
            

            if ( check_GTM_URL > 0 or check_GTM_ACRONYM > 0):
                print ("Google Tag Manager currently in use! " + current_url)
            else:
                print ("Google Tag Manager not in use! " + current_url)
                
        except:
            print ("Error while analyze this url: " + current_url)
  
#query to search on Google 
query = input("Insert query: ")

print("Start Scraping...")

GTMSpider(query)
