from urllib import response
from newsdataapi import NewsDataApiClient
import json
# API key authorization, Initialize the client with your API key
# You can pass empty or with request parameters {ex. (country = "us")}


class scrap:
    def __init__(self, apikey):
        # api = NewsDataApiClient(apikey=apikey)
        # response = api.news_api(q = "trending" , country = "in", language="en")
        response = json.load(open("newsscrap/test.json"))
        self.data = response['results'] if response['status'] == 'success' else None

    def get_data(self):
        # return self.data
        context = {
            'post_data': []
        }
        for dt in self.data:
            try:
                context['post_data'].append((dt['keywords'][0] if dt['keywords'] is not None else "Top", dt['pubDate'] if dt['pubDate'] is not None else "None", dt['title']
                                            if dt['title'] is not None else "None", dt['description'] if dt['description'] is not None else "None", dt['image_url'] if dt['image_url'] is not None else "None", dt['link'] if dt['link'] is not None else "None"))
            except Exception as e:
                print(e)
        return context

    @staticmethod
    def get_name():
        return "scrap v0.1.0"

    @staticmethod
    def get_description():
        return "Scrapes the current news according to geoip2 location."


if __name__ == "__main__":
    # http://news.google.com/news?q=apple&output=rss Google RSS feed
    scrap("pub_86308d85a19dd4b6ec10c5f34bcdd4fa9704").get_data()
