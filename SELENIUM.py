from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get('https://www.sudokuonline.io/pt/impossivel')


def create_neveis() -> list:
    driver.find_element(By.XPATH,'//*[@id="puzzleDifficulty"]').click()
    nivel_atual = driver.find_element(By.XPATH,'//*[@id="puzzleDifficulty"]').text
    niveis = driver.find_element(By.XPATH,'//*[@id="game-header"]/div/div[1]/div/div').text.split('\n')
    return niveis + [nivel_atual], nivel_atual
driver.find_element(By.XPATH,'//*[@id="game-header"]/div/div[1]/div').text

lita, atu = create_neveis()

def returner(la_string:str) -> int:
    if la_string == '':
        return 0
    else: return int(la_string)

def atualize_matrix():
    for rep in range(1, 82, 1):
        value =  driver.find_element(By.XPATH,f'//*[@id="sudoku"]/div[{rep}]').get_attribute('data-value')
        if(rep == 1):
            pre_matrix = [returner(value)]
        else: 
            pre_matrix.append(returner(value))
    new_matrix = np.matrix(np.array(pre_matrix).reshape((9,9)))
    return new_matrix

tabuleiro = atualize_matrix()

tabuleiro
driver