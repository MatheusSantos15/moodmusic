# MoodMusic

MoodMusic é um sistema de microsserviços que foi criado para a matéria de Desenvolvimento de APIs e Microsserviços. A proposta da aplicação é sugerir músicas aos usuários conforme os humores que eles registram, evidenciando na prática conceitos essenciais de arquitetura distribuída, comunicação entre serviços, autenticação, mensageria e monitoramento.
Para a construção da solução, foram utilizados FastAPI, PostgreSQL, Apache Kafka, Docker, Prometheus e Grafana, que se organizam em quatro microsserviços independentes: User Service, Music Service, Recommendation Service e History Service. O projeto também proporciona comunicação assíncrona via Kafka, além da comunicação síncrona com APIs REST, para registrar o histórico de recomendações.
O sistema doi criado com o objetivo de ser didático, utilizando técnicas modernas que são amplamanete adotadas no setor da tecnologia, como autenticação JWT, containerização via Docker, e observabilidade por meio de métricas e monitoramento centralizado.

## Demonstração
A demonstração completa do sistema pode ser acessada através do vídeo abaixo:
*Video de Demonstração:* (LINK)

## Arquitetura

A arquitetura do MoodMusic segue o padrão de microsserviços, onde cada serviço possui uma responsabilidade específica e se comunica com os demais por meio de APIs REST e eventos Kafka.

### Diagrama da Arquitetura
<img width="623" height="771" alt="image" src="https://github.com/user-attachments/assets/ead0c16b-83dd-4a06-b5ac-6a638596b6e4" />

### Componentes da Solução
- User Service: Gerenciamento de usuários e autenticação JWT.
- Music Service: Gerenciamento e consulta do catálogo musical.
- Recommendation Service: Geração de recomendações com base no humor do usuário.
- History Service: Armazenamento do histórico de recomendações.
- Apache Kafka: Comunicação assíncrona entre Recommendation Service e History Service.
- PostgreSQL: Persistência dos dados da aplicação.
- Prometheus: Coleta de métricas dos micresserviços
- Grafana: visualização e monitoramento das métricas coletadas.

##Tecnologias Utilizadas

Para o desenvolvimento do MoodMusic, foram utilizadas tecnologias contemporâneas que se concentram na criação de APIs, na arquitetura de microsserviços, na comunicação assíncrona, na observabilidade e na containerização.
| Tecnologia      | Finalidade                            |
| --------------- | ------------------------------------- |
| FastAPI         | Desenvolvimento das APIs REST         |
| PostgreSQL      | Persistência dos dados                |
| Apache Kafka    | Comunicação assíncrona entre serviços |
| Docker          | Containerização da aplicação          |
| Docker Compose  | Orquestração dos containers           |
| JWT             | Autenticação e autorização            |
| Prometheus      | Coleta de métricas                    |
| Grafana         | Visualização e monitoramento          |
| Swagger/OpenAPI | Documentação interativa das APIs      |
| Python          | Linguagem principal do projeto        |

## Microsserviços

A aplicação foi dividida em quatro microsserviços independentes, cada um com uma responsabilidade específica do domínio da aplicação.

### User Service
Responsável pelo gerenciamento dos usuários e autenticação da aplicação.
#### Principais Funcionalidades
- Cadastro de usuários
- Consulta de usuários
- Atualização de informações
- Remoção de usuários
- Login e geração de token JWT
- Validação de autenticação

#### Documentação da API
<img width="1600" height="826" alt="image" src="https://github.com/user-attachments/assets/151e8972-902b-4a17-b398-aaa0705351fd" />

### Music Service
Responsável pelo gerenciamento do catálogo de músicas disponísveis para recomendação.

#### Principais Funcionalidades
- Cadastro de músicas
- Consulta de músicas
- Busca por humor
- Atualização de registros
- Remoção de músicas

#### Documentação da API
<img width="1600" height="816" alt="image" src="https://github.com/user-attachments/assets/3f269736-90e8-4911-aea5-ad8f2ae126e8" />

### Recommendation Service 
Responsável por processar as solicitações de recomendações e coordenar a comunicação com os demais serviços.

#### Principais Funcionalidades
- Consulta do humor do usuário
- Busca de músicas compatíveis
- Geração de recomendações
- Publicação de eventos no Kafka

#### Documentação da API
<img width="1600" height="809" alt="image" src="https://github.com/user-attachments/assets/b2a2317f-8721-4056-8b51-a42cfb91630b" />

### History Service
Responsável por armazenar e disponibilizar o histórico de recomendações realizadas.

#### Principais Funcionalidades
- Consumo deeventos Kafka
- Registro do histórico
- Consulta do histórico de recomendações
- Persistências dos dados

#### Documentação da API
<img width="1600" height="807" alt="image" src="https://github.com/user-attachments/assets/168371bb-4092-4f62-bf3b-c8bea5119bb9" />

## Comunicação Entre Serviços
Os componentes do MoodMusic se comunicam de duas maneiras diferentes: de forma síncrona via APIs REST e de forma assíncrona utilizando o Apache Kafka.

### Comunicação REST
Para fazer recomendações de músicas, é utilizada a comunicação REST.
O Recommendation Service, ao receber uma solicitação de recomendação, consulta o User Service para obter as informações do usuário, incluindo seu estado de humor atual. Depois, verifica no Music Service quais músicas se alinham a esse estado de espírito.

### Comunicação Assíncrona com Kafka
Depois de criar uma recomendação, o Recommendation Service publica um evento no tópico Kafka denomindado recommendations.
O History Service consome esse tópico, ou seja, ele recebe os eventos para armazenar o histórico de recomendações no banco de dados.

## Segurança com JWT
Para garantir o controle de acesso as funcionalidades protegidas da aplicação, o MoodMusic utiliza autenticação baseada e JSON Web Token (JWT).
No momento da autenticação, o usuário fornece suas credenciais e recebe um token assinado para acesso. Esse token precisa ser incluído nas requisições a endpoints que são protegidos para que os microsserviços possam confirmar a identidade do usuário antes de antender a solicitação.
### Exemplo de autenticação

<img width="1600" height="791" alt="image" src="https://github.com/user-attachments/assets/983fa779-1a02-418a-a1a6-1de8423329a8" />

<img width="997" height="426" alt="image" src="https://github.com/user-attachments/assets/9ed88029-4714-4bfb-956a-d9abb041fa23" />

## Containerização com Docker
Todo o ecossistema do MoodMusic foi containerizado com o uso do Docker, o que possibilita a execução da aplicação de maneira uniforme em diversos ambientes.
Cada parte da arquitetura é hospedada em seu próprio container, sejam microsserviços, bancos de dados, sistemas de mensageria ou ferramentas de monitoramento.

### Containers da solução
- User Service
- Music Service
- Recommendation Service
- History Service
- Apache Kafka
- Zookeeper
- Prometheus
- Grafana

### Ambiente em execução
<img width="1492" height="698" alt="image" src="https://github.com/user-attachments/assets/e209d657-4ee9-4fad-8ffb-efb85dbce71f" />

## Monitoramento
O MoodMusic implementa observabilidade através da integração entre Prometheus e Grafana.
O Prometheus é responsável pela coleta periódica de métricas expostas pelos microsserviços, enquanto o Grafana fornece dashboards para visualização e análise dessas informações em tempo real.

### Métricas monitoradas
- Disponibilidade dos serviços
- Quantidade de requisições
- Tempo de resposta
- Status dos microsserviços

### Dashboard de Monitoramento
<img width="1600" height="821" alt="image" src="https://github.com/user-attachments/assets/3abadbf8-5341-419c-9611-8d003e581985" />

## Resultados Obtidos
Durante o desenvolvimento do projeto foi possível implementar uma arquitetura baseada em microsserviços contemplando os principais conceitos estudados na disciplina.
Entre os resultados alcançados destacm-se:
- Implementação de APIs REST independentes.
- Comunicação síncrona entre microsserviços.
- Comunicação assíncrona utilizando Apache Kafka.
- Autenticação baseada em JWT.
- Persistência de dados utilizando PostgreSQL.
- Containerização completa com Docker.
- Monitoramento com Prometheus e Grafana.
- Documentação automática das APIs com SWagger/OpenAPI.

## Como Executar o Projeto
### Pré-requisitos
Antes de iniciar o projeto é necessário possuir instalado:
- Docker
- Docker Compose

### Clonar o Repositório
git clone https://github.com/MatheusSantos15/moodmusic.git
cd moodmusic

### Iniciar a Aplicação
docker compose up --build

### Acessar os Serviços
| Serviço                | URL                                                      |
| ---------------------- | -------------------------------------------------------- |
| User Service           | [http://localhost:8000/docs](http://localhost:8000/docs) |
| Music Service          | [http://localhost:8001/docs](http://localhost:8001/docs) |
| History Service        | [http://localhost:8002/docs](http://localhost:8002/docs) |
| Recommendation Service | [http://localhost:8003/docs](http://localhost:8003/docs) |
| Grafana                | [http://localhost:3000](http://localhost:3000)           |
| Prometheus             | [http://localhost:9090](http://localhost:9090)           |

## Autor
### Matheus Santos do Nascimento 
Projeto desenvolvido para a disciplina de Desenvolvimento de APIs e Microsserviços, aplicando conceitos de arquitetura distribupida, comunicação entre serviços, autenticação, mensageria e observabilidade.

