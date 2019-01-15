''' JukeBox!

Design a musical jukebox using oop
'''
class Artist:
    def __init__(self, songs):
        self.songs = songs


class Song:
    def __init__(self, title, artist, track, genre):
        self.title = title
        self.artist = artist
        self.track = track
        self.genre = genre
    def playTrack(self):
        # the code for playing the track

class Selection:
    def __init__(self, title, artists, songs):
        self.title = title
        self.artists = artists
        self.songs = songs
        self.currentlyPlaying = 0 # would hold the index
        self.paused = False
    def shuffle(self):
        self.songs = mix(self.songs)
    def playTrack(self):
        for song in self.songs:
            # play song
    def stopTrack(self):
        self.paused = True

class JukeBox:
    def __init__(self, title, owner, location, costPerSong):
        self.title = title
        self.location = location
        self.owner = owner
        self.costPerSong = costPerSong
        self.credit = 0
        self.selections = []
    def insertCoin(self, credit):
        self.credit += credit
    def playRandom(self):
        if self.credit > self.costPerSong:
            # pick a random selection from self.selctions
            # pick a random song from that selection
            self.credit -= self.costPerSong
    def addSongToSelectoin(song, selection):
        if not song or not selection:
            return
        if not self.selection[selection]:
            return
        self.selection = self.seletion.append(s)
    def removeSongFromSelection(song, selection):
        if not song or not selection:
            return
        if not self.selections[selection]:
            return
        self.selections[selection] = [song for song in self.selections[selection] if song != s]