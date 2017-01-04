#! /usr/bin/python2
# -*- coding : utf8 -*-

from os import chmod
from os.path import dirname, realpath, join
from shutil import copy
from crontab import CronTab


print("Initializing paths...")

base_path = dirname(realpath(__file__))
print("\t- " + base_path)

watcher_path = join(base_path, "directory-watcher")
print("\t- " + watcher_path)

conf_path = join(watcher_path, "conf")
print("\t- " + conf_path)

print("Copying configuration files...")

# copy(join(conf_path, "profiles.yaml.dist"), join(conf_path, "profiles.yaml"))
print("\t- profiles.yaml")

# copy(join(conf_path, "directories.yaml.dist"), join(conf_path, "directories.yaml"))
print("\t- directories.yaml")

print("Access rights management...")
chmod(join(watcher_path, "watcher.py"), 0o755)
print("\t- chmod +x " + join(watcher_path, "watcher.py"))

print("Arguments initialization...")
arguments = " >> {0} 2>> {1}".format(
    join(base_path, "logs", "watcher.log"),
    join(base_path, "logs", "watcher-errors.log")
)
print("\t- " + arguments)

# Put on a cron to execute on each minute
cron = CronTab(user=True)

job = cron.new(command=watcher_path + arguments, comment="Directory Watcher")
job.setall("* * * * *")

# cron.write()
