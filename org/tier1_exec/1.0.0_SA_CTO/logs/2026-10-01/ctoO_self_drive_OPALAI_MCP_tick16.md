# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 16 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** 15 (17:24Z, quiet), the inter-tick acts 16:3xZ-18:2xZ, and 16 (18:24Z). Cron 84d0ab03.
**state:** ARMED

## Andrew-direct received (each recorded by its seat; quoted from the records)

1. **~17:0xZ, to laptop CRO** (relay 27974): "You may run through and do what is necessary to apply and deploy now..."
   I ACCEPTED a laptop deploy on base 0a1d9079c6 with 5 host conditions (msg 27978). `2.0.0_SA_COO~O` independently
   accepted with 4 (msg 27977). The route was then superseded by:
2. **~17:2xZ** (relay @d34037d1f5, msg 27984): "Site Z does both (Recommended)". This **lifts the TAXSMA hands-off for
   this one release.** Measured ALB rules: the `/ms/` rules are EXACT paths. Ruled: one exact-path rule for
   `/ms/taxsma-workbook`, no wildcard; the C7 "/ms structure-only" wording tension is carried to OPLGTW's next analysis.
   Routed to `2.0.0_SA_COO~O` as round label 12.
3. **~17:3xZ** (msg 27990): "ON at this deploy (Recommended)": the bearer is non-empty, and the identity is the
   opalbloomberg@ oid, confirmed by a read-only host read before any upload.
4. **~17:4xZ** (msg 27994, @92a542c450): "prioritize this work ahead of their own projects". No in-scope gateway act
   was in flight to hold.
5. **~17:4xZ, to CRO~O** (msg 28000, @ecc8f0e180):
   - 8194 wall apply "sure";
   - G-MSPID "doesnt matter right now" (DEFERRED);
   - partner rollout downstream;
   - **priority: MCPINDEX and Opal-employee MCP use**;
   - the transcripts-bucket question is the CRO's to answer.

## Driver acts

- 8194: routed the approval (msg 28001/28002). The apply FAILED on a script defect (msg 28004: New-NetFirewallRule
  rejects `::1`; 0 rules, nothing partial). **Ruled:** `RemoteAddress 127.0.0.0/8` only; run the reviewed fix commit
  under Andrew's "sure"; the PROD promote of the fix rides the next G-PUSH. The issuer amended it (A2 @b719cae333);
  AC2 PASS @c1d3fd8ef3.
- **G-TEAMS-TX treated as MET** pending OG-tx-2's own live read, on CRO~O finding 28007 (on 9/29 Graph returned
  attributed `text/vtt` for 30 transcripts). OG-tx-2 un-holds after the Tax release. **Provisionally off Andrew's list.**
- The laptop reboot notice (msg 27967) and the non-shared-ref push NOT done (msg 27982; a hook would have shipped 27
  pipeline scripts) were both noted.

## Measurement (18:24Z)

Inbox 0. Sequence: no flags on the 5. Served 0a1d9079c6.
- **Round 12 (Tax):** OG-tt-1 COMPLETE @65ff874a2e; drained @c7d51bb5b5. **Verified here:** ALB listener rule **36 =
  exactly `/ms/taxsma-workbook`**. A public no-bearer probe returns **404** (the app route is not deployed yet), so the
  edge rule is live and harmless until the app release.
- Census over 114 worktrees, in scope: `nfra-mcpindex-r6-bd-merge-retire` (by design). `mdpf_taxsma-tx-r-1` is the
  laptop's open TAXSMA ledger, not this seat's.

## Calls

No open calls in scope OPALAI_MCP_SITEZ (tick 16). Next at this seat: the CTO half on round 12's app release, signed
promptly per Andrew's priority.

## Acts only Andrew can perform (each with its citation)

1. **Re-run the 8194 rule elevated** (his UAC; `0.0.0_AB_MSTR~Z` arranges it). It is already approved ("sure"); only
   his elevation is needed.
2. **opal_ai DEV fast-forward** fd8ab8a -> 9c0a80b (PRD "DEV/PROD release on Andrew's word"). REC: approve.
3. **MCPORTAL G-CLOSE with Alyssa**, at a time he sets (staged @154894312f).
4. **G-W** (an R20 acknowledgement for `platinum/advi`).
5. **r6.J1**: Alyssa's Schwab cold run.
- **Deferred by his word, not listed:** G-MSPID (and MCPMSP's other partner gates), G-2ND (downstream).
- **Removed:** G-TEAMS-TX (treated as met; it re-opens only if OG-tx-2's live read refuses).

## Completion test

NOT DONE: 0 of 5 complete. REACHABLE 2 (OPLGTW, MCPINDEX). UNREACHABLE 3:
- MCPORTAL: G-CLOSE, at Andrew's time.
- OPALAI: the 8194 elevated run, then the close run.
- **MCPMSP: G-MSPID, DEFERRED by Andrew ~17:4xZ** (newly classified).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| aws (read-only) | `elbv2 describe-rules` on the 443 listener | rule 36 = `/ms/taxsma-workbook` only | measured before ruling the exact path, then again after OG-tt-1 |
| curl | public no-bearer GET `/ms/taxsma-workbook` | 404 | edge forwards; app route not yet deployed |
| git worktree census | Python porcelain, 114 worktrees | expected sentinels only | |
