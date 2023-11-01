import enum
import os
from configparser import ConfigParser
from pathlib import Path

from rithmic.tools.general import get_credentials_path
from rithmic.tools.pyrithmic_exceptions import EnvironmentNotConfiguredException, ConfigFileNotFoundException

ENVIRONMENT_MAP = dict(
    RITHMIC_TEST='RITHMIC_TEST',
    RITHMIC_PAPER_TRADING='RITHMIC_PAPER_TRADING',
    RITHMIC_LIVE='RITHMIC_LIVE',
)

PATH_PROJECT_ROOT = Path(__file__).parent.parent


class RithmicEnvironment(enum.Enum):
    RITHMIC_TEST = 'RITHMIC_TEST'
    RITHMIC_PAPER_TRADING = 'RITHMIC_PAPER_TRADING'
    RITHMIC_LIVE = 'RITHMIC_LIVE'


def _get_config_file(environment: RithmicEnvironment):
    try:
        environment = ENVIRONMENT_MAP[environment.value]
    except KeyError as e:
        raise EnvironmentNotConfiguredException('Environment {0} is not configured, available options: {1}'.format(
            environment, ', '.join(ENVIRONMENT_MAP.keys())
        ))
    path = get_credentials_path()
    config_file = path / '{0}.ini'.format(environment)
    if config_file.exists() is False:
        raise ConfigFileNotFoundException('No Config File found at {0}'.format(config_file))
    return config_file


def get_default_rithmic_environment():
    env_name = os.environ['RITHMIC_ENVIRONMENT_NAME']
    return getattr(RithmicEnvironment, env_name)


def get_rithmic_credentials(environment: RithmicEnvironment = None):
    environment = environment if environment is not None else get_default_rithmic_environment()
    parser = ConfigParser()
    parser.read(_get_config_file(environment))
    return dict(parser.items('credentials'))
