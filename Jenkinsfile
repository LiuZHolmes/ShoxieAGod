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
        sh '''JENKINS_NODE_COOKIE=DONTKILLME
/home/admin/script/run.sh
'''
      }
    }
  }
}