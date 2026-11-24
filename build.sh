#!/usr/bin/env bash
# Build paper/paper.pdf from paper/paper.md.
# Tries pandoc + tectonic (LaTeX); falls back to pandoc HTML + headless Chrome.
set -euo pipefail
cd "$(dirname "$0")/paper"
if pandoc paper.md --citeproc --pdf-engine=tectonic --pdf-engine-opt=--only-cached \
     -V geometry:margin=1in -V fontsize=11pt -V linkcolor=blue -V urlcolor=blue \
     --resource-path=. -o paper.pdf 2>build.log; then
  echo "built paper.pdf with tectonic"; exit 0
fi
echo "tectonic failed (see paper/build.log); falling back to HTML + Chrome" >&2
pandoc paper.md --citeproc --standalone --mathml --embed-resources \
  --css=paper.css --resource-path=. -o paper.html
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$PWD/paper.pdf" "file://$PWD/paper.html"
echo "built paper.pdf with Chrome"
