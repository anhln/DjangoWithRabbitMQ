# DjangoWithRabbitMQ
- A simple example using RabbitMQ to communicate between two API which used Django Rest Framework
- Using docker to install a RabbitMQ server [RabbitMQ](https://www.rabbitmq.com/download.html)
## Benefits
- Have a better understanding of how RabbitMQ works.
- Be able to communicate between your APIs using RabbitMQ as a messaging service.
## Introduction
- In the first API (Quotes), when users create, change, delete a quote then the API send message via RabbitMQ by producer
- In the second API (Likes), always running a consumer to listen from RabbitMQ, if having a message it will do it (create, change, delete quote in Likes) 
## Structure
1.Quotes Project
2.Likes Projects
