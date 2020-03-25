import unittest
from playlist import Song, Playlist


class TestSong(unittest.TestCase):
	
	def test_if_class_can_be_initialized(self):
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")


	def test_if_str_representation_is_as_expected(self):
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")


		self.assertEqual(str(s),'Manowar - Odin from The Sons of Odin - 3:44')


	def test_if_eq_is_workign_as_expected(self):
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		p = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		

		self.assertEqual(s,p)

	def test_if_hash_is_working_as_expected(self):
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")

		self.assertTrue(hash(s))

	def test_if_lenght_is_being_converted_to_all_vals(self):
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="2:03:44")

		res1 = s.length(secounds = True)
		res2 = s.length(minutes = True)
		res3 = s.length(hours = True)
		res4 = s.length()

		self.assertEqual(res1, 7424)
		self.assertEqual(res2, 123)
		self.assertEqual(res3, 2)
		self.assertEqual(res4, '2:03:44')

	def test_if_to_secounds_is_working(self):
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="2:03:44")
		dur = s._length.split(':')


		self.assertEqual(s.to_secounds(dur),7424)

class TestPlaylist(unittest.TestCase):

	def test_if_playlist_can_be_initialized(self):

		code_songs = Playlist(name="Code", repeat=True, shuffle=True)

	def test_if_songs_can_be_added_to_Playlist(self):
		code_songs = Playlist(name="Code", repeat=True, shuffle=True)
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')

		code_songs.add_song(s)
		code_songs.add_song(c)

		self.assertEqual(code_songs.song_list[0],s)
		self.assertEqual(code_songs.song_list[1],c)

	def test_if_adding_an_already_existing_song_in_Playlist_returns_a_reminder(self):
		code_songs = Playlist(name="Code", repeat=True, shuffle=True)
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')

		code_songs.add_song(s)
		

		self.assertEqual(code_songs.add_song(s),'Song is already in playlist')

	def test_if_remove_song_removes_sepcific_song_from_Playlist(self):
		code_songs = Playlist(name="Code", repeat=True, shuffle=True)
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:26')

		code_songs.add_song(s)
		code_songs.add_song(c)
		code_songs.add_song(m)
		code_songs.remove_song(s)

		self.assertEqual(code_songs.song_list[0],c)
		self.assertEqual(code_songs.song_list[1],m)

	def test_if_a_list_of_songs_can_be_added_to_Playlist(self):
		code_songs = Playlist(name="Code", repeat=True, shuffle=True)
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:26')

		ls = [s,c,m]

		code_songs.add_songs(ls)
		
		self.assertEqual(code_songs.song_list,ls)

	def test_if_total_length_works(self):
		code_songs = Playlist(name="Code", repeat=True, shuffle=True)
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:25')

		ls = [s,c,m]

		code_songs.add_songs(ls)

		res = code_songs.total_length()

		self.assertEqual(res,'00:13:59')


	def test_if_artists_works(self):
		code_songs = Playlist(name="Code", repeat=True, shuffle=True)
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:25')

		ls = [s,c,m]

		code_songs.add_songs(ls)

		res = code_songs.artists()

		self.assertEqual(res,{'Manowar' : 1, 'RHCP' : 2})


	def test_if_next_song_is_working_without_repeat_or_shuffle(self):
		code_songs = Playlist(name="Code")
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:25')

		ls = [s,c,m]

		code_songs.add_songs(ls)

		res1 = code_songs.next_song()
		res2 = code_songs.next_song()

		self.assertEqual(res1,s)
		self.assertEqual(res2,c)

	def test_if_next_song_gives_error_if_song_list_ends_with_repeat_and_shuffle_off(self):

		code_songs = Playlist(name="Code")
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:25')
		err = None
		ls = [s,c,m]

		code_songs.add_songs(ls)

		code_songs.next_song()
		code_songs.next_song()
		code_songs.next_song()

		try:
			code_songs.next_song()
		except Exception as exc:
			err = exc

		self.assertIsNotNone(err)
		self.assertEqual(str(err),'No more songs in playlist')

	def test_if_next_song_starts_from_beggining_if_repeat_is_on_still_shuffle_off(self):
		code_songs = Playlist(name="Code", repeat=True)
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:25')
		ls = [s,c,m]

		code_songs.add_songs(ls)

		code_songs.next_song()
		code_songs.next_song()
		code_songs.next_song()

		self.assertEqual(code_songs.next_song(),s)

	def test_if_next_song_works_with_suffle_and_repeat_on(self):
		code_songs = Playlist(name="Code", repeat=True, shuffle = True)
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:25')
		ls = [s,c,m]

		code_songs.add_songs(ls)

		# Nikakva ideq kak da tesvam random.shuffle no raboti
		# print(code_songs.next_song())
		# print(code_songs.next_song())
		# print(code_songs.next_song())
		# print(code_songs.next_song())
		# print(code_songs.next_song())
		# print(code_songs.next_song())

	def test_if_next_song_works_with_suffle_only(self):
		code_songs = Playlist(name="Code", shuffle = True)
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:25')
		ls = [s,c,m]

		code_songs.add_songs(ls)

		# Nikakva ideq kak da tesvam random.shuffle no raboti
		# print(code_songs.next_song())
		# print(code_songs.next_song())
		# print(code_songs.next_song())

	def test_if_unpack_songs_is_working(self):
		code_songs = Playlist(name="Code", shuffle = True)
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:25')
		ls = [s,c,m]

		code_songs.add_songs(ls)
		
		res = code_songs.unpack_songs()	

		exc = [{'title': 'Odin', 'artist': 'Manowar', 'album': 'The Sons of Odin', 'length': '3:44'}, {'title': 'Snow', 'artist': 'RHCP', 'album': 'Stadium Arcadium', 'length': '5:50'}, {'title': 'Under the Bridge', 'artist': 'RHCP', 'album': 'Blood Sugar Sex Magik', 'length': '4:25'}]

		self.assertEqual(res,exc)

	def test_if_save_creates_a_new_file_with_playlist_name_and_songs_there(self):
		code_songs = Playlist(name="Code Imam1", shuffle = True)
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:25')
		ls = [s,c,m]

		code_songs.add_songs(ls)

		code_songs.save()

		#ne sum siguren kak da proverq dannite

	def test_if_load_works(self):
		code_songs = Playlist(name="Code Imam", shuffle = True)
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:25')
		ls = [s,c,m]

		code_songs.add_songs(ls)
		code_songs.save()

		code = Playlist.load("Code-Imam.json")
		
		self.assertEqual(str(code.name), 'Code Imam')
		self.assertEqual(code.song_list,code_songs.song_list)


	def test_if_packing_songs_works(self):
		code_songs = Playlist(name="Code Imam")
		s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		c = Song('Snow','RHCP','Stadium Arcadium','5:50')
		m = Song('Under the Bridge','RHCP','Blood Sugar Sex Magik','4:25')
		ls = [s,c,m]
		code_songs.add_songs(ls)
		data = [{"title": "Odin", "artist": "Manowar", "album": "The Sons of Odin", "length": "3:44"}, {"title": "Snow", "artist": "RHCP", "album": "Stadium Arcadium", "length": "5:50"}, {"title": "Under the Bridge", "artist": "RHCP", "album": "Blood Sugar Sex Magik", "length": "4:25"}]

		res = code_songs.pack_songs(data)
		
		exp = code_songs.song_list


		self.assertEqual(res,exp)

		
if __name__ == '__main__':
	unittest.main()