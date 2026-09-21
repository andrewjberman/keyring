# /self-drive IRPT_FNTEND IRPT_BCKEND -- tick 7 (2026-09-21 ~17:4xZ)  state: ARMED

Driver `1.0.0_SA_CTO`; carrier @`c9ccd9f4e3`; cadence 30m (cron `46e545b7`). Previous log:
tick 4 @`8347c3c8ee`.

## IB-rth-6 (new LGIC buckets) resolved MOOT: the original buckets are recovered

`2.0.0_SA_COO~B` (msg 99113) stopped `IB-rth-6` (build `opal-data-inflectionwealth` +
`opal-data-cottonwoodcapital`) on a real registry-naming-law wall: a firm's `bucket`
field cannot diverge from `opal-data-{long}` under `lib/opal_naming.py validate()`,
and Terraform's `aws_s3_bucket.bucket` is `ForceNew` besides. Pitched three options
(full rename / R20 registry exception / re-attempt the original lockout), routed to
this seat as a naming-law + Andrew's-own-instruction-fork call. This seat's
independent read converged with `4.0.0_SA_CRO`'s, which had it live with Andrew
already (msg 99116) -- declined to duplicate the ruling, stood by to build the
`lib/opal_naming.py` side if option (ii) landed.

**Resolved cleanly, no naming-law change needed.** `4.0.0_SA_CRO` (msg 99125): Andrew,
at that terminal, found the actual mechanism himself -- the live Deny's
`ArnNotLike aws:PrincipalArn` condition matches only `role/*-inf-*` / `role/*-cot-*`,
never a user, which is exactly why no user-level IAM grant (including his own earlier
ListBucket attempt) could ever have worked. He created two recovery IAM roles named
inside the fence pattern (via `lib/opal_naming.py name()`, CONFORMANT), granted each
`GetBucketPolicy`+`PutBucketPolicy` on one bucket, and CRO used them to PUT the
correct fence+exemptions policy (the same shape `s3-lgic-firm-buckets.tf` renders) on
both buckets. Measured before/after: `user/Andrew_Berman` (no role) now reads
`get-bucket-policy`/`head-bucket`/versioning cleanly on both. Ledger L2 closed
@`a0097b1ef4`. `IB-rth-6` and the R20 exception card are withdrawn/moot;
`2.0.0_SA_COO~B` re-cuts. This seat's own standby (msg 99121/99122) stood down, no
naming-law edit made.

**Acted on the follow-through:** flagged to `2.0.0_SA_COO~B` that `IB-rtf-7`'s own
goal (clear bucket-policy access so `IB-rtf-5` can apply) may now be independently
satisfied by this same fix -- worth a fresh re-run rather than assuming the original
delete-bucket-policy path is still the only route. Their sequencing call.

Handled entirely under this loop's own CALL ROUTING (default: driver's own rec) --
no ruling needed once the mechanism resolved itself upstream; this tick's act was
confirming stand-down and connecting one dot for the owning lane.

## Scope state (denominators printed)

`IRPT_BCKEND`: `status: active`/`EXECUTING`, no sequence flags, 9 PENDING TOs at this
read. `IRPT_FNTEND`: `status: active`/`EXECUTING`, 1 PENDING TO at this read (wave-A
draining). **REACHABLE: 2 of 2.** **COMPLETION TEST: NOT DONE** -- 0 of 2 `status:
complete`.

## RESERVED cards still at Andrew

`irpt-ycharts-runner` EC2 stop-confirmation (unchanged, still open); the non-MFA
portal service-account question (unchanged). The new-bucket naming-exception card is
WITHDRAWN as of this tick (moot, see above) -- no longer open.

## Next tick (~18:11Z) watches

`2.0.0_SA_COO~B`'s re-cut of the freed `IB-rth-6` slot and whether `rtf-7`/`rtf-5`
clear on a fresh run; `IB-rth-1`'s 7-function apply; `IRPT_FNTEND` wave-A close-out.

Push state: LOCAL on CLOUD; `origin/CLOUD` `d32d3ad8b8` per `ls-remote` read this
write; only `0.0.0_AB_MSTR` pushes.

## Compiler Tools

`get_agent_status`; `to-check --all --project` x2; `sequence-check --project`;
`ack_messages`; `send_message`.
