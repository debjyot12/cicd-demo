pipeline {
	agent any

	stages {
		
	 stage('checkout') {
	  steps {
		echo 'pulling latest code...'
		checkout scm
 }
 }

	stage('Install Dependencies') {
  steps {
                echo 'Installing required libraries...'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest tests...'
                sh 'pytest tests/ -v'
            }
        }

    }

    post {
        success {
            echo 'All tests passed! Pipeline successful.'
        }
        failure {
            echo 'Tests failed! Pipeline stopped.'
        }
    }
}
