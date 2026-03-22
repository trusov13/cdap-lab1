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

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    echo "=== Применяем все манифесты из lab_03/ ==="
                    kubectl apply -f lab_03/
                    
                    echo "=== Ждём готовности приложения ==="
                    kubectl rollout status deployment/analytics-app --timeout=120s || true
                    
                    echo "=== Состояние кластера после деплоя ==="
                    kubectl get pods,svc,pvc,job -o wide
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