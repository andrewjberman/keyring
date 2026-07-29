#!/usr/bin/env bash
# missions-refresh-post-commit.sh -- keep org/missions/ current WITHOUT anyone running a tool.
#
# Andrew-direct 2026-07-28: "most of this process needs some kind of githook or function that keeps
# it updated so we dont fall into traps of finding it stale and having to initiate some tool call."
#
# THREE PROPERTIES, EACH LOAD-BEARING. Do not relax one without re-reading why it is here.
#
#   1. IT NEVER STAGES.  org/missions/** is an MSTR-only lane. A hook that staged into another
#      agent's commit would trip the owned-paths gate on EVERY non-MSTR commit and halt the fabric.
#      It updates the WORKING TREE only; MSTR commits the accumulation on its own cadence. The
#      owned-paths gate then also protects the tree: a non-MSTR agent who tries to sweep these files
#      into their own commit is BLOCKED, so the dirty tree is safe by construction.
#
#   2. IT NEVER BLOCKS.  post-commit cannot fail a commit, and this exits 0 unconditionally anyway.
#      A register-freshness hook that could stop the fabric committing would be a far worse defect
#      than a stale register.
#
#   3. IT NEVER RUNS THE EXPENSIVE PATH.  A FULL rebuild (forced when the attribution rules change)
#      scans ~20k commits. That must NOT fire inside someone's commit. If the config fingerprint has
#      moved, the hook SAYS SO and stops, leaving the deliberate rebuild to a human/MSTR run. A hook
#      that silently does 20 seconds of work on a teammate's commit is how hooks get deleted.
#
# It also backgrounds itself, so it adds ~0ms of perceived latency to the commit.

REPO="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
[ -n "$REPO" ] || exit 0
[ -f "$REPO/.tools/comp_missions.py" ] || exit 0
[ -f "$REPO/org/tier0/missions.yaml" ] || exit 0

# Opt-out for bulk/scripted work: MISSIONS_REFRESH=0 git commit ...
[ "${MISSIONS_REFRESH:-1}" = "0" ] && exit 0

WM="$REPO/.comp-graph/missions-watermark.json"
OWNER_FILE="$REPO/org/missions/.register-owner"

# MULTI-DEVICE GUARD. org/missions/ is DERIVED; if two devices compile and commit it, the later push
# overwrites the earlier with a view built from a different git state and the losing rows vanish
# with no error. Exactly one device owns it. A non-owner SKIPS SILENTLY -- no warning, because a
# hook that complains on every commit of a correctly-configured second device is a hook that gets
# deleted.
if [ -f "$OWNER_FILE" ]; then
  _owner="$(sed -n 's/^owner_hostname:[[:space:]]*//p' "$OWNER_FILE" | head -1 | tr -d '\r')"
  _host="$(hostname 2>/dev/null)"
  if [ -n "$_owner" ] && [ -n "$_host" ] && [ "$_owner" != "$_host" ]; then
    exit 0
  fi
fi

(
  cd "$REPO" || exit 0

  # Cheap guard: if the attribution rules moved, a FULL rebuild is required. Announce, do not do it.
  if [ -f "$WM" ]; then
    CUR="$(python -c "
import sys
sys.path.insert(0, '.tools')
try:
    import comp_missions as cm
    print(cm.config_fingerprint(cm.load_index()))
except Exception:
    print('')
" 2>/dev/null)"
    OLD="$(python -c "
import json
try:
    print(json.load(open(r'$WM')).get('config_fingerprint',''))
except Exception:
    print('')
" 2>/dev/null)"
    if [ -n "$CUR" ] && [ -n "$OLD" ] && [ "$CUR" != "$OLD" ]; then
      echo "[missions] attribution rules CHANGED ($OLD -> $CUR)." >&2
      echo "[missions] a FULL rebuild is required and is NOT run from a hook." >&2
      echo "[missions] run: .tools/comp-missions emit && .tools/comp-missions compile" >&2
      exit 0
    fi
  fi

  python .tools/comp_missions.py emit    >/dev/null 2>&1 || exit 0
  python .tools/comp_missions.py compile >/dev/null 2>&1 || exit 0
) >/dev/null 2>&1 &

exit 0
