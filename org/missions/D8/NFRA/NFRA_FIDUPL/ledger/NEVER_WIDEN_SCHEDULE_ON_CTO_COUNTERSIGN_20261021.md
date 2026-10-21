# NFRA_FIDUPL -- CTO COUNTERSIGN of the never-widen ADDENDUM: the three schedule rules ON

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-21 ~02:2xZ. **Binds the COO addendum**
`org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/2.0.0_SA_COO~P1/NEVER_WIDEN_ADDENDUM_schedule_on_20261021.md` as committed at
1a4ed1797f, sha256 `a1a8a794de0ee123fc6a7be37e564f88213380eb5d7ea120904aca0170bcb7e1` (re-hashed by me on disk and at the pin; equal).

## What I read at countersigning, by my own instrument

- `secretsmanager describe-secret fidelity/alongside/perg-list` (metadata only, no value): one version `8473b6cf-e3c0-4b5b-8dcc-94480a41b57b`,
  the only `AWSCURRENT`, last changed 2026-10-21T02:13:23Z. Equal to the addendum.
- `events describe-rule` on the three rules: `fidelity-alongside-fetch-leg-{1,2,3}-daily`, `cron(45 9 * * ? *)`, `cron(15 10 * * ? *)`,
  `cron(45 10 * * ? *)`, all DISABLED. Equal to the addendum's table.
- The six keys of the first day (content date 20261019) and run record `run-20261021T012004Z.json`, read by me at 01:20Z; sizes equal.
- The producer's own rule for both branches, as the addendum states it: a fire that finds a partial listing records the missing files
  and the failed step; a later leg completes the day; a landed day is `skipped_existing` by sha256. The lander is add-only.

## Blast radius and rollback, as signed

Exactly three EventBridge rules change `State` DISABLED to ENABLED under `safe-apply` with no `-target`; the pre-apply plan reads
exactly `3 to change`, the post-apply plan `No changes`. Rollback per resource: `schedule_enabled = false`, apply; a started fire
finishes and lands only raw files under `fidelity/alongside/bronze/`. No object is deleted by the act or its rollback. The box role,
buckets, prefixes and secrets are unchanged; no alert, SNS or SES.

## What this enable does NOT deliver, stated so no one reads it as done

- A fire runs the `once` mode: sign-in, six files, raw landing, run record, logout. The FIRM SPLIT (Andrew's deliverable 1,
  "split out to the relevant firms per each G Number"), the coverage record and the in-run recovery do NOT run until the box config
  carries `mode`, `firm_labels` and `account_columns`: that is the NEXT addendum, owed by the issuer, and the drive loop's stop
  condition is not met by this act alone.
- The per-G list (31 G numbers, 8 firms, 1 unattributed, masked) is a cross-check in this mode, not a driver. The one unattributed
  G number is a row for the split addendum to disposition.
- Three sign-ins a day, ~30 minutes apart, sit at the standing cap (3 per hour post-password); a fourth in the hour is refused by
  the standing rule, not by this act.

## Conditions on the first fire read-back (addendum section 3)

The issuer appends the first fire's time, the run record key and `outcome`, the six keys or `skipped_existing`, the logout
statuses, and the Quo message count. A first fire that fails is rolled back the same turn and its step reported.

**VERDICT: COUNTERSIGNED.** `2.0.0_SA_COO~P1` may release the ENABLE to `0.7.0_AE_CloudOps~NFRA1` on this file's commit.

-- 1.0.0_SA_CTO~DELL1
