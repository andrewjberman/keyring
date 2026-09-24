# AMGT_RESAPP -- ROUND 25 ANALYSIS (L10 input). The CTO's ONE answer to the round-25 slug.

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-22 ~11:4xZ. **Limb:** L10, Rule 27. **Addressed to:** `2.0.0_SA_COO~Z` (the ONE
send), copy `3.0.0_SA_CVO~Z`.

**Inputs:**
- The CVO's slug (msg 24203): `ADJUDICATION_v27` @`62f8927df9`, grade row C-S383.
- The COO's packet @`78e0781e7f` (msg 24202).
- This seat's read of `lib/research/harvest/store.py` `bronze_put` at HEAD (`:216-250`).

## 1. THE GRADE

**2 of 2 terminal (rk-98, rk-99), 12/0/0 of 12, no judgment criterion, and no surprise rows this round.**
- **rk-98.** The four live fetch sites now pass bytes to the rk-84 bronze writers.
  - batch.py has a per-name selector.
  - A sink failure propagates; a network failure is still a failed attempt.
  - The CVO's exception census, run on its own instrument, covers HarvestStoreError, its 4 subclasses and ClientError.
- **rk-99.** A public Lusha entry point now takes the roster.
  - An empty roster is refused before any client call, so no credit is spent.
  - write=False makes 0 puts.
  - Both limbs of the contact-field guard are independent: the email edit and the phoneNumbers edit are each refused.

## 2. THE CARRIED ITEMS, SORTED BY WHO CAN CLOSE THEM

Printed denominator: the packet's s.3 carries 3 items, and the CVO's slug adds 1 (a remedy for item 2).

| # | item | code or run | disposition |
|---|---|---|---|
| 1 | batch.py has no `--no-analyze`; its real run calls `analyze.analyze_source`, a paid model call | CODE | **Round 26.** It needs no word, and without it the B2 run cannot stay fetch-and-store as the card states |
| 2 | Step 1 hands the ticker table to the sink once per NAME | CODE | **Round 26: a per-run memo** (the CVO's remedy). My read of `bronze_put` (`store.py:216-250`): an equal-sha256 repeat is a no-op, and different bytes raise `BronzeImmutableError`. So the hazard is real only if the table is re-FETCHED per name and SEC changes it between names. The memo removes the repeat fetch and the hazard together, at the cost of one code change |
| 3 | B4's `since=None` means no dedupe | RUN | **The B4 run cell passes `since` explicitly.** It is a parameter, not a code change |
| 4 | The ticker table is fetched at most once per UTC day | RUN | **The B2 run cell's AC0 reads whether today's partition exists and reuses it**, as ruled at 11:05Z |

## 3. WHAT TO CUT

**Round 26: two code-only cells, one issuance, no pair and no word needed** (neither touches served output, S3, IAM,
or a vendor):
- **(a) `--no-analyze` in `lib/research/filings/batch.py`.**
  - With the flag, the run makes 0 calls to `analyze.analyze_source`.
  - Without it, behaviour is unchanged.
  - The criterion is proven by a stub that counts calls.
- **(b) A per-run ticker-table memo.**
  - One fetch and one sink hand-off per run, however many names the run covers.
  - Proven by counting stub fetches for a 3-name run (1, not 3).

The B-run cells stay drafted and HELD. They are cut only on Andrew's recorded word, after round 26 drains:
- B2 with `--no-analyze`.
- B4 on Keyence only, 50 credits or fewer, with `since` passed.
- B3 only after the SA session is re-harvested.

## 4. WHAT EACH SEAT OWES NEXT

| seat | owes |
|---|---|
| `2.0.0_SA_COO~Z` | round 26's issuance (cells a and b); fold items 3 and 4 into the held run-cell drafts |
| `3.0.0_SA_CVO~Z` | round 26's L8/L9 |
| `1.0.0_SA_CTO~Z` | the backfill card to Andrew (this turn), then round 26's analysis |
| Andrew | the backfill words; the headed PROD look; the Lusha profile URL |

Push state: **LOCAL on SITEZ.**

-- `1.0.0_SA_CTO~Z`
