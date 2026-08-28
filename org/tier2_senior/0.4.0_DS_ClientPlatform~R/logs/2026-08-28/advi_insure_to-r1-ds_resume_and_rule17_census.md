# ADVI_INSURE TO-R1-DS — resume, the gate that had moved, and the Rule-17 limb

**archetype:** MIXED
**Seat:** `0.4.0_DS_ClientPlatform~R` · **Window:** 2026-08-28 15:54–16:5xZ · **TO:**
`ADVI_INSURE.TO-R1-DS.landing-gold-platinum-planes` (the only thing in scope for this seat, per
`2.0.0_SA_COO` 78245)
⛔ **DISTRIBUTION: NOT TO `4.0.0_SA_CRO`** (PRD s.3, Andrew ~16:1xZ).

---

## Current State

**AC1 moved from `UNCOMPUTABLE-BY-DEPENDENCY` to `EMISSION-GATED`, and the landing plane went from
2 of 4 feeds to 3 of 3 convertible feeds — all three measured against Rule 17 for the first time.**

The predecessor session closed at 19:32Z on 08-27 with AC1 gated on `0.6.0_AE_PartnerETL` landing
real captures. **That gate had already opened and nothing told the seat.** The tree that `~J`
measured ABSENT on 08-25 (0 insurance keys over 480,954 walked, positive control 416) now holds
8,862 keys.

| criterion | state at close |
|---|---|
| AC1 | **`EMISSION-GATED`** (issuer 78303, transcribed verbatim). 3 of 3 convertible feeds landed; the 4th-feed count is an open issuer question — see the proposal |
| AC2 · AC3 | `APPLIED-GATED` / `AFTER-HALF-GATED`, unchanged — they read against the `0.6.0` bronze-leg deploy, which is not this lane's |
| AC4 | **SHUT** behind the arm-(a) sovereign gate. Not re-asked. |
| AC5 · AC6 | `PASS`, unchanged |

Instance re-validated: **rows=6, violations=0, VALID, TRUE rc=0** (`$?`, not a parsed string).

## What I Did

1. **`/watcher`** — lane `~R` read NOT REGISTERED with no watcher process. Registered (PID 19808),
   armed the persistent Monitor (task `bc0rx2hw2`, **parent-tied pid 1122709**, so the orphan
   self-exit is ARMED). Identity cross-check clean: `~R` LIVE at *my* PID, no peer conflict.
2. **Reported TO state to `2.0.0_SA_COO` + `1.0.0_SA_CTO`** (78279/78280) on first read, as 78245
   required — measured, not the face.
3. **Re-measured the AC1 gate** rather than inheriting a 3-day-old read. This is the whole session.
4. **Discharged INS-inv-4's Rule-17 limb**, which had been carried as *inferred from the 17a limb*.
5. **Extended `bd49f_insurance_conversion.py`** to a third feed on issuer ruling 78303 and **landed
   `fact_insurance_relationshipdetail/date=2026-08-27/`**.
6. **Proposed the receipt's silver shape** (78303(ii) delegated it to this seat).

## The Measurement

```
blackdiamond/49financial/           8,862 keys   (9 pages, summed CLIENT-SIDE)
  positive control blackdiamond/49f/  294
  layers: silver_legacy 7,921 | bronze_legacy 931 | bronze 8 | silver 2 -> 3
INS-inv-4 Rule 17a:  .parquet under bronze/ = 0   (positive control: under silver/ = 2)
INS-inv-4 Rule 17 :  3/3 CONFORM, F1=F2=F3=0 on every table
```

⛔ **A per-page `--query length()` returns the PAGE count** (Rule 22a). I summed pages client-side;
the raw output was nine lines of `1000…862`, which a single `length()` would have rendered as `1000`.

**The Rule-17 census is a new instrument** —
`org/tier2_senior/0.4.0_DS_ClientPlatform~R/deliverables/insurance_silver_rule17_census.py` — built
because `1.0.0_SA_CTO` (78287) asked that the same read run on four tables when the rest land.
Self-test PASS, arms firing from **different planted truths**: bronze drops a field → F2; silver
gains an invented column → F2; bronze drops rows → F3; fillna a null-bearing column → F4.

## Decisions Made

- **Landed a 1-row silver partition, and said so loudly rather than quietly.** `relationshipdetail`
  is a per-id fan-out; one call was made, so the partition is a **complete silver of an incomplete
  pull**. Silver converts what was pulled and must not invent the other 76. The producer now prints
  `COHORT COVERAGE: N of <authority>` and, when the authority is missing, `UNKNOWN — UNKNOWN IS NOT
  COMPLETE`. **Do not read 3-of-3 tables as 77-of-77 relationships.**
- **Did not build a completeness control for the new feed, and that is the decision.** `read_detail`
  enforces rows == the vendor's self-declared `total`. An S4 response ships no count, so comparing
  against the export's 77 would be a **cross-feed inference wearing a control's clothes** — a
  shortfall there means *fewer calls were made*, never *the vendor withheld rows*, and those demand
  opposite responses. Coverage is REPORTED, never enforced. **A number that cannot fail is not a
  control.**
- **Extended, never forked** (issuer 78303, build-ladder rung 2, NEVER-5).
- **No change-management ledger entry.** That class is infra deploys — both existing ADVI_INSURE
  entries are an IAM/Lambda package — and the precedent for this exact producer is `~J`'s two
  partitions `@4b494cf3ae` with none.
- **Did not edit any criterion status.** 73382 stands on synthesis; 78303 authorised *transcription*
  of AC1's status_reason, so it is verbatim, with my post-ruling measurement appended as a
  **separately marked** note. Editing the issuer's sentence to match my later measurement would
  destroy the basis for auditing either one.

## Files Modified

| file | what |
|---|---|
| `data/assets/scripts/silver/bd49f_insurance_conversion.py` | +`FEED_DETAILREL`, `read_relationshipdetail`, `_cohort_authority`, per-feed fault isolation; docstring corrected 3→4 families |
| `…~R/deliverables/insurance_silver_rule17_census.py` | NEW — the Rule-17 instrument |
| `…~R/deliverables/ADVI_INSURE_TO-R1-DS_RECEIPT_SHAPE_PROPOSAL_20260828.md` | NEW — 78303(ii) |
| `…~R/deliverables/ADVI_INSURE.TO-R1-DS_PROOF_OF_SPEC.json` | AC1 transcription + evidence; `assignee` ~J→~R |
| `s3://opal-data-assets/…/fact_insurance_relationshipdetail/date=2026-08-27/data.parquet` | **MINTED**, 28,086 B |

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-pipescript io` | on the silver script, **BEFORE the write** | **OUT-OF-GRAPH** — answered by AST derivation. 7 I/O sites: READS 0, WRITES 0, **UNRESOLVED 7**. Unresolved ≠ absent |
| `comp-pipescript postdeps` | `--firm 49f` then `--firm bd` | `49f` is **not a valid choice** (bd/inf/cot/mdpf) — 49F is a *scope* under blackdiamond, not a firm. `--firm bd` → **rc=2 REFUSED**, script not in the bd gold tree |
| `comp-validate` | on the silver script | **no config** — `UNVALIDATED`. Never signal SAFE on it; I signal nothing to AE |
| `.tools/commit-gate.sh` | both `.py` files, each edit | clean, 1 of 1 |
| `proof-of-spec-check` | positional, all six ids | rows=6, violations=0, **VALID, TRUE rc=0** |
| `comp-which` | not run this session | The two questions were "did these exact S3 keys change since 08-25" and "what is in this parquet" — both are direct artifact reads at a known path, and the raw calls carry `# rail-checked:` markers |

⛔ **BOTH GOLD-LANE DS GATES ARE STRUCTURALLY BLIND TO THIS PRODUCER, AND THEY FAIL DIFFERENTLY.**
`postdeps` **fails closed** (rc=2 REFUSED, universe printed) — correct. `comp-validate` returns
`no script matching` and lists candidates; its shell rc was 0 through a pipe, so **a caller reading
`$?` after a pipe would score an unvalidated script as fine.** This corroborates the predecessor's
finding on the *gold* producer with a **different subject** (the silver script), so it is a second
observation, not a repetition of the first.

## Blockers

**None at this seat.** Two items are gated elsewhere, evidence-cited:

1. **AC2/AC3** read against the `0.6.0_AE_PartnerETL` bronze-leg deploy — `2.0.0_SA_COO` seats that
   lane under its own TO (78303). Not mine.
2. **AC4** — Andrew's arm-(a) word. Not re-asked.

**One thing is owed TO me and it changes AC1's close condition:** `2.0.0_SA_COO`'s ruling on the
receipt shape. 78303 sets AC1 to close at *"4 of 4"*; if my proposal is adopted the reachable
maximum is **3 of 3** and the condition must be restated, **or AC1 cannot close on its own terms.**

## Surprises Routed

Three OBSERVATION/INERT, all filed in the instance and reported to `2.0.0_SA_COO`:

1. **The 2026-08-27 detailsearch pull is incomplete** — 50 rows against a vendor-attested 77, only
   `page0` landed. `~J`'s completeness control caught it and correctly refused the conversion. A
   finding about the **pull**, owned by whoever ran it.
2. **It exposed a coupling defect that was mine to fix** — that raise aborted the whole run before
   `relationshipdetail` was reached, so **the controlled feed silently took the uncontrolled one
   down with it.** Per-feed fault isolation; the error still prints in full and still forces rc=1.
3. **This instance's own `assignee` was stale for three days** — `~J`, with `session_log` pointing at
   a dead lane, while the TO's `<issued_to>` reads `~R` and the file was moved to `~R` `@4b358413d7`.
   **The move corrected the path and not the identity inside it,** and nothing compares the two.

## Closing note — the error that is worth carrying forward

**I reported "2 of 4 bronze tables lack silver" to two exec seats, and the correct answer was
already written in my own lane's code.** `insurance_insurancerelationshiplist` is the async export
**job receipt** (77 bytes of `{exportResultID, resultGuid}`), and `…_export` is an **XLSX workbook
under a `.json` key** (magic `50 4b 03 04`). Both facts sit in
`bd49f_insurance_conversion.py`'s docstring, written by `~J` on 08-25 `@4b494cf3ae`.

I inferred four data tables from four bronze **prefix names** and routed that upward. `2.0.0_SA_COO`
reached the right reading independently at 78303 — so the record self-corrected, but only because a
second seat happened to read the source I should have read first.

> **Build-ladder rung 2 — "the estate already has it" — is usually cited before BUILDING something.
> The cost here was at the REPORTING step, one turn earlier, and it was about to seat a lane to
> convert a job ticket into a fact table.** The general form: *a prefix is not a table, an extension
> is not a carrier, and a name is not an identity.* The remedy is not more care — it is opening the
> object, which cost one `cat` and one `od -An -tx1 -N16`.
