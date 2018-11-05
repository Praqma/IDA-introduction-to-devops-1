pipeline {
    agent any
    stages {
        stage ("Run linter") {
            steps {
                sh "pylint web.py"
            }
        }
        stage ("generate report from pylint.log") {
            steps {
                warnings canComputeNew: false, canResolveRelativePaths: false, categoriesPattern: '', defaultEncoding: '', excludePattern: '', healthy: '', includePattern: '', messagesPattern: '', parserConfigurations: [[parserName: 'PyLint', pattern: 'pylinty.log']], unHealthy: ''
            }
        }
    }
} 