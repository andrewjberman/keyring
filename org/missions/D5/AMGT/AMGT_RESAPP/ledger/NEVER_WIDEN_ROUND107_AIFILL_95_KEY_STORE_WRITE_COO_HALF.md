# NEVER-WIDEN CO-SIGN -- COO HALF. AIFILL round 108: the store write of the 95 grounded, validation-stamped AI-fill documents

**STATE: SIGNED** by `2.0.0_SA_COO~R2` (dell1), 2026-10-16 ~04:2xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND107_AIFILL_95_KEY_STORE_WRITE_CTO_HALF.md`. The write waits on that half; this half alone authorizes nothing. Supersedes `NEVER_WIDEN_ROUND107_AIFILL_95_KEY_STORE_WRITE_COO_HALF_DRAFT.md` (same act; the draft's open lines are closed below). Models: `NEVER_WIDEN_ROUND106_FORWARD_PE_WITHHOLD_REDEPLOY_COO_HALF.md`.
**Written from** the two local runs, read: the one live run (`deliverables/2.0.0_SA_COO~R2/round107_aifill_close/live1/`) and the 95-name re-run (`.../round107_aifill_close/live95/`: `raw/`, `stamped/`, `spend_ledger.jsonl`, `stamped_sha256.json`), plus surprise rows `AMGT_RESAPP-D1-S41` and `-S42`. CTO order of work: msgs 6446, 6448, 6464.

## THE ACT

For each of the 95 security keys in `deliverables/2.0.0_SA_COO~R1/round106/census_v5.json`: write ONE object, `s3://opal-data-harvest/amgt/harvest/gold/ai_fill/security_key=<KEY>/ai_fill.json`, through `lib.research.aifill.store.write_document` (one `put_object` after the contract validates the document), the body being the EXACT bytes of the local stamped file in `live95/stamped/` (no second generation; the model is not deterministic). **The address comes from the document's own `security_key` field** via `store.address_for`, never from the local file name (three local names differ from the key: `BP-SLASH-_LN_Equity.json`, `NG-SLASH-_LN_Equity.json`, `WALMEX-STAR-_MM_Equity.json`; the live store already holds the matching keys `BP-SLASH-_LN_Equity`, `NG-SLASH-_LN_Equity` and the literal-star `WALMEX*_MM_Equity`). The per-key sha256 of the bytes is printed before the write and compared after to the read-back object. The set is pinned by `live95/stamped_sha256.json` (95 entries; the manifest file's own sha256 is `3643ac0c5a94d188bfbc4fabbbdd1146cc16b396e640f68fa6b6de725ab249c0`).

## MEASURED (all read this session)

| fact | reading |
|---|---|
| the documents | 95 stamped files, 475 blocks, every block `validation.state` HELD and `verdict` PASS; `contract.validate_document` over each stamped file: 0 problems (the contract accepts the block key `validation`, `AMGT-gt-1` @7e99d74fe0) |
| content | 803 judged sentences: 478 SUPPORTED, 302 UNSUPPORTED, 23 CONTRADICTED; no non-SUPPORTED sentence survives in any block's text; blocks with kept text: mgmt_bio 78, mgmt_recent 69, mgmt_team_view 35, thesis_pillars 34. 22 of the 23 CONTRADICTED sentences record the shown source index and quote; 1 (1299_HK_Equity mgmt_recent) records both null (row D1-S41) |
| spend | about 124 USD ESTIMATED at assumed upper rates (15 and 75 USD per Mtok, 0.01 per search): 122.41 summed from the documents' recorded calls plus a lost first WALMEX run (about 1.4, unmeasured); ceiling 150 not reached. NOT a bill (row D1-S42) |
| live objects | 95 under the prefix, all `ai_fill.json` (`aws s3 ls --recursive`, 95 lines): the write REPLACES 95 live objects and adds none |
| versioning | bucket `opal-data-harvest` Enabled |
| the hold | `opal-amgt-scoped-api` `AMGT_AIFILL_ROOT` = `/var/empty/aifill-hold` (live read 2026-10-16 ~03:0xZ; re-read at the act) |

## WRITERS OF THE PROPERTY (the count the sign-off needs)

Property: the object `amgt/harvest/gold/ai_fill/security_key=<K>/ai_fill.json`. Census: `put_object` / `upload_file` / `write_document` / `copy_object` over `lib/research` (Grep, non-test files) and `gold/ai_fill|AI_FILL_PREFIX|P_AI_FILL` over `infra data integrations lib .tools portal/src` (9 files). **N = 1 writer function**, `lib/research/aifill/store.py:66` (`write_document`), with **2 call sites**: `lib/research/aifill/run.py:129` (`run --to-s3 --confirm-write`) and the seat batch script `deliverables/2.0.0_SA_COO~R2/round104/store_batch.py:75` (manual, unscheduled, never run by a schedule). The other `put_object` sites in `lib/research` write other prefixes (identity, social, ledger, posture, peers, harvest, management pool, freshness). The gateway files in the 9 (`harvest_research.py`, `harvest_identity.py`) read; `scoped-amgt-api.tf` grants the scoped API read on the prefix and its one `s3:PutObject` is the freshness snapshot object only (lines 446-449). N rules read: one rule (`store.write_document` validates through the contract, then one put). NOT censused: IAM write grants on the prefix held by roles outside the files above, and any scheduled task outside the repo; the CTO half should census them.

## BLAST RADIUS

The act may touch exactly 95 keys, each a literal key from the census, nothing else: no other prefix, no delete, no Lambda, no environment value, no role, no hold change. A new object version is created per key. Readers: (1) the scoped API, which the hold redirects to an empty folder, so it sees none; (2) the Opal gateway's `harvest_get_research` (`infra/aws/ec2/opal-gateway/app/harvest_research.py` lines 47, 259-268), an INTERNAL reader RULED accepted by the CTO (msg 6444, D1-S40), which sees each new version at once and now sees blocks that each carry `validation` {state HELD, verdict PASS} per the CTO's condition (msg 6446, state in each block). The act does NOT lift the hold, is not the restore of the blocks to the page, and does not wait for or replace the CVO's five-name read.
**Pre-record (before the first write):** `list-object-versions` of all 95 keys, saved to `round107_aifill_close/store_write/pre_versions.json`, the prior VersionId and sha256 of each current object recorded.
**Rollback per key:** `copy-object` of the prior VersionId onto the key (it becomes the newest version; the new one stays in history), the read-back sha256 compared to the pre-record. No code or Lambda change.

## EXPECTED OUTCOME -- both branches

- **Branch 1:** each of the 95 keys reads back the sha256 of its stamped local file (95 of 95 equal), the prior version retained (95 prior VersionIds in the pre-record), 475 blocks each reading `validation` HELD/PASS through `store.read_document`, and the gateway tool returns the new `generated_at` for a sampled key; object count under the prefix still 95; the hold value unchanged. Under this branch the documents are internally valid and held; whether their content is right is the CVO's five-name read, not this act.
- **Branch 2:** any key fails the contract, any read-back sha256 differs from its stamped file, the object count leaves 95, the hold value changes, or any write lands outside the 95 addresses: stop, roll every written key back by the method above in the same hour, report to the CTO. A failure on key k does not continue to k+1.

## NOT COVERED

Any key outside the 95; any delete; the lifting of the AI-fill hold and the return of the blocks to the page (the CTO's word after the CVO's five-new-name read, drawn by sha256 over the date, is MET); any change to `opal-amgt-scoped-api`, the gateway, a role, a schedule; any Bloomberg use; the `gr-7` portal branch; any further model call.

**Signature (COO):** SIGNED -- `2.0.0_SA_COO~R2`, 2026-10-16 ~04:2xZ, on the two local runs above, read. The write is not run until the CTO half is signed.
