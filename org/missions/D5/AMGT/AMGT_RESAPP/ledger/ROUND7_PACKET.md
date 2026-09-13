# AMGT_RESAPP ROUND 7 -- the drain-end task-order packet, `2.0.0_SA_COO~ZZZ` to `3.0.0_SA_CVO~Z`

**Round 7 is SIX cells on TWO workers.** Issued @`c9b1fc5ed0` (`fanout: 2 of 2 chains, cap 8`) to
`0.9.0_WK_AMGT_RESAPP~11` (rf-1..rf-5, one chain -- all five write
`lib/research/api/scoped_amgt.py`) and `~12` (rf-6). Drained across five merges: `bb9009c924`,
`458083f0b3`, `88eefbfb5e`, `1effa7ac68`, `a8659e8baa`.

**EVERY TASK ORDER UNDER `AMGT_RESAPP` IS TERMINAL: 43 of 43** -- 40 `complete`, 3 `superseded`,
**0 open** -- with a POSITIVE control (`POSN_ASTTAX` -> **4 open of 15**) and a NEGATIVE control
(`ZZZZ_NOSUCH` -> 0 of 0, out-of-corpus rather than an absence) taken in the same sweep, so the census
discriminates in both directions.

⚠ **THIS ARTIFACT IS NOT THE SPINE'S L8.** The spine's L8 is the CHANNEL compile, whose output is the
compiled channel and the CVO's watermark. This is the COO's drain-end packet, a different artifact
sharing that label; Rule 27 places that ambiguity deliberately and does not resolve it. Nothing here
changes who owns a limb, and nothing here grades a cell.

---

## 1. WHAT L9 OWES -- a list, not a summary

| # | owed | why it is L9's and not mine |
|---|---|---|
| 1 | **Six judgment criteria**, one per cell (`rf-1..rf-5` AC5, `rf-6` AC4) | each carries `judgment="true"`, no children, no verdict; each instance records `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO. A `PASS`/`FAIL` on a judgment row is INVALID |
| 2 | **26 undispositioned rows of 91** (`comp-surprise --project AMGT_RESAPP --json`: `investigation_items 91, open 26, armed 64, adjudication_rows 64, remediation_rows 59, duplicate_ids {}, files 86`) | the 21 minted this round are enumerated in §3 |
| 3 | **Whether five L6 defects in orders I cut change how this round's greens should be read** | §4. Five criteria of mine could not discriminate; three were amended and re-run, two were left for you. This is the round's central question and it is not mine to settle |
| 4 | **Two band-vocabulary criteria, graded on substance by the worker and routed here ungraded by me** | `Z-W11-S3` and `Z-W11-S7`. §5 |
| 5 | **Whether any portal-dependent outcome may be graded REALIZED** | §6. My answer is NO and it binds my own acts, but the grade is yours |

⛔ **GRADE THE `DONE WHEN` STATE LINE, NEVER THE `ACCEPT` PARAGRAPH.** No cell may carry an EXERCISED
outcome to REALIZED on the strength of its own artifact.

---

## 2. THE SIX CELLS -- as the worker reported them, as the checker graded them

**All six instances `VALID rc=0`, graded by the MAIN TREE's `proof-of-spec-check.py` AFTER the drain**,
so the rows the SURPRISES limb resolves are at HEAD. (Round 6's packet had to warn against quoting a
main-tree `INVALID`; that verdict is an artifact of grading a worker's branch from the wrong tree, and
grading after the merge removes it rather than explaining it away.)

| cell | criterion evidence, as recorded | denominator |
|---|---|---|
| `rf-1` | AC1 `SERVED_EQ_REQUESTED=4 of 4`, all four partitions LANDED · AC2 `REFUSED=2 of 2` (both `AdapterError`) · AC3 17 passed -> 1 collection error on the sentinel, `RESTORED_BYTE_IDENTICAL` · AC4 43 hits / 101 files, 10 record-carrying | 10 of 101 |
| `rf-2` | **AC1 `0 -> 3`, and the AGGREGATE MOVED: 835 -> 838 calls, 96 -> 97 roles, 992 -> 1006 lines, positive control steady at 37** · AC2 16 hits / 6603 files against a baseline of 0 of 6601, 11 route keys · AC3 31 passed · AC4 `RESTORED_BYTE_IDENTICAL` | 3 of 1006 |
| `rf-3` | AC1 31 passed incl. `test_fiscal_figure_count_is_183_and_not_zero` · **AC2 `HEADER=13 FISCAL=183 TOTAL=196`** (amended key) · **AC3 `POSITIVE=183 WRONG_SCOPE=0`** (amended, now carries a positive arm) · AC4 `RESTORED_BYTE_IDENTICAL` | 196 of 196 |
| `rf-4` | **AC1 `DENOMINATOR=183 PX_LAST_ROWS=10`, 0 of 10 read the raw 146.58, 10 of 10 full provenance** (amended) · AC2 56 passed, both arms, unresolved -> check face REFUSE · AC3 39 hits / 87 files against a baseline of 28 of 86 · AC4 `RESTORED_BYTE_IDENTICAL` | 10 of 183 |
| `rf-5` | AC1 7 passed / 40 deselected, one test per required response shape · AC2 9 hits / 88 files, `SURFACED=5 TEST=4` · AC3 `MENTIONS_UNPROCESSED=5 HAS_REFUSAL_OR_RETRY=True`, **recorded as WEAK and unchanged in the mutant world** · AC4 `RESTORED_BYTE_IDENTICAL` | 7 of 47 |
| `rf-6` | AC1 18 files / 0 non-ASCII (an 18 that refuses a zero-denominator pass) · AC2 `tsc -b` over 2069 source files · AC3 1 injected error caught, restored byte-identical under an independent sha256 | 18 of 18 |

⭐ **THE INSTRUMENT EARNED ITS KEEP ON rf-2, AND THIS IS THE ROUND'S BEST SINGLE OUTCOME.** Registering
the adapter in `lambda-source-map.json` made `comp-iam` verdict it for the first time and it
immediately found a **real missing grant**: `scoped_amgt.py:522` (`read_coverage_set`) queries the
ARTICLE store while the first-draft IAM covered only the metrics table. **That route would have
returned AccessDenied in production while all 31 local tests passed.** Fixed in the same cell (Sid
`ReadTheArticleStoreForTheCoverageTab`). The worker notes it had read that code twice and the gap
survived both readings.

⚠ **AND IT REFINES `Z-S27` IN A DIRECTION THAT ROW DID NOT COVER.** `Z-S27` says an UNCHANGED
denominator after adding a consumer proves the instrument never saw it. The worker measured the
converse and it does not hold: registering with `source_dir` alone moved mapped roles 96 -> 97 while
calls stayed at 835 and AC1 stayed 0. **A MOVED DENOMINATOR IS NOT A VERDICTED CALL.**

---

## 3. THE 21 ROWS MINTED THIS ROUND -- enumerated, not counted

**Worker-surfaced (11).** `Z-W11-S1` ARMED · `Z-W11-S2` **BLOCKING** ARMED · `Z-W11-S3` INERT ·
`Z-W11-S4` **BLOCKING** ARMED · `Z-W11-S5` ARMED · `Z-W11-S6` **BLOCKING** ARMED · `Z-W11-S7` INERT ·
`Z-W12-S1` ARMED · `Z-W12-S2` ARMED · `Z-W12-S3` INERT · `Z-W12-S4` ARMED.

**Issuer-surfaced (10).** `Z-S32` INERT (disarms W12-S2/S4) · `Z-S33` ARMED · `Z-S34` ARMED ·
`Z-S35` INERT · `Z-S37` INERT · `Z-S38` INERT · `Z-S39` INERT · `Z-S40` INERT (disarms W11-S4/S5) ·
`Z-S41` INERT. (`Z-S36` is `1.0.0_SA_CTO~Z`'s, ARMED, and is that seat's.)

**Every ARMED row naming this seat, and what each still needs:**

| row | still needs |
|---|---|
| `Z-W11-S1` | a worker worktree created with `portal/` ALREADY materialized, or a spawn-face probe that discriminates "not a repo" from "empty answer". Neither has happened |
| `Z-W11-S2` | its **artifact upload** limb only. The package and source-map entry landed and `comp-iam` moved; the upload was DELIBERATELY not taken -- AC1 is a SOURCE-plane criterion and no criterion required a world act. **"Cannot be deployed" is still true and is round 8's** |
| `Z-W11-S6` | nothing from me: the amended AC1 was re-run and met (`PX_LAST_ROWS=10`, 0 of 10 raw, 10 of 10 provenance). **Its disarm is available and I have not taken it** -- it is offered to L9 rather than claimed |
| `Z-W12-S1` | same as `Z-W11-S1`; same condition |
| `Z-S33` | `~11`'s drains recorded NO gitlink change across all five. Condition (a) held every time; the row stays ARMED because the queue is only now empty |
| `Z-S34` | a REMOTE-plane reachability check in the drain path -- a limb in `safe-merge.sh` or a named step in the COO's drain. The incident itself is closed |

---

## 4. FIVE L6 DEFECTS IN ORDERS I CUT -- and this is what §1 item 3 asks you to weigh

| row | the defect, in one line | disposition |
|---|---|---|
| `Z-W11-S2` | rf-2's grant omitted `infra/aws/lambda/`, so AC1 was UNSATISFIABLE inside it | grant amended `545ee5ee82`, narrow |
| `Z-W11-S3` | rf-2's AC2 requires a band no `.tf` can ever carry (68 of 68 `SURFACED` estate-wide) | **NOT amended -- yours** |
| `Z-W11-S4` | rf-3's AC2 was **ALWAYS-FAILS**, and its failure output was identical to the defect it grades | amended `5dc02a83d5`, re-run, met |
| `Z-W11-S5` | rf-3's AC3 was a negative control that **could not fail** (read a key `read_thesis_bundle` does not return) | amended `5dc02a83d5`, re-run, met |
| `Z-W11-S6` | rf-4's AC1 was **ALWAYS-PASSES** -- same spaced-key typo as S4, opposite direction | amended `f5461c6884`, re-run, met |

⛔ **EVERY ONE WAS FOUND BY A WORKER. NONE BY A GATE.** `to-pipeline-gate` verifies a criterion's
GRAMMAR -- one `<invocation>`, one `<expect>`, no compound -- and **nothing in the pipeline runs a
criterion against the world before a worker does.**

⭐ **THE ASYMMETRY THAT MATTERS TO YOUR GRADE:** an ALWAYS-FAILS criterion wastes a worker's time and
gets reported. An **ALWAYS-PASSES** one certifies a defect and gets filed as evidence. rf-4's AC1 would
have graded the uncorrected price bypass as MET -- over zero selected rows, *"no row reads the raw
146.58"* and *"every row carries provenance"* are both vacuously true. **The worker declined that green
rather than bank it.** Four of these five surfaced only because it refused greens it could have taken
and been believed.

**THE TEST I APPLIED TO EVERY AMENDMENT, stated before each and offered here for you to check:** an
amendment that lets a criterion DISCRIMINATE is a repair; one that lowers a bar is laundering. All
three raise the bar -- rf-3 AC2 from always-fails to able-to-fail; rf-3 AC3 gained a POSITIVE arm that
refuses `POSITIVE=0 WRONG_SCOPE=0`; rf-4 AC1 gained a first clause that refuses `PX_LAST_ROWS=0` and a
field selector replacing a substring match that over-selected 110 rows where 10 are price rows.
**I graded nothing** -- in every case the worker re-ran and recorded.

⭐ **AND THE WORKER CHECKED MY AMENDMENTS AGAINST THAT TEST INDEPENDENTLY**, unprompted, and reports
all three are repairs: *"rf-3 AC2's expectation text is byte-identical apart from the key; rf-3 AC3 and
rf-4 AC1 both gained clauses that refuse output the originals accepted -- I falsified that rather than
asserting it."*

**TWO OF THE THREE AMENDED CRITERIA WERE ALSO EXERCISED AGAINST THEIR FALSE-CLAIM WORLD BY THIS SEAT**,
in the main tree, before the worker re-ran them -- so the discrimination is not the worker's
self-report:

```
amended rf-3 AC2 at HEAD (pre-repair)   HEADER=13 FISCAL=0        vs 183 on the branch
amended rf-4 AC1 at HEAD (pre-repair)   PX_LAST_ROWS=10, has_146.58 TRUE,
                                        has_corrected_overlay_status FALSE   -> clauses (2),(3) FAIL
```

⚠ **AND THE LIMIT OF THAT CHECK, because it does not reach every criterion:** rf-3's AC3 is a GUARD,
not a repair criterion -- its claim is TRUE in the broken world too, so the broken-world run proves
NON-VACUITY and never FAILABILITY. Its false world must be MANUFACTURED, which is a mutation, which
belongs to a worker under the mutation-control rule and never to a seat in a shared tree. `Z-S40`
disarmed `Z-W11-S5` on the lead clause of its own condition plus a discrimination it did not
anticipate (**183 is not 196** -- the matcher refused 13 of the block's figures, so "loosened into
matching everything" is falsified directly against the real artifact). **The literal `i.e.` clause of
that row was NOT satisfied and the disarm is a judgment. If you read it as binding, RE-ARM IT.**

---

## 5. THE TWO BAND-VOCABULARY CRITERIA -- routed here ungraded, deliberately

| row | the mismatch | why I did not amend |
|---|---|---|
| `Z-W11-S3` | rf-2's AC2 wants a `route_key` in the **CONFIG or DEF** band; `comp-find` bands every `.tf` route declaration **SURFACED**, 68 of 68 estate-wide against a long-live route as a positive control | the only way to satisfy the literal clause is to abandon the bd-pipeline precedent section 1 MANDATES for the JSON-contract pattern. **That is letting the band label drive the architecture** |
| `Z-W11-S7` | rf-5's AC2 wants a **`CODE`** band; `comp-find`'s vocabulary is `HEAD\|DEF\|SURFACED\|CONFIG\|TEST\|DOC\|COLD` (read from its own `--help`, not recalled). `CODE` belongs to `comp-read --enumerate` | the order is TERMINAL. Amending a criterion after its order closes, to make its grade read better, is the laundering the test in §4 forbids |

**Both were graded on their substantive clauses by the worker, which recorded both readings and
swapped no instrument.** rf-2 AC2: 16 hits / 6603 files against a baseline of 0 of 6601, 11 route
keys, neither DOC nor TEST. rf-5 AC2: `SURFACED=5 TEST=4`, the two-sided shape the clause means.

**A SWEEP FOR THE REMAINDER, run rather than assumed** -- every round-7 criterion that names a band
beside a comp-tool invocation, checked against that tool's printed vocabulary: **2 of 6 orders name
bands; 1 of 2 names an impossible one** (`rf-5`). rf-2's four are all real `comp-find` bands, so S3 is
a different defect from S7: S3's band EXISTS and the ARTIFACT never receives it; S7's band the
INSTRUMENT never emits. **No unreported remainder.**

---

## 6. THE PORTAL THREAD -- one fact, four rows, and it binds the grade

`Z-W12-S2`, `Z-W12-S4`, `Z-S34` and `Z-W11-S1` are four measurements of ONE fact: **round 7's portal
work is VERIFIED AND UNPUBLISHABLE.** The rf-6 hygiene commit `83cc87f2` and the AC4-enabling pointer
`c67281460a` are each reachable from **ZERO portal remote refs** (positive control: the recorded
`e85f6eb84f` -> `origin/DEV`; negative control fires). Publishing either requires a portal push, which
Andrew has frozen on both fabrics.

**`HEAD:portal` is `e85f6eb84f` and equals `origin/SITEZ:portal`** -- I moved it at the rf-6 drain and
**backed it out at `275530053c`** when three seats measured that it would publish a pointer no other
checkout could resolve. The work is not lost: `83cc87f2` is pinned by `wk-amgt_resapp-7-2-portal` in
the shared portal clone.

⛔ **SO: NO ROUND-7 ARTIFACT MAY GRADE A PORTAL-DEPENDENT OUTCOME REALIZED.** rf-6's AC1/AC3 and rf-1's
AC4 are **EXERCISED against a state HEAD does not carry** -- a different verdict from "failed", and the
one the record must show. The single unblocking condition is Andrew's word on publishing the portal
branch, carded at his terminal by `1.0.0_SA_CTO~Z`. Nothing here asks for it.

---

## 7. CARRIED, AND NOT CLOSED BY THIS ROUND

**Nine remediation obligations**, named every tick since round 7 opened and none of them closed here:
`Z-W10-S1` `Z-S23` `Z-S9` `Z-S10` `Z-W1-S7` `Z-W2-S6` `Z-W2-S7` `Z-W7-S6` `Z-W7-S7`. Round 8's input is
that table minus whatever this L9 closes.

**Owed at teardown, not yet done and deliberately so:** `git worktree remove` for
`C:/tmp/wk-amgt-7-1` and `C:/tmp/wk-amgt-7-2` plus their branch deletes. Held until L9 has what it
needs, because a respawn is bound by RULING 1 to the SAME serial and a fresh full checkout on this
device is the OOM-under-memory-pressure case. **The portal branch ref in the shared clone stays until
the gitlink it backs is superseded.**

**State at hand-off:** `dep_stage: EXECUTING` · 43 of 43 orders terminal · channel 91 rows, **0
duplicate ids** · residue 1 path, the known `Z-S14` test-generated false positive · `HEAD` `a8659e8baa`
· **PORTAL FROZEN both fabrics, COMMIT YES / PROMOTE NO.**
