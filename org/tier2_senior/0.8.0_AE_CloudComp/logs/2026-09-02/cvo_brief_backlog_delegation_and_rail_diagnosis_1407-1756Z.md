# The CVO brief, the comp-tool backlog, Andrew's delegation, and the rail that writes DENY for searches that run -- 0.8.0_AE_CloudComp

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE, COORDINATE

**Date:** 2026-09-02, 14:07Z -> 17:56Z (single session, base seat, no lane suffix)
**Task Order:** none dispatched to this base seat. Work arrived as: Andrew-direct (the CVO brief, then
"proceed through the backlog", then "team up with CVO Base ... delegation"), CTO rulings (Q5, Q3, Q4),
COO sequencing (Q3 GO then HELD; Q4 re-homed), CVO delegation (unit 1), and one lane-owner release.
**Status:** all owned work delivered, routed, or explicitly gated. Nothing blocked on this seat.

## Objective

1. Address `CVO_FINDING_comp_similar_provenance_20260902.md` (Andrew-ferried) by MEASUREMENT, not read.
2. Proceed through the inbox backlog naming this seat as owner (Andrew: "proceed through the backlog items").
3. Operate under `3.0.0_SA_CVO` base's delegation (Andrew ~16:53Z, verbatim on the record @1bb6769055).
4. Diagnose the rail-enforcement defect (released to this lane by CVO 92617; mine by CTO ruling before that).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-read | `comp-read <file> --for/--enumerate` (dozens) | PASS | the day's primary instrument; caught the `summary_corpus.py` edit-surface qualifier, the C3 control text, the fptest payload shape, the `.owned-paths` lane line |
| comp-read --enumerate | `comp-read org/XXX.md --enumerate 'Step 1b-F'` | WARN | FALSE ZERO on a line-wrapped token; re-probe on `1b-F` gave the true 1 hit. Recorded in the log body |
| comp-find | `comp-find '<pat>' --all --files` (consumer censuses x4) | PASS | no machine consumer of comp-similar stdout; two consumers of `coverage()`; ANY-lane on `.tools/**` |
| comp-pipescript | `comp-pipescript deployed build_cottonwood_mdpf_slice.py --pipeline mdpf` | PASS | MATCH, basis LF-NORMALISED -- corroborated CVO's E-arm diagnosis on a different instrument |
| comp-similar | `--self-test`, `cluster`, `<a>`, `<a> <b>` (pre and post) | PASS | 7/7 -> 9/9; vintage rendered live post-fix |
| comp-adversary | `--self-test`, `compose <specimen> --no-packet`, `compose --digest-budget 4` | PASS | 5/5 held; bound-1 specimen 0 -> 1 pins; packet basis disclosed |
| comp-system | regen before the two `.tools/` commits | PASS | prescribed regen, no override used |
| comp-which | A.3 exercise at startup | PASS | 106 of 106 resolve AND one ran (resolution is not execution) |
| comprail-gate1-fptest | full run x3, pre-fix hook, fixed hook, pre-T1 hook copy | WARN | 47/47 on a hook with a live defect; found structurally blind THREE ways (see Decisions 9) |

**What worked:** comp-read's qualifier surfacing and comp-pipescript's live deployed sweep each produced a corroboration on a DIFFERENT instrument from the seat that filed the finding -- Rule 22 corroboration, not repetition, twice.
**What failed:** comp-read `--enumerate` returned a false zero on a token wrapped across a line break (`Step 1b-F` in `org/XXX.md`); the unwrapped token found it. Line-grain enumerate cannot match across a newline and says nothing about it.
**Gap found:** `.tools/comprail-gate1-fptest.sh` cannot construct a `path`-shaped payload (every `gpath` branch unreachable), is order-dependent on the per-session nudge throttle, and feeds stdin with no harness deadline -- so it certified the T1 rail green while the harness discarded roughly half its DENYs. Three blindnesses, one suite, one day. Surfaced to `1.0.0_SA_CTO` (rail owner); not fixed here.

## Work Completed

Eight commits under this author line, all via `safe-commit.sh -F`, all gate-clean. Push state measured at 17:50:09Z against origin/CLOUD `87728e42cd`: seven ON ORIGIN (integrator ran three times during the session), `ff15b94559` LOCAL. Perishable.

### 1. comp-similar D1/D2/D3 -- `b8a73cc064` (ON ORIGIN)
CVO's brief rested on source, not exercise (corpus would not build on their device). It builds here. All three confirmed by exercise, then fixed. D1 landed in `coverage()` (not the comp-similar surface) because `build_w1_cards.py:96` is a second consumer -- the defect was in what they share. Root cause: the vintage rides comp-kuzu's STDERR and `_kuzu_json` read stdout. My first fix also read stdout, self-tested GREEN 8/8, and still rendered UNKNOWN live; caught only by re-running the exercise. Hence C3c (a verbatim real header must parse to MEASURED) beside C3b (which had committed C3's own defect: testing only the path that already worked). 9/9, two planted mutants each reddening only its own clause, byte-exact restore. CVO retracted their own s.2 within the hour -- the vintage line I added is what let them see their failed run had hit a cold DB built 27 min later.

### 2. comp-pipescript E arms -> assert the PROPERTY -- `4a6f564c6f` (ON ORIGIN). F9 GATE GREEN
CTO Q5 ruling implemented as written. The E arms pinned a live mutable object's digest and failed when the world moved; now they fetch the ETag at run time and assert the classifier agrees with an independent LF-normalised compare. Added SKIPPED as a third verdict (PASS/FAIL-only encodes non-evaluation as a verdict). The live arm nearly shipped decorative: `WinError 193` on the shebang shim, swallowed into a permanent silent SKIP; caught because a SKIP on a box that had just reached S3 did not add up; routed through `git_bash_resolver.bash_argv`. 19/19. Planted mutant (LF normalisation disabled) turned all four live arms RED; E2b caught the mutant lying about its own basis. The gate then ran on my own next commit: `141 passed`. No seat needs `PIPESCRIPT_SUITE_SKIP` for this cause.

### 3. comp-adversary `:49` COMMIT_RE + zero-pin guard -- `a9dc767e34` (ON ORIGIN). Bound 1 CLOSED
Measured the bytes first (CVO said "prev char = backtick", CVO~C wrote `@`hash``; those imply different fixes): form is `` @`6bac8e6cdb` ``. `@`?([0-9a-f]{7,40})\b`. Specimen went 0 -> 1 pins, source 1 `1 attempted / 1 verified`. Scoped to an optional backtick after `@` only -- a bare backticked hex run is NOT promoted (md5s/ETags/snapshot ids). Zero-pin guard gains CVO's predicate (commits==0 AND raw hex>0) and PRINTS the runs. Discriminating pair: same profile shape, hex present FIRES, hex absent SILENT. CVO: "keep that split; do not widen the regex later."

### 4. ascii -- `6412cb26f7` (ON ORIGIN)
I introduced 8 U+26D4 glyphs across four files and landed them in two commits before the gate warned on the fourth file -- the non-ASCII check is path-scoped to `.tools/`. Attribution measured at the pre-edit pins, not assumed; the pre-existing mojibake at comp_similar.py:262 left alone and named.

### 5. Q4 both halves -- `8ed23144cb` (ON ORIGIN)
Re-homed to this seat by COO 92538 after CVO declined the consumer half on charter. Producer: comp-read `_shape()` routes on the python SHEBANG for extensionless files (`.tools/comp-adversary` 10 sections/top-level-keys -> 22/python-ast; `.tools/aws` bash stays generic -- negative control). Consumer: comp-adversary's packet prints `digest basis:` per file and a rollup, so a changed backend is DECLARED, not left for a diff to find. Red-first both halves. Surfaced: `test_comp_adversary_stage4_packet.py:151` calls `sys.exit()` at module scope -- green battery, uncollectable under pytest. CTO took it (92575, 92581).

### 6. Andrew-direct record -- `1bb6769055` (ON ORIGIN)
Verbatim, channel, time; broadcast to COO/CTO/MSTR the same turn; both senior seats concurred "no wider, no narrower" (CTO 92604, COO 92606). Deliberately did NOT read "these matters" as closing my second open call.

### 7. CVO delegated unit 1 -- `f34122edfb` (ON ORIGIN). GRADED CLEARED by exercise (CVO 92628)
comp-find and comp-read made ZERO `comp_log_auto` calls (3,722 and 2,401 rail rows / 0 runs.jsonl rows over 30d); comp-pulse reads runs.jsonl, so it was blind to both. Added `_self_report(rc)` mirroring comp-which's. Negative control pre-change content-matched by token (0/0); acceptance post-change with distinct tokens against the 30s dedup (1/1 each, all fields populated, both denominators). Lane bound checked before widening: `.tools/**` -> `lane: ANY` (`.owned-paths.yaml:1856` -- I cited :1847 in the commit and CVO corrected the line number; substance stands). Surfaced: comp-adversary is a third tool with 0 calls; comp-read `--enumerate` writes no rail row; comp-find has no battery at all.

### 8. Rail-enforcement diagnosis -- `ff15b94559` (LOCAL)
`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/FINDING_COMPRAIL_HOOK_STRADDLES_ITS_OWN_5S_TIMEOUT_20260902.md`. See Decisions 8-10. Routed to CTO (record holder), CVO, COO (92638-40). NOT fixed: Q3 is HELD on the hook file, COO placed the `-f` predicate to ride the enforcement fix, CTO gates the rail.

## Decisions Made

1. **Q3 (`comp-tool-hud.sh:182`) -- built it, then reverted it, and agree with the hold.** COO's GO rested on a "false-gate" half CVO falsified. My own diagnosis: COO/CVO measured the Bash rail (`_search_seg`), I measured the native-tool nudge (`gpath`) -- different mechanisms, both right. The residual is advisory-only. Not enough to touch the widest-blast-radius file. Working tree restored to HEAD (my uncommitted edit had been LIVE fabric-wide for ~20 min -- hooks run from the working tree). Patches saved off-repo.
2. **My background falsifier run contaminated COO's rail measurement** (pids 829235/834026, 16:03Z) -- it toggles the marker that arms the rail, takes no lock, announces nothing. COO nearly filed a false estate-wide "rail disarmed." Owned it plainly. Will not run it in the background while other seats are live.
3. **My own Q3 test cases were unsound** -- one SID per run, so the nudge throttle silenced every NUDGE-expecting case after the first (51/52). Not landed.
4. **send_message "body is EMPTY" -- cause UNRESOLVED.** I claimed subject length; CVO refuted it with receiver-side data (subj 213 landed); my controlled arm killed the plural-path hypothesis too. Memory entry rewritten to say unresolved, workaround-not-fix. First single-variable isolation later: removing a literal `'<token>'` from the body flipped refused -> delivered with nothing else changed (n=1, candidate).
5. **Refused to build off a one-line relay** (92527 never reached this seat -- absent at every delivery state). COO: "correct, and the relay gap was mine."
6. **74-file revert (CTO~Y 90045): closed without action.** All 10 named files tracked, clean vs HEAD, and GENERATED (`comp_closure.py:80`, `:834-854`, `:53`). A re-run today is new work wearing a restoration's name. COO: "recorded so nobody re-opens it."
7. **Did not treat CTO's battery placement as a dispatch** ("no TO until step 6"), and did not start the rail diagnosis under the delegation until CVO released it explicitly (92617: "his word did not move it").
8. **The rail defect, diagnosed:** `settings.json` registers the hook with `"timeout": 5`; its deny path takes 3.0-6.1 s on this box (N=10, mean 4,763 ms, 5 of 10 over 5 s; per-spawn jq 200 / grep 273 / date 401 ms). Discriminator: hook on stdin in isolation 10/10 rail rows; same hook under the real harness, five concurrent bare gated searches, 0/5 rows and 5/5 EXECUTED. Same seat had refused a sequential probe an hour earlier. One mechanism, all four states (a)-(d). Kills the `--model/--effort` argv correlation (same seat, same flags, five (c)).
9. **My own onset story, falsified before it landed.** I had written conditionally that T1 (08-28) pushed a fitting hook over. Measured the pre-T1 hook (`22947cd7ab`) beside the live one: 12-30 s, mean 20,168 ms, SILENT. FOUR TIMES SLOWER. T1 built a DENY on a hook that had never met its deadline, and made the path faster (20 s -> 4.8 s) -- enough to turn a guaranteed miss into a coin flip. The 5 was set at creation (06-15) and never changed. A subtraction is not a measurement.
10. **Probe discipline, four instances in one day, two mine:** every ALLOW-path probe (pipe-receiver, `# rail-checked:`) agreed with whatever its seat already believed; my log delta was a same-call delta (PreToolUse writes before the body runs, so it could only read 0 -- the 1 I saw was another seat's row). The only sound enforcement probe is a bare gated search where you record whether the BODY EXECUTED. Every agreement between probes today was manufactured by the instrument.
11. **RC harness graduation into `.tools/tests` (my lane per Andrew via CTO 92637): ACCEPTED on one condition** -- it collects zero tests under pytest (no `test_*` function; correct `__main__` guard). A `def test_all_controls()` wrapper, ~5 lines, mine to add on arrival. Sent 92641.

## Files Modified

See commit messages: `b8a73cc064`, `4a6f564c6f`, `a9dc767e34`, `6412cb26f7`, `8ed23144cb`, `1bb6769055`, `f34122edfb`, `ff15b94559`. Every one carries per-file rationale, red-first evidence, and its own bounds. Memory (outside repo): two new reference entries (send_message refusal -- unresolved; rail DENY row is not a block) plus index lines.

## Blockers

None BLOCKED. Four GATED, each with its citing message:
- Q3 `comp-tool-hud.sh:182` -- HELD by `2.0.0_SA_COO` 92538/92539; my diagnosis agrees (92541). The `-f` form rides the enforcement fix when COO sequences it (COO 92606 placement).
- comp-kuzu wrapper retirement -- HELD by `3.0.0_SA_CVO` 92617 pending Andrew's KUZUSPLIT reconciliation. "DO NOT touch the kuzu wrappers until you hear from me."
- Any per-tool pass under NFRA_COMPEFFICACY -- gated by `3.0.0_SA_CVO` 92628 on reading PRD s.4 (the result schema). PRD not in the worktree at 17:52Z.
- T-16 (stage-4 `sys.exit`) and the RC harness move -- await `2.0.0_SA_COO` sequencing after the PRD (CTO 92581 "no TO until step 6"; CVO 92628 "COO sequences").

## Current State

For a reader with no prior context:
- **Seven of eight commits are on origin/CLOUD** (`87728e42cd` at 17:50:09Z). `ff15b94559` (the rail diagnosis record) is LOCAL; this seat never pushes (integrator-only, LD-0367/0368).
- **The F9 comp-pipescript suite gate is GREEN** (141 passed, exercised on three of my own later commits). `org/modules/graph/tests/test_pipescript_digest.py` now fetches the live ETag via `.tools/aws` through `git_bash_resolver.bash_argv` and has a SKIPPED verdict.
- **comp-similar** discloses `corpus built: <ts> (age) DB <name>` in all four modes; `summary_corpus.coverage()` carries `corpus_built/corpus_age/corpus_db/corpus_vintage_claim`. NOTE: `summary_corpus.py` is baked into the globgrph derive container image (deploy ledger 20260718T2051Z L2) which now carries pre-fix bytes -- additive-only, no crash either side; rebuild is `0.7.0_AE_CloudOps`' call.
- **comp-adversary** parses `` @`hash` `` pins; prints `digest basis:` per packet digest.
- **comp-read** routes extensionless python (shebang) to the AST backend; self-reports to `org/mcp/comp-tool-runs.jsonl`. **comp-find** self-reports too. Rail writers untouched.
- **The rail hook** (`.tools/hooks/comp-tool-hud.sh`) is UNCHANGED at HEAD (my Q3 edit reverted). It is registered with `timeout: 5` and takes 3-6 s; **a DENY row in `org/mcp/comp-which-rail.log` does not mean the search was blocked.** Remedy proposed in `ff15b94559` (raise timeout to 30 outside the held file now; cut spawns riding Q3). Not implemented; CTO/COO decide.
- **`.tools/tests/**` is a minted lane on this seat** (TOOL_BATTERIES, @30ae4e67c2, Andrew-approved via CTO's card). My `/open-calls` CALL 2 is therefore CLOSED as answered elsewhere.
- **Andrew's standing direction:** this seat works under `3.0.0_SA_CVO` base's delegation for the comp-tool efficacy project (NFRA_COMPEFFICACY, D11, register ask at MSTR, PRD pending). Lane ownership unchanged; a CVO delegation does not lift a COO hold.
- Rail log rows added by this seat's probes, all identifiable: `ZZZTIMING_CC_0902` x10 (DENY, isolation), `ZZZFALS_CC_0902_1..5` (0 rows -- harness killed the hook), `ZZZNEG_/ZZZACC_` x2 (unit-1 controls). The rail log was ruled uncitable for compliance before any of these.

## Next Steps

- **[1.0.0_SA_CTO]** rule on the rail remedy (92638): (i) `timeout` 5 -> 30 in `settings.json` now; (ii) spawn cut riding Q3. Fold `ff15b94559` into the finding record @`8ff3c970a7` or say where it goes. Name release condition 5 in one line (asked 92638).
- **[2.0.0_SA_COO]** sequence the enforcement fix (Q3's `-f` rides it per your placement) and T-16 + the RC harness move once the PRD lands.
- **[3.0.0_SA_CVO]** land NFRA_COMPEFFICACY PRD s.4; delegate the next unit. I read s.4 before any per-tool pass.
- **[0.8.0_AE_CloudComp]** on COO's word: T-16 (`test_comp_adversary_stage4_packet.py:151` `sys.exit` -> `__main__` guard + `test_` entry point) and the RC harness graduation (~5-line wrapper, `test_` filename). On CTO's word: whichever rail remedy is ruled -- and the acceptance for it must include a bare gated search through the REAL harness recording whether the body executed, or it is certified by the instrument that certified the defect.
- **[0.7.0_AE_CloudOps]** decide whether the globgrph derive image is rebuilt for `summary_corpus.py` (surfaced 92515; no crash risk; repo and image have diverged).
- **[Andrew]** nothing open at this seat. CALL 2 closed via CTO's card.
