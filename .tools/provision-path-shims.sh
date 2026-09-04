#!/usr/bin/env bash
# provision-path-shims.sh -- NFRA_TOOLARCH.PATHFIX durable fix (0.8.0_AE_CloudComp~D, 2026-07-25).
#
# MECHANISM THIS FIXES (grounded, not inferred -- see the dispatch report for the full trace):
#   1. Every agent-harness Bash-tool call is `bash -c "<cmd>"` -- a NON-INTERACTIVE, NON-LOGIN
#      shell (`$-` carries no `i`; `BASH_ENV` unset). Per bash's own startup rules, a shell
#      invoked this way sources NEITHER ~/.bashrc NOR ~/.bash_profile/~/.profile. So the
#      `.tools` PATH line already written into ~/.bashrc:5 NEVER RUNS in the harness's actual
#      execution path -- only in a genuinely interactive terminal.
#   2. Even when ~/.bashrc IS sourced (a real interactive terminal), its PATH line reads
#      `/c/Users/.../.tools` -- the Git-Bash/MSYS mount convention. Under THIS machine's current
#      Cygwin-flavored bash, `/c` is not a mounted path at all (`ls /c` -> ENOENT; only
#      `/cygdrive/c` resolves) -- so even a sourced .bashrc adds a dead PATH entry.
#   3. PowerShell has the identical gap independently (`$env:PATH` carries no .tools entry
#      either) -- this is not a Cygwin-only defect.
#
# WHY ~/bin: it is ALREADY on PATH in every shell sampled (bash non-interactive, and PowerShell)
# despite not existing on disk and despite no profile file being sourced -- it is a persistent
# Windows USER-level PATH environment variable entry, inherited unconditionally by every child
# process on this machine regardless of shell flavor or interactivity. That is the one layer that
# actually reaches the harness's real invocation pattern; profile files structurally cannot.
#
# WHAT THIS SCRIPT DOES: writes small, single-purpose forwarding shims into ~/bin for the
# DERIVED FULL SET of .tools/comp-* (93 on disk) PLUS the named non-comp `aws` case
# -- both a bash-invocable form (no
# extension) and a PowerShell/cmd-invocable .cmd form, mirroring the existing .tools/aws +
# .tools/aws.cmd atomic-pair precedent (PATHEXT prefers .cmd under Windows shells; bash ignores
# it and uses the extensionless file). ALL LOGIC STAYS IN THE TRACKED .tools/ ORIGINALS -- these
# shims are dumb, absolute-path forwarders, never a second copy of any real logic.
#
# >> SCOPE -- WIDENED TO THE FULL DERIVED SET, 2026-07-28 (3.0.0_SA_CVO, Andrew-direct). This
# now provisions EVERY .tools/comp-* plus aws, with each tool's Windows interpreter READ FROM ITS
# OWN SHEBANG rather than hand-named. The historical caveat below is PRESERVED because the reasoning
# is still correct and still binding on any FUTURE narrowing -- but the specific claim it makes
# ("provisions 5 tools") is NO LONGER TRUE. Count from the run output, never from this prose.
#
# That distinction is not pedantry -- it is the exact defect this comment exists to prevent
# recurring. org/XXX.md Step 1b-A.3's startup check probes `comp-which` alone and an agent reads
# the result as a class-level "PATH is fine". Measured independently by two lanes on 2026-07-25
# (~C and ~D, separate sessions): the check PASSES and `comp-grep` is `command not found` on the
# very next call. The probe is ANTI-CORRELATED with the failure, because comp-which is the most
# likely member to be provisioned precisely by being the documented reflex. The script was
# correctly scoped; the CHECK generalized it. Do not let the script drift into the same
# overclaim -- when you add a tool, EXTEND THE NAMED LIST, never reword this to imply coverage.
#
# WHY comp-grep/comp-glob were added (CTO~Z 2026-07-25 171513Z) -- an operational break, not a
# cleanup: CLAUDE.md Rule 21's Gate-1 is ARMED and HARD-DENIES estate-scoped raw Bash grep/find/rg.
# The sanctioned alternative the rail names is comp-grep/comp-glob. Neither resolved. So the gate
# denied the raw search and handed the agent an escape hatch that was `command not found` -- the
# door real, the key not -- and comp-which's own output printed that dead fallback verbatim.
#
# RESOLVED 2026-07-28 (3.0.0_SA_CVO, Andrew-direct) -- the widening above. The blocker named here
# was per-tool shebang verification across the remaining tools; that is now MECHANICAL rather than
# manual: the loop reads each tool's own shebang and maps python->py.exe, bash->Git-Bash, and
# REPORTS-AND-SKIPS anything unmappable instead of guessing. Shebang census at widening time:
# 70 bash / 23 python across 93 tools, ZERO without a shebang.
#
# WHAT FORCED IT (an outage, not a cleanup): safe-commit.sh:483 guards its COMPUNIFY coverage gate
# on `command -v comp-coverage-check`. That tool was NOT in the named five, so the guard FAILED and
# THE GATE SILENTLY SKIPPED ON EVERY COMMIT. comp-manifest-check was in the same position. A gate
# that cannot be found is not advisory -- it is off, and it reports nothing while being off. <<
#
# THE aws CASE NEEDS EXTRA CARE: .tools/aws itself does `which -a aws` at runtime to find the
# REAL underlying pip-installed CLI, skipping any candidate matching `*/.tools/aws`. If a naive
# ~/bin/aws forwarder stayed importable as a PATH candidate named `aws` while .tools/aws ran its
# own self-discovery, .tools/aws could mistake ~/bin/aws for "the real aws" and exec it --
# which re-enters ~/bin/aws -> re-execs `aws` -> .tools/aws again -> infinite loop. Fixed by
# having ~/bin/aws strip ~/bin out of the PATH it hands down before re-invoking `aws` by name,
# so .tools/aws's own `which -a aws` search never sees this bootstrap shim as a candidate.
#
# IDEMPOTENT: safe to re-run (overwrites with identical content; a fresh agent session running
# this at startup is a no-op once another session already provisioned this machine).
#
# ROLLBACK: rm -rf ~/bin/{aws,aws.cmd,comp-which,comp-which.cmd,comp-system,comp-system.cmd} --
# every shell falls back to today's pre-fix state (the documented explicit-.tools/-prefix
# convention in CLAUDE.md still works regardless, unaffected by this script either way).
set -euo pipefail

WS="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WS_WIN="$(cygpath -w "$WS" 2>/dev/null || echo "$WS")"
BIN="$HOME/bin"
mkdir -p "$BIN"

# INHERITANCE RESTORE (NFRA_CLDGRPH-S26, 2026-09-04; 3.0.0_SA_CVO C-S1 @8fc3921769). On an ACL-emulating MSYS the
# chmod +x below is honoured by writing a PROTECTED explicit DACL with two DENY ACEs onto the file -- the exact state
# that denied a Codex seat every shim (S26; this seat's S29/S30). Measured: S30's reset left 0 of 211 protected and
# every forwarder worked all evening; the next provisioning run re-protected 105 of 211 within two seconds. So the
# mode write is followed by `icacls /reset` (default inherited ACLs), the state proven to work; the .cmd twins never
# needed it. Fail-open with a WARN naming the file -- a shim that exists with a bad DACL beats no shim; the DACL read
# at the end of the run prints the count either way. No-op where icacls is absent (a non-Windows host).
_restore_inheritance() {
  command -v icacls >/dev/null 2>&1 || return 0
  local _w
  _w="$(cygpath -w "$1" 2>/dev/null || echo "$1")"
  # MSYS_NO_PATHCONV: without it MSYS rewrites the /reset switch into "C:/Program Files/Git/reset" and icacls refuses
  # every file (measured at the first exercise: 105 of 211 still protected, one WARN per file). The variable is
  # scoped to this one call; it is the ARN/TF-import exemption CLAUDE.md names, on a Windows switch.
  MSYS_NO_PATHCONV=1 icacls "$_w" /reset >/dev/null 2>&1 || echo "WARN: icacls /reset failed on $1 -- its DACL may still carry a chmod's DENY ACEs (S26)"
}

echo "provision-path-shims: workspace=$WS  ~/bin=$BIN"

# ---- aws: PATH-strip-then-reinvoke, so .tools/aws's own self-discovery never sees this file ----
cat > "$BIN/aws" << EOF
#!/usr/bin/env bash
# Bootstrap shim (NFRA_TOOLARCH.PATHFIX) -- generated by .tools/provision-path-shims.sh, do not
# hand-edit; re-run that script instead. Strips ~/bin from PATH before re-invoking \`aws\` by
# name so .tools/aws's own "find the real aws, skip myself" search can never mistake THIS file
# for the real underlying CLI (which would otherwise loop: this file -> aws -> .tools/aws ->
# picks this file as "real" -> this file again).
#
# PATH-FLAVOR BUG FIXED 2026-07-29: this line used to strip a GENERATION-TIME string ("\$BIN",
# which expanded to /c/Users/<user>/bin) while PATH at RUN time carried the OTHER MSYS flavor
# (/cygdrive/c/Users/<user>/bin). String equality across two flavors of the same directory NEVER
# MATCHES, so the strip silently no-opped, the loop it exists to prevent fired, and every \`aws\`
# call in every agent shell died with a Python SyntaxError reading THIS bash file. Worse, the two
# halves of the same generated line disagreed with each other: \$WS came out cygdrive-flavored and
# \$BIN came out /c-flavored.
#
# THE FIX IS THE SAME ONE AS THE LAUNCHERS (LD-0344): resolve at RUN time from this file's OWN
# location, in whatever flavor the running shell uses, instead of baking a path string at
# generation time. \`cd ... && pwd\` returns the flavor the CURRENT shell understands by
# construction, so it matches its own PATH entry no matter which flavor that is.
_self_dir="\$(cd "\$(dirname "\${BASH_SOURCE[0]}")" 2>/dev/null && pwd)"
export PATH="\$(printf '%s' "\$PATH" | tr ':' '\n' | grep -Fxv "\$_self_dir" | paste -sd: -)"
# Prepend the workspace .tools ONLY if it resolves here. Baked (this file lives outside the repo
# and must point home somehow) but VERIFIED rather than assumed -- a stale or wrong-flavor bake
# now degrades to "use whatever aws is on PATH" instead of breaking every call.
if [ -x "$WS/.tools/aws" ]; then
  export PATH="$WS/.tools:\$PATH"
fi
exec aws "\$@"
EOF
chmod +x "$BIN/aws" || echo "WARN: chmod EINVAL on $BIN/aws (ACL-inherited fs; file is executable by ACL) -- continuing"
_restore_inheritance "$BIN/aws"

cat > "$BIN/aws.cmd" << EOF
@echo off
rem Bootstrap shim (NFRA_TOOLARCH.PATHFIX) -- generated by .tools\\provision-path-shims.sh, do
rem not hand-edit. Delegates directly to the tracked .tools\\aws.cmd by absolute path -- that
rem file already hardcodes the real python Scripts aws.cmd target with no self-discovery, so
rem there is no loop risk here (unlike the bash form above).
call "$WS_WIN\\.tools\\aws.cmd" %*
EOF

# ---- comp-which / comp-system: plain absolute-path forwarders, no self-discovery risk ----------
# .cmd form's interpreter MUST match each tool's actual shebang -- comp-which is
# `#!/usr/bin/env python3` (Python), comp-system is `#!/bin/bash` (bash). A bash script's
# content fed to python.exe (or vice versa) is not a slow failure, it is an immediate syntax
# error -- verified per-tool below, not assumed uniform.
declare -A _INTERP_WIN=(
    [comp-which]="py.exe"
    [comp-system]="\"C:\\Program Files\\Git\\bin\\bash.exe\""
    # comp-grep / comp-glob added 2026-07-25 (CTO~Z 171513Z). Both are `#!/usr/bin/env python3`
    # -- VERIFIED by reading their shebangs, not assumed from comp-which's. Same interpreter
    # class as comp-which, which is already exercised live, so this adds no new failure mode.
    [comp-grep]="py.exe"
    [comp-glob]="py.exe"
    # comp-find added 2026-08-05 (3.0.0_SA_CVO~B, NFRA_SCRIPTGEN Part B). Shebang READ, not assumed:
    # `#!/usr/bin/env python3`, same interpreter class as comp-grep/comp-glob which it unifies.
    [comp-find]="py.exe"
    # comp-read added 2026-08-06 (same Part B pair). Shebang READ: `#!/usr/bin/env python3`.
    [comp-read]="py.exe"
)

# --- DERIVED SET (3.0.0_SA_CVO 2026-07-28, Andrew-direct) -------------------------------------
# WAS: a hardcoded `for tool in comp-which comp-system comp-grep comp-glob`. THE NAMED SET WAS THE
# DEFECT. Measured this session: 4 of 92 comp-tools resolved bare, and BOTH commit-gate tools --
# comp-coverage-check and comp-manifest-check -- were outside the five. safe-commit.sh:483 guards
# its coverage gate on `command -v comp-coverage-check`, so the guard FAILED and THE GATE SILENTLY
# SKIPPED. A gate that cannot be found is not advisory, it is off.
#
# The interpreter is now DERIVED FROM EACH TOOL'S OWN SHEBANG, never assumed -- which is exactly
# why the set was hand-named before (the .cmd form has no shebang mechanism and must name the
# interpreter explicitly). Reading it per-tool removes the reason for the hand-list.
# Shebang census at authoring: 70 bash / 23 python across 93 tools, ZERO without a shebang.
# Anything unmappable is REPORTED AND SKIPPED LOUDLY -- never guessed, never silently dropped.
_GITBASH='"C:\\Program Files\\Git\\bin\\bash.exe"'
_unmapped=""
_derived=""
for _f in "$WS"/.tools/comp-*; do
    [ -f "$_f" ] || continue
    _t=$(basename "$_f")
    case "$_t" in *.cmd) continue;; esac
    _sb=$(head -1 "$_f" | tr -d '\r' | sed 's/[[:space:]]*$//')
    case "$_sb" in
        *python*) _INTERP_WIN[$_t]="py.exe" ;;
        *bash*)   _INTERP_WIN[$_t]="$_GITBASH" ;;
        *)        _unmapped="$_unmapped $_t"; continue ;;
    esac
    _derived="$_derived $_t"
done
if [ -n "$_unmapped" ]; then
    echo "provision-path-shims: UNMAPPED SHEBANG (skipped, NOT guessed):$_unmapped" >&2
fi

for tool in $_derived; do
    cat > "$BIN/$tool" << EOF
#!/usr/bin/env bash
# Bootstrap shim (NFRA_TOOLARCH.PATHFIX) -- generated by .tools/provision-path-shims.sh, do not
# hand-edit; re-run that script instead. All logic stays in the tracked .tools/$tool.
# \`exec\` performs a real execve, so the target's own shebang resolves the interpreter.
#
# BOTH-FLAVOR FALLBACK (added 2026-07-29). The baked prefix is whatever flavor the PROVISIONING
# shell used. At site Z a reboot killed LD-0340's volatile \`mount -f C: /c\`, and ALL 186
# forwarders -- every one baked against /c/... -- died at once. The comp rail was dead at the
# entrypoint and safe-commit's own hooks printed "No such file or directory" and let commits
# THROUGH: a live gate failing OPEN and SILENT.
#   GENERAL FORM: A NON-DURABLE FIX THAT GENERATES DURABLE ARTIFACTS PROPAGATES ITS OWN EXPIRY
#   INTO THEM. \`mount -f\` was correctly labelled "dies at reboot"; nobody labelled the
#   forwarders it had silently made conditional on itself.
# So: try the baked path, then the OTHER flavor. /cygdrive/c is a compiled-in default and is
# always present; /c exists only while something mounts it. Costs one \`[ -x ]\` per call.
_t="$WS/.tools/$tool"
if [ ! -x "\$_t" ]; then
  case "\$_t" in
    /c/*)        _alt="/cygdrive\${_t}" ;;
    /cygdrive/c/*) _alt="\${_t#/cygdrive}" ;;
    *)           _alt="" ;;
  esac
  [ -n "\$_alt" ] && [ -x "\$_alt" ] && _t="\$_alt"
fi
exec "\$_t" "\$@"
EOF
    chmod +x "$BIN/$tool" || echo "WARN: chmod EINVAL on $BIN/$tool (ACL-inherited fs; file is executable by ACL) -- continuing"
    _restore_inheritance "$BIN/$tool"

    cat > "$BIN/$tool.cmd" << EOF
@echo off
rem Bootstrap shim (NFRA_TOOLARCH.PATHFIX) -- generated by .tools\\provision-path-shims.sh, do
rem not hand-edit. Windows .cmd has no shebang mechanism, so the interpreter is named
rem explicitly and MUST match $tool's actual shebang (py.exe for python3, bash.exe for bash) --
rem never a bare \`bash\` (Windows would resolve that to the WSL stub, not Git Bash; this
rem workspace's own git_bash_resolver.py exists for exactly that hazard).
${_INTERP_WIN[$tool]} "$WS_WIN\\.tools\\$tool" %*
EOF
done

# Report what was ACTUALLY written, counted from disk -- never a hardcoded list. A hand-written
# summary drifts silently the moment the loop changes (this line said "aws comp-which comp-system"
# while the loop wrote 5 tools), and an output that under-reports its own scope is the same
# unstated-denominator defect this script's header is about.
_written=$(ls "$BIN" 2>/dev/null | grep -cv '\.cmd$')
echo "provision-path-shims: wrote $_written tool(s) x2 forms to $BIN -- $(ls "$BIN" | grep -v '\.cmd$' | tr '\n' ' ')"
echo "provision-path-shims: SCOPE = DERIVED from .tools/comp-* ($(ls "$WS"/.tools/comp-* 2>/dev/null | wc -l) on disk) + the named non-comp set. Interpreter per-tool from its OWN shebang."

# THE DACL READ (NFRA_CLDGRPH-S26, 2026-09-04): the number that names whether a Codex seat can resolve a shim. Every
# chmod above is followed by _restore_inheritance, so this prints 0 unless a chmod's DACL survived; a non-zero
# count is the finding, printed with its denominator, never hidden. Windows only; elsewhere the read is DECLARED-N/A.
if command -v powershell.exe >/dev/null 2>&1; then
  _prot="$(powershell.exe -NoProfile -Command "\$f=Get-ChildItem -File '$(cygpath -w "$BIN" 2>/dev/null || echo "$BIN")'; \$p=(\$f | Where-Object { (Get-Acl \$_.FullName).AreAccessRulesProtected }).Count; Write-Output \"\$p of \$(\$f.Count)\"" 2>/dev/null | tr -d '\r')"
  case "$_prot" in
    0\ of\ *) echo "provision-path-shims: DACL inheritance intact -- protected $_prot (S26 expects 0)" ;;
    "")       echo "provision-path-shims: WARN: the DACL read could not run (PowerShell answered nothing) -- protected count UNREAD" ;;
    *)        echo "provision-path-shims: WARN: protected $_prot files carry an explicit DACL (S26: a chmod's emulation survived; a Codex seat may be denied) -- run icacls /reset on them" ;;
  esac
else
  echo "provision-path-shims: DACL read DECLARED-N/A (no powershell.exe on this host)"
fi
