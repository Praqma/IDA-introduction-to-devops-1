
    agent any

    stages {
        stage("Install dependencies") {
            steps {
                sh "pip install -r requirements.txt"
            }
        }
        stage("Run code linter") {
            steps {
                sh "pylint web.py --exit-zero --output-format=parseable > pylint.log"
                sh "cat pylint.log"
                warnings canComputeNew: false, canResolveRelativePaths: false, categoriesPattern: '', defaultEncoding: '', excludePattern: '', healthy: '', includePattern: '', messagesPattern: '', parserConfigurations: [[parserName: 'PyLint', pattern: 'pylint.log']], unHealthy: ''
            }
        }
    }
}