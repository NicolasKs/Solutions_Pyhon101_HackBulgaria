import sys
import random
import json
import os

class Song():

	def __init__(self, title, artist, album, length):
		self.title = title
		self.artist = artist
		self.album = album
		self._length = length


	def __str__(self):
		return f'{self.artist} - {self.title} from {self.album} - {self._length}'


	def __eq__(self,other):
		return self.title == other.title and self.artist == other.artist and self.album == other.album and self._length == other._length



	def __hash__(self):
		return hash((self.title,self.artist,self.album,self._length))


	def length(self, secounds = False, minutes = False , hours = False):
		dur = self._length.split(':')
		tot_len_in_sec = Song.to_secounds(dur)

		if secounds:
			return tot_len_in_sec
		elif minutes:
			return tot_len_in_sec // 60
		elif hours:
			return tot_len_in_sec // 3600
		else:
			return str(self._length)

	@staticmethod
	def to_secounds(ls):
		ls = ls[::-1]
		tot_len_in_sec = 0
		for i in range(len(ls)):
			if i == 0:
				tot_len_in_sec += int(ls[i])
			elif i == 1:
				tot_len_in_sec += int(ls[i]) * 60
			elif i == 2:
				tot_len_in_sec += int(ls[i]) * 3600
		return tot_len_in_sec


class Playlist():


	def __init__(self, name, repeat = False, shuffle = False):
		self.name = name
		self.repeat = repeat
		self.shuffle = shuffle
		self.song_list = []
		self.curr_song = 0
		self.state =0


	def _eq__(self,other):
		return self.name == other.name and self.song_list == other.song_list


	def add_song(self,song):
		for val in self.song_list:
			if val == song:
				return 'Song is already in playlist'
		self.song_list.append(song)

	def remove_song(self,song):
		for val in self.song_list:
			if val == song:
				self.song_list.remove(song)

	def add_songs(self,ls):
		for val in ls:
			self.add_song(val)

	def total_length(self):
		sums = 0
		for val in self.song_list:
			sums += val.length(secounds = True)
		hours = sums // 3600
		minutes = int((sums % 3600) / 60)
		secounds = sums % 60

		hours, minutes, secounds = Playlist.better_look(hours,minutes,secounds)

		return f'{hours}:{minutes}:{secounds}'


	def artists(self):
		dic = {}
		for val in self.song_list:
			if val.artist not in dic:
				dic[val.artist] = 1
			else:
				dic[val.artist] += 1
		return dic


	def next_song(self):
		now_curr_song = self.curr_song
		self.curr_song += 1

		if self.shuffle and self.state == 0:
			random.shuffle(self.song_list)
			self.state = 1

		if self.repeat:
			try:
				return self.song_list[now_curr_song]
			except:
				if self.shuffle:
					random.shuffle(self.song_list)
				self.curr_song = 1
				return self.song_list[self.curr_song - 1]
		else:
			try:
				return self.song_list[now_curr_song]
			except:
				raise IndexError('No more songs in playlist')

	def save(self):
		path = 'python-songlists'
		if not os.path.exists(path):
			os.makedirs(path)
		name = self.name.replace(' ','-')
		with open(os.path.join(path,f'{name}.json'),'w') as f:
			json.dump(self.unpack_songs(), f)


	def unpack_songs(self):
		songs = []
		for song in self.song_list:
			songs.append({'title' : song.title, 'artist' : song.artist, 'album' : song.album, 'length' : song._length})
		return songs

	@classmethod
	def load(cls, name):
		try:
			with open(os.path.join('python-songlists',name),'r') as f:
				data = json.load(f)
			name1 = name.replace('.json','')
			name1 = name1.replace('-',' ')
			p = cls(name1)
			p.add_songs(cls.pack_songs(data))
			return p
		except:
			raise TypeError('Wrong information')


	@staticmethod
	def pack_songs(data):
		songs = []
		for song in data:
			songs.append(Song(song["title"], song["artist"], song["album"], song["length"]))
		return songs


	@staticmethod
	def better_look(h,m,s):
		ls = [str(h),str(m),str(s)]

		for i in range(len(ls)):
			if len(ls[i]) < 2:
				ls[i] = '0' + ls[i]		
		return ls




def main():
	code_songs = Playlist(name ='Code', repeat = True, shuffle = True)
	s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:03:44")
	c = Song('Snow','RHCP','Stadium Arcadium','5:50')
	m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:25')
	
	ls = [c,m]

	print(s)
	print('secounds: ', s.length(secounds = True))
	print('minutes: ', s.length(minutes = True))
	print('hours: ', s.length(hours = True))

	code_songs.add_song(s)
	code_songs.add_songs(ls)
	code_songs.remove_song(c)
	print(code_songs.total_length())
	print(code_songs.artists())
	print(code_songs.next_song())
	print(code_songs.next_song())
	code_songs.save()
	code = Playlist.load('Code.json')
	print(code.name)



if __name__ == '__main__':
	main()