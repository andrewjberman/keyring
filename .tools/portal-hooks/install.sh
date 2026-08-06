#!/bin/bash
# Install portal git hooks. Run once per session from workspace root.
# Usage: bash .tools/portal-hooks/install.sh

PORTAL_DIR="$(git rev-parse --show-toplevel)/portal"
HOOK_DIR="$PORTAL_DIR/.git/hooks"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ ! -d "$HOOK_DIR" ]; then
  echo "ERROR: $HOOK_DIR not found -- is portal submodule initialized?"
  exit 1
fi

install_hook() {
  local name="$1"
  local src="$SCRIPT_DIR/$name"
  local dst="$HOOK_DIR/$name"
  if [ ! -f "$src" ]; then
    echo "SKIP: $src not found"
    return
  fi
  cp "$src" "$dst"
  chmod +x "$dst"
  echo "OK: installed $name -> $dst"
}

install_hook pre-push
# pre-commit hook REMOVED 2026-08-06 -- it existed solely to run comp-surface-check, which is
# RETIRED (Andrew-direct). Installing a hook that calls a deleted binary would WARN-and-SKIP
# on every portal commit -- noise that reads like a degraded gate rather than an absent one.
install_hook commit-msg   # SURFACE_ACK auto-append (CTO gate 2026-08-04): one authoring act feeds the audit log AND the CI-parseable message line

echo "OK: portal hooks installed"
