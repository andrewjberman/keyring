# NFRA_MCPINDEX -- ROUND 6 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-02 ~01:1xZ

**L10 on `3.0.0_SA_CVO~O`'s slug** (msg 28124).
- The slug: `REMEDIATION_v5.md` @75c751b6c6. Compiled by `ADJUDICATION_v6.md` Z-C-S36/S37 and the Z-C-S39 addendum;
  graded by Z-C-S38.
- 6 of 6 orders are terminal and the channel holds 0 undispositioned rows.
- Grade tokens: `REALIZED | NOT_REALIZED | DEFERRED | HELD`.

**Written under** `/self-drive OPALAI_MCP_SITEZ` (arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d).
**Issuer: `2.0.0_SA_COO~MI`.** The recut is ONE issuance (section 5), under the next free round label.

**Priority this analysis applies** (Andrew-direct ~17:4xZ 2026-10-01 to `4.0.0_SA_CRO~O`, msg 28000): *MCPINDEX and
Opal-employee MCP use* first; the partner rollout is downstream; G-MSPID "doesnt matter right now".

---

## 1. What round 6 did

Packet: `round6/L8_PACKET_ROUND6.md` @235653342a. MX-s-16 closed on its scheduled run (msg 28123, drained
@e24ef2b9d0, ledger `nfra-mcpindex-r6-bd-merge-retire` CLOSED 8/8).

**L7, 6 of 6 terminal:**

| order | what landed |
|---|---|
| MX-d-6 | Discover reads `silver_datasets`; Schwab catalog rows; the reachability grade. AC2 routed 24 of 27 and AC3 reached 10 of 10. A1 is fail-closed: a firm-scoped silver row serves OPAL_INTERNAL only. |
| MX-g-3 | G-RDR: `unrouted=0`. |
| MX-r-8 | The slot-4 release, **LIVE `e3567ce5f7` since 2026-10-01T12:36:17Z**. Ledger 5/5. |
| MX-v-7 | The thread re-run. Served 63.43 equals the source 63.43 by VersionId `Qp7FdHII...`, as_of 2026-09-29. |
| MX-x-4 | Batch repair: the deploy wrapper's UTF-8 manifest rewrite, the session-resolved halt-gate serial, the channel resolver and the emitter arguments. |
| MX-s-16 | One BD writer for **unrealized and allocations**. Realized and transactions are HELD (Z-W24-S2/S4). The scheduled run at 00:14:54Z read unrealized `failures=0 empty_stub=6`, so Z-S72 is REMEDIATED. |

**L8:** 20 rows dismissed (Z-C-S36), 7 graduated (Z-C-S37), and the Z-S76 addendum (Z-C-S39). Adopted as stated,
including the CVO's correction that the stale merge script still runs for realized and transactions (Z-W24-S3).

**L9 (Z-C-S38):**
- **MXV7-J1 PASS.** The route and the figure were measured independently by the CVO and by the cell. This reverses
  round 5's r7.J1 FAIL.
- **MXV7-J2 (r6.J1) NOT_EVALUATED.** Alyssa's cold run has not happened. Its prerequisite is now served.

## 2. Outcome grades

| FWD | grade | why (artifacts) |
|---|---|---|
| FWD-1 (discover routes a cold question to the right tool) | **HELD** on r6.J1 | Every author-side measurement is MET. Live through a principal session, BD fees routes to `blackdiamond_list_fees`, Schwab positions to `schwab_query`, and ETF positioning to `etfs_get_positioning` (packet section 2; Z-C-S35). MX-d-6 routed 24 of 27 and reached 10 of 10. What remains is the outcome's own instrument: a cold run by a non-author. That is a person by Andrew's word (A6), which makes it the one essential wait. |
| FWD-2 (portal figures equal the portal's) | NOT_REALIZED | Unchanged from round 5. `platinum/advi` is HELD on G-W (MX-t-12 CANCELLED). Not re-graded. |
| FWD-3 (Schwab) | **HELD** on r6.J1 | The tools are live and routed (MX-r-6, MX-d-6, live read by the CVO). The cold run is the remaining grader. |
| FWD-4 (custodian and platform tools) | NOT_REALIZED | **Black Diamond is MET**: J1 PASS, route plus figure plus as-of against the source by VersionId. Orion, Eclipse and SmartX are not started (section 5, item 4). |
| FWD-5 (ETF tools) | NOT_REALIZED | Unchanged. Holdings, net assets and daily NAV per fund are not all answered by a purpose-built tool. |
| FWD-6..FWD-10 | DEFERRED | Nothing in round 6 moved them. |

**Round tally: 0 REALIZED, 3 NOT_REALIZED, 2 HELD, 5 DEFERRED.** Round 6 closed the round-5 defect (the discover
reader) and the BD thread now passes end to end. FWD-1 and FWD-3 wait on ONE sitting with Alyssa, booked through
`0.0.0_AB_MSTR~Z` for Andrew. MCPORTAL's G-CLOSE is staged into the same sitting.

## 3. Rulings on the slug's rows

### 3a. Rows owned by `1.0.0_SA_CTO~O`

| row | ruling | reason |
|---|---|---|
| **Z-W24-S4** (the sentinel writer refuses a legitimately empty PERIOD window, so BRONZE_COMPLETE is never written on 9 of 29 days) | **Fix it in the BD runner's OWN sentinel check, never in the shared script under `data/cot/`.** For the transactions PERIOD table only, the check accepts a MEASURED `has_data_rows=0` sidecar. The runner prints `OK: bronze sentinel emitted` only after a `head_object` on the sentinel key reads it back. Negative controls: (i) a snapshot table with 0 rows still withholds the sentinel; (ii) `data/cot/` is byte-unchanged (a `git diff --quiet` arm). | cot is a separate firm from bd (CLAUDE.md rule 13), so a fix scoped to the BD runner leaves cot unchanged by construction rather than by a test. The false `OK` is a value without its claim; a read-back is the claim. |
| **Z-S74** (the freshness gate does not block production dispatch; weekly tables are graded on a 48h daily threshold) | **(1) The basis is RULED now.** `allocations` and `unrealized` are weekly producers, so their entries take `freshness_basis: trading-day-frontier` at a WEEKLY cadence: stale only when the last write predates the most recent scheduled weekly production day per `lib/trading_calendar.py`. Daily tables keep their basis. **(2) The skip path is MEASURED, not changed.** A read-only cell names which of the three paths production takes (PATH, bypass flag, or bd config skipped), with the code line and one scheduled run's log. **(3) No change to whether the gate blocks this round.** | Making the gold dispatch block moves served output: a NEVER-1 act with its own sign-off, and it is not needed to retire the transactions document once the sentinel fix lands. The basis fix stops a false alarm and changes no dispatch. |
| **Z-W22-S1** (no firm field on `silver_datasets`, so firm principals cannot discover their own rows) | **DEFERRED, with A1 fail-closed kept.** | Firm principals are the partner rollout, which Andrew placed downstream (msg 28000). Today A1 shows silver rows only to OPAL_INTERNAL, which is the safe direction. The C1 schema change (a ratified-text change, re-signed by the CVO) enters with the partner rollout's first round. |
| **Z-W23-S2** (the halt gate's recipient-scoping test is red: it identifies the gate through the retired `.agent_context`) | **Round-7 batch cell.** Repair the fixture to declare a session serial file. | MX-x-4 moved the gate to a session-resolved serial in THIS project, so its test fixture is this project's to follow. |

### 3b. Rows owned by `2.0.0_SA_COO~MI`

| row | ruling |
|---|---|
| **Z-W24-S3** (realized and transactions documents v3 still run `scripts/merge-daily-incremental.py`, so 2 code versions write each table) | **Disarm FIRST, this round, before the sentinel fix:** point both HELD documents' merge step at `code/silver/`, the script `bd-silver-merge` runs. Disarm read: both documents' Default content names no `scripts/` path. **Then retire** both merge steps with the sentinel fix (item 1). Criterion: a writer census reads 1 writer per BD silver table, 4 of 4. |
| **Z-W24-S8** (transactions retirement HELD on the freshness-gate premise) | The premise is contradicted by Z-S74's measurement and the dependency is replaced: transactions retires on the sentinel fix (item 1). The skip-path read (item 2) is evidence, not a precondition. |

### 3c. Rows carried from REMEDIATION_v4 (for the CVO to re-grade or close at the next compile)

| row | ruling |
|---|---|
| Z-W20-S3 (MX-t-12) | **CLOSE.** MX-t-12 is `cancelled` per the round-5 analysis section 3. Nothing remains to remediate. |
| Z-W15-S3 (`platinum/etfs` uncertified) | **CLOSE.** Certified by MX-d-6 AC3 reachability (10 of 10, ETF positioning routing to `etfs_get_positioning`). |
| Z-W19-S22 (NEVER-2 sentinel outside `<paths>`) | **CLOSE.** Deliberate: `.owned-paths.yaml:1818` (round-5 ruling). |
| Z-W21-S23, Z-S57, Z-W21-S7 (tooling) | **Re-grade against MX-x-4** (x4.AC1 8 passed, AC2 3 arms, AC3 10 passed). Close any row that MX-x-4's criteria exercised. |
| Z-S69 (two merge paths) | Resolved for unrealized and allocations by MX-s-16. Closes with Z-W24-S3 at 4 of 4. |
| Z-W21-S15 (suite red: 13 tests) | 2 tests are MCPINDEX's (`test_schwab_host_inputs`, `test_mx_s15_dataset_registered`): round-7 batch cell. 9 are NFRA_OPLGTW's and 2 are NFRA_OPALAI's, routed to those issuers with the packet's section-4 table. |
| Z-W21-S12 (BD ExternalId option A) | **DEFERRED to this project's next own gateway release.** Round 7 carries no gateway change, and a release for this alone is not proportionate. The `.env` copy is a held secret on a host only CloudOps reads. |
| Z-W21-S19, Z-W19-S13 | NFRA_OPLGTW's (round-5 ruling), now joined by ETFS_RIVALS-W5-S3 (MSTR~Z register @44ed4dbcc3). |

## 4. No release this round

Round 7 changes no gateway code. Items 1 and 3 touch BD pipeline infrastructure: Lambda, SSM documents and
freshness config, each through Terraform and never `update-function-code`. Each WORLD act carries its NEVER-2 ledger.
The document repoint and the retirement each carry never-widen halves (CTO + COO) that name per-table rollback.

## 5. THE ENRICHMENT LIST ROUND 7 CUTS (one issuance, `2.0.0_SA_COO~MI`)

1. **One BD writer for realized and transactions** (Z-W24-S3, S4, S8; Z-S69). WORLD, one chain:
   - (a) repoint both HELD documents' merge step to `code/silver/`; disarm read as in 3b;
   - (b) the sentinel fix in the BD runner per 3a, with both negative controls;
   - (c) retire both documents' merge step.

   Criteria:
   - (i) `has_data_rows=0` on a transactions window yields a sentinel and the runner's `OK` line follows a
     `head_object` read;
   - (ii) a 0-row snapshot table still withholds;
   - (iii) `data/cot/` is unchanged;
   - (iv) the writer census reads 4 of 4 tables with 1 writer;
   - (v) acceptance is the next scheduled `bd-silver-merge` run after a Mon/Tue empty window, reading failures=0
     with the partition landing the same evening.
2. **Z-S74:**
   - (a) READ-ONLY (LOCAL): name the gold chain's skip path, with its code line and one scheduled run's log;
   - (b) the weekly basis for `allocations` and `unrealized` per 3a.

   Criterion: the freshness reader grades both tables FRESH on a day the weekly producer has run and STALE only past
   the next scheduled weekly production day. The positive control is a date one week past the last write.
3. **Opal-employee use, the one essential wait:** r6.J1, Alyssa's cold run, graded at L9 by `3.0.0_SA_CVO~O` against
   A5. Booked through `0.0.0_AB_MSTR~Z` for Andrew, in the same sitting as MCPORTAL's G-CLOSE. The grader's notes
   (Z-C-S38) travel with it:
   - discover's silver freshness names the field only, so the as-of comes from the tool;
   - the asker must resolve OPAL_INTERNAL.
4. **FWD-4 coverage, measure before build** (LOCAL, one cell): for Orion, Eclipse and SmartX, a census of served
   silver data and catalog rows. For each: dataset keys, newest partition and as-of, the row count, and whether a
   catalog row exists. Tools are cut in round 8 only where data is served (the build ladder: no tool over absent
   data). Denominator printed per platform.
5. **Batch repair cell at the drain:**
   - the 2 stale MCPINDEX tests (Z-W21-S15);
   - the halt-gate scoping fixture (Z-W23-S2);
   - proof-of-spec-check flagging a re-committed instance that still carries PENDING rows (packet section 6.5);
   - the cp1252 SSM-output trap behind Z-S75's empty read.

**Stated dependencies, not cells:**
- r6.J1 waits on Alyssa (a person, by Andrew's word).
- Z-W21-S19, Z-W19-S13 and ETFS_RIVALS-W5-S3 are NFRA_OPLGTW's.
- `platinum/advi` waits on G-W.
- Z-W22-S1 and Z-W21-S12 are DEFERRED as ruled.
- FWD-6..FWD-10 enter after item 4 measures.

## 6. The D9 -> D6 move

Andrew agreed the move to D6 at this project's round close (~15:51Z, record @53ad7cb452; CVO verdict 27494
@058a71c713). This analysis is that round close.
- **This seat lands it as ONE commit BEFORE the round-7 issuance:** the `DIRECTIVES.yaml` members line, the tree
  path, the UNPINNED live references, and a redirect README at the old root. Pinned `@<sha>` citations are not
  rewritten.
- The laptop row-owner removes the D9 row.
- `2.0.0_SA_COO~MI` issues round 7 into the D6 tree. The issuer waits for this seat's move-commit message before
  cutting.

## 7. What this analysis does not do

- It deploys, applies and flips nothing. The row closes in 3c are the CVO's at the next compile.
- It re-measured nothing. Every figure is the slug's, the packet's, the CVO's grade record or the investigation
  rows', as cited.
