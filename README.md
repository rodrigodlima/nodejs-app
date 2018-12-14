# nodejs-app

Repositório para realizar o deploy de uma aplicação NodeJS de exemplo na Amazon EC2. A distribuição Linux usada no deploy é a Ubuntu 16.04 LTS 64Bits (Xenial).

Este repositório contém playbooks Ansible com algumas roles:

- Deploy:

Faz o deploy da aplicação NodeJS de exemplo, utilizando o módulo PM2 para garantir escabilidade, balanceamento de carga e outras features que o NodeJS por si só não possui. Para maiores informações sobre o PM2: http://pm2.keymetrics.io/

- NodeJS:

Faz a instalação e configuração do NodeJS na última versão LTS.

- PM2:

Faz a instalação e configuração do módulo PM2.

- nginxinc.nginx:

Faz a instalação do Nginx e faz a configuração de um proxy reverso para a aplicação Nodejs de exemplo. Este módulo é o oficial do Nginx para o Ansible, com algumas modificações necessárias para o funcionamento do deploy utilizado no exemplo.

- Rollback:

Role para realizar o rollback de algum deploy que não funcionou corretamente.


# Pré requisitos

Para realizar o deploy, é necessário ter uma conta na Amazon e ter configurado o AWS CLI na estação que fará o deploy. 
Para maiores informações sobre como efetuar a configuração do AWS CLI consulte a seguinte documentação:
https://docs.aws.amazon.com/pt_br/cli/latest/userguide/installing.html

# Deploy da aplicação na Amazon

$ git clone -b develop https://github.com/rodrigodlima/nodejs-app.git

$ aws cloudformation create-stack --stack-name Stack_Name --template-body file://///nodejs-app/cloudformation-stack/deploy-nodejs-app.json --parameters ParameterKey=KeyName,ParameterValue=your_key --on-failure DO_NOTHING

Obs: altere Stack_name para o nome da stack de sua preferência e ParameterValue para o nome do seu par de chaves utilizado na Amazon. Você precisa ter essa chave na região que for realizar o deploy.

A região que será realizado o deploy é a região que está configurado no seu ambiente (AWS CLI). As seguintes regiões são suportadas neste deploy:

"us-east-1"        
"us-west-2"        
"us-west-1"        
"eu-west-1"        
"eu-west-2"        
"eu-west-3"        
"eu-central-1"     
"ap-northeast-1"   
"ap-northeast-2"   
"ap-southeast-1"  
"ap-southeast-2"   
"ap-south-1"       
"us-east-2"       
"ca-central-1"   
"sa-east-1"        

Por default, o deploy é realizado em uma instância T2.small. Caso queira alterar, basta passar o parâmetro InstanceType. Ex:

$ aws cloudformation create-stack --stack-name Stack_Name --template-body file://///nodejs-app/cloudformation-stack/deploy-nodejs-app.json --parameters ParameterKey=KeyName,ParameterValue=your_key ParameterKey=IntanceType,ParameterValue=t2.medium --on-failure DO_NOTHING


# Status do deploy

Para acompanhar o status da stack que você acabou de disparar, pode ser feito pelo Console da AWS, ou então via CLI:

$ aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --query '"StackSummaries"[*]."StackStatus"'


Após o deploy da stack ser conclúida, é disparado o deploy via Ansible, e isso deve demorar alguns minutos.

Verifique o IP público que foi disponibilizado no deploy:

$ aws ec2 describe-addresses --filters "Name=domain,Values=vpc" --query 'Addresses[*]."PublicIp"'


Para validar a aplicação acesse a url:

http://public_ip/
https://public_ip/

