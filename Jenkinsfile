pipeline {
    agent any

    stages {
        stage("Run code linter") {
            agent {
                docker {
                    image 'eeacms/pylint'
                }
            }
            steps {
                sh "pip install -r requirements.txt"
                sh "pylint --output-format=parseable web.py > pylint.log || exit 0"
                sh "cat pylint.log"
                warnings canComputeNew: false, canResolveRelativePaths: false, categoriesPattern: '', defaultEncoding: '', excludePattern: '', healthy: '', includePattern: '', messagesPattern: '', parserConfigurations: [[parserName: 'PyLint', pattern: 'pylint.log']], unHealthy: ''
            }
        }
    }
}