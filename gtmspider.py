#Gianluca Benucci
#GTMSpider
#v. 1.0.0
#https://www.gianlucabenucci.com/#portfolio

#pyppeteer.errors.NetworkError: Protocol error Page.navigate: Target closed. Errore causato da vecchia versione di WebSocket
# Fix: Da terminale pip3 install websockets==6.0 --force-reinstall

#Try-Except per evitare che sollevi errori se non sono stati installati i moduli necessari

#ToDo Translate comments
try:
    from googlesearch import search
    from requests_html import HTMLSession
except ImportError:  
    print("Installa tutti i moduli per avviarlo")
  
#query da cercare 
query = "search term here"

session = HTMLSession() # Inizializzo HTMLSession
  
for current_url in search(query, lang="it", num=10, start=0, stop=10, pause=15, only_standard=True):

    try:
        content_js = session.get(current_url) #Apro la sessione per url corrente
        content_js.html.render() #Renderizzo la pagina

        rendered_html = content_js.html.html #Contenuto della pagina con js renderizzato

        check_GTM_URL = rendered_html.find("www.googletagmanager.com/gtm.js") #Check utilizzati per vedere se GTM è presente
        check_GTM_ACRONYM = rendered_html.find("GTM-") #Check utilizzati per vedere se GTM è presente

        #print (check_GTM_URL)
        #print (check_GTM_ACRONYM)

        if ( check_GTM_URL > 0 or check_GTM_ACRONYM > 0):
            print ("Google Tag Manager in uso! " + current_url)
        else:
            print ("Google Tag Manager non in uso! " + current_url)
    except:
        print ("Errore in esecuzione: " + current_url)
