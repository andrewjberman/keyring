# /self-drive AMGT_RESAPP & POSN_ASTTAX -- ticks 19-22

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-11T20:54Z**
Covers ticks 19, 20, 21, 22. Last log was tick 18 (`@5517e071e8` window). Ticks 19 and 21 wrote
nothing at the time and their findings are carried here.

---

## 1. THE OPERATOR EVENT THAT SHAPED THIS WINDOW: a PAUSE this seat took at face value

Andrew-direct at THIS terminal ~19:5xZ: **"pause, CRO is going to remediate"** (the fuller sentence
relayed by `0.0.0_AB_MSTR~Z` @21589 adds *"with full authority"*). **Tick 21 fired into the pause and
was HELD, not run** -- no sweep, no pitch, no commit. A cron does not know about a pause; the seat
does.

⭐ **THE PART WORTH KEEPING: this seat did NOT narrow the pause to make its own work legal.** The
obvious escape was available and declined -- the gate fix touches no harvest path, so "he only paused
the harvest surface" was a reading that would have let the tick run. But the word landed at this
terminal, addressed to this seat, and `0.0.0_AB_MSTR~Z` then STRUCK its own relay line ("AMGT_RESAPP
and POSN_ASTTAX rounds continue") precisely because it had asserted something about terminals it
cannot observe. The operative rule it published -- **act on what landed at your OWN terminal** -- is
the rule this seat had already followed. That struck sentence was the one line that could have argued
the loop back into driving, and nothing here leaned on it.

⛔ **AND THE PAUSE WAS NOT CONVERTED INTO A TEARDOWN EITHER.** The cron was NOT cancelled and the
`org/XXX.md` carrier clause was NOT struck. "Pause" is not `/self-drive off`, whose terminal state is
STOPPED-BY-OPERATOR; widening his word in the restrictive direction is the same error as widening it
in the permissive one. Lifted ~20:0xZ: **"remediation complete, all agents may unpause."**

## 2. ACTS TAKEN -- four commits, all LOCAL

| commit | act |
|---|---|
| `dc8444a93b` | **GATE FIX.** Both L10 precondition limbs now discriminate CARRIED-vs-MINTED against the merge's parents, replacing the `Z-` fabric constant. |
| `b4fce8efab` | Strip the one non-ASCII char THIS seat put into that gate one commit earlier. |
| `98380c753e` | **POSN_ASTTAX round-2 L10 ANALYSIS** -- the read the slug handed this seat. |
| `932d83eb17` | **AMGT_RESAPP PRD v0.5 brief half** -- 7 deprecated-live references purged. |
| `49ddcc481d` | **POSN_ASTTAX PRD v0.5 brief half** -- C-RETAG-SAFETY RE-FOUNDED; step (2) restated as a BAR. |

### 2a. The gate fix, and the finding nobody was looking for

Andrew ~19:3xZ: *"the surprise-row gate must be project specific."* `_row_is_other_fabric` is a
CONSTANT, not a comparison -- its docstring called a row without `Z-` "THIS fabric's record", true on
the laptop and **inverted on site Z**, so 100 already-committed laptop rows arriving by merge read as
native here and refused an authorised leg.

⭐ **THE OLD RULE WAS ALSO TOO LOOSE, AND EVERY SEAT INCLUDING THIS ONE HAD FRAMED IT AS ONLY TOO
STRICT.** On this box a row **MINTED** in a merge commit carrying `Z-` was EXEMPTED outright.
```
old _row_is_other_fabric(AMGT_RESAPP-Z-S99)        -> True  -> EXEMPT   (a hole)
new _row_was_carried(same row, parents without it) -> False -> BINDS
```
Surfaced only by running the NEGATIVE arm. The commit closes a hole in the same act that opens the
carried case, so it is not a relaxation.

⛔ **THE FIRST RED-FIRST PROBE WAS WORTHLESS AND IS RECORDED AS SUCH.** `4.0.0_SA_CRO~Z` set the bar:
*"If you cannot write an arm that fails today, the diagnosis is not yet proven."* The first probe
asserted the new semantics through a `parent_ids=` keyword that did not exist, so all 8 arms "failed"
with **TypeError on the SIGNATURE** -- which is not evidence about BEHAVIOUR, cannot distinguish a
real defect from a missing parameter, and would have gone green after the fix for an unrelated
reason. Rewritten to call today's exact signature and fail on the ANSWER:
```
BEFORE  A=4 failed (behavioural) · B=8 (signature-gated) · C=4 controls PASS
AFTER   A=0 · B=0 · C=4 controls still PASS        self-test 108 arms, 0 failed
REAL DATA  87 IRPT_FNTEND rows the merge adds -> 87 carried -> 87 EXEMPT -> 0 REFUSED
NEGATIVE   minted AMGT_RESAPP-Z-S99 -> REFUSED, naming rd-8 (1 of 36 non-terminal)
```
⚠ **87 is the ROW count and is NOT the 100 VIOLATIONS reported** -- one row can violate on both limbs.
Stated rather than reconciled; the denominators differ in kind and nobody should read it as a conflict.

**CRO item (2), "scope the verdict by project": NOT BUILT, because measurement says it is ALREADY
TRUE.** AMGT_RESAPP 1/36, POSN_ASTTAX 2/8, IRPT_FNTEND 1/11, NFRA_COMPEFFICACY 0/28 -- four distinct
denominators, and AMGT's open rd-8 does not appear in POSN's verdict. Build-ladder rung 2: the estate
already has it. ⚠ That census reads orders tracked on THIS branch, so IRPT reads 1 of 11 here against
`0.0.0_AB_MSTR~Z`'s 3 of 18. Correct by design -- at a merge it reads the merged index -- but it is a
denominator that MOVES WITH BRANCH STATE and must not be quoted cross-fabric without naming the tree.

### 2b. The PRD, and a fifth reference a careful scan could not see

`4.0.0_SA_CRO~Z` flagged 4 deprecated-live refs and correctly did not edit L4. A **fifth** was found
at `:652` -- a second present-tense citation to `infra/aws/terraform/research/s3.tf:11`, a retired
file.
⭐ **WHY A HONEST CENSUS MISSED IT, which is the transferable part:** it enumerated the three retired
RESOURCE NAMES, with a printed denominator. `:652` cites the DEAD FILE PATH with no resource name on
the line. **A token census finds only the token it was given, and a rename retires at least TWO
vocabularies -- the resource NAMES and the DECLARATION PATHS.** Found only by enumerating the
REMAINDER line-by-line after editing (Rule 24 by SUBTRACTION) instead of assuming leftovers were
history: 13 lines still name a retired resource and **all 13 are correct**.

⛔ **TWO OF THE SEVEN WERE THIS SEAT'S OWN ERROR, not the CRO's finding.** `:546` and `:742` said the
tables were *"genuinely empty (0 items, measured)"*. The word **"measured" was mine and it was false**
-- it read `ItemCount`, a **~6-hourly CACHE**. Same table, two instruments: `describe-table` 0,
`scan --select COUNT` **42**, reconciling exactly to rd-6's own output (32 PRICE + 10 CHATTER). A
DynamoDB rename is DESTROY/RECREATE, so on my sentence's premise it would have dropped 42 live rows.
It did not, because `4.0.0_SA_CRO~Z` distrusted a number this seat had repeated all session --
including to Andrew.
Half discipline checked BEFORE writing via `prd_signoff_lib.half_of_section`, not asserted after:
```
ratified-text  4eb997ed71ee -> UNCHANGED   3.0.0_SA_CVO~Z's signature INTACT
brief          944853bacc43 -> 7c5337381   RE-SIGN OWED BY 4.0.0_SA_CRO~Z (its 6th)
```
All seven folded into ONE commit deliberately: same class, all brief-half, so ONE review not two.

## 3. VERDICTS / PEER INPUT CONSUMED

- **`4.0.0_SA_CRO~Z` 21600** -- confirmed build (1) and (2); measured that the merge was ABORTED not
  committed (`--is-ancestor` NO, with a CLOUD-only negative control) and no override was used. Its
  discrimination bar became this commit's acceptance condition. **21629: "NO -- I hold no gate edit"**,
  answering Andrew's "they may have already worked on it" directly.
- **`2.0.0_SA_COO~ZZZ` 21586/21625** -- confirmed the change does not weaken the precondition where it
  binds, from its own round-close path. Ran this seat's SECOND-VOCABULARY finding against the COO lane:
  11 hits / 37 files, **zero deprecated-live**. Also read at source that the investigations limb binds
  only a ROUTE-CARRYING row, so **AMGT's round-5 slug is gated on `3.0.0_SA_CVO~Z`'s L9 dispositions
  (51 rows UNDER_INVESTIGATION), not merely on rd-8 going terminal.**
- **`2.0.0_SA_COO~Z` 21613/21619** -- POSN deprecated scan: **0 refs across 31 live artifacts**, both
  outstanding TOs clean, corroborated on a second instrument at a wider grain. Declined
  `/canonical-flow --midstream` on SCOPE (AMGT is `~ZZZ`'s), not on the merits. Then filed an
  OBSERVATION with **no disposition attached** that `ROUND_ANALYSIS.round2.md` was written but
  UNTRACKED, and refused to cut an issuance against uncommitted bytes. ⭐ **That refusal was exactly
  right and its timing diagnosis was correct** -- written 19:53Z, pause landed ~19:57Z, commit
  correctly held. Resolved by `98380c753e`; its obligation 1 has since fired (21631).

## 4. OPEN CALLS IN SCOPE -- 0 adjudicable, 1 RESERVED

Pitched to `3.0.0_SA_CVO~Z` @21632, marked NON-URGENT so that seat does not come off L9 for it.
**CALL: extend Bright Data Web Unlocker from WSJ to the three SESSION harvesters?** CARRIED, nothing
blocked. **REC: ask per-use when the box actually stands up** -- it does not exist, so the call has no
act behind it. CITATION: CLAUDE.md Agent Autonomy, *"NEVER call an external vendor API without
Andrew's explicit per-use word -- availability is not authorization."* Verified still open at
`AMGT_RESAPP_PRD.md:581-583`.

⚠ **THE ALL-RESERVED TELL FIRED (1 of 1) AND IS REPORTED RATHER THAN HIDDEN.** Re-ran the citation
test; it holds -- a flat NEVER-class line naming the decision CLASS. The queue is small because
Andrew RULED almost everything in scope tonight.
**TWO ITEMS WERE DECIDED IN LANE RATHER THAN CARDED UPWARD**, per /open-calls' own rule that listing a
decidable item is a finding that the driver should decide it:
- **PRD version bump: NO.** The L4-R binding carrier is the section half_hash, never `prd_version`.
- **`AMGT_RESAPP-Z-S16`: PARKED with a named un-parking condition, NOT disarmed.** The hazard can
  still bite -- the panel cannot reach DEV without the 19 IRPT commits reaching DEV first -- and
  portal is FROZEN both fabrics. Not disarmable today; recorded as ARMED-with-a-condition.

### 2c. The L4 hand-back -- `2.0.0_SA_COO~Z` refused to cut round 3, and was right twice

Obligation 1 fired on `98380c753e`. That seat then **measured its own input before cutting against
it** and found POSN_ASTTAX PRD v0.5 still stating the FALSIFIED mechanism verbatim at `:155`, `:166`
and `:210`. It handed items 1 and 2 BACK to L4.

⭐ **RIGHT ON BOTH COUNTS.** Cutting would have had every round-3 cell inherit "KeyError blanks the
page" -- reproducing, one layer down and under a new author's name, the exact defect the round-2
analysis had just diagnosed. And it refused the faster route: **encoding a re-founded constraint
inside a DECOMPOSITION, where no signer would ever see it.** An earlier limb's gap does not become
the next limb's by being inconvenient.

**DONE THIS TICK @`49ddcc481d`.** C-RETAG-SAFETY re-founded on the measured mechanism (silent zeroing,
not blanking) with the original preserved IN PLACE as history rather than deleted; step (2) restated
as a CONDITION with a threshold that names its own current truth -- NOT MET. ⭐ **The structural
lesson went into the PRD, not only into this log: this bullet ORDERED the measurement that
contradicted it, so the instruction worked and the failure is that PROSE PREDATES ITS OWN
INSTRUMENT'S ANSWER. A spec that orders a measurement must be re-read when the answer lands, and
nothing in the ladder does that automatically today.**
```
POSN ratified-text  SIGNED, current, UNCHANGED -- 3.0.0_SA_CVO~Z's signature INTACT
POSN brief          6bb1b9894d28 -> 3c1c3202c   RE-SIGN OWED BY 4.0.0_SA_CRO~Z
POSN_ASTTAX         ADMITTED -> WITHHELD, which is the gate working, not a regression
```
Items 3 and 4 remain `2.0.0_SA_COO~Z`'s and it has declared them ready; its recorded choice that
round 3 is a RE-DECOMPOSITION (L5) + ONE issuance (L6) is the COO's to make and is not second-guessed.

⚠ **A PEER'S MERGE BLOCKED THE FIRST COMMIT ATTEMPT AND WAS LEFT ALONE.** `safe-commit` refused with
an open `MERGE_HEAD` = `1a619eef6f`, `2.0.0_SA_COO~ZZZ` draining its rd-8 WORKER branch
(`0.9.0_WK_AMGT_RESAPP~2`). Identified before acting, never `--abort`ed; waited and re-ran. Nothing
was left staged.

## 5. COMPLETION TEST

```
COMPLETION TEST: NOT DONE -- 0 of 2 projects complete (denominator: 2 in scope)
  AMGT_RESAPP  status=active  dep_stage=EXECUTING  REACHABLE   v0.5 WITHHELD (brief owed, 6th)
  POSN_ASTTAX  status=active  dep_stage=EXECUTING  REACHABLE   round 2 CLOSED at L10; recut is COO~Z's
  UNREACHABLE: 0    HELD-AT-STOP: not reached
```
Read from `org/projects/*.json`, never declared.

## 6. CORRECTIONS THIS SEAT OWES

- **`C-S34` corrects msg 21505 and is RIGHT** -- this seat read each entry's OWN id and never what the
  entry ADJUDICATED. Recorded in the round-2 analysis.
- ⛔ **THE ASCII GATE REFUSED THIS SEAT THREE TIMES IN ONE SESSION** (two commit messages, then a
  SOURCE file) and the first two fixes taught nothing, because the message limb BLOCKS and the source
  limb only **WARNs** -- so the third one shipped in `dc8444a93b` and needed `b4fce8efab` to undo.
  Banked to memory with the generalising remedy: check BOTH objects by SUBTRACTION and print the
  leftover set, never by recalling which symbols were typed.

## 7. STATE / NEXT

- **Owed BY this seat: nothing blocking.** Owed TO it: `4.0.0_SA_CRO~Z`'s brief re-sign at
  `7c5337381`; `2.0.0_SA_COO~Z`'s round-3 issuance; `3.0.0_SA_CVO~Z`'s L9 dispositions for AMGT.
- ⚠ **ANOMALY, NOT YET CHASED:** `heartbeat("1.0.0_SA_CTO~Z", ...)` returned *"Heartbeat OK for
  1.0.0_SA_CTO"* -- the lane suffix absent from the receipt. `get_live_agents` does show `~Z` LIVE, so
  this is probably display-only, but a lane heartbeat landing on the BASE serial would leave the `~Z`
  summary stale for every seat that reads it. Named rather than assumed benign.
- **Push state: LOCAL for all four commits.** `0.0.0_AB_MSTR~Z` pushes origin/SITEZ; last integrator
  read reported origin/SITEZ @`d0efe81ca8`.

## Compiler Tools

`safe-commit.sh` · `surprise-row-gate.py --self-test` (108 arms) · `prd-signoff.py status` ·
`prd_signoff_lib.half_of_section` · `_open_tos_for_project` · `_parent_row_ids` ·
`git log --all -- <path>` · `git worktree list` · `get_live_agents` · two scratchpad probes
(`redfirst_carried_minted.py`, `realdata_merge_check.py`).
