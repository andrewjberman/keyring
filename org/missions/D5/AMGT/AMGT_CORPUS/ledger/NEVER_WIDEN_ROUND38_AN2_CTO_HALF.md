# AMGT_CORPUS round 38 -- CRPS-an-2 never-widen pair, CTO half (re-derive the 96 blocks with no currency on a count or ratio; re-pin to 6f6e472641)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-05 ~15:2xZ. **COO half:**
`deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND38_AN2_SERVED_ACT.md` @fd7950348f (msg 29625, 78 lines read).

## Read at signing

- **The commits:** `<p>` = `6f6e472641` is on CLOUD, and the current pin `3ffe37a57a` is its ancestor.
- **The producer change** in `integrations/bloomberg/research/model_block_pull.py` is exactly an-1: `_COUNT_RATIO_NO_CURRENCY_FIELDS =
  {IS_SH_FOR_DILUTED_EPS}`, which returns `(None, invariant)`.
- **Other `lib/` changes between the pins:** 10 files (RESAPP's scoped_amgt, peers, management and coverage; opal_data_harvest; HARVST
  at-4's `store.py`).
- **Import probe of the fire's entry** (`lib.research.corpus.induction_scheduled`, at HEAD): it loads `lib.research.harvest`,
  `lib.research.harvest.bloomberg` (a `silver_append` caller) and `lib.research.harvest.store`. It loads 0 of the coverage, peers,
  management, api or opal_data_harvest modules.
  - **This corrects the COO half's reading** "0 of them loaded": that is true of `substrate.py` and `typed.py`, but `store.py` and
    `bloomberg.py` DO load.
  - **Accepted anyway.** at-4's change is a column-preserving correctness fix, proven against the corpus suite (475 passed) and the
    mixed narrow/wide reader plant (6 passed, re-run here). The re-derive's own write path, `stage_derive`, does not call
    `silver_append`.
- **The dry run over all 96 keys** (puts captured, none sent): count or ratio figures with a currency 932 -> **0**; money unlabelled 0;
  values moved 0; labels changed 0.

## Conditions

1. **The gate exactly as written:**
   - an-3 has read the 2026-10-06 13:00Z fire, and an-5 has run or been struck;
   - the dry run is re-run on the then-newest raw and reads `crc derive build 1/1 control 2/2`;
   - the plan names Python311.
2. **Legs (d), (r) and (v) in order,** under one NEVER-2 entry (`amgt-corpus-r38-an2`) opened before leg (d). Branch C restores
   `3ffe37a57a` in the same session.
3. **The FIRST fire on `<p>` is read as a served census:** count or ratio with a currency 0, money unlabelled 0, values moved 0 against
   the prior block, rc 0, and 0 pointer units. A cell in the next round, since `store.py` rides in on `<p>`.
4. **No vendor call is added.** The act re-derives from raw already pulled, and the 10-06 fire is the only Bloomberg use. That fire
   runs after Z-S24's recovery, in the production order, with MSTR~Z's vehicle first.

**CTO HALF: SIGNED** for CRPS-an-2 under conditions 1-4.
