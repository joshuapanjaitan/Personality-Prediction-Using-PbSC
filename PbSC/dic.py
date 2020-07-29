import numpy as np

# tw = ['#bestday gais di hidupku', 'gaiss haha pada dimana nih', 'hoax ihh']

# kamus
highExtrovert = ['wkawka', 'haha', 'yuk', 'kuy', 'kami', 'yeah', 'orang', 'handshake', 'lot of laught', 'hore',
                 'guys', 'gais', 'kumpul', 'joy', 'wkwk', 'main', 'kumpul', 'tears of joy', 'ayo', 'hehe', 'siapa', 'kita']

lowExtrovert = ['hmmm', 'unhappy', 'ahh', 'disapointed', 'huft', 'face without mouth', 'maaf',
                'maap', 'sorry', 'gua', 'gw', 'sendiri', 'alone', 'rumah', 'home', 'aku', 'weary face']

highAgreeableness = ['keren', 'wow', 'wah', 'bagus', 'puji tuhan', 'alhamdulillah', 'bless', 'selamat',
                     'semangat', 'love', 'terima kasih', 'thanks', 'makasi', 'hai', 'sayang', 'mantap', 'heart', 'kasian', 'good', 'thank', 'thank you', 'rasa', 'cinta', 'aman']

lowAgreeableness = ['jangan', 'keluar', 'diam', 'benci', 'mampus', 'mampos', 'rasain', 'anjir', 'cok', 'jelek',
                    'lo', 'elo', 'ngantuk', 'mager', 'smirking face', 'kesal', 'tidur', 'males', 'malas', 'marah', 'rasa']

highConscientiousnes = ['belajar', 'kampus', 'work hard', 'sibuk', 'stres', 'tugas', 'sekolah', 'ujian', 'kuat', 'raih', 'enjoy',
                        'ulangan', 'sukses', 'done', 'berhasil', 'sks', 'setres', 'bersih', 'rapi', 'baca', 'sempro', 'skripsi']

lowConscientiousnes = ['mabok', 'fight', 'brantem', 'mati',
                       'fuck', 'males', 'malas', 'shit', 'bangke', 'goblok', 'cok', 'telek']

"""
ct = []
for line in highExtrovert:
    for x in range(len(tw)):
        print(tw[x])
        # if line in tw[x]:
        #   ct.append(x)

# print(np.unique(ct))
"""
