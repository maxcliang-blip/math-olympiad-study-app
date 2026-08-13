#!/usr/bin/env bash
# Fast deploy for amc10tooly math app.
# The hub /math/ proxies to a local Node server (PM2: amc10tooly) serving from this dir,
# so git push + PM2 reload = live instantly (no 40s GH Pages wait).
# Usage: ./deploy.sh [commit message]

set -euo pipefail

REPO_DIR="/home/opc/amc10tooly"
cd "$REPO_DIR"

if ! git diff --quiet || ! git diff --cached --quiet; then
    msg="${1:-auto deploy $(date '+%Y-%m-%d %H:%M')}"
    git add -A
    git commit -q -m "$msg"
    git push -q
    echo "✓ git push done"
else
    echo "ℹ no git changes to commit"
fi

# Reload the live server (PM2) so the running process picks up the new file
if command -v pm2 >/dev/null 2>&1; then
    pm2 restart amc10tooly >/dev/null 2>&1
    echo "✓ PM2 reloaded (hub /math/ live immediately)"
else
    echo "⚠ pm2 not found — restart the server manually"
fi

# Sanity: confirm the server is serving fresh HTML (no-cache headers)
sleep 1
echo "✓ verify: $(curl -sI https://hub.laxmiang.work.gd/math/ | grep -i 'cache-control')"