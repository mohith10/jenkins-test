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
				sh 'python3 -m pytest test_file.py --junitxml Test_Result_${BUILD_NUMBER}.xml'
				sh 'cat Test_Result_${BUILD_NUMBER}.xml'
			}
		}
		stage('Packaging'){
			steps{
				echo 'Packaging your application'
				sh 'python3 -m PyInstaller cli.py'
			}
		}
	}
}