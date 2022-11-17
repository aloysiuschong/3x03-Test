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
				//sh 'apt install virtualbox'
				sh 'pip install docker-compose'
				sh 'pip install Flask'
				sh 'pip install selenium'
				sh 'apt-get install ca-certificates curl gnupg lsb-release -y'

				//sh 'docker-machine create default'
				//sh 'export DOCKER_MACHINE_NAME=default'
				//sh 'export DOCKER_TLS_VERIFY=1'
				//sh 'export DOCKER_CERT_PATH=~/.docker/machine/machines/default'
				//sh 'docker-machine regenerate-certs default'
                //sh 'pip install -r requirements.txt'
            }
        }
		stage('OWASP DependencyCheck') {
			steps {
				echo 'OWASP Dependency Check'
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'OWASP-Dependency-Check'
			}
		}

		//stage('Build Test-Env') {
        //    steps {
        //        echo 'Building Environment'
        //        sh 'docker network create selenium_network || echo selenium_network exists'
        //        sh 'docker-compose -f docker-compose.yml -f docker-compose.test.yml -f docker-compose.selenium.yml down'
        //        sh 'docker-compose -f docker-compose.yml -f docker-compose.test.yml -f docker-compose.selenium.yml up --build -d'
        //        sh 'docker-compose ps'
        //    }
        //}

		stage ('Checkout') {
			steps {
				git branch:'master', url: 'https://github.com/aloysiuschong/3x03-Test.git'
			}
		}
		stage ('Build') {
			steps {
				sh '/var/jenkins_home/apache-maven-3.6.3/bin/mvn --batch-mode -V -U -e clean verify -Dsurefire.useFile=false -Dmaven.test.failure.ignore'
			}
		}
		stage ('Analysis') {
			steps {
				sh '/var/jenkins_home/apache-maven-3.6.3/bin/mvn --batch-mode -V -U -e checkstyle:checkstyle pmd:pmd pmd:cpd findbugs:findbugs'
			}
		}
	}
	post {
		always {
			echo 'ended'
			//junit testResults: '**/target/surefire-reports/TEST-*.xml'
			//recordIssues enabledForFailure: true, tools: [mavenConsole(), java(), javaDoc()]
			//recordIssues enabledForFailure: true, tool: checkStyle()
			//recordIssues enabledForFailure: true, tool: spotBugs(pattern:'**/target/findbugsXml.xml')
			//recordIssues enabledForFailure: true, tool: cpd(pattern: '**/target/cpd.xml')
			//recordIssues enabledForFailure: true, tool: pmdParser(pattern: '**/target/pmd.xml')
		}
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}