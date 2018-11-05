pipeline {
    agent any
    stages {
        stage ("Run linter") {
            steps {
                sh "pylint web.py"
            }
        }
    }
} 