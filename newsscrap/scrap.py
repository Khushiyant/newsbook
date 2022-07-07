import json
from urllib import response

from newsdataapi import NewsDataApiClient

from .summarizer import summarize
import yaml

# API key authorization, Initialize the client with your API key
# You can pass empty or with request parameters {ex. (country = "us")}


class scrap:
    def __init__(self, apikey):
        # api = NewsDataApiClient(apikey=apikey)
        # response = api.news_api(q = "trending" , country = "in", language="en")
        response = json.load(open("newsscrap/test.json"))
        self.data = response['results'] if response['status'] == 'success' else None

    def get_data_newsdataapi(self):
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

    def get_hindu_editorials(self):
        pass
    
    @staticmethod
    def get_name():
        return "scrap v0.1.0"

    @staticmethod
    def get_description():
        return "Scrapes the current news according to geoip2 location."


if __name__ == "__main__":
    scrap(yaml.full_load("/tmp/config.yaml")['newsdata']['api_key']).get_data()
