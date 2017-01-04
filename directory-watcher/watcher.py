#! /usr/bin/python2
# -*- coding : utf8 -*-


def load_yaml_configuration(file_name):
    from yaml import load

    return load(open(file_name, "r"))


def list_files_in_dir(dir_path):
    from os import listdir
    from os.path import isfile, join

    return [join(dir_path, f) for f in listdir(dir_path) if isfile(join(dir_path, f))]


def apply_profiles_to_configuration(watched_directories, profiles):
    from copy import deepcopy

    # Use only a copy of the configuration dicts, prevents loops
    watched_directories = deepcopy(watched_directories)

    if watched_directories is not None:
        for watched_directory in watched_directories:
            if "rules_profile" in watched_directory:
                if watched_directory["rules_profile"] in profiles:
                    profile = profiles[watched_directory["rules_profile"]]

                    if "rules" not in watched_directory:
                        watched_directory["rules"] = []

                    # Use only a copy of the configuration dicts, prevents loops
                    watched_directory["rules"] += deepcopy(profile["rules"])
                    del watched_directory["rules_profile"]

                else:
                    raise Exception(
                        "profile {0} does not exist".format(
                            watched_directory["rules_profile"]
                        )
                    )

    return watched_directories


def apply_directory_rules(watched_directory):
    files_list = list_files_in_dir(watched_directory["directory_path"])

    for file_path in files_list:
        is_transfered = False

        for rule in watched_directory["rules"]:
            if is_transfered:
                break

            if does_file_respect_rule(file_path, rule):
                transfer_file(file_path, rule["destination_folder"])
                is_transfered = True


def does_file_respect_rule(file_path, rule):
    from os.path import splitext, basename

    file_name, file_extension = splitext(basename(file_path))

    # Removes the extension's trailing dot
    file_extension = file_extension[1:]

    if "extensions" in rule:
        if file_extension not in rule["extensions"]:
            return False

    if "ignore_hidden" in rule:
        if rule["ignore_hidden"] is True and file_name.startswith("."):
            return False

    if "title_contains" in rule:
        if rule["title_contains"] not in file_name:
            return False

    return True


def transfer_file(file_path, destination):
    from os.path import basename, join
    from shutil import move

    new_file = join(destination, basename(file_path))
    print("{0} -> {1}".format(file_path, new_file))
    move(file_path, new_file)


def main():
    from os.path import dirname, realpath, join

    base_path = dirname(realpath(__file__))
    conf_path = join(base_path, "conf")

    profiles = load_yaml_configuration(join(conf_path, "profiles.yaml"))
    configuration = load_yaml_configuration(join(conf_path, "directories.yaml"))

    configuration = apply_profiles_to_configuration(
        configuration,
        profiles
    )

    if configuration is not None:
        for watched_directory in configuration:
            apply_directory_rules(watched_directory)


if __name__ == '__main__':
    main()
