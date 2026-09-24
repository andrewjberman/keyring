#!/usr/bin/env bash
# Performance retained installation -- the flight checks around ONE safe-apply.
#
# Every value below is RE-MEASURED at execution (CLAUDE.md: an operator recipe that asserts a
# state carries the guard that re-measures it). The expected values are the ones the CTO's GO
# names; a mismatch stops the flight before anything irreversible.
#
#   preflight  [--no-ledger]   plan hash, artifact + layer object versions/hashes, live function
#                              unchanged since the plan, no layer version yet, then OPEN the
#                              deploy ledger (skipped with --no-ledger, e.g. as a dry control).
#   postflight                 live function == the approved artifact, layer version published
#                              with the approved hash, both new policies present, zero-diff plan.
#
# The apply itself is NOT in this script: it is `.tools/safe-apply.sh -chdir=<root> apply <plan>`
# run by the seat, with the halt gate's routine surface acknowledged by hand after reading it.
# ASCII only. Git Bash 3.6.7 utilities only (CLAUDE.md Rule 16).
set -uo pipefail

WT="/cygdrive/c/Users/AndrewBerman/Desktop/irpt-smoke-p-backend-20260923"
WS="/cygdrive/c/Users/AndrewBerman/Desktop/ajb_workspace"
AWS="$WS/.tools/aws"
JQ="$WS/.tools/jq.exe"
ROOT="infra/aws/terraform/investor-reporting/performance"
PLAN="$WT/.runtime/performance-install/install.tfplan"
FN="irpt-performance-adapter"
LAYER="irpt-performance-native-layer"
LEDGER_SLUG="irpt-performance-install-20260923"

# The values the GO names (receipt PERFORMANCE_INSTALL_CANDIDATE_20260923.json).
EXPECT_PLAN_SHA="f0a189191e4f566f8cd76673ee8fb83f707f78c07e6f75dd7bad1a7d2b247a55"
ART_BUCKET="opal-313476888478-lambda-artifacts"
ART_KEY="investor-reporting/irpt-performance-adapter.zip"
ART_VER="h.hlJhL3dKXAFT5NsNzceZX6Jls_f39V"
ART_SHA="JwJEEQGTENJJukTvrNQt3dq6VIAI8xqioIYA1atL+hk="
LAYER_BUCKET="opal-313476888478-lambda-layers"
LAYER_KEY="irpt-performance-native-layer.zip"
LAYER_VER="tf.fKYdfNRbn9AGt1AEHqn35f6bwGqPb"
LAYER_SHA="EhuEB0Fc6ANFj1LeA9EdgdJnkflNIPQTBlinc80fOfY="
LIVE_BEFORE_SHA="jVktMAiRK+2mYPXEzyst6HjSFFv4xR3Kxm47hAyulyw="
COMMON_LAYER="arn:aws:lambda:us-east-1:313476888478:layer:irpt-common:5"
ROLE="irpt-performance-adapter-role"

fail=0
ok()   { printf 'OK:   %s\n' "$1"; }
bad()  { printf 'FAIL: %s\n' "$1"; fail=1; }
check_eq() { # label expected actual
  if [ "$2" = "$3" ]; then ok "$1 = $3"; else bad "$1 expected [$2] measured [$3]"; fi
}

head_obj() { # bucket key -> "VersionId sha"
  "$AWS" s3api head-object --bucket "$1" --key "$2" \
    --query '[VersionId, Metadata."content-sha256"]' --output text 2>&1 | tr -s '[:space:]' ' '
}

preflight() {
  local no_ledger="${1:-}"
  printf '== PREFLIGHT %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  check_eq "plan sha256" "$EXPECT_PLAN_SHA" "$(sha256sum "$PLAN" | awk '{print $1}')"
  check_eq "artifact version+sha" "$ART_VER $ART_SHA " "$(head_obj "$ART_BUCKET" "$ART_KEY")"
  check_eq "layer object version+sha" "$LAYER_VER $LAYER_SHA " "$(head_obj "$LAYER_BUCKET" "$LAYER_KEY")"
  local live
  live="$("$AWS" lambda get-function-configuration --function-name "$FN" \
    --query '[CodeSha256, Handler, State]' --output text 2>&1 | tr -s '[:space:]' ' ')"
  check_eq "live function unchanged since plan" "$LIVE_BEFORE_SHA entry.lambda_handler Active " "$live"
  local versions
  versions="$("$AWS" lambda list-layer-versions --layer-name "$LAYER" --query 'length(LayerVersions)' --output text 2>&1)"
  check_eq "native layer versions before" "0" "$versions"
  local serial
  serial="$("$AWS" s3 cp "s3://opal-313476888478-terraform-state/investor-reporting/performance/tfstate" - 2>/dev/null | "$JQ" -r '.serial')"
  printf 'INFO: performance remote state serial now %s (the plan refuses a moved state on its own)\n' "$serial"
  if [ "$fail" -ne 0 ]; then printf 'PREFLIGHT: BLOCKED -- do not apply.\n'; return 1; fi
  if [ "$no_ledger" = "--no-ledger" ]; then printf 'PREFLIGHT: PASS (ledger not opened: control run)\n'; return 0; fi
  ( cd "$WT" && python .tools/deploy_ledger.py open --slug "$LEDGER_SLUG" \
      --title "Performance retained installation: native layer, two-family role, runtime handler" \
      --author 2.0.0_SA_COO~P --window-hours 4 \
      --leg "A1|activation|Saved plan f0a18919 via safe-apply|apply receipt: 3 add 1 change 0 destroy" \
      --leg "V1|verify|Live function, layer version, policies, zero-diff|readback JSON + post-install plan rc 0" \
      --leg "R1|git|Exact-function recorder|record-terraform-deploy commit hash" ) || { bad "ledger open"; return 1; }
  printf 'PREFLIGHT: PASS -- ledger %s OPEN. Now: .tools/safe-apply.sh -chdir=%s apply -input=false -no-color "<plan>"\n' "$LEDGER_SLUG" "$ROOT"
}

postflight() {
  printf '== POSTFLIGHT %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  local cfg
  cfg="$("$AWS" lambda get-function-configuration --function-name "$FN" \
    --query '[CodeSha256, Handler, Timeout, MemorySize, State, LastUpdateStatus]' --output text 2>&1 | tr -s '[:space:]' ' ')"
  check_eq "live function after" "$ART_SHA runtime.lambda_handler 120 1536 Active Successful " "$cfg"
  local layers
  layers="$("$AWS" lambda get-function-configuration --function-name "$FN" --query 'Layers[].Arn' --output text 2>&1 | tr -s '[:space:]' ' ')"
  case "$layers" in
    *"$COMMON_LAYER"*"layer:$LAYER:"*|*"layer:$LAYER:"*"$COMMON_LAYER"*) ok "layers = $layers" ;;
    *) bad "layers expected common:5 + $LAYER, measured [$layers]" ;;
  esac
  local lv
  lv="$("$AWS" lambda list-layer-versions --layer-name "$LAYER" --query 'LayerVersions[].Version' --output text 2>&1 | tr -s '[:space:]' ' ')"
  check_eq "native layer versions after" "1 " "$lv"
  local lsha
  lsha="$("$AWS" lambda get-layer-version --layer-name "$LAYER" --version-number 1 --query 'Content.CodeSha256' --output text 2>&1)"
  check_eq "native layer content sha" "$LAYER_SHA" "$lsha"
  local pol
  for pol in irpt-performance-retained-policy irpt-performance-adapter-selection-read-policy; do
    if "$AWS" iam get-role-policy --role-name "$ROLE" --policy-name "$pol" --query 'PolicyName' --output text >/dev/null 2>&1; then
      ok "policy present: $pol"; else bad "policy absent: $pol"; fi
  done
  ( cd "$WT" && ./.tools/terraform.exe -chdir="$ROOT" plan -input=false -no-color -detailed-exitcode \
      -out="C:/Users/AndrewBerman/Desktop/irpt-smoke-p-backend-20260923/.runtime/performance-install/post-install.tfplan" \
      > .runtime/performance-install/post-install-plan.log 2>&1 )
  check_eq "post-install plan exit code (0 = no changes)" "0" "$?"
  if [ "$fail" -ne 0 ]; then printf 'POSTFLIGHT: NOT CLEAN -- do not close the ledger; report the FAIL lines.\n'; return 1; fi
  printf 'POSTFLIGHT: PASS. Next: recorder (--function %s --code-sha256 %s), then close legs A1/V1/R1 and the ledger.\n' "$FN" "$ART_SHA"
}

case "${1:-}" in
  preflight)  preflight "${2:-}" ;;
  postflight) postflight ;;
  *) printf 'usage: %s preflight [--no-ledger] | postflight\n' "$0" >&2; exit 2 ;;
esac
