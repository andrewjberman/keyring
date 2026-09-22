# AMGT_RESAPP task order -- `AMGT-rk-95` -- never-rules-gate GATE 5 resolves the target repo from a QUOTED `git -C` / `cd` argument WHOLE (double or single quotes) and treats a Windows drive path `[A-Za-z]:/` or `[A-Za-z]:\` as ABSOLUTE, so a quoted, space-containing worktree path is judged against that worktree; a PARSER fix to an existing gate that narrows false denials and adds NO refusal

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-95</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~95</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one PreToolUse hook script and its test suite; it arms no
  cron, alarm, monitor or cadence, reads no schedule and writes none, and the edited hook is not wired anywhere new
  (the harness already runs it; the edit takes effect only when the branch drains).
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant is read or changed; no AWS call of any kind is made
  (every gate verdict is taken on a SYNTHETIC payload piped to the hook on stdin; nothing is pushed or pulled).
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~95`.** Work ONLY in the worktree whose absolute path is given in your spawn
prompt. Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`org/`, `.tools/` and the paths in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~95;`. **NEVER RUN AN INSTALL.** Never read, show, diff or check out
branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential. **NEVER run a real `git push` or
`git pull`.** Every gate verdict in this order is a synthetic JSON payload piped to the hook.

## 1. THE CELL, inlined in full -- `AMGT-rk-95` (round 23, second cell; row `AMGT_RESAPP-Z-S209`)

**The ruling, verbatim (`ledger/ROUND_ANALYSIS.round22.md` @ace3f7ca38, `1.0.0_SA_CTO~Z`), `:36-46`:**
*"**Z-S209 (gate owner): `never-rules-gate.sh` GATE 5 resolves the target repo with a no-whitespace pattern**
(`:286-303` @HEAD). A quoted path containing a space is cut at the space, and a quoted Windows-drive path (`C:/...`)
fails the `/*)` absolute test, so it is taken as relative. On this box that denies a DT's PROD push from a quoted
worktree path. The failure is fail-closed; the workaround is the relative form, measured twice.
- **ROUND 23, SECOND CELL, a tooling cell:** parse a double- or single-quoted `git -C` / `cd` argument whole, and
treat `[A-Za-z]:/...` as absolute.
- Criteria: a quoted space-containing worktree path resolves to that worktree; the relative form is unchanged; and
**a negative control, a shared-branch push from the workspace repo, is still DENIED.**
- The gate's own false-positive test (`.tools/comprail-gate1-fptest.sh`'s pattern, or a new fixture script) runs
before the commit.
- It is a fix to an existing mechanical gate's parser, NOT a new gate. It narrows false denials and adds no
refusal."* **`:52`:** *"2. **The GATE 5 parser fix (S209)**, tooling, with a negative control."* The covering
message (msg 24153): *"GATE 5 PARSER FIX (Z-S209), a tooling cell in .tools/hooks/never-rules-gate.sh :286-303 ...
It is a parser fix to an existing gate, not a new gate. It narrows false denials and adds no refusal."*

**The row this cell answers, `AMGT_RESAPP-Z-S209`** (filed by `0.2.0_DT_PortfolioAnalytics` at the `AMGT-rk-89` PROD
promote): GATE 5 cut a quoted `git -C` / `cd` path at the space in this box's path, so the DT's PROD push from the
absolute worktree path was DENIED; the space-free relative `git -C .runtmp/<wt> push origin PROD` was admitted, with
no override used.

**THE MEASURED STATE, at HEAD `ace3f7ca38` (SITEZ). RE-READ every line below at your branch HEAD before editing:**
- `.tools/hooks/never-rules-gate.sh`: 644 lines, 50,182 bytes, CRLF 0, non-ASCII bytes 0. **Last changed @`e58250f261`**
  (`git log --format=%H -1 -- .tools/hooks/never-rules-gate.sh` = `e58250f2615069d8f59160e9762f721e71a28bdb`), and
  HEAD's copy is byte-equal to it. That commit is this order's PIN for every before/after comparison (Z-S193: a pinned
  hash, never HEAD or a merge-base).
- **PARSE-SITE CENSUS (by subtraction).** Every line of the hook that extracts a `git -C <path>` or a `cd <path>`
  argument: 2 detector lines (`:286`, `:297`) and 2 extractor lines (`:287`, `:298`), forming exactly **2 parse sites**:
  - SITE A, `:286-291` (`git -C`): the detector requires `-C[[:space:]]+[^[:space:]]+`; the extractor
    `sed ... 's/.*git[[:space:]]\+-C[[:space:]]\+\([^[:space:]]\+\).*/\1/p'` takes the first NON-WHITESPACE run, so
    `"C:/Users/Opal Bloomberg/..."` becomes `"C:/Users/Opal` (quote character INCLUDED); then `case "$_c" in /*)
    REPO="$_c" ;; *) REPO="$WS/$_c" ;;` treats a drive path, and any quote-prefixed token, as RELATIVE.
  - SITE B, `:297-303` (`cd <path> &&`/`;`): the same shape, extractor class `[^[:space:];&|]`, and the same `/*)`
    absolute test, and the same quote-inclusion.

  The other `git -C` mentions are NOT path extractors, and this order does not edit them:
  - `_O2` (`:~345`) consumes `-C <token>` for VERB MATCHING in `_GIT`.
  - `:532` (`_g3_c`) is GATE 3's token attribution, an unrelated variable of the same name family.
- **The defect, measured on the pinned hook with `probe_s209.sh` (AC0's file, synthetic payloads, caller
  `0.2.0_DT_PortfolioAnalytics`, workspace = the MAIN checkout):** P1 (relative `git -C portal push origin PROD`) =
  PASS; P2 double-quoted forward-slash absolute = DENY; P3 single-quoted = DENY; P4 double-quoted backslash = DENY;
  P5 `cd "<abs>/portal" && git push origin PROD` = DENY; negatives N1-N4 = DENY. **4 false denials, 0 false admits.**
- **The existing suite `.tools/hooks/tests/test_never_rules_gate.sh`** (447 lines, CRLF 0, non-ASCII bytes 1 -- a
  pre-existing byte, leave it) reads **PASS: 96 FAIL: 0** on the main checkout at HEAD (more than 2 minutes per run).
  Its DT carve-out block is at `:393-427` (`check_as` at `:407`).
- **WORKTREE CAVEAT (measured):** in a linked worktree, `portal/` is an UNINITIALISED gitlink directory, and
  `git -C <worktree>/portal` walks UP to the worktree repo (origin = ajb_workspace, not portal). Run in your
  worktree with the payload carrying no cwd, the hook sets `WS` to your worktree and the suite's portal arms FAIL
  for an environmental reason. **So every suite and probe run in this order sets `CLAUDE_PROJECT_DIR` to the MAIN
  checkout root** -- derived, never typed: `dirname "$(git rev-parse --path-format=absolute --git-common-dir)"` --
  and runs the suite FROM that directory, while the HOOK under test is still YOUR worktree's file (the suite's
  `HOOK` resolves relative to its own path). This is read-only toward the main checkout: the suite routes its audit
  writes to a temp file (`NEVER_GATE_AUDIT`), and the probe sends them to `/dev/null`.
- **LANE:** `.tools/hooks/**` has no rule of its own; it resolves to `.tools/**` = lane `ANY` (`.owned-paths.yaml`
  `:2026`), and a worker serial is admitted to exactly this order's `<paths>`. There is no lane blocker.
- **Path handling measured on this box:** both `[ -d "C:/.../portal" ]` and `[ -d "C:\...\portal" ]` are true, and
  `git -C` accepts both forms. `git rev-parse --show-toplevel` already prints the drive form with a space
  (`C:/Users/Opal Bloomberg/Desktop/ajb_workspace`).

**RULED, what you build:**
1. **SITES A and B parse a quoted argument WHOLE.** If the token after `-C` (SITE A) or after `cd` (SITE B) begins
   with `"`, the argument runs to the next `"`; if it begins with `'`, to the next `'`; the quotes are STRIPPED from
   the value. An unquoted token keeps TODAY'S extraction byte-for-byte (the relative and unquoted absolute forms
   must be unchanged -- AC4 proves it over the whole suite). An unterminated quote extracts nothing (REPO keeps its
   prior value), which is fail-closed, as today.
2. **A Windows drive path is ABSOLUTE.** The absolute test in both sites admits `/*` (as today) OR a value matching
   `^[A-Za-z]:[/\\]`. SITE B keeps its existing `.git` existence check for absolute values exactly as today.
3. **Nothing else in the hook changes.** GATE 5's DT carve-out (the caller is DT, the branch is PROD/DEV, the
   origin is portal, the verb is push), the integrator test, every deny text, `_GIT`/`_O2`, and GATES 1-4 stay
   byte-identical outside `:286-303`. A NEW refusal anywhere is a defect of this cell (AC4).
4. **Tests.** Append to the suite's DT carve-out block (after `:427`) exactly these 10 `check_as` arms, with every
   path DERIVED at run time -- `_NRG_ROOT="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel)}"`,
   `_NRG_M="$(cygpath -m "$_NRG_ROOT")"`, `_NRG_W="$(cygpath -w "$_NRG_ROOT")"` -- never a typed path (CLAUDE.md:
   derive, don't hardcode):
   - PASS: DT (`0.4.0_DT_ClientPlatform~Z`, the suite's DT serial) `git -C "<M>/portal" push origin PROD`;
   - PASS: DT `git -C '<M>/portal' push origin PROD`;
   - PASS: DT `git -C "<W>\portal" push origin PROD`;
   - PASS: DT `cd "<M>/portal" && git push origin PROD`;
   - PASS: DT `cd '<M>/portal' && git push origin PROD`;
   - DENY: DT `git -C "<M>" push origin CLOUD` (the negative control: a shared-branch push from the workspace repo);
   - DENY: DT `cd "<M>" && git push origin CLOUD`;
   - DENY: `1.0.0_SA_CTO~Z` `git -C "<M>/portal" push origin PROD` (non-DT on portal PROD);
   - DENY: DT `git -C "<M>/no such dir" push origin PROD` (a quoted missing path fails closed);
   - PASS: `0.0.0_AB_MSTR~Z` `git -C "<M>" push origin CLOUD` (the integrator is unaffected).

   Name each arm with the prefix `S209:`. The suite then reads 106 arms.

**What this cell does NOT change:** any other gate, any deny text, `.claude/settings.json`, the hook wiring,
`.tools/comprail-gate1-fptest.sh`, `/prod-deploy`, or any lane. The DT carve-out's three-way scope is untouched.

## 2. WHERE THIS CAME FROM

**ROUND 23**, decomposition s.31 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s round-22 analysis
`ledger/ROUND_ANALYSIS.round22.md` @ace3f7ca38 (s.2 `:36-46`, s.3 `:52`), sent as msg 24153. Row
`AMGT_RESAPP-Z-S209`, filed by `0.2.0_DT_PortfolioAnalytics` at `AMGT-rk-89`'s portal v2.1.182 PROD promote.
Andrew-direct ~15:12Z (record @1e2a54bf0f) governs the one-slug issuance.

## 3. SURFACES -- what you may read and write

<paths>
.tools/hooks/never-rules-gate.sh
.tools/hooks/tests/test_never_rules_gate.sh
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~95/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-95.gate5-quoted-path-parser.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant. Scratch is `<your worktree>/.scratch/r95/`
  only (never committed); the three scripts below are written THERE, from this order's text verbatim.
- **Collision check, done at the cut:** round 23's other cell `AMGT-rk-94` (the print fix) writes
  `lib/research/print/render_pack.py`, its tests, and the adapter build/deploy surfaces. **There is zero file
  overlap.** The held branch `wk-amgt-14-50` touches no path here (names only). The only shared file is
  `INVESTIGATION_v1.md` (append-only; do not isolate it).
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~95 <0.9.0_WK_AMGT_RESAPP~95@opal.agent>" -F <msgfile> -- <paths>`
  (message file written by the Write tool). Never push, merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**NO LIVE ACT: no AWS call, no push, no pull, no deploy, no S3 write, no vendor call.** Every verdict is a synthetic
payload on the hook's stdin. The edited hook governs the harness only after this branch drains, and it cannot
loosen any refusal except the 4 measured false denials -- AC4 proves that over all 106 arms.
**NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No secrets are needed. No non-ASCII in
anything you write (the suite's one pre-existing non-ASCII byte stays; the hook stays at 0). **PUSH: never**
(LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- in particular never by editing a deny text, the
DT carve-out, another gate, or any lane.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator:** re-run AC0 and the suite baseline (96/0) before you edit;
a moved baseline is recorded, not a failure, as long as the delta rules in AC2 and AC4 hold.
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W95-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row. A pure disarm sets
`DISMISSED_WITH_REASON` with a `dismissal_reason`. The CVO dispositions `Z-S209` at L9, not you.

**THE THREE SCRIPT FILES** (write each to `.scratch/r95/` from the fenced text below, VERBATIM -- they carry
backslashes and must never be typed inline, rule W84-S1):

`.scratch/r95/probe_s209.sh`:
```
#!/usr/bin/env bash
# rk-95 probe: never-rules-gate GATE 5 on quoted absolute git -C / cd paths. READ-ONLY (synthetic payloads).
set -uo pipefail
TOP="$(git rev-parse --show-toplevel)"
MAINROOT="$(dirname "$(git rev-parse --path-format=absolute --git-common-dir)")"
export CLAUDE_PROJECT_DIR="$MAINROOT"
JQ="$TOP/.tools/jq.exe"
HOOK="${NRG_HOOK:-$TOP/.tools/hooks/never-rules-gate.sh}"
M="$(cygpath -m "$MAINROOT")"
W="$(cygpath -w "$MAINROOT")"
verdict() {
  local out
  out=$("$JQ" -nc --arg c "$1" '{tool_name:"Bash",tool_input:{command:$c}}' \
        | OPAL_AGENT_SERIAL="$2" NEVER_GATE_AUDIT=/dev/null bash "$HOOK" 2>/dev/null)
  if printf '%s' "$out" | grep -q '"permissionDecision"[[:space:]]*:[[:space:]]*"deny"'; then echo DENY; else echo PASS; fi
}
DT='0.2.0_DT_PortfolioAnalytics'
row() { printf '%-5s %s\n' "$(verdict "$2" "$3")" "$1"; }
row "P1 DT relative            git -C portal push origin PROD"        "git -C portal push origin PROD" "$DT"
row "P2 DT double-quoted fwd   git -C \"<ROOT>/portal\" push PROD"   "git -C \"$M/portal\" push origin PROD" "$DT"
row "P3 DT single-quoted fwd   git -C '<ROOT>/portal' push PROD"     "git -C '$M/portal' push origin PROD" "$DT"
row "P4 DT double-quoted back  git -C \"<ROOT win>/portal\" PROD"    "git -C \"$W\\portal\" push origin PROD" "$DT"
row "P5 DT cd double-quoted    cd \"<ROOT>/portal\" && git push"      "cd \"$M/portal\" && git push origin PROD" "$DT"
row "N1 DT quoted ws root      git -C \"<ROOT>\" push origin CLOUD"   "git -C \"$M\" push origin CLOUD" "$DT"
row "N2 CTO quoted portal      git -C \"<ROOT>/portal\" push PROD"   "git -C \"$M/portal\" push origin PROD" "1.0.0_SA_CTO~Z"
row "N3 DT cd quoted ws root   cd \"<ROOT>\" && git push origin CLOUD" "cd \"$M\" && git push origin CLOUD" "$DT"
row "N4 DT quoted missing dir  git -C \"<ROOT>/no such dir\" PROD"   "git -C \"$M/no such dir\" push origin PROD" "$DT"
```

`.scratch/r95/suite_as_main.sh` (runs a suite file against a hook, with the MAIN checkout as the workspace):
```
#!/usr/bin/env bash
# usage: suite_as_main.sh <suite file> [<hook file>]   -- read-only toward the main checkout
set -uo pipefail
SUITE="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
MAINROOT="$(dirname "$(git rev-parse --path-format=absolute --git-common-dir)")"
export CLAUDE_PROJECT_DIR="$MAINROOT"
if [ -n "${2:-}" ]; then export NRG_HOOK="$(cd "$(dirname "$2")" && pwd)/$(basename "$2")"; fi
cd "$MAINROOT" && bash "$SUITE"
```

`.scratch/r95/no_new_refusal.sh` (the whole-suite before/after comparison, AC4):
```
#!/usr/bin/env bash
# Runs YOUR suite against the PINNED pre-fix hook and against YOUR hook; compares every arm's verdict.
set -uo pipefail
TOP="$(git rev-parse --show-toplevel)"
PIN=e58250f2615069d8f59160e9762f721e71a28bdb
mkdir -p "$TOP/.scratch/r95"
OLD="$TOP/.scratch/r95/never-rules-gate.PIN.sh"
git show "$PIN:.tools/hooks/never-rules-gate.sh" > "$OLD"
test -s "$OLD" || { echo "FAIL: pinned hook unreadable"; exit 2; }
S="$TOP/.tools/hooks/tests/test_never_rules_gate.sh"
bash "$TOP/.scratch/r95/suite_as_main.sh" "$S" "$OLD" > "$TOP/.scratch/r95/suite_old.txt" 2>&1
bash "$TOP/.scratch/r95/suite_as_main.sh" "$S" > "$TOP/.scratch/r95/suite_new.txt" 2>&1
python - "$TOP/.scratch/r95/suite_old.txt" "$TOP/.scratch/r95/suite_new.txt" <<'PY'
import re, sys
def arms(p):
    out = []
    for line in open(p, encoding="utf-8", errors="replace"):
        m = re.match(r"^  (PASS|FAIL)  (.*?)\s+-> (PASS|DENY)", line)
        if m: out.append((m.group(2).strip(), m.group(3)))
    return out
old, new = arms(sys.argv[1]), arms(sys.argv[2])
print("arms old", len(old), "new", len(new))
assert len(old) == len(new), "arm count differs"
flips = [(n, a, b) for (n, a), (_, b) in zip(old, new) if a != b]
up = [f for f in flips if f[1] == "DENY" and f[2] == "PASS"]
down = [f for f in flips if f[1] == "PASS" and f[2] == "DENY"]
print("flips", len(flips), "DENY->PASS", len(up), "PASS->DENY", len(down))
for n, a, b in flips: print("  FLIP", a, "->", b, "|", n)
print("new_refusals", len(down))
PY
```

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; AC0 and AC3 run under timeout 120; AC2 under timeout 600; AC4 under timeout 900)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-95"><invocation>cd "$(git rev-parse --show-toplevel)" && git diff --quiet e58250f2615069d8f59160e9762f721e71a28bdb HEAD -- .tools/hooks/never-rules-gate.sh && echo "hook_equals_pin True" && bash .scratch/r95/probe_s209.sh</invocation><expect>BEFORE ANY EDIT: "hook_equals_pin True", then the 9-row table exactly as measured at the cut -- P1 PASS; P2, P3, P4, P5 DENY (the 4 false denials); N1, N2, N3, N4 DENY. If P2-P5 already read PASS, the defect is gone and this order STOPs with a row; if the hook differs from the pin, STOP with a row</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-95"><invocation>cd "$(git rev-parse --show-toplevel)" && bash -n .tools/hooks/never-rules-gate.sh && bash -n .tools/hooks/tests/test_never_rules_gate.sh && echo "syntax OK" && git diff --stat e58250f2615069d8f59160e9762f721e71a28bdb -- .tools/hooks/never-rules-gate.sh && git diff -U0 e58250f2615069d8f59160e9762f721e71a28bdb -- .tools/hooks/never-rules-gate.sh | grep -E "^@@" </invocation><expect>"syntax OK"; the hook's diff against the pin is confined to the SITE A / SITE B block -- every hunk header's pre-image range lies within :286-303 of the pinned file (a hunk outside it is a FAIL: nothing else in the hook changes, RULED item 3)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-95"><invocation>cd "$(git rev-parse --show-toplevel)" && bash .scratch/r95/suite_as_main.sh .tools/hooks/tests/test_never_rules_gate.sh 2>&1 | grep -E "^PASS: |ALL CHECKS|FAILURES|  FAIL |S209:"</invocation><expect>"PASS: 106   FAIL: 0" and "ALL CHECKS PASS" (the spawn baseline of 96 plus exactly the 10 S209 arms); all 10 lines named "S209:" read PASS against their stated expectations (5 quoted positives PASS, 4 negatives DENY, the integrator PASS); 0 FAIL lines. The baseline is read at spawn: the bar is "spawn baseline + 10, FAIL 0"</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-95"><invocation>cd "$(git rev-parse --show-toplevel)" && bash .scratch/r95/probe_s209.sh</invocation><expect>AFTER the edit: P1, P2, P3, P4, P5 all PASS (the relative form unchanged and the 4 false denials removed); N1, N2, N3, N4 all still DENY -- in particular N1 and N3, a shared-branch push from the WORKSPACE repo through a quoted absolute path, are still DENIED (the ruled negative control)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-95"><invocation>cd "$(git rev-parse --show-toplevel)" && bash .scratch/r95/no_new_refusal.sh</invocation><expect>"arms old 106 new 106"; "flips 5 DENY->PASS 5 PASS->DENY 0" -- the ONLY verdicts that differ between the pinned hook and yours are the 5 S209 quoted positives (each "FLIP DENY -> PASS"), and "new_refusals 0": every arm the pinned hook admitted, yours still admits, over all 106 arms. Any PASS->DENY flip is a FAIL (this cell adds no refusal)</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-95"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import io; [print(f, "crlf", io.open(f, "rb").read().count(bytes([13, 10])), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8"))) for f in (".tools/hooks/never-rules-gate.sh", ".tools/hooks/tests/test_never_rules_gate.sh")]'</invocation><expect>never-rules-gate.sh crlf 0 non_ascii_bytes 0; test_never_rules_gate.sh crlf 0 non_ascii_bytes 1 (the one pre-existing byte, unchanged from the cut)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~95/AMGT_RESAPP.TO-AMGT-rk-95.gate5-quoted-path-parser.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5` (rc 0 is the verdict); flip the status tag on
the record face to `complete`; commit with `--only -- <paths>`. Report once, naming the suite counts before and after,
AC3's 9-row table, and AC4's flip list.

**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES of both files to `.scratch/r95/` before editing. Never
`git checkout --`, never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>pending</status>
<round>23</round>
<slot>~95</slot>
<fabric>site-z</fabric>
