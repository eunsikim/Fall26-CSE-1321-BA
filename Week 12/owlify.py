# We are developing a Music Application, 
# similar to Spotify, Youtube Music,
# Apple Music, etc.

# For this application we are going to have
# three classes:
# Class Song

# Class Album

# Class Playlist

# Think about the attributes and behaviors 
# for each of these clases.
import time

class Song:
    def __init__ (self, title, author, song_duration, music_file):
        self.title = title
        self.author = author
        self.song_duration = song_duration
        self.music_file = music_file

        self.is_playing = False

    def play(self):
        if self.is_playing == False:
            print(f"Playing {self.get_song_info()}")
            self.is_playing = True
        else:
            print(f"The song is already playing.")

    def stop(self):
        if self.is_playing == True:
            print(f"Stopping {self.get_song_info()}")
            self.is_playing = False
        else:
            print(f"The song is already stopped.")

    def get_song_info(self):
        return f"{self.title} by {self.author}, music file: {self.music_file}"

class Album:
    def __init__(self, title, author, album_duration, songs):
        self.title = title
        self.author = author
        self.album_duration = album_duration
        self.songs = songs # `songs` is a list of Song objects

    def print_songs(self):
        for song in self.songs:
            print(song.get_song_info())

    def play(self):
        for song in self.songs:
            song.play()
            time.sleep(song.song_duration)
            song.stop()

class Playlist:
    def __init__(self, title, author, duration):
        self.title = title
        self.author = author
        self.duration = duration
        self.songs = []

    def print_songs(self):
        for song in self.songs:
            print(song.get_song_info())

    def play(self):
        for song in self.songs:
            song.play()
            time.sleep(song.song_duration)
            song.stop()

def main():
    song1 = Song("Hello World", "Eun Sik", 2, "hello_word.mp3")
    song2 = Song("Thriller", "Michael Jackson", 3, "thriller.flac")
    song3 = Song("Billie Jean", "Michael Jackson", 3, "billie_jean.flac")

    album1 = Album("Thriller", "Michael Jackson", 6, [song2, song3])
    album2 = Album("Example", "Eun Sik", 2, [song1])

    playlist1 = Playlist("Example Playlist", "Eun Sik", 8)

    playlist1.songs.append(song1)
    playlist1.songs.append(song2)
    playlist1.songs.append(song3)

    album1.play()

if __name__ == "__main__":
    main()