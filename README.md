# Estudos de Python e Engenharia de Dados

Repositório pessoal de estudos sobre Python, Ciência de Dados, Computação em Nuvem e Engenharia de Dados. O conteúdo reúne anotações teóricas, notebooks de aulas e exercícios, pequenos projetos em Python e um pipeline ETL com a API DummyJSON.

## Conteúdo do repositório

### Computação em nuvem

[computação em nuvem.md](conteudo-teorico/computacao%20em%20nuvem/computa%C3%A7%C3%A3o%20em%20nuvem.md) reúne anotações sobre:

- conceitos, características e benefícios da computação em nuvem;
- modelos IaaS, PaaS, SaaS, CaaS, FaaS e DaaS;
- responsabilidade compartilhada e segurança;
- nuvens pública, privada, híbrida, comunitária e multicloud;
- termos básicos, como `on-premise`.

### Notebooks Google Colab

Os notebooks podem ser abertos no Google Colab, no Jupyter Notebook ou no VS Code:

- [Aula_01_Python_para_Data_Science.ipynb](conteudo-teorico/google%20colab/Aula_01_Python_para_Data_Science.ipynb): introdução a Python para Data Science, `matplotlib`, gráficos, funções, médias, `lambda`, `map`, listas, tuplas e dicionários.
- [Ciência_de_Dados_Dia_01.ipynb](conteudo-teorico/google%20colab/Ci%C3%AAncia_de_Dados_Dia_01.ipynb): introdução à Ciência de Dados, Pandas, Series, DataFrames, métricas, seleção e filtragem de dados.
- [dia02.ipynb](conteudo-teorico/google%20colab/dia02.ipynb): pré-processamento e limpeza dos datasets Iris e Penguins, incluindo conversão de tipos, tratamento de valores ausentes e padronização de colunas.
- [exercicios.ipynb](conteudo-teorico/google%20colab/exercicios.ipynb): exercícios de Python, Pandas e limpeza de dados.
- [Projeto_Python_Data_Science(1).ipynb](conteudo-teorico/google%20colab/Projeto_Python_Data_Science%281%29.ipynb): fundamentos de Python, com variáveis, tipos, strings, entrada de dados, condicionais, laços, listas, tuplas, dicionários e funções.

#### Dependências dos notebooks

Os notebooks utilizam Python e, conforme o arquivo, `pandas`, `numpy`, `matplotlib`, `seaborn` e `scikit-learn`. Alguns também usam `google.colab` e arquivos armazenados no Google Drive.

Os arquivos externos esperados incluem `spotify_processed.csv`, `iris_sujo.csv`, `iris.csv` e `penguins_lter_sujo_maior.csv`. Os caminhos originais apontam para o Google Drive do ambiente em que as aulas foram produzidas; por isso, podem precisar ser adaptados antes da execução local.

O notebook `Projeto_Python_Data_Science(1).ipynb` contém células vazias, exemplos incompletos e uma saída com erro de sintaxe preservado. Ele deve ser entendido como material didático, e não como um programa que necessariamente executa do início ao fim sem ajustes.

### Projetos simples

Os programas abaixo usam a biblioteca padrão do Python e são executados pelo terminal:

- [number-guesser.py](estudos-python/projetos%20simples/number-guesser.py): jogo de adivinhação de números aleatórios.
- [quiz.py](estudos-python/projetos%20simples/quiz.py): quiz interativo com oito perguntas sobre hardware e informática, com pontuação final.
- [rock_paper_scissors.py](estudos-python/projetos%20simples/rock_paper_scissors.py): jogo de pedra, papel e tesoura contra o computador, com placar.

Exemplos no PowerShell, a partir da raiz do repositório:

```powershell
python "estudos-python\projetos simples\number-guesser.py"
python "estudos-python\projetos simples\quiz.py"
python "estudos-python\projetos simples\rock_paper_scissors.py"
```

### Projetos de POO

- [musica.py](estudos-python/projetos%20POO/musica.py): criação da classe `Musica`, instanciação de objetos e exibição dos atributos.
- [restaurante.py](estudos-python/projetos%20POO/restaurante.py): classe `Restaurante`, atributos de instância, atributo de classe, método de listagem e representação dos objetos.

Execução:

```powershell
python "estudos-python\projetos POO\musica.py"
python "estudos-python\projetos POO\restaurante.py"
```

### Pipeline ETL

O diretório [pipeline-dados/pipeline-1](pipeline-dados/pipeline-1/) contém um pipeline que consulta a API pública [DummyJSON](https://dummyjson.com/), transforma os dados mantendo o formato recebido e salva cada registro em um arquivo JSON.

- [ETL.py](pipeline-dados/pipeline-1/ETL.py): implementa extração, transformação e carga de usuários e produtos.
- [README.md](pipeline-dados/pipeline-1/README.md): documentação específica do pipeline.
- `users/1.json` até `users/19.json`: registros de usuários retornados pela API.
- `products/`: diretório reservado para os registros de produtos; atualmente está vazio.

Para configurar e executar o ETL:

```powershell
Set-Location "pipeline-dados\pipeline-1"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install requests
python ETL.py
```

A implementação atual possui limitações documentadas no README do pipeline: a URL dos registros precisa usar uma barra antes do ID, o diretório de saída deve ser criado corretamente e as requisições deveriam ter timeout e tratamento de exceções. Portanto, revise esses pontos antes de considerar a execução reproduzível em uma instalação nova.

Os JSON podem conter campos sensíveis simulados, como senha, cartão, IBAN e SSN. Mesmo sendo dados fictícios de demonstração, revise-os antes de publicar no GitHub.

## Estrutura completa

```text
.
├── README.md
├── conteudo-teorico/
│   ├── computacao em nuvem/
│   │   └── computação em nuvem.md
│   └── google colab/
│       ├── Aula_01_Python_para_Data_Science.ipynb
│       ├── Ciência_de_Dados_Dia_01.ipynb
│       ├── dia02.ipynb
│       ├── exercicios.ipynb
│       └── Projeto_Python_Data_Science(1).ipynb
├── estudos-python/
│   ├── projetos POO/
│   │   ├── musica.py
│   │   └── restaurante.py
│   └── projetos simples/
│       ├── number-guesser.py
│       ├── quiz.py
│       └── rock_paper_scissors.py
└── pipeline-dados/
    └── pipeline-1/
        ├── ETL.py
        ├── README.md
        ├── products/
        └── users/
            ├── 1.json ... 9.json
            └── 10.json ... 19.json
```

## Requisitos gerais

- Python 3 para os scripts e notebooks;
- Jupyter, VS Code ou Google Colab para os notebooks;
- `requests` para o pipeline ETL;
- `pandas`, `numpy`, `matplotlib`, `seaborn` e `scikit-learn` para os notebooks que utilizam essas bibliotecas.

Recomenda-se usar um ambiente virtual para as dependências do pipeline. Ainda não existe um `requirements.txt` centralizado.

## Versionamento

Artefatos locais de execução não fazem parte do conteúdo de estudo e devem ser ignorados pelo Git:

```gitignore
.venv/
__pycache__/
*.pyc
```

Se os JSON forem gerados pelo ETL e não fizerem parte do objetivo do repositório, também podem ser adicionados ao `.gitignore`:

```gitignore
pipeline-dados/pipeline-1/users/*.json
pipeline-dados/pipeline-1/products/*.json
```

Antes de publicar, verifique se não há senhas, tokens, dados pessoais reais ou arquivos gerados que não deveriam ser versionados.

## Próximos passos sugeridos

- corrigir a montagem das URLs e dos caminhos de saída do ETL;
- adicionar timeout e tratamento de erros HTTP;
- criar um `requirements.txt`;
- substituir caminhos absolutos do Google Drive por caminhos configuráveis;
- adicionar testes automatizados para os scripts e para o pipeline.
