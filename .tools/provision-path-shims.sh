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
# ROLLBACK: restore ~/bin from a byte copy taken before the run, then re-run the PREVIOUS
# version of this script (`git show <ref>:.tools/provision-path-shims.sh`). The older note --
# "rm -rf ~/bin/{aws,comp-which,comp-system}..." -- NAMED SIX FILES WHILE THE LOOP WRITES TWO
# HUNDRED-PLUS, and deleting them does not restore anything: every shell then reaches NO
# comp-tool by bare name at all. A rollback that is a partial delete is not a rollback.
# Count the population from disk (`ls ~/bin | wc -l`), never from this prose.
set -euo pipefail

# THE BAKED FALLBACK MUST NAME A DURABLE TREE, AND THE RUNNING CHECKOUT IS NOT ONE.
# (0.9.0_WK_NFRA_COMPEFFICACY~2, NFRA_COMPEFFICACY CE-e-2, 2026-09-10.) This script used to bake
# whatever checkout happened to RUN it. Under spine v3 that checkout is usually a worker's LINKED
# WORKTREE under C:/tmp -- which the worker REMOVES when its order ends. Every forwarder on the
# box would then carry a fallback into a deleted directory, and the moment a caller stood outside
# any git worktree (no toplevel to resolve) it would get rc 127 from every comp-tool on this
# machine. That is the SAME DEFECT FAMILY this cell exists to fix -- a generated artifact bound to
# the tree that generated it -- one layer beneath the one the row named.
# So: RUN from anywhere, BAKE the MAIN worktree, DERIVED and never hardcoded
# (`git worktree list --porcelain` names the main worktree on its first line). Both are printed.
# The derived main path is Windows-form (C:/...), which is also strictly more durable than either
# MSYS flavor: /c exists only while something mounts it (LD-0340 died exactly that way at site Z).
WS_RUN="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WS="$(git -C "$WS_RUN" worktree list --porcelain 2>/dev/null | sed -n '1s/^worktree //p')"
if [ -z "$WS" ] || [ ! -d "$WS/.tools" ]; then
    echo "provision-path-shims: WARN: could not derive a main worktree from $WS_RUN -- baking the RUNNING checkout instead. If that checkout is temporary, every forwarder's fallback dies with it." >&2
    WS="$WS_RUN"
fi
WS_WIN="$(cygpath -w "$WS" 2>/dev/null || echo "$WS")"
BIN="$HOME/bin"
mkdir -p "$BIN"

# INHERITANCE RESTORE (NFRA_CLDGRPH-S26, 2026-09-04; 3.0.0_SA_CVO C-S1 @8fc3921769). On an ACL-emulating MSYS the
# chmod +x below is honoured by writing a PROTECTED explicit DACL with two DENY ACEs onto the file -- the exact state
# that denied a Codex seat every shim (S26; this seat's S29/S30). Measured: S30's reset left 0 of 211 protected and
# every forwarder worked all evening; the next provisioning run re-protected 105 of 211 within two seconds. So the
# mode write is followed by `icacls /reset` (default inherited ACLs), the state proven to work.
#
# CORRECTED 2026-09-10 (0.9.0_WK_NFRA_COMPEFFICACY~2, NFRA_COMPEFFICACY CE-e-2, row W2-S5). THIS BLOCK USED TO SAY 'the
# .cmd twins never needed it' AND THAT WAS BACKWARDS -- THE .cmd TWINS ARE THE ONLY ONES THAT DO. Measured by
# dry-running this script into a scratch HOME before the live run: 105 of 210 files came out with a protected
# DACL and EVERY ONE OF THEM WAS A .cmd (aws.cmd, comp-adversary.cmd, comp-arity.cmd, ...); the chmod'd
# extensionless forwarders all read AreAccessRulesProtected=False because _restore_inheritance already ran on
# them. The count 105 the header cites is therefore the .cmd plane, not the chmod plane, and the count matches
# the twin population exactly. That also matches the standing note that a ~/bin shim denied to a Codex seat is
# broken ACL inheritance ON THE .cmd PLANE. So _restore_inheritance is now called on the twin as well: without
# it, EVERY RUN OF THIS SCRIPT TAKES THE FLEET FROM 0 PROTECTED TO 105 -- measured live pre-run 0 of 211.
# Fail-open with a WARN naming the file -- a shim that exists with a bad DACL beats no shim; the DACL read
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

echo "provision-path-shims: RUNNING FROM $WS_RUN"
echo "provision-path-shims: BAKING (durable fallback + tool census) $WS  ~/bin=$BIN"

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
#
# CALLER-TOPLEVEL RESOLUTION (NFRA_COMPEFFICACY CE-e-2, 2026-09-10, row W1-S2). Same rule as the
# comp-* forwarders: prepend the CALLER'S OWN .tools when it carries an aws wrapper, so a seat
# editing .tools/aws in a linked worktree exercises the file it changed rather than the
# provisioning tree's. The baked prefix stays as the fallback -- this file lives outside the repo
# and must point home somehow -- but it is VERIFIED rather than assumed, and a fallback SAYS SO
# on stderr. NO NEW LOOP RISK: .tools/aws's own "find the real aws, skip myself" search skips any
# candidate matching */.tools/aws, which is true of the caller's copy exactly as it was of the
# baked one.
_aws_baked_tools="$WS/.tools"
_git_out="\$(git rev-parse --show-toplevel 2>&1)"; _git_rc=\$?
_aws_tools=""
if [ \$_git_rc -eq 0 ] && [ -n "\$_git_out" ] && [ -x "\$_git_out/.tools/aws" ]; then
  _aws_tools="\$_git_out/.tools"
elif [ -x "\$_aws_baked_tools/aws" ]; then
  _aws_tools="\$_aws_baked_tools"
  printf '%s\n' "WARN: aws: no caller-toplevel .tools/aws (git rc=\$_git_rc) -- PREPENDING THE BAKED \$_aws_tools instead (run: aws --which)" >&2
else
  printf '%s\n' "WARN: aws: neither a caller-toplevel nor the baked \$_aws_baked_tools carries an aws wrapper -- DEFERRING TO WHATEVER aws IS ON PATH (run: aws --which)" >&2
fi

if [ "\${1-}" = "--which" ]; then
  if [ -n "\$_aws_tools" ]; then printf '%s\n' "\$_aws_tools/aws"; else printf '%s\n' "(none -- this shim would exec whatever aws is on PATH)"; fi
  exit 0
fi

[ -n "\$_aws_tools" ] && export PATH="\$_aws_tools:\$PATH"
exec aws "\$@"
EOF
chmod +x "$BIN/aws" || echo "WARN: chmod EINVAL on $BIN/aws (ACL-inherited fs; file is executable by ACL) -- continuing"
_restore_inheritance "$BIN/aws"

# CRLF, deliberately: see the goto note inside. sed adds the CR the heredoc does not.
sed 's/$/\r/' > "$BIN/aws.cmd" << EOF
@echo off
setlocal EnableExtensions
rem Bootstrap shim (NFRA_TOOLARCH.PATHFIX) -- generated by .tools\\provision-path-shims.sh, do
rem not hand-edit. Delegates directly to the tracked .tools\\aws.cmd by absolute path -- that
rem file already hardcodes the real python Scripts aws.cmd target with no self-discovery, so
rem there is no loop risk here (unlike the bash form above).
rem CALLER-TOPLEVEL RESOLUTION (NFRA_COMPEFFICACY CE-e-2): resolve the CALLER'S git toplevel
rem first, fall back to the baked path and SAY SO on stderr, and answer --which.
set "SHIM_BAKED=$WS_WIN\\.tools\\aws.cmd"
set "SHIM_TARGET=%SHIM_BAKED%"
set "SHIM_TOP="
for /f "usebackq delims=" %%i in (\`git rev-parse --show-toplevel 2^>nul\`) do set "SHIM_TOP=%%i"
if not defined SHIM_TOP goto _shim_no_top
if exist "%SHIM_TOP%\\.tools\\aws.cmd" goto _shim_use_top
echo WARN: aws.cmd: the caller toplevel %SHIM_TOP% carries no .tools\\aws.cmd -- CALLING THE BAKED PATH %SHIM_BAKED% instead ^(run: aws --which^) 1>&2
goto _shim_resolved
:_shim_no_top
echo WARN: aws.cmd: no git toplevel at %CD% -- CALLING THE BAKED PATH %SHIM_BAKED% instead ^(run: aws --which^) 1>&2
goto _shim_resolved
:_shim_use_top
set "SHIM_TARGET=%SHIM_TOP%\\.tools\\aws.cmd"
:_shim_resolved
rem SINGLE-LINE STATEMENTS ONLY, CRLF-written -- see the comp-* twin for the measurement.
rem BRACKET COMPARISON, NOT "%~1" -- a MEASURED choice, not a style. %~1 strips only the OUTER
rem quote pair, so an argument that reaches this file with DOUBLED quotes (a bash caller doing
rem cmd.exe /c "..." does exactly that) leaves an ODD number of quotes, and "%~1"=="--which"
rem then expands to an unbalanced comparison that cmd refuses with "<word> was unexpected at
rem this time" -- measured on comp-which.cmd "what produces canonical prices". [%1] adds no
rem quotes, so the token stays balanced whatever it holds and the compare is false, not fatal.
if /i [%1]==[--which] goto _shim_which
call "%SHIM_TARGET%" %*
exit /b %ERRORLEVEL%
:_shim_which
echo %SHIM_TARGET%
exit /b 0
EOF
_restore_inheritance "$BIN/aws.cmd"

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
# CALLER-TOPLEVEL RESOLUTION (NFRA_COMPEFFICACY CE-e-2, 2026-09-10, on round-7 row W1-S2).
# THE DEFECT THIS REPLACES: this file used to point ONLY at a path baked into whichever tree
# provisioned it. Spine v3 puts every worker in a LINKED WORKTREE (CLAUDE.md 14b), so a worker
# that edited .tools/$tool in its worktree and verified it BY THE BARE NAME ran the provisioning
# tree's copy -- THE FILE IT DID NOT CHANGE -- and the run succeeded, printed a plausible answer
# and returned rc 0. The wrong-object result and the correct result are byte-identical and
# nothing in the output said which file answered. That is a FALSE GREEN, and it is invisible.
# SO: resolve the CALLER'S own git toplevel first and exec ITS .tools/$tool when that exists;
# fall back to the baked path otherwise AND SAY SO ON STDERR. A SILENT fallback would rebuild
# the same defect one layer down -- the caller still could not tell which file answered.
# --which prints the absolute target this shim would exec, and exits 0 without running it.
# COST: one \`git rev-parse --show-toplevel\` per invocation. NON-APPLICATION: none -- the
# resolution IS the point, and the tools it fronts each cost far more than the rev-parse.
_baked="$WS/.tools/$tool"

# BOTH-FLAVOR FALLBACK for the BAKED path (added 2026-07-29; reasoning unchanged and still
# binding). The baked prefix is whatever flavor the PROVISIONING shell used. At site Z a reboot
# killed LD-0340's volatile \`mount -f C: /c\` and ALL forwarders -- every one baked against
# /c/... -- died at once; safe-commit's own hooks printed "No such file or directory" and let
# commits THROUGH: a live gate failing OPEN and SILENT. /cygdrive/c is a compiled-in default and
# is always present; /c exists only while something mounts it.
#   GENERAL FORM: A NON-DURABLE FIX THAT GENERATES DURABLE ARTIFACTS PROPAGATES ITS OWN EXPIRY
#   INTO THEM.
_shim_flavor() {
  if [ -x "\$1" ]; then printf '%s' "\$1"; return 0; fi
  case "\$1" in
    /c/*)          [ -x "/cygdrive\$1" ] && { printf '%s' "/cygdrive\$1"; return 0; } ;;
    /cygdrive/c/*) [ -x "\${1#/cygdrive}" ] && { printf '%s' "\${1#/cygdrive}"; return 0; } ;;
  esac
  printf '%s' "\$1"
  return 1
}

# The toplevel read KEEPS its rc AND its stderr. An empty answer here carries a VERDICT -- which
# file is about to answer -- and CLAUDE.md rule 16 forbids sending a verdict-bearing read to
# /dev/null. Both are reported in the fallback line below.
_git_out="\$(git rev-parse --show-toplevel 2>&1)"; _git_rc=\$?
if [ \$_git_rc -eq 0 ] && [ -n "\$_git_out" ] && [ -x "\$_git_out/.tools/$tool" ]; then
  _t="\$_git_out/.tools/$tool"
elif [ \$_git_rc -eq 0 ] && [ -n "\$_git_out" ]; then
  _t="\$(_shim_flavor "\$_baked")"
  printf '%s\n' "WARN: $tool: the caller toplevel \$_git_out carries no .tools/$tool -- EXECUTING THE BAKED PATH \$_t instead (run: $tool --which)" >&2
else
  _t="\$(_shim_flavor "\$_baked")"
  printf '%s\n' "WARN: $tool: no git toplevel at \$PWD (git rc=\$_git_rc: \$_git_out) -- EXECUTING THE BAKED PATH \$_t instead (run: $tool --which)" >&2
fi

if [ "\${1-}" = "--which" ]; then
  printf '%s\n' "\$_t"
  exit 0
fi

if [ ! -x "\$_t" ]; then
  printf '%s\n' "ERROR: $tool: no executable target -- neither the caller toplevel nor the baked path \$_baked resolves .tools/$tool" >&2
  exit 127
fi
exec "\$_t" "\$@"
EOF
    chmod +x "$BIN/$tool" || echo "WARN: chmod EINVAL on $BIN/$tool (ACL-inherited fs; file is executable by ACL) -- continuing"
    _restore_inheritance "$BIN/$tool"

        # CRLF, deliberately: see the goto note inside.
    sed 's/$/\r/' > "$BIN/$tool.cmd" << EOF
@echo off
setlocal EnableExtensions
rem Bootstrap shim (NFRA_TOOLARCH.PATHFIX) -- generated by .tools\\provision-path-shims.sh, do
rem not hand-edit. Windows .cmd has no shebang mechanism, so the interpreter is named
rem explicitly and MUST match $tool's actual shebang (py.exe for python3, bash.exe for bash) --
rem never a bare \`bash\` (Windows would resolve that to the WSL stub, not Git Bash; this
rem workspace's own git_bash_resolver.py exists for exactly that hazard).
rem
rem CALLER-TOPLEVEL RESOLUTION (NFRA_COMPEFFICACY CE-e-2, 2026-09-10, row W1-S2) -- THE SAME RULE
rem AS THE BASH TWIN, AND IT IS NOT OPTIONAL HERE. A PowerShell or cmd caller standing in a
rem linked worktree otherwise runs the provisioning tree's copy: the file it did not change,
rem returning rc 0 with a byte-identical answer. Fixing only the bash plane would leave the
rem defect alive on the plane PowerShell uses, which is the primary shell on this box.
rem Resolve the CALLER'S git toplevel first; fall back to the baked path and SAY SO on stderr;
rem answer --which with the absolute target.
set "SHIM_BAKED=$WS_WIN\\.tools\\$tool"
set "SHIM_TARGET=%SHIM_BAKED%"
set "SHIM_TOP="
for /f "usebackq delims=" %%i in (\`git rev-parse --show-toplevel 2^>nul\`) do set "SHIM_TOP=%%i"
if not defined SHIM_TOP goto _shim_no_top
if exist "%SHIM_TOP%\\.tools\\$tool" goto _shim_use_top
echo WARN: $tool: the caller toplevel %SHIM_TOP% carries no .tools\\$tool -- EXECUTING THE BAKED PATH %SHIM_BAKED% instead ^(run: $tool --which^) 1>&2
goto _shim_resolved
:_shim_no_top
echo WARN: $tool: no git toplevel at %CD% -- EXECUTING THE BAKED PATH %SHIM_BAKED% instead ^(run: $tool --which^) 1>&2
goto _shim_resolved
:_shim_use_top
set "SHIM_TARGET=%SHIM_TOP%\\.tools\\$tool"
:_shim_resolved
rem SINGLE-LINE STATEMENTS ONLY BELOW, AND THIS FILE IS WRITTEN CRLF -- both are load-bearing.
rem A .cmd emitted with LF-only endings (which a bash heredoc does by default, and which every
rem earlier version of this twin had) survives while every line is a lone command, and BREAKS the
rem moment a multi-line \`if (...)\` block or a goto label is introduced: measured on the first
rem exercise of this shim, \`comp-which.cmd "what produces canonical_prices.parquet?"\` answered
rem "produces was unexpected at this time." while \`--which\` on the same file worked. So the
rem block form is replaced by a goto and the heredoc is piped through sed to add the CR.
rem BRACKET COMPARISON, NOT "%~1" -- a MEASURED choice, not a style. %~1 strips only the OUTER
rem quote pair, so an argument that reaches this file with DOUBLED quotes (a bash caller doing
rem cmd.exe /c "..." does exactly that) leaves an ODD number of quotes, and "%~1"=="--which"
rem then expands to an unbalanced comparison that cmd refuses with "<word> was unexpected at
rem this time" -- measured on comp-which.cmd "what produces canonical prices". [%1] adds no
rem quotes, so the token stays balanced whatever it holds and the compare is false, not fatal.
if /i [%1]==[--which] goto _shim_which
${_INTERP_WIN[$tool]} "%SHIM_TARGET%" %*
exit /b %ERRORLEVEL%
:_shim_which
echo %SHIM_TARGET%
exit /b 0
EOF
    # THE TWIN NEEDS THE RESET TOO -- and only the twin comes out protected (see the
    # _restore_inheritance header). Without this line every run of this script moves the
    # fleet from 0 protected to one-per-tool, which is S26 re-armed by the fix itself.
    _restore_inheritance "$BIN/$tool.cmd"
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
