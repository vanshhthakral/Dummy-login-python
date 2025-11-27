pipeline {
    agent any

    environment {
        // Load the SonarQube token from Jenkins Credentials.
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
                    // FIX: Using 'bat' for Windows execution. Removed manual -Dsonar.login.
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
                    // This ensures the pipeline fails if new vulnerabilities are found.
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
                // FINAL FIX: Using -it for Interactive and TTY. This prevents the EOFError
                // by allocating a terminal for your interactive Python script.
                // NOTE: This stage will now wait indefinitely for input unless you manually 
                // stop the build or set a job timeout.
                bat 'docker run -it --rm dummy-login' 
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
