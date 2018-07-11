# Simple ChatBot


## Prerequisites

1.- Install IBM Cloud CLI

```
curl -sL https://ibm.biz/idt-installer | bash
ibmcloud login
ibmcloud target -o org -s space
```

2.- Connect to the API endpoint
```
bluemix api https://api.ng.bluemix.net
```

3.- Install Watson Developer Cloud library for python
```
git clone https://github.com/watson-developer-cloud/python-sdk/tree/develop/examples
pip install --upgrade "watson-developer-cloud>=1.4.0"

```

Verify installation
```
pip show watson-developer-cloud
```

### Running

Simply run wtsn.py
```
python wtsn.py
```

## Authors
@leguiart

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgments
(TODO)


