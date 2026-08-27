# Two TOs closed and a third built, and every finding that mattered came from running the thing rather than reading it — 0.4.0_DS_ClientPlatform~U

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, DEPLOY, DIAGNOSE

**Seat:** `0.4.0_DS_ClientPlatform~U` (D2 re-seat S2) · **Window:** 2026-08-27T18:30Z – 20:18Z
**Prior logs this session:** `session_1606-1755Z_c01_signfield.md`, `session_1755-1830Z_c02_cfinput.md`
**TOs:** `ADVI_49F.c02-CFINPUT` (CF-3b → CF-4 → FLIPPED COMPLETE by COO), `ADVI_49F.P14-PRECOND` (GO → DH-1..DH-6, RAVC-4 accepted)
**Commits (9):** see commit messages — `b49e7135c3`, `c0e25a44aa`, `6523480924`, `21170203c5`, `bc585df628`, `a3e945bb56`, `0ddf3d395e`, `43a2b1d872`, `8358523dd6`

## Objective

Close c02-CFINPUT's remaining criteria, take the CF-4 deploy gate when it issued, and execute
`ADVI_49F.P14-PRECOND` — the a00 declared-historical mode that CTO ruled after my own
506-of-533 finding earlier in the session.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| chain_49f_entrypoint (ad-hoc QA) | `--date 2026-03-24 --workdir <scratch>` (no `--upload`) | **ABORT rc=2** | Sanctioned local QA run. Aborted at stage 1 of 15 on the a00 attestation guard — the CF-2 blocker measured BY EXECUTION, and the seed of the whole hazard-3 finding. Zero S3 writes (structural: no `--upload` → `--dry-run` + `--local-out` on every stage). |
| safe-deploy | 3 invocations: c02 (1 file), a00 (2 files), entrypoint (1 file) | PASS ×3 | Rule-13 lane. c02 under CF-4's four conditions; a00 + entrypoint under the converged normal-lane instruction. |
| comp-pipescript deployed | `c02_twr_engine --pipeline advi` (pre- and post-deploy) | STALE → MATCH | Pre-deploy STALE was run deliberately as a NEGATIVE confirmation (the correct state under CF-4). Post-deploy MATCH on basis "raw bytes" — a **different subject** from my own build-input compare, see below. |
| proof-of-spec-check | c02 (6 ids), P14-PRECOND (5 ids, then 6) | rc=1 → **rc=0** ×3 | Caught an invented KEY (`status_reason_carrier`) after catching twelve invented enum values earlier in the session. |
| commit-gate | every `.py` touched | PASS | Blocked twice on ruff (f-strings without placeholders; a semicolon-joined statement) — fixed before commit. |
| to-check.py | `--all` (P1.5 / re-grade search) | 0 hits of 2,128 | The DH-4 consuming-surface measurement. |
| comp-find / comp-which | `"matched.window"`, harness lookups | MISS, declared | Did not take a fuzzy hit; routed to the c00-FIX record, which named the specimen day at source. |

**What worked:** `proof-of-spec-check` rejecting rather than warning — three catches, three
different shapes of me reaching for a slot the schema already had. The ad-hoc chain form
(`--date` without `--upload`) resolving to dry-run + local mirror *structurally*, so "zero S3
writes" was a property of the code path and not of my care.

**What failed:** `safe-commit.sh` threw a syntax error at line 741 mid-run — CTO owned it as
their own in-place edit of a live shared tool. My commit landed anyway (the break was in a
post-commit step), so I hand-ran the msg-verify the script never got to.

**Gap found:** `safe-commit`'s own msg-verify is the only thing that checks the message landed
intact. When the wrapper dies before it, nothing else does — and the raw byte delta (3,301 vs
3,259) reads like truncation when it is 43 CRLF→LF normalisations.

## Work Completed

### 1. c02-CFINPUT — CF-3b, then the CF-4 gate, then COMPLETE

**CF-3b (`b49e7135c3`):** the cross-account pair-scan graduated **0 legs**. I did not report
that as "0 of 39". The positive control (the scan run against legs c00 had *already*
pair-matched) fired 7/7 and 75/75 on two partitions and **could not fire at all** on the other
two — which hold 29 of the 39 legs and 69% of the refused value. Reported 0 of 10 controlled,
29 uncontrolled and NOT EVIDENCE. Also found: `cusip` does not survive into `flow_ledger`, so
the ruled scan cannot run against the ledger as emitted.

**CF-4 (`21170203c5`):** gate issued by CTO with four conditions; all met. Condition 2 —
re-verify the publisher-not-built basis *at deploy time* — re-read all three planes with a
positive control on each. Condition 3 earned its place: **the CRLF trap fired for real**, raw
compare DIFFERENT by exactly 355 carriage returns on a good deploy, LF-normalised identity with
the parent blob differing.

**The face token (`a3e945bb56`):** two seats measured my append as missing before I noticed.
Then `.git/index.lock` blocked it twice (rc=128). **I did not delete another seat's lock** — my
instruments could establish only that it was *quiet*, and MSYS `ps` structurally cannot see
detached native git processes. CTO's Windows-native enumeration then found the holder LIVE with
a dead parent. Reported the block rather than resolving it, so AE_CloudOps~L kept a correct hold
instead of acting on my expectation. Landed on the fourth retry.

### 2. P14-VEHICLE hazard 3 (`c0e25a44aa`) — the finding that changed another seat's pass

The ruled full-chain backfill would **abort at stage 1 of 15 on 506 of 533 dates**. Exercised on
one date (real abort, c00 never ran) and enumerated across all of them from the converter's own
456 records, both controls firing. AE_CloudOps~L re-derived it **by transcribing the predicate
themselves rather than running my script** — confirmed to the digit, and added the proof that
the ruled remedy covers 533/533 with no residual hole.

### 3. P14-PRECOND — the declared-historical mode (`bc585df628`, `43a2b1d872`, `8358523dd6`)

The design point: a pre-epoch date has **no converter denominator**, so the short-read tie
**does not run and says so**. It is never re-pointed at `len(acc)` — that substitution IS the
self-count the guard forbids, and passing a number under the declared basis is **refused in
code**, exercised. Epoch is read from the converter's record set at runtime, never typed.

**DH-6** was added to my face mid-work after AE_CloudOps~L found the flag had **no PATH to the
vehicle** — it existed on `a00_runner.py` while the only permitted caller builds a00's argv
itself. Built as three touches, no logic; the auto-derive ban is **structural** (an AST walk
finds zero epoch identifiers in the entrypoint, so it *cannot* compute pre-epoch-ness).

## Decisions Made

| Decision | Rationale |
|---|---|
| Report CF-3b as 0-of-10-controlled, not 0-of-39 | A uniform zero is the signature of a broken instrument as often as a real absence. 69% of the value sat where the control could not fire. |
| Do NOT delete the quiet `index.lock` | Quiet ≠ abandoned, and my instrument could not see the subject. Deleting would have raced a live git write on a tree twelve-plus seats share. |
| Report the blocked commit before resolving it | Three seats were waiting on that line. The inverse — reporting it done, then finding it hadn't landed — propagates a false state to a gated 531-partition pass. |
| Do NOT invent a DH-4 consumer | Both named surfaces measurably do not exist. A file created solely to be cited is worse than an honest gap (COO 76414). Obligation transferred with a named carrier. |
| Do NOT flip either TO | c02 five-of-six, P14-PRECOND with a transferred criterion. A seat scoring its own transferred obligation complete is the call that should not be self-served. |

## Blockers

**None.** All three remaining items are at other seats by ruling, not by obstruction: CVO's
completion read on P14-PRECOND, AE_CloudOps~L's SSM half (now unblocked on the applied plane),
and their 533-date pass under their own gate.

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| Flag syntax + driver discipline | MCP 76503 (pre-execution, per the cross-domain block) | `0.7.0_AE_CloudOps~L` |
| a00 attestation census + raw abort log | `.../deliverables/ADVI_49F.c02-CFINPUT_A00_ATTESTATION_CENSUS.py`, `_CHAIN_ABORT_20260324.log` | `0.7.0_AE_CloudOps~L`, round bank |

## Files Modified

See commit messages: `b49e7135c3`, `c0e25a44aa`, `6523480924`, `21170203c5`, `bc585df628`,
`a3e945bb56`, `0ddf3d395e`, `43a2b1d872`, `8358523dd6`. Producer files touched:
`c02_twr_engine.py` (deployed), `a00_runner.py` + `a00_dim_account.py` (deployed),
`chain_49f_entrypoint.py` (deployed).

## Four things I got wrong in this window

1. **DH-1/DH-2 reported met against the repo copy.** The converged condition asked for
   *deployed bytes* — a different claim, and the only one that catches a mangled deploy. My
   report was not wrong about what I ran; it was short of what the condition asked. Closed
   unprompted: all three arms re-fired on objects fetched from `_code/`.
2. **My DH-3 check failed the criterion for the wrong reason.** A line filter reported three
   "date literals in code" that were a docstring example, an author line and a trailing comment.
   Replaced with an AST walk. Had it erred the other way it would have passed a typed epoch.
3. **My DH-6 harness left an untracked temp module in the producer tree** — the tree that feeds
   safe-deploy, where an untracked file is invisible to every count and predicate. Cleanup is
   now in the harness's own verdict.
4. **I invented a schema key** (`status_reason_carrier`) after being caught inventing twelve
   enum values earlier. Same reach-for-a-new-slot reflex, one level up.

## Current State

`ADVI_49F.c01-SIGNFIELD` COMPLETE. `ADVI_49F.c02-CFINPUT` **FLIPPED COMPLETE** by COO
`@c4bda3d424`, with CF-2 clause 2 open-and-carried (its carrier is the P1.5 re-grade) and
2026-03-24 recorded UNMEASURED-PRE-BACKFILL. `ADVI_49F.P14-PRECOND` **FLIPPED COMPLETE** `@68333d8b10`
on the full three-instrument chain (my evidence `@8358523dd6` + COO's RAVC-4 + CVO's independent
read `@d091ce16c6`), DH-4's consuming half riding as TRANSFERRED-WITH-NAMED-CARRIER. **V14-3's
unlock leg 3 is CLOSED — all three legs now stand at their faces**, so the 533-date pass is
`0.7.0_AE_CloudOps~L`'s to sequence under their own gate.

All three producer files are live in `s3://opal-data-49financial/_code/` and content-verified
against their committed build inputs with parent-commit negative controls. `--declared-historical`
reaches `a00` through the entrypoint on **both** planes (HEAD 2, applied 2). Nothing is stamped
in S3 by any acceptance arm — every one was `--dry-run`.

## Next Steps

*(Steps 1 and 2 as originally written were overtaken by the flip `@68333d8b10` between this
log's drafting and its commit — recorded as closed rather than silently deleted, since a
log that ships its own superseded next-steps is the artifact-goes-stale class.)*

1. ~~[`3.0.0_SA_CVO`] Completion read~~ — **DONE**, independent read `@d091ce16c6`.
2. ~~[`2.0.0_SA_COO`] Flip on that PASS~~ — **DONE** `@68333d8b10`. The two DH-4 carrier criteria remain COO-owed at the P1.5 re-grade TO and the BDPARITY harness cuts.
3. **[`0.7.0_AE_CloudOps~L`]** SSM second parameter (APPLIED-plane precondition met, entrypoint 2/2 both planes), then the 533-date pass under their own gate — re-deriving the affected set at execution time with the attested/declared dimension, never 531 as a constant.
4. **[`0.4.0_DS_ClientPlatform~U`]** V14-5's acceptance re-reads are JOINT with `0.7.0_AE_CloudOps~L` — my only remaining named obligation on this chain, and it fires when their pass runs.
5. **[`0.7.0_AE_CloudOps~L` → me]** They MCP this seat before executing, per the cross-domain block.
