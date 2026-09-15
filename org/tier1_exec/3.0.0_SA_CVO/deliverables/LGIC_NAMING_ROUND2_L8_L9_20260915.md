# LGIC_NAMING ROUND 2 -- L8 COMPILE AND L9 ADJUDICATION

**Author:** `3.0.0_SA_CVO` (Chief Validation Officer).

**Input:**
- 2.0.0_SA_COO~G's drain-end read, msg 96792: 8 of 8 orders drained, the last merge @`5cbcfec371`.
- The issuance @`b9ea6f3686`, 8 orders, on decomposition v4 @`32795c348c` s.0c, under PRD v1.6 @`2706014705` (ADMITTED).
- Round 1's carriers `ADJUDICATION_v2.md`, `C-S3`..`C-S12`. C-S11 carries S14 and C-S12 carries S15.

**Push state:** LOCAL. This seat does not push.

**Every figure below is this seat's own read**, re-derived with its own instrument: rows parsed from every JSON fence, criteria
re-run on a different checkout, answer files read directly. The drain message was a pointer, not a verdict to inherit.

**Result:**
- **L8:** 7 new rows, all carried by `C-S13`..`C-S17` @`b10229bdf3`: 4 DISMISSED_WITH_REASON and 3 GRADUATED. There is
  also this seat's own FWD-1 observation, `C-S14`, and the grade record. Carrier-less: 0 of 42.
- **L9:** 1 judgment criterion, F1R-J1, graded PASS with a named qualification.
  - FWD-1 is NOT REALIZED.
  - FWD-2 is NOT REALIZED on its reading limb and REALIZED on its one-referent limb.
  - FWD-3 is REALIZED on canonical forms.
  - FWD-4 is REALIZED on its reading limb.
- **L10:** the two FAIL orders, LN-e-3-r2 and LN-e-5-r2, read `pending` with VALID proofs. See section 5.

---

## 1. L8 -- THE COMPILE

**The population, by set difference over two git states:** round 2's new rows are the investigation rows at HEAD that
were absent at the issuance commit `b9ea6f3686`.

| | at HEAD | at issuance |
|---|---|---|
| `INVESTIGATION_v1.md` | 42 | 35 |

- **42 - 35 = 7 new:** S16, W1-S6, W2-S5, W3-S4, W4-S1, W4-S2 and W6-S4.
- **The carrier-less census at HEAD before this record was exactly those 7.** The difference is 0 either way.
- **Between rounds:** the rows that landed after round 1's L8 input (@`d292bca3ba`) and before the issuance are S14 and
  S15. They are already carried by C-S11 and C-S12 (@`8f291c8770`).
- **By class and hazard:**
  - BLOCKING: W6-S4.
  - ARMED: W1-S6, W2-S5 and W3-S4, each with disarm owner 2.0.0_SA_COO~G. That seat disarmed them with the fix
    @`ca44748a44`, recorded as S16.
- **After:** carrier-less 0 of 42 (read at HEAD after @`b10229bdf3`).

## 2. L9 -- THE CRITERIA, RE-RUN ON A DIFFERENT CHECKOUT

**Census:** 8 orders, 26 criteria, and exactly 1 judgment criterion, F1R-J1 (`judgment="true"` parsed from every order).

- **The re-run:** this seat re-ran all 25 machine criteria with `check_ln_r2.py` on the SHARED tree (cwd = workspace root,
  core.autocrlf=true). That is a different checkout from every writing worktree, so it is not a repetition of the issuer's
  or a worker's run.
  - **23 printed their expected VERDICT.**
  - **2 did not:** E3R-AC1 `VERDICT: FAIL-DIFFERENT` and E5R-AC1 `VERDICT: FAIL-MISREAD`. Each equals its instance's status.
- **The proofs:** `proof-of-spec-check.py` read VALID (rc=0) on 8 of 8 instances. Every run was BOUND with
  `--governing-order <its own order>`, which is this seat's commitment on IRPT_FNTEND-W4-S14. Each frame printed
  `governing-binding: BOUND`.

## 3. THE OUTCOMES, GRADED AGAINST THEIR OWN TEXT (PRD v1.6 :34-76)

### FWD-1 -- NOT REALIZED (C-S14, GRADUATED)

- **Agreement:** namer A wrote the ruled name on 18 of 18, and namer B on 15 of 18.
- **The basis:** it is the one C-S12 committed. On the 17 items other than i15, **14 agree**. i15 agrees too, but its
  answer is spelled in the briefing. i05 counts, as the output of the bucket rule.
- **The three differences, read by this seat from `exercises/r2/n3-namer-{a,b}.tsv`:**
  - i03: A `orion-inf-ingest-daily`, B `orion-inf-orion-ingest-daily`.
  - i10: A `smartx-49f-platform-export-weekly`, B `smartx-49f-smartx-platform-export-weekly`.
  - i11: A `pathfinder-etfs-ingest-task`, B `pathfinder-etfs-pathfinder-ingest-task`.
- **FN1 admits namer B's reading.** At `NAMING_SCHEMA.json:59` @`2706014705`: *"Where the item NAMES the process or
  subject as a noun phrase (the SmartX platform export, the Orion ingest, ...), the function is that phrase as named,
  kebab-case, ONE token"*.
  - Nothing in the clause drops a phrase token already written in the system slot.
  - Its own example, "the Orion ingest", is item i03.
  - The ruled table applies that subtraction unwritten.
  - **So the split is the schema's, not the namers'.** E3R-AC2 PASS (one prompt, two sessions, two folders) excludes
    conferring.
- **No worker row carries this FAIL, so C-S14 does.**

### FWD-2 -- NOT REALIZED on the reading limb; REALIZED on the one-referent limb (C-S15 on W6-S4, GRADUATED)

- **Measurable:** the canary read blind (E4R-AC1..AC3 PASS), so FWD-2 can be measured in this fabric. That answers
  round 1's C-S6.
- **The reading limb:** E5R-AC1 is 16 of 18. The two misses:
  - i09: `demo`, marked none. The spine calls it "a tenant class the doctrine does not define" (`05_IDENTITY_SPINE.md:69`).
  - i11: the vendor `pathfinder` in the system slot, marked as the firm. The key has read none since RULING Q.
- **The one-referent limb:** E5R-AC2 PASS, 0 clashes.

### FWD-3 -- REALIZED on canonical forms; F1R-J1 PASS with a named qualification (C-S13; C-S17 GRADUATED on W4-S1 and W4-S2)

- **The machine criteria:** F1R-AC1..AC5 PASS on the re-run. Dispositions: 68 attributed, 0 excluded, 1 raise
  (68 + 0 + 1 = 69).
- **Scope of the catch:** the four patterns catch 68 of 68 canonical forms, and 12 of 68 live names today. The renames
  are LGIC_ENFORCE's.
- **F1R-J1, graded here:**
  - This seat's own script compared round 2's record JSON with round 1's: **68 of 68 attributions identical** in firm
    and canonical form.
  - Round 1's were graded F1-J1 PASS on 12 hand re-derivations (C-S3). Six of those were re-read in round 2 and carry
    the same values.
  - The one change: `wp5-49f-feeder-scheduler-role` under `raise`, step R1.f. `GRADING_RULE.md:150` reads *"Any other
    t1 is in no vocabulary. RAISE: a token no registry row resolves."*
- **Qualifications:**
  - (1) 31 of 68 forms carry a kind word inside the name, which FN1 v1.6 forbids. This seat recounted it with the
    schema's 20 kind words (row W4-S2).
  - (2) The face paraphrases the bd step as position, but R3 tests adjacency. This seat counted 20 bd roles, 12 with no
    adjacent firm token, all bd-first (row W4-S1).
  - (3) 48 of 68 forms carry `{system}` (PH1).

### FWD-4 -- REALIZED on the reading limb

- **The reading limb:** L3R-AC1 read 6 of 6 conforming addresses right, including a3, the code tier that round 1
  missed. L3R-AC2 flagged the control.
- **The "older descriptions say they are replaced" limb** was served by round 1's LN-l-1. It is not re-graded here.

## 4. THE CARRIERS (`ADJUDICATION_v3.md` @`b10229bdf3`, a NEW file)

| carrier | adjudicates | disposition |
|---|---|---|
| C-S13 | (grade record, F1R-J1) | DISMISSED_WITH_REASON |
| C-S14 | (this seat's FWD-1 observation) | GRADUATED -> 1.0.0_SA_CTO |
| C-S15 | W6-S4 | GRADUATED -> 1.0.0_SA_CTO |
| C-S16 | W1-S6, W2-S5, W3-S4, S16 | DISMISSED_WITH_REASON: the disarm is EXERCISED, 8 of 8 seat criteria PASS on the shared tree; `.gitattributes` carries `exercises/r2/seats/** binary` |
| C-S17 | W4-S1, W4-S2 | GRADUATED -> 2.0.0_SA_COO~G (W4-S1), 1.0.0_SA_CTO (W4-S2) |

- 5 rows, and 0 jsonschema violations against `investigation_item.schema.json`.
- The widened grades pattern `^[A-Za-z0-9]+-(AC|J)[0-9]+R?$` (@`120afe354e`) admits F1R-J1 with no override.

## 5. L10 -- THE GATE

**REMEDIATION_v2 LANDED at the channel path @`ab8d584c0f`:** 6 rows, all OPEN, round v2, and 0 violations against
`remediation_row.schema.json`.
- The committed bytes equal the built file (sha256 `11d7c66a...`, 8511 bytes).
- The rows are C-S14, W6-S4, W4-S1 and W4-S2, plus S14 (from C-S11) and S15 (from C-S12). The last two were owed from
  round 1's late carriers.

**The gate facts, in order:**
1. **At this seat's census,** LN-e-3-r2 and LN-e-5-r2 read `pending`, with VALID proofs and FAIL rows (E3R-AC1, E5R-AC1).
2. **The first remediation attempt did not reach the gate.** safe-commit refused it (rc=3): *"REFUSED -- A MERGE IS IN
   PROGRESS IN THIS WORKTREE ... MERGE_HEAD : 81285c0abd"*. That was 0.9.0_WK_LGIC_ENFORCE~1's EN-b-1 drain, an unmerged
   conflict on LGIC_ENFORCE's channel. *"NOTHING WAS STAGED BY THIS RUN."* This seat waited for the merge to clear and
   did not override.
3. **2.0.0_SA_COO~G flipped both orders `pending -> complete` @`b9fa612c43`** (2026-09-15T00:50:16Z), *"on RULING T,
   applied to round 2 by 1.0.0_SA_CTO (96793)"*.
4. **The attempt that reached the gate** (after a second foreign merge cleared) was ADMITTED. The gate read, per row:
   *"L10 precondition ... 22 task order(s) at HEAD on both roots, 0 open; 42 investigation item(s) across 5 channel
   file(s) in the index, 0 undispositioned; route admitted"*.

**So every LGIC_NAMING order reads terminal at HEAD: 22 of 22 `complete`.** That is the un-park condition of round 1's
held remediation, `LGIC_NAMING_ROUND1_REMEDIATION_HELD_BY_GATE_20260914.md` @`f679b1e2b5`. This record does not land it.
It lands unchanged at `remediations/REMEDIATION_v1.md` by the parent session, with no further message.

**Named for 1.0.0_SA_CTO at L10:**
- **The two FAIL orders, closed on RULING T (96793).** The FAILs are the round's measurement: FWD-1 at FN1's clause and
  FWD-2 at demo and vendor-as-system.
- **W4-S2:** GRADING_RULE.md, v1.4 vintage, against FN1, in 31 of 68 forms.
- **The widened clean-context seat.** Decomposition v4 s.0c widens it from the reader to all four blind cells, because
  a worker namer's worktree holds round 1's answer files and the analysis s.2 table. 4 of 4 canaries read blind. Andrew
  holds the standing-mechanism question.
- **S16:** the seat records are pinned byte-exact by the root `.gitattributes`, and this seat EXERCISED that on the
  shared tree.

**NOT EVALUATED here:**
- FWD-4's "older descriptions replaced" limb, served in round 1 by LN-l-1.
- FWD-5, which no round-2 cell serves.
- The four seats' raw session transcripts, beyond the checker's own re-derivation.
- Any live AWS state, because no egress was used.
