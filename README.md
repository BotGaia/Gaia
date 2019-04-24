<p align="center">
  <img src="https://i.imgur.com/sEkmmNN.png" width="260" height="">
</p>

<h1 align="center"> Gaia </h1>

Saudações! Sou Gaia, a Mãe-Terra e estou aqui para compartilhar informações sobre meu clima.

## Como usar
Com o Docker compose instalado, acesse a pasta raiz do projeto e execute o seguinte comando em seu terminal:
Este comando treinará o bot e irá iniciá-lo no telegram.

```$ sudo docker-compose up bot```

Para rodar no Telegram, é necessário utilizar o ngrok para expor determinada porta para ser utilizado pelo Telegram. Ao baixar, é só executar utilizando o seguinte comando:

```$ ngrok http 5001```

Para executar o serviço do bot em seu terminal, utilize o seguinte comando para treiná-lo:

```$ sudo docker-compose run --rm bot make train```

Em seguida execute:

```$ sudo docker-compose run --rm bot make run-console```




