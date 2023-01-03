from selenium import webdriver
import random

directory = 'C:\Python\projects\instagram\chromedriver'
browser = webdriver.Chrome("chromedriver.exe")

def musicInput():
    music_name = input("type in something for searching music")


def siteLoader():
    with open("music_sites.txt") as sites:
        music_sites = sites.readlines()
    music_clues = {}
    with open("music_clues.txt") as clues:
        music_clues_raw = clues.readlines()
        for i in range(1,len(music_clues_raw):
            music_clues{i} = music_clues_raw[i-1]
    return music_sites music_clues

def siteRefresher()
    with open("music_sites.txt") as sites:
        sites.write("")
    with open("music_clues.txt") as clues:
        clues.write("")

def randomTimeGenerator():
    pass

def sliderLoad():
    


def mp3juiceLoad():

def scraper():
    music_sites = siteloader()
    driver = webdriver.Chrome(directory)
    for i in music_clues:
    music_clues[i] = 
    driver.get()

