#!/usr/bin/env bash
# parity-gates.sh -- ADHC_VALGATE.009 deployment-manifest parity gates
#
# Builds 3 of the declared-vs-empirical parity gates the ADHC_VALGATE.008 catalog
# enumerated (org/modules/parity/PARITY_CLASS_CATALOG.md, pairs P6/P9/P8). A parity
# gate compares a DECLARED inventory (a manifest / source-map) against the EMPIRICAL
# inventory it claims to describe (running AWS fleet / deployed Lambda set / S3 code).
#
# WARN-mode v1 (ADHC_VALGATE PRD section 7 Q1): every gate SURFACES a parity break
# and blocks NOTHING. The script exits 0 regardless of findings. A future BLOCK
# ratchet would add a --strict flag; v1 does not have one by design.
#
# Usage:
#   parity-gates.sh ec2-manifest      # P6
#   parity-gates.sh lambda-sourcemap  # P9
#   parity-gates.sh inf-deploy        # P8
#   parity-gates.sh all               # all three
#
# Rule-16 compliant: uses only Git Bash 3.6.7 default utilities (bash, aws, jq, git,
# grep, sed, awk, tr, sort, timeout) -- no pgrep/pkill/flock/wget.
#
# AWS pagination note: `aws ... --output json` auto-merges all pages into one JSON
# document; `--query` with `--output text` does NOT (it applies per-page). All AWS
# reads here use `--output json | jq` so paginated fleets/functions come back whole.
# All external output is `tr -d '\r'`-stripped -- jq.exe / aws on Windows emit CRLF.
#
# ----------------------------------------------------------------------------------
# GATE ANATOMY (ADHC_VALGATE PRD section 3.2 six-field tables)
#
# P6 -- EC2_MANIFEST completeness vs running fleet
#   Trigger    : on demand / scheduled infra audit (placement: ad-hoc + candidate
#                for a daily CloudOps sweep; not wired to a deploy path in v1)
#   Input      : infra/aws/ec2/EC2_MANIFEST.json .services[].instance_id + .source_path
#   Reference  : aws ec2 describe-instances (running instances in the account)
#   Comparison : every running instance-id must appear as some service's instance_id;
#                every service's non-null source_path must resolve on disk
#   Verdict    : running instance absent from manifest = WARN;
#                manifest source_path that does not resolve = WARN
#   Action     : WARN-only v1 -- print the break; register the service or fix the path
#
# P9 -- Lambda source-map vs deployed AWS Lambda set
#   Trigger    : on demand / scheduled infra audit
#   Input      : infra/aws/lambda/ci/lambda-source-map.json -- .functions{} keys
#                UNION the top-level function-object keys (schema-split tolerant)
#   Reference  : aws lambda list-functions (deployed function names, all pages)
#   Comparison : set diff, both directions
#   Verdict    : deployed Lambda with no source-map entry = WARN (CLAUDE.md Rule 4);
#                source-map entry with no deployed function = WARN (stale manifest)
#   Action     : WARN-only v1 -- register the function or prune the stale entry
#
# P8 -- repo-HEAD vs S3-deployed sweep across the INF chain
#   Trigger    : on demand / pre-chain-dispatch / scheduled
#   Input      : local INF gold + silver scripts (data/inf/scripts/{gold,silver})
#   Reference  : s3://opal-data-inf/code/{gold,silver}/ object ETags
#   Comparison : thin wrapper over `comp-pipescript deployed --pipeline inf-{gold,silver}`
#                which already sweeps the chain (MD5 vs S3 ETag, per script)
#   Verdict    : any script STALE / MISSING_ON_S3 / LOCAL_MISSING = WARN
#                (catches single-homed deploy-misses -- AE 0.6.1 f39550d99 anchor)
#   Action     : WARN-only v1 -- re-run the S3 upload for the drifted script
#   Coverage   : inf-gold + inf-silver tiers (what comp-pipescript deployed sweeps).
#                Bronze/pull-tier scripts are NOT swept by comp-pipescript deployed --
#                noted as a coverage limitation, not core surgery (TO STOP-condition
#                is about wrapper feasibility; the wrapper itself is clean).
# ----------------------------------------------------------------------------------

set -u

WORKSPACE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

export AWS_EC2_METADATA_DISABLED="${AWS_EC2_METADATA_DISABLED:-true}"
export AWS_METADATA_SERVICE_NUM_ATTEMPTS="${AWS_METADATA_SERVICE_NUM_ATTEMPTS:-1}"
export AWS_PAGER=""

TOTAL_WARN=0

warn() { printf '  WARN: %s\n' "$1"; TOTAL_WARN=$((TOTAL_WARN + 1)); }
ok()   { printf '  OK: %s\n' "$1"; }

# ---- P6 -- EC2_MANIFEST completeness vs running fleet --------------------------
gate_ec2_manifest() {
  # PARITY_EC2_MANIFEST overrides the manifest path (synthetic-drift verification only).
  local manifest="${PARITY_EC2_MANIFEST:-$WORKSPACE/infra/aws/ec2/EC2_MANIFEST.json}"
  printf '== P6: EC2_MANIFEST completeness vs running EC2 fleet ==\n'
  if [ ! -f "$manifest" ]; then warn "EC2_MANIFEST.json not found at $manifest"; return; fi

  local declared running iid
  declared="$(jq -r '.services | to_entries[] | select(.value.instance_id != null) | .value.instance_id' "$manifest" | tr -d '\r' | sort -u)"

  running="$(aws ec2 describe-instances \
      --filters "Name=instance-state-name,Values=running" \
      --output json 2>/dev/null | jq -r '.Reservations[].Instances[].InstanceId' 2>/dev/null | tr -d '\r' | sed '/^$/d' | sort -u)"
  if [ -z "$running" ]; then
    warn "aws ec2 describe-instances returned no running instances (or call failed) -- parity not verifiable"
    return
  fi

  local found_drift=0
  for iid in $running; do
    if ! printf '%s\n' "$declared" | grep -qx "$iid"; then
      warn "running EC2 instance $iid is NOT registered in EC2_MANIFEST.json"
      found_drift=1
    fi
  done

  # source_path resolution for declared services
  local svc sp
  while IFS=$'\t' read -r svc sp; do
    [ -z "$svc" ] && continue
    sp="$(printf '%s' "$sp" | tr -d '\r')"
    if [ ! -e "$WORKSPACE/$sp" ]; then
      warn "service '$svc' source_path does not resolve on disk: $sp"
      found_drift=1
    fi
  done < <(jq -r '.services | to_entries[] | select(.value.source_path != null) | "\(.key)\t\(.value.source_path)"' "$manifest")

  [ "$found_drift" -eq 0 ] && ok "all running instances registered; all source_paths resolve"
}

# ---- P9 -- Lambda source-map vs deployed AWS Lambda set ------------------------
gate_lambda_sourcemap() {
  # PARITY_LAMBDA_SOURCEMAP overrides the source-map path (synthetic-drift verification only).
  local sm="${PARITY_LAMBDA_SOURCEMAP:-$WORKSPACE/infra/aws/lambda/ci/lambda-source-map.json}"
  printf '== P9: Lambda source-map vs deployed AWS Lambda set ==\n'
  if [ ! -f "$sm" ]; then warn "lambda-source-map.json not found at $sm"; return; fi

  # Declared = .functions{} keys UNION any top-level function-object keys (the
  # source-map has a schema split: functions under .functions + siblings of it).
  local declared deployed
  declared="$(jq -r '
      (.functions // {} | keys[]),
      (to_entries[] | select(.key != "functions")
                    | select(.key | startswith("_") | not)
                    | select(.value | type == "object")
                    | .key)
    ' "$sm" | tr -d '\r' | sort -u)"

  # --output json auto-merges all paginated pages into one document.
  deployed="$(aws lambda list-functions --output json 2>/dev/null | jq -r '.Functions[].FunctionName' 2>/dev/null | tr -d '\r' | sed '/^$/d' | sort -u)"
  if [ -z "$deployed" ]; then
    warn "aws lambda list-functions returned nothing (or call failed) -- parity not verifiable"
    return
  fi

  local fn found_drift=0
  # deployed Lambda with no source-map entry
  while read -r fn; do
    [ -z "$fn" ] && continue
    printf '%s\n' "$declared" | grep -qx "$fn" || { warn "deployed Lambda '$fn' has NO source-map entry (CLAUDE.md Rule 4)"; found_drift=1; }
  done < <(printf '%s\n' "$deployed")
  # source-map entry with no deployed Lambda
  while read -r fn; do
    [ -z "$fn" ] && continue
    printf '%s\n' "$deployed" | grep -qx "$fn" || { warn "source-map entry '$fn' has NO deployed Lambda (stale manifest)"; found_drift=1; }
  done < <(printf '%s\n' "$declared")

  [ "$found_drift" -eq 0 ] && ok "source-map function set matches the deployed Lambda set"
}

# ---- P8 -- repo-HEAD vs S3-deployed sweep across the INF chain -----------------
gate_inf_deploy() {
  printf '== P8: repo-HEAD vs S3-deployed sweep (INF gold + silver chain) ==\n'
  local cps="$WORKSPACE/.tools/comp-pipescript"
  if [ ! -x "$cps" ] && ! command -v comp-pipescript >/dev/null 2>&1; then
    warn "comp-pipescript not found -- P8 sweep not runnable"
    return
  fi
  local runner; runner="$cps"; [ -x "$cps" ] || runner="comp-pipescript"

  local out tier found_drift=0
  for tier in inf-gold inf-silver; do
    out="$(timeout 240 "$runner" deployed --pipeline "$tier" 2>&1 | tr -d '\r')"
    local stale missing localmiss unreach
    stale="$(printf '%s\n' "$out"     | grep -cE '[[:space:]]STALE[[:space:]]')"
    missing="$(printf '%s\n' "$out"   | grep -cE '[[:space:]]MISSING_ON_S3[[:space:]]')"
    localmiss="$(printf '%s\n' "$out" | grep -cE '[[:space:]]LOCAL_MISSING[[:space:]]')"
    unreach="$(printf '%s\n' "$out"   | grep -cE '[[:space:]](AWS_UNREACHABLE|TIMEOUT)[[:space:]]')"
    if [ "$unreach" -gt 0 ]; then
      warn "[$tier] $unreach script(s) AWS_UNREACHABLE/TIMEOUT -- parity not verifiable for those"
    fi
    if [ "$stale" -gt 0 ] || [ "$missing" -gt 0 ] || [ "$localmiss" -gt 0 ]; then
      warn "[$tier] deploy parity break -- STALE=$stale MISSING_ON_S3=$missing LOCAL_MISSING=$localmiss"
      printf '%s\n' "$out" | grep -E '[[:space:]](STALE|MISSING_ON_S3|LOCAL_MISSING)[[:space:]]' | sed 's/^/    /'
      found_drift=1
    fi
  done
  [ "$found_drift" -eq 0 ] && ok "all swept INF gold+silver scripts MATCH their S3-deployed bytes"
}

main() {
  local cmd="${1:-}"
  case "$cmd" in
    ec2-manifest)     gate_ec2_manifest ;;
    lambda-sourcemap) gate_lambda_sourcemap ;;
    inf-deploy)       gate_inf_deploy ;;
    all)              gate_ec2_manifest; echo; gate_lambda_sourcemap; echo; gate_inf_deploy ;;
    *)
      echo "usage: parity-gates.sh {ec2-manifest|lambda-sourcemap|inf-deploy|all}" >&2
      exit 2 ;;
  esac
  echo
  if [ "$TOTAL_WARN" -eq 0 ]; then
    echo "PARITY GATES: PASS -- 0 WARN"
  else
    echo "PARITY GATES: $TOTAL_WARN WARN -- review above (WARN-mode v1: nothing blocked)"
  fi
  # WARN-not-BLOCK v1: always exit 0. A future --strict ratchet would change this.
  exit 0
}

main "$@"
