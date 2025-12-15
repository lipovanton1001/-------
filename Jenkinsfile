pipeline {
    agent any

    environment {
        // Замініть на ваш логін
        DOCKER_IMAGE = 'lipovanton1001/scholarship-app' 
        DOCKER_CREDS_ID = 'dockerhub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo '--- Building Docker Image ---'
                    // Використовуємо bat замість sh
                    bat "docker build -t %DOCKER_IMAGE%:latest ."
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo '--- Running Tests inside Container ---'
                    // bat для Windows
                    bat "docker run --rm %DOCKER_IMAGE%:latest pytest"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo '--- Pushing to Docker Hub ---'
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDS_ID}", passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        // Логін на Windows через bat виглядає трохи інакше
                        bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                        bat "docker push %DOCKER_IMAGE%:latest"
                    }
                }
            }
        }
    }

    post {
        always {
            // Очистка на Windows
            bat "docker logout"
            // || exit 0 допомагає не валити білд, якщо образу немає
            bat "docker rmi %DOCKER_IMAGE%:latest || exit 0"
        }
    }
}