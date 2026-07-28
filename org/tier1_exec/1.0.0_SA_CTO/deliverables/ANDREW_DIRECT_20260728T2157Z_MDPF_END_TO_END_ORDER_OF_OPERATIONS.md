# ANDREW-DIRECT — 2026-07-28 ~2157Z — MDPF END-TO-END, ORDER OF OPERATIONS, NO TANGENTS

**Received by:** `1.0.0_SA_CTO` (Andrew at this terminal)
**Recorded + broadcast:** same turn, per `org/XXX.md`.

## VERBATIM

> "I am going to break down the order of operations exactly as it is needed right now and I need them
> carried through to completion without distraction and without tangent. First, I need MDPF completely
> done end to end as I have described above. That means that all production of mdpf artifacts from the
> opal-data-assets bronze and silver layers need to be condensed in
> opal-data-assets/portal/gold/mdpf/{"firm" or "global"}/... That needs to be validated immediately.
> Second to that, we need to validate that the publisher lambda that writes those assets to the
> opal-data-portal-v2 bucket is functional and on schedule. Third, we need to run it right now and make
> sure that we have maximally updated data for every single channel. Please proceed with this directive
> immediately."

Also, same window, on `data/analysis/`: deprecated, archive — **PARKED by his own subsequent order**
(*"instead of doing that, we are now fucking around with data/analysis"*). Worktree verified clean; the
interrupted move never landed. Nobody touches it until MDPF is done.

## WHAT THIS AUTHORIZES (CTO reading, stated not implied)

1. **The immediate chain run** — Andrew's explicit word satisfies the ad-hoc carve-out ("run it right
   now" / "maximally updated data for every single channel"). First run since the Stage-6 cottonwood
   grant landed 20:26Z, so this run is ALSO the grant's acceptance test.
2. **The publisher re-point + schedule + live write to `opal-data-portal-v2`** — this IS items 2 and 3.
   Sovereign direction on exactly the never-widen question; CTO half supplied herewith, COO CC'd for the
   co-sign record. Target = the locked layout: `platinum/{product}/{scope}/{artifact-type}.json`.
3. **Everything else in every lane is BELOW this.** No tangents.

## STATE AT DIRECTIVE TIME (grounded this turn, applied plane)

- **STEP 1 tree EXISTS and produces daily**: 11 objects, 4 scopes, all written 15:49Z today.
  Data vintages: 49f 07-27/28 · inflection 07-27 · global 07-27/28 · **cottonwood 07-20/07-22 (stale —
  cause known+fixed: emitters were IAM-blocked at dispatch `:523` until 20:26Z; the 15:49Z run predates
  the grant)**. Type coverage asymmetric per scope (aum-metrics/account-units cottonwood-only,
  non-model-assets global-only) — validation must say whether that is declared or drift.
- **STEP 2 publisher is NOT functional for the canonical path and NOT scheduled** (measured live 2157Z):
  `STAGING_ROOT=gold/mdpf_revamp` (pre-canonical tree), role = old fenced
  `opal-assets-mdpf-portal-publisher-role` (explicit-denied from portal-v2 by the fan-in fence),
  **zero EventBridge rules target it**. The new egress principal (role, correct legs) landed tonight
  @`a11b8e2cc3`; the live-serve grant sits at `count = 0` awaiting exactly this authorization.
- **STEP 3** blocked on 2 for the publish; chain re-run required first so cottonwood publishes fresh,
  not 07-22.

## DISPATCH (same turn)

| who | order |
|---|---|
| `0.7.0_AE_CloudOps~C` | FIRE THE CHAIN NOW; verify cottonwood emitters execute; report per-scope vintages of `portal/gold/mdpf/**` after |
| `0.7.0_AE_CloudOps` | Publisher: re-point BOTH legs (read `portal/gold/mdpf/`, write `platinum/mdpf/{scope}/{type}.json`), swap to egress role, flip live-serve grant (Andrew-direct + CTO; COO CC), add its OWN ScheduleExpression (R2), targeted apply; INVOKE on chain completion; verify objects |
| `2.0.0_SA_COO` | co-sign record + sequence the consumer re-point (portal reads `platinum/`) immediately behind the publisher — the true end of "end to end" |
