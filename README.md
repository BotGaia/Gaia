<p align="center">
  <img src="https://i.imgur.com/sEkmmNN.png" width="260" height="">
</p>

<h1 align="center"> Gaia </h1>

[![pipeline status](https://gitlab.com/botgaia/Gaia/badges/master/pipeline.svg)](https://gitlab.com/botgaia/Gaia/commits/master)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

---

Saudações! Sou Gaia, a Mãe-Terra e estou aqui para compartilhar informações sobre minha meteorologia e correlacioná-la com modalidades esportivas.

Esse projeto teve como base o [Rasa Boilerplate](https://github.com/lappis-unb/rasa-ptbr-boilerplate).

## Como contribuir

Se tiver interesse em como contribuir para o projeto, olhe nossa [wiki](https://github.com/fga-eps-mds/2019.1-Gaia).

## Como usar

O nosso projeto utiliza o Docker e o Docker Compose como ferramentes de desenvolvimento. Para instalar eles, siga o tutorial no site oficial do [Docker](https://www.docker.com/).

### Telegram

Para rodar o bot no Telegram, é necessário utilizar o [ngrok](https://ngrok.com/) para expor determinada porta para ser utilizado pelo Telegram. Ao baixar, é só executar utilizando o seguinte comando:

```$ ngrok http 5001```

Utilize a rota fornecida pelo ngrok, de preferência https. Cole sua rota do ngrok no arquivo .env, no espaço:

`TELEGRAM_WEBHOOK={https://SEUNGROK/webhooks/telegram/webhook}`

Insira também no .env as seguintes informações do bot, caso não tenha essas informações, acesse o [BotFather](https://telegram.me/BotFather):

```TELEGRAM_TOKEN```

```TELEGRAM_BOT_USERNAME```

Com o Docker compose instalado, acesse a pasta raiz do projeto e execute o seguinte comando em seu terminal:
Este comando treinará o bot e irá iniciá-lo no telegram.

```$ sudo docker-compose up bot```

### Terminal

Para executar o serviço do bot em seu terminal, utilize o seguinte comando para treiná-lo:

```$ sudo docker-compose run --rm bot make train```

Em seguida execute:

```$ sudo docker-compose run --rm bot make run-console```
