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
			junit testResults: '**/target/surefire-reports/TEST-*.xml'
			recordIssues enabledForFailure: true, tools: [mavenConsole(), java(), javaDoc()]
			recordIssues enabledForFailure: true, tool: checkStyle()
			recordIssues enabledForFailure: true, tool: spotBugs(pattern:'**/target/findbugsXml.xml')
			recordIssues enabledForFailure: true, tool: cpd(pattern: '**/target/cpd.xml')
			recordIssues enabledForFailure: true, tool: pmdParser(pattern: '**/target/pmd.xml')
		}
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}