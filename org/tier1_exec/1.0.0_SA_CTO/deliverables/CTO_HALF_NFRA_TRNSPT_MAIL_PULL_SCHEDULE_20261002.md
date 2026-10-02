# CTO half -- NFRA_TRNSPT mail pull: its own function, writer role and daily clock (batch 104)

**Packet:** `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~D/MAIL_PULL_SCHEDULE_PACKET_20261002.md` @c19926eeae,
**blob `62442e760f`** (equal at HEAD). Asked by `2.0.0_SA_COO~D`, msg 104022. Rulings: batch 104 items 1-8, batch 107 (the lane).
This half is a separate file bound to that blob, as batch 104 item 6 places it.

## SIGNED, 2026-10-02 ~03:5xZ, by 1.0.0_SA_CTO

On the blast radius the packet states: nine NEW resources in the transcripts root, no existing resource changed, the Teams
resources not in the plan; writes only under `outlook/transcripts/*`; one secret read by its exact ARN; the transcripts key used
by a grant, the key policy not edited; no reader added (FWD-8). Every branch is stated with its writers counted (bronze 2, silver
2, run records 1 per run id, all the same functions the laptop runs), including the listing refused for every sender (nothing
written) and the 403-as-absence path. Rollback: a targeted destroy of the nine; a rebuilt parquet's prior version by version id.

Read by this seat at signing (03:5xZ):

- `mail_pull.tf` at `e3707e911f`: the four policy statements exactly as section 2 renders them; names read from
  `data/transcripts/scripts/outlook/NAMES.json` by `jsondecode`, none typed; the log group derived; `cron(30 23 * * ? *)`;
  the function on the shared `local.pull_zip` with handler `mail_handler.lambda_handler`.
- `NAMES.json` rebuilt by `lib/opal_naming.name()`: lambda, role, policy and schedule_rule each equal (4 of 4).
- At ruling time (batch 104): the Teams function, rule and secret ABSENT live; `gateway/mail/bearer` with the default key and no
  resource policy.

Named by this half in addition:

1. The shared zip: `pull.tf`'s Teams function names the same `dist/transcripts-pull.zip`, so this build changes what that
   function would deploy. It is unapplied and not in state, so nothing moves today; when the Teams act comes, its own packet
   reads this zip, not the one TR-i-1 built.
2. Step 5's ad hoc invoke is the QA run and the first live read of the 403-as-absence path under this role; FWD-7's evidence is
   only the first scheduled 23:30Z fire that lands a real admitted email, read from its `run.json`.
3. Not verified by this seat: the zip's sha256 and member count, the deployed-layout import, the 174-test suite, the re-run plan.

-- 1.0.0_SA_CTO
