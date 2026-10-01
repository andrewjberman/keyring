# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 14 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** inter-tick 15:2xZ-16:2xZ and tick 14 (16:24Z). Cron 84d0ab03.
**state:** ARMED

## Andrew-direct received (recorded by `4.0.0_SA_CRO~O`, msg 27931)

Record `org/tier1_exec/4.0.0_SA_CRO~O/deliverables/ANDREW_DIRECT_20261001_1551Z_FABRIC_STATUS_ANSWERS_GPUSH_ALYSSA_D6.md`
@53ad7cb452. Verbatim: "1.) Promote opal_ai to PROD, approved. 2.) Explain further. 3.) What is her question? 4.) We can
do this with Alyssa. 5.) Let me know what you need fro me on this. 6.) I agree with the movements to D6."

## Driver acts since the tick-13 log

1. **G-PUSH routed** to `0.0.0_AB_MSTR~Z` and `2.0.0_SA_COO~AI` (msgs 27934/27935). The 8194 rule apply is NOT in the
   quote, so the item-0 close run stays held. **Done and verified:** opal_ai origin PROD = 9c0a80b8d0 (ls-remote here;
   a fast-forward from fd8ab8a). DEV is still fd8ab8a.
2. **G-CLOSE colleague = Alyssa:** asked `0.0.0_AB_MSTR~Z` to seat `2.0.0_SA_COO~MP`. It is now LIVE (msg 27950) and
   stages MP-c-1 for a time Andrew sets. G-2ND is not covered.
3. **D9 -> D6 card ANSWERED.** It moves at each project's round close (CVO verdict 27494), recorded in both project
   blocking fields @568c34b9cd. Pinned citations are not rewritten. The D9 row's removal is the laptop row-owner's
   half.
4. **OG-rl-2 (slot 5) VERIFIED LIVE:** S3 and the manifest read 0a1d9079c6 (15:33:58Z). Issuer rl2.AC1 9 of 9, and the
   CVO L1 hash matched. **Laptop order 103750 served**, relayed through `0.0.0_AB_MSTR~Z`. Both laptop orders (103564,
   103750) are now served. **The gateway release train is complete: slots 1-5 and Terraform acts #1, #2, #2b and #3.**
5. **OPALAI cutover plan @8db0ecf602 ACCEPTED** (msg 27956):
   - the runtime pull happens at the close-run launch, with the gate refusing CHECKOUT-NOT-AT-PROD;
   - the t-1 parent half merges only after the close run (C11);
   - Z-S51, a silent downstream hook left a MERGE_HEAD open, is routed to MSTR~Z.
   **New act for Andrew:** the opal_ai DEV fast-forward.

## Measurement (16:24Z)

Inbox 0. Sequence: no flags on the 5. Served 0a1d9079c6. Space-safe census over 111 worktrees: only
`nfra-mcpindex-r6-bd-merge-retire` (MX-s-16, open by design) in scope. NFRA_OPLGTW round 11 is terminal; round 8 is
terminal except OG-tx-2, held on G-TEAMS-TX. The OPLGTW and MCPINDEX L10 slugs are not yet received.

## Calls

No open calls in scope OPALAI_MCP_SITEZ (tick 14). Andrew's items 2, 3 and 5 are questions; `4.0.0_SA_CRO~O`, the
brief's author, answers them.

## Acts only Andrew can perform (each with its citation)

1. **Apply the Opal_Agent / Opal_MSP port 8194 Firewall rule** (OA-f-10's script). AC3 decides whether it works. It is
   an admin act: isolation design R1; CTO ruling @ff362bfa86 as amended. It gates the OPALAI close run.
2. **NEW: fast-forward opal_ai DEV fd8ab8a -> 9c0a80b** (PRD "DEV/PROD release on Andrew's word"; shared-branch law). REC:
   approve, so DEV never trails PROD.
3. **G-MSPID** (MCPMSP calling identities; identity and entitlement) is now the only gate on MCPMSP round 2. Also
   G-USER, G-IT-INF, G-ADVISOR, G-FIRM, and G-KEY (spend).
4. **MCPORTAL G-CLOSE** (with Alyssa; his Entitlements-tab acts at a time he sets) and **G-2ND** (a person signs in as
   Opal Bloomberg).
5. **G-TEAMS-TX** (Teams transcript tenant settings via IT; it holds OG-tx-2) and **OG-g-1** (an Opal IT test user).
6. **G-W** (an R20 acknowledgement for any `platinum/advi` literal).
7. **r6.J1**: Alyssa's Schwab cold run. The catalog no longer blocks it.

## Completion test

NOT DONE: 0 of 5 complete. REACHABLE 3 (OPLGTW, MCPINDEX, MCPMSP); UNREACHABLE 2 (MCPORTAL: G-CLOSE, G-2ND; OPALAI:
the 8194 apply, then the close run).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| git ls-remote | opal_ai origin | PROD 9c0a80b8d0, DEV fd8ab8a | G-PUSH verified |
| aws (read-only) | `s3api head-object` | served 0a1d9079c6 | OG-rl-2 verified |
| git worktree census | Python porcelain, 111 worktrees | 1 in-scope sentinel, expected | |
