#!/usr/bin/env bash
# ISCK gate runner -- runs EVERY declared gate against an ATOMIC extract of a cited commit.
# DT-R2-3: every gate reads files from disk, and a live working tree is not atomic -- a gate run
# during any seat's multi-file landing samples a torn state and fakes either colour. A COMMIT is
# atomic. This runner is the remedy: extract, run, stamp provenance.
#
# Usage: bash run_gates.sh <commit-ish>          (e.g. bash run_gates.sh 9fa5a91af5)
# Exit: 0 only if every FAILING-CLASS gate passes. Gate outputs stream through unchanged.
# COO-R2-1 (2.0.0_SA_COO~X 77035): the probes gate exits 0 on unadjudicated CANDIDATES by design,
# so a green summary can carry open items invisibly. The summary line therefore prints the
# candidate DENOMINATOR beside the colour -- a pass and an absence must not render identically.
set -u
COMMIT="${1:?usage: run_gates.sh <commit-ish>}"
ROOT="$(git rev-parse --show-toplevel)" || exit 2
FULL="$(git -C "$ROOT" rev-parse --verify "${COMMIT}^{commit}")" || { echo "ERROR: '$COMMIT' names no commit"; exit 2; }
TMP="$(mktemp -d)" || exit 2
trap 'rm -rf "$TMP"' EXIT
git -C "$ROOT" archive "$FULL" org/standards/isck | tar -x -C "$TMP" || { echo "ERROR: archive/extract failed"; exit 2; }
cd "$TMP/org/standards/isck" || exit 2
# R3-CRO-15: the extract is atomic but is NOT a git checkout, so the sidecar link resolver would read
# UNRESOLVED and suppress nothing (exit 1 | 32 open at ab052139a8). Hand the gate the TRUSTED repo
# root -- the resolver reads commits/blobs from its OBJECT DATABASE (git cat-file / git show <commit>:<path>),
# never from the working tree, so the pin cannot be contaminated by later tree bytes.
export ISCK_REPO_ROOT="$ROOT"

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
  elif [ "$gate" = "isck_coverage_probes.py" ]; then
    # tee the probe output so its candidate counts can be lifted onto the summary line
    python "$gate" | tee "$TMP/probes.out"; grc=${PIPESTATUS[0]}
  else
    python "$gate"; grc=$?
  fi
  echo "GATE $gate: exit $grc"
  [ "$grc" -ne 0 ] && RC=1
done
CAND="probe counts UNREAD"
if [ -s "$TMP/probes.out" ]; then
  a1=$(sed -n 's/^ *ARM 1 coverage gaps *: *\([0-9]*\).*/\1/p' "$TMP/probes.out" | tail -1)
  a3=$(sed -n 's/^ *ARM 3 unreachable values *: *[0-9]* *open (no repair): *\([0-9]*\).*/\1/p' "$TMP/probes.out" | tail -1)
  a4=$(sed -n 's/^ *ARM 4 require-only arms *: *\([0-9]*\).*/\1/p' "$TMP/probes.out" | tail -1)
  # ARM 4 consume gate (DT~X @9fb81b743a): the UNDISPOSED residual is what stays open --
  # "REQUIRE-ONLY: N (A adjudicated, D deferred, K NEW, R re-adjudication)" -> open = N - A
  a4adj=$(sed -n 's/^ *REQUIRE-ONLY: *[0-9]* *(\([0-9]*\) adjudicated.*/\1/p' "$TMP/probes.out" | tail -1)
  if [ -n "$a4" ] && [ -n "$a4adj" ]; then a4open=$((a4 - a4adj)); a4note="ARM4 $a4open of $a4 undisposed"; else a4open="$a4"; a4note="ARM4 $a4 (consume line UNREAD)"; fi
  # ARM 1 consume gate (DT~X @6286d725e8): same shape -- "GAPS: N (A adjudicated, D deferred, ...)" -> open = N - A;
  # a missing consume line renders UNREAD, never the raw count (COO~X, 20260828T025454Z item 4)
  a1adj=$(sed -n 's/^ *GAPS: *[0-9]* *(\([0-9]*\) adjudicated.*/\1/p' "$TMP/probes.out" | tail -1)
  if [ -n "$a1" ] && [ -n "$a1adj" ]; then a1open=$((a1 - a1adj)); a1note="ARM1 $a1open of $a1 undisposed"; else a1open="$a1"; a1note="ARM1 $a1 (consume line UNREAD)"; fi
  if [ -n "$a1" ] && [ -n "$a3" ] && [ -n "$a4" ]; then
    CAND="$((a1open + a3 + a4open)) open candidates ($a1note, ARM3 $a3, $a4note -- adjudication records, not colour, dispose them)"
  else
    CAND="probe counts UNPARSED (format drift -- read the gate output above)"
  fi
fi
echo "RUN_GATES: commit $FULL -> overall exit $RC | $CAND"
exit $RC
