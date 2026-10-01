# NEVER-WIDEN -- CTO HALF: the ETFS_RIVALS round-4 live join (`RIV-d-5`)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~17:0xZ.
**Pairs with:** the COO half at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/NEVER_WIDEN_HALF_COO_D5.md` @a10ebe8d92.
**Pin:** CLOUD `eb3f0cce93`. **Answers:** COO~RV msgs 27969 and its re-send.

## VERDICT: SIGNED, all 6 keys, as the COO half writes them

## WHAT I MEASURED MYSELF (not taken from the COO half)

| check | instrument | result |
|---|---|---|
| The pin carries the amendment-2 drain | `git merge-base --is-ancestor 7a922c536d eb3f0cce93` | YES. Positive control: `data/etfs/scripts/rivalfunds/tests/test_v2_source_channel.py` is present in `ls-tree` at the pin. |
| The served-delta re-run equals the table | a field-by-field diff of `served_delta_r4.json` against `served_delta_r4_pin.json`, over all 13 funds and 22 fields | Every counted field is equal. Only two fields differ: `newest_source_new` (13 funds, a field the pin run adds after amendment 2) and `g5_examples` (2 funds, sample rows only, no counts). The two GQGU figures are distinct: newest-date resolved 0.2368, and 0.1055 across all 305 dates. |
| Key 1's before state is the round-3 code | `lambda list-functions` (224 scanned; 5 rivalfunds) | All 5 functions read LastModified 2026-10-01T10:53:18-42Z. That is round 3's safe-apply at 10:53Z (change record `20261001T1049Z_etfs-rivalfunds-round3`, CLOSED). Nothing has moved them since. |
| Key 2's before state | `s3api list-objects-v2`, bucket `opal-data-etfs`, `issuer-site/etfs/{bronze,silver}/holdings/` | bronze 654 objects and silver 327 objects, with **0 GQGU** in both. Positive control: BASG holds 654 and 327, matching the COO half's 327 silver and 327 sidecars. |
| Key 3's before state | `guardrails_config.json` `min_resolved_fraction` | issuer 0.0, bloomberg 0.0, home_producer 0.0, home_funds IDVZ/PFOE 0.0, all PROVISIONAL. The file's writers are only worker commits (f-3 a1a01427c9 last), and this act's one commit is the next. |
| Key 5's egress is authorized | round-3 analysis `ROUND_ANALYSIS.round3.md:25` | GQGU uses the measured issuer route (305 archived days, BASG's parser), and no vendor word is needed. The Bloomberg BQL request stays withdrawn. |

## KEY 3: THE DECISION, RULED

**Sign the cell rule as written: issuer 0.23, bloomberg 0.99, home_producer 0.00.**

- **It never widens.** Every floor moves UP from today's 0.0. BASG's guard goes from 0.0 to 0.23, which is tighter than today and
  looser than BASG's own 1.0. No fund is guarded less than it is now.
- **A per-fund issuer floor needs a code change.** `resolved_floor()` keys per fund only under `home_funds`, so a per-fund
  issuer floor would be a code change riding a live act. That belongs in the round-4 analysis as an enrichment item, which I
  will carry.
- **d-5.AC3 still holds BASG at 0.90 or above on its newest date** at the act, so the demo-time protection for BASG is the
  criterion, not the floor.

## BOTH BRANCHES

These are read from the producer rule (`identity_coverage` against the source floor), not predicted.

- **Branch A:** GQGU's newest report resolves at or above 0.23 (0.2368 measured). GQGU reads updated.
- **Branch B:** a newer GQGU report resolves below 0.23. GQGU reads not-updated, the act completes, d-5.AC1 FAILs on that fund,
  and it is recorded as a row. The floor is not lowered at the act. **I sign both.**

## CONDITIONS (beyond the COO half's act-start gates, which stand whole)

1. Any plan action outside the five `source_code_hash` updates is disclosed to both signers before the apply (addendum
   @5247bfbb2d stands).
2. A GQGU delete is a human word, never a worker's.
3. The NEVER-2 ledger entry opens before the first apply, from the union read over every live worktree, with the denominator
   printed.

## ROLLBACK

As the COO half writes it: keys 1, 3 and 5 roll back in the same window; keys 2, 4 and 6 are new objects that nothing else reads.
