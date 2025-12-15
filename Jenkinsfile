pipeline {
    agent any

    environment {
        // ЗАМІНИ НА СВІЙ ЛОГІН DOCKERHUB
        DOCKER_IMAGE = 'tviy_login_dockerhub/scholarship-app' 
        // ID, який ми створимо в Jenkins на кроці 2
        DOCKER_CREDS_ID = 'dockerhub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                // Завантаження коду з Git
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo '--- Building Docker Image ---'
                    sh "docker build -t ${DOCKER_IMAGE}:latest ."
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo '--- Running Tests inside Container ---'
                    // Запускаємо контейнер, проганяємо pytest і видаляємо контейнер (--rm)
                    sh "docker run --rm ${DOCKER_IMAGE}:latest pytest"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo '--- Pushing to Docker Hub ---'
                    // Використовуємо збережені логін/пароль для входу і пушу
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDS_ID}", passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                        sh "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }
    }

    post {
        always {
            // Очистка: видаляємо локальний образ та виходимо з докера
            sh "docker logout"
            sh "docker rmi ${DOCKER_IMAGE}:latest || true"
        }
    }
}