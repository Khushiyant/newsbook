import json
import requests
import bs4
from newsdataapi import NewsDataApiClient

from summarizer import summarize
import os

# API key authorization, Initialize the client with your API key
# You can pass empty or with request parameters {ex. (country = "us")}


class scrap:
    @staticmethod
    def get_name():
        return "scrap v0.2.0"

    @staticmethod
    def get_description():
        return "Scrapes the current news according to geoip2 location and hindu editorials"

    def __init__(self, apikey: str):

        # api = NewsDataApiClient(apikey=apikey)
        # response = api.news_api(q = "trending" , country = "in", language="en")
        response = json.load(open("newsscrap/test.json"))
        self.data = response['results'] if response['status'] == 'success' else None

        # Hindu Editorial Data

    def get_data_newsdataapi(self) -> dict:
        # return self.data
        context = {
            'post_data': []
        }
        for dt in self.data:
            try:
                context['post_data'].append((dt['keywords'][0] if dt['keywords'] is not None else "Top", dt['pubDate'] if dt['pubDate'] is not None else "None", dt['title']
                                            if dt['title'] is not None else "None", dt['description'] if dt['description'] is not None else summarize.summary(dt['content']).getsummary(), dt['image_url'] if dt['image_url'] is not None else "None", dt['link'] if dt['link'] is not None else "None"))
            except Exception as e:
                print(e)
        return context

    def get_hindu_editorials(self) -> dict:

        r = requests.get("https://www.thehindu.com/opinion/editorial/")
        self.soup = bs4.BeautifulSoup(r.text, "html.parser")
        links = []
        context = {
            'editorials': []
        }

        for div in self.soup.find_all("div", {"class": "ES2-100x4-text1 hover-icon"}):
            links.append(div.find("a")['href'])

        for link in links:
            r = requests.get(link)
            soup = bs4.BeautifulSoup(r.text, "html.parser")
            article = soup.find("div", {"class": "article"})

            title = article.find("h1").text
            desc = article.find("h2").text
            content = article.find(
                "div", id=lambda x: x and x.startswith('content-body-')).text
            context['editorials'].append((title, desc, content))
        return context

    def get_upcoming_exams(self):
        context = {}
        r = requests.get(
            "https://www.embibe.com/exams/upcoming-government-exams/")
        soup = bs4.BeautifulSoup(r.text, "html.parser")

        data = []
        table = soup.find("table")
        for tr in table.find_all("tr"):
            data.append(tr)
        context['exams'] = data
        return context


if __name__ == "__main__":
    print(scrap(os.getenv("API_KEY")).get_upcoming_exams())
