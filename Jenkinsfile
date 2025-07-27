pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flaskapp:latest'
        CONTAINER_NAME = 'flaskapp'
        APP_PORT = '5000'
    }

    stages {

        stage(' Clone Repository') {
            steps {
                echo "Cloning Git repository..."
                git branch: 'main', url: 'https://github.com/dilip8700/flask-jenkins-devops.git'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                echo "Installing Python dependencies..."
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running unit tests..."
                sh 'python3 -m pytest'
            }
        }

        stage('Clean Old Docker Resources') {
            steps {
                echo "Stopping and removing any existing container..."
                sh """
                   docker stop $CONTAINER_NAME || true
                   docker rm $CONTAINER_NAME || true
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Run Docker Container') {
            steps {
                echo " Running Docker container..."
                sh "docker run -d -p $APP_PORT:$APP_PORT --name $CONTAINER_NAME $IMAGE_NAME"
            }
        }
    }

    post {
        success {
            echo 'Flask App Deployed Locally via Docker!'
        }
        failure {
            echo 'Build/Deployment Failed. Check Console Output.'
        }
    }
}

