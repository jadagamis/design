#!/usr/bin/env python
import click
import os
import hashlib


@click.command()
@click.option('--dir', help='The person to greet.', required=True)
def say(dir):
    print("Filtering now...")
    for file in os.listdir(dir):
        print(file)
    get_hash(dir)
    display()


hash_map = {}
copies = []
ext = (".jpeg", ".png", ".py")


def map_update(file, file_hash):
    hash_map[file] = file_hash


def check_for_double(file, file_hash):
    if file_hash not in hash_map.values():
        return True
    elif file_hash in hash_map.values():
        copies.append(file)
        return False


def get_hash(dir):
    for file in os.listdir(dir):
        if os.path.isdir(file):
            pass
        elif file.lower().endswith(ext):
            print(file)
            block_size = 32768
            file_hash = hashlib.md5()
            with open(file, "rb") as f:
                # for byte_block in iter(lambda: f.read(block_size),b""):
                #     file_hash.update(byte_block)
                chunk = f.read(block_size)
                while chunk:
                    file_hash.update(chunk)
                    if check_for_double(file, file_hash):
                        map_update(file, file_hash.hexdigest())


def display():
    print("Possible duplicate files are:")
    print(copies)

if __name__ == '__main__':
    say()
