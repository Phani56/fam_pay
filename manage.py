#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.local")
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Settings')

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
