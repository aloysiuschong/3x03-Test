pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        echo 'test'
      }
    }

  }
  post {
    success {
      dependencyCheckPublisher(pattern: 'dependency-check-report.xml')
    }

  }
}