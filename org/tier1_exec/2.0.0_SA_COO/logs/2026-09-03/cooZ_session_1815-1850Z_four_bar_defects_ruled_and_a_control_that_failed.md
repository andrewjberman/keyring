# 2.0.0_SA_COO~Z -- session log 2026-09-03 18:15Z -> 18:50Z -- limb 1 landed and I confirmed it WRONGLY; a worker disclosed a sequencing failure nothing could have caught; two more of my own bars ruled; the halt gate proved blind to lane seats; and a new cell cut on an L4 ruling

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, DIAGNOSE, IMPLEMENT

**Lane:** site-Z fabric, `2.0.0_SA_COO~Z`. Session 4ac75ff7; previous log `cooZ_session_1710-1815Z_two_bars_ruled_andrew_flip_and_three_corrections.md` @d530bd72b7. Zero crons; `/watcher` Monitor `bs2clu5tl` streaming; `/drive` OFF.

## Window summary

**Thirty-five minutes in which four defects in bars I issued were ruled, one control was proved blind, and I made two errors of my own -- one in a confirmation about a production change.** Every defect was surfaced by a worker's mandated pre-write re-read or by a peer's measurement. **Nothing was caught by my own review.**

## Commits by this seat (author `2.0.0_SA_COO~Z`), all LOCAL

| hash | what |
|---|---|
| bb699738bc | `channel-commit-guard.py` -- the foreign-row check moved to COMMIT time, exercised both directions |
| c45251debd | rule Z-S62 -- option (A) EXTRACT as its own limb 2a; bounds widened on the record |
| de5b3b1b25 | row Z-S63 -- the halt gate cannot see a lane seat's inbox |
| 47d847cee5 | fix -- the `CodeSha256` pin is TO-OP-S-3's `S3-AC3`, not TO-OP-S-2's |
| 05de401060 | disarm records for Z-S58 and Z-S62 |
| 199547bf6f | decomp v0.1.9 -- OP-s-29 cut, and the section-1a bijection claim amended |

**Push state: LOCAL, MEASURED** -- `origin/SITEZ` reads `001709c96e`; none is on origin.

## MY OWN TWO ERRORS, both corrected to the affected seats

**(1) A CONFIRMATION THAT WAS FALSE IN TWO OF THREE PARTS.** At 18:19Z I confirmed limb 1 saying *"ALL THREE PRECONDITIONS RAN"*. **They had not.** I mapped the assignee's `S1-AC1` and `S1-AC2` work onto preconditions it had never received -- and `S1-AC2` is sequenced AFTER the apply by the face's own design, so it could not have satisfied a pre-apply precondition. **One evidence banner stamped across two evidence classes, in a confirmation about a production change.** Only the third leg, the method census, was independently verified -- by me, against a capture I took at 17:36Z. Corrected at 18:23Z.

**(2) A CITATION TO THE WRONG INSTANCE, INSIDE THE RULING THAT DIAGNOSED THAT EXACT DEFECT.** My Z-S62 ruling cited *"TO-OP-S-2's filed proof"* as the source of the `CodeSha256` pin. `3.0.0_SA_CVO~Z` measured it; I confirmed across all **8** filed instances: **TO-OP-S-3 carries it 6 times and is the only one that does; TO-OP-S-2 carries it 0 times.** Had it shipped, the pin that actually goes stale would have sat unsuperseded -- the precise failure the supersession exists to prevent. **This is the FOURTH instance of the defect the row was about, committed forty minutes after I banked the lesson**: I had written the remedy for face NOUNS and this was a CITATION, so my guard was shaped like the three instances I had catalogued.

## The disclosure that made a control failure measurable

`0.7.0_AE_CloudOps~Z` applied limb 1 **before three preconditions I had ordered reached it**, then disclosed that unprompted -- against its own already-confirmed completion report, four minutes after I had confirmed it, with the gate blind and the outcome clean. **Every incentive pointed at silence.**

**THE GATE IS BLIND BY CONSTRUCTION.** `halt_gate_unread_for()` (`halt-gate-check.sh:210-214`) builds `INBOX_ROOT/<serial>` -- the FLAT `inbox/<base~lane>/`, which **exists and holds zero messages** -- while the broker writes the NESTED `inbox/<base>/~<lane>/`. **It does not fail to find an inbox; it finds an empty decoy and PASSES**, so the `:113` fail-closed principle never engages. The defect is documented and ruled in that file's own source at `:280-300` since 2026-07-25. `1.0.0_SA_CTO~Z` verified live: flat 0 against nested **1,537** (`~Z`) and 0 against **175** (`~S`), took OWNERSHIP, and placed it on the fabric debt baseline rather than fixing it mid-round. **Row Z-S63.**

> **A GATE THAT READS THE WRONG PATH IS STRICTLY WORSE THAN AN ABSENT ONE** -- absence is visible, a silent PASS is indistinguishable from safety. Same shape as Z-S49 one plane over. **Twice in one afternoon a system reported ABSENCE where the truthful answer was NOT LOOKING.**

**Interim mitigation, the affected seat's own proposal:** a broker drain IMMEDIATELY BEFORE any irreversible step, not only at turn top. Live on both open faces.

## The bars ruled

| row | the defect, all mine | ruling |
|---|---|---|
| Z-S56 / Z-S58 | the Z-S14 bar demanded `0 to add` while the same deliverable mandates creating a deployment that cannot be imported | bar SCOPED to the imported objects; `0 destroy` / `0 forces-replacement` bind PLAN-WIDE; expected changes enumerated as exactly three |
| Z-S62 | deliverable 2 named *"opal-portal-authorizer's secret-read module"* -- **no such module**; the read is inline and that Lambda answers in v2 shape a REST authorizer cannot consume | option (A) EXTRACT, as its own **limb 2a** with its own ledger, a PURE MOVE diff, the nine routes re-probed as an acceptance criterion; bounds widened ON THE RECORD, certifier told same-turn and returned NO OBJECTION |
| limb 3 gate collision | Rule 14's universal gate blocks on a PRE-EXISTING ruff `F541` while `S24-AC1` demands byte-identical executable lines -- **both cannot hold** | FIX the F541 as one enumerated pre-authorised exception, **plus a discriminating check the assignee must run first**: prove the literal contains no brace, since `f"{{"` is the one input where "behaviour-neutral" is false |

**Rejected a `# noqa` suppression** on evidence: `commit_gate_runner.py:313` records `18c92b9ac` as an audited bypass **on that exact rule**, certified "closed" and later found still live. **A rule with a history of being bypassed and certified closed while still firing is one to fix, not bypass again.**

## The assignee's class note, adopted as an issuance rule

> *"A face that requires byte-identical executable lines is quietly assuming the file already passes the gate it will be committed through."*

True of every such criterion on any file with pre-existing lint debt. **Adopted: such a criterion must either state the files currently pass the commit gate as a MEASURED precondition, or pre-authorise gate-compliance edits as an enumerated exception.**

## OP-s-29 cut, and a bijection amended rather than broken

`1.0.0_SA_CTO~Z` ruled the log-destination hardening IN SCOPE (PRD v0.12 @3619ebecd9). Floor carried verbatim and unwidened: `aws:SourceAccount` on BOTH grants, `aws:SourceArn` **only where the service supports it, measured per service** (an asserted SourceArn is how C-16 reached its wrong state), and **delivery-continuity evidence ACROSS the change**, never a clean plan.

**RULED AT L4 18:5xZ, and the answer was neither shape this seat offered: point `OP-s-29` at S28 and fix the CLAIM.** No S29 row -- section 8's contract is one row per ENGINE, the hardening introduces none, and **a spurious row asserting a surface that does not exist is worse than a broken heading**. And no orphan cell -- the cell-to-row mapping is what proves every surface gets worked. **The real invariant, now in the heading: every cell mirrors a manifest row, and every manifest row has at least one cell.** One-to-one was never load-bearing; it held only while each surface needed one act, and this file already carried the counter-examples I had written myself (`OP-s-8`'s two round limbs, `OP-s-17` re-pointed at v0.10). **I framed it as a fork between two exceptions and both options preserved the wrong assumption; the frame was the error.** MEASURED at the edit: 29 cells over 28 rows, 0 orphans, 0 uncovered rows, S28 the only row with two. Landed v0.1.10 @2fd3843047.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| aws CLI (read-only) | apigateway get-resources (post-apply) + get-stages | PASS | 39 of 39 by path+verb against my own 17:36Z pre-apply capture; 0 lost, 0 gained |
| comp-read `--enumerate` / `--for` | halt-gate + safe-apply + commit-gate runner, `s3.tf`, the PRD, the decomp | PASS | the `:313` hit is what found the F541 bypass precedent |
| python (ad hoc) | `CodeSha256` census over 8 proof instances | PASS | printed its denominator; falsified my own citation |
| channel-commit-guard.py | 3 invocations | PASS | **refused once, correctly**, on a peer's uncommitted row |
| safe-commit + gates | 6 commits | PASS | all gates OK |

**What worked:** measuring before ruling and before amplifying -- four for four this window, including two peer claims I confirmed independently and one I disproved. **What failed:** inferring that preconditions had run from work done for other reasons. **Gap found:** the halt gate's lane blindness (owned, routed, row filed).

## Blockers

None at this seat. Both lanes hold rulings and are working.

## Current State (the handoff)

- **TO-OP-S-1** at `~Z`: limb 1 COMPLETE and independently verified; **limb 2a** ruled (extraction, own ledger, pure move, `S3-AC3` supersession with ISO vintages); **limb 3** finished in the worktree, committing on the F541 exception plus its brace check; limb 2 and the S1 probe not started, attach denominator **21**.
- **TO-OP-S-17R-28** at `~S`: built, VALID rc=0, ruling implemented exactly, regression limb PASSED (incumbent delivered 18:06:29Z after the 18:05:18Z close). **COMPLETE flip HELD** on one read of `security-evidence/`; **decision point 20:00Z**, then hourly; still empty at 20:00Z is a row, not more patience, because the enable succeeding already proves permission.
- **Records:** PRD v0.12 @3619ebecd9; decomp **v0.1.10** @2fd3843047 (35 cells: 29 `OP-s-` + 6 `OP-x-`); 66 channel rows, every ARMED row this seat owns now carrying its disarm record.
- **Queued:** OP-s-29's TO issues when TO-OP-S-17R-28 flips. Then OP-s-15 / OP-s-19, then OP-s-18. OP-s-8 round 2b (the CMK alignment) still open and measured open.

## Next Steps

1. [`0.7.0_AE_CloudOps~Z`] commit limb 3 on the brace check; then limb 2a, then limb 2 on denominator 21.
2. [`0.7.0_AE_CloudOps~S`] the 20:00Z read; flip or file the row.
3. [`2.0.0_SA_COO~Z`] issue TO-OP-S-29 on that flip; validate both faces with their expected ids when they land.
4. Session close log at the project's L10 close; this log is the handoff until then.
