# AMGT_RESAPP ROUND 6 -- the drain-end task-order packet, `2.0.0_SA_COO~ZZZ` to `3.0.0_SA_CVO~Z`

**Round 6 is ONE cell.** `AMGT-re-1`, the recut of `AMGT-rd-8`, issued @`4352fe1c47` to
`0.9.0_WK_AMGT_RESAPP~10` and drained @`b2cd6e9ee7`. Every task order under `AMGT_RESAPP` is terminal:
`_open_tos_for_project(root,'AMGT_RESAPP')` at HEAD returns `[]` of **37**, with a POSITIVE control
(`POSN_ASTTAX` -> 5 open of 15) and a NEGATIVE control (`ZZZZ_NOSUCH` -> [] of 0) beside it.

⚠ **THIS ARTIFACT IS NOT THE SPINE'S L8.** The spine's L8 is the CHANNEL compile, whose output is the
compiled channel and the CVO's watermark. This is the COO's drain-end packet, a different artifact
sharing that label; Rule 27 places that ambiguity deliberately and does not resolve it. Nothing in
this document changes who owns a limb.

---

## 1. WHAT L9 OWES, as a list and not a summary

| # | owed | why it is L9's and not mine |
|---|---|---|
| 1 | **`AMGTre1-AC6`**, the judgment criterion | `judgment="true"`, no children, no verdict. The instance records it `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO. A `PASS`/`FAIL` on a judgment row is INVALID, so the worker correctly recorded rather than graded it. |
| 2 | **8 undispositioned rows of 64** | `comp-surprise --project AMGT_RESAPP --json`: `denominators.open = 8`, `investigation_items = 64`, `adjudication_rows = 51`, `remediation_rows = 29`, `defects = 0`, `malformed = 0`, `files = 82`. The eight, enumerated, are in section 3. |
| 3 | **Whether the four named gaps are CLOSED or merely ANSWERED** | A completed verification cell is not a passed one. The worker's own deliverable `AMGT-re-1.four-gaps-closed.md` cites file-and-change for 4 of 4; whether each is the gap L9 meant is L9's read, not the issuer's. |
| 4 | **Whether AC2's and AC3's controls actually repaired rd-8's defect** | That is the whole point of the recut and it must not be graded on the issuer's word. See section 4. |

⛔ **GRADE THE `DONE WHEN` STATE LINE, NEVER THE `ACCEPT` PARAGRAPH.** No criterion of this cell may
carry an EXERCISED outcome to REALIZED on the strength of its own artifact. In particular: the
`/api/scoped/amgt` read path is CODE THAT EXISTS, not a served route (see `Z-W10-S3`).

---

## 2. THE SIX CRITERIA, as the worker reported them and as the checker graded the instance

Instance: `deliverables/0.9.0_WK_AMGT_RESAPP~10/AMGT_RESAPP.TO-AMGT-re-1.lead-panel-recut.proof_of_spec.json`
-- **VALID rc=0**, graded by **the worktree's own** `proof-of-spec-check.py` run from inside that
worktree.

⛔ **AND THE MAIN TREE'S COPY SAID `INVALID`. DO NOT QUOTE THAT.** Run from
`C:/Users/Opal Bloomberg/Desktop/ajb_workspace`, the checker returned `INVALID (rc=1)` with
`artifact-resolution/CHECKER-SCOPE` plus four phantom "row resolves to NO row" violations -- because
the checker grades the tree it lives in and the rows were committed on the worker's branch. That is
not a finding against the instance. Quoting the first verdict would have failed a clean cell.

| id | shape | invocation result | denominator |
|---|---|---|---|
| AC1 | build | `tsc -b --force` -> no lines, exit 0 | 0 `error TS` lines of 2069 source files examined |
| AC2 | **VACUITY control** | `tsc -b --force --listFiles \| grep -c` -> **2069** | 2069 of 2069 files the referenced-project build resolves; 18 under `src/pages/SecurityAnalysis/`. **ZERO WAS THE EXACT DEFECT rd-8 SHIPPED** |
| AC3 | **MUTANT control** | inject `TS2322`, recount -> **1**, then restore | 1 of 1 injected error; restore verified by 3 reads |
| AC4 | negative census | `comp-find "Replica\|PlaceholderOnly\|__fixtureOnly"` -> **0 hits across 18 files** | baseline at `e6057f26` was 2 hits over the same 18 |
| AC5 | cache collisions | `comp-cache collisions` -> within budget | 523 of 523 portal files, 126 of 126 `useQuery` sites, 17 shared keys, 0 AMGT keys among them |
| AC6 | **judgment -- L9's** | RECORDED, not graded: render check clean, 4 of 4 declared combinations across 16 panel states, 828 elements, 0 colour-law violations, reader control discriminates, 16/16 adapter tests pass | 4 of 4 gaps cited file-and-change |

⭐ **AC2 AND AC3 ARE THE RECUT'S SUBSTANCE.** rd-8 FAILED because both its instruments measured a
STAND-IN: `--noEmit` against a `files: []` references-only root examined ZERO source files (the
textbook always-passes), and `renderCheck.tsx` rendered a `PrintTriggerButtonReplica` rather than the
route (true-and-insufficient). AC2 now PRINTS the file count and declares zero NOT MET; AC3 injects a
type error and requires the same instrument AC1 uses to CATCH it. **Both controls fired: 2069, and 1.**

---

## 3. THE EIGHT UNDISPOSITIONED ROWS, enumerated -- NOT a count

| row | standing | surfaced by | what it says, in one line |
|---|---|---|---|
| `Z-S23` | ARMED | `2.0.0_SA_COO~ZZZ` | both rd-8 FAILs measured a STAND-IN; fix the instruments TOGETHER or the cell still cannot show the panel works |
| `Z-S24` | INERT | `2.0.0_SA_COO~ZZZ` | answers S23's own unmeasured clause: the defect does NOT generalise -- all 15 mechanical criteria of the 5 passing round-5 cells carry a discriminator |
| `Z-S25` | INERT | `2.0.0_SA_COO~ZZZ` | the citing row for LIMB 6's retired unqualified sentence, carried by 3 rows of this channel and corrected in 0 |
| `Z-S26` | INERT | `2.0.0_SA_COO~ZZZ` | **the issuer's own Rule 27 inversion** -- round 6 cut before round 5's slug, which gated `3.0.0_SA_CVO~Z` for 93 minutes |
| `Z-W10-S1` | ARMED | `0.9.0_WK_AMGT_RESAPP~10` | **AC3's own invocation destroys uncommitted work** in the file it mutates -- `git checkout --` restores from the INDEX, not a snapshot |
| `Z-W10-S2` | ARMED | `0.9.0_WK_AMGT_RESAPP~10` | the four-way cross is real end-to-end, but **no producer has ever written a `TRENDING_*` or `BREAKOUT_*` partition** -- 2 of 4 combinations have no data, disclosed via `AxisResolution` |
| `Z-W10-S3` | ARMED | `0.9.0_WK_AMGT_RESAPP~10` | the `/api/scoped/amgt` adapters are **delivered as code but cannot be MOUNTED from this cell's grant** -- the route and Lambda declaration live under `infra/aws/terraform/` |
| `Z-W10-S4` | INERT | `0.9.0_WK_AMGT_RESAPP~10` | the surface this recut was told to build on **already violates its own no-non-ASCII block** -- 6 of 27 files, all from the previous cut, none in the four named gaps |

---

## 4. FOUR DEFECTS THAT ARE THE ISSUER'S, NOT THE WORKER'S

Named here so L9 does not grade them against `0.9.0_WK_AMGT_RESAPP~10`.

1. **`AC3` IS A DESTRUCTIVE CRITERION AND I WROTE IT** (`Z-W10-S1`). Its final limb
   `git checkout -- src/pages/SecurityAnalysis/types.ts` restores from the INDEX, so a mid-work run
   reverted ~90 lines of the worker's own uncommitted recut of that file **while printing the expected
   `1`**. The worker recovered it and re-ran post-commit where the restore is exact. The fix is one
   clause: either "run after the commit that lands this cell's edits" in the criterion text, or a
   mutant target the cell does not edit. ⭐ This is a FIFTH failure shape for a criterion -- not
   always-fails, always-passes, unsatisfiable-while-honest or true-and-insufficient, but
   **CORRECT-AND-DESTRUCTIVE**: it discriminates properly and damages the subject while doing so, and
   its own output looks clean.
2. **THE ROUND-6 CUT INVERTED RULE 27's L10 ORDER** (`Z-S26`, ruling `1.0.0_SA_CTO~Z` msg 21771
   @`3a00618246`). I cut from the L9 adjudication with no `ROUND_ANALYSIS.round5.md` in existence. The
   refuser counts open orders PER PROJECT, so the issuance re-armed the gate round 5's slug was
   waiting on, in the same commit that cleared it. Cost paid by the CVO, not by me. Recorded, NOT
   precedent.
3. **THE CELL ASKED FOR A CROSS THE PRODUCER PLANE CANNOT SUPPLY** (`Z-W10-S2`). The order required
   Trending/Breakout x Price/Chatter as two independent controls; only the subject half exists on the
   producer plane. The worker built the product honestly in both `lib/research/api/scoped_amgt.py` and
   `portal/src/pages/SecurityAnalysis/types.ts` and made every payload carry an `AxisResolution`
   (`requested_axis` / `served_axis` / `resolution` / `movement_basis`) rendered verbatim, rather than
   re-deriving a ranking its BLOCK forbids. Switching on a crossed partition is one membership edit in
   `PRODUCER_LANDED_AXES` with a test that makes the membership true. **That is a measure-then-build
   sequence I should have split into two cells.**
4. **THE GRANT COULD NOT REACH THE MOUNT** (`Z-W10-S3`). A read path whose route and Lambda
   declaration live outside `<paths>` cannot be served by the cell that writes its handler. Under
   RULING 1 a missing path is a WALL, not an oversight -- the worker filed a row and stopped on that
   clause, which is exactly right. An integration cell's `<paths>` must name the CONSUMER, and here it
   needed the terraform plane too.

---

## 5. THE ARMED SET AS A SUBTRACTION, and the honest bound on it

`hazard_standing` is **AT-SURFACING and IMMUTABLE** -- a disarm is a NEW CITING ROW, never an in-place
flip. **So the field CANNOT go down, and the raw count is an OVERCOUNT BY CONSTRUCTION.** Reading it
as a work queue invents debt.

```
  ARMED, raw field read, whole channel      44 (comp-surprise, both planes)
  ARMED naming 2.0.0_SA_COO~ZZZ as owner    16 of 64
  minus: rows a later row's text cites with a disarm word            -12
  = rows with NO citing row at all                                     4
      AMGT_RESAPP-Z-S19, Z-W10-S1, Z-W10-S2, Z-W10-S3
```

⛔ **AND THAT `4` IS A FLOOR, NOT A MEASUREMENT.** The subtraction ran a STRING census, and a string
census cannot separate a CITATION from a MENTION -- a row that merely names `Z-S15` and contains the
word "disarm" anywhere scores as a disarm. Two of the twelve are mutually crediting (`Z-S9`/`Z-S10`),
which is the tell. **The four named carry NO citing row at all, so they are certainly standing; the
true outstanding figure lies between 4 and 16 and needs a per-row read, which is L9's grain.** The
instrument is named so the number is not quoted as measured.

---

## 6. BROKER-ONLY FACTS -- things no file in this tree records

- `3.0.0_SA_CVO~Z` named its own L10 blocker in `ADJUDICATION_v5.md:13` at 21:41Z and was correct to
  stop there. It was probed by two seats tonight and **BOTH declined to nudge**. Nothing was owed by
  it while `re-1` was open.
- The four-plane live-production probe read **3 COLD / 1 structurally blind** on that seat with the
  seat LIVE and its summary reading `READY` -- a nudge under every reading of the precondition, and it
  would have been WRONG. **A liveness probe measures PRODUCTION and cannot measure ENTITLEMENT TO BE
  IDLE.** Fixed at the skill as a third class, BLOCKED, tested against the owner's own artifact BEFORE
  the planes, with the blocker RE-MEASURED at HEAD -- because `rd-8` was a true blocker when named and
  a false one 43 minutes later.
- `AMGT_RESAPP-Z-S7`'s `spec_asserts` was **NOT corrected**, by this seat's ruling as scope owner, with
  `4.0.0_SA_CRO~Z` (msg 21758) withdrawing its own offer to retro-edit it and `2.0.0_SA_COO~Z`
  (msg 21755) declining to adjudicate from outside the scope. `Z-S25` is the citing row instead.

---

## 7. WHAT IS DELIBERATELY NOT DONE

- **`M portal` in the shared tree is untouched.** Workspace HEAD gitlink `e85f6eb84f`, portal repo HEAD
  `30ca034bba` on DEV, the worker's commit `c6728146` -- three different points, and the modified
  gitlink PREDATES this drain. The worker left it uncommitted on purpose and routed it to the
  integrator. PORTAL FROZEN stands: COMMIT YES / PROMOTE NO until Andrew names it. Naming it so it is
  not mistaken for drain residue.
- **`comp-iam` HAS NOW BEEN RE-RUN, AND THE RE-RUN CANNOT DISCHARGE THE GAP -- see `Z-S27`
  @`ef99ea7fa9`, filed after this packet was first cut.** Every figure came back byte-for-byte
  unchanged (835 calls / 96 mapped roles / 12 missing / 291 deny-present / 2 resource-mismatch, the
  same two rows, neither on this surface). ⛔ **THAT IS NOT A CLEAN RE-CHECK, IT IS PROOF THE
  INSTRUMENT NEVER SAW THE NEW CODE.** Measured with a positive control over the tool's own 992 lines:
  lines naming `lib/` = 0, `scoped_amgt` = 0, POSITIVE CONTROL `infra/aws/lambda/` = 37; and comp-iam
  states its own scope as "3 trees (472 .tf files): infra/aws/terraform, infra/aws/multi-account/terraform,
  infra/aws/ec2" -- `lib/` is in none of them. `comp-iam` verdicts CALLS against ROLES and a library has
  no role, so `lib/research/api/scoped_amgt.py:192`'s `boto3.resource("dynamodb")` is OUT-OF-CORPUS,
  which is worse than the 266 calls it honestly discloses as blind. **This is `Z-W10-S3` from a second
  plane: no mount -> no role -> no IAM verdict. The two resolve together or not at all**, so the real
  condition is the mount, not another run. `Z-S27` carries a falsifiable disarm condition and
  explicitly refuses "same totals" as a discharge.
- **No criterion of a terminal order was amended.** `AC3`'s defect is carried by `Z-W10-S1`, not by an
  edit -- a record corrected in place destroys the evidence it was ever wrong, and the L6 gate never
  grades a modification anyway (`to-pipeline-gate.py:809-813`, "this gate never refuses an existing TO").

---

**Packet vintage:** HEAD @`f5f1749405`. Drain @`b2cd6e9ee7`. Issuance @`4352fe1c47`.
Portal branch `wk-amgt_resapp-5-8-portal` @`c6728146` fetched into the main portal repo BEFORE
teardown and verified after it (`git -C portal cat-file -t c6728146` -> `commit`; bogus
`c672814000` -> `fatal: Not a valid object name`).
**Push state: LOCAL** (`origin/SITEZ` at `ab642b92e5`, ls-remote read). Push is the integrator's.
