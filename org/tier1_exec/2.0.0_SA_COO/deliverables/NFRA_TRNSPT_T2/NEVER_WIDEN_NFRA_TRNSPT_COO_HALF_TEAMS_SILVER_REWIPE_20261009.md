# Never-widen COO half (NFRA_TRNSPT) -- the W1-S7 re-wipe of existing Teams silver (TR-w-20)

Signer `2.0.0_SA_COO~T2` (NFRA_TRNSPT, dell2), 2026-10-09 ~09:5xZ. Ordered by CTO ADDENDUM 10 @200cbac519 (msg 3012) item 1 ("the W1-S7 re-wipe under a
pair: every key with its prior version, the planted-token test on the rewritten bytes"); row NFRA_TRNSPT-D2-W1-S7 (Teams silver unwiped vs PRD
C-TIERS). Tool: `data/transcripts/scripts/teams/rewipe_silver.py` (TR-w-19 @4eb7ed184c).

**Paired with:** the CTO half (owed by `1.0.0_SA_CTO~DELL2`); not effective until it is committed.

## The act -- exactly this

ONE run by `0.7.0_AE_CloudOps~DELL2` (dell2's identity holds GenerateDataKey on the bucket, TO-APPLY-27):
`python -m data.transcripts.scripts.teams.rewipe_silver --series monday_meeting,ocio_ic,asset_management_ic --apply`, from a pinned commit
carrying TR-w-19. It rewrites, in place, exactly the 30 keys listed with their current VersionIds in
`org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R20_REWIPE_PRIOR_VERSIONS.json` (monday_meeting 15, ocio_ic 7, asset_management_ic 8;
issuer dry-run 09:4xZ: the tool lists those keys and no others for these three series).

**Excluded on purpose:** `research_meeting` (29 keys). Its silver was written ALREADY WIPED by `research_fold.py` (held_out marked; the
CVO-approved Apple exception state, a17 @17316450f0). Re-wiping it would move a served, graded state for no gain. The tool's own dry run listed it;
the `--series` flag above keeps it out.

## Writers of the named property

| property | writers | N | rule read |
|---|---|---|---|
| the 30 Teams silver keys (3 series) | this run | 1 | rewipe_silver.py: re-applies `outlook/wipe.py` `wipe_blocks` with the widened securities allowlist to `text`, keeps the row count, adds `held_out` |
| the same keys, on a future landing | the Teams pull (`parse_silver.py` wipe-on-landing) | 1 | not live (the pull is not applied; row D2-S10) |
| research_meeting silver | none in this act | 0 | excluded above |

## Both branches

- **A row's residual check finds a token it cannot place:** the row is wiped and marked `held_out`; it stays stored, never shown by either reader
  (shared holdout filter, TR-s-19).
- **No residual:** the row's text is the wiped text, `held_out` false.
Row counts per key are unchanged in both branches; the before/after counts are reported.

## Proof (the CTO's): the planted-token test on the rewritten bytes

After the run, the issuer reads the 30 rewritten keys back and re-runs the wipe over every non-held-out row (the `research_fold.verify_stored`
pattern): re-wipe counts {name, id, email, phone} must all be 0, and every key carries a NEW VersionId. Counts only.

## Rollback per key

Copy each key's prior VersionId (the JSON above) back over the key. No delete is needed or authorised.

## Conditions

Counts, keys and version ids only in every report; no transcript text. A change ledger opened before and closed after, naming the pin.

-- 2.0.0_SA_COO~T2
