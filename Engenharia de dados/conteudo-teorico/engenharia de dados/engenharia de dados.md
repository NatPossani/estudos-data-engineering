### O QUE É ENGENHARIA DE DADOS

&#x09;é responsável por coletar, transformar e disponibilizar os dados - série de processos que viabiliza o uso de dados em uma empresa



##### Fundamentos da Higienização

A higienização de dados é o processo de identificar e corrigir (ou remover) erros e inconsistências em conjuntos de dados brutos. Essa etapa é crucial para transformar dados desorganizados em informações confiáveis, tornando o produto final adequado para análises, geração de insights e tomada de decisão.



##### Mecanismos e Técnicas Utilizadas

Diversas estratégias podem ser empregadas na higienização. Entre elas, destacam-se:



Verificação de dados em branco ou nulos, que podem indicar ausência de informações importantes;

Detecção de valores duplicados ou inconsistentes que precisam ser consolidados ou removidos;

Padronização, onde os dados são formatados de forma uniforme (por exemplo, padronizando datas ou valores monetários) para evitar interpretações equivocadas.

Como exemplo, em Python com Pandas, é comum usar funções como dropna(), fillna() e duplicated() para identificar e tratar essas situações:



&#x09;*import pandas as pd*

&#x09;

&#x09;*# Suponha que df seja o DataFrame com os dados*

&#x09;*# Remover linhas com valores nulos*

&#x09;*df\_limpo = df.dropna()*

&#x09;

&#x09;*# Preencher valores nulos com um valor padrão*

&#x09;*df\_preenchido = df.fillna(0)*

&#x09;

&#x09;*# Remover duplicatas*

&#x09;*df\_unico = df.drop\_duplicates()*





### DADOS



##### o valor dos dados

&#x09;o valor está na informação, insights, decisões



##### transformar dados em valor não é simples

&#x09;- formatos inconsistentes

&#x09;-  baixa qualidade de dados

&#x09;- dificuldade de integração - entre times



###### &#x09;dificuldades técnicas

&#x09;	- processamento de grandes volumes

&#x09;	- escalabilidade da infraestrutura

&#x09;	- integração



###### &#x09;dificuldades culturais

&#x09;	- decisões baseadas apenas em opinião

&#x09;	- resistência ao uso de dados

&#x09;	- pouca colaboração entre areas



### PIPELINE DE DADOS

&#x09;serie de processos que vai coletar dados de diversas fontes, logo em seguida transforma esse dado (higienizar, tirar valores nulos, organizar, etc) e por último disponibilizamos para que seja usado por outras areas (cientistas e analistas de dados)



##### &#x09;ETL

&#x09;	- coleta

&#x09;	- transformação

&#x09;	- armazenamento



##### &#x09;ELT

&#x09;	- coleta

&#x09;	- armazenamento

&#x09;	- transformação



&#x09;a diferença entre eles é a ordem em que são realizados os processos



##### arquitetura mista

&#x09;A arquitetura mista em pipelines de dados propõe a utilização tanto de abordagens ETL quanto de ELT dentro do mesmo fluxo. Em vez de optar por um único modelo para todo o processo, essa estratégia mescla as etapas de extração, transformação e carregamento de maneira a aproveitar os pontos fortes de cada abordagem. Isso pode ser especialmente útil em cenários com diferentes tipos de fontes e necessidades de processamento, em que determinados dados exigem transformações imediatas, enquanto outros podem ser transformados posteriormente.



##### Motivações para a Adoção

&#x09;Adotar uma arquitetura mista pode trazer várias vantagens:



&#x09;- Flexibilidade Operacional: Permite que o engenheiro de dados adapte os processos de acordo com os requisitos específicos de cada conjunto de dados. Por exemplo, dados que chegam em alta frequência podem ser carregados rapidamente no ambiente para transformações posteriores, enquanto outros, que exigem validações mais rígidas, podem ser processados previamente.



&#x09;- Aproveitamento de Recursos: Em alguns casos, o ambiente de armazenamento (como um Data Lake) pode oferecer capacidades de processamento escaláveis, possibilitando a transformação dos dados já armazenados. Dessa forma, transfere-se parte da carga do processo inicial para uma fase posterior, otimizando recursos computacionais e garantindo agilidade nos fluxos críticos.



&#x09;- Adaptação ao Cenário de Negócio: Nem todos os dados requerem tratamento intensivo no momento da ingestão. Ao possibilitar decisões estratégicas – como quando transformar e validar os dados – a arquitetura mista se torna uma ferramenta valiosa para ambientes onde a volumetria e a variedade dos dados variam significativamente.



##### por que usamos pipeline de dados

&#x09;- padronização de dados

&#x09;- confiabilidade



### CICLO DE VIDA DE DADOS

&#x09;todas as etapas pelas quais os dados passam, desde sua criação ou coleta até o descarte

##### &#x09;sem processo estruturado

&#x09;	- dados ficam espalhados

&#x09;	- diferentes versões surgem

&#x09;	- difícil confiar nas informações



##### &#x09;benefícios

&#x09;	- garante governança

&#x09;	- segurança

&#x09;	- valor para organização



### COLETA E INGESTÃO DE DADOS

##### &#x09;primeira etapa do ciclo

&#x09;	dados podem vir de:

&#x09;		- APIs

&#x09;		- banco de dados

&#x09;		- sensores



##### &#x09;formas de coletar dados

&#x09;	- batch:

&#x09;		- coletados em intervalos

&#x09;	- streaming:

&#x09;		- coletados em tempo real (próximo de tempo real)



### ARMAZENAMENTO

##### &#x09;primeira etapa do ciclo

&#x09;	dados podem vir de:

&#x09;		- APIs

&#x09;		- banco de dados

&#x09;		- sensores



##### &#x09;formas de coletar dados

&#x09;	- batch:

&#x09;		- coletados em intervalos

&#x09;	- streaming:

&#x09;		- coletados em tempo real (próximo de tempo real)



### PROCESSAMENTO E TRANSFORMAÇÃO DOS DADOS

##### &#x09;problema

&#x09;		- dados duplicados

&#x09;		- formatos diferentes

&#x09;		- valores inconsistentes



##### &#x09;transformações

&#x09;		- limpeza de dados

&#x09;		- padronização de formatos

&#x09;		- agregação de informações



### CONSUMO DE DADOS

##### &#x09;formatos mais comuns

&#x09;		- dashboard

&#x09;		- modelos de machine learning

&#x09;		- relatórios



&#x09;aqui é onde os dados geram valor para o negócio



### LINGUAGENS DE PROGRAMAÇÃO

##### &#x09;linguagens

&#x09;		- python

&#x09;		- sql

&#x09;		- scala

&#x09;		- java



### FERRAMENTAS DE PROCESSAMENTO

&#x09;processamento simples nem sempre é eficiente



##### &#x09;para que serve

&#x09;		- transformar dados

&#x09;		- executar pipelines de processamento

&#x09;		- trabalhar com dados distribuído: capacidade de dividir uma tarefa pesada entre várias máquinas que trabalham de forma coordenada

&#x09;		

##### &#x09;ferramentas comuns

&#x09;		- apache spark: ferramenta de processamento distribuído, desenhada especificamente para lidar com grandes volumes de dados. sua principal vantagem é a capacidade de realizar processamentos complexos em paralelo, dividindo a carga entre várias máquinas para garantir alta performance

&#x09;		- apache kafka: plataforma focada no processamento de dados em fluxo (streaming) em tempo real, ou mais precisamente, próximo ao tempo real. ele é ideal para capturar e processar eventos no momento exato em que ocorrem, como cliques em um site ou transações, permitindo que os dados sejam disponibilizados para outras ferramentas quase instantaneamente

&#x09;		- pandas: biblioteca da linguagem python, extremamente eficiente para manipulação e análise de dados em volumes menores

&#x09;



### ORQUESTRAÇÃO DE PIPELINE

&#x09;pipelines de dados podem ter várias etapas e dependências



##### &#x09;sem organização

&#x09;		- tarefas podem falhar

&#x09;		- etapas podem rodas fora de ordem

&#x09;

##### &#x09;o que elas fazem

&#x09;		- agendar pipelines

&#x09;		- controlar dependências

&#x09;		- monitorar execuções

&#x09;



