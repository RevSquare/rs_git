# -*- coding: utf-8 -*-
import os

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from optparse import make_option


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--branch'),
        make_option('--remote'),
        make_option('--requirements'),
    )

    def handle(self, *args, **options):
        import subprocess

        # setup option variables
        branch = options.get('branch')
        if branch is None:
            branch = getattr(settings, 'RSGIT_DEVELOPPMENT_BRANCH', None)
        if branch is None:
            raise CommandError('--branch or settings.RSGIT_DEVELOPPMENT_BRANCH is required')

        remote = options.get('remote')
        if remote is None:
            remote = 'origin'

        requirements = options.get('requirements')
        if requirements is None:
            requirements = getattr(settings, 'RSGIT_REQUIREMENTS_FILE', None)
        if requirements is None:
            raise CommandError('--requirements or settings.RSGIT_REQUIREMENTS_FILE is required')

        def call(cmd):
            env = os.environ.copy()
            env.update({'EDITOR': ''})
            return subprocess.Popen(cmd,
                                    stdout=subprocess.PIPE,
                                    cwd=settings.BASE_DIR,
                                    env=env
                                    ).communicate()[0].strip()

        call(['git', 'checkout', branch])
        call(['git', 'pull', remote, branch])
        subprocess.call('pip install -r %s' % requirements, shell=True)
        call_command('syncdb')
        call_command('migrate')

        frontend = getattr(settings, 'RSGIT_FRONTEND', None)
        if frontend:
            call(['git', 'subtree', 'pull', '--prefix=%s' % frontend['path'], frontend['remote'], frontend['branch']])
