import requests

class YoutubeAPI:

    _api_base_url   = None
    _watch_base_url = None
    _developer_key  = None
    _max_results    = None

    def __init__(self):
        self._api_base_url   = "https://www.googleapis.com/youtube/v3/"
        self._watch_base_url = "https://www.youtube.com/watch?v="
        self._developer_key  = "API_KEY"
        self._max_results    = 26

    def _get_api_base_url(self):
        return self._api_base_url

    def _get_watch_base_url(self):
        return self._watch_base_url

    def _get_developer_key(self):
        return self._developer_key

    def _get_max_results(self):
        return self._max_results

    def search_results(self, query):
        api_base_url = self._get_api_base_url()
        max_results = self._get_max_results()
        developer_key = self._get_developer_key()
        search_url = "{}search?q={}&maxResults={}&key={}".format(api_base_url, query, max_results, developer_key)
        response = requests.get(search_url)
        json = response.json()

        lists = {}
        available_videos = self._get_video_informations(json)
        organized_list = self._organized_videos_list(available_videos)

        lists["available_videos"] = available_videos
        lists["organized_list"] = organized_list

        return lists

    def _get_video_informations(self, json):
        available_videos = {}
        for video in json['items']:
            video_ids = video['id']
            if video_ids['kind'] == "youtube#video":
                video_id = video_ids['videoId']
                api_url = "{}videos?id={}&part=snippet,contentDetails&key={}".format(self._get_api_base_url(), video_id, self._get_developer_key())
                response = requests.get(api_url)
                response = response.json()
                for item in response['items']:
                    video_title = item['snippet']['localized']['title']
                    available_videos[video_title] = "{}{}".format(self._get_watch_base_url(), video_id)
            continue
        return available_videos

    def _link_title_list(self, video_informations):
        link_list = {}
        for (key, title) in enumerate(video_informations, start = 1):
            link_list[key] = title
        return link_list

    def _organized_videos_list(self, video_informations):
        organized_list = {}
        for (key, title) in enumerate(video_informations, start = 1):
            organized_list[key] = title
        return organized_list
