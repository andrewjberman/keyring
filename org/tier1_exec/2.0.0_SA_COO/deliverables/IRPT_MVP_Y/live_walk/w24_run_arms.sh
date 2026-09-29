#!/usr/bin/env bash
# W24 part Y: run arms 1-4 in 2.0.0_SA_COO~P's ruled order, serialized on the irpt-jobs terminal.
#
#   bash w24_run_arms.sh            # run for real, from the first arm
#   bash w24_run_arms.sh --plan     # print what WOULD run against the clock; no login, no POST
#   bash w24_run_arms.sh --from 3   # resume at arm 3
#
# ~P's ruling 102921, enforced here so no judgement happens at fire time:
#   "Do not start an arm whose slow-case finish passes 18:18:34Z; name it as cap-truncated instead."
# The S206 discriminator is DROPPED BY NAME (102921); this script does not carry it.
# 1.0.0_SA_CTO condition 1: serialize on the irpt-jobs row terminal, not the NORMALIZATION row.
set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/../W24"
CAP_ISO="2026-09-29T18:18:34+00:00"
CAP_EPOCH=$(python -c "import datetime;print(int(datetime.datetime.fromisoformat('$CAP_ISO').timestamp()))")
SLOW_MIN=32   # W22 measured 31.5 min for its slowest job; round up, never down

export WALK_PW_NAME=irpt/ui-walk-principal/1790698706/password
export WALK_EMAIL=irpt-uiwalk-1790698706@opal.test
export WALK_PW_RETAINED=1
export WALK_DEADLINE="$CAP_ISO"   # always the cap itself, never now+N
export WALK_AUTHORITY="W24 packet 3089695cc6 (@cbbe9ed0db, amended); CTO 102899 @895964dda7; CRO 102904 @bf61fecc94; ledger irpt-ui-walk-principal-w24-20260929; ~P 102908/102921"

XLSX="C:\\Users\\AndrewBerman\\Desktop\\ajb_workspace\\org\\tier1_exec\\2.0.0_SA_COO\\deliverables\\IRPT_MVP_Y\\aapl-vnq-target-weight.xlsx"

# arm | tenant | out basename | extra env (space separated NAME=VALUE)
ARMS=(
  "Multi-Comp|cottonwood|Y1_multicomp_cottonwood|WALK_COMPARISON_KEYS=opal_short_term,opal_intermediate_term"
  "Target Weight n=1000 XLSX|cottonwood|Y2_targetweight_xlsx_cottonwood|WALK_UPLOAD_FILE=$XLSX WALK_FILE_TYPE=xlsx WALK_REFERENCE_NOTIONAL=1000"
  "Overview 49financial|49financial|Y3_overview_49financial|"
  "Overview inflection|inflection|Y4_overview_inflection|"
)

PLAN=0; FROM=1
while [ $# -gt 0 ]; do
  case "$1" in
    --plan) PLAN=1 ;;
    --from) shift; FROM="$1" ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
  shift
done

say() { echo "$(date -u +%H:%M:%SZ) $*"; }

mkdir -p "$OUT"
say "CAP $CAP_ISO | slow-case allowance ${SLOW_MIN} min | arms ${#ARMS[@]} (discriminator DROPPED by name, ~P 102921)"

i=0
for row in "${ARMS[@]}"; do
  i=$((i+1))
  [ "$i" -lt "$FROM" ] && continue
  name="${row%%|*}";  rest="${row#*|}"
  tenant="${rest%%|*}"; rest="${rest#*|}"
  base="${rest%%|*}";   extra="${rest#*|}"

  now=$(date -u +%s)
  left=$(( (CAP_EPOCH - now) / 60 ))
  if [ "$left" -lt "$SLOW_MIN" ]; then
    say "ARM $i $name: CAP-TRUNCATED -- ${left} min left, slow case needs ${SLOW_MIN}. Not started; the arm carries."
    # --plan must be side-effect free: it may print the verdict but never writes the record.
    [ "$PLAN" -eq 0 ] && echo "CAP-TRUNCATED arm $i ($name): ${left} min remained at $(date -u +%H:%M:%SZ); not started" >> "$OUT/CAP_TRUNCATED.txt"
    continue
  fi
  say "ARM $i $name [$tenant] -- ${left} min to cap, starting"

  if [ "$PLAN" -eq 1 ]; then
    say "  --plan: would run live_chain.py -> $OUT/$base.json with [$extra]"
    continue
  fi

  # shellcheck disable=SC2086
  ( export WALK_TENANT="$tenant"; [ -n "$extra" ] && export $extra; \
    python "$HERE/run_upload.py" "$OUT/$base.json" live_chain.py )
  rc=$?
  say "  live_chain rc=$rc"

  # The out path MUST arrive as ARGV. MSYS converts a unix path in argv to a Windows path, but NOT one embedded in
  # the -c source text: Windows Python then reads /c/Users/... as C:\c\Users\... and the open fails silently, the REQ
  # reads empty, the jobs-terminal wait is skipped and the next arm starts concurrently -- which is the exact S206
  # failure. Measured live in W24 at 17:26Z (row IRPT_BCKEND-S212).
  req=$(python -c "
import json,re,sys
try:
    d=json.load(open(sys.argv[1],encoding='utf-8'))
    m=re.search(r'REQ-[0-9a-f]+', d.get('request_ref') or '')
    print(m.group(0) if m else '')
except Exception as exc:
    print('', file=sys.stderr)
    print('REQ-READ-FAILED:%s' % exc, file=sys.stderr)
    print('')
" "$OUT/$base.json")
  if [ -z "$req" ]; then
    say "  WARNING: no REQ parsed from $OUT/$base.json -- NOT starting the next arm blind"
  fi
  if [ -z "$req" ]; then
    say "  no REQ (K4 did not normalize, or K5 not made) -- nothing to wait on; next arm"
    continue
  fi
  say "  REQ $req -- waiting for the irpt-jobs terminal (CTO condition 1)"
  python "$HERE/job_terminal_wait.py" "$tenant" "$req" --floor 20 --deadline "$CAP_ISO"
  say "  arm $i done"
done

say "part Y run finished; case-trace every REQ, then hand ~P the credoff"
