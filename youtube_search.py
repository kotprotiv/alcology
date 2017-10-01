#coding=UTF-8
import requests


def get_info(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('что-то не так'+'код ошибки: '+str(result.status_code))


def youtube_search(search_text):
    api_key = 'AIzaSyCwO8iVRlarbi_7S7ZR9KQBvGItRcqAFrw'
    url = "https://content.googleapis.com/youtube/v3/search?part=snippet&type=video&key=%s&q=%s" % (api_key, search_text)

    search_result = get_info(url)
    video_url = []
    for video in search_result['items']:
        video_id = video['id']['videoId']
        video_url.append('https://www.youtube.com/embed/{}'.format(video_id))
    return video_url
