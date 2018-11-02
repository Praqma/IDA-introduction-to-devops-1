pipeline {
    agent any

    stages {
        stage("Install dependencies") {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage("Run code linter") {
            steps {
                sh "pylint web.py"
            }
        }
    }
}