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
                    echo "=== Применяем все манифесты из lab_03/ (игнорируем TLS и валидацию для Minikube) ==="
                    kubectl apply -f lab_03/ --validate=false --insecure-skip-tls-verify=true
                    
                    echo "=== Ждём готовности приложения (игнорируем TLS) ==="
                    kubectl rollout status deployment/analytics-app --timeout=120s --insecure-skip-tls-verify=true || true
                    
                    echo "=== Показываем состояние кластера ==="
                    kubectl get pods,svc,pvc,job -o wide --insecure-skip-tls-verify=true
                '''
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