# WhatsAutomate
![WhatsApp Logo](https://logospng.org/download/whatsapp/logo-whatsapp-1024.png){:height="100px" width="100px"}


Este projeto visa automatizar o envio de mensagens, incluindo imagens, para contatos do WhatsApp.

## Arquivos do projeto:

1. **config.py**

    Arquivo contendo variáveis de configuração:

    - `contatos_arquivo`: Nome do arquivo que contém os números de contato para os quais as mensagens serão enviadas.
    - `mensagem_arquivo`: Nome do arquivo que contém a mensagem a ser enviada.
    - `diretorio_imagens`: Diretório das imagens a serem enviadas.
    - `tempo_entre_envios`: Tempo de espera entre os envios para cada contato, em segundos.
    - `tempo_fechar_guia`: Tempo de espera para fechar a guia do navegador, em segundos.
&nbsp;
2. **requeriments.txt**

    Este arquivo contém a lista de dependências do Python necessárias para executar o projeto. Utilize o seguinte comando para instalar as dependências:

    ```bash
    pip install -r requeriments.txt
    ```

3. **contatos.txt**

    Arquivo contendo os números de contato no formato:
    ```
    +5561987654321
    +5561912345678
    ```

4. **metodos.py**

    Contém funções para carregar a lista de contatos, ler a mensagem do arquivo e enviar mensagens com imagens para os contatos.

## Uso do módulo

O arquivo `metodos.py` contém as funções necessárias para enviar mensagens com imagens para os contatos listados no arquivo `contatos.txt`. Ajuste as variáveis no arquivo `config.py` para controlar as configurações de envio.

Execute o arquivo `metodos.py` da seguinte forma:

```bash
python uteis/metodos.py
```

## Logs PyWhatKit_DB

Este arquivo é uma introdução ao projeto, detalhando os arquivos, a instalação de dependências e a execução do script principal `metodos.py`. Também fornece informações sobre os logs gerados pelo PyWhatKit_DB e sugere seguir um padrão específico para os números de contato no arquivo `contatos.txt`.
