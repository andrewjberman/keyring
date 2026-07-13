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
TERRAFORM="${SAFE_APPLY_TERRAFORM:-$SCRIPT_DIR/terraform.exe}"
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
    if "$TERRAFORM" ${CHDIR_TREE:+-chdir="$CHDIR_TREE"} plan -input=false -lock=false -out="$TAG_TMP.bin" >/dev/null 2>&1 \
       && "$TERRAFORM" ${CHDIR_TREE:+-chdir="$CHDIR_TREE"} show -json "$TAG_TMP.bin" > "$TAG_TMP.json" 2>/dev/null; then
      "$CTZ" check --default-tags-tree "$CHDIR_TREE" --from-plan "$TAG_TMP.json" >&2
      rc=$?
      rm -f "$TAG_TMP" "$TAG_TMP.bin" "$TAG_TMP.json" 2>/dev/null
      if [ "$rc" -ne 0 ]; then
        echo "safe-apply: BLOCKED by comp-tagauthz (rc=$rc). This apply would overwrite an access-granting" >&2
        echo "            tag, or the gate could not evaluate. Route to CTO; do not TAGAUTHZ_OVERRIDE past a" >&2
        echo "            genuine DANGER. (rc 2 = collision, rc 1 = could-not-evaluate; both fail closed.)" >&2
        exit "$rc"
      fi
      echo "safe-apply: comp-tagauthz gate PASSED -- no plan resource overwrites an access-granting tag." >&2
    else
      rm -f "$TAG_TMP" "$TAG_TMP.bin" "$TAG_TMP.json" 2>/dev/null
      echo "safe-apply: ERROR -- could not produce a plan JSON to run the tag-authz gate on $CHDIR_TREE." >&2
      echo "safe-apply: a gate that cannot evaluate must not pass. Refusing to apply. (Fail closed.)" >&2
      echo "safe-apply: if the plan genuinely carries no tag-authz collision, re-run with TAGAUTHZ_OVERRIDE=\"reason\"." >&2
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
