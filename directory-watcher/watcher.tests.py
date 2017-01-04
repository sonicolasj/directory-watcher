# -*- coding : utf8 -*-
import watcher


def test_does_file_respect_rule():
    file = "/foo/bar/baz/random_file.foo"
    rule = {
        "extensions": ["foo", "bar"],
        "title_contains": "file",
        "ignore_hidden": True
    }

    return watcher.does_file_respect_rule(file, rule) == True


def test_file_wrong_extension():
    file = "/foo/bar/baz/random_file.foo"
    rule = {
        "extensions": ["bar", "baz"]
    }

    return watcher.does_file_respect_rule(file, rule) == False


def test_file_does_not_contain_string():
    file = "/foo/bar/baz/random_thing.foo"
    rule = {
        "extensions": ["foo", "bar"],
        "title_contains": "file",
        "ignore_hidden": False,
    }

    return watcher.does_file_respect_rule(file, rule) == False


def test_file_is_hidden():
    file = "/foo/bar/baz/.random_file.foo"
    rule = {
        "extensions": ["foo", "bar"],
        "title_contains": "file",
        "ignore_hidden": True,
    }

    return watcher.does_file_respect_rule(file, rule) == False


if __name__ == '__main__':
    tests = [
        test_does_file_respect_rule,
        test_file_wrong_extension,
        test_file_does_not_contain_string,
        test_file_is_hidden
    ]

    for test in tests:
        print(test.__name__)
        if test():
            print("...Passed\n")
        else:
            print("...Failed\n")
