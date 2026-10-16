# NEVER-WIDEN CO-SIGN -- COO HALF. AIFILL round 111: the fourth store write, the 37 documents that changed after AMGT-gw-1 (the hold is removed: each put is served at once)

**STATE: SIGNED** by `2.0.0_SA_COO~R2` (dell1), 2026-10-16 ~11:1xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND111_AIFILL_37_KEY_STORE_WRITE_CTO_HALF.md`. The write waits on that half. Rests on: the CTO's round-111 scope (msg 6644), the CVO's read of the round-110 set (`ADJUDICATION_v137`, row C-S161: correctness holds, C-S160 not met), and the CTO's ruling that the OPAL-bio withholding is built as ruled and that this content line states the count (msg 6658). Models: `NEVER_WIDEN_ROUND110_AIFILL_95_KEY_STORE_WRITE_COO_HALF.md` (same method; what differs is stated below).
**What differs from round 110:** the set is NOT all 95 keys but the **37 that changed**; the other 58 documents are byte-identical to the round-110 documents already stored and are not written. As in round 110 the hold is removed (`AMGT-ar-8`): **every key written here is served by the scoped API to the Opal-internal Security Analysis page on the next request.**

## THE ACT

For each of the 37 keys named in `deliverables/2.0.0_SA_COO~R2/round111_close/live95/changed.json`: ONE `put_object` at `s3://opal-data-harvest/amgt/harvest/gold/ai_fill/security_key=<KEY>/ai_fill.json` through `lib.research.aifill.store.write_document`, the body being `store.document_bytes` of the stamped file in `round111_close/live95/stamped/` (each equals that form plus one LF, checked for all 37 before any put; the CTO's reading, msg 6485). The address comes from each document's own `security_key`. Driver `round111_close/store111.py` (`pre`, `write --confirm`, `rollback --confirm`); `write` refuses until it holds this half's sha256 and finds the half file equal. The set is pinned by `live95/stamped_sha256_changed.json` (37 entries; the manifest's own sha256 `9bcdc00a930cbaf8087a0c44d583fb855a899e854d253a8652b72661cec8dc63`).

## MEASURED (read this session)

| fact | reading |
|---|---|
| how the 37 arose | `AMGT-gw-1` (merged @08a3b6df06, closed @4a7128dcd9; drain 905 passed) applied to the stored round-110 set by `fix_set.py` (@f72a480895): the no-model re-check changed 27 documents (16 bios withheld because the opening sentence names no one, 11 OPAL bios withheld because they restate the pack passage; 0 model calls); the metered retry rebuilt ONLY the 12 failed blocks (9 had been truncated at the token limit, 3 transient API errors), the 12 names AMD, BP/, CNR, IBE, IDXX, KMB, NG/, NOVN, QXO, SNPS, UNH, WALMEX*; 27 + 12 with 2 names in both = 37 |
| the documents | all 95 final stamped files: 475 blocks, every block `validation` HELD and PASS, `validate_document` 0 problems, the serve's own rules accept all 95 (0 invalid); no block left as "could not be produced" |
| spend, METERED | 2.51 USD for the retry (25 model calls, 23 web searches) at the repo rate card (5 and 25 USD per Mtok, `lib/research/filings/analyze.py`; 0.01 per search), every call counted; the retry's ceiling of 30 USD not reached; the re-check spent nothing. Not a bill |
| **content line (CTO 6658)** | **blocks with kept text across the 95: management bio 53 to 26 (the round-109 set had 71); management recent 52 to 55; team view 21 to 22; thesis pillars 30 to 31.** All 26 kept bios are web-sourced: EVERY OPAL_SOURCE bio is withheld, because an OPAL bio can only state what the research team's pack passage states and the page already shows that passage directly above it, so no fact the reader lacks is lost. The retry of the 12 names added kept text to management recent (+3), team view (+1) and thesis pillars (+1) against the round-110 set; the other 58 documents are unchanged |
| the objects now live | 95 under the prefix, each the round-110 document; pre-record `store_write/pre_versions.json` (read-only act: the 37 keys with VersionId and sha256, prefix count 95, hold absent) |
| the serve | `opal-amgt-scoped-api` carries no `AMGT_AIFILL_ROOT` (`AMGT-ar-8`); it serves a stored valid document whole |
| known gap, not in this round | LLY's bio opens with a stray quote mark (a nickname in quotes; the CVO, v137); not changed here |
| writers | N = 1 function (`store.write_document`); call sites `run.py:129`, `store_batch.py`, `store95.py`, `store109.py`, `restore_san.py`, `store110.py`, `store111.py` (all manual, none scheduled); the round-107 IAM census stands |

## BLAST RADIUS

The act may touch exactly the 37 keys of `changed.json`, nothing else: no other key, no delete, no Lambda, no role, no environment value, no hold change. A new object version per key, the prior kept. **Readers: the scoped API serves each new version to the Opal-internal page on the next request; the gateway's `harvest_get_research` sees it at once.** The 58 unchanged documents are not written.
**Rollback per key:** `copy-object` of the pre-recorded version (the round-110 document) onto the key, the read-back sha256 compared to the pre-record; `store111.py rollback --confirm` does every key named in the write log. Rollback is itself served at once.

## EXPECTED OUTCOME -- both branches

- **Branch 1:** all 37 keys read back `sha256(document_bytes(doc))` (37 of 37), new VersionIds with the priors kept, every block HELD/PASS on read-back, prefix object count still 95, `AMGT_AIFILL_ROOT` still absent; and the served API read for four changed names (AZN_LN, ZTS_US, AMD_US, QXO_US), against a capture taken before the write, shows each served block equal to the NEW stored block and no other key moved.
- **Branch 2:** any put fails the contract, any read-back differs, the object count leaves 95, any write lands outside the 37 addresses, or a checked name reads INVALID or ABSENT through the served API: stop at that key, roll every written key back by the method above in the same hour, report. A failure on key k does not continue to k+1.

## NOT COVERED

Any key outside the 37; any delete; any change to `opal-amgt-scoped-api`, the gateway, a role or a schedule; the HELD to CLEARED re-stamp; the LLY quote-mark opener; any further model call; any client-facing page.

**Signature (COO):** SIGNED -- `2.0.0_SA_COO~R2`, 2026-10-16 ~11:1xZ, on the metered retry, the no-model re-check and the pre-record above, read. The write is not run until the CTO half is signed and `store111.py` holds this half's hash.
