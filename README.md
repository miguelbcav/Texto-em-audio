# Gerador de Áudio a partir de Texto

Este projeto permite a conversão de texto em áudio utilizando a tecnologia de síntese de fala (TTS) do Microsoft Azure (Edge TTS). Você pode inserir um texto, escolher uma voz e gerar um arquivo de áudio no formato MP3.

## Funcionalidades

- Conversão de texto para áudio utilizando vozes neurais.
- Suporte para diferentes vozes em português brasileiro.
- Geração do áudio e salvamento em arquivos MP3 com nome único baseado no timestamp.
- Interface simples e intuitiva para entrada de texto e seleção de voz.

## Requisitos

Antes de executar o projeto, certifique-se de que você tenha as seguintes dependências instaladas:

1. **Python** (versão 3.7 ou superior).
2. **Pacotes Python**:
    - `flet` (Para criação da interface gráfica)
    - `edge-tts` (Para geração de áudio com a tecnologia Edge TTS)
    - `asyncio` (Para execução assíncrona)
   
Você pode instalar as dependências utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
Como Usar
Clone este repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/gerador-voz-texto.git
cd gerador-voz-texto
Crie um arquivo de texto chamado vozes.txt no mesmo diretório do projeto. Este arquivo deve conter uma lista das vozes disponíveis, cada uma em uma linha. O formato é o seguinte:

Copiar código
pt-BR-AntonioNeural
pt-BR-FranciscaNeural
pt-BR-ThalitaMultilingualNeural
Caso o arquivo não exista, vozes padrão serão usadas.

Execute o aplicativo:

bash
Copiar código
python main.py
A interface será aberta. Insira um texto, escolha a voz desejada e clique em "Gerar Áudio". O áudio será gerado e salvo na pasta Audios Gerados dentro da sua pasta de documentos.

O arquivo de áudio será salvo com um nome único, com base no timestamp no formato audio_gerado_YYYY-MM-DD_HH-MM-SS.mp3.

Como Funciona
O usuário insere o texto e escolhe a voz desejada na interface gráfica.
O áudio é gerado usando a API do Edge TTS.
O áudio gerado é salvo na pasta "Audios Gerados" na área de documentos do usuário.
Contribuição
Se desejar contribuir para o projeto, sinta-se à vontade para enviar pull requests ou criar issues para relatar problemas ou sugerir melhorias. Agradecemos as contribuições!

Licença
Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.

Feito com ❤️ por Seu Miguelbcav.

markdown
Copiar código

### Explicação:

- **Funcionalidades**: Descreve as principais funcionalidades do projeto, como a conversão de texto para áudio e a escolha de vozes.
- **Requisitos**: Lista as dependências necessárias para rodar o projeto e como instalá-las.
- **Como Usar**: Explica o processo de clonagem, configuração e execução do projeto.
- **Como Funciona**: Detalha o fluxo básico do projeto, desde a inserção do texto até o salvamento do arquivo de áudio.
- **Contribuição**: Instruções para quem deseja contribuir com o projeto.
- **Licença**: A licença do projeto (MIT no exemplo, pode ser modificada se necessário).

Esse modelo ajuda a documentar o seu projeto e torna mais fácil para outras pessoas entenderem como usá-lo e contribuir.


💬 Como Contribuir:
Faça um fork do repositório.
Crie uma nova branch (git checkout -b minha-contribuicao).
Faça suas modificações e commit.
Push para a branch (git push origin minha-contribuicao).
Abra uma pull request.

📚 Mais Informações 🎓 Curso FLET 360 Python: Aprofunde-se no Python e na construção de interfaces gráficas com o Flet!
👉 https://go.hotmart.com/J91353466S?dp=1


