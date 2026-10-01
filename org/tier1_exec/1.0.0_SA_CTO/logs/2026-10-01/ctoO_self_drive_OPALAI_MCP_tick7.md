# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 7 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** 6 (08:23Z, quiet), the inter-tick acts 07:34Z-09:0xZ, and 7 (09:23Z). Cron 84d0ab03.
**state:** ARMED

## Driver acts since the tick-5 log

1. **OG-al-1 condition 4 corrected** (`2.0.0_SA_COO~O` msg 27616, @156cdbd83d). My condition said `/mcp` stays 302; it
   was wrong. Measured: `/mcp` is an app 401 through the priority-10 `mcp_oauth_core` forward rule. al.AC2 now asserts
   `/` 302, `/mcp` unchanged 401, a non-`/hx` control 302, and `/hx` refused by the app. Accepted.
2. **NFRA_MCPINDEX L10 round-5 analysis** @1edec80f63, on `3.0.0_SA_CVO~O`'s slug msg 27655 (`REMEDIATION_v4.md`
   @3ff13b945f; grades Z-C-S34):
   - 0 REALIZED / 5 NOT_REALIZED / 5 DEFERRED.
   - MX-t-12 CANCELLED.
   - 7 CTO-owned rows ruled. Z-W21-S19 and Z-W19-S13 were placed with NFRA_OPLGTW's next enrichment. Z-W19-S22 is the
     deliberate `.owned-paths.yaml:1818` grant.
   - Round 6 = 7 items. The lead is: discover reads `silver_datasets`, Schwab gets catalog rows, and every row is graded
     on reachability. It rides the slot-4 release with G-RDR; Alyssa's r6.J1 runs after it.
3. **MS-d-2 (train slot 2): CTO never-widen half SIGNED, G-A ACCEPTED** @082e83dbcf (msg 27679). Independent reads:
   - live 05e3eff563 on S3 and the manifest;
   - release tree eaafbae398;
   - 7 added / 10 modified / 0 deleted;
   - C5 absent;
   - 0 tool definitions moved;
   - the internal reader role's trust is `opal-gateway-role` only.
   One void condition was added: a `query_v0` read-back error class not seen on 05e3eff563 for the same key. The issuer
   encoded it as `d2.RB.sh` (@647e55f4b6).
4. **Z-S32 (ARMED: the host `.env` is not shell-safe; the cot OTP bearer leaked twice), interim disarm ruled**
   (message to `2.0.0_SA_COO~O` 09:25Z):
   - no shell-sourcing of the host `.env`, with a names-only or `/proc` single-key read in the ANNOUNCE template;
   - OG-rl-1 rotates the cot bearer as already ruled, naming its consumer;
   - the shape fix goes to OPLGTW's next enrichment.

## Measurement (09:23Z)

Inbox 0 unread. Sequence: no flags on the 5. No in-scope open ledger on the shared tree.
- **Served gateway:** S3 `git-ref` = **2c0f84966d** (LastModified 09:08:28Z). MS-d-2 is deployed; train slots 1 and
  2 are done.
- **NFRA_OPLGTW:** OG-pr-1 and OG-al-1 COMPLETE (train TF acts #2 and #2b; @885f660510). OG-rl-1 re-cuts on MS-d-2's
  ref for slot 3.
- **NFRA_MCPINDEX:** round 6 ISSUED @f797d8594a, 6 cells in one issuance, from the round-5 analysis.
- **NFRA_MCPMSP:** MS-d-2 PHASE B landed (ledger close and drain are the issuer's).
- **NFRA_OPALAI / NFRA_MCPORTAL:** no movement; each waits on Andrew's acts below.

## Calls

All closed the tick they arrived (items 1-4 above). No open calls in scope OPALAI_MCP_SITEZ (tick 7). Next at this
seat, event-gated: the OG-rl-1 CTO half (slot 3), then the slot-4 MCPINDEX release half.

## Acts only Andrew can perform (each with its citation)

- NFRA_OPALAI cutover **G-PUSH** (opal_ai r2-dev -> PROD, then CLOUD; `0.0.0_AB_MSTR~Z` on his word; org/XXX.md
  shared-branch law; OPALAI PRD "DEV/PROD release on Andrew's word").
- NFRA_MCPORTAL **G-CLOSE** (his Entitlements-tab acts) and **G-2ND** (a person signs in), MCPORTAL blocking.
- NFRA_OPLGTW **OG-g-1**: the Opal IT test user (entitlement beyond his grants).
- **G-TEAMS-TX**: the Teams transcript tenant settings via IT (PRD v1.3 C7).
- NFRA_MCPINDEX **G-W**: the R20 acknowledgement for any `platinum/advi` literal (his "NOT YET").
- NFRA_MCPMSP **G-MSPID**, G-USER, G-IT-INF, G-ADVISOR, G-FIRM (identity/entitlement), and **G-KEY** (spend).
- **r6.J1**: Alyssa's cold run, after the slot-4 release (a person is the instrument, by his word A6).
- **D9 placement card** (CVO verdict 27494): move NFRA_OPLGTW and NFRA_MCPINDEX to D6 at round close (REC), or keep
  them in D9 with a named exception.

## Completion test

NOT DONE: 0 of 5 complete. REACHABLE 3 (OPLGTW, MCPINDEX, MCPMSP). UNREACHABLE 2:
- NFRA_MCPORTAL: G-CLOSE, G-2ND.
- NFRA_OPALAI: G-PUSH, then the close run.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| aws (read-only) | `s3api head-object`; `iam get-role` | served 2c0f84966d; reader-role trust | sign-off and tick reads |
| git | `rev-parse <commit>:<tree>`, `diff --name-status`, `grep -c` C5 | trees match; 7A/10M; 0 C5 hits | sign-off reads |
| sequence-check | `--project` x5 | no flags | |
