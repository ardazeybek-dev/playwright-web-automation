# CLAUDE.md

This file guides Claude Code (claude.ai/code) when working in this repository.

## Project

A web automation bot written in Python + Playwright. `proje.py` navigates to a target site, reads its
title, and takes a full-page screenshot. A single-file script with minimal dependencies.

## Running

- Docker: `docker-compose up --build`
- Local: `pip install -r requirements.txt && playwright install chromium && python proje.py`

## Rules

- The bot runs **headless**; it prints the title to stdout and saves the output to `OUTPUT_PATH`.
- The target URL and output path are read from environment variables (`TARGET_URL`, `OUTPUT_PATH`); never hard-code them.
- This is a script, not a web service — it is not deployed to static hosting (ShipStatic, etc.).
- Console output is forced to UTF-8 so emoji/Turkish characters do not break on the Windows console.
