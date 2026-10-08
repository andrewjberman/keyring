# Never-widen half: MDPF_HEALGAP round 2, drain act 4 -- mark 2026-08-31..2026-09-10 rebalancer_model_detail as missing (FWD-3)

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-08 ~16:3xZ. **For:** `1.0.0_SA_CTO~DELL1`, who owes the CTO half.
**Status:** COO half SIGNED; CTO half owed. The acting seat runs the act on dell1 under a change-management entry.

## The act

```
python infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/mark_missing.py --from 2026-08-31 --to 2026-09-10 \
  --feed rebalancer_model_detail --execute \
  --reason "the vendor serves current state only; model detail did not land on this date (2026-08-31..09-10 gap, brief PART VI.3-4) and cannot be truthfully fetched after the day"
```

- The act makes no vendor call.
- The dry run at 16:3xZ printed `WOULD-MARK` for exactly 11 dates, 2026-08-31 through 2026-09-10, all for `rebalancer_model_detail`.
- The tool prints `PRESENT` and writes nothing for a day where the feed exists (`mark_missing.py:9`).
- The CTO's live read at 16:3xZ found the 11 dates absent out of 80 (`CTO_HALF_MDPF_HEALGAP_R2_RUNNER_CODE_DEPLOY_20261008.md`).

## Write set and writers

The act writes exactly 11 new keys: `s3://opal-data-assets/blackdiamond/cottonwood/meta/<d>-missing.json`, each containing
`{as_of, feed, reason, marked_at}`.

- **Writers:** N = 1, this tool. The runner writes `-result.json` and `-complete.json`, never `-missing.json`.
- **Collisions:** none of the 11 paths exists (16:3xZ listing: 878 `meta/` keys, untruncated, 0 ending `-missing.json`; positive control: the `2026-10-08-complete.json` stamp is listed; 0 detail keys on the 11 dates). The tool's `PRESENT` guard is about the feed, not the mark, so the
  act reads the 11 paths before it writes and refuses if any key already exists.
- **Triggers:** none.
  - Census of 152 EventBridge rules: none matches `opal-data-assets` or `cottonwood`.
  - The bucket's notifications on the cottonwood prefix fire only on `bronze/` with the suffix `.xlsx`.
  - EventBridge delivery on the bucket is off.
- **Readers today:** none. The marks are what FWD-3's ACCEPT says a reader of the eleven days sees.

## Both branches

- **(A) The write is permitted:** the 11 marks land, and silver, gold and served output are untouched. Served delta 0.
- **(B) AccessDenied (the dell1 identity lacks `s3:PutObject` on that prefix):** nothing is written, and served delta is 0. The
  denial is reported with ACTION and RESOURCE the same hour (laptop CTO ruling 3), and the act re-routes to a seat that holds
  the grant.

## Rollback

Delete the 11 keys. The bucket is versioned, so a delete adds a delete marker.

An S3 delete needs Andrew's word under the autonomy rules. The rollback is therefore named here but not pre-authorized. It is
needed only if a mark is wrong, and the guard above makes a wrong mark unlikely.

## Acceptance

1. A listing of `meta/` shows exactly 11 `-missing.json` keys for 2026-08-31..09-10.
2. One body is read back: `feed rebalancer_model_detail`, with the reason above.
3. No `rebalancer_model_detail/<d>/` key appears for any of the 11 dates. The act filled nothing.
