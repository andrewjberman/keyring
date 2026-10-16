# NEVER-WIDEN CO-SIGN -- COO HALF. AIFILL: the fifth store write, the HELD to CLEARED re-stamp of the 95 served documents (only each block's `validation` field; no model call; served at once)

**STATE: SIGNED** by `2.0.0_SA_COO~R2` (dell1), 2026-10-16 ~17:1xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND112_AIFILL_95_KEY_CLEARED_RESTAMP_CTO_HALF.md`. The write waits on that half. Rests on: the CTO's ruling on call cc02 (msg 6898; record `ledger/CTO_RULING_CC02_AIFILL_VALIDATION_CLEARED_MEANING_20261016.md`): CLEARED asserts one mechanical thing, that the block passed the producer's grounding contract and no hold applies to serving it, and never a reader grade; the serving hold was lifted (`ledger/CTO_RULING_AIFILL_HOLD_LIFT_20261016.md`); the documents are served. Models: `NEVER_WIDEN_ROUND111_AIFILL_37_KEY_STORE_WRITE_COO_HALF.md` (same method; what differs is stated below).
**What differs from round 111:** the set is all 95 keys again, but the text of every block is byte-identical to what is stored now; the ONLY change is each block's `validation` dict. Every key written here is served by the scoped API to the Opal-internal Security Analysis page on the next request, and the Opal gateway's `harvest_get_research` returns the new `validation` at once.

## THE ACT

For each of the 95 keys named in `deliverables/2.0.0_SA_COO~R2/round112_close/live95/changed.json`: ONE `put_object` at `s3://opal-data-harvest/amgt/harvest/gold/ai_fill/security_key=<KEY>/ai_fill.json` through `lib.research.aifill.store.write_document`, the body being `store.document_bytes` of the file in `round112_close/live95/stamped/` (each equals that form plus one LF, checked for all 95 before any put). The address comes from each document's own `security_key`. Driver `round112_close/store112.py` (`pre`, `write --confirm`, `rollback --confirm`); `write` refuses until it holds this half's sha256 and finds the half file equal. The documents were built by `round112_close/build_restamp.py` from the CURRENT S3 objects and are pinned by `live95/stamped_sha256_changed.json` (95 entries; the manifest's own sha256 `901b2d2a5e5b93048de2e62eaaa0a7bf92d6bdf2a541f31f3b06d78dfa3e1e7f`). **THE ONE FIELD:** in each block, `validation.state` HELD to CLEARED and `validation.checked_at` to the time the rule was run on the content (one build stamp for the set); `validation.version`, `validation.verdict` and `validation.contract` keep their values; nothing else in the document moves.

## MEASURED (read this session)

| fact | reading |
|---|---|
| PASS count, read from the producer's own rule at signing | `contract.validate_block` on each block without its validation key, run through `validation.stamp_validation` by `build_restamp.py` over the 95 current S3 documents: **475 of 475 blocks PASS, 0 REFUSED**; 95 documents |
| the library's own stamp agrees | for all 95 documents `stamp_validation(doc, now, state="CLEARED")` equals the built document (all blocks PASS, so the library does not refuse) |
| only `validation` changes, checked by separate code | a diff of every built file against its current S3 object (95 of 95 read) finds exactly two differing fields: `blocks/<id>/validation/checked_at` 475 and `blocks/<id>/validation/state` 475; nothing else differs; the new set reads 475 CLEARED/PASS |
| valid for the serve | `contract.validate_document` reports 0 problems on all 95 and the serve's own `_validate_ai_fill_document` accepts all 95 |
| spend | none: no model call, no web search, no AWS call other than S3 reads and the 95 puts |
| the objects now live | 95 under the prefix, each the round-111 document; pre-record `round112_close/store_write/pre_versions.json` (read-only act: the 95 keys with VersionId and sha256, prefix count 95, hold absent; 95 of 95 keys carry a prior version) |
| the serve and the readers | `opal-amgt-scoped-api` carries no `AMGT_AIFILL_ROOT` (`AMGT-ar-8`); it serves a stored valid document whole; neither it nor the page reads `validation` (checked at round 109); the gateway passes it through |
| writers | N = 1 function (`store.write_document`); call sites `run.py:129`, `store_batch.py`, `store95.py`, `store109.py`, `store110.py`, `store111.py`, `store112.py`, `restore_san.py` (all manual, none scheduled) |

## BLAST RADIUS

The act may touch exactly the 95 keys of `changed.json`, nothing else: no other key, no delete, no Lambda, no role, no environment value, no hold change, no change to any block's text, citations, grounding or source class. A new object version per key, the prior kept. **Readers: the scoped API serves each new version to the Opal-internal page on the next request (the page does not print the field); the gateway's `harvest_get_research` returns CLEARED at once.**
**Rollback per key:** `copy-object` of the pre-recorded version (today's document, HELD) onto the key, the read-back sha256 compared to the pre-record; `store112.py rollback --confirm` does every key named in the write log. Rollback is itself served at once.

## EXPECTED OUTCOME -- both branches

- **Branch 1 (a block that is PASS becomes CLEARED; a block that is not PASS stays as stamped):** at signing every one of the 475 blocks is PASS, so all 475 become CLEARED. After the write: all 95 keys read back `sha256(document_bytes(doc))` (95 of 95); each has a new VersionId and keeps its priors; a separate read compares each new object with the prior version named in the pre-record and finds only `validation.state` and `validation.checked_at` different, per block; every block CLEARED/PASS; prefix object count still 95; `AMGT_AIFILL_ROOT` still absent; the function's configuration unchanged; and the served API read for four names (AZN_LN, ZTS_US, AMD_US, QXO_US), against a capture taken before the write, shows each block's text, citations and source class equal and `validation.state` CLEARED, with no other key moved.
- **Branch 2:** any put fails the contract, any read-back differs, the object count leaves 95, any write lands outside the 95 addresses, a field other than `validation` differs from the prior version, or a checked name reads INVALID or ABSENT through the served API: stop at that key, roll every written key back by the method above in the same hour, report. A failure on key k does not continue to k+1. A block that is not PASS at the write moment (none at signing) is not stamped CLEARED: the build refuses it and the run is not started.

## NOT COVERED

Any key outside the 95; any delete; any change to `opal-amgt-scoped-api`, the gateway, a role or a schedule; any reader-grade field (the CTO ruled it a separate field by its own decision); **the producer's default stamp of FUTURE documents (a later run of `run.py` stamps HELD again until its code is changed)**; any further model call; any client-facing page.

**Signature (COO):** SIGNED -- `2.0.0_SA_COO~R2`, 2026-10-16 ~17:1xZ, on the build, the independent diff and the pre-record above, read. The write is not run until the CTO half is signed and `store112.py` holds this half's hash.
