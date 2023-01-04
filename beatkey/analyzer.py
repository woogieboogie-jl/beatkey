import librosa
import numpy as np

# BASIC ANALYSIS / OUTPUT :
def analyze(song, song_dir):
    # Load the audio and save waveform as `y`, with the sampling rate of 'sr'
    try:
        # Load audio file
        y, sr = librosa.load(song_dir + '/' + song)
        return y, sr
    except EOFError:
        y = "ERR"
        sr = "ERR"
        return y, sr

# calculate bpm , beat_frames with the give 'y', 'sr' values
def analyzeBeat(y,sr):
    if y == "ERR":
        bpm = "ERR"
    else:
        # Run the default beat tracker
        bpm, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        print('Estimated tempo: {:.2f} beats per minute'.format(bpm))
    return bpm


#calculate pitches / magnitudes with the given 'y', 'sr' values (WIP)
def analyzePitch(y,sr):
    pitch, third = pitchCalculate(y,sr)
    key_org = pitch +" "+ third
    if third == "":
        print(f"key for harmonic mixing : Unavaliable (undistinguishable minor/major ratio)")
        key_dj = "N/A"
    else :
        key_dj = pitchConvert(key_org)
        print(f"key for harmonic mixing : {key_dj}")
    return key_dj, key_org

def pitchConvert(key_org):
    keys_camelot ={
    "B Major" : "1B",
    "F# Major" : "2B",
    "C# Major" : "3B",
    "G# Major" : "4B",
    "D# Major" : "5B",
    "A# Major" : "6B",
    "F Major": "7B",
    "C Major": "8B",
    "G Major": "9B",
    "D Major": "10B",
    "A Major": "11B",
    "E Major" : "12B",
    "G# minor" : "1A",
    "D# minor" : "2A",
    "A# minor" : "3A",
    "F minor": "4A",
    "C minor": "5A",
    "G minor": "6A",
    "D minor": "7A",
    "A minor": "8A",
    "E minor" : "9A",
    "B minor" : "10A",
    "F# minor" : "11A",
    "C# minor" : "12A",
    }
    key_dj = keys_camelot[key_org]
    return key_dj



def pitchCalculate(y,sr):
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    song_chroma = chroma.sum(axis=1)
    # pitches in 12 tone equal temperament
    pitches = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

    # print note to value relations
    for k in range(len(song_chroma)):
        print(str(pitches[k]) + '\t' + str(song_chroma[k]))

    # select the most dominate pitch
    pitch_id = np.argmax(np.squeeze(song_chroma))
    pitch = pitches[pitch_id]

    min_third_id = (pitch_id+3)%12
    maj_third_id = (pitch_id+4)%12

    # check if the musical 3rd is major or minor
    if song_chroma[min_third_id] < song_chroma[maj_third_id]:
        third = 'Major'
        print(str.format('\nThis song is likely in {} {}',pitch, third))
    elif song_chroma[min_third_id] > song_chroma[maj_third_id]:
        third = 'minor'
        print(str.format('\nThis song is likely in {} {}',pitch, third))
    else:
        print(str.format('\nThis song might be in {} something???',pitch))
        third = ''
    return pitch, third


# # pitch calculator for the whole song (WIP, 더 정확한 방법이지만 일단은 시간상 보류)
# def pitchCalculate(pitches, magnitudes):
#     pitches_dict = {"1": [32.70], "2":[34.64], "3":[36.70], "4":[38.89], "5":[41.20], "6":[43.65], "7":[46.24], "8":[48.99], "9":[51.91], "10":[55.00], "11":[58.27], "12":[61.73]}
#     pitch_fullframe = []
#     shape = np.shape(pitches)
#     nb_samples = shape[0]
#     nb_windows = shape[1]
#     for i in range(0, nb_windows):
#         index = magnitudes[:,i].argmax()
#         pitch_frame = pitches[index,i]
#         pitch_fullframe.append(pitch_frame)
#         print(pitch_frame)
#     return pitch
