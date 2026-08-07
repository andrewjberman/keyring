# A law-cited invariant had never once fired, and printed PASS every time it did not -- 0.8.0_AE_CloudComp

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, IMPLEMENT

**Date:** 2026-08-06
**Window:** 2107Z - 2212Z (session start -> now; prior log `addparser_ast_fix_1955-2035Z.md` @aa7f9df9f1 covers the predecessor session)
**Task Order:** ad-hoc -- Andrew-direct at my terminal, VERBATIM: *"i need you to review the below because I want to make sure that this tool is in proper working order"*, pasting the predecessor's 26-defect delivery + `1.0.0_SA_CTO~B`'s confirmation of the `_ADD_PARSER` finding. Routing for the remediation: `1.0.0_SA_CTO~B` MCP `20260806T213335Z`.
**Status:** COMPLETE

---

## Objective

Establish whether `comp-manifest-check` is in proper working order after the morning's
`_ADD_PARSER` AST fix. Not re-run the predecessor's harness -- independently verify, then act on
whatever the verification found.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-manifest-check | `completeness` | PASS | rc=0 before AND after every edit -- the commit-path control. Its retired-alias line was the defect |
| comp-manifest-check | `retired-alias` | FAIL -> PASS | rc=1 naming 1 citation (pre-fix, HUD-only substrate) -> rc=1 naming all 7 (post-sweep-fix) -> rc=0 (post-cleanup, 108 surfaces) |
| comp-manifest-check | `selfcheck` | PASS | AC4 synthetic anti-pattern, 3 findings / 0 false-positive. Confirms the tool is not globally broken |
| commit-gate.sh | `commit-gate.sh org/modules/graph/manifest_check_cli.py` | PASS | Rule 14, run on both `.py` edits |
| comp-pulse | (auto `[risk-reflex]`) | WARN | [HOLD] on prod-deploy. Citation READ this time (I tail'd past it once and went back) -- see Gap found |
| comp-which | `"how do I grep the repo"` | PASS | Startup A.3 EXERCISE limb; 96 of 97 comp-tools resolve bare |
| comp-grep / comp-glob | not run | -- | Targeted reads of known files + two purpose-built harnesses; native Grep used for the citation sweep with the invariant's own word-boundary pattern |

**What worked:** importing the SHIPPED `_add_parser_names` instead of re-implementing it. A
re-implementation can share the author's wrong premise and then agree with itself; importing the
artifact makes the test a cross-check rather than an echo. And the E4/E5 discriminating pair --
feeding the invariant a citing file directly (blocks) versus committing that same file (passes) --
is what separated "the logic is wrong" from "the wiring is dead", which are different repairs.

**What failed:** my own first `--since` window returned `0 commits` while gathering evidence for
this log. `--since` reads LOCAL time and I passed a UTC figure, putting the window in the future.
Zero was a broken retrieval wearing a fact's clothing. Caught by running the same query with no
`--since` as a positive control (16 commits), exactly the class CLAUDE.md's retrieval rule names.

**Gap found:** two, both routed to `1.0.0_SA_CTO~B`, neither touched.
(1) The retired-alias finding text says *"CITED in committed routing surface(s)"* while the scan
reads the WORKING TREE -- so it reports an UNTRACKED file as committed. Same
say-what-you-actually-checked class as the PASS line I fixed, one field over, and it is what let
my own pathspec error through.
(2) `comp-pulse diff` emitted an identical `[HOLD]` citing
`memory/feedback_ds_sc_no_commit_coo_sole_committer.md` for prod-deploy AND for six unrelated
sibling skills -- keying on directory co-membership, not on the claim binding the change.

---

## Work Completed

### 1. The extractor fix is sound -- verified, not accepted

8 controls, importing the shipped function. Positive (8 real subparsers still harvested, retrieval
denominator 84,244 bytes), negative (`drift_cli.py`: old regex `['reconcile']` -> AST `[]`), mutant
(4 planted prose shapes harvested by the regex, none by the AST, and DISCRIMINATING -- it still
harvests the real call, so the test cannot pass by finding nothing).

Two controls the delivery had not run: unparseable source returns `None`, parseable-but-empty
returns `set()`, verified genuinely distinct and not collapsed. That distinction is the difference
between "could not tell" and "registers nothing", and collapsing it is how a gate reports a clean
pass it never earned.

Regression across 48 comparable engines: 46 identical, 0 AST-only additions, 0 lost to parse
failure, 2 phantoms removed. **My denominator is 48 compared, not the delivery's 51** -- I excluded
pinned wrappers and unresolvable engines. Different scoping, same conclusion; stated, not
adjudicated, and CTO~B explicitly wanted no adjudication.

### 2. The finding: a check that had never run, reporting PASS

```
comp-manifest-check completeness  -> "retired-alias invariant PASS ... none cited in
                                      committed routing surfaces."
comp-manifest-check retired-alias -> rc=1 BLOCKED, naming a citation.
```

Same tool, same HEAD, same second. Ground at source: `commit_gate_runner._is_completeness_substrate`
excludes every routing surface there is -- `.claude/skills/**` and `**/prompt.md` are absent from
`_COMPLETENESS_SUBSTRATE_EXACT`, and the `.tools/` branch requires a file directly under `.tools/`,
so `.tools/hooks/comp-tool-hud.sh` falls out too.

Exercised rather than asserted:

| Control | Result |
|---|---|
| E4 fed a citing skill file directly | rc=1, correctly names both retired tools -- LOGIC SOUND |
| E5 real commit staging 4 citing files | substrate=[] -> rc=0, sails through -- WIRING DEAD |
| E1-ctl positive control on the predicate | `graph-call-manifest.yaml` -> True, so it discriminates and E1's False is a real exclusion |

CLAUDE.md Rule 20 cites that invariant verbatim as the thing that polices exactly this class.

### 3. What it was missing: 7 live citations in 6 files

Swept all 108 routing surfaces the invariant's own predicate recognises. Sharpest:
`.claude/skills/prod-deploy/SKILL.md:99,104` -- a **standing SEV1 portal promote step** with a
literal `.tools/comp-surface-check check --mode blocking` invocation. Andrew retired that tool this
morning; verified GONE from disk AND unresolvable on PATH. An operator following that procedure
gets `command not found` under a step whose own text reads *"silence is not a pass."*

### 4. The prerequisite nobody saw: a tombstone is indistinguishable from a route

CTO~B's instruction -- *"say plainly in the file that the check is retired"* -- was
**unexecutable**. The check text-matches the NAME, so a strike note reading "comp-surface-check is
RETIRED, do not run it" is byte-identical to a route, and it fired on my own strike note. The only
way to satisfy the gate was to delete the explanation.

**Third instance of one class in this tool in one day:** the comment-blind `_ADD_PARSER` regex
(prose read as code), the false all-clear (a claim without a check), and a matcher that cannot tell
a gravestone from a signpost. CLAUDE.md F-010 already names the boundary and cites LD-0274 as the
counter-example -- *"a matcher that fires on mentions."* This member fires on mentions.

Fixed with the estate's existing idiom rather than a new mechanism (build-ladder rung 2): an
audited inline `retired-tombstone: <name>` marker, per-file and per-name, sibling to
`# never-override:` and `# rail-checked:`. Tombstoned mentions are COUNTED AND PRINTED -- an
invisible exemption would be a second blind spot wearing the first one's fix as a disguise.

### 5. My own error, self-caught and reverted

`22947cd7a` reported **167 insertions for 10 lines of intended edit**. `create mode 100644` on
`.claude/skills/prd-delta/SKILL.md` was the tell: untracked WIP, and I named its path in my
safe-commit pathspec off the sweep's hit list, publishing 162 lines of another agent's unfinished
skill under my author line. Reverted at `25afd0ba0` -- `git rm --cached`, file stays on disk, their
work unpublished, my one-line repoint left as an uncommitted edit for them to take or drop.

Mechanism, since it generalises: safe-commit's contamination guard protects against paths OUTSIDE
your declared pathspec and structurally CANNOT protect you from one inside it -- an explicit
pathspec is read as intent, correctly. My pathspec came from a sweep that reads FILES ON DISK and
never asks whether they are tracked. Caught by reading the commit STAT, not the exit code. Applied
the lesson immediately: tracked-status checked before the final commit's pathspec.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Import the shipped function; do not re-implement it | A re-implementation can share the wrong premise and agree with itself. Testing the artifact makes it a cross-check |
| Fix the MESSAGE before widening any scan | "Never claim what you did not check" is correct independent of how much gets checked, and it blocks nothing |
| Commit path NOT widened in the same act as the finding | Would have blocked commits touching citing files before anyone could clean them. Sequencing was CTO~B's call, and they took it |
| Tombstone scoped per-file AND per-name | A repo-wide exemption list re-creates the hole it closes |
| Tombstones COUNTED and PRINTED, never silent | A silent exemption is the same defect family this whole session is about |
| Extract `_is_routing_surface` and mirror it, not re-spell it inline | The two predicates decide REACHES vs SCANNED; drift between them recreates the invisibility. W1 asserts they agree across 7 probes |
| `comp-surface-check` DROPPED from tooling lists, never repointed | No 1:1 successor. Rule 20 records "no automated commit-time guard" as the ACCEPTED consequence; naming a substitute invents a control Andrew did not ask for |
| `pipescript` repoint chosen per sentence, not by find-and-replace on the successor field | CLAUDE.md is explicit that `comp-pipescript` is a DIFFERENT tool, not a synonym. Every site here asked for lineage traversal, so `comp-estate` was both the declared successor and the right call |
| Un-track prd-delta rather than leave it published | I have no authority to publish another agent's WIP. Reversible, restores their state exactly |
| Mutant-test the CLEAN sweep | rc=0 on a clean estate is indistinguishable from a broken sweep. 0 -> 1 -> 0 under a planted citation is the only thing that separates them |

---

## Files Modified

See commit messages: `1bd97f37a`, `c564b4fcb`, `997434c08`, `4912045b2`, `22947cd7a`, `25afd0ba0`,
`f8a278b8c`. Rows needing extra context:

| File | Change | Committed |
|---|---|---|
| `org/modules/graph/manifest_check_cli.py` | PASS line prints its denominator; `_routing_surfaces()` estate sweep for the human-facing subcommand; `retired-tombstone:` exemption (counted); order-preserving dedupe of the file list | Yes -- `1bd97f37a`, `c564b4fcb` |
| `.tools/commit_gate_runner.py` | `_is_routing_surface()` extracted, mirroring the CLI predicate; routing surfaces now reach the completeness family | Yes -- `4912045b2` |
| `.claude/skills/prod-deploy/SKILL.md` | SEV1 hand-check STRUCK + tombstoned; states no guard replaces it; promote SEQUENCE untouched (verified the citation sat in a comment block, not a numbered step) | Yes -- `997434c08` |
| `.claude/skills/prd-delta/SKILL.md` | ACCIDENTALLY COMMITTED then UN-TRACKED. On disk, untracked, carrying my uncommitted one-line repoint | No -- deliberately reverted `25afd0ba0` |
| `scratchpad/verify_manifest_check.py`, `exercise_retired_alias_reach.py` | 13 controls + the E1/E4/E5 reach exercise | No -- session scratchpad, not committed |

---

## Deployment Sequence

None. Compiler-tool source + records only -- no Lambda, EC2, Terraform or S3 leg, nothing deployed
to verify. The gate runs below are the behavioural evidence. Not pushed (lanes commit, integrators
push); 23 ahead of `origin/CLOUD` including peers'.

---

## Verification

```
EXTRACTOR (8 controls, shipped function imported)                       ALL PASS
  A1 positive   8 real subparsers, retrieval denominator 84,244 bytes
  A2 negative   drift_cli.py: regex ['reconcile'] -> AST []
  A3 mutant     4 prose shapes harvested by regex, 0 by AST; still harvests the REAL call
  A4/A5         unparseable -> None; parseable-empty -> set(); NOT collapsed
  A6 regression 48 engines: 46 identical, 0 added, 0 parse failures, 2 phantoms removed

REACH (the finding, pre-fix)
  E1  4 real citing surfaces -> _is_completeness_substrate False for ALL
  E1-ctl graph-call-manifest.yaml -> True            <- predicate DISCRIMINATES
  E4  invariant fed a citing file -> rc=1, names both tools
  E5  real commit of those 4 files -> substrate=[] -> rc=0

WIRING (post-fix, 6 controls)                                           ALL PASS
  W1 no predicate drift runner-vs-cli across 7 probes
  W2 citing skill file      -> BLOCKED (was rc=0)
  W3 CLEAN skill file       -> passes        <- the whole risk of closing the wiring
  W4 tombstoned prod-deploy -> passes
  W5 manifest substrate     -> rc=0, UNCHANGED
  W6 MUTANT freshly-planted citation in a clean file -> BLOCKED
     ^ fires on the defect EVENT, not on a roster of files I enumerated

TOMBSTONE LEAK CONTROL
  prod-deploy alone (tombstoned) rc=0, "1 tombstoned mention(s) exempted"
  seams alone (NOT tombstoned)   rc=1        <- does NOT leak across files
  both together                  rc=1

FINAL STATE
  comp-manifest-check retired-alias -> rc=0
    "7 retired name(s) declared ... none cited across the 108 routing surface(s) in scope
     (1 tombstoned mention(s) exempted)."
  comp-manifest-check completeness  -> rc=0
    "... citation check (C) DID NOT RUN -- no routing surface in scope."   <- honest, was "none cited"
  MUTANT on the clean sweep: 0 -> 1 -> 0        <- clean result is DISCRIMINATING, not blind
```

---

## MCP Traffic

4 significant (1 broker re-surface of an already-handled message, not counted): received CTO~B
`20260806T200157Z` TASKED (already discharged by the predecessor, RAVC2 sent `202749Z` -- no action);
sent FINDING `213236Z`; received CTO~B ROUTING CALL `213335Z` ("you keep all 7", ordering set);
sent RAVC-ACK + correction `213455Z`; sent RAVC2 CLOSED `220031Z`.

---

## Blockers

None. All seven citations discharged, both tool defects fixed, estate sweep rc=0 on an earned pass.

---

## Current State

`comp-manifest-check`'s retired-alias invariant now (a) prints the denominator of what it scanned,
so a check that did not run can never read as one that passed; (b) sweeps all 108 routing surfaces
in its human-facing `retired-alias` subcommand, which blocks nothing; and (c) honours an audited,
counted `retired-tombstone: <name>` marker so a retirement can be DOCUMENTED without the note being
read as a route. `.tools/commit_gate_runner.py` now routes routing surfaces into the completeness
family via `_is_routing_surface()`, mirrored against the CLI predicate and asserted non-drifting --
so a commit TOUCHING a citing file is blocked while a clean skill commit passes.

The estate carries zero un-tombstoned citations of the 7 declared retired names, verified across
108 surfaces and mutant-controlled. The `comp-surface-check` SEV1 hand-check is struck from the
portal promote procedure with the no-replacement consequence stated in the file; the promote
sequence itself is untouched and any change to it remains DT's.

`.claude/skills/prd-delta/SKILL.md` is UNTRACKED on disk (as its author left it) carrying one
uncommitted line of mine: `graph/pipescript/blast` -> `graph/estate/blast`. Theirs to take or drop.

7 commits this window, none pushed; 23 ahead of `origin/CLOUD` including peers'. Startup complete
(watcher Monitor `bx3f9th3u` live and confirmed delivering a real message mid-session; registration
re-taken after a dead-PID predecessor leftover at PID 15052). IDLE and event-driven.

---

## Next Steps

1. **[1.0.0_SA_CTO~B] The finding-text honesty gap** -- the invariant says "CITED in committed
   routing surface(s)" while the scan reads the working tree, so an UNTRACKED file reports as
   committed. Same class as the PASS line, one field over, and it is the mechanism that let my
   pathspec error through. Routed with the repro.
2. **[1.0.0_SA_CTO~B] comp-pulse `[HOLD]` precision** -- identical citation emitted for prod-deploy
   and six unrelated sibling skills; keying on directory co-membership rather than the claim
   binding the change. Different tool, flagged not chased.
3. **[1.0.0_SA_CTO~B] The doctrine candidate, offered and not landed** -- stated so it is
   actionable without its incident, per CLAUDE.md's editing test: *a commit-scoped citation check
   can only ever catch a citation added AFTER a retirement, so at the instant a name is retired
   every existing citation becomes permanently invisible to it. Retirement day is exactly when the
   estate-wide read is needed.* Whether that earns a line is CTO's.
4. **[0.8.0_AE_CloudComp]** IDLE, event-driven. The genuine-10 subcommand backfill worklist from the
   prior window is still open at CTO~B; `.tools/portal-hooks/commit-msg` (auto-appending
   `SURFACE_ACK`, self-testing against a deleted CI workflow, still installed by `install.sh:31`)
   remains a named carried item.
