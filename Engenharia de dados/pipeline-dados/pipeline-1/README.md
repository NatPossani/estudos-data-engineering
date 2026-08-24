# Pipeline de Dados ETL

Pipeline simples em Python para extrair dados da API pública [DummyJSON](https://dummyjson.com/), transformá-los no formato JSON retornado pela API e carregá-los em arquivos locais.

## Objetivo

O projeto demonstra um fluxo ETL:

- **Extract (Extração):** consulta os endpoints de usuários e produtos.
- **Transform (Transformação):** utiliza os dados JSON retornados pela API sem alteração de campos.
- **Load (Carga):** grava cada registro em um arquivo JSON identificado pelo seu `id`.

## Tecnologias

- Python 3.10 ou superior
- Biblioteca `requests`
- API DummyJSON

## Estrutura do projeto

```text
pipeline-dados/
├── ETL.py
├── products/
│   └── arquivos JSON dos produtos
├── users/
│   └── arquivos JSON dos usuários
└── README.md
```

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/SEU-USUARIO/pipeline-dados.git
   cd pipeline-dados
   ```

2. Crie e ative um ambiente virtual, recomendado para manter as dependências isoladas:

   **Windows PowerShell:**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **Linux ou macOS:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instale a dependência:

   ```bash
   pip install requests
   ```

## Como executar

Na raiz do projeto, execute:

```bash
python ETL.py
```

O script percorre os endpoints definidos nesta lista:

```python
endpoints = ["users", "products"]
```

Para cada endpoint, ele consulta os registros sequencialmente (`1`, `2`, `3`...) até que a API não retorne mais dados. Cada resposta bem-sucedida é enviada para a função de carga e deve ser salva em uma pasta local.

## Funcionamento do código

### `extract_data(endpoint)`

Faz uma requisição HTTP `GET` para o endereço recebido. Quando o status HTTP é `200`, retorna o conteúdo convertido para Python com `response.json()`. Em caso de erro, exibe uma mensagem e retorna `None`.

### `load_data(data, path)`

Obtém o campo `id` do registro e grava o objeto completo em um arquivo chamado `<id>.json` dentro do caminho informado.

### `loop_load_data(endpoint)`

Monta a URL do endpoint, inicia a sequência no ID `1` e repete as etapas de extração e carga até encontrar uma resposta vazia ou inválida.

## Exemplo de saída esperada

Depois de uma execução bem-sucedida, as pastas devem conter arquivos semelhantes a:

```text
users/1.json
users/2.json
products/1.json
products/2.json
```

Cada arquivo contém um único objeto JSON retornado pela API.

## Limitação conhecida

Na versão atual, `loop_load_data()` passa a URL completa para `load_data()`:

```python
load_data(data, endpoint)
```

Como `endpoint` contém algo como `https://dummyjson.com/users`, ele não representa corretamente as pastas locais `users/` e `products/`. Antes de executar o projeto em uma instalação nova, esse caminho deve ser ajustado para usar o nome do endpoint como diretório e garantir que a pasta exista.

Também é recomendável tratar timeout e erros de conexão HTTP para evitar que uma indisponibilidade da API interrompa o pipeline sem uma mensagem detalhada.

## Cuidados com os dados

Os dados de exemplo podem conter campos sensíveis simulados, como senha, número de cartão e SSN. Mesmo sendo dados fornecidos por uma API de demonstração, não publique dados reais no repositório. Se os arquivos JSON forem apenas resultados gerados localmente, considere adicioná-los ao `.gitignore`.

Exemplo de `.gitignore`:

```gitignore
.venv/
__pycache__/
*.pyc
users/*.json
products/*.json
```

## Publicação no GitHub

Depois de revisar os arquivos que serão enviados:

```bash
git init
git add ETL.py README.md .gitignore
git commit -m "Documenta pipeline ETL"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/pipeline-dados.git
git push -u origin main
```

Substitua `SEU-USUARIO` pelo seu usuário do GitHub e confirme que nenhum segredo ou dado real foi incluído antes do `git push`.

## Possíveis melhorias

- Corrigir o caminho de saída para as pastas locais.
- Criar um `requirements.txt` com a dependência `requests`.
- Usar `response.raise_for_status()` e configurar timeout nas requisições.
- Registrar erros com `logging`.
- Adicionar testes automatizados para extração e gravação.
- Permitir que endpoints e diretórios sejam configurados por argumentos ou variáveis de ambiente.
