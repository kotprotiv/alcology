import gdata.youtube
import gdata.youtube.service

#yt_service = gdata.youtube.service.YouTubeService()
yt_service.developer_key = 'AIzaSyCwO8iVRlarbi_7S7ZR9KQBvGItRcqAFrw'
yt_service.client_id = '676524909128-8tsrurmq962bnh0kr7o63emvchvjf7jq.apps.googleusercontent.com'

def GetAndPrintVideoFeed(uri):
  yt_service = gdata.youtube.service.YouTubeService()
  feed = yt_service.GetYouTubeVideoFeed(uri)
  for entry in feed.entry:
    PrintEntryDetails(entry) # full documentation for this function

def SearchAndPrint(search_terms):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = search_terms
  query.orderby = 'viewCount'
  query.racy = 'exclude'
  feed = yt_service.YouTubeQuery(query)
  PrintVideoFeed(feed)

if __name__=='__main__':
	user_search = 'котики играют в ладушки'
	print(SearchAndPrint(user_search)) 