# made by Revan on the 11/23/2024 

from requests import get
import json
import click

# ===== Initialize usefull variables =====

URL = []
BASE_URL = "https://web.archive.org/web/timemap/json?url={}&matchType=prefix&collapse=urlkey&output=json&fl=original,mimetype,timestamp,endtimestamp,groupcount,uniqcount&filter=!statuscode:[45]..&limit=10000&_=1732319682048"
BASE_URL2 = "https://web.archive.org/web/"

# ===== Proceed to scrapping =====

def handle(url : str) -> list: 
    print(f"[STATUS] start scrapping : {url}")
    req = get(BASE_URL.format(url))
    z = json.loads(req.text)
    n = 0

    for _ in z : 
        if z[n][0] == 'original' : 
            n+=1
            continue
        else : 
            search = z[n][0]
            ids = z[n][3]
            if search : 
                URL.append(BASE_URL2+""+ids+"/"+search)
                n+=1
            else : 
                n+=1

    print(f"[CONSOLE] Successfully scrapped {len(URL)} urls")
    return URL

# ===== Save the urls =====

@click.command()
@click.argument('url')
def main(url : str) :
    with open('results.txt' , 'a+') as f :
        for y in handle(url) : 
                f.write(y+"\n")
    
    print("[CONSOLE] saved to results.txt")

if __name__ == "__main__" : 
    main()