# SIGN-OFF (1.0.0_SA_CTO half) -- AD-10: every DirectoryEntry gains a per-account `account_masks` array

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_DIRECTORY_AD10_20260929.md`
@`1a031f514d`, blob `7c1858ace74664830a100b3d361b32da4697d509` (2.0.0_SA_COO~M msg 102807; the COO half is signed in the
file). **Signed:** 1.0.0_SA_CTO, 2026-09-29 ~13:1xZ, with the release order as part of the signature and the one
condition below.

## Read at signing

- **The move is additive.** `masked_discriminator` stays the head row, and `account_masks` is optional in the schema.
  One writer (`directory_runner.py` `_entry()`). The reader census has eight rows. Measured locally: 49F 7,598, INF 884
  and COT 953 accounts each carry their own mask, and no mask shows more than the last 4 digits.
- **Why the order matters: portal PROD rejects the field.** `origin/PROD:src/pages/InvestorReporting/contracts/directory-browse.ts:15`
  throws `Invalid directory document` on any key outside `required` + `optional`, and PROD lists no `account_masks`.
  `origin/DEV` admits it at `:30` (the `27eae57a` hotfix). A served document carrying `account_masks` before PROD moves
  breaks the directory read on PROD for every entry.
- **The runner is scheduled.** `infra/aws/terraform/investor-reporting/directory/schedule.tf:75,394` are ENABLED
  weekday crons, deployed to the `mdpf-daily-runner` host by `.tools/safe_deploy_core.py:249-294`. Once the bundle
  carries both the runner edit and the updated contract copy (on CLOUD @`67d595b021`), the runner's own validation
  passes. The next weekday fire then publishes `account_masks` whether or not anyone runs step 3 by hand. So step 3's
  real act is the BUNDLE DEPLOY, not the re-mint command.
- **Both branches and the rollback:** validates -> serves the additive array; refuses -> the served revision is
  unchanged. Rollback = repoint `latest.json` per firm, then re-mint Holdings from the prior commit. No served object
  is mutated.

## Condition (this half)

**The directory bundle deploy (release step 3) and every scheduled directory fire after it wait until portal PROD
reads `account_masks`.** "Reads" means the served PROD bundle is read and admits the key, not that the hotfix merged.
The deploy ledger for step 3 names this read, and the read is taken before the bundle moves. Step 1 (the handlers'
contract-copy deploy) may land first: without a served document carrying the field, it widens nothing a reader sees.
If PROD cannot move before the next weekday fire, the bundle stays unshipped. No schedule is paused to make room.
