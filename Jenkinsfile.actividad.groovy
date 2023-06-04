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
                echo 'Building stage!'
                sh 'make build'
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
        success {
            // Send mail with Email Extension Plugin (Configure SMTP Jenkins)
            /*emailext (
                to: 'example@maildestino.com',
                subject: "Job ${env.JOB_NAME} failed - Execution #${env.BUILD_NUMBER}",
                body: "A pipeline failure has occurred. See the Jenkins logs for more details: ${env.JENKINS_URL}/job/${env.JOB_NAME}/${env.BUILD_NUMBER}/testReport"
            )*/

            //Simulate send mail with echo in Console
            echo "to: example@maildestino.com"
            echo "subject: Job ${env.JOB_NAME} SUCCESS - Execution #${env.BUILD_NUMBER}"
            echo "body: A pipeline SUCCESS has finished. See the Jenkins logs for more details: ${env.JENKINS_URL}/job/${env.JOB_NAME}/${env.BUILD_NUMBER}/testReport"
            cleanWs()
        }
        unstable {
            // Send mail with Email Extension Plugin (Configure SMTP Jenkins)
            /*emailext (
                to: 'example@maildestino.com',
                subject: "Job ${env.JOB_NAME} failed - Execution #${env.BUILD_NUMBER}",
                body: "A pipeline failure has occurred. See the Jenkins logs for more details: ${env.JENKINS_URL}/job/${env.JOB_NAME}/${env.BUILD_NUMBER}/testReport"
            )*/

            //Simulate send mail with echo in Console
            echo "to: example@maildestino.com"
            echo "subject: Job ${env.JOB_NAME} UNSTABLE - Execution #${env.BUILD_NUMBER}"
            echo "body: A pipeline UNSTABLE has occurred. See the Jenkins logs for more details: ${env.JENKINS_URL}/job/${env.JOB_NAME}/${env.BUILD_NUMBER}/testReport"
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
            echo "subject: Job ${env.JOB_NAME} FAILED - Execution #${env.BUILD_NUMBER}"
            echo "body: A pipeline failure has occurred. See the Jenkins logs for more details: ${env.JENKINS_URL}/job/${env.JOB_NAME}/${env.BUILD_NUMBER}/testReport"
            cleanWs()
        }
    }
}
