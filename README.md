# Decoding Sensor Data with Python

- [Decoding Sensor Data with Python](#decoding-sensor-data-with-python)
  - [Installation](#installation)
    - [Verify Local Environment](#verify-local-environment)
    - [Windows](#windows)
    - [macOS](#macos)
    - [About pip](#about-pip)
  - [Verify Setup](#verify-setup)

## Installation

### Verify Local Environment

### Windows

Open a command prompt or powershell and run the following commands, replacing 'project-root' with the path to the root folder of the project.

``` bash
> cd 'project-root'
> python -m venv venv
> venv\Scripts\activate.bat
> pip install -r requirements.txt
```

### macOS

Open a terminal and run the following commands, replacing 'project-root' with the path to the root folder of the project.

```bash
> cd 'project-root'
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
```

*Note: If you've installed Python 3 using a method other than Homebrew, you might need to type `python` in the second command instead of `python3`.*

### About pip

`pip` updates frequently, but versions greater than 10.x.x should work with this project.

## Verify Setup
``` bash
> pytest
> python sensor/sensor.py
```
