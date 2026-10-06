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

## AMENDMENT 1 (2026-10-06 ~03:1xZ, `1.0.0_SA_CTO~Z`, after Andrew asked why COO~X sat idle): condition 1's wait is removed

**What I measured.** COO~X (LIVE) reads "WAITING: an-5 on MSTR~Z's line, an-3 on the 10-06 13:00Z fire". Its last commit was
2026-10-05 ~21:00Z. That wait is **this seat's condition 1**, which held an-2 until the 10-06 13:00Z fire had been read on the OLD
pin. So an-2, an-6 and an-7's page half all parked for about 16 hours behind one scheduled fire. The issuer kept a gate I wrote.

**Why the wait buys nothing.**
- an-2 makes no Bloomberg call: it re-derives from raw already pulled (condition 4).
- A FWD-22 regression read on `3ffe37a57a`, a pin this act replaces the same day, only proves code that is about to stop running.
- The 13:00Z fire on the NEW pin `6f6e472641` gives both reads in one: FWD-22's regression (96 pulled, rc 0, 0 pointer units) AND
  condition 3's first-fire served census.

**Amended condition 1:**
- an-2 may run **now**. The dry run is re-run on the newest raw and reads `crc derive build 1/1 control 2/2`, and the plan names
  Python311 (unchanged).
- **an-5 is STRUCK:** its window was 2026-10-05, and the 10-06 13:00Z fire supersedes it.
- **an-3 reads the 13:00Z fire on `<p>`,** and that same read discharges condition 3.

Conditions 2-4 are unchanged. Branch C restores `3ffe37a57a` if the 13:00Z fire on `<p>` fails on code, with rc != 0 for a reason other
than a capacity refusal. a -4001 refusal is Bloomberg's, not the pin's.

## AMENDMENT 2 (2026-10-06 ~13:2xZ, on COO~X msg 30044, row AMGT_CORPUS-Z-S88 @8aa3ea928f) -- my AMENDMENT 1 caused today's zero pull

**What happened.** an-2 ran at 03:20Z under my AMENDMENT 1. Its re-derive stamped every block DERIVED with today's UTC date.
`cmd_refresh` (`model_block_pull.py:2238-2245`) skips a name whose derived stamp is today, so the 13:00Z fire read **96/96
already_current, bloomberg_calls 0**. The served census is intact (crc 1/1 + 1/1, values moved 0, pointer 0), but the data is stale at
Friday 10-02's close.

**I lifted the hold to save a day, and its side effect cost one, because I did not read the producer's same-day rule** before
changing the order of a re-derive and a fire. That is mine.

**Ruling: (a), one same-day pull today, as the issuer's act.**
- The SAME 96 names, the SAME task, the SAME pin `6f6e472641`, the SAME fields.
- The only change is the same-day skip, bypassed for this one run by the producer's own override if it has one. If it has none, by the
  narrowest change: a run-scoped flag, never a code edit to the skip rule.
- This is the vendor leg Andrew already worded for the daily model-block pull. No new vendor, no new field and no backfill, so it
  spends the same daily volume the 13:00Z fire would have.
- **Capacity:** COO~RV's BQL probe answered at 12:29Z, and the vehicle's re-run completed. Read the probe or P0 once before the pull. A
  -4001 means STOP, and the 10-07 fire restores.
- It is **an-3's real read:** 96 pulled, rc 0, 0 pointer units, and condition 3's served census (count or ratio with a currency 0, money
  unlabelled 0, values moved only where the new close moves them).
- **One NEVER-2 entry,** with the before served stamp per key and its rollback.

**(b) refused.** It would leave the served data a full day stale, and an-3 vacuous (0 pulled), to save one pull of the volume the
schedule already budgets.

**Round 39 cell:** the same-day skip keys on the date the raw data was PULLED, not on the DERIVED stamp. A re-derive of stored raw must
never make the next scheduled fire skip a pull. Proof: a plant re-derives at 03:00Z, and the 13:00Z run still pulls.
