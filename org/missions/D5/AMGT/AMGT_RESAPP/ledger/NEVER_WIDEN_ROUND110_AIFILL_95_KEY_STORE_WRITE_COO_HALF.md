# NEVER-WIDEN CO-SIGN -- COO HALF. AIFILL round 110: the third store write, the 95 documents re-made after AMGT-gv-1, WITH THE HOLD ALREADY REMOVED

**STATE: SIGNED** by `2.0.0_SA_COO~R2` (dell1), 2026-10-16 ~10:1xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND110_AIFILL_95_KEY_STORE_WRITE_CTO_HALF.md`. The write waits on that half. Rests on: the CTO's rulings `CTO_RULING_AIFILL_HOLD_LIFT_20261016.md` and its addendum (msgs 6634, 6635: re-run all 95 under the meter, ceiling 150 USD; "store under a new pair"; "the page keeps the round-109 set until that write lands"). Models: `NEVER_WIDEN_ROUND109_AIFILL_95_KEY_STORE_WRITE_COO_HALF.md` (same act, keys and method).
**What differs from the round-109 pair, and it is the point of this half:** that write ran with the hold IN PLACE, so no reader but the gateway saw it. **The hold is now removed (`AMGT-ar-8`, @77cac6580b): every key written here is served by the scoped API to the Opal-internal Security Analysis page on the NEXT request.** A write that lands is a page change for 95 names, not a record. `AMGT-gv-1` (merged @d6e03c68b7, closed @3eb66908af) is what the re-made documents differ by: diacritic names are no longer withheld, a sentence that only describes its source is not kept, an OPAL bio that only restates the pack is withheld, and a bio opening on an unnamed pronoun is withheld.

## THE ACT

For each of the 95 keys of `deliverables/2.0.0_SA_COO~R1/round106/census_v5.json`: ONE `put_object` at `s3://opal-data-harvest/amgt/harvest/gold/ai_fill/security_key=<KEY>/ai_fill.json` through `lib.research.aifill.store.write_document`, the body being `store.document_bytes` of the stamped file in `deliverables/2.0.0_SA_COO~R2/round110_close/live95/stamped/` (each file equals that form plus one LF, checked for all 95 before any put; the CTO's reading, msg 6485). The address comes from each document's own `security_key` field (`BP-SLASH-_LN_Equity`, `NG-SLASH-_LN_Equity` and the literal-star `WALMEX*_MM_Equity` keys already exist live). Driver `round110_close/store110.py` (`pre`, `write --confirm`, `rollback --confirm`); `write` refuses until it holds this half's sha256 and finds the half file equal. The set is pinned by `live95/stamped_sha256.json` (95 entries; the manifest's own sha256 `0dd404aff567e9c8263c964ff53ccb67088af53b622ac881e8b0ce30bf835e7f`).

## MEASURED (read this session)

| fact | reading |
|---|---|
| the documents | 95 stamped files, 475 blocks, every block `validation` HELD and PASS; `validate_document` 0 problems; the serve's OWN rules (`scoped_amgt._validate_ai_fill_document`) accept all 95 (0 invalid); no non-SUPPORTED sentence survives in any block's text |
| spend, METERED | 61.57 USD for the 95 (636 model calls, 524 web searches) at the repo rate card (5 and 25 USD per Mtok, `lib/research/filings/analyze.py`; 0.01 per search), every call counted; ceiling 150 not reached; the blocks themselves record 31.68. Not a bill |
| content against the round-109 set | blocks with kept text: mgmt_bio 71 to 53, mgmt_recent 53 to 52, mgmt_team_view 24 to 21, thesis_pillars 34 to 30; sentences SUPPORTED 331 to 300, UNSUPPORTED 356 to 284, CONTRADICTED 16 to 11. Why bios fell: 23 bios withheld by the new unnamed-pronoun rule ("The text opens without naming the person it describes, so it was withheld."), 1 by the restatement rule, 6 sentences in 5 names dropped by the recency pass. The set is more conservative than round 109 and shows less |
| what the new rules did on real data | SAN FP's bio now opens "Belen Garijo was appointed chief executive of Sanofi ..." (the diacritic false drop is gone); SAN FP `mgmt_recent` reads NONE in the new draw too (the CTO's ruling that it does not ship holds without the one-key patch). **A known gap, not fixed here:** the pronoun rule tests only the FIRST word, so a bio opening "Earlier she was ..." or "Before joining X, she ..." (5 of the 53 kept bios open on "Before", ZTS on "Earlier") still ships |
| blocks lost to errors | 12 blocks "could not be produced" (round 109: 9): 9 model answers truncated at the token limit, 3 transient API errors (`WinError`); 12 names (AMD, BP/, CNR, IBE, IDXX, KMB, NG/, NOVN, QXO, SNPS, UNH, WALMEX*). Not retried; the truncation is a producer finding for the CTO |
| the objects now live | 95 under the prefix, each the round-109 document (SAN FP the one-key patch, `mgmt_recent` NONE); pre-record `store_write/pre_versions.json` (read-only act, 95 keys with VersionId and sha256, prefix count 95, hold absent) |
| the serve | `opal-amgt-scoped-api` carries no `AMGT_AIFILL_ROOT` (`AMGT-ar-8`); it reads the stored documents and serves a valid one whole |
| writers | N = 1 function (`store.write_document`); call sites `run.py:129`, `round104/store_batch.py:75`, `store95.py`, `store109.py`, `restore_san.py`, `store110.py` (all manual, none scheduled); the round-107 CTO half censused live IAM writers (0 of 318 roles), no change |

## BLAST RADIUS

The act may touch exactly 95 keys, each a literal key of the census, nothing else: no other prefix, no delete, no Lambda, no role, no environment value, no hold change. A new object version is created per key, the prior kept. **Readers: the scoped API serves each new version to the page on the next request (the hold is gone); the gateway's `harvest_get_research` sees it at once.** Surface: the Opal-internal Security Analysis page (staff-only); no client-facing page reads these documents.
**Rollback per key:** `copy-object` of the pre-recorded version (the round-109 document) onto the key (it becomes the newest version), the read-back sha256 compared to the pre-record; `store110.py rollback --confirm` does every key named in the write log. Rollback needs no code and no Lambda change, and it is itself served at once.

## EXPECTED OUTCOME -- both branches

- **Branch 1:** all 95 keys read back `sha256(document_bytes(doc))` (95 of 95), new VersionIds with the priors kept, every block HELD/PASS on read-back, prefix object count 95, `AMGT_AIFILL_ROOT` still absent from the function configuration; and the post-write served read, `check_restore_served.py`-style on four names, shows each served block equal to the new stored block.
- **Branch 2:** any put fails the contract, any read-back differs, the object count leaves 95, any write lands outside the 95 addresses, or any of the checked names reads INVALID or ABSENT through the served API: stop at that key, roll every written key back by the method above in the same hour, report. A failure on key k does not continue to k+1.

## NOT COVERED

Any key outside the 95; any delete; any change to `opal-amgt-scoped-api`, the gateway, a role or a schedule; the HELD to CLEARED re-stamp; the pronoun-opening gap and the truncation (round 111 if the CVO's read or the CTO calls for it); any further model call; any client-facing page.

**Signature (COO):** SIGNED -- `2.0.0_SA_COO~R2`, 2026-10-16 ~10:1xZ, on the metered re-run and the pre-record above, read. The write is not run until the CTO half is signed and `store110.py` holds this half's hash.
