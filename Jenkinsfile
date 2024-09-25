pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials' // Change this to your Jenkins credentials ID
        DOCKER_IMAGE = 'mishafakhar1t/ml-docker-app'
        DOCKER_REGISTRY = 'docker.io'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub repository
                git branch: 'main', url: 'https://github.com/MishaFakhar/ml-docker-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image from the Dockerfile
                    bat 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub using credentials from Jenkins
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        bat 'echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin'
                    }
                    // Push Docker image to Docker Hub
                    bat 'docker push ${DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        always {
            // Cleanup Docker images after pushing
            bat 'docker rmi ${DOCKER_IMAGE} || true'
            cleanWs()  // Clean up workspace after the build
        }
    }
}
