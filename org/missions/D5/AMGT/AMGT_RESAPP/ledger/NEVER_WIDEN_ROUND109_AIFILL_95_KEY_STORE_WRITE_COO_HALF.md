# NEVER-WIDEN CO-SIGN -- COO HALF. AIFILL round 109: the second store write of the 95 re-made, validation-stamped AI-fill documents

**STATE: SIGNED** by `2.0.0_SA_COO~R2` (dell1), 2026-10-16 ~08:5xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND109_AIFILL_95_KEY_STORE_WRITE_CTO_HALF.md`. The write waits on that half; this half alone authorizes nothing. CTO ruling: `CTO_RULING_AIFILL_R109_RERUN_BUDGET_20261016.md` (msgs 6580, 6599): re-run all 95 after `gu-1`, metered, ceiling 150 USD; "the store write needs its own never-widen pair"; the hold lifts only on a fresh CVO five-new-name read that reads MET. Model: `NEVER_WIDEN_ROUND107_AIFILL_95_KEY_STORE_WRITE_COO_HALF.md` (same act, same keys, same method; what differs is stated below).
**Why a second write:** the CVO's read of the first stored set was NOT MET (`ADJUDICATION_v135.md`, row `AMGT_RESAPP-D1-C-S158`); `AMGT-gu-1` (merged @0fd6ae013a, closed @b1c5fb47ae) changes what a block may keep; the 95 documents were re-made with it. The CVO reads documents from S3, so the fresh read needs this write first.

## THE ACT

For each of the 95 security keys of `deliverables/2.0.0_SA_COO~R1/round106/census_v5.json`: ONE `put_object` at `s3://opal-data-harvest/amgt/harvest/gold/ai_fill/security_key=<KEY>/ai_fill.json` through `lib.research.aifill.store.write_document` (it validates through the contract first), the body being `store.document_bytes(doc)` of the stamped local file in `deliverables/2.0.0_SA_COO~R2/round109_close/live95/stamped/` (each file equals that form plus one LF, checked for all 95 before any put; the CTO accepted this reading of "read-back equal" in msg 6485). The address comes from the document's own `security_key` field, never from the file name (`BP-SLASH-_LN_Equity`, `NG-SLASH-_LN_Equity` and the literal-star `WALMEX*_MM_Equity` keys already exist live). Driver: `round109_close/store109.py` (`pre`, `write --confirm`, `rollback --confirm`); its `write` refuses until it holds this half's sha256 and finds it equal. The set is pinned by `live95/stamped_sha256.json` (95 entries; the manifest's own sha256 is `06a76e26cd13374ca44b9a5faa09ec5d78f0b6031274f8220e9a53fd15f4b9f4`).

## MEASURED (read this session)

| fact | reading |
|---|---|
| the documents | 95 stamped files, 475 blocks, every block `validation` HELD and PASS; `validate_document` 0 problems; no non-SUPPORTED sentence survives in any block's text; each file passes the serve's own rules at the merged head (`gu-1` drain: aifill suite plus the api serve test, 869 passed) |
| content against the first stored set | SUPPORTED sentences 478 to 331, UNSUPPORTED 302 to 356, CONTRADICTED 23 to 16; blocks with kept text mgmt_bio 78 to 71, mgmt_recent 69 to 53, mgmt_team_view 35 to 24, thesis_pillars 34 to 34. The new documents withhold more; part of that is the new checks (the specifics check and the recency pass, which dropped 10 sentences as contradicted by another block's page), part is that the model drafts different text each run |
| spend, METERED | 63.16 USD for the 95 (659 model calls, 531 web searches) at the repo rate card, 5 and 25 USD per Mtok (`lib/research/filings/analyze.py`) and 0.01 per search; ceiling 150 not reached. The blocks themselves record 37.11, so the first run's recorded figure missed a factor of 1.7 (CTO 6599). Not a bill |
| the objects now live | 95 under the prefix, all `ai_fill.json`, each carrying the round-107 document (version count after the first write: every key has a prior version); the pre-record `store_write/pre_versions.json` (read-only, 08:5xZ): 95 keys, prefix count 95, hold `/var/empty/aifill-hold` |
| the hold | `opal-amgt-scoped-api` `AMGT_AIFILL_ROOT` = `/var/empty/aifill-hold` (live read at the pre-record; re-read at the act) |
| writers of the property | N = 1 function (`store.py:66` `write_document`) with call sites `run.py:129`, `round104/store_batch.py:75`, `round107_aifill_close/store95.py` and `round109_close/store109.py` (all manual, none scheduled). The CTO half of round 107 censused live IAM writers (0 of 318 roles; 5 users through admin groups; no bucket policy); this half adds none |

## BLAST RADIUS

The act may touch exactly 95 keys, each a literal key of the census, nothing else: no other prefix, no delete, no Lambda, no environment value, no role, no hold change. A new object version is created per key. Readers: the scoped API (the hold redirects it to an empty folder, so it sees none); the Opal gateway's `harvest_get_research`, an INTERNAL reader ruled accepted (msg 6444), which sees each new version at once, every block carrying `validation` HELD. The act does NOT lift the hold, does not return the blocks to the page, and does not replace the CVO's read.
**Pre-record:** `store_write/pre_versions.json` (exists, read-only act, 95 keys with prior VersionId and sha256).
**Rollback per key:** `copy-object` of the pre-recorded version (the round-107 document) onto the key (it becomes the newest version; the round-109 one stays in history), the read-back sha256 compared to the pre-record; `store109.py rollback --confirm` does all keys named in the write log.

## EXPECTED OUTCOME -- both branches

- **Branch 1:** all 95 keys read back `sha256(document_bytes(doc))` (95 of 95), a new VersionId each with the priors kept, every block `validation` HELD/PASS on read-back, prefix object count 95, hold value unchanged, and the gateway returns the new `generated_at` for a sampled key.
- **Branch 2:** any put fails the contract, any read-back differs, the object count leaves 95, the hold value changes, or any write lands outside the 95 addresses: stop at that key, roll every written key back by the method above in the same hour, report to the CTO.

## NOT COVERED

Any key outside the 95; any delete; the lifting of the AI-fill hold and the return of the blocks to the page (the CTO's word after a fresh CVO read reads MET; the restore half stays a void draft until then); the HELD to CLEARED re-stamp; any change to `opal-amgt-scoped-api`, the gateway, a role or a schedule; any further model call; any Bloomberg use.

**Signature (COO):** SIGNED -- `2.0.0_SA_COO~R2`, 2026-10-16 ~08:5xZ, on the re-run and the pre-record above, read. The write is not run until the CTO half is signed and `store109.py` holds this half's hash.
