pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    environment {
        PYTHON = 'C:/Users/hirem/AppData/Local/Python/pythoncore-3.14-64/python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching TaskFlow source code'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
                bat '.venv\\Scripts\\python.exe -m pip install build'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Build Application') {
            steps {
                bat '.venv\\Scripts\\python.exe -m build'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'dist/*.whl', fingerprint: true
            echo 'TaskFlow build completed successfully!'
        }
    }
}