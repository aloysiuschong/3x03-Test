pipeline {
  agent any
  stages {
    stage('') {
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