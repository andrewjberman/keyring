# SELF-DRIVE OPALAI_MCP_SITEZ -- tick 10 -- 1.0.0_SA_CTO~O

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d
**Ticks covered:** inter-tick 11:25Z-12:2xZ and tick 10 (12:23Z). Cron 84d0ab03.
**state:** ARMED

## Driver acts since the tick-9 log

1. **DESIGN FORK ruled: Opal_Agent walled off Bloomberg DAPI 8194** @ff362bfa86. The fork came from
   `2.0.0_SA_COO~AI` msg 27790 (OA-e-6: Opal_Agent reaches 8194). Research: `4.0.0_SA_CRO~O` msg 27806 @5d804ea419.
   - DAPI has no per-OS-user check, and G3 alone leaves a shell + Python + readable blpapi DLL path.
   - The fix is a per-user Firewall outbound block on 127.0.0.1:8194 for Opal_Agent and Opal_MSP; 8790 stays open.
   - The falsifier runs first. The apply is Andrew's admin act. It is a precondition of the OPALAI item-0 close run.
   - `2.0.0_SA_COO~AI` cut OA-f-10 @e058398966. Accepted as LOCAL; no CVO L9 is needed.
   - The DAPI directory ACL (Users FullControl) was surfaced to `0.0.0_AB_MSTR~Z`.
2. **MX-r-8 (train slot 4): CTO never-widen half SIGNED, G-A ACCEPTED** @aaf822e7ad (msg 27815). Independent reads:
   - live daa56d81ac;
   - trees 7d222e01f6;
   - 3 served files plus 2 tests (a non-material count note);
   - deploy script identical;
   - no tool, `$select` or params change (the widened census);
   - C5 absent.
   Two void conditions added: an A1 firm-principal silver leak, and `unrouted` other than 0.
3. **The `/hx/mail` request contract** for laptop `2.0.0_SA_COO~D` (msg 103715), @3a05db059a, read from deployed
   code. It flags the no-listing-route gap as a C7 addition accepted in principle.
4. **Routing:** laptop COO~D 103728 asked for the positive-arm message id. Routed to `2.0.0_SA_COO~O` with a CTO OK:
   the id only, an identifier and not a secret.

## Measurement (12:23Z)

Inbox 0. Sequence: no flags on the 5. Served: daa56d81ac (MX-r-8 PHASE B not yet run).
- **In-scope open ledger:** `nfra-mcpindex-r6-bd-merge-retire` (MX-s-16). It waits on its scheduled `bd-silver-merge`
  acceptance, as signed.
- **New row Z-S36** (`2.0.0_SA_COO~O`): a release without `OG_MAIL_SENDER_TABLE` silently blanks the `/hx/mail`
  table. The MX-r-8 half's read-back (shape unchanged, else roll back) and the COO half's "not in hand -> no deploy"
  already cover slot 4. The durable fix, a host-side read like the R4 rosters, goes to OPLGTW's next enrichment.
- **Duplicate artifact noted:** `2.0.0_SA_COO~O` also wrote a `/hx/mail` contract (@bc4452a2aa) beside this seat's
  @3a05db059a. Both are read from deployed code. The laptop holds this seat's via relay. No act.

## Calls

All closed the tick they arrived (above). No open calls in scope OPALAI_MCP_SITEZ (tick 10). Owed, event-gated:
- the NFRA_OPLGTW L10 analysis, on the CVO's slug;
- the NFRA_MCPINDEX round-6 analysis, which places the cot sentinel fix and Z-S74;
- the MS-dn-1 Deny half, after slot 4 serves.

## Acts only Andrew can perform (each with its citation)

- **NEW: apply the Opal_Agent / Opal_MSP 8194 Firewall rule** (OA-f-10's script), after the falsifier reads
  refused-inside. Citation: OS-account and host administration, isolation design R1 class; CTO ruling @ff362bfa86 R2.2.
  It gates the OPALAI close run.
- **NFRA_OPALAI cutover G-PUSH** (`0.0.0_AB_MSTR~Z` on his word; shared-branch law).
- **NFRA_MCPORTAL G-CLOSE, G-2ND** (his Entitlements-tab acts; a person signs in).
- **OG-g-1** Opal IT test user; **G-TEAMS-TX** (it also holds OG-tx-2).
- **G-W** (an R20 acknowledgement for any `platinum/advi` literal).
- **NFRA_MCPMSP G-MSPID**, G-USER, G-IT-INF, G-ADVISOR, G-FIRM; **G-KEY** (spend).
- **r6.J1**: Alyssa's cold run, after slot 4 serves.
- **The D9 placement card** (CVO verdict 27494; REC: move to D6 at round close).

## Completion test

NOT DONE: 0 of 5 complete. REACHABLE 3 (OPLGTW, MCPINDEX, MCPMSP). UNREACHABLE 2:
- MCPORTAL: G-CLOSE, G-2ND.
- OPALAI: G-PUSH plus the 8194 wall apply, then the close run.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| git | `diff --name-status`; widened tool/`$select`/params census; `rev-parse` trees | MX-r-8: 3 served + 2 tests, 0 tool changes | census widened after the OG-rl-1 miss |
| git show | `mail_route.py`, `transcript_route.py` at daa56d81ac | contract read from deployed bytes | one rail denial, then re-run with a rail-checked marker |
| aws (read-only) | `s3api head-object` | served daa56d81ac | |
| sequence-check | `--project` x5 | no flags | |
