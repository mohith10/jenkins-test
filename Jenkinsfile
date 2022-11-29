pipeline{
	agent any
	stages{
		stage("Build"){
			steps{
				echo 'Building your python application'
				sh 'python3 hello.py'
				sh 'java -version'
			}
		}	
	}
}