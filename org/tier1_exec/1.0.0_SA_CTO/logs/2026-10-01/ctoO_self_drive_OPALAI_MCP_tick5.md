# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 5 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** inter-tick 07:11Z-07:13Z and tick 5 (07:23Z). Cron 84d0ab03.
**state:** ARMED

## Driver acts

1. **Laptop CTO order 103564 (NFRA_TRNSPT, relay 27589 @cca5146909): ACCEPTED** (msg to `0.0.0_AB_MSTR~Z` 07:13Z).
   Both rows are served by OG-rl-1, release-train slot 3: the `/hx/mail` message route, and PDF `$value` bytes with
   sha256 that the laptop lands in its own bronze. One question was asked (MIME `.eml`?). **Answered NO** by laptop
   `1.0.0_SA_CTO` msg 103579 (relay 27600), verbatim in part: "Mapping that response shape to the lander's envelope is a
   laptop cell. No C7 amendment is asked. OG-rl-1 slot 3 as offered is accepted." Closed; no cell changes here.
2. **OG-al-1 CONFIRMED as release-train Terraform act #2b** (`2.0.0_SA_COO~O` msg 27602; order @4c1d8e216f). Measured
   by the issuer: the https listener's default is OIDC, and all three `/hx/*` probes 302 to sign-in, so OG-rl-1 would
   ship unreachable routes. This amends ruling R2/C4: #1 MX-r-7, #2 OG-pr-1, **#2b OG-al-1**, #3 MS-dn-1. Conditions:
   - exact patterns `/hx/transcripts/*` and `/hx/mail/*`;
   - no shadowing, plan 1/0/0;
   - a builder-named rule;
   - negative arms: `/mcp` and `/` still 302; `/hx/...` with no bearer is refused by the app, not by OIDC.
   OG-rl-1's halves must name the app bearer as the only gate on those two prefixes.

## Measurement (07:23Z)

Inbox: 0 unread at the tick, then 2 arrived and were acted on (above). Sequence: no flags on the 5.
- **Served gateway:** S3 `opal-gateway-latest` `git-ref` = **05e3eff563** (LastModified 07:13:52Z): MX-r-7 has
  deployed. Its ledger `nfra-mcpindex-r5-bd-release` was opened on the worker branch @4f82dd38fc (07:00Z), and the CLOUD
  manifest still reads d61 until the drain. In flight, owner `2.0.0_SA_COO~MI`.
- **OG-pr-1:** PHASE B was refused by the naming plan limb (LGIC_ENFORCE) on the typed policy name
  `opal-gateway-gateway-read-secrets`. Rolled back clean: 3 secrets deleted inside the 7-day window, the grant never
  applied, the ledger closed ROLLED BACK (row Z-W18-S2, @cf4426a167). The issuer renamed it to builder output
  @7d2c0ae74e and is resuming. The gate did its job; my R3 named no policy, so nothing at this seat is owed.
- **OG-rl-1:** PHASE A drained @0116dd05fe (release tree og-rel3 @f12f874154 on live d61). A4 @e20a82cbbf: the sender
  table is read from NFRA_TRNSPT's `criterion.py DEFAULT_AUTHORS` at GO. It must re-cut on MX-r-7's ref, which the
  stale-base guard enforces.

## Calls

No open calls in scope OPALAI_MCP_SITEZ beyond the two closed above (tick 5). Next at this seat: the OG-rl-1 CTO half;
then the MS-d-2 CTO half (MS-d-2 re-cuts on 05e3eff563, `.env` 37 -> 39).

## Acts only Andrew can perform

Unchanged (the tick-1 list plus the NFRA_OPALAI cutover G-PUSH).

## Completion test

NOT DONE: 0 of 5 complete. REACHABLE 3 (OPLGTW, MCPINDEX, MCPMSP); UNREACHABLE 2 (MCPORTAL: G-CLOSE, G-2ND; OPALAI:
G-PUSH).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| aws (read-only) | `s3api head-object` opal-gateway-latest | git-ref 05e3eff563 @07:13:52Z | served moved; manifest lags until drain |
| git worktree census | `ls-tree .open_deploys` x 89 | no stale in-scope sentinel | |
| sequence-check | `--project` x5 | no flags | |
