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
        stage("Build docker image") {
            steps {
                sh "docker build -t mibias/simple-flask:$BUILD_NUMBER ."
            }
        }
        stage("Push docker image to docker hub") {
            steps {
                withDockerRegistry(credentialsId: 'MichaelDockerHubCredentials', url: 'https://index.docker.io/v1/') {
                    sh "docker push mibias/simple-flask:$BUILD_NUMBER"
                }
            }
        }
    }
}