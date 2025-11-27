pipeline {
    agent any

    environment {
        // Load the SonarQube token from Jenkins Credentials for use across the pipeline
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
                    // Using 'bat' for Windows execution. 
                    // The 'withSonarQubeEnv' wrapper handles the token automatically.
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
                // The 'timeout' prevents the pipeline from hanging indefinitely.
                timeout(time: 5, unit: 'MINUTES') {
                    // This waits for the SonarQube result. 
                    // If the Quality Gate fails, the pipeline will stop here.
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                // Correctly uses 'bat' for Windows
                bat 'docker build -t dummy-login .'
            }
        }

        stage('Docker Run') {
            steps {
                echo 'Running Docker container...'
                // Correctly uses 'bat' for Windows
                bat 'docker run --rm dummy-login'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully! ✅'
        }
        failure {
            // This message will appear if any stage, including Quality Gate, fails.
            echo 'Pipeline failed ❌ - Check console output for details.'
        }
    }
}
