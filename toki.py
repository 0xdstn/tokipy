#!/usr/bin/env python3
from random import choice
import sys

PAIRS = [
    ("a", "ah"),
    ("akesi", "animal/amphibian"),
    ("ala", "no/not"),
    ("alasa", "gather"),
    ("ale", "everything/anything/life"),
    ("anpa", "bottom/floor"),
    ("ante", "difference"),
    ("anu", "or"),
    ("awen", "wait"),
    ("en", "and"),
    ("esun", "shop"),
    ("ijo", "thing"),
    ("ike", "bad"),
    ("ilo", "tool/machine"),
    ("insa", "inside"),
    ("jaki", "dirty/gross"),
    ("jan", "person"),
    ("jelo", "yellow"),
    ("jo", "having/take"),
    ("kala", "fish"),
    ("kalama", "sound"),
    ("kama", "come/become/happen"),
    ("kasi", "plant"),
    ("ken", "can"),
    ("kepeken", "use"),
    ("kili", "fruit/vegetable"),
    ("kin", "also"),
    ("kiwen", "hard"),
    ("ko", "semi-solid/squishy"),
    ("kon", "air/wind"),
    ("kule", "color"),
    ("kulupu", "group"),
    ("kute", "listen"),
    ("lape", "sleep"),
    ("laso", "blue"),
    ("lawa", "head"),
    ("len", "clothing"),
    ("lete", "cold"),
    ("lili", "small"),
    ("linja", "long/thin"),
    ("lipu", "flat"),
    ("loje", "red"),
    ("lon", "present/awake"),
    ("luka", "hand/arm"),
    ("lukin", "see/look/watch/read"),
    ("lupa", "hole/window/door"),
    ("ma", "land"),
    ("mama", "parent"),
    ("mani", "money"),
    ("meli", "female"),
    ("mi", "I/me/we"),
    ("mije", "male"),
    ("moku", "food/eat"),
    ("moli", "death/kill"),
    ("monsi", "back/rear"),
    ("mu", "animal noise/woof/meow"),
    ("mun", "moon"),
    ("musi", "fun"),
    ("mute", "many"),
    ("namako", "food additive"),
    ("nanpa", "number"),
    ("nasa", "silly/crazy"),
    ("nasin", "way/path"),
    ("nena", "bump/nose/hill"),
    ("ni", "this/that"),
    ("nimi", "word/name"),
    ("noka", "leg/foot"),
    ("o", "calling attention"),
    ("oko", "eye"),
    ("olin", "love"),
    ("ona", "she/he/it/they"),
    ("open", "open"),
    ("pakala", "blunder"),
    ("pali", "activity/work"),
    ("palisa", "long/hard"),
    ("pan", "grain"),
    ("pana", "give"),
    ("pi", "of/belonging to"),
    ("pilin", "feelings"),
    ("pimeja", "black"),
    ("pini", "end"),
    ("pipi", "bug"),
    ("poka", "side/hip/next"),
    ("poki", "container"),
    ("pona", "good"),
    ("sama", "same"),
    ("seli", "fire"),
    ("selo", "outside/skin"),
    ("seme", "what/which/question"),
    ("sewi", "high/up"),
    ("sijelo", "body"),
    ("sike", "n circle"),
    ("sin", "new"),
    ("sina", "you"),
    ("sinpin", "front/chest"),
    ("sitelen", "picture/draw/write"),
    ("sona", "knowledge"),
    ("soweli", "animal/mammal"),
    ("suli", "big/tall"),
    ("suno", "sun/light"),
    ("supa", "flat surface"),
    ("suwi", "candy/sweet"),
    ("tan", "because"),
    ("taso", "but"),
    ("tawa", "towards"),
    ("telo", "water"),
    ("tenpo", "time"),
    ("toki", "language"),
    ("tomo", "house"),
    ("tu", "two"),
    ("unpa", "sex"),
    ("uta", "mouth"),
    ("utala", "conflict"),
    ("walo", "white"),
    ("wan", "one"),
    ("waso", "bird"),
    ("wawa", "energy"),
    ("weka", "away"),
    ("wile", "want/need")
]

total = len(PAIRS)

QUIT_CHAR = 'q'
INTRO = """This script was modified from ~vilmibm/bin/hiragana.py
For each printed english description, type its toki pona version.
enter {} to quit.""".format(QUIT_CHAR)
FINAL_REPORT = """good job! you got {}% right."""

def final_report(num_correct, rounds):
    print('')
    if rounds == 0:
        return 'see ya~'
    score = int((num_correct / rounds) * 100)
    return FINAL_REPORT.format(score)

def main():
    num_correct = 0
    rounds = 0

    print(INTRO)
    quitting = False
    while not quitting:
        if len(PAIRS) == 0:
            break
        else:
            question = choice(PAIRS)
            PAIRS.remove(question)
            answer, challenge = question
            print('')
            print('({}/{})'.format(total-len(PAIRS),total))
            response = input('{} > '.format(challenge)).rstrip()
            if QUIT_CHAR == response:
                break
            rounds += 1
            if answer == response:
                num_correct += 1
                print('Yes! {}/{}'.format(num_correct, rounds))
            else:
                print('Nope - {} - {}/{}'.format(answer, num_correct, rounds))

    print(final_report(num_correct, rounds))
    return 0

if __name__ == '__main__':
    sys.exit(main())
