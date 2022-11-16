pipeline {
	agent any
	stages {
		stage('Initialize') {
            steps {
                sh 'sudo apt-get update -y'

                sh 'which docker-compose || sudo curl -L https://github.com/docker/compose/releases/download/2.12.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose'

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
		stage('Build') {
			steps {
				sh 'composer install'
			}
		}
		stage('Test') {
			steps {
                sh './vendor/bin/phpunit --log-junit logs/unitreport.xml -c tests/phpunit.xml tests'
            }
		}
		stage('Integration UI Test') {
			parallel {
				stage('Deploy') {
					agent any
					steps {
						sh './jenkins/scripts/deploy.sh'
						input message: 'Finished using the web site? (Click "Proceed" to continue)'
						sh './jenkins/scripts/kill.sh'
					}
				}
				stage('Headless Browser Test') {
					agent {
						docker {
							image 'maven:3-alpine' 
							args '-v /root/.m2:/root/.m2' 
						}
					}
					steps {
						sh 'mvn -B -DskipTests clean package'
						sh 'mvn test'
					}
					post {
						always {
							junit 'target/surefire-reports/*.xml'
						}
					}
				}
			}
		}
	}
}