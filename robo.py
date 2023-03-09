from selenium.common import exceptions
import chromedriver_binary
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

arq = open("resultados.txt", "w")

class RoboYoutube:
    def __init__(self):
        self.webdriver = webdriver.Chrome()

    def buscar(self, busca):
        j = 0
        url = "https://www.youtube.com/results?search_query=%s" % busca
        self.webdriver.get(url)
    
        titulos = self.webdriver.find_elements(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')

        for i in range(0,4):
            arq.write('%s \n' % (titulos[i]).text)
                        
bot = RoboYoutube()
bot.buscar("teste")