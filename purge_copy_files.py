#!/usr/bin/env python
import click
import os
import hashlib


@click.command()
@click.option('--dir', help='The person to greet.', required=True)
def say(dir):
    print("Filtering now...")
    print("\n")
    copies = calculate_digests(dir)
    display(copies)


ext = (".jpeg", ".png", ".py")


def check_for_double(file, file_hash, digest_map, copies):
    if file_hash not in digest_map.values():
        return False
    elif file_hash in digest_map.values():
        copies.append(file)
        return True


def calculate_digests(dir):
    digest_map = {}
    copies = []
    abs_directory = os.path.abspath(dir)
    for file in os.listdir(dir):
        abs_file = os.path.join(abs_directory, file)
        if os.path.isdir(file):
            continue
        elif file.lower().endswith(ext):
            block_size = 1048
            file_hash = hashlib.md5()
            with open(abs_file, "rb") as f:
                chunk = f.read(block_size)
                while chunk:
                    file_hash.update(chunk)
                    chunk = f.read(block_size)
                if not check_for_double(file, file_hash.hexdigest(), digest_map, copies):
                    digest_map[file] = file_hash.hexdigest()
    return copies


def display(copies):
    print("Possible duplicate files are:")
    for i in copies:
        print(i)


if __name__ == '__main__':
    say()
