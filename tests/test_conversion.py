import memtrace2npz
import pytest
import tempfile
import zipfile
import os
import filecmp
import subprocess

def test_conversion():

    # Create tmp directory
    with tempfile.TemporaryDirectory() as tmpdirname:

        # Unzip file into tmp
        with zipfile.ZipFile('./tests/data/trace.zip', 'r') as zip_ref:
            zip_ref.extractall(tmpdirname)
        count = 0

        # Yes its hacky. TODO: cleanup
        for root, dirs, files in os.walk(tmpdirname):
            for filename in files:
                tracefile = filename

        # Run converter, output to tmp
        infile  = '{}/{}'.format(tmpdirname, tracefile)
        outfile = '{}/testout.npz'.format(tmpdirname)
        memtrace2npz.file_to_npz(infile, outfile)

        # Check that converter output matches gold.npz
        assert filecmp.cmp('./tests/data/gold.npz', outfile)

def test_cli_conversion():

    # Create tmp directory
    with tempfile.TemporaryDirectory() as tmpdirname:

        # Unzip file into tmp
        with zipfile.ZipFile('./tests/data/trace.zip', 'r') as zip_ref:
            zip_ref.extractall(tmpdirname)
        count = 0

        # Yes its hacky. TODO: cleanup
        for root, dirs, files in os.walk(tmpdirname):
            for filename in files:
                tracefile = filename

        # Run converter, output to tmp
        infile  = '{}/{}'.format(tmpdirname, tracefile)
        outfile = '{}/testout.npz'.format(tmpdirname)

        subprocess.run(["memtrace2npz", "-i", infile, "-o", outfile])

        # Check that converter output matches gold.npz
        assert filecmp.cmp('./tests/data/gold.npz', outfile)

