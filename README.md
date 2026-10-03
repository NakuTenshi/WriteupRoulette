# WriteupRoulette

🌐 فارسی: [README_fa.md](README_fa.md)

A simple terminal tool for bug bounty hunters who want to build a consistent writeup-reading habit.

Instead of wasting time deciding what to read next, WriteupRoulette randomly selects a bug bounty writeup from a curated collection and keeps track of what you've already read.

## Features

* Random writeup selection
* Track completed writeups
* Prevent already-read writeups from being selected again
* Remove unwanted writeups from the pool
* Lightweight and dependency-free
* Local file-based storage
* Simple installation and usage

## Data Sources

Writeup links are collected from the following repositories:

* [Awesome Bug Bounty Writeups](https://github.com/devanshbatham/Awesome-Bugbounty-Writeups?utm_source=chatgpt.com)
* [bb-resouces](https://github.com/Voorivex/bb-resouces?utm_source=chatgpt.com)

All credit for the writeup collections belongs to their respective maintainers and contributors.

## Installation

Clone the repository:

```bash
git clone https://github.com/NakuTenshi/WriteupRoulette.git
cd WriteupRoulette
```

Run the installer:

```bash
chmod +x install.sh
./install.sh
```

Then run it with 
```bash
writeuproulette
```

Or run directly from source:

```bash
python3 writeuproulette.py
```

## Usage

When started, the tool randomly selects a writeup and displays a small interactive menu:

```text
[1] Mark As Readed
[2] Choice Another One
[3] Remove It from List
[exit] or [quit]
```

### Mark As Readed

Moves the selected writeup from:

```text
not_readed_writeups.txt
```

to:

```text
readed_writeups.txt
```

The writeup will no longer appear in future random selections.

### Choice Another One

Randomly selects another unread writeup.

### Remove It from List

Removes the writeup from the unread pool without marking it as read.

Useful for:

* Broken links
* Duplicate entries
* Writeups you are not interested in

## Storage

When running directly from source:

```text
./writeups/
```

When installed:

```text
~/.local/share/writeups/
```

Files used by the application:

```text
not_readed_writeups.txt
readed_writeups.txt
```

## Project Structure

```text
.
├── install.sh
├── README.md
├── README_FA.md
├── writeuproulette.py
└── writeups
    └── not_readed_writeups.txt
```
# WriteupRoulette
