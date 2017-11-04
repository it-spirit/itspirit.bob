# -*- coding: utf-8 -*-
"""Pre- and Post-Render Hooks for mr.bob."""

# pyhton imports
import subprocess


def get_git_info(value):
    """Try to get information from the git-config."""
    gitargs = ['git', 'config', '--get']
    try:
        result = subprocess.check_output(gitargs + [value]).strip()
        return result
    except (OSError, subprocess.CalledProcessError):
        pass


def prepare_diazo_render(configurator):
    """Some variables to make templating easier."""
    namespace = 'spirit'
    namespace2 = 'diazo'

    dottedname = '.'.join([
        namespace,
        namespace2,
        configurator.variables['package.name'],
    ])
    configurator.variables['package.dottedname'] = dottedname
    configurator.variables['package.namespace'] = namespace
    configurator.variables['package.namespace2'] = namespace2

    # package.uppercasename = 'SPIRIT_DIAZO_MYTHEME'
    configurator.variables['package.uppercasename'] = \
        dottedname.replace('.', '_').upper()

    camelcasename = dottedname.replace('.', ' ').title()\
        .replace(' ', '')\
        .replace('_', '')
    testlayer = '{0}Layer'.format(camelcasename)

    # package.testlayer = 'SpiritDiazoMythemeLayer'
    configurator.variables['package.testlayer'] = testlayer

    browserlayer = 'I{0}'.format(testlayer)
    # package.browserlayer = 'ISpiritDiazoMythemeLayer'
    configurator.variables['package.browserlayer'] = browserlayer

    # package.longname = 'spiritdiazomytheme'
    configurator.variables['package.longname'] = camelcasename.lower()


def pre_email(configurator, question):
    """Get email from git."""
    default = get_git_info('user.email')
    if default:
        question.default = default


def pre_username(configurator, question):
    """Get email from git and validate package name."""
    default = get_git_info('user.name')
    if default:
        question.default = default
