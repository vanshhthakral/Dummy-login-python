pipeline {
    agent any

    environment {
        // Load the SonarQube token from Jenkins Credentials. 
        // We keep this here in case other stages need it, but it's not explicitly
        // passed in the 'withSonarQubeEnv' block.
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
                    // Using 'bat' for Windows execution. Removed manual -Dsonar.login.
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
                    // This waits for the Quality Gate result and fails the pipeline if the gate is broken.
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
                // ADDED -i FLAG to keep STDIN open. This prevents the EOFError
                // when your Python script tries to read interactive input.
                bat 'docker run -i --rm dummy-login'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully! ✅'
        }
        failure {
            echo 'Pipeline failed ❌ - Check console output for details.'
        }
    }
} 
