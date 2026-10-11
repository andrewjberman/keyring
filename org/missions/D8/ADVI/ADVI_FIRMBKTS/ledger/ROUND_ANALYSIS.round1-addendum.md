# ADVI_FIRMBKTS -- ROUND 1 ANALYSIS, ADDENDUM 1 (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~02:2xZ)

**Input:**
- the CVO's round-1 L10 slug (msg 3303);
- `surprise-channel/remediations/REMEDIATION_v2.md` @b7ab3268d1.

The slug agrees with `ROUND_ANALYSIS.round1.md` @4c9229fee2 on FWD-1 PARTIAL and confirms the S10 disarm. It names two rows the analysis
did not place. This addendum places both. The ENDPOINT is unchanged; sections 1-4 of the analysis stand.

**Hold:** Andrew-direct 2026-10-10 ~21:1xZ holds heavy drive ops on dell1. This addendum is a ruling and cuts nothing. The round-2
issuance by `2.0.0_SA_COO~F1` waits for that hold to lift.

## 1. ADVI_FIRMBKTS-D1-S2: R19, not a rider

**Ruling:** FWD-2's domain stays the three legacy buckets. The 08-18 template's tier-first `gold/advi/**` keys in `opal-data-49financial`
are an existing pipeline's output. Under `infra/logic/02_DOCTRINE.md` R19 (CLAUDE.md rule 30, non-application), that pipeline reaches
conformance through its own migration project, never as a rider here. W2-S10's `_campaign/` prefix is ruled the same way.

**Bound on round 2's F7:**
- F7 writes only at `address()` paths and touches no residue key.
- Its negative arm prints the residue key count under `gold/advi/` and `_campaign/` before and after the copy. The two counts must be
  equal, with the denominator printed.

**Owner:** `1.0.0_SA_CTO~DELL1` registers the producing pipeline's R19 migration row when the dell1 hold lifts. That registration is the
un-park condition. This ruling closes the row's remedy ("the addendum or ruling exists and names this row").

## 2. ADVI_FIRMBKTS-S11: placed in round 2 as enrichment item 6

6. **The literal rename in `build_canonical_prices_v2.py`, with the tolerant-load patch in the same diff.**
   - The new name is builder output (`lib/opal_naming.py`), never typed by hand.
   - The patch is `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ADVI_FIRMBKTS_INPUT_S00_TOLERANT_LOAD.patch`
     @091ccbafa2.
   - The optional S_00 step changes the cot-pipeline's SSM terraform, which is a served change. It rides its own never-widen pair
     (blast radius: one new step ahead of A_00; rollback: remove the step) and lands by `safe-apply`.
   - Three mechanical criteria at most:
     1. the naming gate passes on the diff;
     2. the build runs with `silver/historical_prices.parquet` and `config/ticker_lookup.json` absent, and exits 0;
     3. with the S_00 step included, one SSM run reads SUCCESS.

   The issuer may drop the S_00 step from the cell and state why. The rename and the patch do not split.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-11 ~02:4xZ) -- the hold lifted; D1-S2's R19 home; the COO seat

**Hold:** Andrew lifted the dell1/dell2 hold at ~01:58Z, record @cbcfdc0c1c. Round 2 is no longer gated on it.

**D1-S2, un-park condition met by an existing row.** The residue's R19 home is already registered:
`infra/logic/06_CONFORMANCE_LEDGER.md` @ebd078314d, the `opal-data-49financial/gold/` row (DECIDED). It reads MIGRATE
(grammar), re-folding `gold/` to `advi/49financial/gold/` (R1 v0.3, source-first), plus MIGRATE (format), json to parquet.
The tier-first `gold/advi/**` classes D1-S2 measured sit inside that plane. This seat therefore adds no second row. The
migration project itself does not exist yet; it opens through its own L1 brief (`4.0.0_SA_CRO`), never as a rider here.
Round 2's F7 bound stands as section 1 states it.

**COO seat: `2.0.0_SA_COO~B1` replaces `2.0.0_SA_COO~F1`.** ~F1 is not registered (bus read ~02:4xZ) and its last log
(2026-10-08) is on another project. ~B1 is live on dell1 with no project, and asked for this seat (msg 3298). This call
touches only dell1, so this seat rules it. `project.json` `leads.coo` now names ~B1. ~B1 is the ONE issuer of round 2:
a relaunched ~F1 does not issue into this project. Round 2 is cut from `ROUND_ANALYSIS.round1.md` @4c9229fee2 plus this
addendum (items 1-6), in one issuance.

-- 1.0.0_SA_CTO~DELL1
