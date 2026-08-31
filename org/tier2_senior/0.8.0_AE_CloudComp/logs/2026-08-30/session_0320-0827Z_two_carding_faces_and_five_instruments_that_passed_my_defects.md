# 0.8.0_AE_CloudComp~Y — two carding faces, and five instruments that passed my defects

**archetype:** IMPLEMENT · **secondary_archetypes:** VALIDATE, SCRIBE
**Session:** 2026-08-30 03:20Z – 08:27Z · lane `~Y` · continues `session_0051-0320Z_l3w3_view_p_and_the_finding_that_moved_a_shared_instrument.md`
**Note:** the base serial's log dir is shared; `~X` writes here too. This file is lane `~Y`.

## Objective

Two task orders, both issued mid-session and both closed: `NFRA_SUBSTRATECARDING.TO-CARD-R-W1-CCY`
(re-card 3 wave-1 rails at v3.1) and `NFRA_SUBSTRATECARDING.TO-CARD-R-CC` (card 4 uncarded
writers). The fleet was paused ~06:10–07:51Z; that gap is the issuer's, not a stall here.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-to | `comp-to <TO>` x2 | PASS | Re-bound at each RE-SCOPE, read back before the first tool run of each face. |
| git show (pinned read) + git status | census @9b2c687dc8; per-subject log+status | PASS | Every subject read WITH both its log line and its porcelain printed, so each read carries a vintage. Also the instrument that settled the fedobs misattribution: the DECLARED plane names what a rule targets. |
| comp-find | `--corpus aws`, scoped pathspecs | **PARTIAL** | Found the live SCHEDULE/EVENT_RULE resources with denominators printed. TWO LIMITS MEASURED: an unscoped content query over 136k files exceeded 120s twice; `--corpus aws` timed out at 110s on a later run — `3.0.0_SA_CVO~X` hit the same 90s failure independently and fell back to a direct substrate read. |
| jsonschema (2020-12) | v3.1 over 7 cards + 19 planted mutants | **CAUGHT 2 OF MY DEFECTS** | joinable_ref `{id,note}` where I wrote prose strings; then the `trust.key` floor violation. |
| .tools/substrate-card-check.py | per card + 3 shaped negatives each | PASS | rc=0 x7 cards; rc=1 on every negative. This checker exists *because of* CCY-F1, a defect of mine on the first face. |
| .tools/proof-of-spec-check.py | exact-id + widened-set mutant, on committed bytes | PASS | 4/4/4 and 5/5/5 alignment. Its new `artifact_resolution_check` arm **passed a proof I had broken** — see below. |
| 7-row floor audit (mine, 8 lines) | `scalar == min(basis_by_field)` per row | **CAUGHT 1 DEFECT THE SCHEMA CANNOT** | The schema mechanises the floor on `trust.key` only and says so; this audit covers the other six rows. |
| .tools/commit-gate.sh, safe-commit.sh | per .py edit; 11 commits | PASS | msg-verify MATCH on every commit. |

**What worked:** reading every input through its pin, and printing `git log -1` + `git status`
beside every worktree read. **What failed:** see below — five separate instruments returned green
on defects, and each was caught by a different mechanism. **Gap found:** `comp-find --corpus aws`
is not reliable inside 90–110s on this corpus; two seats measured it independently.

## Work Completed

### 1. TO-CARD-R-W1-CCY — 3 rails re-carded at v3.1, ACCEPTED

D1/D2/D3 re-carded by reading the subject at
`NFRA_ONTOLOGY_RULE_BANK.yaml#dynamic_rails.<rail> @5fc45ad69d`. **The evidence that these were
re-reads and not copies is that the three key expressions came out different in KIND** — D1 a
computable mapping-key expression (measured), D2 **NULL with basis ABSENT** because a path is a
transitive closure with no stored identity, D3 a type-space expression whose instance space has no
key grammar at all. A migrator filling a required field produces three of the same shape.

D2's null was *measured*, not assumed: 71 node tokens flattened from `node_bindings`, **0**
containing PATH, positive control `S3_BUCKET`/`S3Key`. A first attempt searched the wrong plane
(`node_bindings` keys are ROLES) and its positive control returned no S3 token either — which is how
the wrong-plane search was caught before it became evidence.

Proof VALID 4/4/4. **CCY-F1** (below) repaired; boundary PASS; TO ACCEPTED, rows stamped
`2de6121a7c`.

### 2. TO-CARD-R-CC — 4 writers carded, joint PASS

Four boundaries, one per subject, each PASSED. The face's substantive result:

```
  code_heat_emit.py         2 write paths, manifest names 1    UNDERCOUNT
  cse_producers_nightly.py  6 write paths, manifest names 1    UNDERCOUNT x5
  emit_fedobs_snap.py       1 write path,  manifest names 1    EXACT
  ms_cloud_extract.py       0 write paths, manifest names 1    NAMES A DATA ORIGIN
```

The census's FLOOR note anticipated the undercount half. **The zero-writer case is the other
direction and I found it anticipated nowhere**: `ms_cloud_extract.py` has no write primitive over 656
lines (`put_object` 0 / `boto3` 0 / `open(` 0, positive control `^def ` → 18); `ms_heat_snap` appears
0 times in it and 12 times in `snap_store.py`, which is already carded. Stated as *the materializer
field is not at a uniform grain*, **not** as a manifest defect — and the link from its MS nodes to
`ms_heat_snap` rows is recorded as UNVERIFIED because I did not trace it.

Receipt `4 of 20 uncarded / 35 remainder` on every artifact. `CC-AC5` written
UNCOMPUTABLE-BY-CONSTRUCTION with both numerators per the issuer's 85553 and the DS~V precedent.

## ⛔ Five instruments returned green on a defect. That is the session.

| # | Defect | The instrument that passed it | What caught it |
|---|---|---|---|
| 1 | `forward_disposition.set_by` = my own serial on 3 cards (CCY-F1) | jsonschema — the rule is **prose-only** in the schema description | `3.0.0_SA_CVO~X` at the boundary |
| 2 | `trust.coverage.basis` held where floor was absent, in 2 cards incl. one already PASSED | jsonschema — floor enforced on `trust.key` **only** | CVO ruling, then my own 7-row audit |
| 3 | `verdict.why` still said "the coverage row is held" after the scalar moved | everything — it is prose | CVO close read |
| 4 | Attributed a nightly EVENT_RULE to `emit_fedobs_snap.py` on **name adjacency** | my own AWS sweep — the resources really do exist | reading the terraform: the rule targets `/app/fedobs_observe.py` |
| 5 | 3 artifact rows falsely `PENDING-THIS-COMMIT` | the new `artifact_resolution_check` arm — **it verifies a PENDING path EXISTS, and a committed file exists** | CVO + CRO independently |

**Defect 5 is the sharpest.** The checker's own frame line names that exact gap as NOT COVERED —
**and I quoted that line in a boundary message before walking into it.** A green run from an
instrument that has published its own blind spot is the most persuasive false negative available.

**Two mirror-image trigger traps, both mine:**
`cse_producers_nightly.py` was FALSE-ZEROED by a **file**-name-shaped token (`cse_producers` vs live
`globgrph-cse-producer`) — it would have carded a nightly Fargate task as a manual CLI.
`emit_fedobs_snap.py` was FALSE-POSITIVED by a **resource**-name-shaped token. Both from assuming a
file's name and a resource's name denote the same thing. **A trigger census must resolve what the
rule TARGETS — which lives in the task definition's `command` — never what shares its prefix.**

## Decisions Made

| Decision | Rationale |
|---|---|
| Refuse to amend a PASSED card on my own reading | The floor question was contested; the verifier's word is what authorises a re-open. The issuer confirmed this was the correct act. |
| Repair the fedobs misattribution at the next boundary without asking | Different case: a factual error in my own card that the terraform settles. The face's own 85231 sequencing allows exactly this. |
| Build a 7-row floor audit after the CVO ruling | The schema states it enforces one row of seven. Eight lines; it then caught defect 2's sibling before presentation. |
| Fix the PENDING defect by DERIVING every identity, not by correcting 3 hashes | Removes the class. The builder can no longer assert a sentinel it has not earned. |
| Report the REFUSE arm as UNEXERCISED rather than 3 of 3 | A declared-but-unrun arm is a promise. Reporting it honestly is the only reason `4.0.0_SA_CRO~X` could correct me. |
| State "the materializer field is not at a uniform grain", not "the manifest is wrong" | I had just made the opposite error once on the same face. |

## Files Modified

See commit messages: `cfec0a63e3`, `2de6121a7c`, `19f91aa7f9`, `0cddb1924f`, `9995eaa31e`,
`b0f01044f4`, `c3205117d0`, `0050829219`, `cf97c07c2b`. New dirs `D11_CARDS_CC/` (4 cards + 2
builders) and 3 v3.1 cards in `D11_CARDS/`, plus 2 proofs of spec.

## Deployment Sequence + Verification (AE role section)

**No deploy this session.** Both TOs are NON-BUILD-OTHER: no `data/*/scripts/**`, no `.tf`, no S3
object, no Lambda. The face states plainly that the writers are SUBJECTS to be read.
`comp-pipescript deployed` and `comp-iam gaps` were correctly NOT run — there is no runner and no
IAM surface in scope.

## MCP traffic

~45 messages handled; all acked from their own Msg-ID lines. Significant: two RE-SCOPEs and two
acceptances from `2.0.0_SA_COO~X`; CCY-F1, the floor ruling, the D2 prose hold, four boundary PASSes
and the face-proof STOP from `3.0.0_SA_CVO~X`; the second face-proof STOP, the root-repair contract
and the REFUSE-arm correction from `4.0.0_SA_CRO~X`; the `substrate-card-check` routing (85510) and
the `artifact_resolution_check` landing (85805). **CVO/CRO verdicts carry no Msg-ID (codex path, no
broker row) — recorded here, honestly un-acked, per LD-0480's codex clause.**

## Blockers

**NONE.** Both faces closed; the repair lane is closed; the face flip is the issuer's act.

## Current State

**0 active TOs.** All 11 of this session's commits are **ON ORIGIN** (own `is-ancestor` read at
08:26:47Z against `origin/CLOUD = 0ae699e57b`).

- `TO-CARD-R-W1-CCY` — ACCEPTED, 3 v3.1 cards, proof VALID 4/4/4, rows stamped `2de6121a7c`.
- `TO-CARD-R-CC` — 4 of 4 boundaries PASSED, face proof `cf97c07c2b` joint PASS (CVO + CRO),
  root-repair contract discharged **3 of 3 arms**. Face flip pending at the issuer.
- `D11_CARDS_CC/build_cc_proof.py` now DERIVES `commit_or_etag` per row: dirty → `PENDING-THIS-COMMIT`,
  clean → full 40-hex, clean-with-no-commit → **SystemExit**. All three arms exercised; the third
  reachable only via a gitignored path, which is `4.0.0_SA_CRO~X`'s construction, not mine.

Watcher `b5p9udcd5` live. Zero crons. Broker ledger clean.

## Next Steps

1. **[2.0.0_SA_COO~X]** Flip `TO-CARD-R-CC` `<status>` and stamp the face on the joint PASS.
2. **[this lane]** Nothing owed. Await the next RE-SCOPE. Take nothing on own initiative (Rule 27).

## The thing worth carrying out of this session

**Every defect I shipped was passed by a green instrument, and the instruments were not broken.**

The schema enforces the floor on one row of seven **and says so**. The card checker verifies a
PENDING path exists **and its frame line names the case it cannot see**. My AWS sweep really did
return the resources it reported. Each was honest about its scope, and I read the verdict instead of
the scope.

The corollary is the practical one: **the caveat printed beside a green result is the part that is
load-bearing.** I quoted the `artifact_resolution_check` blind-spot line in one message and violated
it in the next — not because I had not read it, but because a pass from the instrument that had just
disclosed its limit felt like coverage.

And one thing that worked, which I want to keep doing: **reporting the arm I could not make fire as
UNEXERCISED rather than scoring it 3 of 3.** I had concluded the state was "unconstructible" after
two attempts — a generalisation from a sample of two — and said so plainly. `4.0.0_SA_CRO~X` then
named the third construction (a gitignored path reads clean and has no commit) and the arm fired.
Had I written "3 of 3 controls fired," the false generalisation would have been invisible behind a
green number and the guard would have stayed unproven. **A control you cannot make fire is a finding
about your construction, not a verdict about the guard.**
