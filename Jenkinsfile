pipeline {
    agent any
    
    environment {
        // Load the SonarQube token from Jenkins Credentials
        SONAR_TOKEN = credentials('sonar-token') 
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling latest code...'
                checkout scm
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                echo 'Running SonarQube analysis...'
                withSonarQubeEnv('MySonarQube') {
                    bat """
                    sonar-scanner ^
                    -Dsonar.projectKey=dummy-login ^
                    -Dsonar.sources=. ^
                    -Dsonar.host.url=http://localhost:9000
                    """
                }
            }
        }
        
        stage('Quality Gate Check') {
            steps {
                echo 'Waiting for SonarQube Quality Gate status... (Max 5 minutes)'
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        
        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t dummy-login .'
            }
        }
        
        stage('Verify Docker Image') {
            steps {
                echo 'Docker image built successfully! ✅'
                echo 'Listing Docker images...'
                bat 'docker images dummy-login'
                echo ''
                echo '================================================'
                echo 'CI/CD Pipeline Complete!'
                echo 'Docker image "dummy-login:latest" is ready'
                echo 'To run locally: docker run -it --rm dummy-login'
                echo '================================================'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully! ✅'
            echo 'Docker image is ready for deployment.'
        }
        failure {
            echo 'Pipeline failed ❌ - Check console output for details.'
        }
        always {
            echo 'Cleaning up workspace...'
            // Optional: Clean up old Docker images
            // bat 'docker image prune -f'
        }
    }
}
