#!/bin/bash
# MDPF_SECCLASS item 4 (E_18's scheduled trigger), 1.0.0_SA_CTO rulings batch 68.
# Grades data/black_diamond/scripts/gold/gold_dispatch.sh at the CANDIDATE bytes against the
# DEPLOYED bytes (repo commit 606263dd22 = s3://opal-data-bd/code/gold/gold_dispatch.sh).
#
#   1. the candidate parses (bash -n)
#   2. the freshness gate with the switch UNSET prints byte-for-byte what the deployed bytes
#      print and returns the same code, over four cases; with the switch SET it runs the guard
#   3. E_18 is in the catalog and in the canonical chain between B_01b and B_02, and has its
#      own phase in the parallel dispatcher between PHASE_B3 and PHASE_B4
#   4. run_script: E_18 exiting non-zero returns 0 with a WARN line; any other id keeps its code
#   5. run_script under --dry-run: E_18 gets no flag, every other id gets --dry-run
#
# Usage: bash test_gold_dispatch_e18_slot.sh [candidate file]   (default: the repo file at the
# worktree this test sits in). Exit 0 = all pass. No AWS call, no network: aws and python3 are
# stubs on PATH.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(git -C "$HERE" rev-parse --show-toplevel)"
REL="data/black_diamond/scripts/gold/gold_dispatch.sh"
CAND="${1:-$ROOT/$REL}"
DEPLOYED_PIN="606263dd22"
T="$(mktemp -d)"
trap 'rm -rf "$T"' EXIT
fails=0
pass() { echo "PASS: $1"; }
fail() { echo "FAIL: $1"; fails=$((fails + 1)); }

git -C "$ROOT" show "$DEPLOYED_PIN:$REL" > "$T/deployed.sh" || { echo "FAIL: cannot read $DEPLOYED_PIN:$REL"; exit 1; }
[ -s "$T/deployed.sh" ] || { echo "FAIL: deployed bytes empty"; exit 1; }
REALPY="$(command -v python || command -v python3)"

# ---- 1. parse ---------------------------------------------------------------------------
if bash -n "$CAND"; then pass "1 candidate parses (bash -n)"; else fail "1 candidate does not parse"; fi

# ---- 2. freshness gate ------------------------------------------------------------------
fn() { sed -n "/^$2() {/,/^}/p" "$1"; }   # one top-level function's text
mkdir -p "$T/gate/bin" "$T/gate/scripts_absent/lib" "$T/gate/scripts_present/lib"
cat > "$T/gate/bin/aws" <<'EOF'
#!/bin/bash
# stub: `aws s3 ls <silver>` prints listing lines; `aws s3 cp <header> -` prints the header JSON
if [ "$2" = "ls" ]; then
    [ -n "$STUB_SILVER" ] && printf '2026-10-01 04:00:00   1234 %s.parquet\n' $STUB_SILVER
    exit 0
fi
if [ "$2" = "cp" ]; then
    [ -n "$STUB_GOLD" ] && printf '{"data_as_of": "%s"}\n' "$STUB_GOLD"
    exit 0
fi
exit 0
EOF
printf '#!/bin/bash\nexec "%s" "$@"\n' "$REALPY" > "$T/gate/bin/python3"
chmod +x "$T/gate/bin/aws" "$T/gate/bin/python3"
cat > "$T/gate/scripts_present/lib/trading_calendar.py" <<'EOF'
import datetime as dt
def expected_last_trading_day(now):
    return dt.date(2026, 9, 29)
EOF

gate() {  # gate <file> <scripts dir> <silver keys> <gold as-of> [switch]
    local src="$1" scripts="$2" silver="$3" gold="$4" sw="${5:-}"
    {
        echo 'BD_S3_BUCKET=stub-bucket'
        echo "SCRIPTS=\"$scripts\""
        fn "$src" _expected_last_trading_day
        fn "$src" check_freshness
        echo 'check_freshness; echo "RC=$?"'
    } > "$T/gate/run.sh"
    if [ -n "$sw" ]; then
        PATH="$T/gate/bin:$PATH" STUB_SILVER="$silver" STUB_GOLD="$gold" GOLD_CALGUARD_ENABLE="$sw" bash "$T/gate/run.sh" 2>&1
    else
        ( unset GOLD_CALGUARD_ENABLE; PATH="$T/gate/bin:$PATH" STUB_SILVER="$silver" STUB_GOLD="$gold" bash "$T/gate/run.sh" 2>&1 )
    fi
}

n=0
while IFS='|' read -r label silver gold want; do
    n=$((n + 1))
    gate "$T/deployed.sh" "$T/gate/scripts_absent" "$silver" "$gold" > "$T/gate/dep.out"
    gate "$CAND" "$T/gate/scripts_absent" "$silver" "$gold" > "$T/gate/cand.out"
    gate "$CAND" "$T/gate/scripts_present" "$silver" "$gold" > "$T/gate/cand_mod.out"   # module landed, switch still unset
    if ! grep -q "^RC=$want\$" "$T/gate/dep.out"; then fail "2.$n control ($label): deployed bytes returned $(grep '^RC=' "$T/gate/dep.out"), wanted RC=$want"; continue; fi
    if diff -q "$T/gate/dep.out" "$T/gate/cand.out" > /dev/null && diff -q "$T/gate/dep.out" "$T/gate/cand_mod.out" > /dev/null; then
        pass "2.$n switch unset, $label: output and RC=$want identical to the deployed bytes (module absent and module present)"
    else
        fail "2.$n switch unset, $label: output differs from the deployed bytes"; diff "$T/gate/dep.out" "$T/gate/cand.out"; diff "$T/gate/dep.out" "$T/gate/cand_mod.out"
    fi
done <<'CASES'
silver newer than gold|2026-09-29 2026-09-30|2026-09-29|0
silver equal to gold|2026-09-29 2026-09-30|2026-09-30|1
no silver listing||2026-09-30|0
no gold header|2026-09-30||0
CASES
if grep -q "CALGUARD" "$T/gate/cand.out" "$T/gate/cand_mod.out"; then fail "2.5 a CALGUARD line printed with the switch unset"; else pass "2.5 no CALGUARD line with the switch unset"; fi

# switch SET: the guard runs (the difference control for the switch)
gate "$CAND" "$T/gate/scripts_absent" "2026-09-29 2026-09-30" "2026-09-29" 1 > "$T/gate/on_absent.out"
if grep -q "WARN: CALGUARD-UNAVAILABLE" "$T/gate/on_absent.out" && grep -q "^RC=0$" "$T/gate/on_absent.out"; then
    pass "2.6 switch set, module absent: fails open (CALGUARD-UNAVAILABLE, RC=0)"
else fail "2.6 switch set, module absent"; cat "$T/gate/on_absent.out"; fi
gate "$CAND" "$T/gate/scripts_present" "2026-09-29 2026-09-30" "2026-09-29" 1 > "$T/gate/on_present.out"
if grep -q "clamped to 2026-09-29" "$T/gate/on_present.out" && grep -q "^RC=1$" "$T/gate/on_present.out" \
   && grep -q "Silver effective (calendar-clamped): 2026-09-29" "$T/gate/on_present.out"; then
    pass "2.7 switch set, module present: clamps 09-30 to 09-29 and turns proceed into skip (RC=1) -- the arm the switch keeps off"
else fail "2.7 switch set, module present"; cat "$T/gate/on_present.out"; fi

# ---- 3. catalog, chain, phase --------------------------------------------------------------
if grep -q '^E_18|E_18.detect_new_securities.py|--upload$' "$CAND"; then pass "3.1 catalog line E_18"; else fail "3.1 catalog line E_18"; fi
if grep -q '^CHAIN_CANONICAL="B_00 B_01 B_01b E_18 B_02 B_03 C_00 C_01 C_02 C_04"$' "$CAND"; then pass "3.2 canonical chain: E_18 between B_01b and B_02"; else fail "3.2 canonical chain"; fi
phases="$(grep -o -- '--- PHASE_[A-Z0-9a-z]*: [^-]* ---' "$CAND" | tr '\n' ';')"
case "$phases" in
    *"--- PHASE_B3: B_01b ---;--- PHASE_B3b: E_18 ---;--- PHASE_B4: B_02 ---;"*) pass "3.3 parallel dispatcher: PHASE_B3b E_18 between PHASE_B3 and PHASE_B4" ;;
    *) fail "3.3 parallel phase order: $phases" ;;
esac
dep_phases="$(grep -o -- '--- PHASE_[A-Z0-9a-z]*: [^-]* ---' "$T/deployed.sh" | tr '\n' ';')"
if [ "${phases/--- PHASE_B3b: E_18 ---;/}" = "$dep_phases" ]; then pass "3.4 every other phase is unchanged from the deployed bytes"; else fail "3.4 other phases changed"; fi
if grep -q '^NONFATAL_IDS="E_18"$' "$CAND"; then pass "3.5 NONFATAL_IDS is exactly E_18"; else fail "3.5 NONFATAL_IDS"; fi

# ---- 4 and 5. run_script ------------------------------------------------------------------
mkdir -p "$T/rs/bin"
cat > "$T/rs/bin/python3" <<'EOF'
#!/bin/bash
# stub for the telemetry-wrapped script call: record argv, exit STUB_RC
echo "$*" >> "$STUB_ARGV_LOG"
exit "${STUB_RC:-0}"
EOF
chmod +x "$T/rs/bin/python3"
rs() {  # rs <id> <stub rc> <dry run 0|1>
    {
        echo 'set -e'
        sed -n "/^read -r -d '' CATALOG/,/^CATALOG_END/p" "$CAND"
        grep '^NONFATAL_IDS=' "$CAND"
        echo 'SCRIPTS=/stub; BD_S3_BUCKET=stub; WORKERS=4; CHAIN_LABEL=test; FULL_REBUILD=0'
        echo "DRY_RUN=$3"
        echo 'log_ts() { echo TS; }; _checkpoint_done() { return 1; }; _checkpoint_write() { echo "  CHECKPOINT $1"; }'
        fn "$CAND" run_script
        echo "run_script $1 \"\" && echo RETURNED=0 || echo RETURNED=\$?"
    } > "$T/rs/run.sh"
    : > "$T/rs/argv.log"
    PATH="$T/rs/bin:$PATH" STUB_RC="$2" STUB_ARGV_LOG="$T/rs/argv.log" bash "$T/rs/run.sh" 2>&1
}
out="$(rs E_18 2 0)"
if echo "$out" | grep -q "E_18 done (rc=2)" && echo "$out" | grep -q "WARN: E_18 exited 2 -- NON-FATAL step, the chain continues." && echo "$out" | grep -q "^RETURNED=0$" && ! echo "$out" | grep -q "CHECKPOINT"; then
    pass "4.1 E_18 exits 2: rc printed, WARN line, run_script returns 0, no checkpoint"
else fail "4.1 E_18 non-fatal"; echo "$out"; fi
out="$(rs B_02 2 0)"
if echo "$out" | grep -q "B_02 done (rc=2)" && echo "$out" | grep -q "^RETURNED=2$" && ! echo "$out" | grep -q "NON-FATAL"; then
    pass "4.2 control: B_02 exits 2 -> run_script returns 2 (still fatal)"
else fail "4.2 control B_02"; echo "$out"; fi
out="$(rs E_18 0 0)"
if echo "$out" | grep -q "E_18 done (rc=0)" && echo "$out" | grep -q "CHECKPOINT E_18" && ! echo "$out" | grep -q "WARN" && grep -q "/stub/E_18.detect_new_securities.py --upload$" "$T/rs/argv.log"; then
    pass "4.3 E_18 exits 0: checkpoint written, no WARN, called with --upload"
else fail "4.3 E_18 success"; echo "$out"; cat "$T/rs/argv.log"; fi
out="$(rs E_18 0 1)"
if grep -q "/stub/E_18.detect_new_securities.py *$" "$T/rs/argv.log" && ! grep -q -- "--dry-run\|--upload" "$T/rs/argv.log"; then
    pass "5.1 --dry-run: E_18 is called with no flag (its own dry run)"
else fail "5.1 E_18 dry-run flags"; cat "$T/rs/argv.log"; fi
out="$(rs B_01 0 1)"
if grep -q "/stub/B_01.holdings_lots.py --dry-run$" "$T/rs/argv.log"; then pass "5.2 control: --dry-run still turns B_01's --upload into --dry-run"; else fail "5.2 control B_01 dry-run"; cat "$T/rs/argv.log"; fi

echo "RESULT: $fails failure(s)"
[ "$fails" = "0" ]
