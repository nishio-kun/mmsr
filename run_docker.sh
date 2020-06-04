sudo nvidia-docker build -t mmsr -f docker/Dockerfile .
sudo nvidia-docker run -v mmsr:/mmsr/ -it mmsr /bin/bash
