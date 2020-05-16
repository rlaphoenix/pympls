rm -r build
rm -r dist
rm -r "pympls.egg-info"
python3 setup.py sdist bdist_wheel
sudo pip install .