#!/bin/sh
python Recorder.py
flac output.wav -f
python fingerscrossed.py
