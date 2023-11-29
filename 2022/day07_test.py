# TIM 2023
# Advent of Code
# Tag 7: No Space Left On Device
# Autor: Stefan Mohr (stefan.mo)
# Requirements: pytest

from day07 import solve_part_1, solve_part_2, read_puzzle


def dummy_puzzle(filename):
    return read_puzzle(filename)


def test_part_1():
    assert solve_part_1("""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""") == 95437


def test_part_2():
    assert solve_part_2("""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""") == None

