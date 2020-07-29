import numpy as np

# tw = ['#bestday gais di hidupku', 'gaiss haha pada dimana nih', 'hoax ihh']

# kamus
highExtrovert = ['wkawka', 'haha', 'yuk', 'kuy', 'kami', 'yeah', 'orang', 'handshake', 'lot of laught', 'hore',
                 'guys', 'gais', 'kumpul', 'joy', 'wkwk', 'main', 'kumpul', 'tears of joy', 'ayo', 'hehe', 'siapa', 'kita', 'orang', 'ngomong', 'cakap', 'teman', 'sobat', 'bro', 'sis', 'keluarga', 'family', 'team', 'tim', 'smiling face with open mouth', '?']

lowExtrovert = ['hmmm', 'unhappy', 'ahh', 'disapointed', 'huft', 'face without mouth', 'maaf',
                'maap', 'sorry', 'gua', 'gw', 'sendiri', 'alone', 'rumah', 'home', 'aku', 'weary face', 'stay at home', 'diam', 'loudly crying face']

highAgreeableness = ['keren', 'wow', 'wah', 'bagus', 'puji tuhan', 'alhamdulillah', 'bless', 'selamat', 'nyaman', 'setia', '!', '?'
                     'semangat', 'love', 'terima kasih', 'thanks', 'makasi', 'hai', 'sayang', 'mantap', 'heart', 'kasian', 'good', 'thank', 'thank you', 'rasa', 'cinta', 'aman', 'person with folded hands', 'kissing face', 'clapping hands sign', 'thumbs up sign']

lowAgreeableness = ['jangan', 'keluar', 'diam', 'benci', 'mampus', 'mampos', 'rasain', 'anjir', 'cok', 'jelek',
                    'lo', 'elo', 'ngantuk', 'mager', 'smirking face', 'kesal', 'tidur', 'males', 'malas', 'marah', 'rasa', 'loudly crying face', 'hate', 'hated', 'angry face', 'face with look of triumph', '!']

highConscientiousnes = ['belajar', 'kampus', 'work hard', 'sibuk', 'stres', 'tugas', 'sekolah', 'ujian', 'kuat', 'raih', 'enjoy',
                        'ulangan', 'sukses', 'done', 'berhasil', 'sks', 'setres', 'bersih', 'rapi', 'baca', 'sempro', 'skripsi', 'sidang', 'ayo', 'pasti bisa', 'tujuan', 'goal', 'semangat', 'person with folded hands', 'clapping hands sign']

lowConscientiousnes = ['mabok', 'fight', 'brantem', 'mati', 'bacot', 'smirking face', 'sleepy face', '!', 'smoking', 'rokok',
                       'fuck', 'males', 'malas', 'shit', 'bangke', 'goblok', 'cok', 'telek', 'angry face', 'face with look of triumph']

"""
ct = []
for line in highExtrovert:
    for x in range(len(tw)):
        print(tw[x])
        # if line in tw[x]:
        #   ct.append(x)

# print(np.unique(ct))
"""
