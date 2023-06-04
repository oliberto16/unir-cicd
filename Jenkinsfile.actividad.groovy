pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('Source') {
            steps {
                git 'https://github.com/oliberto16/unir-cicd.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    try {
                        echo 'Building stage!'
                        sh 'make build'
                        def jobName = env.JOB_NAME
                        def buildNumber = env.BUILD_NUMBER
                        //Simulate send mail with echo in Console
                        echo "to: example@maildestino.com"
                        echo "subject: Job ${jobName} failed - Execution #${buildNumber}"
                        echo "body: A pipeline failure has occurred. See the Jenkins logs for more details: http://localhost:8080/job/${jobName}/${buildNumber}/testReport"
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error("Error en Stage Build: ${e.message}")
                    }
                }
                
            }
        }
        stage('Unit tests') {
            steps {
                sh 'make test-unit'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('Api tests') {
            steps {
                sh 'make test-api'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
        stage('E2E tests') {
            steps {
                sh 'make test-e2e'
                archiveArtifacts artifacts: 'results/*.xml'
            }
        }
    }
    post {
        always {
            junit 'results/*_result.xml'
            cleanWs()
        }
        failure {
            // Get Job_name and Build_number
            def jobName = env.JOB_NAME
            def buildNumber = env.BUILD_NUMBER

            // Send mail with Email Extension Plugin (Configure SMTP Jenkins)
            emailext (
                to: 'example@maildestino.com',
                subject: "Job ${jobName} failed - Execution #${buildNumber}",
                body: "A pipeline failure has occurred. See the Jenkins logs for more details: http://localhost:8080/job/${jobName}/${buildNumber}/testReport"
            )

            //Simulate send mail with echo in Console
            echo "to: example@maildestino.com"
            echo "subject: Job ${jobName} failed - Execution #${buildNumber}"
            echo "body: A pipeline failure has occurred. See the Jenkins logs for more details: http://localhost:8080/job/${jobName}/${buildNumber}/testReport"
        }
    }
}
