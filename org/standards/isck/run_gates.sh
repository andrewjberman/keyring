#!/usr/bin/env bash
# ISCK gate runner -- runs EVERY declared gate against an ATOMIC extract of a cited commit.
# DT-R2-3: every gate reads files from disk, and a live working tree is not atomic -- a gate run
# during any seat's multi-file landing samples a torn state and fakes either colour. A COMMIT is
# atomic. This runner is the remedy: extract, run, stamp provenance.
#
# Usage: bash run_gates.sh <commit-ish>          (e.g. bash run_gates.sh 9fa5a91af5)
# Exit: 0 only if every FAILING-CLASS gate passes. Gate outputs stream through unchanged.
set -u
COMMIT="${1:?usage: run_gates.sh <commit-ish>}"
ROOT="$(git rev-parse --show-toplevel)" || exit 2
FULL="$(git -C "$ROOT" rev-parse --verify "${COMMIT}^{commit}")" || { echo "ERROR: '$COMMIT' names no commit"; exit 2; }
TMP="$(mktemp -d)" || exit 2
trap 'rm -rf "$TMP"' EXIT
git -C "$ROOT" archive "$FULL" org/standards/isck | tar -x -C "$TMP" || { echo "ERROR: archive/extract failed"; exit 2; }
cd "$TMP/org/standards/isck" || exit 2

echo "PROVENANCE: gates running against ATOMIC extract of $FULL"
echo "            (working-tree state is irrelevant to every number below)"
RC=0
for gate in validate_isck.py check_rule_ablation.py check_enum_collisions.py \
            check_mutant_isolation.py check_postulate_labels.py isck_coverage_probes.py; do
  if [ ! -f "$gate" ]; then
    echo "GATE $gate: ABSENT AT THIS COMMIT (counts as FAIL -- the package declares it)"
    RC=1
    continue
  fi
  echo "---- $gate ----"
  if [ "$gate" = "validate_isck.py" ]; then
    python "$gate" --self-test; grc=$?
  else
    python "$gate"; grc=$?
  fi
  echo "GATE $gate: exit $grc"
  [ "$grc" -ne 0 ] && RC=1
done
echo "RUN_GATES: commit $FULL -> overall exit $RC"
exit $RC
