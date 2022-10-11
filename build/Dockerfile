ARG APP_VERSION
FROM sonatype/nexus-iq-server:${APP_VERSION} as temp

USER root

RUN apt-get update && apt-get install -y python3

# Need to the config.yml to support https. 
# Reference config.yml: https://github.com/sonatype/docker-nexus-iq-server/blob/master/config.yml
ENV NEXUS_IQ_CONFIG_FILE="/etc/nexus-iq-server/config.yml"
ENV NEXUS_IQ_NEW_CONFIG_FILE="/tmp/config.yml"

COPY . . 
RUN python3 modify-config.py 

# Final Image
ARG APP_VERSION
FROM sonatype/nexus-iq-server:${APP_VERSION}
COPY --from=temp /tmp/config.yml /etc/nexus-iq-server/config.yml 
