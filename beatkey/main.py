import os
import analyzer
import organizer


#ANALYSABLE MUSIC FORMATS
format_list = (".m4a",".mp3", ".wav", "aac", ".ape",".flac")
#USER FRIENDLY DIRECTORY INPUT
def askDirectory():
    while True:
        directory = input("insert your working directory...")
        if os.path.isdir(directory) is True:
            print(f"directory checked...{directory}...")
            break
        else:
            print("wrong directory / input, please try again...")
            pass
    return directory

#SONG LIST INPUT
def songsGet(directory, format_list):
    file_list = os.listdir(directory)
    songs_dict = {}
    for file in file_list:
        #EXCLUDING ALREADY TAGGED FILES
        if file.endswith(format_list) and organizer.repeatCheck(file) is False:
            songs_dict[file] = [directory]
        else:
            pass
    return songs_dict

#PRINTER
def printer(songs_dict):
    for song in songs_dict:
        print(f"""
        name      : {song}
        bpm       : {songs_dict[song][0]}
        key_dj    : {songs_dict[song][1]}
        key_orgin : {songs_dict[song][2]}
        directory : {songs_dict[song][3]}
        """)
    print(f"the total number of songs schedulued for labelling are :{len(songs_dict)}...")


#MAIN
def __main__():
    while True:
        directory = askDirectory()
        songs_dict = songsGet(directory, format_list)
        if len(songs_dict) == 0:
            print("no audio file eligible for an analysis!...")
            pass
        else:
            break
    for song in songs_dict:
        song_dir = songs_dict[song][-1]
        print(f"analyzing song : {song}")
        y, sr = analyzer.analyze(song, song_dir)
        bpm = analyzer.analyzeBeat(y,sr)
        key_dj, key_org = analyzer.analyzePitch(y,sr)
        songs_dict[song].insert(0,bpm)
        songs_dict[song].insert(1,key_dj)
        songs_dict[song].insert(2,key_org)
    printer(songs_dict)
    input("press enter to start labeling bpms...")
    organizer.rename(songs_dict)

#REPEATING MAIN
while True:
    __main__()






