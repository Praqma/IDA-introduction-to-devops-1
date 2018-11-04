pipeline {
    agent any
    stages {
        stage ("Use docker to run pylint") {
            agent {
                docker{ image 'eeacms/pylint' }
            }
            steps {
                sh "pip install -r requirements.txt"
                sh "pylint web.py --output-format=parseable > pylint.log || exit 0"
                sh "cat pylint.log"
                warnings canComputeNew: false, canResolveRelativePaths: false, categoriesPattern: '', defaultEncoding: '', excludePattern: '', healthy: '', includePattern: '', messagesPattern: '', parserConfigurations: [[parserName: 'PyLint', pattern: 'pylint.log']], unHealthy: ''

            }
        }
        stage ("Build docker image") {
            steps {
                sh "docker build -t mibias/simple-flask:latest ."
            }
        }
        stage ("Upload docker image to Docker Hub") {
            steps {
                    withDockerRegistry(credentialsId: 'MichaelDockerHubCredentials', url: 'https://index.docker.io/v1/') {
                    sh "docker push mibias/simple-flask:latest"
                }
            }

        }
    }
}