def output

pipeline {
    
   agent any

   stages {
      stage('Hello') {
         steps {
             script {
                 output = sh label: '', returnStdout: true, script: 'echo "Hello, World"'
             }
         }
      }
      stage('echo') {
         steps {
            echo output
         }
      }
	  stage('build') {
		  steps {
			  sh 'python3 --version'
			  sh 'python3 ./fib.py'
		  }
	  }
   }
}
