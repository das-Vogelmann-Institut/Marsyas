import eyed3
import sys
from os import listdir
from os.path import isfile, join

def to_latin(title):
    title = title.lower()
    # ěščřžýáíéúůňťďó
    prohibited_chars = "ěščřžýáíéúůňťďó"
    allowed_chars = "escrzyaieuuntdo"
    for old, new in zip(prohibited_chars,allowed_chars):
        title = title.replace(old,new)
    return title

def edit_metadata(title, number,artist,album,album_artist=None):
    audiofile = eyed3.load(title)
    title = to_latin(title)
    audiofile.tag.artist = artist
    audiofile.tag.album = album
    #audiofile.tag.album_artist = album_artist
    audiofile.tag.title = title
    audiofile.tag.track_num = number
    audiofile.tag.save()
    
def loop_for_files(filelist,path,artist,album):
    #for file in filelist:
    for index, file in enumerate(filelist):
        if file[-4:] == ".mp3":
            title = file
            number = index
            edit_metadata(title,number,artist,album)
            print(title)
            
            
def get_file_list(path):
    filelist = [f for f in listdir(path) if isfile(join(path, f))]
    return filelist


if __name__ == "__main__":
    
    path = sys.argv[1]
    #title = input("Input title of your song \n")
    artist =input("Input the artist \n")
    album = input("Input the album \n")
    #number = input("Input the number \n")
    #album_artist = input("Input the album artist")
    filelist = get_file_list(path)
    loop_for_files(filelist,path,artist,album)
    
    #edit_metadata(title,number,artist,album)
