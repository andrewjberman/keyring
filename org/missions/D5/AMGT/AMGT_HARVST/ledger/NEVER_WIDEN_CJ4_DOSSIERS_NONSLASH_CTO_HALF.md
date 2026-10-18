# NEVER-WIDEN -- CTO HALF: `HVST-cj-4`, 75 non-slash dossiers rebuilt (round 95)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~07:2xZ. **Binds the COO half**
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round95/NEVER_WIDEN_HALF_COO_CJ4_DOSSIERS_NONSLASH.md` as committed at
845b69a8cc, sha256 `35e368f31b784a7d4e285dafd124588e56b87fb8773c272dfda052b7b7972e57`. Any edit to that file voids this half.

## What I read at signing

- **The model-row rule, which the COO half left unread** (`lib/research/corpus/dossier.py:1185-1250`, `_model_block_read`, and :1511-1513):
  - `model_rows` is built from the ONE model block whose key sorts last under
    `derived/model_block/<slash_safe_key>/<timestamp>/model_block.json`, which is the newest landed stamp, read RAW;
  - the block's key enters `inputs`.
  - So "a differing model_block input" means a newer stamped block has landed since the stored dossier was built, and the `model_rows`
    move is that newer block. "Newer Bloomberg pulls" is my shorthand for that; the rule is "newest landed stamp".
- **A hazard the subset check does not catch:**
  - the read's `record["status"]` can be `READ_FAILED` or `ABSENT`, and `model_rows` is then built from no block;
  - that move still sits inside the allowed set `{fund_form_ref, model_rows}`;
  - so a failed read would pass Branch A and serve emptier model rows.
  - Condition 1 closes this.
- **The writer:** N = 1, `dossier.write_one` (:1651), which never overwrites. The COO half states the rest of the rule as I read it.
- **KMB_US_Equity:** W1's REC to leave it out is accepted. My ruling names the moved names, and KMB moves no served field.

## Blast radius

- 75 gold keys are added under `amgt/harvest/gold/research_dossier/`. Nothing is overwritten or deleted.
- Served values move, per name: `fund_form_ref` and/or `model_rows` as `cj4_expected_moves.txt` lists, plus `as_of`, `dossier_key`,
  `content_sha256`, the dossier entry of `source_keys`, and the duplicate and denominator counts.
- Every other served value stays equal.
- No continuation, fund form, ai_fill, gateway, IAM or schedule change.

## Both branches

As the COO half states them, per name, with condition 1 added to Branch B.

## Rollback

ADD-ONLY. Removing the 75 keys restores the pre-act pick. That is an S3 delete, Andrew's act, and it is not pre-approved here. Served
values move the moment each object lands, so the canary (C-7) bounds the first exposure.

## Conditions of this signature

1. **Model-block guard, pre-write, per name that moves `model_rows`:**
   - the build's model-block record reads `status: SERVED`;
   - its object key's timestamp is LATER than the model-block stamp in the stored dossier's `inputs`;
   - the new `model_rows` count of rows with a value is not lower than the served count.
   - Otherwise STOP for that name.
   - For a name that does not move `model_rows`, the record still reads SERVED, or the name's served `model_rows` is already built from
     no block.
2. **C-1 to C-10 bind as written.** That includes:
   - C-1: the `lib/research` diff from the census commit to the worktree commit prints empty, so a later HEAD that differs is not used;
   - C-6: no continuation and no slash-key write;
   - C-7: the UNH-then-CPA canary through the gateway;
   - C-8: the counts after;
   - C-10: site Z is told first, and there is no GO before its answer.
3. **The S44 rule:** foreground, 5 to 10 names per command, a manifest line flushed per name. The NEVER-2 close is COMMITTED with the
   manifest.

## VERDICT: SIGNED (CTO).
