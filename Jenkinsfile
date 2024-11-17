pipeline {
    agent any
    
    environment {
        CONTAINER_ID = ''
        SUM_PY_PATH = '/app/sum.py'
        DIR_PATH = '/home/issa/ECE/COURS/MSc1/DevOps_with_SRE/docker-jenkins-tp'
        TEST_FILE_PATH = "${DIR_PATH}/test_variables.txt"
    }
    
    stages {
        stage('Build') {
            steps {
                script {
                    sh "docker build -t sum-image ${DIR_PATH}"
                }
            }
        }
        
        stage('Run') {
            steps {
                script {
                    def output = sh(script: "docker run -d sum-image", returnStdout: true)
                    CONTAINER_ID = output.trim()
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    def testLines = readFile(TEST_FILE_PATH).split('\n')
                    for (line in testLines) {
                        def vars = line.split(' ')
                        def arg1 = vars[0]
                        def arg2 = vars[1]
                        def expectedSum = vars[2].toFloat()
                        def output = sh(script: "docker exec ${CONTAINER_ID} python ${SUM_PY_PATH} ${arg1} ${arg2}", returnStdout: true)
                        def result = output.split('\n')[-1].trim().toFloat()
                        if (result == expectedSum) {
                            echo "Test réussi pour ${arg1} + ${arg2} = ${result}"
                        } else {
                            error "Test échoué pour ${arg1} + ${arg2}. Attendu: ${expectedSum}, Obtenu: ${result}"
                        }
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "docker login -u <issamentacode> -p <Pa55word.dockerhub>"
                    sh "docker tag sum-image <issamentacode>/sum-image:latest"
                    sh "docker push <issamentacode>/sum-image:latest"
                }
            }
        }


    post {
        always {
            sh "docker stop ${CONTAINER_ID}"
            sh "docker rm ${CONTAINER_ID}"
        }
    }

    stage('Performance Analysis') {
    steps {
        script {
            sh "docker run -d --name sum-container sum-image tail -f /dev/null"
            def statsOutput = sh(script: "docker stats sum-container --no-stream --format '{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}'", returnStdout: true).trim()
            echo "Container Resource Usage: ${statsOutput}"
            sh "docker stop sum-container && docker rm sum-container"
        }
    }
}

    stage('Generate Documentation') {
    steps {
        script {
            sh "docker run --rm -v ${WORKSPACE}:/app sum-image sh -c 'cd /app && sphinx-build -b html docs _build'"
            archiveArtifacts artifacts: '_build/**', fingerprint: true
        }
    }
}
    }    
}


