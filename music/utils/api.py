import requests
from builtins import str

default_timeout = 10

class NetEase(object):
	def __init__(self):
		self.header = {
			'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/',
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'  # NOQA
		}
		self.cookies = {
			'appver': '1.5.2'
		}
		self.session = requests.Session()

	def httpRequest(self, method, url, query = None, timeout = default_timeout):
		text = self[method](url, query, timeout)
		return text

	def get(self, url, query = None, timeout = default_timeout):
		response = self.session.get(url, params = query, headers = self.header, 
			timeout = timeout)

		response.encoding = 'UTF-8'
		return response.json()

	def post(self, url, query = None, timeout = default_timeout):
		response = self.session.post(url, data = query, headers = self.header, 
			timeout = timeout)

		response.encoding = 'UTF-8'
		return response.json()

	# 获取（最热或者最新）歌单列表
	def playlists(self, order, cat, limit, offset):
		url = 'http://music.163.com/api/playlist/list?order={}&cat={}&limit={}&offset={}'.format(order, cat, limit, offset)
		try:
			result = self.get(url)
			# print(result)
			return result
		except requests.exceptions.RequestException as e:
			print(e)
			return {}

	# 获取歌单详情
	def playlist_detail(self, id):
		url = 'http://music.163.com/api/playlist/detail?id={}'.format(id)
		try:
			result = self.get(url)
			return result['result']
		except requests.exceptions.RequestException as e:
			print(e)
			return {}

	# 获取歌曲详情，多个歌曲id会返回多个歌曲详情
	def songs_detail(self, ids):
		id_list = map(str, ids)
		url = 'http://music.163.com/api/song/detail/?ids=[{}]'.format(','.join(id_list))
		try:
			result = self.get(url)
			return result['songs']
		except requests.exceptions.RequestException as e:
			print(e)
			return []

	# 获取歌曲评论，首页的歌曲评论会带有该歌曲的热评评论
	def song_comments(self, music_id, offset = 0, limit = 10, total = 'fasle'):
		url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}/?rid=R_SO_4_{}&\
            offset={}&total={}&limit={}'.format(music_id, music_id, offset, total, limit)

		try:
		    result = self.get(url)
		    return result
		except requests.exceptions.RequestException as e:
		    print(e)
		    return {}

ne = NetEase()

if __name__ == '__main__':
	# ne = NetEase()
	# ne.song_comments(354593)
	ne.songs_detail([354593])