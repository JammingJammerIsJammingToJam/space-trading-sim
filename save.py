from planet_gen import *
#systems = gen_systems(x1, x2, y1, y2, r, i, p)
#names = planet_names(systems)

def encode_name(name):
    syllables = ['ka', 'ke', 'ku', 'ko', 'ki',
            'sha', 'shi', 'su', 'se', 'so',
            'ha', 'hi', 'hu', 'he', 'ho',
            'ta', 'te', 'tu', 'ti', 'to',
            'the', 'thi', 'thu', 'thro',
            'xi', 'xu', 'xe', 'xa', 'xo',
            'da', 'di', 'du', 'de', 'do',
            'ja', 'ji', 'ju', 'je', 'jo',
            'za', 'ze', 'zu', 'zi', 'zo',
            'la', 'li', 'lu', 'le', 'lo',
            'fe', 'fu', 'fi',
            'cha', 'chi', 'chu', 'che', 'cho',
            'ya', 'yu', 'yo', 'yi', ' '
        ]
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!.'
    name = name.lower()
    text = ""
    syls = []
    for char in name:
        text += char
        if text in syllables:
            syls.append(text)
            text = ""
    new = ''.join([chars[syllables.index(syl)] for syl in syls])
    return new

def decode_name(name):
    syllables = ['ka', 'ke', 'ku', 'ko', 'ki',
            'sha', 'shi', 'su', 'se', 'so',
            'ha', 'hi', 'hu', 'he', 'ho',
            'ta', 'te', 'tu', 'ti', 'to',
            'the', 'thi', 'thu', 'thro',
            'xi', 'xu', 'xe', 'xa', 'xo',
            'da', 'di', 'du', 'de', 'do',
            'ja', 'ji', 'ju', 'je', 'jo',
            'za', 'ze', 'zu', 'zi', 'zo',
            'la', 'li', 'lu', 'le', 'lo',
            'fe', 'fu', 'fi',
            'cha', 'chi', 'chu', 'che', 'cho',
            'ya', 'yu', 'yo', 'yi', ' '
    ]
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!.'
    text = ''.join([syllables[chars.index(syl)] for syl in name])
    text = ' '.join([part.capitalize() for part in text.split(' ')])
    return text

"""
print(len(names), len(systems))
combo = [{"name" : encode_name(names[i]), "pos" : systems[i]} for i in range(0, len(systems))]
print(''.join([combo[i]["name"] for i in range(0, len(combo))]))
print()
print(''.join([decode_name(combo[i]["name"]) for i in range(0, len(combo))]))
"""

def encode_coord(coord):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!.'
    return chars[coord // 62] + chars[coord % 62]

def decode_coord(coord):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!.'
    return chars.index(coord[0]) * 62 + chars.index(coord[1]) 

#Format of [["name", x, y, faction(1/2/3/4), planet1, planet2, planet3 ...]]
#Name, x, y, faction = name + 5 chars for metadata
#Format of planet data = resource numbers = 0-61 for abundance for say 5 resources
def encode_systems(systems):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!.'
    new = []
    for sys in systems:
        new2 = []
        new2.append(encode_name(sys[0]) + encode_coord(sys[1]) + encode_coord(sys[2]) + str(sys[3]))
        for item in sys[4:]:
            text = ""
            for num in item:
                text += chars[num]
            new2.append(text)
        new.append('!'.join(new2))
    return '.'.join(new)

def decode_systems(systems):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!.'
    new = systems.split('.')
    news = []
    for item in new:
        news2 = []
        txt = item.split('!')
        metadata = txt[0]
        news2.append(decode_name(metadata[:-5]))
        news2.append(decode_coord(metadata[-5:-3]))
        news2.append(decode_coord(metadata[-3:-1]))
        news2.append(int(metadata[-1]))
        for planet in txt[1:]:
            news2.append([chars.index(num) for num in planet])
        news.append(news2)
    return news

systems = gen_systems(x1, x2, y1, y2, r, i, p)
print(systems)
print(encode_systems(systems))