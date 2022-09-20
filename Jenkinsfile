pipeline{
	agent any
	parameters{
		choice(name:'Version', choices: ['1.0', '2.0', '3.0'], description:'Pick version')
	}
	stages{
		stage("build"){
			steps{
				echo 'buildingggg'
			}
		}
		stage("test"){
			steps{
				echo 'testing'
			}
		}
		stage("deploy"){
			steps{
				echo "deploying the version ${params.Version}"
			}
		}
	}
}