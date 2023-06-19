# Purpose
[Nexus IQ server](https://help.sonatype.com/iqserver) is an application provided by Sonatype Product. This repository helps you to setup the Nexus IQ application on a VM in on-premises or in Cloud with [SSL enabled](https://help.sonatype.com/iqserver/configuring/configuring-inbound-traffic#ConfiguringInboundTraffic-HTTPSConfigHTTPS/SSLConfiguration) & [external database support](https://help.sonatype.com/iqserver/configuring/external-database-configuration).  

# Pre-requisite
- SSL Certificates Keystore. 
- External Postgres DB details.
- RHEL or Centos VM.
  - VM admin account credentials needed and are updated in `group_vars/all.yaml` file. 

# Sections
This repository has two sections:
- build
- deploy

## Build
In the build phase, 
- The official nexus iq application from Docker Hub is pulled and the `config.yaml` file is configured to include SSL & external DB related configurations.
- The new custom Image is pushed to Docker Registry.

## Deploy
In the deploy phase, 
- Ansible scripts are used to configure the VM to install required packages like Docker.
- Deploy the new custom Image generated in the build phase as a Docker container. 

# Upgrade
- To upgrade nexusiq application, just change the iq version in the `app_properties.json` file.

