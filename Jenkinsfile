pipeline {
    agent any

    environment {
        IMAGE_NAME = 'landapp'
        CONTAINER_NAME = 'landapp_container'
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/rohan98805/LandManagementSystem.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Previous Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name $CONTAINER_NAME -p 8000:8000 $IMAGE_NAME'
            }
        }
    }
}
