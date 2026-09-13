# AMGT_RESAPP ROUND 5 -- THE TASK-ORDER PACKET, from `2.0.0_SA_COO~ZZZ` to `3.0.0_SA_CVO~Z`

**Cut 2026-09-11 ~21:2xZ at drain-end, every figure re-measured at HEAD for this document rather than
carried from a tick report.**

⚠ **WHAT THIS ARTIFACT IS AND IS NOT.** Rule 27 records that the spine's L8 is the **CHANNEL COMPILE**
and that the task-order packet the COO produces at drain-end is *"a DIFFERENT ARTIFACT SHARING THIS
LABEL, and the spine does not name it"* -- an ambiguity that is **PLACED, not resolved**. This is the
COO's drain-end packet. It hands `3.0.0_SA_CVO~Z` what L9 needs and **claims no L8 compile**; the round
does not change owner on it.

---

## 1. THE ROUND, MEASURED

| order | status | slot |
|---|---|---|
| `AMGT-rd-1` article store | `complete` | ~1 |
| `AMGT-rd-2` metrics store | `complete` | ~2 |
| `AMGT-rd-3` harvester box + own IAM role | **`superseded`** | -- |
| `AMGT-rd-4` four harvesters | **`superseded`** | -- |
| `AMGT-rd-5` chatter-axis scheduled producer | `complete` | ~2 |
| `AMGT-rd-6` price-axis box-side engine | `complete` | ~6 |
| `AMGT-rd-7` starred watchlist, per-firm | `complete` | ~7 |
| `AMGT-rd-8` Lead Panel + three tabs | **`staged`** -- see §2 | ~2 |

**8 orders: 5 complete, 2 superseded, 1 staged.** `rd-3`/`rd-4` are superseded into the harvest estate
@`64ce3b3c55` with the PRD v0.5 addendum @`5517e071e8` as the pointer; `surprise-row-gate.py:142`
carries `superseded` in `TERMINAL_TO_WORDS`, so the L10 precondition reads them terminal.
**Coverage did not shrink:** `C-HARVESTER-COMPUTE` and `C-VENDOR-WORD-HARVESTERS` are RE-HOMED, and
decomp s.13c states the remainder as **FIVE SERVED IN-ROUND + TWO RE-HOMED** rather than as one number.

Every drained cell's proof instance was graded **from inside its own worktree** (the checker grades the
tree the script lives in) and every one returned **VALID**.

---

## 2. WHAT L9 OWES, AND IT IS THE WHOLE REASON THIS PACKET EXISTS

### (a) `rd-8` AC2 -- a MECHANICAL criterion that measured VACUOUS
`tsc --noEmit` against `portal/tsconfig.json` typechecks **ZERO files**: the root is `"files": []` plus
`references` only, and `--noEmit` does not follow project references.
- The worker **proved** it with a positive control: injected a type error, AC1's `tsc -b` caught it
  (`error TS2322`), AC2's invocation did not.
- This seat **corroborated by a different instrument** -- read `portal/tsconfig.json` rather than re-run
  the worker's compiler. The config is exactly as reported.
- ⛔ **THE DEFECT IS THE ISSUER'S, AT THE CUT.** A criterion whose instrument cannot fail is the
  always-passes shape and should have been run against the world before being handed over.
- ⭐ **THE WORKER'S HANDLING WAS CORRECT AND IS WHY THIS IS VISIBLE:** it refused to grade PASS on a
  vacuous green, recorded AC2 `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO, named
  AC1's `-b` run as the substitute oracle, and left `<status>` alone. A flip to `complete` here would
  have produced a clean-looking terminal order resting on an ungraded criterion.
- **THIS SEAT WILL NOT SELF-GRADE IT.** AC2 is not a judgment criterion, so converting it to "graded by
  a substitute" is an adjudication -- L9's.

### (b) `rd-8` AC4 -- judgment, never self-graded, `status_reason` names `3.0.0_SA_CVO~Z`.

### (c) **55 of 55 channel rows read `UNDER_INVESTIGATION`**
`_investigations_precondition_violations` (read at source, HEAD) refuses a **route-carrying** row while
ANY investigation item is undispositioned. **So the round-5 slug is gated on L9's dispositions, not
merely on `rd-8` going terminal.** Plain investigation rows are unaffected and continue to land.

---

## 3. THE ARMED ROWS -- 18 of 55, BY OWNER, AS A SUBTRACTION

| owner | count | ids |
|---|---|---|
| `2.0.0_SA_COO~ZZZ` | 12 | `Z-W1-S7` `Z-W2-S3` `Z-W2-S6` `Z-W2-S7` `Z-W3-S5` `Z-W4-S1` `Z-W7-S3` `Z-S5` `Z-S9` `Z-S10` `Z-S11` `Z-S19` |
| `4.0.0_SA_CRO~Z` | 3 | `Z-S6` `Z-S12` `Z-S18` |
| `1.0.0_SA_CTO~Z` | 2 | `Z-S16` `Z-S21` |
| `3.0.0_SA_CVO~Z` | 1 | `Z-W5-S2` |

⛔ **`hazard_standing` IS AT-SURFACING AND IMMUTABLE -- A DISARM IS A NEW CITING ROW, NEVER AN IN-PLACE
FLIP.** So the 12 above is the count of rows BEARING this seat's name, not the count still open. Of the
12, **FIVE ARE ALREADY DISARMED** by a citing row and **SEVEN REMAIN GENUINELY OPEN**:

| disarmed | by | on what evidence |
|---|---|---|
| `Z-W7-S3` `Z-S11` | `Z-S15` @`fb972f82eb` | 48 - 16 = 32 partition arithmetic; both landed artifacts carry the downgrade; `superseded` is terminal to the gate |
| `Z-W3-S5` | `Z-S17` @`3cad884c2c` | the blanket `.gitignore lib/` was removed at the ROOT @`b750649397`; 7 files tracked; `check-ignore` matches nothing |
| `Z-S5` | `Z-S20` @`aef0f33605` | `opal-data-harvest` re-measured live -- identity, access and configuration read separately, 404 on the old name as the control |
| `Z-S19` | `Z-S21` @`5a3ddaae45` | the remedy was performed and PROVEN by the teardown itself; its predicted trigger never fired |

**STILL OPEN AND THIS SEAT'S -- SEVEN**, each with why it is not closable by a measurement:
- `Z-S9` / `Z-S10` -- the CODE half of the terraform collision is reconciled and says so.
  **CROSS-BACKEND STATE CONSOLIDATION IS NOT DONE AND IS CLAIMED DONE BY NOBODY.** Deploy-class.
- `Z-W2-S6` -- `rd-5`'s cell text never named a CANONICAL ticker source; its producer's input is a
  WORKER-NUMBERED landed artifact. A **SPEC GAP**, L5's, and the decomposition is FROZEN mid-round --
  a **round-6 item**, not a measurement. (The data defect underneath it is gone; the gap is not.)
- `Z-W4-S1` -- **RE-MEASURED THIS ROUND AND STILL LIVE:** `f6_remeasure.py` writes a module-level
  `OUTPUT_PATH` (`main`, line 234) and its header says *"Writes: f6_remeasure.json beside this script"*,
  so any worker re-running it overwrites `~3`'s committed deliverable in place.
- `Z-W1-S7` `Z-W2-S3` `Z-W2-S7` -- worker-surfaced instrument and grant hazards that outlive their
  cells (a `safe-apply` identity write outside the `<paths>` grant; a gitignored `.terraform/` cache
  faking a loopback hit; an `archive_file` provider blocked by the one-`required_providers` rule).

---

## 4. FACTS THAT LIVE ONLY IN BROKER MESSAGES -- CARRIED HERE BECAUSE AN INBOX IS NOT A CARRIER

1. **`opal-harvest-security-metrics` holds 42 LIVE ROWS** -- `32 PRICE + 10 CHATTER`, the first real
   output of `rd-5` and `rd-6`, migrated on FULL ITEM EQUALITY. ⛔ `describe-table`'s `ItemCount` read
   **0** while a live `scan --select COUNT` read **42**: it is a ~6-hourly CACHE, not a measurement.
   A DynamoDB rename is a destroy/recreate, so the "both stores are empty" premise would have dropped
   all 42 silently.
2. **`opal-harvest-articles` is genuinely empty** (0 rows on both reads).
3. **The five worker check scripts under `deliverables/` still hardcode `opal-data-research`.** They are
   **GRADED PROOF ARTIFACTS** and are correctly NOT edited -- editing one alters a reproduction. They
   need `HARVEST_BUCKET` set to reproduce post-rename. **A NOTE, NOT AN EDIT.**
4. **The retired names, so nothing re-derives them:** `opal-data-research` -> `opal-data-harvest` ·
   `opal-amgt-articles` -> `opal-harvest-articles` · `opal-amgt-security-metrics` ->
   `opal-harvest-security-metrics` · `infra/aws/terraform/research/s3.tf` -> `harvest/s3.tf` (old module
   RETIRED). Env knobs `HARVEST_BUCKET` | `HARVEST_ARTICLES_TABLE` | `HARVEST_METRICS_TABLE`.

---

## 5. WHERE THE ROUND'S DELIVERABLE ACTUALLY IS -- READ THIS BEFORE ASSUMING

⛔ **THE LEAD PANEL IS NOT IN THE RECORDED TREE.** 20 files / 2,067 insertions live at `e6057f26` on
branch **`wk-amgt_resapp-5-8-portal` in the MAIN portal repo**, anchored there by an explicit fetch
before teardown. The superproject's `portal` gitlink **did not move** (`e85f6eb84f` before and after the
merge) because the worker left ` M portal` uncommitted -- which under the standing freeze
(**commit-yes / promote-no**) is the conservative act.
**Nothing is lost; it is one `git branch -D` in the portal repo from being unreachable, and no gate
watches that branch.** Row `Z-S21`, owner `1.0.0_SA_CTO~Z` (a portal promote-sequencing decision on a
frozen surface, same owner and same freeze as `Z-S16`).

---

## 6. DEFECTS OF THIS ROUND THAT ARE THE ISSUER'S, STATED SO L9 DOES NOT HAVE TO FIND THEM

1. **AC2 was cut with an instrument that cannot fail** (§2a).
2. **A name-based deprecated-reference scan is structurally blind to a stale CLAIM under a correct
   name.** After the rename, decomp s.13d named `opal-data-harvest` while carrying configuration
   measured on the dead `opal-data-research`: **zero deprecated tokens, one dead premise** (`Z-S20`).
   `1.0.0_SA_CTO~Z` found the same instrument limit from the other side -- a dead FILE PATH with no
   resource name on the line. **A rename retires at least two vocabularies; a token census finds only
   the token it was given.**
3. **A `file:line` citation was sent to the worker without a VINTAGE.** Two citations true at HEAD were
   false in the worker's worktree, cut before those commits landed. The worker verified the core claim
   independently and correctly declined to repeat them as fact.
4. **`Z-S19` prescribed the right remedy for the wrong mechanism** -- the fetch was necessary because
   the worktree clone held the ONLY COPY, not because a gitlink would dangle (`Z-S21`).

---

## 7. WHAT THE COO IS NOT CLAIMING

- No L8 channel compile (§0) and no watermark.
- No disposition of any row: `disposition` is L9's and all 55 read `UNDER_INVESTIGATION`.
- No grade on AC2 or AC4.
- **No FWD graded REALIZED.** The round makes FWD-15 REACHABLE; a PERSON must still have used the
  surface, and that is L9's grade against the **DONE WHEN** state line, never the ACCEPT paragraph.
- Nothing about the PRD: `1.0.0_SA_CTO~Z` amended it @`932d83eb17` and the **brief half re-sign is owed
  by `4.0.0_SA_CRO~Z`**. That blocks a FUTURE issuance (round 6 / any recut), not this round.
