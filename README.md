
<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>

<h1 align="center">apple-health-bot</h1>

<p align="center">
    <em>Helping you understand your health data</em>
</p>

<p align="center">
    <img src="https://img.shields.io/github/license/nk3750/AppleHealthLLMBot?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
    <img src="https://img.shields.io/github/last-commit/nk3750/AppleHealthLLMBot?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/nk3750/AppleHealthLLMBot?style=default&color=0080ff" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/nk3750/AppleHealthLLMBot?style=default&color=0080ff" alt="repo-language-count">
</p>
`apple-health-bot` lets you easily query your Apple Health data leveraging OpenAi LLM and RAG over SQL. 

![Health Bot gif demo](img/demo.gif)
## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Modules](#modules)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Tests](#tests)
- [Project Roadmap](#project-roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

apple-health-bot works by converting your apple health export data to CSV and then performing RAG over SQL on top of those CSV to help answer your queries. It transforms XML data into CSVs via `xmldataparser.py`, ensuring seamless data analysis. The `appleHealthBot.py` categorizes user queries for workouts, sleep, or exerciseTime, storing information in an SQL database. Leveraging AI tools like ChatOpenAI, the bot retrieves and presents data, enhancing user experience and data visualization capabilities. The projects streamlined workflow and data management cater to health enthusiasts seeking efficient health data processing and analysis.

---

## Repository Structure

```
AppleHealthLLMBot/
├── Dockerfile
├── LICENSE
├── README.md
├── dataParser
│   └── xmldataparser.py
├── entrypoint.sh
├── healthBot
│   └── appleHealthBot.py
└── setup
    └── requirements.txt
```

---

## Modules

- **entrypoint.sh**: Trigger scripts based on user input
- **Dockerfile**: Defines Docker image setup for Python-based application.
- **setup/requirements.txt**: Lists essential dependencies for the project.
- **healthBot/appleHealthBot.py**: Performs RAG over SQL data using langchain and OpenAI
- **dataParser/xmldataparser.py**: Converts Apple Health XML data into structured CSVs, to be loaded in to sqlLite DB.

---

## Getting Started

### Get Your Apple Health Data

For instructions on how to export your Apple Health data, please follow the [Apple Support guide](https://support.apple.com/guide/iphone/share-your-health-data-iph5ede58c3d/ios).

Or follow the instructions below

![Export Gif](img/export.gif)

### System Requirements

- **Docker**: Latest version

### Installation

**From Source**

1. Clone the repository:
   ```
   git clone https://github.com/nk3750/apple-health-bot.git
   ```
2. Change to the project directory:
   ```
   cd apple-health-bot
   ```
3. Edit the .env file
   ```
   vim .env
   ```
   Replace YOUR_OPENAI_API_KEY with your OpenAI API Key

4. Copy the `export.xml` file from the health app to the project directory:
   ```
   cp /path/to/export.xml .
   ```

### Setup

**Create Docker Image**

1. Build the Docker image:
   ```
   docker build -t healthbot .
   ```

### Usage

**Parse the XML and Create CSV Files**

```
docker run -v "$(pwd)":/data healthbot parseData /data/export.xml
```
This is a long-running process and might take around 8-10 minutes depending on the size of your export.xml file, go get yourself a coffee or something. 

This is how it should look like once the script is executed successfully.
![Parse](img/parse.png)

**Start the Bot**

```
docker run -it -v "$(pwd)":/data healthbot healthBot
```
Have fun!
---

## Project Roadmap

- [ ] Fix inaccuracies with the handling of sleep data
- [ ] Handle complex queries involving sleep and workout
- [ ] Add testing details

---

## Contributing

Contributions are welcome! Here are several ways you can contribute:

- **Report Issues**: Submit bugs or feature requests.
- **Submit Pull Requests**: Review open PRs or submit your own.
- **Join the Discussions**: Share insights or ask questions.

Please follow the [Contributing Guidelines](https://github.com/nk3750/AppleHealthLLMBot)
```
