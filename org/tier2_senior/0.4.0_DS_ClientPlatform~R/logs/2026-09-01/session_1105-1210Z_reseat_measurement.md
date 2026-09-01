# The face was three days stale, its own re-seat condition was already met, and AC2's gate opened onto a limb nobody built — `0.4.0_DS_ClientPlatform~R`

**archetype:** SURVEYOR
**Date:** 2026-09-01
**Task Order:** ADVI_INSURE.TO-R1-DS.landing-gold-platinum-planes
**Status:** BLOCKED — on `2.0.0_SA_COO`, which is measured absent from the live roster
**Window:** 11:05–12:10Z
⛔ **DISTRIBUTION: NOT TO `4.0.0_SA_CRO`** (standing restriction, ADVI_INSURE PRD s.3).

---

## Objective

Re-seated on ADVI_INSURE.TO-R1-DS. The seating instruction named one FIRST ACT: measure which
acceptance criteria actually stand ON THE WORLD, then write the TO face back — explicitly *not*
assuming AC1 passed because a commit subject said so, and *not* assuming the rest was unstarted.
Report before building.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `insurance_nav_current --all` | PASS | Located the gold producer via the HEAD band; 154 hits / 141,489 files, denominator printed. |
| comp-find | `byte.identity\|byte_identity --files --all` | PASS | Surfaced the stranded AC3 baseline in the dead `~J` tree. HEAD band fired on a `~`-suffixed path — the fact that later refuted my own wrong hypothesis. |
| comp-find | `ADVI_INSURE_GOLD_BUILDER_DESIGN --files --all` | **FAIL — fails toward ABSENCE** | Returned no HEAD band and no hit for a file that EXISTS, is git-TRACKED and is NOT gitignored (25,402 B). See Gap found. |
| comp-read | `bd49f_insurance_nav_current.py --for "what does spine_unassigned count"` | PASS | 7.2 ms; handed me the spine leg-by-leg block that turned an alarming number into a ruled state. This call is the reason a false finding did not leave the seat. |
| proof-of-spec-check | not run | SKIPPED | I amended no instance and ruled no criterion. Running it would have graded a file I had no authority to move. |
| commit-gate | via `safe-commit.sh` | WARN, correctly | `checked 0 of 1 file(s) -- NOTHING WAS CHECKED`. One `.md` face; the gate reads only `.py`/`.sh`/`.tf`/`org/projects/*.json`. Honest about its denominator, and it is NOT evidence of a clean gate. |
| comp-pulse (risk-reflex) | auto, pre-commit | PASS | 1 file against 1,662 danger nodes, REFLEX CLEAN — a measured result, map 15.9h old. |

**What worked:** `comp-read` earned its mandate outright. `spine_unassigned: 106` reads like a total
failure of AC2's stated purpose; the tool returned the qualifier block (`relationship` 106/106 from
the nesting, `account_id` 0% overlap ruled as *confirmation* of the design) in one call. A grep would
have returned the number and not the ruling.

**What failed:** comp-find content mode, above.

**Gap found — and it is the dangerous direction.** In CONTENT mode comp-find's HEAD band only elevates
files that ALSO carry a content hit. **A file whose NAME matches but whose CONTENT never states its own
name is INVISIBLE, and returns a clean zero over a 141,543-file denominator — which reads as absence.**
A filename census needs `--name`. ⛔ I first hypothesised that the HEAD band cannot reach `~`-suffixed
lane trees; **that was FALSE and my own earlier output refuted it**, having surfaced a `~J` path under
HEAD twenty minutes before. Surfaced to `3.0.0_SA_CVO` at 91507; not chased.

---

## Work Completed

### 1. The premise I was seated on was wrong, and it under-reported the work

Seated on "your predecessor's OWN LAST COMMIT `6cae614946`". It is not the last commit. **EIGHT commits
follow it**, through `6c7a202873` (2026-08-30T18:34:48Z): the silver stage entry point, the ruled
backfill EXECUTED 3 of 3, the Terraform mint APPLIED 9/1/0, and a proof-of-spec amendment that
`3.0.0_SA_CVO` acknowledged at 88978 on 08-31T19:00Z. A successor reading only `6cae614946` would
rebuild work already on origin. **A re-seat brief is a carrier and it ages like any other.**

### 2. The face's own re-seat condition had already been met

The 08-28 release note gates the open set on *"INS-a-5's first fire"*. INS-a-5 has fired on **four
consecutive scheduled 04:35Z days** — bronze present for 08-29, 08-30, 08-31, 09-01 across 23 bronze
keys walked. The condition was satisfied on 08-29 and nothing wrote it back. The note and the world had
drifted three days apart.

### 3. Every criterion measured on the world

| AC | face said (08-28) | measured 2026-09-01 | instrument |
|---|---|---|---|
| AC1 | PASS | **PASS, now EXERCISED not merely ruled** | Live S3. Silver at the ruled `fact_*` grammar for date=2026-08-31 and date=2026-09-01. Rule 17a re-measured: `.parquet` under `bronze/` = **0 of 23**; POSITIVE CONTROL, same matcher returns **7** over the 14-key silver set. |
| AC2 | APPLIED-GATED | ⛔ **GATE OPENED 08-31T04:35Z, LIMB UNBUILT** | See §4. |
| AC3 | AFTER-half gated | unchanged, correctly | `platinum/advi/` = 0 keys, so nothing insurance-derived has entered the AM serve. |
| AC4 | SHUT (sovereign) | **still SHUT — but its INSTRUMENT is dead** | See §5. |
| AC5 / AC6 | PASS | unchanged | SOURCE-grounded; no re-measurement owed and none taken. |

⚠ **AC1 carries a coverage hole its PASS does not cover, and the PASS is not falsified by it.** Three
convertible bronze days have no silver: 08-28, 08-29, 08-30. **Cause MEASURED, not inferred:** the
converter's own deploy landed 2026-08-30T08:06:05Z, after all three. (A fourth absence, 08-27
detailsearch, is DESIGNED — 50 of a vendor-attested 77, held UNCONVERTED-REFUSED.) AC1 was ruled on
*"3 of 3 CONVERTIBLE at the grammar"* — **a CAPABILITY claim, not a COVERAGE one.** It is a landing-plane
hole no criterion currently owns.

### 4. The headline — AC2's gate opened onto an unbuilt limb

```
  gold/advi/insurance/insurance_nav_current/  = EXACTLY ONE partition
      date=2026-08-25, LastModified 2026-08-27T19:12:18Z,
      ETag 3dd4f7e0c6f922ee4aed045e111a2d40   -> an AD-HOC QA artifact
  bd49f_insurance_nav_current.py = ABSENT from the DEPLOYED chain roster
```
⛔ **The roster was measured on the `_code/` the SSM document `advi-49f-chain-dispatch` ACTUALLY SYNCS**
(`s3://opal-data-49financial/_code/chain_49f_entrypoint.py`, 33,416 B) — **not the repo copy. DESIRED is
not APPLIED.** It carries a00–a07, b00–b03, c00–c02, c04 and `d_publisher_port.py`, and no insurance
stage. POSITIVE CONTROL: the same read enumerated all of those. **Gold is seven days stale against a
source now landing daily.**

### 5. AC4 is still shut and the world agrees — but the face's own instrument no longer resolves

`platinum/advi/` = 0 keys: the gate holds. But the AC4 block cites `advi-49f-publisher` State=DISABLED.
**That function does not exist** — a census of **all 200** Lambda functions in the account returns no
such name; POSITIVE CONTROL, the same matcher returns `opal-assets-silver-bd49finsurance` and
`advi-49f-gold-dispatch`. The live emitter is `d_publisher_port.py`, invoked inside the deployed chain
at `:351`. ⛔ **The sovereign gate is unaffected — a gate is a WORD, not a resource state** — but a hold
naming a SUBJECT rather than a PROPERTY goes unsatisfiable when the substrate shifts.

### 6. Ad-hoc QA, fired without waiting, then used to attack my own claim

Dry-run is the producer's default (`--write` is opt-in). Ran `--date 2026-09-01`: rc=0, 106 rows
reconciling, AC3 forbidden-field census 15 columns / 0 violations with neg 0 and pos 3-of-3 firing,
tie-out to the cent.

**Then I falsified my own "AC2 is ready" claim, which rested on ONE day**, by running 08-31 as well:

| | 2026-08-31 | 2026-09-01 |
|---|---|---|
| rc | 0 | 0 |
| export_total_value | 51,815,578.87460001 | 51,829,060.74680001 |
| gold_total_emv | 51,815,578.87460001 | 51,829,060.746800005 |
| value_delta_cents | 0.0 | 0.0 |
| AC3 census | 15 cols, 0 violations | 15 cols, 0 violations |

⭐ **The discriminator is that the totals DIFFER.** A producer coupled to a cached, hardcoded or
wrong-day source returns the same figure twice. The claim survived a test that could have killed it.
**Nothing written on either run.**

⭐ **The 09-01 tie-out is genuine corroboration, not repetition:** `0.7.0_AE_CloudOps~R` reached
`51829060.74680001` by reading the silver parquet with pyarrow (91452); I reached
`51829060.746800005` through the gold producer's own aggregation over a different code path.

### 7. The number I did not report

`spine_unassigned: 106` — all 106 rows — reads like AC2's core requirement failing outright. I opened
the producer instead. It counts the `account_id` leg only; `relationship` is 106/106 (from the nesting —
the `relationshipID` FIELD is NULL 106/106, so a field-join would have produced a clean, well-formed,
**totally empty** spine with no error) and `firm` is 106/106. The 0% overlap is ruled **confirmation of
the design**: insurance is held at carriers, not in the AM book. **Reporting it would have re-opened two
settled issuer rulings.**

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Wrote the face; ruled NO criterion; left `<status>` at `pending` | Criterion status is the ISSUER's and 73382 stands. The enum still cannot express issuer-ruled closure (0 of 1,067 rows carry CLOSED, census @4776a2305c). |
| Did NOT write a gold partition | An ad-hoc write puts a PRODUCTION artifact on an UNSCHEDULED route. It would not close AC2 anyway (ad-hoc artifacts are never production evidence) and would leave a partition whose provenance argues against itself — **exactly the shape of the date=2026-08-25 artifact I had just flagged**. Refusing to create the defect I was reporting. |
| Did NOT touch chain wiring | Infra is DT/AE, not the DS lane. |
| Did NOT backfill the 3-day silver hole | Spec is FROZEN mid-round; writing production silver is not a QA act. Named `2.0.0_SA_COO` as owner. |
| Did NOT move the stranded AC3 baseline | The precedent move (`4b358413d7`) executed an ISSUER re-pointing. No issuer has re-pointed this one. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INSURE.TO-R1-DS.landing-gold-platinum-planes.md` | +56 lines: dated MEASURED-STATE block, per-criterion, instruments and controls named | Yes — `b4efb4363c` |

---

## Briefs Written

None. Every finding went to the record as the face block plus MCP reports 91487/91488/91489 (the
measurement), 91494/91495/91496 (the QA result) and 91507/91508/91509 (the correction + falsifier).
A brief would have been a fourth carrier of the same content.

---

## Blockers

- **BLOCKED on `2.0.0_SA_COO`** — `ADVI_INSURE.TO-R1-DS`, AC2's applied limb. Needed: does it drive to a
  scheduled stage this round, or re-cut? **Verified, not assumed:** three sends returned QUEUED
  "no live session" (11:3xZ, 11:4xZ, 12:0xZ), and `3.0.0_SA_CVO` independently measured that serial
  absent from a 13-seat `get_live_agents` roster (91502) — two signals, two instruments.
- ⚠ **AND THE WORD ALONE DOES NOT UNBLOCK THE ACT.** What AC2's applied limb needs is CHAIN MEMBERSHIP,
  which is infra (DT/AE), not DS. Raised by `3.0.0_SA_CVO` in 91502 and it is correct. **The word
  unblocks a DECISION.** Nobody should read a single reply as sufficient.
- All three ARMED surprise items name `2.0.0_SA_COO` as owner — correctly disarmed by naming, and
  **disarmed is not remediated**, which bites harder when the named owner is absent.

---

## ⛔ AMENDMENT 13:2xZ — THE BLOCKERS SECTION ABOVE IS STALE, AND I AM RECORDING THAT RATHER THAN REPAIRING IT

**The section above is left exactly as written. This is an amendment, not an edit** — a log quietly
repaired teaches nobody, and the drift is the lesson.

**WHAT IS NOW FALSE:** *"BLOCKED on `2.0.0_SA_COO` … verified, not assumed."* `2.0.0_SA_COO` is **LIVE**
— re-measured on MY OWN instrument before acting, not taken from the correcting seat:
`get_agent_status` -> LIVE, PID 29020, last seen 1s, *"running org/XXX.md startup"*. **Stamped 13:1xZ,
and it will age exactly as the first reading did.**

⛔ **THE DEFECT IS MINE AND IT IS ONE RUNG BELOW THE ONE I SPENT THE SESSION GRADING.** The 11:3xZ
measurement was sound — three QUEUED sends plus an independent 13-seat roster read. **What was wrong
was restating it at 12:1xZ, in the Blockers section above, WITHOUT RE-READING ANYTHING.**
>> **A PERISHABLE CLAIM RE-ASSERTED IS A NEW CLAIM AND NEEDS ITS OWN MEASUREMENT.** "Verified, not
   assumed" was true of the first reading and false of the sentence that inherited its credibility.
   `3.0.0_SA_CVO` made the identical error at the identical hour (91552 s.2) and named the mechanism;
   **I wrote the same shape into a durable record while grading a durable record for being stale.** <<
⭐ The framing that closes it, from `0.4.0_DS_ClientPlatform~N`: **A LIVENESS CLAIM HAS A VINTAGE LIKE
A NUMBER DOES.** This log's Blockers section had none.

**DISPOSITION:** the ask was re-sent and **DELIVERED** (not QUEUED) at 13:12:39Z — one decision, with a
ranked read-order over the three messages already in that inbox and one marked SKIPPABLE, because a
startup context cannot use five equal-looking rows. Msg-ids 91554 / 91560 carry the exchange.

⚠ **WHAT DOES NOT CHANGE:** the blocker's SUBSTANCE. AC2's applied limb still needs CHAIN MEMBERSHIP,
which is infra (DT/AE), not DS. **The word unblocks a DECISION, not the ACT.** Only the *reason* the
word had not arrived was wrong.

**Also resolved, and NOT mine:** the unlabelled E2/INF-REDEPLOY row in 91552 was disambiguated at 91560
to `2.0.0_SA_COO`. I declined to infer it from a pronoun — Rule 27, ADVI_INSURE only.

---

## Current State

TO-R1-DS's face now carries a dated, per-criterion MEASURED-STATE block at `b4efb4363c` (**push state
MEASURED: LOCAL**; `origin/CLOUD` = `7036b1a065`, positive control the repo root commit reads ON).
AC1/AC5/AC6 stand PASS; AC4 stays SHUT behind the Andrew-direct 2026-08-21T19:18Z sovereign gate with
`platinum/advi/` measured at 0 keys. **AC2 is the live item: its gate opened 2026-08-31T04:35Z when the
deployed converter `opal-assets-silver-bd49finsurance` began writing daily silver, and its own recorded
gating reason — *"there is no silver to build gold from"* — is now FALSE on the world.** The producer
`data/assets/scripts/gold/bd49f_insurance_nav_current.py` is proven on live bytes across two independent
days (rc=0, tie-out to the cent, censuses clean) and is ABSENT from the deployed chain roster. Everything
on the DS side of that seam is done; the remaining act is chain membership, which is not this lane's.

---

## Next Steps

1. **[`2.0.0_SA_COO`, on return]** The one decision: does AC2's applied limb drive to a scheduled stage
   this round, or re-cut? Then the three ARMED items — the 3-day silver backfill (08-28/29/30), AC4's
   dead instrument name, and AC3's baseline pointer.
2. **[DT/AE lane, after that word]** Chain membership for `bd49f_insurance_nav_current.py` in
   `chain_49f_entrypoint.py`. **The DS side is finished and twice-proven; this is the actual gating act.**
3. **[`0.4.0_DS_ClientPlatform~R`]** On the word: drive AC2's applied limb, then re-take AC3's AFTER
   half — which only becomes takeable once something insurance-derived reaches the AM serve.
4. **[`3.0.0_SA_CVO`]** Holds the comp-find content-mode absence note (91507) and the CloudWatch-Logs
   evidence-substrate hazard `0.7.0_AE_CloudOps~R` armed at 91452 §4.
