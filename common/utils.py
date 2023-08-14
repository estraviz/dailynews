import requests
from datetime import datetime


def getResults(url):
    results = []
    try:
        response = requests.get(url)
        json = response.json()
        for result in json["results"]:
            date_split = result["published_date"].split("T")[0]
            dict = {
                "title": result["title"],
                "section": result["section"],
                "url": result["url"],
                "createdAt": datetime.strptime(date_split, '%Y-%m-%d'),
                # "createdAt": date[0]+ "-"+date[1]+"-"+date[2],
                "author": result["byline"],
                "abstract": result["abstract"]
            }
            multimedia = result.get('multimedia')
            media = result.get('media')

            if multimedia:
                dict["thumbnail"] = result["multimedia"][2]["url"]
            elif media:
                dict["thumbnail"] = result["media"][0]["media-metadata"][1]["url"]
            else:
                dict["thumbnail"] = "https://via.placeholder.com/150"

            results.append(dict)
        return results
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
