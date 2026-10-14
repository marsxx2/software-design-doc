#!/usr/bin/env bash
# Zip each skill folder into dist/<skill>.zip for upload to claude.ai.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
for d in skills/*/; do
  name=$(basename "$d")
  (cd skills && zip -rq "../dist/${name}.zip" "$name" -x '*/__pycache__/*' -x '*.DS_Store')
  echo "packaged dist/${name}.zip"
done
