#!/usr/bin/env bash
# W25 / S218 STEP 2 -- THE DISCRIMINATING READ. ONE body, one login, one K4, one K5, no retry.
#
#   bash w25_s218_read.sh --plan          # print exactly what would run; no login, no POST
#   EPOCH=<epoch> bash w25_s218_read.sh   # fire, once ~P sends the principal
#
# WHY THIS FILE EXISTS BEFORE THE PACKET DOES. The window is cap 1 and 60 minutes and Andrew's word
# ("yeah Yes run it", ~P 103121) does not extend to a second attempt. Everything decidable in advance is
# decided here so that when the epoch arrives the only act left is to paste it and run -- no judgement at
# fire time. That is the W24 lesson (~P 102921) applied one layer earlier.
#
# WHAT IS DELIBERATELY DIFFERENT FROM w24_run_arms.sh:
#   * ONE arm, not four: the question is about the SESSION, not the report, so the cheapest body that
#     reaches the vendor is the right body (arms file, "The read").
#   * WALK_PW_RETAINED is UNSET. W24 exported it as 1. For W25 ~P credoffs on the login line, BEFORE K4
#     (~P 103128), and live_chain.py waits for the password parameter to read ParameterNotFound.
#   * No cap-truncation loop: with one arm there is no later arm to protect from the clock.
set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/../W25"
PLAN=0
[ "${1:-}" = "--plan" ] && PLAN=1

EPOCH="${EPOCH:-}"
if [ -z "$EPOCH" ] && [ "$PLAN" -eq 0 ]; then
  echo "REFUSED: EPOCH is unset. ~P sends it with the principal; this script never invents one." >&2
  exit 2
fi
EPOCH_SHOWN="${EPOCH:-<epoch-from-P>}"

# NO LEADING SLASH. MSYS converts a leading-slash argument into a Windows path, so "/irpt/..." became
# "/C:/Program Files/Git/irpt/..." and the tool refused at login -- measured on the first W25 attempt at
# 03:33:05Z, BEFORE any POST, so no body was spent. ~P 103132 wrote the name with a leading slash; W24's
# proven form has none, and the proven form wins. Row IRPT_BCKEND-S215 is this same trap.
export WALK_PW_NAME="irpt/ui-walk-principal/${EPOCH_SHOWN}/password"
export WALK_EMAIL="irpt-uiwalk-${EPOCH_SHOWN}@opal.test"
export WALK_TENANT=cottonwood
export WALK_DEADLINE="${WALK_DEADLINE:-<cap-iso-from-P>}"    # always the cap itself, never now+N
export WALK_AUTHORITY="S218 step 2, one-body read. Andrew 2026-09-30 ~03:02Z verbatim 'yeah Yes run it' (~P 103121, record ANDREW_DIRECT_20260930_030xZ_S218_STEP2_ONE_BODY_YCHARTS_WINDOW_YES.md @d821060b8b); W25 never-widen packet NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W25_20260930.md @90aebc3952 (cap 1, 60 min); arms file S218_STEP2_DISCRIMINATING_READ_ARMS_20260929.md; resident st5 sha 8d1f5431 gated by ~Y @5c7c7605f8 and proven RUNNING pid 307882"
# WALK_PW_RETAINED intentionally NOT exported -- see the header.
# WALK_COMPARISON_KEYS intentionally NOT set: Overview, no comparison. The default CSV in live_upload.py
# (aapl-vnq-12.03.csv) is the W15 body the arms file names, so WALK_UPLOAD_FILE stays unset too.

BASE="S218_step2_read"
mkdir -p "$OUT"

echo "=== W25 / S218 step 2 -- ONE body ==="
echo "  tenant        : $WALK_TENANT"
echo "  principal     : $WALK_EMAIL"
echo "  password param: $WALK_PW_NAME"
echo "  deadline      : $WALK_DEADLINE"
echo "  retained      : ${WALK_PW_RETAINED:-<unset, as ~P requires>}"
echo "  body          : Overview, default CSV (aapl-vnq-12.03.csv), no comparison keys"
echo "  out           : $OUT/$BASE.json"
echo

# PRECONDITION, RE-READ AT FIRE TIME AND NOT INHERITED FROM AN EARLIER TICK: the queue must be 0/0 and the
# DLQ must not have grown past its pre-existing 1. The arms file makes solo-ness a condition of the read,
# not a hope -- a body that runs beside other work reproduces S206's concurrency instead of measuring S218.
QURL=https://queue.amazonaws.com/313476888478/irpt-generation
read -r VIS NOTVIS <<EOF
$("$HERE/../../../../../../.tools/aws" sqs get-queue-attributes --queue-url "$QURL" \
    --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible \
    --query 'Attributes' --output text)
EOF
DLQ=$("$HERE/../../../../../../.tools/aws" sqs get-queue-attributes --queue-url "${QURL}-dlq" \
    --attribute-names ApproximateNumberOfMessages --query 'Attributes' --output text)
echo "  PRECONDITION irpt-generation = ${VIS}/${NOTVIS} (must be 0/0)"
echo "  PRECONDITION irpt-generation-dlq = ${DLQ} (baseline 1; growth past 1 is a BLOCKING row)"
if [ "$VIS" != "0" ] || [ "$NOTVIS" != "0" ]; then
  echo "REFUSED: the queue is not 0/0. The read WAITS; it is not attempted alongside other work." >&2
  exit 3
fi

if [ "$PLAN" -eq 1 ]; then
  echo
  echo "PLAN ONLY -- nothing was fired. Fill EPOCH and WALK_DEADLINE from ~P's packet and re-run."
  exit 0
fi

echo "  FIRING at $(date -u +%Y-%m-%dT%H:%M:%SZ) -- one login, one K4, one K5, no retry."
python "$HERE/run_upload.py" "$OUT/$BASE.json" "$HERE/live_chain.py" 2>&1 | tee "$OUT/$BASE.log"

# A REFUSAL MUST STOP THE SCRIPT. On the first attempt the walk refused at login and the script ran on to
# parse an out file that was never written, turning one clear error into two confusing ones.
if [ ! -s "$OUT/$BASE.json" ]; then
  echo "STOPPED: the walk wrote no out file, so nothing was submitted. Read $OUT/$BASE.log for the refusal." >&2
  exit 4
fi

# The jobs terminal, serialized per 1.0.0_SA_CTO condition 1 -- live_chain returns at K5 ACCEPTANCE, which
# is not the outcome. The out path arrives as ARGV: an MSYS unix path inside a python -c SOURCE BODY is not
# converted and Windows python cannot open it (row IRPT_BCKEND-S215, measured live in W24).
req=$(python -c "
import json,re,sys
t=open(sys.argv[1],encoding='utf-8').read()
m=re.search(r'REQ-[0-9a-f]+',t)
print(m.group(0) if m else '')
" "$OUT/$BASE.json")
echo "  REQ = ${req:-<none found>}"
[ -n "$req" ] && python "$HERE/job_terminal_wait.py" "$WALK_TENANT" "$req" 2>&1 | tee -a "$OUT/$BASE.log"

echo
echo "  NOW READ THE ORACLE (IB-yr-231's journal lines, live on st5):"
echo "    python resident_journal.py \"\$(date -u -d '-90 minutes' +'%Y-%m-%d %H:%M:%S')\" 'IRPT_RESIDENT_EVICTION|IRPT_RESIDENT_ATTENTION|Traceback'"
echo "  and grade against the four outcomes in S218_STEP2_DISCRIMINATING_READ_ARMS_20260929.md."
