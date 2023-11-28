#!/usr/bin/env bash
#exit on error
set -o errexit

pipi install --upgrade pip
pip install -r requirements.txt