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
                sh "pylint --output-format=parseable web.py > pylint.log || exit 0"
            }
        }
        stage ("Publish linter report") {
            steps {
                warnings canComputeNew: false, canResolveRelativePaths: false, categoriesPattern: '', defaultEncoding: '', excludePattern: '', healthy: '', includePattern: '', messagesPattern: '', parserConfigurations: [[parserName: 'PyLint', pattern: 'pylint.log']], unHealthy: ''
            }
        }
    }
}