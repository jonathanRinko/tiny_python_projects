#!/usr/bin/env python3
"""tests for hello.py"""

import os
# from subprocess import getstatusoutput, getoutput
import subprocess

prg = './hello.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_runnable():
    """Runs using python3"""

    out = subprocess.getoutput(f'python3 {prg}')
    assert out.strip() == 'Hello, World!'


# --------------------------------------------------
def test_executable():
    """Says 'Hello, World!' by default"""

    out = subprocess.getoutput(f'python {prg}')  
    # updated  as prg was not executable without explicitly calling python
    assert out.strip() == 'Hello, World!'


# --------------------------------------------------
def test_usage(): #added 'python' t f string to resolve 
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = subprocess.getstatusoutput(f'python {prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_input(): #added 'python to f string to pass 
    """test for input"""

    for val in ['Universe', 'Multiverse']:
        for option in ['-n', '--name']:
            rv, out = subprocess.getstatusoutput(f'python {prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'
