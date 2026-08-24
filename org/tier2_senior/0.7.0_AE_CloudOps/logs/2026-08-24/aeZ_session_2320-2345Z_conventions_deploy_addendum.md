# 0.7.0_AE_CloudOps~Z -- ADDENDUM: the conventions deploy, and a sha my own earlier log now names wrongly

**archetype:** DEPLOY

**Window:** 2026-08-24T23:20Z -> 23:45Z. **This entry exists mainly to correct two of my own logs.**

---

## ⛔ READ THIS BEFORE CITING EITHER EARLIER LOG TONIGHT

`aeZ_session_2006-2240Z_...` records `etfs-netassets-daily` live at
`CodeSha256 BEITykjhmRlEvcM8p9cBUFmKX7doqEP+jHGRPhOprxo=`. **That is now SUPERSEDED.**
A third deploy landed at 23:24:00Z:

```
  etfs-netassets-daily   BEITykjh...OprxoU=  ->  xosks8suawJqxyE0DW2yIHzso5tPPTwnQSa7h8Ua4OU=
                         1,126 lines         ->  1,335 lines
  last_deployed_commit   4e5800fde0          ->  d7aa525fa9  (the TO-4 conventions commit)
```
**A closed record is a snapshot, not an oracle** -- my own banked lesson, and the more precisely
someone cites those two logs the more confidently they can now be wrong. Both remain accurate AS OF
their windows; neither carries a forward reference to this one, which is exactly why this entry
leads with the correction rather than burying it.

## What happened

`0.4.0_DS_ClientPlatform~Z` STOPPED before writing the Z-S16 as-of fix, having measured that the
fields it would point at do not exist in the deployed bytes. `1.0.0_SA_CTO~Z` upheld the stop and
classified the 209-line gap: **PENDING DEPLOY, not drift** -- conventions commit `d7aa525fa9` at
22:26:48Z is **two hours AFTER** the 20:31:09Z deploy. Ruling 5732: deploy the conventions layer,
THEN the as-of fix, both before 13:00Z. **Step (1) was mine.**

>> **THE CLASSIFICATION IS THE WHOLE LESSON: "209 lines behind its tree" invites INVESTIGATE and the
>> correct reflex was DEPLOY.** The two are indistinguishable from the line count alone; only the
>> timestamps separate them. A drift finding and a pending-deploy finding look identical and take
>> opposite actions.

## Acceptance -- CTO~Z's check, run on the DEPLOYED BYTES

```
                                     BEFORE      NOW
  vendor_trueshares_Date                0          2
  as_of_basis                           0          5
  POSITIVE CONTROL fetch_trueshares_holdings       3    <- the census discriminates
  NEGATIVE CONTROL zzz_no_such_token_9999          0
  package sha == live CodeSha256                 YES
  member RAW-matches its HEAD blob               YES
  0-diff re-plan                                 rc=0 (no pipe)
```
**DS~Z's fix now has its input.** Against the prior bytes it would have been authored against the
tree, passed commit-gate, cited Andrew's ruling correctly, and changed nothing -- which is the most
dangerous shape available, and their stop is what caught it.

I re-derived the pending-deploy classification before acting, and applied my own 21:45Z constraint to
myself: verified the packaged file was COMMITTED and tree==HEAD before building, rather than trusting
that I would remember the rule I had written for someone else.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `deploy_ledger.py` | `open` (5 legs) / `close-leg` x5 / `close` | PASS | Third ledger of the session; opened at deploy-START, closed in-session. |
| live AWS primitives | `get-function-configuration`, `get-function` -> Code.Location download | PASS | The acceptance check is a CODE-layer read of the running package, not a tree read -- which is the entire point of the ruling. |
| `terraform` (via `safe-apply`) | plan / apply / `-detailed-exitcode` | PASS | 0 add / 1 change / 0 destroy; rc=0 re-plan. |
| `git log` / `git show` | timestamp + blob comparison | PASS | The timestamps are what classified pending-deploy vs drift; the blob compare is what proved the package matches HEAD. |

**Gap found (SECOND TIME TONIGHT, same tool).** `record-terraform-deploy.sh` routed around again --
measured CRLF-rewrite defect on this box. Set the three fields by hand with a script that PROVES the
JSON round-trip lossless on the UNMODIFIED file before writing. **Twice in one session is no longer
an incident, it is a cost the estate is paying per deploy**, and it is the tooling lane's to fix.

## Blockers

**None.** Three deploys tonight, three ledgers, all closed in-session, none stranded.

## Current State (supersedes the corresponding lines in both earlier logs)

- **`etfs-netassets-daily`**: `CodeSha256 xosks8suawJqxyE0DW2yIHzso5tPPTwnQSa7h8Ua4OU=`,
  1,335-line member, `last_deployed_commit d7aa525fa9`, `last_deployed_at 2026-08-24T23:24:00Z`.
  Carries the TO-4 conventions layer. Trigger `cron(0 22 * * ? *)` unchanged.
- **`etf-positioning-producer`**: `CodeSha256 sR9QvfiS82IyXzRC4JUECpn1yFxLKfSehqT32nteems=`
  (marshal fix), 512 MB / 120 s, `cron(0 13 * * ? *)` ENABLED. Env: `ETFS_BUCKET` +
  `OPAL_ETFS_PUBLISH_GRANT` only.
- **Source map** 201 functions; both ETF rows current on all three Rule-4 fields.

## Next Steps

- [`0.4.0_DS_ClientPlatform~Z`] TO-7 step (2): the as-of VALUE fix at `:526`. **Input is now live.**
- [`0.7.0_AE_CloudOps~Z`] **AC7, ~13:00Z 2026-08-25** -- the first SCHEDULED fire of
  `etf-positioning-producer`, observed at its own invocation record, `run_class: "scheduled"`.
  **Expect ONE invocation and ONE manifest. If three appear, the marshal fix did not take -- report
  that, do not reconcile it.**
- [tooling lane] `record-terraform-deploy.sh`: fails closed on cp1252, CRLF-rewrites under the UTF-8
  workaround. Routed around twice tonight.
