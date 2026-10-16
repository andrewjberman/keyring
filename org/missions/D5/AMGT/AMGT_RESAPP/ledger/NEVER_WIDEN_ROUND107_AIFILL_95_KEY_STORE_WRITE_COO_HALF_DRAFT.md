# NEVER-WIDEN CO-SIGN -- COO HALF, DRAFT. AIFILL round 107: the store write of the 95 grounded AI-fill documents

**STATE: DRAFT, NOT SIGNED.** Author `2.0.0_SA_COO~R2` (dell1), 2026-10-16 ~03:0xZ, drafted at the CTO's word (msg 6435, "Meanwhile, draft that pair"). The half is signed only after the two steps before it have run and been read: the one local live run (one name) and the 95-name local re-run under the 150 USD ceiling (CTO ruling 2026-10-14 item 5), because the expected outcome below is read from their output, not predicted. Counterpart owed: `1.0.0_SA_CTO~DELL1`'s half. Models: `NEVER_WIDEN_ROUND106_FORWARD_PE_WITHHOLD_REDEPLOY_COO_HALF.md`.
Blocked now on: `ANTHROPIC_API_KEY` in this seat's launch environment (call `dell1-20261016T024933Z-eb02`, ruled YES by the CTO, closes on cross-adjudication XA-20261016T025932Z-d7e2, then `0.0.0_AB_MSTR~DELL1` provisions it).

## THE ACT (as drafted)

For each of the 95 security keys in the round-106 census (`deliverables/2.0.0_SA_COO~R1/round106/census_v5.json`): write ONE object, `s3://opal-data-harvest/amgt/harvest/gold/ai_fill/security_key=<KEY>/ai_fill.json`, through `lib.research.aifill.store.write_document` (one `put_object`, after the contract validates the document), the document being the EXACT local file the re-run produced and `revalidate` passed, not a second generation (the model is not deterministic, so a regenerating `run --to-s3 --confirm-write` would write something nobody read). The per-key sha256 of the bytes is printed before and compared after.

## MEASURED NOW (no key needed)

| fact | reading |
|---|---|
| objects under the prefix today | **95**, every one named `ai_fill.json` (`aws s3 ls --recursive`, 95 lines): the write REPLACES 95 live objects, it adds none |
| versioning | bucket `opal-data-harvest` **Enabled**; ASML_NA_Equity has 2 versions, current `Rvzofoe9.aphOdwDynb3av.3bCVJ0o0k` (2026-10-14T03:08:03Z), prior `BF4lwh3ynuFHkzitYAdHKiWGmnw2Flc7` |
| the hold | `opal-amgt-scoped-api` `AMGT_AIFILL_ROOT` = `/var/empty/aifill-hold` (live read) |
| writers of the property | in `lib/research`: ONE writer `store.write_document` (`store.py:57`), ONE call site `run.py:129`. N = 1. Writers outside `lib/research` (a scheduled task, a Lambda) are NOT censused here; the CTO half or the signing reading must census them |
| READERS of the stored documents | **TWO**, not one: (1) the scoped API `lib/research/api/scoped_amgt.py`, which the hold redirects to an empty folder; (2) the Opal gateway `infra/aws/ec2/opal-gateway/app/harvest_research.py` lines 47 and 259-268, a direct S3 read that the hold does NOT touch. Measured live: `harvest_get_research` for ASML_NA_Equity returns the held 2026-10-14 blocks today (row `AMGT_RESAPP-D1-S40`) |

## BLAST RADIUS

The act may touch exactly 95 keys, each a literal key from the census, nothing else: no other prefix, no delete, no Lambda, no environment value, no role. A new object version is created per key; the gateway reader (2) sees each new version at once, and the scoped API reader (1) sees none while the hold stands. The act does NOT lift the hold and is not the restore.
**Rollback per key:** restore the prior VersionId read BEFORE the write (a `list-object-versions` capture of all 95 keys is part of the act's pre-record) by `copy-object` of that prior version onto the key (it becomes the newest version; the new one stays in the history), the read-back comparing the object's sha256 to the pre-record. Rollback needs no code and no Lambda change.

## EXPECTED OUTCOME -- both branches (to be filled from the two local runs before signing)

- **Branch 1:** all 95 documents `VALID` under the contract with `GROUNDING_REQUIRED` true, `revalidate` over the local files reads `checked 95, passed 95` (or the passes and the named refusals the CTO accepts), spend at or under 150 USD; each key then reads, after the write, the new sha256 with the prior version retained and the gateway tool returning the new `generated_at`.
- **Branch 2:** any key invalid, any key read back with another sha256, spend over the ceiling, or any change in the hold: stop, roll the written keys back by the method above in the same hour, report.
- **To be decided by the CTO half before signing (D1-S40):** whether the gateway reader (2) stays open to the held blocks. If the hold is to cover it, that is a separate act (not this half's), and this write waits on it.

## NOT COVERED

Any key outside the 95; any delete; the lifting of the AI-fill hold and the restore of the blocks to the page (the CTO's word after the CVO's five-new-name read is MET); any change to `opal-amgt-scoped-api`, the gateway, a role or a schedule; any Bloomberg use; the `gr-7` portal branch.

**Signature (COO):** NOT SIGNED. To be signed by `2.0.0_SA_COO~R2` after the two local steps are read, in a commit that names their outputs.
