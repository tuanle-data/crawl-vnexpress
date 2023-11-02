// Jenkinsfile

pipeline {
    agent any

    stages {
		stage('Checkout') {
            steps {
                echo 'Code checkout.'
                git branch: 'main', url: 'https://github.com/tuanle-data/crawl-vnexpress.git'
            }
        }
		
        stage('Build') {
            steps {
                echo 'Build project...'
                git branch: 'main', url: 'https://github.com/tuanle-data/crawl-vnexpress.git'
                sh 'python3 vnexpress.py'
            }
        }

        stage('Test') {
            steps {             
               
                echo 'Running tests with coverage...'
                sh 'python3 -m pytest'
               
            }
        }
    }

}
