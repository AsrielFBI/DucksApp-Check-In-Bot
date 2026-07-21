# DucksApp-Check-In-Bot

An unofficial DucksApp automation project created while learning about REST APIs, application communication and reverse engineering.

This repository explores how to interact with DucksApp's REST API in a non-hostile way. The goal is educational: understanding how applications communicate and building a clean automation workflow.

Inspired by projects like AminoPy that encouraged me to explore API reverse engineering.


## ⚠️ Legal Notice

This is an **unofficial, community-maintained project** and is not affiliated with DucksApp.

Automated accounts or bots may violate DucksApp's Terms of Service. Using this software may result in account suspension or bans.

**Use at your own risk.**

</div>

## Features

- 🔍 **Automatic Discovery**
  - Finds the configured community
  - Checks membership
  - Retrieves community information

- ⚡ **Automated Check-In**
  - Logs in
  - Runs discovery
  - Checks current status
  - Performs check-in when available
  - Saves execution results

- 🏗️ **Modular Architecture**
  - Shared API client
  - Centralized configuration
  - Separate discovery and activity modules

---

## Installation

Requirements:

- Python 3.11+

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your configuration:

```bash
cp .env.example bot/.env
```

Edit `bot/.env` with your credentials:

```env
DUCK_BASE_URL=https://api.duckapps.com.br
DUCK_EMAIL=
DUCK_PASSWORD=
DUCK_ANON_KEY=
DUCK_COMMUNITY_ENDPOINT=
```

INFO: The ANON key is located inside the xapk, its used to authenticate the app itself towards the REST API, you can either search for one yourself inside the xapk with jadx, or contact me on discord so I can share you mine.
My discord is linked in my BIO

---

## Usage

Run from the repository root:

```bash
python -m bot.main
```

The bot will automatically execute the full workflow.

---

## Output

Generated files:

```
bot/data/

├── discovery_result.json
└── activity_result.json
```

These contain information collected during discovery and the result of the activity execution.

---

## Roadmap

- [ ] Multiple community support
- [ ] Scheduling
- [ ] Better CLI interface
- [ ] Automated tests
- [ ] More API exploration

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/AsrielFBI/DucksApp-Check-In-Bot/blob/main/LICENSE) file for details.

---
