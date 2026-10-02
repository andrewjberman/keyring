#!/usr/bin/env bash
# Hop 3's proof on the st10 resident: an upload resolves while another job's generation is in flight (rows S206, S215;
# CTO rulings batch 61 item 8, batch 72 item 12). Legs P, S and A are the hop-8 runner's P, S and J with this window's
# folder, root, base and ledger; leg B is ONE upload-only body fired only WHILE leg A's job is non-terminal.
#
#   bash hop3_proof_run.sh --plan   # the running root, the solo gate, both bodies validated offline; no vendor call
#   bash hop3_proof_run.sh --leg-p  # ONE liveness read (hop-8 leg P)
#   bash hop3_proof_run.sh --leg-s  # ONE operator sign-in, only if P read NOT_LIVE (hop-8 leg S)
#   bash hop3_proof_run.sh --leg-a  # ONE upload and ONE Overview (hop-8 leg J); blocks until the job is terminal
#   bash hop3_proof_run.sh --leg-b  # ONE upload, NO submission; refuses unless leg A's job is non-terminal right now
#
# Packet: ../HOP3_PROOF/WINDOW_PACKET_HOP3_PROOF_20261002.md. Each leg once; a leg whose output exists refuses.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$HERE/../../../../../.."
AWS="$ROOT/.tools/aws"
export HOP8_OUT="$HERE/../HOP3_PROOF"
export HOP8_ROOT="/opt/irpt-resident/b1db201025-st10"
export HOP8_BASE="H3_A_overview_cottonwood"
export HOP8_AUTHORITY="hop-3 proof leg A; CTO batch 61 item 8 and batch 72 item 12; Andrew-direct 2026-09-27 124xZ; ledger irpt-hop3-proof-20261002"
BASE_B="H3_B_upload_cottonwood"
NONTERMINAL="RECEIVED CLAIMED SUBMITTING SUBMITTED DOWNLOADING EXTRACTING CERTIFYING"
case "${1:-}" in
  --plan)
    bash "$HERE/hop8_run.sh" --plan || exit $?
    ( export WALK_TENANT=cottonwood WALK_EMAIL="svc-irpt-analysis@opalinvest.com"
      export WALK_DEADLINE="$(date -u -d '+60 minutes' +%Y-%m-%dT%H:%M:%S+00:00)"
      python "$HERE/live_chain.py" "$HOP8_OUT/plan_B.json" --dry )
    echo "  leg B would run : live_chain.py with WALK_K4_ONLY=1, base $BASE_B (ONE upload, no K5), only while A's job is in [$NONTERMINAL]"
    echo "PLAN ONLY -- nothing fired."
    ;;
  --leg-p|--leg-s)
    exec bash "$HERE/hop8_run.sh" "$1"
    ;;
  --leg-a)
    exec bash "$HERE/hop8_run.sh" --leg-j
    ;;
  --leg-b)
    [ ! -e "$HOP8_OUT/$BASE_B.json" ] || { echo "REFUSED: $HOP8_OUT/$BASE_B.json exists; leg B was already run." >&2; exit 6; }
    req=$(python -c "
import re,sys
t=open(sys.argv[1],encoding='utf-8').read()
m=re.search(r'REQ-[0-9a-f]{24}',t)
print(m.group(0) if m else '')
" "$HOP8_OUT/$HOP8_BASE.json" 2>&1)
    [ -n "$req" ] || { echo "REFUSED: leg A made no submission (no REQ in its out file); leg B is not run." >&2; exit 7; }
    job_state() {
      "$AWS" dynamodb get-item --table-name irpt-jobs --consistent-read \
        --key "{\"tenant\":{\"S\":\"cottonwood\"},\"job\":{\"S\":\"$req\"}}" --query 'Item.state.S' --output text
    }
    st=$(job_state)
    echo "  CONDITION UNDER TEST: leg A's job $req reads [$st] at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    case " $NONTERMINAL " in
      *" $st "*) ;;
      *) echo "REFUSED: leg A's job is not in flight; the condition under test is gone and leg B is not run." >&2; exit 7 ;;
    esac
    export WALK_EMAIL="svc-irpt-analysis@opalinvest.com" WALK_PW_NAME="irpt/svc-irpt-analysis/password" WALK_PW_RETAINED=1
    export WALK_TENANT=cottonwood WALK_K4_ONLY=1
    export WALK_AUTHORITY="hop-3 proof leg B (upload only, during leg A's generation); CTO batch 61 item 8; ledger irpt-hop3-proof-20261002"
    export WALK_DEADLINE="$(date -u -d '+20 minutes' +%Y-%m-%dT%H:%M:%S+00:00)"
    WALK_PW="$("$AWS" secretsmanager get-secret-value --secret-id "$WALK_PW_NAME" --query SecretString --output text)"
    [ -n "$WALK_PW" ] || { echo "REFUSED: empty secret read." >&2; exit 5; }
    export WALK_PW
    echo "=== leg B fire at $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
    python "$HERE/live_chain.py" "$HOP8_OUT/$BASE_B.json" 2>&1 | tee "$HOP8_OUT/$BASE_B.log"
    unset WALK_PW
    echo "  after leg B: leg A's job $req reads [$(job_state)] at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "=== leg B is over. No submission is made by this leg. ==="
    ;;
  *)
    echo "usage: hop3_proof_run.sh --plan | --leg-p | --leg-s | --leg-a | --leg-b" >&2
    exit 2
    ;;
esac
