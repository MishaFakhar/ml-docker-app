pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials' // Change this to your Jenkins credentials ID
        DOCKER_IMAGE = 'mishafakhar1t/ml-docker-app'
        DOCKER_REGISTRY = 'docker.io'
        DOCKER_CLIENT_TIMEOUT = '300' // Increase Docker client timeout
        DOCKER_BUILD_TIMEOUT = '300'   // Increase Docker build timeout
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/MishaFakhar/ml-docker-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t %DOCKER_IMAGE% .'
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                    }
                    bat 'docker push %DOCKER_IMAGE%'
                }
            }
        }
    }

    post {
        always {
            bat 'docker rmi %DOCKER_IMAGE% || exit 0'
            cleanWs()
        }
    }
}
