import eyed3

def to_latin(title):
    title = title.lower()
    # ěščřžýáíéúůňťďó
    prohibited_chars = "ěščřžýáíéúůňťďó"
    allowed_chars = "escrzyaieuuntdo"
    for old, new in zip(prohibited_chars,allowed_chars):
        title = title.replace(old,new)
    return title

def edit_metadata(title, number,artist,album,album_artist=None):
    audiofile = eyed3.load(f"{title}.mp3")
    title = to_latin(title)
    audiofile.tag.artist = artist
    audiofile.tag.album = album
    #audiofile.tag.album_artist = album_artist
    audiofile.tag.title = title
    audiofile.tag.track_num = number
    audiofile.tag.save()


if __name__ == "__main__":
    title = input("Input title of your song \n")
    artist =input("Input the artist \n")
    album = input("Input the album \n")
    number = input("Input the number \n")
    #album_artist = input("Input the album artist")
    edit_metadata(title,number,artist,album)
