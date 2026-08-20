#!/bin/sh
# directives-check-post-commit.sh -- fire `comp-directives check` at the REGISTER-TOUCH moment.
# LD-0433 (0.8.0_AE_CloudComp, 2026-08-20). The retirement mechanism's CHECK, wired per the house
# pattern (TRIGGER_LAYER doctrine: an available-but-never-fired check is not a control):
#   - post-commit surface: NON-BLOCKING by construction -- the commit is made; the check only
#     REPORTS. A violation prints LOUDLY (partition/conservation/form/freeze) so the very next
#     read of the terminal carries it; it never rewrites history or blocks closure.
#   - fires ONLY when the commit touched a register view (DIRECTIVES.yaml or
#     DIRECTIVES_RETIRED.yaml) -- never taxes an unrelated commit.
#   - directives-native: reads NOTHING from the missions machinery (the CTO 63580 fence).
_ws="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
[ -n "$_ws" ] || exit 0
_touched="$(git -C "$_ws" diff-tree --no-commit-id --name-only -r HEAD 2>/dev/null)"
case "$_touched" in
  *org/missions/DIRECTIVES.yaml*|*org/missions/DIRECTIVES_RETIRED.yaml*)
    echo "[directives-check] register touched by this commit -- running the retirement invariants:"
    python "$_ws/org/modules/graph/comp_directives.py" check || {
      echo "[directives-check] *** VIOLATION(S) ABOVE -- the register's partition/conservation/" \
           "form/freeze invariants do not hold at HEAD. Non-blocking by design; fix or route" \
           "to the register owner (0.0.0_AB_MSTR) NOW, not later. ***"
    }
    ;;
esac
exit 0
