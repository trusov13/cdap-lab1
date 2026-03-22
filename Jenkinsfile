pipeline {
    agent any
    environment {
        IMAGE_NAME = "cdap-analytics-app"
        TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'lab-04-jenkins', url: 'https://github.com/trusov13/cdap-lab1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t $IMAGE_NAME:$TAG -f Dockerfile .
                    docker tag $IMAGE_NAME:$TAG $IMAGE_NAME:latest
                '''
            }
        }

        stage('Trivy Security Scan') {
            steps {
                sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasecurity/trivy image $IMAGE_NAME:$TAG --exit-code 1 --severity HIGH,CRITICAL'
            }
        }

        stage('Deploy to Kubernetes (Minikube)') {
            steps {
                sh '''
                    kubectl apply -f k8s/
                    kubectl rollout status deployment/analytics-app --timeout=120s
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline завершён!'
        }
        success {
            echo '✅ Успешный деплой!'
        }
    }
}