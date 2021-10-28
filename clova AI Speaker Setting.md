## install
  - sudo apt-get update
  - sudo apt-get upgrade
  - git clone https://github.com/naver/clova-extension-sample-dice.git
  - cd clova-extension-sample-dice
  - git checkout tutorial1

## nodejs & npm install
  - sudo apt-get install nodejs npm
  - npm install

## ufw 설정
  - sudo ufw allow 22
  - sudo ufw reload

## 3000번 포트 열기
  - sudo iptables -I INPUT 1 -p tcp --dport 3000 -j ACCEPT
