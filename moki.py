from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

    #driver.current_window_handle # id da janela atual
#wids = driver.window_handles # ids de todas as janelas atuais

class bot():
    def __init__(self):    
        self.driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
                        
    def preencher_moki(self):
        driver = self.driver     
        driver.get('https://moki.app/login')
        driver.maximize_window()

        empresa = driver.find_element('xpath', '//*[@id="prefixo"]')
        ldap = driver.find_element('xpath', '//*[@id="login"]')
        senha = driver.find_element('xpath', '//*[@id="senha"]')
        entrar = driver.find_element('xpath', '//*[@id="content"]/app-login-page/div/div/div/div/div[2]/div/div[2]/form/button[1]/span')

        empresa.send_keys('leroymerlin')
        ldap.send_keys('51046899')
        senha.send_keys('4609&LMNatan')
        entrar.click()

        time.sleep(3)
        nova_avaliacao = driver.find_element('xpath', '//*[@id="ui-tabpanel-7"]/div/app-home-classica/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/button')
        nova_avaliacao.click()
                

        def find_window(url:str):
            wids = driver.window_handles
            for window in wids:
                driver.switch_to.window(window)
                if url in driver.current_url:
                    break
        find_window('avaliacao')              
        
        unidade = driver.find_element('xpath', '//*[@id="buscaUnidade"]/span/button')
        unidade.click()

        preencher_unidade = driver.find_element('xpath', '//*[@id="buscaUnidade"]/span/input')
        preencher_unidade.send_keys('99')
        time.sleep(2)
        preencher_unidade.send_keys(Keys.ENTER)
        preencher_unidade.send_keys(Keys.ENTER)                


        preencher_tipo_checklist = driver.find_element('xpath', '//*[@id="buscaChecklist"]/span/input')    
        preencher_tipo_checklist.send_keys('Não conformidade')
        time.sleep(2)
        preencher_tipo_checklist.send_keys(Keys.ENTER)
        preencher_tipo_checklist.send_keys(Keys.ENTER)

        time.sleep(2)
        nome_completo = driver.find_element('xpath', '//*[@id="ui-panel-30-content"]/div/div[3]/div/app-avaliacao-resposta-texto/textarea')
        nome_completo.send_keys('Natanael Alves dos Santos')

        turno2 = driver.find_element('xpath', '//*[@id="Opcao_5f8eed161a6dc1130c56282c_fd9ddbaa83580cb844e93842"]')
        turno2.click()



bot = bot()
bot.preencher_moki()

