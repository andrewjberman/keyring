# T-16 second pass, the rail verified at 4 of 4, a crash I caused, unit 2's retirement through the estate's own mechanism, unit 3 -- 0.8.0_AE_CloudComp

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE, COORDINATE

**Date:** 2026-09-02, 17:56Z -> 21:50Z (continues the 14:07-17:56Z log @c5cd0390d6; one session, one
crash-and-resume inside it)
**Task Order:** none dispatched to this base seat. Work arrived as CTO placements/rulings (T-16, its
second pass), CVO delegations under Andrew's ~16:53Z direction (units 2, 3a, 3b), COO sequencing
words, and one Andrew-direct via COO (~A deregistered; excess reallocation answered NONE by CVO).
**Status:** all owned work delivered or gated. Next unit (T-16 s.4 per-tool pass) unblocked as of this
log: the PRD was located by name at 21:47Z.

## Objective

1. Release condition 5 (the stage-4 battery) -- first pass, then the second pass three seats required.
2. Verify CTO's rail remedy at this seat on the sound probe.
3. Unit 2: retire comp-kuzu-inc/-full onto `comp-kuzu --mode`, ONE commit, consumers first.
4. Unit 3: comp-adversary self-report (3a); comp-find's first battery (3b).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-read | `--for` / `--enumerate` on ~20 files | PASS | located every carrier line; surfaced the `--enumerate` `^` limitation twice (anchors must be unanchored substrings) |
| comp-find | `--name 'NFRA_COMPEFFICACY' --all` | PASS | found the PRD in CVO's deliverables after two directory GUESSES found nothing -- name search, not a path I invented |
| comp-find | `'comp-kuzu-(inc\|full)' --all --files` | PASS | 15 live carriers vs the 5 the delegation named; CVO re-scoped by lane on it |
| comp-manifest-check | `completeness`, `retired-alias` | PASS at commit | standalone `completeness` blocks pre-commit on the index universe; the commit-time universe is deletion-aware (manifest_check_cli.py:545-562, read at source) |
| comp-which | two routing intents, post-edit | PASS | "refresh, behind" -> `--mode inc` (2.00); "full rebuild" -> `--mode full` |
| comp-which-routing-test | full harness, twice | PASS | first run measured mid-edit (working_tree_differs true) -- discarded; re-run on the committed tree: sound by construction |
| comp-kuzu | `--mode inc "MATCH ..."` | PASS | inc branch, 0 full-loader mentions, 6 s, 27,122 rows; labeled-stale sub-branch NOT reached (DB current) |
| comp-adversary | `--self-test`, `compose` x4 | PASS | 5/5 held; the composes were 3a's negative + positive controls |
| comp-system | regen before every `.tools/` commit | PASS | prescribed path, no override, three times |
| pytest | `--collect-only` timing on two batteries | PASS | 0.09 s and 0.07 s -- the CLOCK is the acceptance |

**What worked:** measuring before believing, four times over -- the pre-T1 hook (20 s, not faster), the checker's universe (deletion-aware), the sink's cut (80 not 200), the args of the failed send (my tag).
**What failed:** my own envelopes, repeatedly -- a grep filter that hid a git refusal, a display prefix I then copied into anchors, a bare `bash` in a Python subprocess that hit the WSL stub and took the session down, a `head`-cut of an Andrew-direct, five malformed body tags. Every one reported as a CONTENT problem and was never one.
**Gap found:** `comp_log_auto.py:349` cuts `args_head` at 80 -- any token-based acceptance on the runs sink silently fails past that; unit 1's passed only because its args were short. Rule P/T row.

## Work Completed

Seven commits under this author line in the window (`git log --author --since`, count 7, incl. the
first log's own commit). Push state measured 21:46:51Z vs origin/CLOUD `2f1ba8c604`: `e66d5e698d`,
`03cf4d17ac`, `dffbee781c`, `4c3b848c97` ON ORIGIN; `1e6206a267`, `610bb9e31e` LOCAL. Perishable.

### 1. Release condition 5, two passes -- `e66d5e698d` (PARTIAL) then `03cf4d17ac` (CLEARED)
Pass 1 moved the module-scope `sys.exit` into a `__main__` guard: pytest collected 1, passed 1, and
CTO, CVO~A and I all graded it green off "1 test collected in 131.9 s" -- **reading the count and not
the clock beside it.** Four composes still ran at IMPORT; a 90 s ceiling killed collection silently
(rc 124, indistinguishable from the old defect). CVO base read the module for module-scope work and
caught it. Pass 2: `_ws()`/`_tool()` lazy, `_run_battery()` holds every subprocess, `COMP_ADVERSARY_TOOL`
selects the binary so a PRODUCTION mutant lives in a temp copy. Collect 132 s -> 0.09 s; 1 passed;
direct 7/7; mutant (`_comp_read_digest` returns empty) reddened DIGEST-CONTENT 1 of 7, production sha
unchanged. CTO PASS on the file (module read BEFORE the count), CVO~A GREEN @5dbca15a4a, CVO base P0.1
CLEARED. RC5 discharged; with CTO's RC7 the ETFS_GUARDRAIL hold LIFTED (CVO 92779) and the step-6 seam
is clear fabric-wide.

### 2. The rail remedy, verified here -- CTO's `d2eb720bde` (`timeout` 5 -> 30)
The concurrent-5 bare-gated-search shape that produced 5/5 EXECUTED, 0/5 rows at 17:30Z produced 5/5
REFUSED, 5/5 DENY rows at 18:11Z -- same seat, one config line between. Population on sound probes:
CTO (b)->(a), me (c)x5->(a)x5, COO (b)->(a), CVO (c)->(a): 4 of 4 Claude seats. Codex (c) is
structural (no PreToolUse bridge). My own earlier "my hook fires" was an ALLOW-path probe and my delta
was same-call; both conceded on the record (92609). The pre-T1 hook measured 12-30 s -- FOUR TIMES
SLOWER -- so the onset story I had drafted ("T1 pushed it over") was falsified before it landed.

### 3. A crash I caused, and the resume
A Python patch script ran `subprocess.run(["bash", "-n", ...])` -- bare `bash`, which from Python
resolves to the System32 WSL stub (the trap `git_bash_resolver.py` exists for). The session died; on
resume the broker was gone until `ToolSearch` re-surfaced it, the Monitor was dead, and no A.1 serial
file existed. Re-registered (PID 6156), Monitor re-armed (`bzib58ucg`, confirmed running), serial
file written, three OFFER-EXHAUSTED rows opened and acked. The comp-kuzu edit the script had written
was syntactically fine under Git Bash.

### 4. send_message "body is EMPTY" -- ROOT CAUSE, and it was me
Every refused send had my body parameter tag WITHOUT its namespace prefix; every landed one had it.
The tell: a mis-closed invoke merged the next call's `description` into a send and the broker
refused "unknown parameter: description". Five content hypotheses (subject length, plural
recipients, angle brackets "n=2", double-dash, tilde recipient) were confounds with tag hygiene --
each "single-variable" test changed the content AND the tag. A second envelope trap the same hour: a
literal closing tag inside a Write's content ended the parameter early and swallowed the next call.
Memory entry rewritten (`reference_send_message_...`); index line corrected.

### 5. Unit 2 -- `dffbee781c`, 15 files, both wrappers `delete mode`. CLEARED by CVO (92767)
Carrier set MEASURED at ~15 (census over 145,054 files) vs 5 named; CVO re-scoped by lane (PRD =
CTO's; briefs = nobody's). Retired THROUGH the estate's mechanism: `retired_aliases` in
graph-call-manifest.yaml with `successor: comp-kuzu`, in the comp-surface-check precedent's shape,
recording the ORDER (consumers first, callers told, executable last). Routing entries retargeted;
tools_index rows dropped; comp-tools/coverage-map/output-contracts folded `--mode` semantics onto
comp-kuzu (incl. THE VERDICT IS IN-BAND NOT rc); kuzu_cli.py :39/:168 comments only; flow doc dated;
both closed projects' phase notes appended. Callers CTO 7 / CRO 6 / CTO~B 1 re-derived by `ts_epoch`
and notified BEFORE the act (92748). Forwarders removed on device Andrew; the provisioner only ADDS.
First safe-commit hit git rc=128 after every gate passed -- a shared-worktree index-lock race (CVO's
pass-2 landed under me); the identical staged set committed on retry.

### 6. Unit 3 -- `4c3b848c97` (3a) and `1e6206a267` (3b); baseline `610bb9e31e`
3a: comp-adversary `_self_report`, unit-1 shape. Negative control 0; positive control EXACTLY 1 row
token-matched -- on the THIRD attempt, after finding the sink cuts `args_head` at 80.
3b: `.tools/tests/test_comp_find_battery.py`, six arms on the MEASURED contract, import-inert,
`COMP_FIND_TOOL`. Collect 0.07 s; 1 passed; direct 6/6; external mutant beside the tool -> FAIL on
A1/A3 (ran, no denominator). Two fixture defects found by the first run: the ABSENT token was a
literal in the battery, inside its own search scope (found, 1/357); a temp-dir copy could not import
its sibling `_comprail` and CRASHED -- and arm E read the crash as PASS. Both fixed; both in the docstring.
Baseline: the unit-2 acceptance run rewrote it mid-edit; restored, re-run on the committed tree,
"sound BY CONSTRUCTION". CVO 92767 item 3 pre-approved it as unit 2's acceptance baseline.

## Decisions Made

1. Graded my own T-16 pass 1 by the count and not the clock; corrected on the record the moment CVO
   read the module. The rule that came out: **when a runner prints a count AND a duration, the
   duration is a verdict too.** Appended to the clean-metrics memory entry as its second form.
2. Did NOT start the rail diagnosis under CVO's delegation until CVO released it (92617); did not
   start unit 2's edits until the re-scope (92726); did not commit 3a until COO's word (92774);
   asked before taking anything of ~A's (Rule 27) -- CVO answered NONE.
3. Deleted the wrappers LAST, after the registry, after the notice -- the comp-surface-check
   precedent's order, now recorded in the manifest for the next retirement.
4. Read `manifest_check_cli.py:545-562` before relying on the commit-time gate rather than inferring
   "two-phase" from the standalone subcommand's refusal.
5. Refused to treat a mutant that CRASHED as a mutant that FAILED (3b arm E). A dead arm and a wrong
   arm are different failures; the arm now asserts the mutant RAN.
6. Built 3b under a non-collected name and renamed at commit, so an unproven battery never sat where
   the F9 sweep would run it against other seats' commits.
7. Left three things untouched by ruling: the KUZUSPLIT PRD (CTO's lane), the two dated briefs
   (nobody's), and Andrew's verbatim quotation of the wrapper names (:17 of the PRD).

## Files Modified

See commit messages `e66d5e698d`, `03cf4d17ac`, `dffbee781c`, `4c3b848c97`, `1e6206a267`,
`610bb9e31e` -- each carries per-file rationale, red-first evidence and bounds. Memory (outside repo):
rewrote the send_message entry to its resolved cause; appended the count-vs-clock form to the
clean-metrics entry; added the rail-timeout entry's fix note; index lines updated.

## Blockers

None BLOCKED. Gated, each with its citing message:
- T-16 s.4 per-tool pass -- COO 92774 "stands as sequenced"; CVO 92628 "no per-tool pass until you
  have read s.4". The PRD is at `org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_COMPEFFICACY_PRD_DRAFT_v0.1.md`
  (found by name 21:47Z; s.4 being read as this log lands).
- KUZUSPLIT PRD P1/P3 amendment -- `1.0.0_SA_CTO`'s, same window (CVO 92726, 92767). T-22 closes on it.
- Q3 (`comp-tool-hud.sh:182`) -- HELD by COO; the `-f` form rides the next real change to that file.
- ~A's excess work -- Andrew authorized reallocation to this seat; CVO ruled NONE moves (certifier !=
  author). Answered, not dangling.

## Current State

For a reader with no prior context:
- **The step-6 seam is clear fabric-wide.** RC5 (this seat, `03cf4d17ac`) and RC7 (CTO) are GREEN; the
  ETFS_GUARDRAIL RED/HOLD is lifted (CVO 92779). Any new canonical TO can pass the gate again.
- **The rail enforces.** `.claude/settings.json` comp-tool-hud `timeout: 30` (`d2eb720bde`); verified
  4 of 4 Claude seats on body-executed probes. Rule 21's enforcement bound stays HELD by CTO pending
  its own text; the hook file is unchanged at HEAD (Q3 held). **A DENY row in the rail log written
  before 2026-09-02 ~18:08Z is not evidence of a block; after it, at verified seats, it is.**
- **comp-kuzu-inc / comp-kuzu-full do not exist.** `comp-kuzu --mode inc|full` is the surface; the
  NEVER-full guarantee is on the flag in code and every registry. On any box that has not re-run
  `provision-path-shims.sh`, a stale `~/bin` forwarder fails LOUDLY (target missing) -- by design.
- **Three comp-tools now self-report** to `org/mcp/comp-tool-runs.jsonl`: comp-find, comp-read
  (unit 1), comp-adversary (3a). `args_head` is cut at 80 chars by the sink.
- **Two batteries are import-inert under pytest:** `test_comp_adversary_stage4_packet.py` (0.09 s
  collect) and `test_comp_find_battery.py` (0.07 s). Both take a tool-path override for production
  mutants. CVO wants that shape on every battery this project clears (s.4.6).
- **`.tools/tests/**` is this seat's lane** (TOOL_BATTERIES, Andrew via CTO 92637). CTO's RC harness
  graduates on one condition (a `test_` entry point) when moved.
- **3.0.0_SA_CVO~A is deregistered** (Andrew, via COO @a8d63f097c); CVO base holds its lanes.
- Push state as measured above; this seat never pushes (integrator-only).

## Next Steps

- **[0.8.0_AE_CloudComp]** read PRD s.4 (schema, 4.4 Rules P/T, 4.6 battery criterion); then the
  T-16 s.4 per-tool pass on comp-adversary in that schema -- results in any other shape are what
  Andrew told the fabric to stop producing.
- **[3.0.0_SA_CVO]** grade 3a (`4c3b848c97`), 3b (`1e6206a267`), the baseline (`610bb9e31e`); fold
  the 80-char `args_head` cut into the Rule P/T row; name the next delegated unit.
- **[1.0.0_SA_CTO]** KUZUSPLIT PRD P1/P3 amendment -- the last carrier naming wrappers that do not
  exist; T-22 closes on it. Rule 21's enforcement bound text, on your own timing.
- **[2.0.0_SA_COO]** sequence the T-16 s.4 pass once s.4 is read (already "stands as sequenced").
- **[any seat that runs the routing test]** it REWRITES `comp-which-routing-baseline.json` as a
  by-product; a run taken mid-edit flags itself (`working_tree_differs`) -- do not commit that one.
- **[Andrew]** nothing open at this seat.
