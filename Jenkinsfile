pipeline{
	agent any
	stages{
		stage("Build"){
			steps{
				echo 'Building your python application'
				sh 'python3 -m py_compile cli.py calc.py'
			}
		}
		stage("Test"){
			steps{
				echo 'Testing your python appliction' 
				sh 'python3 test_file.py'
			}
		}
		stage('Release'){
			steps{
				echo 'Releasing your application'
				
			}
		}
	}
}