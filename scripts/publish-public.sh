#!/usr/bin/env bash
set -euo pipefail

REPO_NAME="${1:-amlo-cybercrime-management-platform}"
OWNER="${2:-$(gh api user --jq .login)}"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required." >&2
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "Authenticate first with: gh auth login" >&2
  exit 1
fi

if gh repo view "$OWNER/$REPO_NAME" >/dev/null 2>&1; then
  echo "Repository already exists: $OWNER/$REPO_NAME"
else
  gh repo create "$OWNER/$REPO_NAME" --public --disable-wiki
fi

echo "Published: https://github.com/$OWNER/$REPO_NAME"
