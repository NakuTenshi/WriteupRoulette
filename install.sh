#!/usr/bin/env bash

file='./writeuproulette.py'
name="$(basename "${file%.py}")"

cp -r $file ~/.local/bin/$name
cp -r ./writeups ~/.local/share/


echo "done."