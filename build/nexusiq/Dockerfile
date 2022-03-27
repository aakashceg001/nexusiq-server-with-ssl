FROM sonatype/nexus-iq-server:1.135.0 as temp

USER root

RUN apt-get update && apt-get install -y python3

# Need to customize the config.yml to support https. 
# Reference config.yml: https://github.com/sonatype/docker-nexus-iq-server/blob/master/config.yml
RUN 

