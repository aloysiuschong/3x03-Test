pipeline {
	agent any
	stages {
		stage('Initialize') {
            steps {
                //sh 'sudo apt-get update -y'

                sh 'which docker-compose || curl -L https://github.com/docker/compose/releases/download/2.12.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose'

                //Ensure docker compose is executable
                sh 'chmod +x /usr/local/bin/docker-compose'  

                //For static code analysis setup
                sh 'apt-get install -y python3-pip'
                //sh 'pip install -r requirements.txt'
            }
        }
		stage('OWASP DependencyCheck') {
			steps {
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'OWASP-Dependency-Check'
			}
		}

		stage ('Checkout') {
			steps {
				git branch:'master', url: 'https://github.com/ScaleSec/vulnado.git'
			}
		}
	}
}