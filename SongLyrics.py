class Song(object):

    def __init__(self, lyrics, title, artist):
        self.lyrics = lyrics
        self.title = title
        self.artist = artist

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "These lyrics are copywrighted",
                   "So I'll stop here"])

hotline_bling = Song(["You used to call me on my",
                      "You used to, you used to",
                      "Yeah",])
# This is your daily reminder that Drake is Canadian

happy_bday.sing_me_a_song()
hotline_bling.sing_me_a_song()
