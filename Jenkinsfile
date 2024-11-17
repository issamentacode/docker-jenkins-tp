pipeline {
    agent any
    
    environment {
        CONTAINER_ID = ''
        SUM_PY_PATH = '/app/sum.py'
        DIR_PATH = "${WORKSPACE}" // Utiliser WORKSPACE au lieu de '~/docker-jenkins-tp'
        TEST_FILE_PATH = "${DIR_PATH}/test_variables.txt"
    }
    
    stages {
        stage('Check Docker') {
            steps {
                sh 'docker info'
            }
        }

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
                    CONTAINER_ID = sh(script: "docker run -d sum-image tail -f /dev/null", returnStdout: true).trim()
                    echo "Container ID: ${CONTAINER_ID}"
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    def testLines = readFile(TEST_FILE_PATH).split('\n')
                    for (line in testLines) {
                        def vars = line.split(' ')
                        if (vars.size() >= 3) {
                            def arg1 = vars[0]
                            def arg2 = vars[1]
                            def expectedSum = vars[2].toFloat()
                            def output = sh(script: "docker exec ${CONTAINER_ID} python ${SUM_PY_PATH} ${arg1} ${arg2}", returnStdout: true)
                            def result = output.trim().toFloat()
                            if (result == expectedSum) {
                                echo "Test réussi pour ${arg1} + ${arg2} = ${result}"
                            } else {
                                error "Test échoué pour ${arg1} + ${arg2}. Attendu: ${expectedSum}, Obtenu: ${result}"
                            }
                        }
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Remplacez <username> et <password> par vos informations d'identification Docker Hub
                    sh "echo '<Pa55word.dockerhub>' | docker login -u '<issamentacode>' --password-stdin"
                    sh "docker tag sum-image <issamentacode>/sum-image:latest"
                    sh "docker push <issamentacode>/sum-image:latest"
                }
            }
        }

        stage('Performance Analysis') {
            steps {
                script {
                    def statsOutput = sh(script: "docker stats ${CONTAINER_ID} --no-stream --format '{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}'", returnStdout: true).trim()
                    echo "Container Resource Usage: ${statsOutput}"
                }
            }
        }

        stage('Generate Documentation') {
            steps {
                script {
                    sh "docker exec ${CONTAINER_ID} sh -c 'cd /app && sphinx-build -b html docs _build'"
                    sh "docker cp ${CONTAINER_ID}:/app/_build ."
                    archiveArtifacts artifacts: '_build/**', fingerprint: true
                }
            }
        }
    }    

    post {
        always {
            script {
                if (env.CONTAINER_ID) {
                    sh "docker stop ${CONTAINER_ID}"
                    sh "docker rm ${CONTAINER_ID}"
                } else {
                    echo "No container to clean up"
                }
            }
        }
    }
}
