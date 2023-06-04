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
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error("Error en Stage Build: ${e.message}")
                    }
                }
            }
        }
        stage('Unit tests') {
            steps {
                script {
                    try {
                        sh 'make test-unit'
                        archiveArtifacts artifacts: 'results/*.xml'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error("Error en Stage Build: ${e.message}")
                    }
                }
            }
        }
        stage('Api tests') {
            steps {
                script {
                    try {
                        sh 'make test-api'
                        archiveArtifacts artifacts: 'results/*.xml'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error("Error en Stage Build: ${e.message}")
                    }
                }
            }
        }
        stage('E2E tests') {
            steps {
                script {
                    try {
                        sh 'make test-e2e'
                        archiveArtifacts artifacts: 'results/*.xml'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error("Error en Stage Build: ${e.message}")
                    }
                }
            }
        }
    }
    post {
        always {
            junit 'results/*_result.xml'
            cleanWs()
        }
        failure {
            // Send mail with Email Extension Plugin (Configure SMTP Jenkins)
            /*emailext (
                to: 'example@maildestino.com',
                subject: "Job ${env.JOB_NAME} failed - Execution #${env.BUILD_NUMBER}",
                body: "A pipeline failure has occurred. See the Jenkins logs for more details: ${env.JENKINS_URL}/job/${env.JOB_NAME}/${env.BUILD_NUMBER}/testReport"
            )*/

            //Simulate send mail with echo in Console
            echo "to: example@maildestino.com"
            echo "subject: Job ${env.JOB_NAME} failed - Execution #${env.BUILD_NUMBER}"
            echo "body: A pipeline failure has occurred. See the Jenkins logs for more details: ${env.JENKINS_URL}/job/${env.JOB_NAME}/${env.BUILD_NUMBER}/testReport"
        }
    }
}
