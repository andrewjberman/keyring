#!/usr/bin/env bash
# =============================================================================
# safe-apply.sh -- HALTGT-gated `terraform apply` wrapper (ADHC_HALTGT.003)
# =============================================================================
# The PRIMARY HALTGT net. `terraform apply` is the irreversible step and it
# precedes the git push, so a pre-push-only checkpoint (ADHC_HALTGT.002) lets
# the apply happen before a STOP is seen. safe-apply fires the ADHC_HALTGT.001
# checkpoint immediately before the apply -- the last reversible moment.
#
# Behaviour:
#   - Runs the .001 checkpoint (.tools/halt-gate-check.sh) FIRST.
#   - Checkpoint blocks (STOP-class, or routine without HALT_ACK=1) -> safe-apply
#     exits non-zero and terraform is NEVER invoked.
#   - Checkpoint passes -> delegates via exec to the real terraform binary with
#     every argument passed through unchanged; terraform's exit code propagates.
#   - Gates `apply` ONLY. `plan` and other subcommands are non-destructive --
#     call terraform.exe directly for those.
#
# Usage (pass args exactly as to terraform.exe, INCLUDING the `apply` word):
#   .tools/safe-apply.sh [-chdir=DIR] apply [apply-args...]
#   HALT_ACK=1 .tools/safe-apply.sh ... apply ...     # re-run after a routine surface
#
# Env:
#   SAFE_APPLY_TERRAFORM  Override the terraform binary (default: sibling terraform.exe).
#
# Git Bash 3.6.7-safe (CLAUDE.md Rule 16). ASCII only -- no emoji.
# =============================================================================
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Terraform resolution is DEVICE-AGNOSTIC (CLAUDE.md: derive, do not hardcode).
# The sibling terraform.exe exists on some devices and NOT on others -- site Z has no
# .tools/terraform.exe and resolves terraform v1.15.8 on PATH -- and Rule 26 routes every
# apply to the device that owns the work. A baked sibling path therefore does not merely
# fail: it makes the tag-authz gate below unable to produce a plan, which surfaces as
# 'could not evaluate' and steers the operator toward TAGAUTHZ_OVERRIDE. Explicit override
# wins, then the sibling, then PATH, then FAIL LOUD -- never an unresolved value.
if [ -n "${SAFE_APPLY_TERRAFORM:-}" ]; then
  TERRAFORM="$SAFE_APPLY_TERRAFORM"
elif [ -x "$SCRIPT_DIR/terraform.exe" ]; then
  TERRAFORM="$SCRIPT_DIR/terraform.exe"
elif command -v terraform >/dev/null 2>&1; then
  TERRAFORM="$(command -v terraform)"
else
  echo "safe-apply: ERROR -- no terraform binary found." >&2
  echo "            Looked for: \$SAFE_APPLY_TERRAFORM, then $SCRIPT_DIR/terraform.exe, then PATH." >&2
  echo "            Refusing to run. (Fail closed HERE, loudly, rather than later as a gate that cannot evaluate.)" >&2
  exit 5
fi
HALT_GATE="$SCRIPT_DIR/halt-gate-check.sh"

# Gate `apply` only -- refuse if no `apply` subcommand is present.
has_apply=0
for arg in "$@"; do
  if [ "$arg" = "apply" ]; then
    has_apply=1
    break
  fi
done
if [ "$has_apply" -ne 1 ]; then
  echo "safe-apply: ERROR -- no 'apply' subcommand in the arguments." >&2
  echo "safe-apply: this wrapper gates 'terraform apply' only. For 'plan' or any" >&2
  echo "            other subcommand call the terraform binary directly." >&2
  echo "safe-apply: usage -- safe-apply.sh [-chdir=DIR] apply [apply-args...]" >&2
  exit 2
fi

# NFRA_CTLPLN CT-d-3 -- a named commit off the trunk (apply path only; opt-in: DEPLOY_COMMIT unset = no change at all).
if [ -n "${DEPLOY_COMMIT:-}" ]; then
  NC_RC=0
  NC_OUT="$(python "$SCRIPT_DIR/named_commit_check.py" check --commit "$DEPLOY_COMMIT" --record 2>&1)" || NC_RC=$?
  printf '%s\n' "$NC_OUT" >&2
  [ "$NC_RC" -eq 0 ] || { echo "safe-apply: BLOCKED by the named-commit check (rc=$NC_RC). Nothing was applied." >&2; exit 8; }
  [ "${SAFE_NAMED_COMMIT_CHECK_ONLY:-}" = "1" ] && exit 0
fi

# NFRA_CTLPLN CT-s-3 -- SEAT GATES (ONE block): who may apply (apply-who-check.py) and the cross-box deploy
# measurements (crossbox-deploy-check.py). WARN mode (the default) prints and NEVER changes this script's exit code or
# flow; ENFORCE only while org/mcp/seat-gates.enforce exists (OPAL_SEAT_GATES_ENFORCE_FILE points a test elsewhere;
# nothing here creates it). Any error inside the block (no python, an unreadable file, a timeout, a crash) is a WARN
# line and the apply goes on as before. Audited override: SEAT_GATES_OVERRIDE="reason" (org/git-author-override-audit.log).
# --dry-seat-gates runs the two checks, prints, and exits at the end of this block: no halt gate, plan or terraform follows.
SG_RC=0
(
  set +e +u
  sg_enf="${OPAL_SEAT_GATES_ENFORCE_FILE:-$SCRIPT_DIR/../org/mcp/seat-gates.enforce}"
  sg_mode=WARN; [ -e "$sg_enf" ] && sg_mode=ENFORCE
  sg_to=""; command -v timeout >/dev/null 2>&1 && sg_to="timeout 60"
  sg_serial="UNKNOWN"
  [ -f "$SCRIPT_DIR/lib/resolve-actor.sh" ] && . "$SCRIPT_DIR/lib/resolve-actor.sh" && sg_serial="$(resolve_actor)"
  sg_root="."; sg_targs=(); sg_prev=""
  for sg_a in "$@"; do
    case "$sg_prev" in -target|--target) sg_targs+=(--target "$sg_a") ;; esac
    case "$sg_a" in
      -chdir=*) sg_root="${sg_a#-chdir=}" ;;
      -target=*|--target=*) sg_targs+=(--target "${sg_a#*=}") ;;
    esac
    sg_prev="$sg_a"
  done
  sg_bad=""
  sg_w="$($sg_to python "$SCRIPT_DIR/apply-who-check.py" --serial "$sg_serial" --root "$sg_root" "${sg_targs[@]}" 2>&1)"; sg_wrc=$?
  sg_wl="$(printf '%s\n' "$sg_w" | tail -n 1 | tr -d '\r')"
  case "$sg_wl" in
    "APPLY-WHO "*" verdict=REFUSED "*) sg_bad="$sg_bad apply-who" ;;
    "APPLY-WHO "*" verdict=ADMITTED "*) : ;;
    *) echo "safe-apply: WARN [seat-gates] apply-who-check gave no verdict (rc=$sg_wrc): $sg_wl" >&2 ;;
  esac
  echo "safe-apply: [seat-gates] mode=$sg_mode $sg_wl" >&2
  sg_c="$($sg_to python "$SCRIPT_DIR/crossbox-deploy-check.py" --root "$sg_root" --serial "$sg_serial" "${sg_targs[@]}" 2>&1)"; sg_crc=$?
  sg_cl="$(printf '%s\n' "$sg_c" | tail -n 1 | tr -d '\r')"
  case "$sg_cl" in
    "CROSSBOX-DEPLOY "*" verdict=STOP") sg_bad="$sg_bad crossbox-deploy"; printf '%s\n' "$sg_c" | tr -d '\r' | sed -n 's/^STOP: /safe-apply: [seat-gates] STOP: /p' >&2 ;;
    "CROSSBOX-DEPLOY "*" verdict=CLEAR") : ;;
    *) echo "safe-apply: WARN [seat-gates] crossbox-deploy-check gave no verdict (rc=$sg_crc): $sg_cl" >&2 ;;
  esac
  echo "safe-apply: [seat-gates] mode=$sg_mode $sg_cl" >&2
  if [ -n "$sg_bad" ] && [ "$sg_mode" = ENFORCE ]; then
    if [ -n "${SEAT_GATES_OVERRIDE:-}" ]; then
      printf '%s SEAT_GATES_OVERRIDE actor=%s safe-apply root=%s blocked=%s reason=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
        "$sg_serial" "$sg_root" "$sg_bad" "$SEAT_GATES_OVERRIDE" >> "$SCRIPT_DIR/../org/git-author-override-audit.log"
      echo "safe-apply: [seat-gates] OVERRIDDEN (audited): $SEAT_GATES_OVERRIDE" >&2
    else
      echo "safe-apply: BLOCKED by the seat gates (ENFORCE, org/mcp/seat-gates.enforce present):$sg_bad. Nothing was applied. Override: SEAT_GATES_OVERRIDE=\"reason\"." >&2
      exit 9
    fi
  elif [ -n "$sg_bad" ]; then
    echo "safe-apply: WARN [seat-gates] would stop under ENFORCE ($sg_bad ); WARN mode proceeds." >&2
  fi
  exit 0
) || SG_RC=$?
if [ "$SG_RC" -ne 0 ] && [ "$SG_RC" -ne 9 ]; then
  echo "safe-apply: WARN [seat-gates] the block errored (rc=$SG_RC); proceeding exactly as before." >&2
  SG_RC=0
fi
[ "$SG_RC" -eq 9 ] && exit 9
for sg_x in "$@"; do
  if [ "$sg_x" = "--dry-seat-gates" ]; then echo "safe-apply: --dry-seat-gates: the seat gates ran; nothing was applied." >&2; exit 0; fi
done

# HALTGT checkpoint -- fired immediately before the irreversible apply.
if [ -f "$HALT_GATE" ]; then
  # shellcheck source=/dev/null
  . "$HALT_GATE"
  halt_gate_check "safe-apply" || exit $?
else
  echo "safe-apply: ERROR -- halt-gate-check.sh not found at $HALT_GATE; refusing to apply ungated." >&2
  echo "safe-apply: the primary HALTGT net cannot run without its checkpoint library." >&2
  exit 3
fi

# -----------------------------------------------------------------------------
# THE NAMING LIMB, apply side (LGIC_ENFORCE cell EN-t-2; PRD candidate E8; DEC-6).
# ONE stage, placed after the halt checkpoint and BEFORE any plan: .tools/naming-apply-gate.py grades
# the own-name attribute of every top-level resource block in the tree's .tf files with
# lib/opal_naming.py grade(). A name the opal_name module would not produce (OUT-OF-PATTERN, ALIAS, or a
# RAISE) is a REFUSE verdict with the canonical printed; expressions are listed, not graded (their value
# exists only in a plan). Verdict lines go to org/mcp/naming-gate-verdicts.log (runtime, never committed).
# THE WARN WINDOW. ENFORCE is on only when org/mcp/naming-gate.enforce exists or NAMING_GATE_ENFORCE=1 --
# the commit limb's switch. In WARN mode this stage NEVER changes this script's exit code: not on a REFUSE
# verdict, not on the limb's own error (NAMING ERROR), not on a missing interpreter or a missing limb. In
# ENFORCE mode it is fail-closed: any non-zero exit stops here with exit 6, before terraform is called.
# THE SCOPED APPLY (cell MS-s-1, NFRA_MCPMSP round 2; the gate owner's ruling): an apply that names a -target, or
# a saved PLANFILE, runs a plan that is NOT the whole tree's -- so grading the whole tree's plan grades the wrong
# plan. For such a SCOPED apply the plan stage below renders the plan the apply runs (the caller's -target,
# -replace, -var, -var-file, -refresh and -destroy go to `plan`; a planfile is read with `show -json <planfile>`,
# never re-planned) and its verdict BINDS; the pre-plan stage (the tree's literals) is WARN only there; and a plan
# that cannot be rendered REFUSES in ENFORCE (exit 7). An UNSCOPED apply (no -target, no planfile) is unchanged.
# The caller's args are parsed once, here: everything after the first `apply` word.
SA_TARGETED=0; SA_PLANFILE=""; SA_PLAN_ARGS=()
sa_seen_apply=0; sa_pending=""
for arg in "$@"; do
  if [ "$sa_seen_apply" -eq 0 ]; then
    [ "$arg" = "apply" ] && sa_seen_apply=1
    continue
  fi
  if [ -n "$sa_pending" ]; then   # the value of a two-token flag (-target X, -var k=v, -parallelism 5, ...)
    [ "$sa_pending" = "forward" ] && SA_PLAN_ARGS+=("$arg")
    sa_pending=""
    continue
  fi
  case "$arg" in
    -target|--target)           SA_TARGETED=1; SA_PLAN_ARGS+=("$arg"); sa_pending=forward ;;
    -target=*|--target=*)       SA_TARGETED=1; SA_PLAN_ARGS+=("$arg") ;;
    -replace|--replace|-var|--var|-var-file|--var-file)
                                SA_PLAN_ARGS+=("$arg"); sa_pending=forward ;;
    -replace=*|--replace=*|-var=*|--var=*|-var-file=*|--var-file=*|-refresh|--refresh|-refresh=*|--refresh=*|-destroy|--destroy|-destroy=*|--destroy=*)
                                SA_PLAN_ARGS+=("$arg") ;;
    -parallelism|--parallelism|-lock-timeout|--lock-timeout|-state|--state|-state-out|--state-out|-backup|--backup)
                                sa_pending=skip ;;   # an apply-only flag that takes a separate value: not a planfile
    -*)                         : ;;
    *)                          [ -z "$SA_PLANFILE" ] && SA_PLANFILE="$arg" ;;
  esac
done
SA_SCOPED=0
if [ "$SA_TARGETED" -eq 1 ] || [ -n "$SA_PLANFILE" ]; then
  SA_SCOPED=1
fi

NAPPLY_GATE="$SCRIPT_DIR/naming-apply-gate.py"
NAPPLY_TREE="."
for arg in "$@"; do
  case "$arg" in
    -chdir=*) NAPPLY_TREE="${arg#-chdir=}" ;;
  esac
done
NAPPLY_ENFORCE=0
if [ "${NAMING_GATE_ENFORCE:-}" = "1" ] || [ -e "$SCRIPT_DIR/../org/mcp/naming-gate.enforce" ]; then
  NAPPLY_ENFORCE=1
fi
NAPPLY_OUT=""; NAPPLY_RC=0
if [ -f "$NAPPLY_GATE" ]; then
  NAPPLY_OUT="$(python "$NAPPLY_GATE" "$NAPPLY_TREE" 2>&1)" || NAPPLY_RC=$?
else
  NAPPLY_OUT="NAMING ERROR the safe-apply naming limb is absent at $NAPPLY_GATE"; NAPPLY_RC=2
fi
if [ "$NAPPLY_ENFORCE" -eq 1 ] && [ "$NAPPLY_RC" -ne 0 ] && [ "$SA_SCOPED" -eq 0 ]; then
  printf '%s\n' "$NAPPLY_OUT" | sed 's/^/  [naming-apply-gate] /' >&2
  echo "safe-apply: BLOCKED by the naming limb (LGIC_ENFORCE DEC-6, ENFORCE mode, rc=$NAPPLY_RC). Nothing was planned or applied." >&2
  exit 6
elif [ -n "$NAPPLY_OUT" ]; then
  printf '%s\n' "$NAPPLY_OUT" | sed 's/^/  [naming-apply-gate] /' >&2
  if [ "$SA_SCOPED" -eq 1 ] && [ "$NAPPLY_RC" -ne 0 ]; then
    echo "safe-apply: WARN -- the pre-plan naming stage (rc=$NAPPLY_RC) is WARN only for a targeted or planfile apply; the plan stage below decides." >&2
  fi
fi

# -----------------------------------------------------------------------------
# THE NAMING LIMB, apply side, PLAN MODE (LGIC_ENFORCE cell EN-t-2, round 2; DEC-6; row W3-S8).
# The pre-plan stage above cannot tell an ADDITION from an existing resource -- an apply has no diff, and that
# distinction lives only in a plan. This stage renders the SAME plan safe-apply is about to run (plan, then
# show -json) and grades it with naming-apply-gate.py --plan-json, BEFORE any other plan-reading gate
# (tag-authz, tombstone below) and before terraform apply itself -- so a REFUSE here means NOTHING further is
# planned or applied. Same WARN/ENFORCE switch as the commit limb and the pre-plan stage (NAPPLY_ENFORCE, set
# above). In WARN mode this stage never changes this script's exit code, exactly as the pre-plan stage above.
# MS-s-1: for a SCOPED apply (SA_SCOPED, above) the plan it renders carries the caller's -target/-replace/-var/
# -var-file/-refresh/-destroy args, or is the given planfile read with `show -json` (no re-plan), and a plan
# that cannot render REFUSES in ENFORCE (exit 7) rather than passing as a gap.
NPLAN_TMP="$(mktemp 2>/dev/null || echo "${TMPDIR:-/tmp}/safe-apply-naming-plan.$$")"
NPLAN_BLOCKED=0; NPLAN_RC=0; NPLAN_RENDERED=0
if [ -n "$SA_PLANFILE" ]; then
  "$TERRAFORM" ${NAPPLY_TREE:+-chdir="$NAPPLY_TREE"} show -json "$SA_PLANFILE" > "$NPLAN_TMP.json" 2>"$NPLAN_TMP.err" && NPLAN_RENDERED=1
elif [ "$SA_TARGETED" -eq 1 ]; then
  if "$TERRAFORM" ${NAPPLY_TREE:+-chdir="$NAPPLY_TREE"} plan -input=false -lock=false ${SA_PLAN_ARGS[@]+"${SA_PLAN_ARGS[@]}"} -out="$NPLAN_TMP.bin" >/dev/null 2>"$NPLAN_TMP.err" \
     && "$TERRAFORM" ${NAPPLY_TREE:+-chdir="$NAPPLY_TREE"} show -json "$NPLAN_TMP.bin" > "$NPLAN_TMP.json" 2>>"$NPLAN_TMP.err"; then
    NPLAN_RENDERED=1
  fi
elif "$TERRAFORM" ${NAPPLY_TREE:+-chdir="$NAPPLY_TREE"} plan -input=false -lock=false -out="$NPLAN_TMP.bin" >/dev/null 2>"$NPLAN_TMP.err" \
   && "$TERRAFORM" ${NAPPLY_TREE:+-chdir="$NAPPLY_TREE"} show -json "$NPLAN_TMP.bin" > "$NPLAN_TMP.json" 2>>"$NPLAN_TMP.err"; then
  NPLAN_RENDERED=1
fi
if [ "$NPLAN_RENDERED" -eq 1 ]; then
  if [ -f "$NAPPLY_GATE" ]; then
    NPLAN_OUT="$(python "$NAPPLY_GATE" --plan-json "$NPLAN_TMP.json" 2>&1)"; NPLAN_RC=$?
  else
    NPLAN_OUT="NAMING ERROR the safe-apply naming plan limb is absent at $NAPPLY_GATE"; NPLAN_RC=2
  fi
  printf '%s\n' "$NPLAN_OUT" | sed 's/^/  [naming-plan-gate] /' >&2
  if [ "$NAPPLY_ENFORCE" -eq 1 ] && [ "$NPLAN_RC" -ne 0 ]; then
    NPLAN_BLOCKED=1
  fi
else
  if [ "$SA_SCOPED" -eq 1 ] && [ "$NAPPLY_ENFORCE" -eq 1 ]; then
    NPLAN_BLOCKED=1; NPLAN_RC="unrenderable"
    echo "safe-apply: ERROR -- the naming plan limb could NOT render the plan this targeted or planfile apply runs for $NAPPLY_TREE; ENFORCE refuses (a plan that cannot render grades nothing)." >&2
  else
    echo "safe-apply: WARN -- the naming plan limb could NOT render a plan for $NAPPLY_TREE, so it checked NOTHING." >&2
    echo "            This is a GAP, not a pass; the pre-plan stage above still ran on the tree's literals." >&2
  fi
  if [ -s "$NPLAN_TMP.err" ]; then
    sed -e 's/^/  [naming-plan-gate] terraform: /' "$NPLAN_TMP.err" >&2
  fi
fi
rm -f "$NPLAN_TMP" "$NPLAN_TMP.bin" "$NPLAN_TMP.json" "$NPLAN_TMP.err" 2>/dev/null
if [ "$NPLAN_BLOCKED" -eq 1 ]; then
  echo "safe-apply: BLOCKED by the naming plan limb (LGIC_ENFORCE DEC-6, ENFORCE mode, rc=$NPLAN_RC). Nothing was planned further or applied." >&2
  exit 7
fi

# -----------------------------------------------------------------------------
# TAG-AUTHORIZATION pre-apply gate (comp-tagauthz), fail-closed.
# CTO 20260709T203543Z: "a tree that sets default_tags must gate imports on comp-tagauthz, wired into
# safe-apply, deriving its candidate set FROM THE PLAN." In this account tags ARE authorization
# (Project/System are both default_tags keys AND policy Condition keys), so an apply that shows only
# `~ tags` can SILENTLY REVOKE access -- and 0-diff is a claim about attributes, not authorization.
#
# Runs ONLY when: (a) the target tree sets a provider default_tags block, AND (b) comp-tagauthz exists.
# It plans the tree to JSON (read-only) and asks comp-tagauthz whether any aws_instance the plan would
# create/update carries an access-granting tag this tree's default_tags would overwrite.
#   rc 0 -> no collision, proceed.   rc 2 -> DANGER, block the apply.   rc 1 -> could-not-evaluate, BLOCK.
# Bypass (audited, for a plan the operator has hand-verified carries no tag-authz collision):
#   TAGAUTHZ_OVERRIDE="reason" .tools/safe-apply.sh ... apply ...
#
# KNOWN GAP (TOCTOU, accepted -- CTO 20260709T215515Z): the gate plans the tree, then the real apply
# re-plans it seconds later. A tag-authz collision that appears between the two is not caught. The
# window is seconds and the apply re-plans identically; closing it would mean the apply consuming the
# SAME saved planfile the gate checked, which rewrites this wrapper's caller contract. Deferred.
#
# DETECTOR CAVEAT: the default_tags detection below is a GREP -- a fast-path pre-filter to avoid the
# cost of a plan on ungated trees. A grep is a TEXT PROXY for the property, so its NEGATIVE is never
# proof: when it finds no default_tags it prints a LOUD SKIP stating how many files it scanned, so a
# silent-skip and a passed-gate cannot print the same nothing. The durable fix (not tonight) is to bind
# detection to `tags_all != tags` in the plan JSON the gate already fetches -- read off the artifact,
# not the source text.
# -----------------------------------------------------------------------------
CHDIR_TREE="."
for arg in "$@"; do
  case "$arg" in
    -chdir=*) CHDIR_TREE="${arg#-chdir=}" ;;
  esac
done
COMP_TAGAUTHZ="$SCRIPT_DIR/comp-tagauthz"

# Detect a PROVIDER default_tags block across BOTH .tf (HCL) AND .tf.json. Sets DT_FOUND (0/1) and
# DT_FILE_COUNT (the denominator). Over-detection is the SAFE direction (it merely runs the gate);
# a false NEGATIVE is the one that lets an apply through ungated, so the patterns are deliberately broad.
DT_FOUND=0
DT_FILE_COUNT=0
detect_default_tags() {
  local d="$1" f
  [ -d "$d" ] || { DT_FILE_COUNT=0; DT_FOUND=0; return; }
  local files=()
  for f in "$d"/*.tf "$d"/*.tf.json; do
    [ -f "$f" ] && files+=("$f")
  done
  DT_FILE_COUNT=${#files[@]}
  [ "$DT_FILE_COUNT" -eq 0 ] && { DT_FOUND=0; return; }
  # HCL: an anchored provider default_tags block (a leading-comment '# default_tags' cannot match).
  # JSON (.tf.json): the "default_tags" key. Either match across any file => present.
  if grep -lE '^[[:space:]]*default_tags[[:space:]]*\{' "${files[@]}" >/dev/null 2>&1 \
     || grep -l '"default_tags"' "${files[@]}" >/dev/null 2>&1; then
    DT_FOUND=1
  else
    DT_FOUND=0
  fi
}

detect_default_tags "$CHDIR_TREE"
if [ "$DT_FOUND" -eq 1 ]; then
  if [ -n "${TAGAUTHZ_OVERRIDE:-}" ]; then
    # -----------------------------------------------------------------------------------
    # RV-0047 F-001: TWO RECORDS -- INTENT here, OUTCOME after the apply returns.
    # The old line was written HERE and then the script `exec`d terraform, which REPLACES
    # the process -- so nothing after it could ever run. That is not an oversight in the
    # logging; it is the reason a single record was the only thing possible.
    #   *** AN AUDIT LOG WRITTEN BEFORE THE ACTION IS A CENSUS OF INTENTIONS. ***
    # It could say someone MEANT to bypass the tag-authz gate. It could never say whether
    # the apply then SUCCEEDED, FAILED, or was killed -- so a bypass that broke production
    # and a bypass that no-op'd are byte-identical in the record.
    # And it named no ACTOR at all (OPAL_AGENT_SERIAL x0 across .tools/*.sh at build time),
    # so "a second TAGAUTHZ bypass would be exactly as unattributable as the first" (MSTR).
    # -----------------------------------------------------------------------------------
    . "$SCRIPT_DIR/lib/resolve-actor.sh"
    AUDIT="$SCRIPT_DIR/../org/git-author-override-audit.log"
    TA_ACTOR="$(resolve_actor)"
    TA_ID="$(date -u +%Y%m%dT%H%M%SZ 2>/dev/null || echo UNKNOWN-TIME)-$$"
    printf '%s TAGAUTHZ_BYPASS-INTENT id=%s actor=%s safe-apply tree=%s reason=%s\n' \
      "$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo UNKNOWN-TIME)" \
      "$TA_ID" "$TA_ACTOR" "$CHDIR_TREE" "$TAGAUTHZ_OVERRIDE" \
      >> "$AUDIT" 2>/dev/null
    TAGAUTHZ_BYPASSED=1
    echo "safe-apply: TAGAUTHZ_OVERRIDE set -- tag-authz gate BYPASSED (audited: INTENT id=$TA_ID actor=$TA_ACTOR). reason: $TAGAUTHZ_OVERRIDE" >&2
    if [ "$TA_ACTOR" = "UNKNOWN" ]; then
      echo "safe-apply: WARN -- could not resolve the acting agent (no \$OPAL_AGENT_SERIAL, no session serial)." >&2
      echo "            The bypass is recorded as actor=UNKNOWN. An unattributable bypass is a gap, but it is" >&2
      echo "            an HONEST one -- we do NOT guess an actor from the shared .agent_context (it names the" >&2
      echo "            most-recently-STARTED agent, i.e. the innocent). See .tools/lib/resolve-actor.sh." >&2
    fi
  elif [ ! -x "$COMP_TAGAUTHZ" ] && ! command -v comp-tagauthz >/dev/null 2>&1; then
    echo "safe-apply: ERROR -- $CHDIR_TREE sets default_tags but comp-tagauthz is not available to gate it." >&2
    echo "safe-apply: in this account tags carry authorization; refusing to apply ungated. (Fail closed.)" >&2
    echo "safe-apply: install comp-tagauthz or, if you have hand-verified no tag-authz collision, re-run with" >&2
    echo "            TAGAUTHZ_OVERRIDE=\"reason\"." >&2
    exit 4
  else
    TAG_TMP="$(mktemp 2>/dev/null || echo "${TMPDIR:-/tmp}/safe-apply-plan.$$")"
    CTZ="$COMP_TAGAUTHZ"; [ -x "$CTZ" ] || CTZ="comp-tagauthz"
    echo "safe-apply: $CHDIR_TREE sets default_tags -- running the comp-tagauthz pre-apply authorization gate." >&2
    # stderr is CAPTURED, never discarded: the emptiness of this read carries a verdict
    # (fail-closed), and a discarded cause is why a missing binary reads as a dangerous plan.
    if "$TERRAFORM" ${CHDIR_TREE:+-chdir="$CHDIR_TREE"} plan -input=false -lock=false -out="$TAG_TMP.bin" >/dev/null 2>"$TAG_TMP.err" \
       && "$TERRAFORM" ${CHDIR_TREE:+-chdir="$CHDIR_TREE"} show -json "$TAG_TMP.bin" > "$TAG_TMP.json" 2>>"$TAG_TMP.err"; then
      "$CTZ" check --default-tags-tree "$CHDIR_TREE" --from-plan "$TAG_TMP.json" >&2
      rc=$?
      rm -f "$TAG_TMP" "$TAG_TMP.bin" "$TAG_TMP.json" "$TAG_TMP.err" 2>/dev/null
      if [ "$rc" -ne 0 ]; then
        echo "safe-apply: BLOCKED by comp-tagauthz (rc=$rc). This apply would overwrite an access-granting" >&2
        echo "            tag, or the gate could not evaluate. Route to CTO; do not TAGAUTHZ_OVERRIDE past a" >&2
        echo "            genuine DANGER. (rc 2 = collision, rc 1 = could-not-evaluate; both fail closed.)" >&2
        exit "$rc"
      fi
      echo "safe-apply: comp-tagauthz gate PASSED -- no plan resource overwrites an access-granting tag." >&2
    else
      echo "safe-apply: ERROR -- could not produce a plan JSON to run the tag-authz gate on $CHDIR_TREE." >&2
      echo "safe-apply: a gate that cannot evaluate must not pass. Refusing to apply. (Fail closed.)" >&2
      if [ -s "$TAG_TMP.err" ]; then
        echo "safe-apply: ---- terraform stderr (THE CAUSE -- read this before anything else) ----" >&2
        sed -e "s/^/            /" "$TAG_TMP.err" >&2
        echo "safe-apply: ------------------------------------------------------------------" >&2
      else
        echo "safe-apply: terraform produced NO stderr, which is itself the finding -- suspect the binary or the tree." >&2
      fi
      echo "safe-apply: THIS IS MOST OFTEN AN ENVIRONMENT FAULT, NOT A DANGEROUS PLAN -- a missing or wrong" >&2
      echo "            terraform, an uninitialised tree, or bad credentials. FIX THE CAUSE SO THE GATE RUNS." >&2
      echo "            SAFE_APPLY_TERRAFORM=/path/to/terraform makes the gate RUN; TAGAUTHZ_OVERRIDE makes it" >&2
      echo "            NOT RUN. Reach for the first. Do not bypass a gate to work around your own toolchain." >&2
      echo "safe-apply: TAGAUTHZ_OVERRIDE=\"reason\" is a LAST RESORT and is audited -- it is not the remedy for this error." >&2
      rm -f "$TAG_TMP" "$TAG_TMP.bin" "$TAG_TMP.json" "$TAG_TMP.err" 2>/dev/null
      exit 4
    fi
  fi
else
  # LOUD skip stating the denominator -- a grep's negative is not proof, so it must not look like a
  # passed gate (which prints nothing). If you believe a default_tags block exists here, this line is
  # the bug, not a clearance. (CTO amendment 1, 20260709T215515Z.)
  echo "safe-apply: SKIP tag-authz gate -- no provider default_tags block matched across ${DT_FILE_COUNT} .tf/.tf.json file(s) under ${CHDIR_TREE}." >&2
  if [ "${DT_FILE_COUNT}" -eq 0 ]; then
    echo "safe-apply: NOTE -- 0 .tf/.tf.json files found under ${CHDIR_TREE}; is -chdir=DIR correct? (detection scanned nothing to decide on.)" >&2
  fi
fi

# -----------------------------------------------------------------------------
# TOMBSTONE pre-apply gate -- block an apply that would RESURRECT a deleted resource.
# Andrew-direct "build the gate", 2026-07-30. Owner 0.7.0_AE_CloudOps.
#
# THE HAZARD (measured, 4 instances in one estate, 2026-07-30): a resource deleted OUT-OF-BAND
# -- by CLI/console rather than by removing its declaration -- leaves the declaration ARMED, and
# the next apply RECREATES it. Worst observed form: straight after a `terraform destroy`,
# `plan` read "20 to add" -- every resource gone, every one still declared.
#
# WHY THE PLAN ALONE CANNOT DECIDE: "deliberately deleted" and "new work not yet created" are
# byte-identical in a plan (both are `to add`). The record of INTENT is
# infra/aws/terraform/tombstones.json; the gate is that register joined to this plan.
#
# rc 0 -> clean.  rc 2 -> would resurrect, BLOCK.  rc 3 -> could-not-evaluate, BLOCK (fail-closed).
# Audited bypass: TOMBSTONE_OVERRIDE="reason" (logged to org/tombstone-gate-audit.log).
#
# SCOPE LIMIT, STATED SO SILENCE IS NEVER READ AS A PASS: this renders its own plan, exactly as
# the tagauthz gate above does, and inherits the same accepted TOCTOU window. If the tree cannot
# be planned, the gate says so LOUDLY and does not pretend to have checked.
TOMBSTONE_GATE="$SCRIPT_DIR/tombstone-gate.py"
TOMBSTONE_REG="$SCRIPT_DIR/../infra/aws/terraform/tombstones.json"
if [ -f "$TOMBSTONE_GATE" ] && [ -f "$TOMBSTONE_REG" ]; then
  TS_TMP="${TMPDIR:-/tmp}/safe-apply-tombstone-$$"
  if "$TERRAFORM" ${CHDIR_TREE:+-chdir="$CHDIR_TREE"} plan -input=false -lock=false -out="$TS_TMP.bin" >/dev/null 2>&1 \
     && "$TERRAFORM" ${CHDIR_TREE:+-chdir="$CHDIR_TREE"} show -json "$TS_TMP.bin" > "$TS_TMP.json" 2>/dev/null; then
    python "$TOMBSTONE_GATE" --plan-json "$TS_TMP.json" --register "$TOMBSTONE_REG" >&2
    TS_RC=$?
    rm -f "$TS_TMP.bin" "$TS_TMP.json"
    if [ "$TS_RC" -ne 0 ]; then
      echo "safe-apply: TOMBSTONE GATE BLOCKED this apply (rc=$TS_RC). Nothing was applied." >&2
      exit "$TS_RC"
    fi
  else
    rm -f "$TS_TMP.bin" "$TS_TMP.json"
    echo "safe-apply: WARN -- tombstone gate could NOT plan this tree, so it checked NOTHING." >&2
    echo "            This is a GAP, not a pass. Verify by hand that no resource in" >&2
    echo "            infra/aws/terraform/tombstones.json is about to be re-created." >&2
  fi
else
  echo "safe-apply: WARN -- tombstone gate or register missing; resurrection check DID NOT RUN." >&2
fi

# Checkpoint passed (empty inbox, or routine acked, or audited STOP override).
#
# RV-0047 F-001, the OUTCOME half. `exec` REPLACES this process -- nothing after it can ever
# run -- which is precisely why a bypass could only ever be recorded as an INTENT. So when a
# gate was BYPASSED we must NOT exec: we run terraform, capture its real exit code, write the
# OUTCOME record, and exit with that same code. The record then says what ACTUALLY HAPPENED,
# not merely what someone meant to do.
#
# The NON-bypass path is left EXACTLY as it was (exec, transparent exit code, zero new
# behaviour) -- there is nothing to correlate, and the common path should carry no new risk.
if [ "${TAGAUTHZ_BYPASSED:-0}" = "1" ]; then
  "$TERRAFORM" "$@"
  TA_RC=$?
  case "$TA_RC" in
    0) TA_RESULT=SUCCESS ;;
    *) TA_RESULT=FAILED ;;
  esac
  printf '%s TAGAUTHZ_BYPASS-OUTCOME id=%s actor=%s safe-apply tree=%s result=%s rc=%s\n' \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo UNKNOWN-TIME)" \
    "$TA_ID" "$TA_ACTOR" "$CHDIR_TREE" "$TA_RESULT" "$TA_RC" \
    >> "$AUDIT" 2>/dev/null
  echo "safe-apply: TAGAUTHZ bypass OUTCOME recorded (id=$TA_ID result=$TA_RESULT rc=$TA_RC)." >&2
  # An INTENT with no matching OUTCOME id = the apply was KILLED mid-flight. That asymmetry is
  # the point: it is now VISIBLE in the log instead of being indistinguishable from a clean run.
  exit "$TA_RC"
fi

# Delegate to terraform; exec propagates its exit code transparently.
exec "$TERRAFORM" "$@"
