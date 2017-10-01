#coding=UTF-8
import requests

def get_info(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('что-то не так'+'код ошибки: '+str(result.status_code))


if __name__ == "__main__":
	#api_key = 'AIzaSyD-a9IF8KKYgoC3cpgS-Al7hLQDbugrDcw'
	api_key = 'AIzaSyCwO8iVRlarbi_7S7ZR9KQBvGItRcqAFrw'
	search_text = 'котики'

	url = "https://content.googleapis.com/youtube/v3/search?part=snippet&type=video&key=%s&q=%s" % (api_key, search_text)

	info_json = get_info(url)

	for row in info_json['items']:
		video_id = row['id']['videoId']
		print(video_id)