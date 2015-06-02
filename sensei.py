# -*- coding: utf-8 -*-
# せんせい

import alphabet
import random
import romkan
from Tkinter import Tk, Frame, BOTH
from gtts import gTTS
import pyglet

def tts(st):
    try:
        tts = gTTS(text=st, lang="ja")
        tts.save("tts.mp3")
        try:
            pyglet.media.load("tts.mp3").play()
            return 1
        except:
            return 0
    except:
        return 0

def generateWord(lbound, ubound):
    romanji = alphabet.load_romanji()
    lrnd = random.randint(lbound, ubound)
    word = ""
    for i in range(lrnd):
        rnd = random.randint(0, len(romanji)-1)
        word += romanji[rnd]
    return word

def test_cli(lbound, ubound, count):
    score = 0
    for i in range(count):
        word = generateWord(lbound, ubound)
        print romkan.to_hiragana(word)
        userInput = str(raw_input("in romanji: "))
        tts(romkan.to_hiragana(word))
        if userInput == word:
            print "Correct"
            score += 1
        else:
            print "Incorrect"
            print "The correct answer was: " + word
    print str(score) + "/" + str(count)
        
    
        

def main():
    test_cli(1, 1, 50)
    #test_ui(1, 1, 50)

if __name__ == "__main__":
    main()
