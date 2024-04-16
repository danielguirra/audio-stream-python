# Audio Streaming via Socket em Python

Este é um projeto simples de streaming de áudio em Python usando sockets para comunicação entre um cliente e um servidor.

## Descrição

O objetivo deste projeto é demonstrar como transmitir áudio em tempo real de um cliente para um servidor usando sockets em Python. O cliente grava áudio de seu microfone e o envia para o servidor, que pode reproduzi-lo ou realizar qualquer outro processamento necessário.

## Funcionalidades

- Transmissão de áudio em tempo real de um cliente para um servidor.
- Reprodução do áudio recebido pelo servidor.

## Como Usar

1. **Instalação:**
   - Clone este repositório em sua máquina local:
     ```
     git clone https://github.com/seu-usuario/audio-streaming-python.git
     ```
   - Navegue até o diretório do projeto:
     ```
     cd audio-streaming-python
     ```
   - Instale as dependências:
     ```
     pip install -r requirements.txt
     ```

2. **Execução:**
   - Inicie o servidor:
     ```
     python server.py
     ```
   - Inicie o cliente:
     ```
     python client.py
     ```
   - Siga as instruções para gravação e transmissão de áudio.

3. **Customização:**
   - Você pode personalizar as configurações de áudio, como taxa de amostragem, formato e número de canais, no arquivo `audio.py`.
   - Modifique o código conforme necessário para atender aos requisitos específicos do seu projeto.

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão, correção de bugs ou novos recursos, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
