def cat(L):
    return () if L == [] else L[0] + cat(L[1:])

cartes = ["chevalier", "archeres", "gobelins", "gobelins a lances", "barbares", "dragons squelettes" ,"sorcier", "mousquetaire" ,"valkyrie", "pekka" ,"prince" ,"squelette geant", "gobelin a sarbacane" ,"electro geant" ,"bourreau" , "sorciere", "bebe dragon", "princesse", "electro sorcier", "mega chevalier", "fantome royal", "voleuse", "machine gobeline", "roi squelette", "chevalier d'or", "reine des archeres"]

perso_traits = {'chevalier': ('noble', 'colosse'), 'archeres': ('clan', 'guetteur'), 'gobelins': ('gobelin', 'assassin'), 'gobelins a lances': ('gobelin', 'visee'), 'barbares': ('clan', 'bagarreur'), 'dragons squelettes': ('revenant', 'guetteur'), 'sorcier': ('feu', 'mage'), 'mousquetaire': ('visee', 'noble'), 'valkyrie': ('clan', 'colosse'), 'pekka': ('ace', 'vengeuse'), 'prince': ('noble', 'bagarreur'), 'squelette geant': ('revenant', 'bagarreur'), 'gobelin a sarbacane': ('gobelin', 'guetteur'), 'electro geant': ('electro', 'vengeuse'), 'bourreau': ('ace', 'visee'), 'sorciere': ('revenant', 'vengeuse'), 'bebe dragon': ('visee', 'feu'), 'princesse': ('noble', 'guetteur'), 'electro sorcier': ('electro', 'mage'), 'mega chevalier': ('ace', 'bagarreur'), 'fantome royal': ('revenant', 'assassin'), 'voleuse': ('ace', 'assassin'), 'machine gobeline': ('gobelin', 'colosse'), 'roi squelette': ('revenant', 'colosse'), "chevalier d'or": ('noble', 'assassin'), 'reine des archeres': ('clan', 'vengeuse')}

traits = list(set(cat([perso_traits[k] for k in cartes])))

force_perso = {
    'gobelins a lances': 1,
    'dragons squelettes': 2,
    'sorcier': 3,
    'gobelins': 4,
    'archeres': 5,
    'gobelin a sarbacane': 6,
    'princesse': 7,
    'fantome royal': 8,
    'mega chevalier': 9,
    'barbares': 10,
    'prince': 11,
    'squelette geant': 12,
    'electro geant': 13,
    'chevalier': 14,
    'pekka': 15,
    'voleuse': 16,
    'bourreau': 17,
    'sorciere': 18,
    'mousquetaire': 19,
    'valkyrie': 20,
    'electro sorcier': 21,
    'bebe dragon': 22,
    'reine des archeres': 23,
    "chevalier d'or": 24,
    'machine gobeline': 25,
    'roi squelette': 26
}

#CHQT GPT : https://mergetacticsbuild.com/en/tier-list?utm_source=chatgpt.com
'''force_perso = {
    'gobelins a lances': 1,
    'chevalier': 2,
    'dragons squelettes': 3,
    'gobelins': 4,
    'barbares': 5,
    'gobelin a sarbacane': 6,
    'electro geant': 7,
    'sorcier': 8,
    'archeres': 9,
    'bourreau': 10,
    'mousquetaire': 11,
    'valkyrie': 12,
    'pekka': 13,
    'prince': 14,
    'sorciere': 15,
    'squelette geant': 16,
    'machine gobeline': 17,
    'princesse': 18,
    'bebe dragon': 19,
    'voleuse': 20,
    'mega chevalier': 21,
    'roi squelette': 22,
    "chevalier d'or": 23,
    'fantome royal': 24,
    'electro sorcier': 25,
    'reine des archeres': 26
}'''

force_traits = {
    'gobelin': [2.5, 3],
    'guetteur': [2.5, 3],
    'feu': [3],
    'electro': [1],
    'mage': [4],
    'revenant': [2, 3.5, 5],
    'assassin': [3, 4],
    'noble': [2.5, 3.5, float('inf')],
    'vengeuse': [2, 3],
    'ace': [3, 4],
    'colosse': [3.5, 4.5],
    'bagarreur': [1.5, 2.5],
    'visee': [2, 2.5],
    'clan': [3, 5]
}

force_traits = {trait: list(map(lambda x: 5*x, force_traits[trait])) for trait in force_traits}