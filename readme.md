# CV-Generator

## Overview

**CV-Generator** is a tool that helps you to generate your cv with a simple yaml, it is simple but really useful, specially for cs major students.


## Features

- **Easy YAML Configuration:** Quickly input your information using a straightforward YAML format.

- **PDF Output**: Generate a high-quality PDF that's ready to be shared or printed.

- **English and Chinese Support**: Choose between English and Chinese for your CV.

## Getting Started

### Prerequisites
Python 3.x
### Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/cv-generator.git
cd cv-generator
```
2. Install the required packages
```bash
pip install -r requirements.txt
```
3. Edit the `cv.yaml` file with your information. The file can be formatted as follows:
```yaml
metadata:
  version: english
name: Nai Long
email: xxxx@gmail.com
picture: "picture.jpeg"
github: https://github.com/xxx
homepage: https://xxx.github.io

education-experience:
  - name: XXX University
    duration: 2023/09 -- 2026/06
    field: Cybersecurity
    award: Recommended for exemption
  - name: XXX University
    duration: 2019/09 -- 2023/06
    field: software Engineering
    award: First-class scholarship, outstanding student

work-experience:
  - name: xxx
    duration: 2023/09 -- 2026/06
    summary: xxxx
    details:
      - item: xxx
      - item: xxx

research-experience:
  - name: xxx
    price: nips
    duration: 2023/09 -- 2026/06
    details:
      - item: xxx
      - item: xxx

project-experience:
  - name: xxx
    price: xxx
    duration: 2023/09 -- 2026/06
    details:
      - item: xxx
      - item: xxx

skills:
  - name: programming language
    details: cpp, golang
  - name: tools
    details: docker
  - name: english
    details: cet-6
```
You can change the `version` field in metadata to `chinese` to generate a Chinese CV. And delete the field that you don't need.

## Showcases
![Preview]("resume.png")

## Acknowledgements

[Chi's cv] (https://github.com/skyzh/chicv)