# aplicacion


docker run -it -p 8080:8080 -v /workspace/aplicacion/aplicacion:/aplicacion --name aplicacionweb -h aplicacionweb ubuntu:20.04

apt update
apt install -y python3
apt install -y python3-pip
pip3 install web.py