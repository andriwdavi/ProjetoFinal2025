# DOCUMENTO DE VISÃO

## SISTEMA DE GERENCIAMENTO PARA CLUBE DE DESBRAVADORES

## Situação problema

O Clube de desbravadores é uma organização cristã para-militar da igreja
adventista do sétimo dia inspirada nos escoteiros, mas com adições
espirituais e ensinamentos sobre saúde, cuidado próprio e trabalho em
equipe. O clube funciona para juvenis de 10 à 15 anos, os quais são
divididos por idade e gênero. As chamadas "unidades" possuem
desbravadores da mesma faixa de idade e gênero, cada unidade possui um
ou mais líderes chamados "conselheiros", além de que cada desbravador
tem um cargo e função dentro de sua unidade. A junção de todas as
unidades e liderança forma o clube de desbravadores e existem dezenas de
milhares de clubes ao redor do mundo.

Os líderes de cada clube são jovens e adultos voluntários com 16 anos ou
mais, cada um deles também possui uma função, como conselheiro,
instrutor, capelão, vice-diretor etc.\
A situação problema trata da constante falta de organização em frente a
tantos membros, cargos e divisões, que são muitas vezes mal organizadas.

## Solução proposta

Propõe-se uma intervenção que tem o objetivo de organizar todo o clube e
alocar as inscrições dos membros em perfis.

Os perfis irão conter todas as informações de cada um dos membros ativos
no clube de desbravadores. O projeto tem como alvo um sistema que pode
ser replicado e serve para qualquer clube de desbravador espalhado pelo
mundo, com a única necessidade de adaptação sendo o idioma do sistema.

Cada perfil terá:

-   Informação indicando se o membro é desbravador ou pertence à
    liderança.
-   Alocação da unidade à qual o desbravador irá pertencer baseado em
    idade e gênero.
-   Informação de sua função dentro de sua unidade (se for desbravador).
-   Informação de sua função dentro do clube (se for líder).
-   Credencial de login para consultar seus dados.
-   Permissões específicas dependendo do cargo.
-   Informações sobre as classes, que são livros didáticos sobre
    espiritualidade, saúde, técnicas de sobrevivência e acampamento.

## Stakeholders e suas necessidades

Os stakeholders serão todos os membros ativos de um clube, que em
conjunto formam os usuários finais do produto.

-   Sistema limpo, prático e intuitivo.
-   Funcionamento fluído.
-   Armazenamento seguro de informações.

O desenvolvedor do projeto também é stakeholder:

-   Necessidade de cumprir todos os objetivos e construir um sistema
    completamente funcional.

## Requisitos funcionais

-   RF001 -- "CRUD do usuário"
-   RF002 -- "Acessar sistema"
-   RF003 -- "Atribuir, atualizar ou retirar unidade"
-   RF004 -- "Atribuir, atualizar ou retirar cargo"
-   RF005 -- "Atribuir, atualizar ou retirar função"
-   RF006 -- "CRUD de unidade"
-   RF007 -- "Investir classe"

## Requisitos não funcionais

-   RNF001 -- "Controle de acesso" (Segurança, obrigatório)
-   RNF002 -- "Interface intuitiva" (Usabilidade, importante)
-   RNF003 -- "Padronização visual" (Usabilidade, desejável)
-   RNF004 -- "Facilidade de uso" (Usabilidade, importante)
-   RNF005 -- "Backup automático" (Confiabilidade, obrigatório)
-   RNF006 -- "Integridade de dados" (Confiabilidade, importante)
-   RNF007 -- "Código estruturado" (Manutenibilidade, desejável)

## Casos de uso

-   CDU001 -- "Cadastrar desbravador"
-   CDU002 -- "Cadastrar conselheiro"
-   CDU003 -- "Fazer login"
-   CDU004 -- "Criar unidade"
-   CDU005 -- "Atribuir cargo"
-   CDU006 -- "Atribuir função"
-   CDU007 -- "Atribuir unidade"
-   CDU008 -- "Investir classe"
