# OSL API

## Installation

Currently, you can install google sheet simple api by its github's CVS url:

```bash
pip install git+https://github.com/AnthonyDugarte/osl_api.git@0.0.1#osl_api
```

Or, by appending it at your _requirements.txt_:

```bash
echo -e "\ngit+https://github.com/AnthonyDugarte/osl_api.git@0.0.1#osl_api" >> requirements.txt
```

## Setup

### Dependencies

```bash
pip install -r requirements.txt
```

### Environment variables

Create filled `.env` based on [.env.example](.env.example)

```bash
source .env
```

## Usage

Check for available requests at:

- [v2](https://bctv2.docs.apiary.io)
- [v3](https://bctv3.docs.apiary.io)

### Initialization

```python
from osl_api import OslClient

client = OslClient()
```

#### Example request

##### Get Orders list

```python
client.request(path="/api/3/trade/list", method="POST")
```
