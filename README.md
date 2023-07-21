# c2-py-samples

Samples for the Python ChronoCloud (C2) library

## Introduction

The C2 platform enables distributed computing using untrusted 3rd party data.
Consumers can perform calculations on externally-managed data and models
with the same confidence and assurances as on internal artifacts.

The following samples illustrate common solutions built on top of the C2 library and services.

## Setup

### Install the c2-py library

- Clone the `c2-py` repository `https://github.com/pit-labs/c2-py.git`.
  - `c2-py` is the Python library for interacting with the ChronoCloud (C2) environment. 
  It is required by most command-line tools and data science workflows.
  - At the time of this limited release, the repository is private. 
  It can be cloned using GitHub Desktop or another authenticated solution.
  - This guide assumes the repository has been cloned to the local path `~/c2/c2-py`.
- Install the `c2py` Python package from the cloned repository:
```commandline
pip install ~/c2/c2-py
```

### Configure C2 access

If you have previously configured C2 access, for instance when using the `c2-py-tools` package,
you can re-use those settings by copying `.env` file to the `c2-py-samples` folder.
If this is your first time working with C2, you should configure new settings.

If this is your first time accessing C2, please install the `c2-py-tools` package 
and follow the setup instructions using the `config_env` script provided in that package. 
