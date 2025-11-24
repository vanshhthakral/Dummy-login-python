pipeline {
    agent any
    
    environment {
        SONARQUBE_SERVER = 'SonarQube'  // Changed from 'MySonar' to match Jenkins config
        DOCKER_IMAGE = 'dummy-login-python:latest'
        DOCKER_CONTAINER = 'dummy-login-container'
        SONAR_PROJECT_KEY = 'dummy-login-python'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out code from repository...'
                checkout scm
            }
        }
        
        stage('SonarQube Scan') {
            steps {
                script {
                    echo '🔍 Starting SonarQube code analysis...'
                    def scannerHome = tool 'SonarScanner'
                    
                    // Option 1: Using withSonarQubeEnv (if server is configured in Jenkins)
                    withSonarQubeEnv('SonarQube') {
                        bat """
                            "${scannerHome}\\bin\\sonar-scanner.bat" ^
                            -Dsonar.projectKey=${SONAR_PROJECT_KEY} ^
                            -Dsonar.sources=. ^
                            -Dsonar.host.url=http://localhost:9000 ^
                            -Dsonar.python.version=3.8,3.9,3.10,3.11
                        """
                    }
                }
            }
        }
        
        stage('Quality Gate') {
            steps {
                script {
                    echo '⏳ Waiting for Quality Gate result...'
                    timeout(time: 5, unit: 'MINUTES') {
                        def qg = waitForQualityGate()
                        echo "Quality Gate Status: ${qg.status}"
                        
                        if (qg.status != 'OK') {
                            error "❌ SECURITY FAILED: Quality Gate failed with status: ${qg.status}"
                        } else {
                            echo "✅ Quality Gate PASSED! Code is good to deploy!"
                        }
                    }
                }
            }
        }
        
        stage('Docker Build') {
            steps {
                echo '🐳 Building Docker image...'
                bat "docker build -t ${DOCKER_IMAGE} ."
            }
        }
        
        stage('Deploy Container') {
            steps {
                echo '🚀 Deploying Docker container...'
                bat """
                    docker stop ${DOCKER_CONTAINER} 2>nul || echo Container not running
                    docker rm ${DOCKER_CONTAINER} 2>nul || echo Container does not exist
                    docker run -d --name ${DOCKER_CONTAINER} -p 5000:5000 ${DOCKER_IMAGE}
                """
                echo '✅ Container deployed successfully!'
            }
        }
    }
    
    post {
        success {
            echo '🎉 Pipeline completed successfully!'
            echo '✅ All stages passed!'
        }
        failure {
            echo '❌ Pipeline failed!'
            echo '⚠ Check the logs above for details'
        }
        always {
            echo '🎯 Pipeline execution finished!'
        }
    }
}
