pipeline {
    agent any
    stages {
        stage ("Install dependencies on Jenkins server") {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage ("Run linter") {
            steps {
                sh "pylint web.py"
            }
        }
    }
}