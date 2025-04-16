const { Builder, By } = require('selenium-webdriver'); // Importa as ferramentas do Selenium.

(async function testeHanked() { // Função assíncrona para o teste.
  const url = 'https://www.hankeds.com.br/prova/login2.html'; // Endereço da página de login.
  let driver = await new Builder().forBrowser('chrome').build(); // Abre o Chrome.

  try { // Tenta executar o teste.

    await driver.get(url); // Acessa a página.
    await driver.sleep(2000); // Espera a página carregar.

    const username = await driver.findElement(By.id('username')); // Pega o campo de usuário.
    const password = await driver.findElement(By.id('password')); // Pega o campo de senha.
    const botao = await driver.findElement(By.xpath("//button[contains(text(),'Entrar')]")); // Pega o botão Entrar.

    for (const letra of 'admin') { // Digita 'admin' no usuário.
      await username.sendKeys(letra);
      await driver.sleep(250);
    }

    await driver.sleep(1000); // Espera um pouco.

    for (const letra of 'admin123456') { // Digita a senha.
      await password.sendKeys(letra);
      await driver.sleep(250);
    }

    await driver.sleep(1000); // Espera um pouco.
    await botao.click(); // Clica no botão.

    await driver.sleep(4000); // Espera a próxima página.

    const urlAtual = await driver.getCurrentUrl(); // Pega a URL atual.

    if (urlAtual.includes('destino.html')) { // Verifica se foi pra página certa.
      console.log(' Teste passou: ok.');
    } else {
      console.log(' Teste falhou: não redirecionou.');
    }

    await driver.sleep(5000); // Espera antes de fechar.

  } catch (err) { // Se der erro...
    console.error(' Deu ruim no teste:', err);
  } finally { // No final...
    await driver.quit(); // Fecha o navegador.
  }
})();