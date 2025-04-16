from selenium import webdriver # Importa a biblioteca pra controlar o navegador
from selenium.webdriver.common.by import By # Importa a forma de achar os elementos (ID, XPATH, etc.)
from selenium.webdriver.chrome.service import Service # Classe pra configurar o serviço do Chrome
from selenium.webdriver.support.ui import WebDriverWait # Pra esperar que algo aconteça na página.
from selenium.webdriver.support import expected_conditions as EC # Condições esperadas pra usar com o WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager # Pra baixar o driver do Chrome automaticamente
import time # Pra dar uns sleeps no código.

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # Abre o Chrome usando o driver mais novo.
driver.maximize_window() # Deixa a janela do navegador grandona

try: # Tenta fazer o teste aqui dentro.
    url = "https://www.hankeds.com.br/prova/login.html" # O endereço da página de login
    driver.get(url) # Manda o Chrome abrir essa página

    time.sleep(2) # Espera 2 segundos pra página carregar.

    def digitar_lento(elemento, texto, delay=0.25): # Função pra simular digitação lenta
        for letra in texto: # Pra cada letra no texto...
            elemento.send_keys(letra) # ...digita a letra no campo.
            time.sleep(delay) # ...espera um pouquinho

    usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))) # Espera até 10 segundos pra achar o campo de usuário pelo ID
    senha = driver.find_element(By.ID, "password") # Pega o campo de senha pelo ID.
    botao = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]") # Pega o botão 'Entrar' pelo texto dele no XPath

    digitar_lento(usuario, "admin") # Digita 'admin' no campo de usuário devagar.
    time.sleep(1) # Espera 1 segundo.
    digitar_lento(senha, "admin123456") # Digita a senha devagar
    time.sleep(1) # Espera mais 1 segundo.

    botao.click() # Clica no botão 'Entrar'
    time.sleep(4) # Espera 4 segundos pra ver se vai pra outra página

    if "destino.html" in driver.current_url: # Vê se a URL da página agora tem 'destino.html'
        print("✅ Teste passou: redirecionado corretamente.") # Se tiver, logou certo
    else:
        print("❌ Teste falhou: redirecionamento não ocorreu.") # Se não, deu erro no login

    time.sleep(5) # Espera mais um pouco antes de fechar

except Exception as e: # Se der algum erro durante o teste...
    print("❌ Erro durante o teste:", str(e)) # ...mostra qual foi o erro

finally: # No final de tudo, dando erro ou não...
    driver.quit() # ...fecha o navegador