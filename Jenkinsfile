pipeline {
  agent any
  stages {
    stage('Environment Setup') {
      steps {
        sh 'python --version'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Pipeline Compilation') {
      steps {
        sh 'python pipeline.py'
        sh 'ls -l pipeline.yaml'
      }
    }
    stage('Component Validation') {
      steps {
        sh 'python compile_components.py'
        sh 'ls -l components'
      }
    }
  }
  post {
    success { echo 'Pipeline compiled successfully!' }
    failure { echo 'Pipeline compilation failed!' }
  }
}
