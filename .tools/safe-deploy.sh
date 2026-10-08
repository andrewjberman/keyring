#!/usr/bin/env bash
# safe-deploy.sh -- atomic DS deploy gate: S3 cp + SHA verify + comp-pipescript confirm.
# ADHC_DSFLOW.005 (0.7.0_AE_CloudOps, 2026-05-11)
#
# Structural enforcement for CLAUDE.md rule 13:
#   DS commit -> push -> S3 cp -> verify MATCH -> SSM dispatch.
# Replaces the cultural reminder with a gate that structurally closes the gap.
#
# Usage:
#   .tools/safe-deploy.sh [--allow-stale --reason "..."] [--author "..."]
#       [--commit-range <old>..<new>] [--no-pipescript] [file1 file2 ...]
#
#   Called directly with explicit files OR via pre-push hook with --commit-range.
#   With no arguments: detects changed scripts in HEAD~1..HEAD.
#
# Exit codes:
#   0 = all files deployed and verified (or --allow-stale bypass)
#   1 = gate failure (upload error, SHA mismatch, STALE/MISSING after deploy)
#   2 = usage error
#
# Bypass:
#   --allow-stale  Skips deploy+verify; writes audit entry.
#                  Requires --reason. Use for: emergency hotfix when comp-pipescript
#                  is broken, docstring-only changes, multi-agent worktree contention.
#   Audit log: org/safe-deploy-bypass-audit.log
#
# Pipeline->S3 mapping (baked into safe_deploy_core.py PIPELINE_MAP):
#   data/black_diamond/scripts/{gold,silver,bronze}/*.py  -> opal-data-bd
#   data/inf/scripts/{gold,silver,bronze}/*.py            -> opal-data-inf
#   data/cot/scripts/{gold,silver,bronze}/*.py            -> opal-data-cot
# cot (Cottonwood) is a COMPLETELY separate firm pipeline from bd (Andrew sovereign
# 2026-06-10, NFRA_DTAFLP): its gold tree lives in git at data/cot/scripts/gold/ and
# deploys ONLY to opal-data-cot/code/gold/ -- never mirrored/synced from opal-data-bd.
# Cross-firm bucket refs are blocked at commit (ds-precommit-check.py) + runtime (IAM Deny).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="python"
command -v python3 >/dev/null 2>&1 && PYTHON="python3"

# --- NFRA_CTLPLN CT-d-3 -- a named commit off the trunk (opt-in; DEPLOY_COMMIT unset = no change at all) ---
if [ -n "${DEPLOY_COMMIT:-}" ]; then
    NC_RC=0
    NC_OUT="$("$PYTHON" "$SCRIPT_DIR/named_commit_check.py" check --commit "$DEPLOY_COMMIT" --record 2>&1)" || NC_RC=$?
    printf '%s\n' "$NC_OUT" >&2
    [ "$NC_RC" -eq 0 ] || { echo "safe-deploy: BLOCKED by the named-commit check (rc=$NC_RC). Nothing was deployed." >&2; exit 1; }
    [ "${SAFE_NAMED_COMMIT_CHECK_ONLY:-}" = "1" ] && exit 0
fi

# --- NFRA_CTLPLN CT-s-3 -- SEAT GATES (ONE block): who may deploy (apply-who-check.py) and the cross-box deploy
# measurements (crossbox-deploy-check.py), per data/<pipeline> root named by the files, the --commit-range or HEAD~1..HEAD.
# FOUR switches exist, one per check per tool; this wrapper reads two, each a file in org/mcp/ (OPAL_SEAT_GATES_ENFORCE_DIR
# points a test at another directory; nothing here creates one): seat-gates.apply-who.safe-deploy.enforce and
# seat-gates.crossbox.safe-deploy.enforce (safe-apply.sh reads the two .safe-apply. files). A check is in ENFORCE only
# while ITS file exists; otherwise it is in WARN mode: it prints and NEVER changes this script's exit code or flow, whatever
# happens inside the block. The old single org/mcp/seat-gates.enforce is retired: it turns on nothing and prints one WARN line.
# In ENFORCE a check that gives no verdict (a crash, an absent tool, a timeout, no python) BLOCKS with the error printed, and
# so does an error of the block itself; the audited SEAT_GATES_OVERRIDE="reason" (org/safe-deploy-bypass-audit.log) passes both.
# apply-who grades a DEPLOY: it runs only when this invocation will deploy at least one file, as the deploy core itself decides
# (crossbox-deploy-check.py --list-deployable imports the core's own detectors); otherwise one SKIP line and no verdict. OVERLAP
# is judged on the files that will be deployed under each root, never on the root alone. --dry-seat-gates runs the checks,
# prints, and exits at the end of this block: no halt gate and no deploy core follows.
SG_RC=0
(
  set +e +u
  sg_dir="${OPAL_SEAT_GATES_ENFORCE_DIR:-$SCRIPT_DIR/../org/mcp}"
  sg_mw=WARN; [ -e "$sg_dir/seat-gates.apply-who.safe-deploy.enforce" ] && sg_mw=ENFORCE
  sg_mc=WARN; [ -e "$sg_dir/seat-gates.crossbox.safe-deploy.enforce" ] && sg_mc=ENFORCE
  [ -e "$sg_dir/seat-gates.enforce" ] && echo "safe-deploy: WARN [seat-gates] org/mcp/seat-gates.enforce is retired and turns on nothing; the four switches are org/mcp/seat-gates.apply-who.safe-apply.enforce, seat-gates.apply-who.safe-deploy.enforce, seat-gates.crossbox.safe-apply.enforce and seat-gates.crossbox.safe-deploy.enforce." >&2
  sg_to=""; command -v timeout >/dev/null 2>&1 && sg_to="timeout 60"
  sg_serial="UNKNOWN"
  [ -f "$SCRIPT_DIR/lib/resolve-actor.sh" ] && . "$SCRIPT_DIR/lib/resolve-actor.sh" && sg_serial="$(resolve_actor)"
  sg_paths=""; sg_range=""; sg_prev=""; sg_explicit=()
  for sg_a in "$@"; do
    case "$sg_prev" in
      --commit-range) sg_range="$sg_a" ;;
      --reason|--author) ;;
      *) case "$sg_a" in -*) ;; *) sg_paths="$sg_paths$sg_a"$'\n'; sg_explicit+=("$sg_a") ;; esac ;;
    esac
    sg_prev="$sg_a"
  done
  if [ -z "$sg_paths" ]; then
    if [ -n "$sg_range" ]; then sg_paths="$(git -C "$SCRIPT_DIR/.." diff --name-only "$sg_range" 2>&1)"
    else sg_paths="$(git -C "$SCRIPT_DIR/.." diff --name-only HEAD~1 HEAD 2>&1)"; fi
  fi
  if [ "${#sg_explicit[@]}" -gt 0 ]; then
    sg_dl="$(printf '%s\n' "${sg_explicit[@]}" | $sg_to python "$SCRIPT_DIR/crossbox-deploy-check.py" --list-deployable --repo-root "$SCRIPT_DIR/.." --files-from - 2>&1)"; sg_drc=$?
  else
    sg_dl="$($sg_to python "$SCRIPT_DIR/crossbox-deploy-check.py" --list-deployable --repo-root "$SCRIPT_DIR/.." ${sg_range:+--commit-range "$sg_range"} 2>&1 </dev/null)"; sg_drc=$?
  fi
  sg_dl="$(printf '%s\n' "$sg_dl" | tr -d '\r')"
  sg_dn="$(printf '%s\n' "$sg_dl" | sed -n 's/^DEPLOYABLE-COUNT n=\([0-9]*\)$/\1/p' | tail -n 1)"
  sg_roots="$( { printf '%s\n' "$sg_paths" | tr -d '\r' | sed -n 's#^\(.*/\)\{0,1\}\(data/[^/]*\)/scripts/.*$#\2#p'; printf '%s\n' "$sg_dl" | sed -n 's#^DEPLOY-ROOT ##p'; } | sort -u | head -n 4)"
  if [ -z "$sg_roots" ]; then
    echo "safe-deploy: SKIP [seat-gates] no data/<pipeline>/scripts path in the files or commit range; nothing to measure." >&2
    exit 0
  fi
  sg_bad=""; sg_blk=""; sg_first=1
  for sg_root in $sg_roots; do
    if [ "$sg_first" -eq 1 ]; then
      sg_first=0
      if [ "$sg_dn" = "0" ]; then
        echo "safe-deploy: SKIP [seat-gates] apply-who: this invocation deploys nothing" >&2
      else
        [ -n "$sg_dn" ] || echo "safe-deploy: WARN [seat-gates] could not tell what this invocation deploys (rc=$sg_drc): $(printf '%s\n' "$sg_dl" | tail -n 1); apply-who runs as before." >&2
        sg_w="$($sg_to python "$SCRIPT_DIR/apply-who-check.py" --serial "$sg_serial" --root "$sg_root" 2>&1)"; sg_wrc=$?
        sg_wl="$(printf '%s\n' "$sg_w" | tail -n 1 | tr -d '\r')"
        case "$sg_wl" in
          "APPLY-WHO "*" verdict=REFUSED "*) if [ "$sg_mw" = ENFORCE ]; then sg_blk="$sg_blk apply-who"; else sg_bad="$sg_bad apply-who"; fi ;;
          "APPLY-WHO "*" verdict=ADMITTED "*) : ;;
          *) if [ "$sg_mw" = ENFORCE ]; then
               echo "safe-deploy: ERROR [seat-gates] apply-who-check gave no verdict (rc=$sg_wrc); ENFORCE fails closed:" >&2
               printf '%s\n' "$sg_w" | tail -n 5 | tr -d '\r' | sed 's/^/safe-deploy: [seat-gates]   | /' >&2
               sg_blk="$sg_blk apply-who:no-verdict"
             else echo "safe-deploy: WARN [seat-gates] apply-who-check gave no verdict (rc=$sg_wrc): $sg_wl" >&2; fi ;;
        esac
        echo "safe-deploy: [seat-gates] mode=$sg_mw $sg_wl" >&2
      fi
    fi
    sg_fa=(); [ -n "$sg_dn" ] && sg_fa=(--files-from -)
    sg_rf="$(printf '%s\n' "$sg_dl" | sed -n "s#^DEPLOYABLE \(${sg_root}/.*\)\$#\1#p")"
    sg_c="$(printf '%s\n' "$sg_rf" | $sg_to python "$SCRIPT_DIR/crossbox-deploy-check.py" --root "$sg_root" --serial "$sg_serial" "${sg_fa[@]}" 2>&1)"; sg_crc=$?
    sg_cl="$(printf '%s\n' "$sg_c" | tail -n 1 | tr -d '\r')"
    case "$sg_cl" in
      "CROSSBOX-DEPLOY "*" verdict=STOP")
        if [ "$sg_mc" = ENFORCE ]; then sg_blk="$sg_blk crossbox-deploy:$sg_root"; else sg_bad="$sg_bad crossbox-deploy:$sg_root"; fi
        printf '%s\n' "$sg_c" | tr -d '\r' | sed -n 's/^STOP: /safe-deploy: [seat-gates] STOP: /p' >&2 ;;
      "CROSSBOX-DEPLOY "*" verdict=CLEAR") : ;;
      *) if [ "$sg_mc" = ENFORCE ]; then
           echo "safe-deploy: ERROR [seat-gates] crossbox-deploy-check gave no verdict (rc=$sg_crc); ENFORCE fails closed:" >&2
           printf '%s\n' "$sg_c" | tail -n 5 | tr -d '\r' | sed 's/^/safe-deploy: [seat-gates]   | /' >&2
           sg_blk="$sg_blk crossbox-deploy:$sg_root:no-verdict"
         else echo "safe-deploy: WARN [seat-gates] crossbox-deploy-check gave no verdict (rc=$sg_crc): $sg_cl" >&2; fi ;;
    esac
    echo "safe-deploy: [seat-gates] mode=$sg_mc $sg_cl" >&2
  done
  if [ -n "$sg_bad" ]; then
    echo "safe-deploy: WARN [seat-gates] would stop under ENFORCE ($sg_bad ); WARN mode proceeds." >&2
  fi
  if [ -n "$sg_blk" ]; then
    if [ -n "${SEAT_GATES_OVERRIDE:-}" ]; then
      printf '%s SEAT_GATES_OVERRIDE actor=%s safe-deploy roots=%s blocked=%s reason=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
        "$sg_serial" "$(printf '%s' "$sg_roots" | tr '\n' ',')" "$sg_blk" "$SEAT_GATES_OVERRIDE" >> "$SCRIPT_DIR/../org/safe-deploy-bypass-audit.log"
      echo "safe-deploy: [seat-gates] OVERRIDDEN (audited): $SEAT_GATES_OVERRIDE" >&2
    else
      echo "safe-deploy: BLOCKED by the seat gates (ENFORCE, a switch file in $sg_dir):$sg_blk. Nothing was deployed. Override: SEAT_GATES_OVERRIDE=\"reason\"." >&2
      exit 9
    fi
  fi
  exit 0
) || SG_RC=$?
if [ "$SG_RC" -ne 0 ] && [ "$SG_RC" -ne 9 ]; then
  sg_pd="${OPAL_SEAT_GATES_ENFORCE_DIR:-$SCRIPT_DIR/../org/mcp}"
  if [ -e "$sg_pd/seat-gates.apply-who.safe-deploy.enforce" ] || [ -e "$sg_pd/seat-gates.crossbox.safe-deploy.enforce" ]; then
    if [ -n "${SEAT_GATES_OVERRIDE:-}" ]; then
      printf '%s SEAT_GATES_OVERRIDE actor=%s safe-deploy block-error rc=%s reason=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
        "${OPAL_AGENT_SERIAL:-UNKNOWN}" "$SG_RC" "$SEAT_GATES_OVERRIDE" >> "$SCRIPT_DIR/../org/safe-deploy-bypass-audit.log"
      echo "safe-deploy: [seat-gates] the block errored (rc=$SG_RC) under ENFORCE; OVERRIDDEN (audited): $SEAT_GATES_OVERRIDE" >&2
      SG_RC=0
    else
      echo "safe-deploy: BLOCKED by the seat gates: the block itself errored (rc=$SG_RC) and a switch file is present in $sg_pd (ENFORCE fails closed). Nothing was deployed. Override: SEAT_GATES_OVERRIDE=\"reason\"." >&2
      SG_RC=9
    fi
  else
    echo "safe-deploy: WARN [seat-gates] the block errored (rc=$SG_RC); proceeding exactly as before." >&2
    SG_RC=0
  fi
fi
if [ "$SG_RC" -eq 9 ]; then exit 1; fi
for sg_x in "$@"; do
  if [ "$sg_x" = "--dry-seat-gates" ]; then echo "safe-deploy: --dry-seat-gates: the seat gates ran; nothing was deployed." >&2; exit 0; fi
done

# --- ADHC_HALTGT.002 -- HALTGT deploy-time checkpoint ---
# Source the .001 checkpoint library and gate before the S3 deploy: a STOP-class
# inbox message hard-blocks; a routine message surfaces + needs HALT_ACK=1; an
# empty inbox passes silently. Non-zero = abort before exec.
HALT_GATE="$SCRIPT_DIR/halt-gate-check.sh"
if [ -f "$HALT_GATE" ]; then
    # shellcheck source=/dev/null
    . "$HALT_GATE"
    halt_gate_check "safe-deploy" || exit $?
fi

exec "$PYTHON" "$SCRIPT_DIR/safe_deploy_core.py" "$@"
