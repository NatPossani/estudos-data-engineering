# ENGENHARIA DE DADOS

	é responsável por coletar, transformar e disponibilizar os dados - série de processos que viabiliza o uso de dados em uma empresa

#### fundamentos da higienização

	a higienização de dados é o processo de identificar e corrigir (ou remover) erros e inconsistências em conjuntos de dados brutos. essa etapa é crucial para transformar dados desorganizados em informações confiáveis, tornando o produto final adequado para análises, geração de insights e tomada de decisão

#### mecanismos e técnicas utilizadas

	diversas estratégias podem ser empregadas na higienização. entre elas, destacam-se:
	- verificação de dados em branco ou nulos, que podem indicar ausência de informações importantes
	- detecção de valores duplicados ou inconsistentes que precisam ser consolidados ou removidos
	- padronização, onde os dados são formatados de forma uniforme (por exemplo, padronizando datas ou valores monetários) para evitar interpretações equivocadas

	como exemplo, em python com pandas, é comum usar funções como dropna(), fillna() e duplicated() para identificar e tratar essas situações:

	import pandas as pd

	# suponha que df seja o dataframe com os dados
	# remover linhas com valores nulos
	df_limpo = df.dropna()

	# preencher valores nulos com um valor padrão
	df_preenchido = df.fillna(0)

	# remover duplicatas
	df_unico = df.drop_duplicates()


# DADOS

#### o valor dos dados

	o valor está na informação, insights, decisões

#### transformar dados em valor não é simples

	- formatos inconsistentes
	- baixa qualidade de dados
	- dificuldade de integração entre times

	dificuldades técnicas
	- processamento de grandes volumes
	- escalabilidade da infraestrutura
	- integração

	dificuldades culturais
	- decisões baseadas apenas em opinião
	- resistência ao uso de dados
	- pouca colaboração entre áreas


# PIPELINE DE DADOS

	série de processos que vai coletar dados de diversas fontes, logo em seguida transforma esse dado (higienizar, tirar valores nulos, organizar, etc) e por último disponibilizamos para que seja usado por outras áreas (cientistas e analistas de dados)

#### ETL
	- coleta
	- transformação
	- armazenamento

#### ELT
	- coleta
	- armazenamento
	- transformação

	a diferença entre eles é a ordem em que são realizados os processos

#### arquitetura mista

	a arquitetura mista em pipelines de dados propõe a utilização tanto de abordagens ETL quanto de ELT dentro do mesmo fluxo. em vez de optar por um único modelo para todo o processo, essa estratégia mescla as etapas de extração, transformação e carregamento de maneira a aproveitar os pontos fortes de cada abordagem. isso pode ser especialmente útil em cenários com diferentes tipos de fontes e necessidades de processamento, em que determinados dados exigem transformações imediatas, enquanto outros podem ser transformados posteriormente

#### motivações para a adoção

	- flexibilidade operacional: permite que o engenheiro de dados adapte os processos de acordo com os requisitos específicos de cada conjunto de dados. por exemplo, dados que chegam em alta frequência podem ser carregados rapidamente no ambiente para transformações posteriores, enquanto outros, que exigem validações mais rígidas, podem ser processados previamente
	- aproveitamento de recursos: em alguns casos, o ambiente de armazenamento (como um data lake) pode oferecer capacidades de processamento escaláveis, possibilitando a transformação dos dados já armazenados. dessa forma, transfere-se parte da carga do processo inicial para uma fase posterior, otimizando recursos computacionais e garantindo agilidade nos fluxos críticos
	- adaptação ao cenário de negócio: nem todos os dados requerem tratamento intensivo no momento da ingestão. ao possibilitar decisões estratégicas – como quando transformar e validar os dados – a arquitetura mista se torna uma ferramenta valiosa para ambientes onde a volumetria e a variedade dos dados variam significativamente

#### por que usamos pipeline de dados

	- padronização de dados
	- confiabilidade


# CICLO DE VIDA DE DADOS

	todas as etapas pelas quais os dados passam, desde sua criação ou coleta até o descarte

#### sem processo estruturado
	- dados ficam espalhados
	- diferentes versões surgem
	- difícil confiar nas informações

#### benefícios
	- garante governança
	- segurança
	- valor para organização


### COLETA E INGESTÃO DE DADOS

#### primeira etapa do ciclo
	dados podem vir de:
	- APIs
	- banco de dados
	- sensores

#### formas de coletar dados
	- batch: coletados em intervalos
	- streaming: coletados em tempo real (próximo de tempo real)


### ARMAZENAMENTO

#### primeira etapa do ciclo
	dados podem vir de:
	- APIs
	- banco de dados
	- sensores

#### formas de coletar dados
	- batch: coletados em intervalos
	- streaming: coletados em tempo real (próximo de tempo real)


### PROCESSAMENTO E TRANSFORMAÇÃO DOS DADOS

#### problema
	- dados duplicados
	- formatos diferentes
	- valores inconsistentes

#### transformações
	- limpeza de dados
	- padronização de formatos
	- agregação de informações


### CONSUMO DE DADOS

#### formatos mais comuns
	- dashboard
	- modelos de machine learning
	- relatórios

	aqui é onde os dados geram valor para o negócio


### LINGUAGENS DE PROGRAMAÇÃO

#### linguagens
	- python
	- sql
	- scala
	- java


### FERRAMENTAS DE PROCESSAMENTO

	processamento simples nem sempre é eficiente

#### para que serve
	- transformar dados
	- executar pipelines de processamento
	- trabalhar com dados distribuídos: capacidade de dividir uma tarefa pesada entre várias máquinas que trabalham de forma coordenada

#### ferramentas comuns
	- apache spark: ferramenta de processamento distribuído, desenhada especificamente para lidar com grandes volumes de dados. sua principal vantagem é a capacidade de realizar processamentos complexos em paralelo, dividindo a carga entre várias máquinas para garantir alta performance
	- apache kafka: plataforma focada no processamento de dados em fluxo (streaming) em tempo real, ou mais precisamente, próximo ao tempo real. ele é ideal para capturar e processar eventos no momento exato em que ocorrem, como cliques em um site ou transações, permitindo que os dados sejam disponibilizados para outras ferramentas quase instantaneamente
	- pandas: biblioteca da linguagem python, extremamente eficiente para manipulação e análise de dados em volumes menores


### ORQUESTRAÇÃO DE PIPELINE

	pipelines de dados podem ter várias etapas e dependências

#### sem organização
	- tarefas podem falhar
	- etapas podem rodar fora de ordem

#### o que elas fazem
	- agendar pipelines
	- controlar dependências
	- monitorar execuções
