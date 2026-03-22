pipeline {
    agent any
    environment {
        IMAGE_NAME = "cdap-analytics-app"
        TAG        = "${BUILD_NUMBER}"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t $IMAGE_NAME:$TAG -f lab_02/Dockerfile lab_02/
                    docker tag $IMAGE_NAME:$TAG $IMAGE_NAME:latest
                '''
            }
        }

        stage('Trivy Security Scan') {
            steps {
                sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasecurity/trivy image $IMAGE_NAME:$TAG --exit-code 1 --severity HIGH,CRITICAL'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl apply -f lab_03/k8s/     # ← если манифесты в lab_03/k8s/
                    kubectl rollout status deployment/analytics-app --timeout=120s
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline успешно завершён!'
        }
        failure {
            echo '❌ Pipeline упал'
        }
    }
}