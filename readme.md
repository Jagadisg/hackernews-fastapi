#### Hacker news fastapi application

#### Prerequisites

Install docker on your system

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)


1. **Clone the Repository**

   ```sh
   git clone https://github.com/Jagadisg/social_network.git

2. **Create virtual environment**
   
   ```sh
   python -m venv venv

3. ### Build the Docker images.

    ```sh
    docker compose up --build

4. **Access the Application**

    ### Once the containers are up and running, you can access the application in your web browser at:

    ```sh
    http://localhost:8000/top-news?count=5

5. **Test api using swagger by accessing docs endpoint which is easier than postman**

    ```sh
    http://localhost:8000/docs