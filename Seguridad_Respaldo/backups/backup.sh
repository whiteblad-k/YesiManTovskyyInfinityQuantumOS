#!/usr/bin/env bash
# Simple encrypted backup placeholder — adjust to your environment
VENV_PATH=".venv"
TARGET_DIR="backups/$(date +%F)"
mkdir -p "$TARGET_DIR"
# Example: tar + gpg (requires configuration)
tar -czf - ./ | gpg --symmetric --cipher-algo AES256 -o "$TARGET_DIR/backup-$(date +%F).gpg"
echo "Backup saved to $TARGET_DIR"