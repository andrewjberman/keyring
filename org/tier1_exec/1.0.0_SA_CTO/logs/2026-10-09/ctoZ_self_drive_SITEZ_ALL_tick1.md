# `/self-drive 30m` every site-Z project -- tick 1 (2026-10-09 ~07:45Z to ~08:4xZ), `1.0.0_SA_CTO~Z`

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_074xZ_SELF_DRIVE_30M_EVERY_SITEZ_PROJECT.md` @4752d8dfcc.
Cron `fff05062` at :19/:49. **state: ARMED.**

## Andrew-direct this session (recorded)

| when | words | record |
|---|---|---|
| ~07:3xZ (laptop MSTR, relay 32505) | "cto needs to be running /self-drive on 30m interval covering all projects on sitez box ..." | arming record above |
| ~07:4xZ (this terminal) | "we don't need CTO~O anymore, you just lead the fabric here" | `deliverables/ANDREW_DIRECT_20261009_074xZ_CTO_O_RETIRED_CTO_Z_LEADS_SITEZ_FABRIC.md` @7d88c614cc |

CTO~O's session was already gone (MSTR~Z msg 32562). Its handoff was taken from its own 07:01Z log: no open calls at Andrew; r29 CTO
half signed; MCPINDEX v0.8 FWD-19 landed. Its three orphaned asks were answered here (C7, OG-bh-1, plus the r29 FYI).

## Scope (re-read at tick)

SITEZ-placed projects, 448 JSONs scanned. 9 at arm, 7 after this tick's acts:

| project | status | dep_stage | COO | after tick 1 |
|---|---|---|---|---|
| NFRA_REPORT | **closed** | ROUND_CLOSE | ~ZZ | CLOSED @57f8a76bf0 (PRD v0.9 @6813ebf91c, CVO signed @1ebbf7ecdf) |
| NFRA_OPSEC202609 | **closed** | CLOSED | -- | status carried forward @6000a6c482 (closed 2026-09-10, 85907c8985) |
| NFRA_MCPMSP | active | ROUND_CLOSE | ~MS | round-2 analysis @8a9def3720: round 3 = 2 cells; G-MSPID stays Andrew's act |
| NFRA_IAMROLES202609 | active | ROUND_CLOSE | ~ZI | FWD-4 owner ruled @fa8ec0e726; round-4 analysis @20c2fcabe8: round 5 = 3 cells |
| NFRA_OPLGTW | active | EXECUTING | ~O | C7 v2.4 @da1e2122fa; OG-da-1 half @93ddbb1288; OG-bh-1 half @e9bda7b982 |
| NFRA_OPALAI | active | EXECUTING | ~AI | ruled no /closer now (msg 32534) |
| NFRA_MCPINDEX | active | EXECUTING | ~MI | `0.7.0_AE_CloudOps~MX` seated for MX-r-9 PHASE B (MSTR~Z 32582) |
| NFRA_MCPORTAL | active | EXECUTING | ~MP | no call this tick |
| COMM_ASSIST | active | EXECUTING | **~ZZ** (new) | coo_lane @c4dea02951 |

Sequence: `sequence-check --project` returned no flags for all 8 read (5 UNPLACED by the sequence, so their directives govern).
**Completion test: NOT DONE**, 2 of 9 closed.

## Calls closed this tick (all by the driver, on its own rec)

| call | ruling | carrier |
|---|---|---|
| NFRA_REPORT FWD-13/15 after the 09-17 revert | RETIRE; endpoint = Andrew's ratified spec; header question NO; no round 5 | PRD v0.9 @6813ebf91c |
| open call `sitez-20261009T081243Z-6017`, IAMROLES FWD-4 owner | `0.7.0_AE_CloudOps~Z` is owner of record; acceptance is its act, by task order | @fa8ec0e726, call closed |
| Codex `~Z*` seat-home deadlock (dell1 pass, 32524) | AGENTS.md:48 admits a mission-tree order whose `<issued_to>` names the full serial | @a55888e3a2 |
| NFRA_OPALAI closer candidate | no closer now | msg to COO~AI |
| MCPINDEX fresh lane | `0.7.0_AE_CloudOps~MX` | seated by MSTR~Z |
| COMM_ASSIST lane | `2.0.0_SA_COO~ZZ` | @c4dea02951 |
| bbg-teams-assist pin (BG 32499) | pin by the opalbloomberg oid; Andrew's tokens carry a different oid | @16fb949b5b |

## Never-widen halves signed

AMGT_HARVST bq-2 @dccc0f2865; OG-da-1 @93ddbb1288; AMGT_RESAPP gg-1 @83b31c3fa9; MDPF_DEMQUE DQ-t14 @3607c76017 (acts DONE by ~ZQ; this seat
decoded the live task: shared tree, SKIP on a missing day); OG-bh-1 @e9bda7b982.

## Acts only Andrew can do (cited)

- G-MSPID, the MSP calling identity and its MFA sign-in (NFRA_MCPMSP decomp G-MSPID/G-MSPCL; his "Not yet" 2026-09-30, "doesnt matter
  right now" 2026-10-01). Nothing asks him again.

## Observations

- `OPAL_BBGTML_daily_pull` LastTaskResult on 2026-10-08 was **50**, not 0 (Get-ScheduledTask). Named in the DQ-t14 half; owner the BG seat.
- `prd-manifest-gate` read a `FWD-13 RETIRED` line as a live definition; the retired lines were reworded `[retired] FWD-n`.
- My own over-reach, corrected: a 5-recipient send that told four Tier-2 Codex lanes to act was refused by LD-0529; the issuers carry it.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `directives-check --json`, project-JSON census | PASS | 9 SITEZ-placed of 448; the directive device field over-matched D2 (its placement prose names sitez) |
| `sequence-check --project` x8 | PASS | no flags; slow (~2 min for 8, backgrounded) |
| `prd-manifest-gate`, `prd-signoff status` | WORKED AS BUILT | refused a header/section disagreement; WITHHELD then ADMITTED |
| `missions-tree-index derive --write` | PASS | 3 row regenerations |
| `open-calls.py close` | PASS | |
| `git archive` + pytest | PARTIAL | bq-2 12/12 and gg-1 27/27; the full harvest suite needs repo-relative files |
| live AWS reads | PASS | bucket notifications, prefix count, authorizer source |
| a JSON re-dump of a project row | FAILED | rewrote 110 lines of formatting; reverted and edited by bytes |

-- 1.0.0_SA_CTO~Z
