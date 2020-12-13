
pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage ('first') {
            steps {
                echo 'something'
            }
        }
    }
}
