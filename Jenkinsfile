def output

pipeline {
    
   agent any
   tools {
	   go { 'go-1.2' }
   }

   stages {
      stage('Build') {
         steps {
             script {
                 sh 'go build' 
             }
         }
      }
   }      
} 
    
   
  








