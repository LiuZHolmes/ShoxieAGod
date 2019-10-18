pipeline {
  agent any
  stages {
    stage('Stop Original Process') {
      steps {
        sh 'whoami'
        sh 'kill $(ps aux | grep \'[p]ython3 /home/admin/code/ShoxieAGod/shoxieAGod.py\' | awk \'{print $2}\')'
      }
    }
    stage('Run') {
      steps {
        sh '''OLD_BUILD_ID=$BUILD_ID

echo $OLD_BUILD_ID

BUILD_ID=DONTKILLME

/home/admin/script/run.sh

BUILD_ID=$OLD_BUILD_ID

echo $BUILD_ID'''
      }
    }
  }
}