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
nohup python3 ./ShoxieAGod/shoxieAGod.py > /home/admin/log/shoxieagod.log &
'''
      }
    }
  }
}