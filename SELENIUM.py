from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
import time
import fnmatch
import random
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get('https://www.sudokuonline.io/pt/impossivel')


def create_neveis() -> list:
    driver.find_element(By.XPATH,'//*[@id="puzzleDifficulty"]').click()
    nivel_atual = driver.find_element(By.XPATH,'//*[@id="puzzleDifficulty"]').text
    niveis = driver.find_element(By.XPATH,'//*[@id="game-header"]/div/div[1]/div/div').text.split('\n')
    driver.find_element(By.XPATH,'//*[@id="puzzleDifficulty"]').click()
    return niveis + [nivel_atual], nivel_atual

def transform_cell(la_string:str) -> int:
    if la_string == '':
        return 0
    else: return int(la_string)

def atualize_matrix():
    for rep in range(1, 82, 1):
        value =  driver.find_element(By.XPATH,f'//*[@id="sudoku"]/div[{rep}]').get_attribute('data-value')
        if(rep == 1):
            pre_matrix = [transform_cell(value)]
        else: 
            pre_matrix.append(transform_cell(value))
    new_matrix = np.matrix(np.array(pre_matrix).reshape((9,9)))
    return new_matrix

ind = 0
ind_two = 0
def global_input():
    global tabuleiro
    for ind in range(0, 9):
        for ind_two in range(0, 9 ):
            value = tabuleiro[ind, ind_two]
            if value > 0 :
                cell  = driver.find_elements( By.XPATH , f'//*[@data-row="{ind}"]')[ind_two]
                if cell.text == "":
                    print(value)
                    cell.send_keys( str(value))

value = 6



def verify_button_erro():
    global driver
    if fnmatch.fnmatch(driver.current_url , "https://www.sudokuonline.io/pt/*"):
        while len(driver.find_elements(By.XPATH, '//*[@class="custom-control-label change-image"]')   ) == 0:
            try :
                driver.find_element(By.XPATH, '//*[@id="game-header"]/div/div[2]/div').click()
                time.sleep(1)
            except: time.sleep(2)

driver.find_elements(By.XPATH, '//*[@class="custom-control-label change-image"]').click()

tabuleiro = atualize_matrix()
pre_tabuleiro()



def infinity_while():
    global tabuleiro
    tabuleiro = atualize_matrix()
    def clonagem(tab = None):
        if tab is None:
            tab = tabuleiro
        clone =np.copy( tab)
        return clone
    def restart(value: int):
        nonlocal cell_alteration, setor_alteration, rest_alteration, hipotese_alteration
        if value ==0: pass
        else:
            cell_alteration = 1
            setor_alteration = 0
            rest_alteration = 0
            hipotese_alteration = 0

    def repetidores(value:int)->int:
        if value>0:
            return 0
        else: return 1

    error = 0
    cell_alteration = 1
    setor_alteration = 0
    rest_alteration = 0
    hipotese_alteration = 0
    pre_tabuleiro()
    while (len(np.where(tabuleiro > 0)[0]) != 81 and error ==0):
        while cell_alteration > 0:
            clone = clonagem()
            resolver_cell()
            cell_alteration = len(np.where(clone != tabuleiro)[0])
            setor_alteration = repetidores(cell_alteration)
        while setor_alteration > 0:
            clone = clonagem()
            resolver_setor()
            setor_alteration = len(np.where(clone != tabuleiro)[0])
            rest_alteration = repetidores(setor_alteration)
            restart(setor_alteration)
        while rest_alteration >0:
            clone = clonagem()
            resolver_rest()
            rest_alteration = len(np.where(clone != tabuleiro)[0])
            hipotese_alteration = repetidores(cell_alteration)
            restart(rest_alteration)
        while hipotese_alteration >0:
            clone = clonagem()
            cadeia_forcada()
            hipotese_alteration = len(np.where(clone != tabuleiro)[0])
            restart(hipotese_alteration)
            if(hipotese_alteration ==rest_alteration and cell_alteration ==setor_alteration ):
                error = 1
    pre_tabuleiro()
    global_input()


infinity_while()

pre_tabuleiro()
resolver_cell()
resto[0] = resolver_setor()
resto = resolver_rest()
cadeia_forcada()


tabuleiro
driver

driver.find_elements(By.XPATH, '//*[@id="victory-screen"]')

aleator = random.randint(0,3)
lita, atu = create_neveis()
driver.find_element(By.XPATH,'//*[@id="puzzleDifficulty"]').click()
driver.find_element(By.XPATH ,f"//*[contains(text(),'{lita[aleator]}')]").click()
time.sleep(2)
if len(driver.find_elements(By.XPATH, '//*[@id="submit_modal"]')) == 1 :
    driver.find_element(By.XPATH, '//*[@id="submit_modal"]').click()

'//*[@id="victory-screen"]'
