# COMPUTAÇÃO EM NUVEM

	um modelo para permitir acesso obliquo, conveniente e sob demanda via rede a um agrupamento compartilhado e configurável de recursos computacionais (como redes, servidores, armazenamento, aplicações e serviços), que pode ser rapidamente provisionado e liberado com esforço mínimo de gerenciamento ou interação com provedor de serviços

	alguns exemplos
	- google drive/OneDrive
	- netflix
	- Microsoft 365


### principais características

	- autoatendimento sob demanda: provisionar recursos com a interação minima/quase nula
	- amplo acesso a rede: a nuvem pode ser acessada em qualquer lugar
	- agrupamento de recursos: confidencialidade de seus recursos (somente sua empresa pode acessar os recursos)
	- elasticidade rápida: representa a capacidade do armazenamento em nuvem se adaptarem com a quantidade de demanda referente a ela
	- serviço mensurável: custos e gastos proveniente do serviço em nuvem


### beneficios

	- escalabilidade: ajuste dinamico de recursos com cobrança proporcional ao uso
	- economia de custos: infraestrutura economica sem investimento inicial
	- segurança aprimorada: adição do fator segurança fisica de ponta do provedor de nuvem
	- disponibilidade global: acesso de qualquer lugar
	- resiliencia e backup: capacidade robusta de recuperação para continuidade dos negocios
	- inovação: inovação ágil e economica com tecnologias em nuvem


### modelos de serviço

	define o nivel de controle e responsabilidade entre provedor e cliente

#### IaaS (infrastructure as a service)

	oferece recursos computacionais virtualizados via internet, como servidores, rede e armazenamento
	- recursos sob demanda
	- alta escalabilidade/elasticidade
	- maior controle do ambiente
	- eliminação de estrutura fisica
	- acesso remoto via internet
	- automação e orquestração
	- modelo de pagamento flexivel

#### PaaS (plataform as a service)

	ambiente complexo para desenvolver, executar e gerenciar aplicativos (interpretadores, bibliotecas, aplicativos de desenvolvimento)
	- ambiente completo para desenvolvimento
	- abstração da infraestrutura
	- escalabilidade automatica
	- implantação simplificada
	- modelo de pagamento flexivel

#### SaaS (software as a service)

	software pronto para uso, acessivel pela internet
	- gerenciamento e manutenção pelo provedor
	- atualizações por responsabilidade do provedor
	- segurança e backup gerenciados pelo provedor
	- escalabilidade sob demanda
	- multi-tenant (varios clientes utilizam o mesmo software)
	- modelo de assinatura

outros modelos
	- Caas (container as a service)
	- Faas (function as a service/serveless computing)
	- Daas (desktop as a service)


### quais as diferenças entre os modelos de serviço

	- diferentes niveis de responsabilidade
	- IaaS: mais controle, mas exige mais responsabilidade do cliente
	- PaaS: equilibra agilidade com segurança compartilhada
	- SaaS: transfere quase toda a responsabilidade ao provedor, mas o cliente ainda precisa gerencias quem acessa e como


### modelos sob a otica de segurança

#### riscos comuns
	- IaaS: ma configuração de firewall, falta de patch, exposição de dados
	- PaaS: vulnerabilidade no codigo da aplicação, ma gestao de dados
	- SaaS: acesso indevido por usuarios, uso indevido de dados

#### exemplos de boas praticas
	- IaaS: hardening de SO, criptografia, IAM, monitoramento com cloudwatch ou azure monitor
	- PaaS: validaçao de entrada, criptografia de dados, controle de acesso
	- SaaS: autenticaçao multifator, gestao de identidade, revisao de permissoes


### o que é um modelo de responsabilidade compartilhada

	é uma estruruta que define de forma clara as obrigaçoes do provedor de nuvem e do cliente
	- pilar fundamental da segurança em nuvem


### por que ele é importante?

	define quem é o responsavel pela:
	- utilização
	- gestao
	- conformidade
	- segurança


### modelos de implantaçao

	os recursos e serviços de computação em nuvem sao organizados e disponibilizados

#### nuvem publica

	caracteristicas
	- infraestrutura física é do provedores de nuvem
	- acesso atraves da internet
	- hardware compartilhado com varias empresas

	vantagens
	- reduçao de custos
	- sem necessidade de manutenção fisica
	- acesso a tecnologias emergentes
	- escalabilidade quase ilimitada
	- alta confiabilidade

	desafios de segurança
	- responsabilidade pela segurança compartilhada
	- solução de problemas apenas em escala digital/logica
	- descobertas de profissionais especializados
	- conformidade e auditoria

#### nuvem privada

	caracteristicas
	- hardware dedicado ao cliente
	- maior controle e personalização (data center local)
	- recursos isolados
	- custo mais elevado

	vantagens
	- maior escalabilidade
	- segurança controlada pelo cliente* (ainda tem uma parte da segurança que é responsabilizada pelo provedor)
	- conformidade com normas regulatórias
	- personalização e integração com sistemas lógicos
	- melhor governança de dados

	desafios de segurança
	- responsabilidade quase total pela segurança
	- complexidade na gestão de ambientes
	- escassez de profissionais especializados
	- limitação na capacidade de monitoramento do ambiente
	- conformidade e auditoria sob responsabilidade total

#### nuvem hibrida (o modelo mais utilizado)

	caracteristicas
	- uso da nuvem publica e privada
	- integração entre ambientes
	- acesso via internet

	vantagens
	- flexibilidade estratégica
	- escalabilidade sob demanda
	- maior controle sobre os dados
	- continuidade de negocio e resiliencia
	- otimização de custos operacionais
	- modernizaçao gradual da ti

	desafios de segurança
	- visibilidade limitada e controle fragmentado
	- integração segura entre ambientes
	- complexibilidade operacional
	- latencia
	- superficie de ataque ampliada

#### nuvem comunitaria

	caracteristicas
	- infraestrutura compartilhada com outros clientes
	- gerenciamento colaborativo
	- ambiente dedicado
	- custos distribuidos entre os participantes

#### modelo multicloud

	caracteristicas
	- 2 ou mais provedores de nuvem
	- infraestruturas diferentes na nuvem se conectam
	- amplitude de serviços

	vantagens
	- redução do risco de dependencia de fornecedor (vendor lock-in)
	- flexibilidade na adoção do melhor recurso de cada plataforma
	- melhoria na recuperação de desastre
	- otimização de custos
	- maior alcance geografico

	desafios de segurança
	- visibilidade limitada e controle fragmentado
	- conformidade regulatoria
	- gerenciamento de identidade e acesso
	- integração entre as clouds
	- superficie de ataque ampliada


### PROVEDORES DE NUVEM

	empresas que oferecem serviços de computação em nuvem (de diversos modelos) através da internet
	- autoatendimento sob demanda
	- amplo acesso a rede
	- agrupamento de recursos
	- elasticidade rapida
	- serviço mensuravel

	principais provedores do mercado
	- AWS
	- Microsoft AZURE
	- google cloud plataform (gcp)

#### AWS

	é a escolha mais madura e versátil, ideal para empresas que buscam amplitude de serviços e escala global

	pontos fortes
	- maior maturidade e variedade de serviços
	- presença global consolidada

	diferenciais estrategicos
	- ampla comunidade e suporte técnico
	- serviços avançados em computação, ia e iot

#### microsoft AZURE

	se destaca em ambientes corporativos e hibridos, com forte integração ao ecossistema microsoft

	pontos fortes
	- integração nativa com produtos microsoft
	- suporte a soluções multicloud com azure arc

	diferenciais estrategicos
	- ideal para empresas que ja usam microsoft
	- liderança em nuvem hibrida

#### GCP - google cloud plataform

	é referencia em dados, ia e inovação, sendo muito atrativo para startups, cientistas de dados e empresas digitais

	pontos fortes
	- exelencia com dados, analytics e ia
	- preços competitivos e modelo de cobrança por segundo

	diferenciais estrategicos
	- ideal para workloads de big data e machine learning
	- integração com serviços google
	- foco em inovação e open source


# VIRTUAL MACHINES

	uma maquina virtual é um recurso lógico que simula um computador físico, com um sistema operacional

	características
	- elasticidade
	- portabilidade
	- snapshots e imagens
	- suporte a diversos SOs
	- alta disponibilidade

	tipos de vm
	- uso geral
	- otimizadas para computação
	- otimizadas para memoria
	- otimizadas para armazenamento
	- propositos específicos


# STORAGES

	storage em nuvem é um modelo de armazenamento de dados em que arquivos, bancos de dados e backups sao mantidos em data centers de provedores de nuvem

	caracteristicas
	- acesso remoto
	- escalabilidade elastica
	- alta durabilidade

	tipos de armazenamento
	- armazenamento em blocos
	- armazenamento de arquivos
	- armazenamento de objetos


# BANCO DE DADOS

	um banco de dados é uma coleção organizada de informações ou dados

	caracteristicas
	- tabelas com colunas e linhas
	- armazena de forma consistente e segura
	- escalabilidade sob demanda
	- alta disponibilidade
	- gerenciamento simplificado (dependendo do modelo de serviço)
	- desempenho otimizado

	tipos de banco de dados
	- banco de dados relacional (sql)
	- banco de daados nao relacional (NoSQL)
	- banco de dados em memória
	- data warehouse


# REDES

	redes em nuvem referem-se à infraestrutura e aos serviços que permitem a conectividade entre recursos, aplicações e usuários dentro e fora da nuvem

	caracteristicas
	- redes virtuais (vpc/vcn)
	- escalabilidade sob demanda
	- segurança integrada
	- conectividade híbrida
	- gerenciamento centralizado

	tipos de serviços de rede
	- rede virtual (vpc/vnet)
	- vpn e conectividade
	- balanceamento de carga
	- dns
	- cdn (content delivery network)
	- firewall e segurança de rede
	- monitoramento e diagnóstico


# COMPUTAÇÃO SERVELESS

	modelo de desenvolvimento de aplicações - criar e implantar aplicações em uma infraestrutura de servidores gerenciados pelos provedores de nuvem

	como funciona
	1. é criado uma função ou gatilho
	2. o provedor executa essas funções sob demanda

	beneficios
	- zero preocupação com servidores físicos ou virtuais
	- alta escalabilidade
	- economia (paga-se apenas pelo uso)
	- foco total no código e na lógica de negócio

	cuidados
	- startup delay
	- limitações de tempo de execução e recursos
	- menor controle sobre a infraestrutura

	casos de uso
	- processamento de imagens e videos
	- APIs e microsserviços
	- automação de tarefas e agendamentos
	- integração com IoT
	- chatbots e assistentes virtuais
	- notificações e envio de emails
