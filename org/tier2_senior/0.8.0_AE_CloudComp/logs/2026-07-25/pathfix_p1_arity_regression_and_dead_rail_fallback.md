# P1 arity regression (mine) + the rail's dead fallback + the /watcher deaf-session prefix -- 0.8.0_AE_CloudComp~D

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, VALIDATE

Window: session respawn 2026-07-25 ~1639Z -> ~1720Z. Prior session killed (whole program's lanes
respawned together). 3 commits, 8 MCP messages handled, 0 AWS deploys.

---

## Current State

**Everything dispatched at this lane is closed. Nothing outstanding at me.**

**1. P1 regression from my own `4d2588f35e` -- FIXED @`0e8ea80`, pushed `82fb44f50c`.**
`4d2588f35e` changed `org/modules/graph/comp_system.py:502` `refresh_managed_regions()` from a
2-tuple to a 3-tuple (adding the N/M denominator). I updated all 8 production call sites
(`comp_system.py:685/741/919/935/942/1179/1344`) and none of the 5 test sites
(`org/modules/graph/tests/test_comp_system_metrics.py:74/79/87/95/103`). 13 sites total.
The unpack runs at MODULE level, so it raised during pytest COLLECTION -- and a collection error
aborts the entire directory. `pytest org/modules/graph/tests/` returned
`Interrupted: 1 error during collection`, which reads as broken tooling, not as a defect.
Found by `1.0.0_SA_CTO~Z` (165744Z), source-confirmed.
Now: `--collect-only` -> **806 collected, rc=0, 7.96s** (CTO~Z independently got 816 after the
tree advanced -- two measurements, not a discrepancy; deliberately not reconciled).
Full directory run: **28 failed / 777 passed / 1 xfailed in 580.61s**. All four CTO~Z asks
closed and ACCEPTED (171720Z).

**2. The 28 failures are NOT mine -- causally excluded, with a positive control.**
15 distinct files carry them; **none** references `refresh_managed_regions` or `comp_system`
(positive control: `test_comp_system_metrics.py` -> 10 refs, so the probe fires). They were
HIDDEN behind the collection abort, not caused. 11 of 15 are bd-hold / sovereign-guard /
held-path tests. I formed a labeled INFERRED hypothesis (they track the 07-14 sovereign-block
lift), did NOT open the enforcement source, and did NOT let it authorize a fix.
**CTO~Z issued a STOP: out of ~Z scope, routed to base `1.0.0_SA_CTO` with the fork stated both
ways. I am not investigating further and have not touched those tests.**

**3. `/watcher` SKILL.md deaf-session prefix -- FIXED @`50a1b346b`.**
This harness shell is cygwin-flavored (`ls /c` -> ENOENT, `/cygdrive/c` resolves; uname says
MINGW64 while OSTYPE says cygwin -- uname is NOT the discriminator). My first inbox-Monitor arm,
following the doc verbatim, died `exit 127`. All 12 live watcher processes in the fabric run the
`/cygdrive/c` form; ZERO use the documented one. CTO~Z's `aef2840826` fixed Step 3; Step 0 still
hardcoded `/c/` as "Workspace abs path" -- the copy an agent reads FIRST and takes the prefix
from. Fixed the survivor only; did not touch CTO~Z's mechanism.
**Census still open, NOT mine:** 20 agent `prompt.md` files + `org/mcp/INBOX_WATCH_DESIGN.md`
carry the broken literal. Routed to CTO~Z. **De-escalated:**
`.tools/hooks/block-bare-inbox-watch.sh` carries it only in its human-readable REASON string --
its block regex keys on the RELATIVE form, so doc drift, not a functional break.

**4. Rule 21's dead fallback -- FIXED @`8ec16dff7`, pushed.**
Rule 21 Gate-1 is ARMED and hard-DENIES estate-scoped raw Bash grep/find/rg. The sanctioned
alternative it names is `comp-grep`/`comp-glob`. **Neither resolved** -- the gate denied the raw
search and handed the agent an escape hatch that was `command not found`. Provisioned both via
`.tools/provision-path-shims.sh` (all three shebangs read + verified `#!/usr/bin/env python3`,
reusing comp-which's already-exercised `py.exe` mapping).
Scope held deliberately narrow per CTO~Z (5 named tools, NOT the ~91), and the open
full-widening residual is now stated IN the header rather than implied.

---

## >> THE LESSON OF THIS SESSION: ONE INSTRUMENT THAT LIES IN FOUR WAYS <<

Recorded at CTO~Z's explicit instruction (171720Z), in the words it used.

**I hit THREE instrument errors in my own hands this session. Every one produced a WELL-FORMED
WRONG ANSWER and never an error.**

1. **MSYS pattern rewrite.** Searched `comp-grep '/c/Users/.../inbox-watch'` -> confident `0`,
   with the tool's own reassurance *"0 matches is a real result here."* MSYS had rewritten my
   leading-slash argument to `C:/Program Files/Git/c/Users/...` before the tool saw it. The tool
   answered the question it was handed, correctly. **I nearly filed a coverage-hole defect
   against a tool that was working.**
2. **Shebang census misread.** Reported CRLF variants from a `sort | uniq -c` split. A byte-exact
   `cat -A` re-measure falsified it: 21 identical, 0 CRLF. I still cannot fully explain the split.
3. **`grep -c` exit-code semantics.** `grep -c ... || echo 0` -- **`grep -c` EXITS 1 on a zero
   count**, so `|| echo 0` appended a SECOND zero. `$hits` became `"0\n0"`, which `!= "0"`, so my
   coupling check printed **COUPLED for all 15 files -- the precise opposite of the truth**, as a
   clean, confident, well-formed list. **I was one step from sending CTO~Z a report that would
   have made my own fix look like the cause of 28 failures. It said it would have acted on it.**
   Caught only because 15-of-15 was too tidy to be real -- **a judgment call, not a control.**

**THE REMEDY (CTO~Z's words): count with `wc -l`, and run a positive control that must be
non-zero.**

**These are not four bugs. They are ONE INSTRUMENT THAT LIES QUIETLY IN FOUR WAYS** -- this is
the fourth grep-family silent-lie in the estate's record, after binary-mode truncation,
case-mismatch, and the MSYS pattern rewrite.

**THE PART I WANT TO SURVIVE THIS LOG: the instrument being MINE and SMALL did not help -- if
anything it REMOVED the suspicion.** I scrutinize comp-tools and AWS output. I did not scrutinize
a three-line shell check I had just written, because I had just written it.

**Corollary earned twice today:** the defect was hiding in the FIXTURE OF ITS OWN REMEDY, twice.
`assert live_ti != 37` sat three lines above the arity bug I was sent to fix, armed on a moving
value, able to abort collection for all 806 tests. And `provision-path-shims.sh`'s closing line
hardcoded 3 tools while its loop wrote 5 -- an unstated-denominator defect inside the fix for
unstated denominators.

**Second corollary (CTO~Z, adopted):** a module-level `assert` on a **STATIC INVARIANT** is a
different risk from one on a **MOVING VALUE**. My ask-4 sweep found 4-of-80; CTO~Z ruled the
other 3 (`assert TOOL.is_file()`, guarding a silently-misresolved repo root) must NOT be
converted -- converting them removes a working control to satisfy a pattern. Correct answer:
*zero remaining module-level asserts on moving values; three on static repo-structure
invariants, deliberately retained.* **I applied the benign/real boundary correctly one level up
(refusing to hand CTO~Z the alarming-but-signal-free 76-of-80) and then failed to apply it one
level down, inside the 4 I did report.**

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-grep` | `'/c/Users/.../inbox-watch'` | **FAIL (my arg, not the tool)** | Confident `0` -- MSYS rewrote the leading-slash pattern. Tool correct; argument corrupted pre-arrival. |
| `comp-grep` | `'ajb_workspace/org/mcp/inbox-watch'` | PASS | 27 hits / 26 files -- the real census after dropping the leading slash. |
| `comp-grep` | `'ORPHAN HAZARD'` (positive control) | PASS | 23/21. Used to falsify my own coverage-hole hypothesis. |
| `comp-grep` | scoped `.claude/skills/watcher` | PASS | 48 matches / 1 file -- proved the enumerator DOES see `.claude/`. |
| `comp-grep`/`comp-glob` | bare-name, fresh shell (post-shim) | PASS | rc=0 both; + negative control returning 0. CTO~Z acceptance. |
| `_comprail.gitignore_aware_files` | direct lib call | PASS | 25,906 files incl. the file I thought was excluded -- killed the false hypothesis. |
| AST walk (ad-hoc) | 80 test files, module-body scan | PASS | Ask-4 sweep. Grep CANNOT do this: text can't separate a call inside a `def` (safe) from module level (dangerous), and **that distinction IS the defect class**. |
| `.tools/commit-gate.sh` | on the edited `.py` | PASS | py_compile + ds-precommit + ruff clean. |
| `.tools/safe-commit.sh` | 3 commits, `-F` form | PASS | `-F` per the commit-message-as-execution-vector rule. |
| `.tools/provision-path-shims.sh` | provision + re-run | PASS | 5 tools x2 forms; output now prints its own denominator. |
| `comp-blast` | **NOT RUN -- and that is the finding** | GAP | See below. |

**What worked:** the AST walk over grep for a structural question. Positive controls -- they
falsified two of my own wrong hypotheses (the comp-grep "coverage hole" and the 15-of-15
coupling) before either reached a peer.

**What failed:** three of my own ad-hoc shell instruments (above). Also `comp-grep` is
`.gitignore`-aware and honest about it, but its "0 matches is a real result here" reassurance is
scoped to *the pattern it received* -- it cannot know the pattern was mangled upstream, and the
reassurance reads as broader than it is.

**Gap found -- the causal one: I did not run `comp-blast` on my own interface change.**
`4d2588f35e` changed a return arity. That is an INTERFACE change and its blast radius is the
caller set -- exactly what `comp-blast <fn>` enumerates. I verified the BEHAVIOR I changed
(comp-system self-test green; CVO~Z's independent mutant pass green at 150704Z) and never the
INTERFACE I changed. **Two verification passes, one adversarial, both legitimately green,
neither pointed at arity.** Added to my own pre-commit habit for interface changes specifically.

---

## Deployment / Verification (AE)

No AWS deploys, no Terraform, no Lambda. One local provisioning action:

```
$ bash .tools/provision-path-shims.sh
provision-path-shims: wrote 5 tool(s) x2 forms to /cygdrive/c/Users/AndrewBerman/bin
  -- aws comp-glob comp-grep comp-system comp-which
provision-path-shims: SCOPE = this NAMED set only, NOT all 91 .tools/comp-* tools (see header).

$ comp-grep 'ORPHAN HAZARD'          -> rc=0, 23 match(es) in 21 file(s)     POSITIVE CONTROL
$ comp-glob '**/provision-path-shims.sh' -> rc=0, 1 file(s)                  POSITIVE CONTROL
$ comp-grep 'zzz-no-such-string-9f3a1'   -> 0 matches                        NEGATIVE CONTROL
$ command -v comp-grep -> /cygdrive/c/Users/AndrewBerman/bin/comp-grep       via shim, not .tools
```

```
$ python -m pytest org/modules/graph/tests/ -q --collect-only
806 tests collected in 7.96s                                    (was: Interrupted, 1 error)
$ python -m pytest org/modules/graph/tests/ -q
28 failed, 777 passed, 1 xfailed, 6 warnings in 580.61s (0:09:40)
```

Tree-state caveat, stated to CTO~Z rather than left for it to discover: the full run predates
the `:58` edit. That edit is in a file none of the 28 touch, so it cannot move the number --
but whether that mattered was CTO~Z's call, not mine to pre-empt.

---

## Blockers

**None.** Nothing evidence-BLOCKED at this lane.

---

## MCP traffic

8 messages. Significant: CTO~Z P1 dispatch (165744Z) -> my ACK (165901Z) -> fix report (171145Z)
-> ask-3 close (171521Z) -> CTO~Z acceptance + bd STOP (171720Z). CTO~Z queued dispatch (171513Z)
-> delivered (171957Z). ~C PATHFIX routing (165535Z) -> my ACK + corroboration (165641Z) -> ~C ACK
(165747Z). CTO~Z independent collection confirmation + ask-4 boundary ruling (171318Z).

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** `org/XXX.md` Step 1b-A.3 wording -- exec-owned, mechanism built, one-line
   call is yours. Honest form is print N-of-M, not probe-an-unprovisioned-tool (the latter goes
   stale the moment someone provisions whichever tool you pick).
2. **[1.0.0_SA_CTO~Z]** The 20 `prompt.md` files + `org/mcp/INBOX_WATCH_DESIGN.md` still carrying
   the broken `/c/` watcher literal. Census delivered; not this lane's files.
3. **[1.0.0_SA_CTO]** (via CTO~Z routing) The bd/sovereign-hold cluster -- 11 files, fork stated
   both ways, one instance grounded by CTO~Z. **STOP standing at this lane.**
4. **[1.0.0_SA_CTO~Z]** OPEN + UNASSIGNED: whether to widen shim provisioning to the full comp-*
   set. Named in the script header as a decision, not a gap.
5. **[1.0.0_SA_CTO~Z]** The `test_comp_system_metrics.py` script-to-pytest-functions conversion.
   The file's own 07-22 guard comment predicted this regression in writing; it has now recurred,
   so it is evidence rather than hypothesis. I will take it if dispatched.
6. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by.
