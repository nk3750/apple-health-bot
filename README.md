<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">APPLEHEALTHLLMBOT</h1>

<p align="center">
    <em>Transforming health data with AI precision.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/nk3750/AppleHealthLLMBot?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/nk3750/AppleHealthLLMBot?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/nk3750/AppleHealthLLMBot?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/nk3750/AppleHealthLLMBot?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

AppleHealthLLMBot automates Apple Health data parsing and bot interactions. It transforms XML data into CSVs via `xmldataparser.py`, ensuring seamless data analysis. The `appleHealthBot.py` categorizes user queries for workouts, sleep, or exerciseTime, storing information in an SQL database. Leveraging AI tools like ChatOpenAI, the bot retrieves and presents data, enhancing user experience and data visualization capabilities. The projects streamlined workflow and data management cater to health enthusiasts seeking efficient health data processing and analysis.

---


##  Repository Structure

```sh
└── AppleHealthLLMBot/
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

##  Modules

<details closed><summary>.</summary>

| File                                                                                   | Summary                                                                                                                                                                                                         |
| ---                                                                                    | ---                                                                                                                                                                                                             |
| [entrypoint.sh](https://github.com/nk3750/AppleHealthLLMBot/blob/master/entrypoint.sh) | Executes XML data parsing and runs the Apple Health bot based on the container argument. Parses data using `xmldataparser.py` and the bot using `appleHealthBot.py` within the parent repositorys architecture. |
| [Dockerfile](https://github.com/nk3750/AppleHealthLLMBot/blob/master/Dockerfile)       | Defines Docker image setup for Python-based application, managing dependencies, and the entrypoint script for seamless container execution in the AppleHealthLLMBot repository.                                 |

</details>

<details closed><summary>setup</summary>

| File                                                                                               | Summary                                                                                                                                                                                          |
| ---                                                                                                | ---                                                                                                                                                                                              |
| [requirements.txt](https://github.com/nk3750/AppleHealthLLMBot/blob/master/setup/requirements.txt) | Lists essential dependencies for the project such as langchain, pandas, and sqlalchemy.-Ensures crucial libraries are available for data parsing, language processing, and database interaction. |

</details>

<details closed><summary>healthBot</summary>

| File                                                                                                     | Summary                                                                                                                                                                                                                                    |
| ---                                                                                                      | ---                                                                                                                                                                                                                                        |
| [appleHealthBot.py](https://github.com/nk3750/AppleHealthLLMBot/blob/master/healthBot/appleHealthBot.py) | Classifies user queries into workouts, sleep, or exerciseTime categories and loads data to an SQL database based on the category. Interacts with the database, queries relevant data, and provides answers using AI tools like ChatOpenAI. |

</details>

<details closed><summary>dataParser</summary>

| File                                                                                                    | Summary                                                                                                                                                                                                                                                                   |
| ---                                                                                                     | ---                                                                                                                                                                                                                                                                       |
| [xmldataparser.py](https://github.com/nk3750/AppleHealthLLMBot/blob/master/dataParser/xmldataparser.py) | Converts Apple Health XML data into structured CSVs by parsing workouts, exercise times, and sleep records. Facilitates analysis and visualization through separate CSV outputs for each data type. Automates the process via CLI input for seamless data transformation. |

</details>

---

##  Getting Started

**System Requirements:**

* **Docker**: `latest version`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the AppleHealthLLMBot repository:
>
> ```console
> $ git clone https://github.com/nk3750/AppleHealthLLMBot
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd AppleHealthLLMBot
> ```
>
> 3. Copy over the export.xml file from the health app and put it inside the project directory.
> ```console
> $ cp /path/to/export.xml .
> ```

### Setup
<h4>From <code>AppleHealthLLMBot</code></h4>
> Add your openAI API key to the .env file
> ```console
> $ vim .env
> ```
 <h4>Create Docker Image</h4>
> Let's first create the docker image
> ```console
> $ docker build -t healthbot .
> ```
###  Usage

<h4>From <code>AppleHealthLLMBot</code></h4>



<h4>Parse the xml and create csv files</h4>
> ```console
> $ docker run -v "$(pwd)":/data healthbot parseData /data/export.xml
> ```
<h4>Start the bot</h4>
> ```console
> $  docker run -it -v "$(pwd)":/data healthbot healthBot
> ```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/nk3750/AppleHealthLLMBot/issues)**: Submit bugs found or log feature requests for the `AppleHealthLLMBot` project.
- **[Submit Pull Requests](https://github.com/nk3750/AppleHealthLLMBot/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/nk3750/AppleHealthLLMBot/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/nk3750/AppleHealthLLMBot
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/nk3750/AppleHealthLLMBot/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=nk3750/AppleHealthLLMBot">
   </a>
</p>
</details>

---

##  License

This project is protected under the MIT License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- 

[**Return**](#-overview)

---
