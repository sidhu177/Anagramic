pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    app = docker.build("sidhu177/anagramic")
                    app.inside {
                        sh 'echo $(curl localhost:8080)'
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_hub_login') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
        stage('DeployToProduction') {
            steps {
                input 'Deploy to Production?'
                milestone(1)
                withCredentials([sshUserPrivateKey(credentialsId: 'ssh_login', usernameVariable: 'ubuntu', keyFileVariable: 'keyfile')]) {
                    script {
                        sh " ssh -i $keyfile -v ssh -o StrictHostKeyChecking=no ubuntu@3.91.200.161 \"docker pull sidhu177/anagramic:${env.BUILD_NUMBER}\""
                        try {
                            sh "ssh -i $keyfile  -v ssh -o StrictHostKeyChecking=no ubuntu@3.91.200.161 \"docker stop anagramic\""
                            sh "ssh -i $keyfile -v ssh -o StrictHostKeyChecking=no ubuntu@3.91.200.161 \"docker rm anagramic\""
                        } catch (err) {
                            echo: 'caught error: $err'
                        }
                        sh "ssh -i $keyfile  -v ssh -o StrictHostKeyChecking=no ubuntu@3.91.200.161 \"docker run --restart always --name anagramic -p 5000:5000 -d sidhu177/anagramic:${env.BUILD_NUMBER}\""
                    }
                }
            }
        }
    }
}
