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
				sh 'pip install docker-compose'
				sh 'pip install Flask'
				sh 'pip install selenium'
                //sh 'pip install -r requirements.txt'
            }
        }
		stage('OWASP DependencyCheck') {
			steps {
				echo 'OWASP Dependency Check'
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'OWASP-Dependency-Check'
			}
		}

		stage('Build Test-Env') {
            steps {
                echo 'Building Environment'
                sh 'docker network create selenium_network || echo selenium_network exists'
                sh 'docker-compose -f docker-compose.yml -f docker-compose.test.yml -f docker-compose.selenium.yml down'
                sh 'docker-compose -f docker-compose.yml -f docker-compose.test.yml -f docker-compose.selenium.yml up --build -d'
                sh 'docker-compose ps'
            }
        }
		
		stage('Static Code Analyis') {
             steps {
                echo 'Analyzing code'
                sh 'pylint *.py > reports/pylint.report | echo 1'
                sh 'docker-compose exec -T flask-app sh -c "python3 -m bandit -r ."'
        	}
        }
	}
	post {
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}