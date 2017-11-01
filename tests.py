# -*- coding: utf-8 -*-
"""Tests for spirit.bob templates."""

# python imports
from scripttest import TestFileEnvironment
import os
import shutil
import tempfile
import unittest


class BaseTemplateTest(unittest.TestCase):
    """Base class for all spirit.bob test cases."""

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tempdir)

        # docs http://pythonpaste.org/scripttest/
        self.env = TestFileEnvironment(
            os.path.join(self.tempdir, 'test-output'),
            ignore_hidden=False,
        )

    def create_template(self):
        """Run mr.bob to create your template."""
        options = {
            'dir': os.path.join(os.path.dirname(__file__)),
            'template': self.template,
            'answers_file': self.answers_file,
        }
        return self.env.run(
            '{dir}/bin/mrbob --config '
            '{dir}/{answers_file} {dir}/src/spirit/bob/{template}'.format(
                **options
            )
        )


class DiazoThemeTest(BaseTemplateTest):
    """Test case for the `diazo_theme` template."""

    template = 'diazo_theme'

    def test_base_template(self):
        """Validate the `diazo_theme` template.

        Generate a project from a template, test which files were created
        and run all tests in the generated package.
        """
        self.maxDiff = None
        self.answers_file = 'test_answers/diazo_theme_base.ini'
        result = self.create_template()
        p = 'spirit.diazo.base'
        p_src = p + '/src/spirit/diazo'
        p_src_pkg = p_src + '/base'
        expected = [
            p,
            p + '/.csslintrc',
            p + '/.editorconfig',
            p + '/.gitignore',
            p + '/.jshintignore',
            p + '/.travis.yml',
            p + '/CHANGES.rst',
            p + '/README.rst',
            p + '/bootstrap.py',
            p + '/buildout.cfg',
            p + '/docs',
            p + '/docs/README',
            p + '/docs/_images',
            p + '/docs/_images/README',
            p + '/docs/source',
            p + '/docs/source/_static',
            p + '/docs/source/_static/logo.png',
            p + '/docs/source/_templates',
            p + '/docs/source/_templates/empty',
            p + '/docs/source/conf.py',
            p + '/docs/source/configuration.rst',
            p + '/docs/source/index.rst',
            p + '/setup.cfg',
            p + '/setup.py',
            p + '/src',
            p + '/src/spirit',
            p + '/src/spirit/__init__.py',
            p_src,
            p_src + '/__init__.py',
            p_src_pkg,
            p_src_pkg + '/Extensions',
            p_src_pkg + '/Extensions/install.py',
            p_src_pkg + '/__init__.py',
            p_src_pkg + '/config.py',
            p_src_pkg + '/configure.zcml',
            p_src_pkg + '/diazo_resources',
            p_src_pkg + '/diazo_resources/favicon.ico',
            p_src_pkg + '/diazo_resources/index.html',
            p_src_pkg + '/diazo_resources/manifest.cfg',
            p_src_pkg + '/diazo_resources/preview.png',
            p_src_pkg + '/diazo_resources/rules.xml',
            p_src_pkg + '/diazo_resources/static',
            p_src_pkg + '/diazo_resources/static/main.css',
            p_src_pkg + '/diazo_resources/static/main.js',
            p_src_pkg + '/interfaces.py',
            p_src_pkg + '/locales',
            p_src_pkg + '/locales/en',
            p_src_pkg + '/locales/en/LC_MESSAGES',
            p_src_pkg + '/locales/en/LC_MESSAGES/spirit.diazo.base.po',
            p_src_pkg + '/locales/manual.pot',
            p_src_pkg + '/locales/plone.pot',
            p_src_pkg + '/locales/spirit.diazo.base.pot',
            p_src_pkg + '/migration.py',
            p_src_pkg + '/profiles',
            p_src_pkg + '/profiles.zcml',
            p_src_pkg + '/profiles/default',
            p_src_pkg + '/profiles/default/browserlayer.xml',
            p_src_pkg + '/profiles/default/cssregistry.xml',
            p_src_pkg + '/profiles/default/jsregistry.xml',
            p_src_pkg + '/profiles/default/metadata.xml',
            p_src_pkg + '/profiles/default/spiritdiazobase_marker.txt',
            p_src_pkg + '/profiles/default/theme.xml',
            p_src_pkg + '/profiles/uninstall',
            p_src_pkg + '/profiles/uninstall/browserlayer.xml',
            p_src_pkg + '/profiles/uninstall/theme.xml',
            p_src_pkg + '/setuphandlers.py',
            p_src_pkg + '/template_overrides',
            p_src_pkg + '/template_overrides/README',
            p_src_pkg + '/testing.py',
            p_src_pkg + '/tests',
            p_src_pkg + '/tests/__init__.py',
            p_src_pkg + '/tests/robot',
            p_src_pkg + '/tests/robot/keywords.robot',
            p_src_pkg + '/tests/robot/test_setup.robot',
            p_src_pkg + '/tests/test_robot.py',
            p_src_pkg + '/tests/test_setup.py',
            p + '/travis.cfg',
        ]
        self.assertItemsEqual(result.files_created.keys(), expected)

    def test_extended_template(self):
        """Validate the `diazo_theme` template.

        Generate a project from a template, test which files were created
        and run all tests in the generated package.
        """
        self.maxDiff = None
        self.answers_file = 'test_answers/diazo_theme_extended.ini'
        result = self.create_template()
        p = 'spirit.diazo.extended'
        p_src = p + '/src/spirit/diazo'
        p_src_pkg = p_src + '/extended'
        expected = [
            p,
            p + '/.csslintrc',
            p + '/.editorconfig',
            p + '/.gitignore',
            p + '/.jshintignore',
            p + '/.travis.yml',
            p + '/CHANGES.rst',
            p + '/README.rst',
            p + '/bootstrap.py',
            p + '/buildout.cfg',
            p + '/docs',
            p + '/docs/README',
            p + '/docs/_images',
            p + '/docs/_images/README',
            p + '/docs/source',
            p + '/docs/source/_static',
            p + '/docs/source/_static/logo.png',
            p + '/docs/source/_templates',
            p + '/docs/source/_templates/empty',
            p + '/docs/source/conf.py',
            p + '/docs/source/configuration.rst',
            p + '/docs/source/index.rst',
            p + '/setup.cfg',
            p + '/setup.py',
            p + '/src',
            p + '/src/spirit',
            p + '/src/spirit/__init__.py',
            p_src,
            p_src + '/__init__.py',
            p_src_pkg,
            p_src_pkg + '/Extensions',
            p_src_pkg + '/Extensions/install.py',
            p_src_pkg + '/__init__.py',
            p_src_pkg + '/config.py',
            p_src_pkg + '/configure.zcml',
            p_src_pkg + '/diazo_resources',
            p_src_pkg + '/diazo_resources/favicon.ico',
            p_src_pkg + '/diazo_resources/index.html',
            p_src_pkg + '/diazo_resources/manifest.cfg',
            p_src_pkg + '/diazo_resources/preview.png',
            p_src_pkg + '/diazo_resources/rules.xml',
            p_src_pkg + '/diazo_resources/static',
            p_src_pkg + '/diazo_resources/static/main.css',
            p_src_pkg + '/diazo_resources/static/main.js',
            p_src_pkg + '/interfaces.py',
            p_src_pkg + '/locales',
            p_src_pkg + '/locales/en',
            p_src_pkg + '/locales/en/LC_MESSAGES',
            p_src_pkg + '/locales/en/LC_MESSAGES/spirit.diazo.extended.po',
            p_src_pkg + '/locales/manual.pot',
            p_src_pkg + '/locales/plone.pot',
            p_src_pkg + '/locales/spirit.diazo.extended.pot',
            p_src_pkg + '/migration.py',
            p_src_pkg + '/profiles',
            p_src_pkg + '/profiles.zcml',
            p_src_pkg + '/profiles/default',
            p_src_pkg + '/profiles/default/browserlayer.xml',
            p_src_pkg + '/profiles/default/cssregistry.xml',
            p_src_pkg + '/profiles/default/jsregistry.xml',
            p_src_pkg + '/profiles/default/metadata.xml',
            p_src_pkg + '/profiles/default/spiritdiazoextended_marker.txt',
            p_src_pkg + '/profiles/default/theme.xml',
            p_src_pkg + '/profiles/uninstall',
            p_src_pkg + '/profiles/uninstall/browserlayer.xml',
            p_src_pkg + '/profiles/uninstall/theme.xml',
            p_src_pkg + '/setuphandlers.py',
            p_src_pkg + '/template_overrides',
            p_src_pkg + '/template_overrides/README',
            p_src_pkg + '/testing.py',
            p_src_pkg + '/tests',
            p_src_pkg + '/tests/__init__.py',
            p_src_pkg + '/tests/robot',
            p_src_pkg + '/tests/robot/keywords.robot',
            p_src_pkg + '/tests/robot/test_setup.robot',
            p_src_pkg + '/tests/test_robot.py',
            p_src_pkg + '/tests/test_setup.py',
            p + '/travis.cfg',
        ]
        self.assertItemsEqual(result.files_created.keys(), expected)
