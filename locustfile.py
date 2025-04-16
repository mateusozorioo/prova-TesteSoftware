from locust import HttpUser, task, between

class WebsiteUser (HttpUser):
    wait_time = between(1, 3) # Tempo de espera entre requisições (segundos)

    @task
    def load_homepage(self):
        self.client.get("/") #Testando a página inicial

    @task
    def load_about_page(self):
        self.client.get("/presencial/administracao-bacharelado")

    @task
    def load_contact_page(self):
        self.client.get("/folder")