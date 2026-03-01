# telegram-repost-restriction

A small Telegram bot/service to detect and restrict repeated reposts in a chat or channel.

> NOTE: This README is intentionally generic — I don't have details about how this repository implements the feature. It provides installation, configuration, and usage guidance you can adapt. If you want the README tailored to specific files or commands in this repository, tell me and I can inspect the repo and update the README.

## Features

- Detect repeated reposts (duplicate media/links/text) in a chat
- Restrict or delete repeated reposts automatically
- Configurable threshold and enforcement behavior

## Requirements

- Python 3.9+ (or adjust per project)
- A Telegram bot token (from @BotFather)
- Optional: a Redis/Mongo/SQLite database if the bot persists state

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ImpostorBoy228/telegram-repost-restriction.git
cd telegram-repost-restriction
```

2. (Recommended) Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

If the repository uses Poetry or Pipenv, use those tools instead.

## Configuration

Create a `.env` file in the project root (or use environment variables). Example variables:

```env
# Telegram bot token from @BotFather
TELEGRAM_BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11

# Enforcement settings
REPOST_THRESHOLD=3        # number of duplicates to consider as spam
REPOST_WINDOW_SECONDS=3600
ENFORCEMENT_ACTION=restrict  # or delete, warn, mute

# Optional persistence
DATABASE_URL=sqlite:///./data.db
# or redis://localhost:6379/0
```

Adjust names to match the actual config keys used by the code.

## Running

If the project provides an entry point (e.g., `bot.py`, `main.py`, or a module), run it like:

```bash
python bot.py
```

Or, if it uses a task runner or Docker:

```bash
docker build -t telegram-repost-restriction .
docker run --env-file .env telegram-repost-restriction
```

## Usage

- Add the bot to a group or channel and grant the necessary permissions (read messages, delete messages, restrict members) depending on enforcement actions.
- Adjust thresholds and window sizes in the config to tune sensitivity.

## Contributing

Contributions welcome. Please open an issue or pull request with a clear description of the change.

Consider adding:
- Tests for detection logic
- Configuration examples
- A sample docker-compose setup for persistence (Redis/Postgres)

## Troubleshooting

- If the bot doesn't respond, check `TELEGRAM_BOT_TOKEN` and bot permissions.
- If duplicates are not detected, verify media hashing or content normalization logic.

## License

This repository currently has no license file. If you want this project to be open source, consider adding a `LICENSE` (for example, MIT).

---

If you'd like, I can:
- Inspect the repository and adapt this README to match actual filenames, commands, and configuration keys (I can look for `bot.py`, `requirements.txt`, config files, or a Dockerfile).
- Add a LICENSE file or example `.env.example`.

Tell me which you'd like and I'll update the repo accordingly.