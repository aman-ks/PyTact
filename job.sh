#!/bin/sh
python Recorder.py
flac output.wav -f
python win.py output.flac
