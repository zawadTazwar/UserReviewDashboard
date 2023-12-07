# Microservices Alternative Architecture Document

## Overview
This document presents the structure of a microservices-based system and compares it to the current approach, which is component-based. It explores the distinctions between the two methods in terms of architectural design and coding practices. Additionally, it addresses the variations in the software development lifecycle when adopting a microservices strategy as opposed to the existing monolithic framework.


## Microservices Architecture:

![Microservices Architecture](C:\Users\zawad\OneDrive\Documents\Microservices Architecture.png)

## Comparison of Microservices and Components-based Architectures

### 1. Architectural Approach Comparison

### Components-based (Monolithic) Architecture:
- **Structure:** The application is structured as a single monolithic server that encompasses various functionalities including user management, session management, and request handling.
- **Server Responsibilities:** A central server directly manages operations such as login, signup, profile information retrieval, and more.
- **Data Management:** All data is stored in a unified MongoDB database, which is accessed by the server for all data retrieval and manipulation tasks.
- **Template Rendering:** Web page templates are rendered on the server-side and delivered to the client.

### Microservices Architecture:
- **Structure:** The application is decomposed into small, independent services each responsible for specific functionality like authentication, review handling, and session management.
- **Service Independence:** Services are developed, deployed, and operated independently. They communicate using well-defined APIs.
- **Database Segregation:** Each service interacts with its own dedicated database, which is aligned with the database-per-service pattern.
- **API Gateway:** An API Gateway is introduced as the single point of entry for all client requests, routing them to the appropriate microservice.

### 2. Architectural and Code Differences

### Components-based Architecture:
- **Codebase:** A single codebase which can be simpler to manage initially but may grow complex over time.
- **Coupling:** High coupling between components, making it difficult to scale or update parts of the application independently.
- **Resilience:** The entire application can be vulnerable to failure if a single component fails.

### Microservices Architecture:
- **Codebase:** Multiple codebases, each corresponding to a microservice. This allows for modular development and deployment.
- **Coupling:** Low coupling between services, which permits independent updates and scaling.
- **Resilience:** Better fault isolation. A failure in one microservice is less likely to affect the entire system.

### 3. Software Process Differences

### Components-based Architecture:
- **Team Collaboration:** Teams work on a shared codebase, which can lead to merge conflicts and bottlenecked workflows.
- **Deployment:** Deployment involves the entire application, which can be less frequent and riskier.
- **Scaling:** Scaling means scaling the entire application, which is not resource-efficient.

### Microservices Architecture:
- **Team Collaboration:** Promotes decentralized and agile development, with teams taking ownership of individual services.
- **Deployment:** Supports CI/CD practices, allowing for more frequent and safer deployments of individual services.
- **Scaling:** Services can be scaled independently in response to specific demands, leading to optimized resource usage.
- **Monitoring and Logging:** Requires comprehensive monitoring and logging to track the health and interactions of various services.
