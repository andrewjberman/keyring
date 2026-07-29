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

  # =========================================================================
  # VIEW-TIME COMPILE (Andrew-direct 2026-07-29). THIS HOOK NO LONGER WRITES
  # ANY TRACKED FILE. It records that a refresh is DUE; the compile happens
  # when someone LOOKS.
  #
  # WHY (measured, not theorized): `emit` and `compile` wrote org/missions/
  # execsum.yaml + commits.jsonl + MISSIONS.md -- ALL TRACKED. The churn was
  # three lines per sub-group (anchor_commit / anchor_time / anchor_author, a
  # pointer to the latest attributed commit), so EVERY commit by ANY agent
  # re-dirtied the register. In a SHARED WORKTREE a dirty tracked file blocks
  # `git pull` for everyone -- it blocked 0.2.0_DT_PortfolioAnalytics twice
  # during an MDPF P0, and it re-dirtied itself within seconds of the very
  # commit that cleaned it, because that commit is itself a new anchor.
  #
  # The defect was storing a VOLATILE DERIVED VALUE in version control. A
  # register whose job is to be TRUE cannot cost a commit every time the
  # repository moves. Auto-committing or auto-pushing it was considered and
  # REJECTED: a pre-push hook that commits creates the commit AFTER git has
  # computed the refs to push, so it never ships and the tree stays ahead --
  # and the commit re-fires this hook. That chases the symptom; this removes
  # the source.
  #
  # CONSEQUENCE, ACCEPTED DELIBERATELY: org/missions/ is now STALE-BY-DESIGN
  # between compiles. That is safe ONLY because the board carries its own
  # anchor commit, so staleness is VISIBLE rather than silent -- a reader can
  # always see which commit the view was built from. Refresh with:
  #     .tools/comp-missions emit && .tools/comp-missions compile
  # =========================================================================
  python - <<'PYEOF' >/dev/null 2>&1 || exit 0
import io, json, os, subprocess
wm = os.path.join('.comp-graph', 'missions-refresh-due.json')
os.makedirs('.comp-graph', exist_ok=True)
head = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
io.open(wm, 'w', encoding='utf-8').write(json.dumps({
    'refresh_due_at_head': head,
    'note': 'org/missions/ is DERIVED and compiled at VIEW time. Run '
            '.tools/comp-missions emit && .tools/comp-missions compile to refresh. '
            'This file is gitignored; the hook writes nothing tracked.',
}, indent=2))
PYEOF
) >/dev/null 2>&1 &

exit 0
