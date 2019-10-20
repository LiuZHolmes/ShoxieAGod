pipeline {
  agent any
  stages {
    stage('Prepare and Run Test') {
      steps {
        sh 'pip3 install -r requirements.txt'
        sh 'python3 -m unittest discover -s plugins/test'
      }
    }
    stage('Stop Original Process') {
      steps {
        sh '''whoami
pwd'''
        sh 'kill $(ps aux | grep \'[p]ython3 ./shoxieAGod.py\' | awk \'{print $2}\')'
      }
    }
    stage('Run') {
      steps {
        sh 'ls'
        sh '''JENKINS_NODE_COOKIE=DONTKILLME
nohup python3 ./shoxieAGod.py > /home/admin/log/shoxieagod.log &
'''
      }
    }
  }
}