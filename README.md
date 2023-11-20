# tg-sticker-cauldron

[![Python 3.10](https://img.shields.io/badge/python-3.10-yellow.svg)](https://www.python.org/downloads/release/python-3106/)

## Telegram stickers

https://core.telegram.org/stickers

## Goal
Easily generate telegram stickers by:
- Convert any files to a format compatible to telegram sticker.
- Generate a sticker pack from a directory of images.

## Run
1. Install ffmpeg (If you're a mac, simply run `brew install ffmpeg`)
2. Place your video in `src/input` directory. 
3. Install python requirements, and run

```shell
python3 src/main.py
```

## Status
The project is **not ready for production use**.
It currently only supports video Stickers.

### TODO
1. Add support for animated, static stickers
2. dockerize