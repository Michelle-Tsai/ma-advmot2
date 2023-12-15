# export CURL_CA_BUNDLE="" # ssl
rm -r dist && rm -r build && rm -r maAdvMot2.egg-*
python setup.py sdist bdist_wheel
twine upload --repository testpypi dist/*