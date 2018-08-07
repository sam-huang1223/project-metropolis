# TODO given list of comsoc names, scrape their events from fb

from config import USER_ACCESS_TOKEN

import facebook

def test_scraping():
    graph = facebook.GraphAPI(access_token=USER_ACCESS_TOKEN, version = 2.7)
    events = graph.request('me?fields=id,name')
    print(events)

    # TODO how to get all events shared to group??
    # go through this process to use groups api https://developers.facebook.com/docs/groups-api#app-review
    # https://developers.facebook.com/tools/explorer to experiment with graph api