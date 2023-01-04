import os

cleanlist = [".com",".net",".org",".kr"]

# 중복되어 라벨링을 방지
def repeatCheck(song):
    return song.startswith("[")

# 다운로드한 사이트들의 태그들을 자동삭제
def tagCleaner(cleanlist, song):
    pass

# 파일들의 이름을 바꿔줌
def rename(songs_dict):
    for song in songs_dict:
        bpm = bpmRounder(songs_dict[song][0])
        song_dir = songs_dict[song][-1]
        if bpm =="ERR":
            song_labeled = f"[{bpm}] {song}"
        else:
            key_dj = songs_dict[song][1]
            song_labeled = f"[{bpm}][{key_dj}] {song}"
        os.rename(song_dir+'/'+song,song_dir+'/'+song_labeled)

# bpm 소수점 반올림 / 에러코드는 에러로 비피엠란에 표기
def bpmRounder(bpm):
    try:
        bpm_view = int(round(bpm))
    except TypeError:
        bpm_view = "ERR"
    return bpm_view


# 추후에 ANALYZE 및 TAGGED된 음악들의 데이터를 저장하는 기능을 추가할 예정
def logRead():
    pass

def logWrite():
    pass
