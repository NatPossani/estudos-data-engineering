# computação em nuvem



### o que é

&#x09;um modelo para permitir acesso obliquo, conveniente e sob demanda via rede a um agrupamento compartilhado e configurável de recursos computacionais (como redes, servidores, armazenamento, aplicações e serviços), que pode ser rapidamente provisionado e liberado com esforço mínimo de gerenciamento ou interação com provedor de serviços



&#x09;alguns exemplos

&#x09;	- google drive/OneDrive

&#x09;	- netflix

&#x09;	- Microsoft 365



### principais características

&#x09;- autoatendimento sob demanda: provisionar recursos com a interação minima/quase nula

&#x09;- amplo acesso a rede: a nuvem pode ser acessada em qualquer lugar

&#x09;- agrupamento de recursos: confidencialidade de seus recursos (somente sua empresa pode acessar os recursos)

&#x09;- elasticidade rápida: representa a capacidade do armazenamento em nuvem se adaptarem com a quantidade de demanda referente a ela

&#x09;- serviço mensurável: custos e gastos proveniente do serviço em nuvem



### beneficios

&#x09;- escalabilidade: **ajuste dinamico de recursos** com cobrança proporcional ao uso

&#x09;- economia de custos: infraestrutura economica **sem investimento inicial**

&#x09;- segurança aprimorada: adição do fator **segurança fisica de ponta** do provedor de nuvem

&#x09;- disponibilidade global: acesso de qualquer lugar

* resiliencia e backup: capacidade **robusta de recuperação para continuidade** dos negocios

&#x09;- inovação: **inovação ágil e economica** com tecnologias em nuvem





### modelos de serviço

&#x09;define o **nivel de controle e responsabilidade** entre provedor e cliente



#### IaaS(infrastructure as a service)

&#x09;oferece recursos computacionais virtualizados via internet, como servidores, rede e armazenamento

&#x09;- recursos sob demanda

&#x09;- alta escalabilidade/elasticidade

&#x09;- maior controle do ambiente

&#x09;- eliminação de estrutura fisica

&#x09;- acesso remoto via internet

&#x09;- automação e orquestração

&#x09;- modelo de pagamento flexivel



#### PaaS(plataform as a service)

&#x09;ambiente complexo para desenvolver, executar e gerenciar aplicativos (interpretadores, bibliotecas, aplicativos de desenvolvimento)

&#x09;- ambiente completo para desenvolvimento

&#x09;- abstração da infraestrutura

&#x09;- escalabilidade automatica

&#x09;- implantação simplificada

&#x09;- modelo de pagamento flexivel



#### SaaS(software as a service)

&#x09;software pronto para uso, acessivel pela internet

&#x09;- gerenciamento e manutenção pelo provedor

&#x09;- atualizações por responsabilidade do provedor

&#x09;- segurança e backup gerenciados pelo provedor

&#x09;- escalabilidade sob demanda

&#x09;- multi-tenant (varios clientes utilizam o mesmo software)

&#x09;- modelo de assinatura



outros modelos

* Caas (container as a service)

&#x09;- Faas (function as a service/serveless computing)

&#x09;- Daas (desktop as a service)



### quais as diferenças entre os modelos de serviço

&#x09;- diferentes niveis de responsabilidade

&#x09;	- IaaS: mais controle, mas exige mais responsabilidade do cliente

&#x09;	- PaaS: equilibra agilidade com segurança compartilhada

&#x09;	- SaaS: transfere quase toda a responsabilidade ao provedor, mas o cliente ainda precisa gerencias quem acessa e como



### modelos sob a otica de segurança



##### riscos comuns

&#x09;- IaaS: ma configuração de firewall, falta de patch, exposição de dados

&#x09;- PaaS: vulnerabilidade no codigo da aplicação, ma gestao de dados

&#x09;- SaaS: acesso indevido por usuarios, uso indevido de dados



##### exemplos de boas praticas

&#x09;- IaaS: hardening de SO, criptografia, IAM, monitoramento com cloudwatch ou azure monitor

&#x09;- PaaS: validaçao de entrada, criptografia de dados, controle de acesso

&#x09;- SaaS: autenticaçao multifator, gestao de identidade, revisao de permissoes



### o que é um modelo de responsabilidade compartilhada

&#x09;é uma estruruta que define de forma clara as obrigaçoes do provedor de nuvem e do cliente

&#x09;- pilar fundamental da segurança em nuvem



### por que ele é importante?

&#x09;- define quem é o responsavel pela:

&#x09;	- utilização

&#x09;	- gestao

&#x09;	- conformidade

&#x09;	- segurança



### modelos de implantaçao

&#x20;	os recursos e serviços de computação em nuvem sao organizados e disponibilizados

##### 

##### nuvem publica

&#x09;caracteristicas

&#x09;	- infraestrutura física é do provedores de nuvem

&#x09;	- acesso atraves da internet

&#x09;	- hardware compartilhado com varias empresas



&#x09;vantagens

&#x09;	- reduçao de custos

&#x09;	- sem necessidade de manutenção fisica

&#x09;	- acesso a tecnologias emergentes

&#x09;	- escalabilidade quase ilimitada

&#x09;	- alta confiabilidade



&#x09;desafios de segurança

&#x09;	- responsabilidade pela segurança compartilhada

&#x09;	- solução de problemas apenas em escala digital/logica

&#x09;	- descobertas de profissionais especializados

&#x09;	- conformidade e auditoria



##### nuvem privada

&#x09;caracteristicas

&#x09;	- hardware dedicado ao cliente

&#x09;	- maior controle e personalização (data center local)

&#x09;	- recursos isolados

&#x09;	- custo mais elevado



&#x09;vantagens

&#x09;	- maior escalabilidade

&#x09;	- segurança controlada pelo cliente\* (ainda tem uma parte da segurança que é responsabilizada pelo provedor)

&#x09;	- conformidade com normas regulatórias

&#x09;	- personalização e integração com sistemas lógicos

&#x09;	- melhor governança de dados



&#x09;desafios de segurança

&#x09;	- responsabilidade quase total pela segurança

&#x09;	- complexidade na gestão de ambientes

&#x09;	- escassez de profissionais especializados

&#x09;	- limitação na capacidade de monitoramento do ambiente

&#x09;	- conformidade e auditoria sob responsabilidade total

##### 

##### nuvem hibrida (o modelo mais utilizado)

&#x09;caracteristicas

&#x09;	- uso da nuvem publica e privada

&#x09;	- integração entre ambientes

&#x09;	- acesso via internet



&#x09;vantagens

&#x09;	- flexibilidade estratégica

&#x09;	- escalabilidade sob demanda

&#x09;	- maior controle sobre os dados

&#x09;	- continuidade de negocio e resiliencia

&#x09;	- otimização de custos operacionais

&#x09;	- modernizaçao gradual da ti

&#x09;

&#x09;desafios de segurança

&#x09;	- visibilidade limitada e controle fragmentado

&#x09;	- integração segura entre ambientes

&#x09;	- complexibilidade operacional

&#x09;	- latencia

&#x09;	- superficie de ataque ampliada



#### nuvem comunitaria

&#x09;caracteristicas

&#x09;	- infraestrutura ompartilhada com outros clientes

&#x09;	- gerenciamento colaborativo

&#x09;	- ambiente dedicado

&#x09;	- custos distribuidos entre os participantes



##### modelo multicloud

&#x09;caracteristicas

&#x09;	- 2 ou mais provedores de nuvem

&#x09;	- infraestruturas diferentes na nuvem se conectam

&#x09;	- amplitude de serviços



&#x09;vantagens

&#x09;	- redução do risco de dependencia de fornecedor (vendor lock-in)

&#x09;	- flexibilidade na adoção do melhor recurso de cada plataforma

&#x09;	- melhoria na recuperação de desastre

&#x09;	- otimização de custos

&#x09;	- maior alcance geografico



&#x09;desafios de segurança

&#x09;	- visibilidade limitada e controle fragmentado

&#x09;	- conformidade regulatoria

&#x09;	- gerenciamento de identidade e acesso

&#x09;	- integraçao entre as clouds

&#x09;	- superficie de ataque ampliada







\------------------------------------------------------------



dicionario



on-premise: infraestrutura local

