# AMGT_CORPUS -- ROUND 26 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-01 ~00:5xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27459, *"L10 slug AMGT_CORPUS round 26 @00575fa0ba"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v31.md` (read to EOF, 5,777 B). Issuer packet: `ROUND26_DRAIN_END_PACKET.md` @`aa35ffcdca`.

**Round 26 is CLOSED:**
- 4 of 4 orders terminal, plus the ab-4 act, whose ledger is CLOSED;
- `Z-S71` GRADUATED;
- `Z-S70` disarmed @`1730652e13`;
- 0 judgment criteria.

**The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED (the CVO's re-read on the served plane)

- **UNRESOLVED units over 100 keys: 31 -> 11** (BBSE3 10, TSM 1), with 0 sign contradictions.
  - BP's `PE_RATIO` reads RATIO and `PROF_MARGIN` reads PERCENT: the series-median rule (round-25 ruling 2) works as ruled.
- **BP's market cap** serves no currency, with "UNMEASURED: the value is measured in GBP ...". A wrong USD label became an honest
  absence. The negative arm holds: BA stays USD.
- **`Z-S71` end to end:** BP's and NG's newest dossiers reference their encoded current blocks.
  - The CVO's own first read sorted dossier keys lexically, which orders by hash, and returned an older object. It re-read by
    `LastModified`. That is the instrument trap a time question needs, and it was corrected in the same read.
- **The packet's correction:** round 25's "375 measured" was 365 measured plus 10 to UNRESOLVED. That confirms v30 and this seat's own
  aa-4 miss.

## 2. RULINGS

1. **BP's mixed-currency case input (778.57) is read on the payload after AMGT_RESAPP's scoped-API redeploy** (RESAPP round 56 item
   1, ruled 23:30Z).
   - The block carries the fix; the deployed `case_rule` does not.
   - No page face renders the input (aa-4 AMENDMENT 2).
   - That read is CORPUS's round-27 FWD check. It is not a CORPUS cell.
2. **A NEVER-2 ledger sentinel is committed after EACH leg close** (the issuer's defect 2). Two leg closes reverted in an uncommitted
   working copy: the "shared tree loses uncommitted work" class.
   - Adopted as issuer discipline.
   - It is also this seat's input to `Z-S322` (`deploy_ledger.py` staging), which this seat owns: the tool should commit the
     sentinel itself, under the caller's author, pathspec-scoped.
3. **BBSE3 `CAPITAL_EXPEND`** (6 zeros in 10 years; an insurer with near-zero capex) stays UNRESOLVED this round.
   - A zero-dominated series has no magnitude to classify by.
   - The honest fix is a classifier rule that reads ZERO-DOMINATED as its own class ("no magnitude: n of m years are zero"), never a
     guessed unit. That is round-27 cell 1.
   - **TSM `CURR_ENTP_VAL` stays UNRESOLVED.** Its currency is measured only by the EV identity, which is not a census instrument, so
     it is an honest absence.
4. **The 2 pre-existing test failures** (`test_readonly_proof_bound`, `test_harvest_prefixes`) are routed to their owners, by lane and
   last author, as one row each. They stop riding every drain's hygiene line.

## 3. FWD GRADES

- **13 of 19 REALIZED.**
- **Standing:**
  - the six render outcomes are MET on local DEV, with the PROD promotion pending (Andrew);
  - `r-1`'s scheduled positive branch waits on a fire with a population of at least 1.
- The served-label FWD (TSM, BP) holds, with honest absences where a currency is unmeasured.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 27 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **A ZERO-DOMINATED unit class** in `build_unit_map` (ruling 3) | LOCAL | The AC: BBSE3 `CAPITAL_EXPEND` reads the new class, with its count. A planted all-nonzero series still classifies by median. Every other key's unit is byte-unchanged over 100 keys (the full (from, to) census). |
| 2 | **The paired re-derive of BBSE3 only**, carrying cell 1 | WORLD, pair | The expected diff is 10 unit-reason strings on BBSE3, 0 values. The positive arm comes from the serializing dry run. |
| 3 | **Owner rows for the 2 base test failures** (ruling 4) | LOCAL | One row each, with lane and owner named. |

**Fan-out:** 1 and 3 are independent. 2 follows 1.

**Watch, not a cell:**
- BP's `/thesis` payload after RESAPP's round-56 redeploy (ruling 1);
- `r-1`'s first fire with a population of at least 1.

## 5. ACTS ONLY ANDREW CAN DO (cited)

- **Portal PROD promotion** [CLAUDE.md Portal]: the six render outcomes.

## Compiler Tools

- The CVO's v31: the 100-key census; the deployed `/thesis` invokes (BP, BA); the dossier reads by `LastModified`.
- This seat ran no new instrument for this analysis.
