#### ⚙️ **`core/` e `.env`**: Configuração Centralizada

- **`.env`**: Um arquivo na raiz do projeto para armazenar informações sensíveis e configurações que variam entre ambientes (desenvolvimento, produção). **Nunca** versione este arquivo no Git.
- **`config.py`**: Lê as variáveis do arquivo `.env` (usando bibliotecas como `python-dotenv`) e as disponibiliza de forma organizada para o resto da aplicação. É aqui que você carrega a `OPENAI_API_KEY`, por exemplo.