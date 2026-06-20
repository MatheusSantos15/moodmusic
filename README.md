# MoodMusic

MoodMusic é um sistema de microsserviços que foi criado para a matéria de Desenvolvimento de APIs e Microsserviços. A proposta da aplicação é sugerir músicas aos usuários conforme os humores que eles registram, evidenciando na prática conceitos essenciais de arquitetura distribuída, comunicação entre serviços, autenticação, mensageria e monitoramento.
Para a construção da solução, foram utilizados FastAPI, PostgreSQL, Apache Kafka, Docker, Prometheus e Grafana, que se organizam em quatro microsserviços independentes: User Service, Music Service, Recommendation Service e History Service. O projeto também proporciona comunicação assíncrona via Kafka, além da comunicação síncrona com APIs REST, para registrar o histórico de recomendações.
O sistema doi criado com o objetivo de ser didático, utilizando técnicas modernas que são amplamanete adotadas no setor da tecnologia, como autenticação JWT, containerização via Docker, e observabilidade por meio de métricas e monitoramento centralizado.

##Demonstração
A demonstração completa do sistema pode ser acessada através do vídeo abaixo:
*Video de Demonstração:* (LINK)

##Arquitetura

A arquitetura do MoodMusic segue o padrão de microsserviços, onde cada serviço possui uma responsabilidade específica e se comunica com os demais por meio de APIs REST e eventos Kafka.

###Diagrama da Arquitetura###
<img width="623" height="771" alt="image" src="https://github.com/user-attachments/assets/ead0c16b-83dd-4a06-b5ac-6a638596b6e4" />

###Componentes da Solução###
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

##Microsserviços

A aplicação foi dividida em quatro microsserviços independentes, cada um com uma responsabilidade específica do domínio da aplicação.
