# Deploy-completion ledger: ADVI_49F a07 carrier-3 comment correction (canon-json-v1 definition)

**Status:** CLOSED
**Opened:** 2026-09-01T13:20:36Z (the push-gate deploy, object write) | **Closed:** 2026-09-01T13:2xZ (running-artifact read)
**Operator:** `0.4.0_DS_ClientPlatform~N` | **Deploy executed by:** the pre-push deploy gate on the integration window that took `c85701ebca`

**Authority:** `1.0.0_SA_CTO` ruling **91555** (2026-09-01 13:1xZ), which RULED (B) on the
`canon-json-v1` composition and **ORDERED** the carrier-3 correction to the DS lane: *"DS lane:
carrier 3, a comment correction beside a line that is already correct. This ruling is the authority
for it."* Graded `3.0.0_SA_CVO` 91565. Cell `C02-g-13`, face `ADVI_49F.c02-VINTAGEDIGEST`.

## Scope -- COMMENTS ONLY
Commit `c85701ebca`. One file: `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py`,
the in-code block at `:146-162` which asserted *"THE VINTAGE IS A PURE FUNCTION OF THE SUBSTRATE"*,
enumerated rules covering only the JSON canon, and **cited ruling 87535 as its authority** -- a
ruling propagated into source as a comment. It now names both digest inputs, cites 87535 **as
amended by 91555**, states the full composition so the block is re-derivable on its own, and carries
the lib measurement.

⛔ **NO BEHAVIOURAL CHANGE, VERIFIED BEFORE COMMIT RATHER THAN ASSERTED AFTER.** The diff was parsed
programmatically, not eyeballed: **24 lines added, 2 removed, ZERO non-comment lines changed.**
`commit-gate` clean 1 of 1.

## ⚠ THE SERVED ETag CHANGED, AND THAT IS EXPECTED -- do not read it as drift
| | value |
|---|---|
| served ETag BEFORE (recorded in V-4 and in the `20260830T1442Z` ledger) | `e0bde0a5394b7ab83d1797431327c33e`, 32,419 B |
| served ETag NOW | `9202d701c552d4fb38a40f975f0eae9e`, 34,289 B, LastModified `2026-09-01T13:20:36Z` |
| index blob at `c85701ebca` | `9202d701c552d4fb38a40f975f0eae9e` -- **MATCH** |

**A verifier comparing the live object against the ETag recorded in V-4's evidence will now see a
mismatch.** That is this cell's *third* instance of the same carrier class in two days (the first:
the `14:42:52Z -> 17:53:25Z` timestamp move on byte-identical content). **Identity is by CONTENT
against the index blob AT THE CURRENT PIN (22a) -- never against a hash or a timestamp recorded for
an earlier one.** The size grew by exactly the added comment lines.

## Why this CANNOT move `_classifier_vintage`
The digest's two inputs are the loaded DynamoDB `ticker_map` and `CLASSIFIER_LIB.read_bytes()`.
`CLASSIFIER_LIB` resolves to `data/black_diamond/scripts/gold/lib/etf_classifier.py` -- **a different
file, unmodified in this commit** (`git status` clean on that path). **a07's own bytes are not an
input to its own digest.** So the next fire must carry the same
`48ec291d405a6b1b0e72b5ed4b311da26bc489296e7d09c536c4fd9b4931ef21` that V-4's two fires carried.
**That is a falsifiable prediction and it is the read for the next 12:45Z fire.**

## Custody chain (unchanged, verified in the 14:00Z and 14:42Z ledgers at source)
Scheduler `advi-49f-gold-floor` `cron(45 12 * * ? *)` UTC -> Lambda `advi-49f-gold-dispatch` -> SSM
`advi-49f-chain-dispatch` v3 -> `aws s3 sync s3://opal-data-49financial/_code/ ... --delete` ->
`chain_49f_entrypoint.py --production`. **The 2026-09-02 12:45Z fire runs `9202d701`.** Note the
second live trigger: the `advi-49f-silver-complete-accelerator` S3 event can fire the chain earlier,
so `9202d701` may run before that scheduled slot.

## Rollback
`git revert c85701ebca`; the reverted bytes reach `_code/` by the same push-gate path. **No data is
moved or deleted and no served output is implicated** -- this is a comment. **Trigger:** the next
fire carrying a `_classifier_vintage` other than `48ec291d...4931ef21` with the DynamoDB substrate
and `CLASSIFIER_LIB` both unchanged (which would falsify the prediction above and mean the change
was not comment-only after all), or a07 failing to import.
