import os
import yaml 

os.environ['NEXUS_IQ_CONFIG_FILE'] = 'build/nexusiq/config.yml'
os.environ['NEXUS_IQ_NEW_CONFIG_FILE'] = 'config-new.yml'

CONFIG_FILE = os.environ['NEXUS_IQ_CONFIG_FILE']
NEW_CONFIG_FILE = os.environ['NEXUS_IQ_NEW_CONFIG_FILE']

with open(CONFIG_FILE, "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        raise RuntimeError(exc)


config['server']['applicationConnectors'] = [
    {
        "type": "https",
        "port": "8443",
        "keyStorePath": r"${KEYSTORE_PATH}",
        "keyStorePassword": r"${KEYSTORE_PASSWORD}"
    }
]

config['server']['adminConnectors'] = [
    {
        "type": "https",
        "port": "8471",
        "keyStorePath": r"${KEYSTORE_PATH}",
        "keyStorePassword": r"${KEYSTORE_PASSWORD}"
    }
]

config['database'] = {
    "type": r"${DB_TYPE:-postgresql}",
    "hostname": r"${DB_HOST:-localhost}",
    "port": r"${DB_PORT:-5432}",
    "name": r"${DB_NAME:-postgres}",
    "username": r"${DB_USER:-postgres}",
    "password": r"${DB_PASS:-postgres}"
}

with open(NEW_CONFIG_FILE, "w") as stream:
    yaml.dump(config, stream)

