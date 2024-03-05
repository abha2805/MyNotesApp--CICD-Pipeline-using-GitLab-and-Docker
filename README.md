1. Build Notes App: 
 - Develop a Python-Django app for Note Application.
2. Set Up GitLab:
 - Create a GitLab repository for version control.
3. Database in Container:
 - Use Docker to containerize a database (e.g., MySQL) with volume.
4. Containerize App:
 - Create a Dockerfile for the Django app.
5. Build Pipeline for Docker Image:
 - Configure GitLab CI for automatic Docker image creation on code changes.
6. Deploy on AWS EC2 with Docker Compose:
 - Set up an EC2 instance on AWS.
 - Install Docker and Docker Compose.
 - Configure CI/CD pipeline to deploy Docker Compose stack on EC2.

TECHNOLOGY STACK
Backend Framework:
Django, a Python web framework, serves as the backend to facilitate user authentication, note management, and data security.
 
Database:
MySQL, a reliable and widely used open-source relational database, is employed to ensure data integrity and efficient storage.

Frontend:
The user-friendly interface was developed using HTML, Bootstrap, CSS, and JavaScript.

IMPLEMENTATION AND DEVELOPMENT
The Note app was developed using the Django framework as the backend. MySQL was used as the database, where the application is hosted on EC2 Machine, an AWS cloud-based service. 
GitLab was used for version control, and Docker was used to build an image and containerize the app, allowing it to be deployed easily across different environments, and deployed on AWS.
