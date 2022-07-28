from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path=r"geckodriver.exe")  
            # Coloque o caminho até o diretório do seu geckodriver.exe

    # Def responsável pelo seu login automático
    def login(self):
        driver = self.driver
        driver.get("https://instagram.com")
        time.sleep(6)
        campo_usuario = driver.find_element_by_xpath(
            "//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(3)
        # Insira o usuário da publicação em que deseja comentar
        self.comente_nas_fotos_com_a_hashtag("usuário-comentário")

    # Def responsável pela camuflagem do seu bot no instagram digitando semelhando a uma pessoa
    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1, 5)/30)

    # Def responsável pelo caminho até a publicação em que deseja comentar e por comentar
    def comente_nas_fotos_com_a_hashtag(self, hashtag):
        driver = self.driver
        # Insira o link da publicação que deseja comentar aqui
        driver.get("Endereço da publicação")
        time.sleep(3)

        # Estrutura While responsável pela automatização de comentários
        i = 0
        while(1):
            try:
                # Digite os comentários que deseja na quantidade que quiser
                comentarios = ['Comentários', 'Comentários', '...']
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(4, 7))
                self.digite_como_uma_pessoa(
                    random.choice(comentarios), campo_comentario)
                time.sleep(random.randint(30, 130))
                driver.find_element_by_xpath(
                    "//button[contains(text(),'Publicar')]").click()
                i += 1
                print(i)
                time.sleep(15)
            except Exception as e:
                print(e)
                time.sleep(2000)


# Informe o seu Usuário e a Senha aqui
Bot = InstagramBot('usuário', 'Senha')
Bot.login()
