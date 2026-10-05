#!/usr/bin/env bash
set -euo pipefail

REPO_NAME="${1:-amlo-cybercrime-management-platform}"
OWNER="${2:-$(gh api user --jq .login)}"

gh repo edit "$OWNER/$REPO_NAME" --visibility private --accept-visibility-change-consequences

echo "Repository visibility changed to private: https://github.com/$OWNER/$REPO_NAME"
echo "Previously public content may still exist in clones, forks, caches, or screenshots."
