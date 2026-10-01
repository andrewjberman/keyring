# NFRA_MCPINDEX -- ROUND 5 ANALYSIS (L10, rounds 4+5), `1.0.0_SA_CTO~O`, 2026-10-01 ~08:4xZ

**L10 on `3.0.0_SA_CVO~O`'s slug** (msg 27655; `REMEDIATION_v4.md` @3ff13b945f, grades `ADJUDICATION_v5.md` Z-C-S34).
The fold reads 0 of 206 undispositioned. Grade tokens: `REALIZED | NOT_REALIZED | DEFERRED | HELD`.
**Written under** `/self-drive OPALAI_MCP_SITEZ` (arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_04xxZ_SELF_DRIVE_OPALAI_MCP_SITEZ.md` @80102ed73d).

**Issuer: `2.0.0_SA_COO~MI`.** The recut is ONE issuance (section 5). The round-6 label is the next free one.

---

## 1. What rounds 4+5 did

- **L7:** 8 of 9 orders terminal, issuer-graded on CLOUD (packet `round5/L8_PACKET_ROUND5.md` @81887e8ae8).
  - MX-a-8: the Black Diamond analysis.
  - MX-s-15: Schwab `dim_transaction`.
  - MX-q-3: the `gateway_query_catalog` tool.
  - MX-t-13: `blackdiamond_list_fees`.
  - MX-t-10: `etfs_get_positioning`.
  - MX-s-14: the BD Playwright strip; ledger closed 9/9.
  - MX-r-6: the Schwab enable release, live since 2026-09-30T18:33Z.
  - **MX-r-7: the BD + ETF release, LIVE since 2026-10-01T07:13:52Z at `05e3eff563`.** It was slot 1 of the
    opal-gateway release train. Its ledger closed 7/7, with the CTO half @adcbe6b693; tools went 58 -> 60.
  - MX-t-12 is HELD (Z-S67); ruled in section 3.
- **L8:** 12 rows graduated OPEN (Z-C-S33). Adopted as stated.
- **L9 (Z-C-S34):**
  - **a8.J1 PASS** with limits.
  - **r7.J1 FAIL.** The route clause is UNMET: live discover reads `catalogued=false` for the BD fees question. The
    VersionId figure check was not performed.
  - **r6.J1 NOT_EVALUATED.** Alyssa's cold run has not run, and would fail its Schwab clause by construction until
    Z-W21-S22 lands.

## 2. Outcome grades

| FWD | grade | why (artifacts) |
|---|---|---|
| FWD-1 (discover routes a cold question to the right tool) | NOT_REALIZED | Measured MET for one row: the CVO's live discover routes "ETF positioning" to `etfs_get_positioning`. UNMET for BD and Schwab: `opal_discover` never reads `silver_datasets`, where the BD row sits, and Schwab has no catalog row at all (Z-W21-S22, re-measured live ~08:1xZ). The cold run by a non-author has not run. |
| FWD-2 (portal figures equal the portal's) | NOT_REALIZED | `platinum/mdpf` was EQUAL in round 3, and `platinum/etfs` now has a purpose-built tool. Not re-graded this round. `platinum/advi`: its tool (MX-t-12) is CANCELLED here, so that surface is HELD on G-W (section 3). |
| FWD-3 (Schwab) | NOT_REALIZED | The tools are live (MX-r-6) and r6.AC1/AC2 PASS on 05e3eff563. The cold run (r6.J1) waits on (i) the Z-W21-S22 repair, then (ii) Alyssa, a person by Andrew's word (A6). |
| FWD-4 (custodian and platform tools) | NOT_REALIZED | BD: `blackdiamond_list_fees` is live, and its in-process call is ok (as_of 2026-09-29). r7.J1 FAILS on the route clause. Orion, Eclipse and SmartX are not started. |
| FWD-5 (ETF tools) | NOT_REALIZED | `etfs_get_positioning` is live and routed. Holdings, net assets and daily NAV per fund are not all answered by a purpose-built tool, and no ETF judgment criterion has been graded. |
| FWD-6..FWD-10 | DEFERRED | Nothing in rounds 4+5 moved them. |

**Round tally: 0 REALIZED, 5 NOT_REALIZED, 5 DEFERRED.** Rounds 4+5 put three new tool families on the live gateway.
What stands between "live" and "realized" is now ONE defect, the discover reader, plus G-RDR. Both fit one release.

## 3. Rulings on the decisions the slug hands this seat (7 rows owned by `1.0.0_SA_CTO~O`)

| row | ruling | reason |
|---|---|---|
| **Z-W21-S22** (discover never reads `silver_datasets`; Schwab has no row) | **Fix the READER, not the row.** `opal_discover` reads the `silver_datasets` section beside the existing sections. Schwab gets catalog rows for its served datasets. Reachability, not presence, is the grade for every catalog row from now on (section 5, item 1). | `silver_datasets` is where silver rows belong. Moving one row would leave the next silver row unreachable. MX-t-13's AC passed on PRESENCE in a section no reader consumes; a catalog AC that does not run discover cannot fail. |
| **Z-W20-S3** (MX-t-12, advi) | **CANCELLED.** Pointer: this ruling. The issuer flips the status, naming this file. | A tool over a frozen twin (publisher disabled since 2026-08-21) cannot meet FWD-2 parity. Its literals need an R20 entry Andrew has not given (G-W "NOT YET"). The `platinum/advi` surface re-enters only as a NEW cell on the advisor page's LIVE source, after Andrew's R20 acknowledgement. FWD-2's advi surface is HELD on G-W. |
| **Z-W21-S19** (CLOUD opal-gateway TF root does not render under safe-apply) | **Placed with NFRA_OPLGTW** (`2.0.0_SA_COO~O`, owner of the root). Its next enrichment carries a hygiene cell: re-measure first (OG-pr-1 has since created the three `gateway/*` secrets); then every data source of an unapplied file is applied in its train slot or gated; acceptance is a plan on the committed root with 0 errors and no pruned copy. | The root is OPLGTW's, and the train's acts #2b and #3 need it. Not cut into this project. |
| **Z-W19-S13** (NFRA_OPLGTW_CONTRACT.json in three copies) | **Placed with NFRA_OPLGTW.** `org/standards/NFRA_OPLGTW_CONTRACT.json` is the single source. The release suite fails when the gateway's `deploy/` copy or the grant-writer Lambda's bundled copy differs from it. The release removes a host `deploy/` file the artifact no longer carries. | One writer per property. A tar extract never deletes, so a stale host copy outlives its rollback. |
| **Z-W21-S23** (safe-ec2-deploy.sh mojibake + halt-gate serial) | **Round-6 tooling cell** (section 5, item 6). The manifest rewrite reads and writes UTF-8 through a JSON parser, never `jq \| tr` through cp1252. The halt gate resolves the serial from the session, not the tree. | Twice measured (e159e023f0, da1f54bfda). The deploy wrapper is shared tooling, and this project's releases are its heaviest users. |
| **Z-W15-S3** (the authored `platinum/etfs` row serves uncertified) | **Certify it by the reachability grade**, folded into item 1. A live discover names `etfs_get_positioning`, and one figure plus as-of equal the served object read by VersionId. | For a routing row, "certified" means it routes to a tool that answers truly; the same check covers every row item 1 adds. |
| **Z-W19-S22** (a NEVER-2 sentinel outside MX-r-6's `<paths>` was admitted) | **Deliberate, recorded: no gap.** `.owned-paths.yaml:1818` grants `org/critical_paths/**` to lane ANY ("entries are written STRUCTURALLY by the mechanism that fires under the committing agent's author"). | Read at HEAD; the validator behaved as configured. |

Rows owned by `2.0.0_SA_COO~MI` (Z-W21-S12, Z-S69, Z-W21-S15, Z-S57, Z-W21-S7) are cut in section 5. Rulings this seat
adds to them:
- **Z-S69:** `bd-silver-merge` stays the writer of record. The documents' merge step is retired, so each BD table
  has 1 writer.
- **Z-W21-S15:** MX-t-10's catalogued ETF row is the later, Andrew-acknowledged state (R20 X11), so MX-d-5's
  "NOT catalogued" assertion is retired, not the row.

## 4. The release this round needs

One narrow MCPINDEX gateway release, the **G-RDR release at slot 4 of the train**
(`CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md` @cf5989190d R1), carries items 1-3. It cuts on OG-rl-1's live ref,
or on MS-d-2's if OG-rl-1 has not landed. The C1-C6 surface rules bind it, along with the CTO + COO never-widen halves
and G-A. **Alyssa's r6.J1 cold run is scheduled AFTER this release serves**, never before (the CVO's note 1).

## 5. THE ENRICHMENT LIST ROUND 6 CUTS (one issuance, `2.0.0_SA_COO~MI`)

1. **Discover reads `silver_datasets`; Schwab catalog rows; the reachability grade** (Z-W21-S22, Z-W15-S3). Criteria:
   - (a) in-process on the release tree, `opal_discover` names `blackdiamond_list_fees` for "what fees did Black
     Diamond charge", and names the Schwab tool for "Schwab positions" (and for each Schwab row added);
   - (b) "ETF positioning" still names `etfs_get_positioning`, and the MX-v-6 harness does not fall below its last
     count;
   - (c) every catalog row added or touched is graded by a discover call naming its tool, never by presence.
2. **G-RDR:** route `portal_index` and `opal_discover` through `INTERNAL_READER_ROLE_ARN` (ruling 27413; train R7).
   Criterion: `e1z.AC1.sh` on the release tree reads `unrouted=0`.
3. **The slot-4 release (WORLD)** carrying 1 and 2, and BD ExternalId option A if the issuer folds it (Z-W21-S12; a
   runtime secret read retires the `.env` copy). Never-widen halves CTO + COO; G-A. Read-back:
   - (a) live discover equals 1(a) and 1(b) through a principal session whose tool list postdates the release;
   - (b) `.env` keys printed before and after, nothing lost;
   - (c) host equals the artifact.
4. **The thread re-run (WORLD, after 3 serves)**, and **r7.J1 re-graded at L9 by `3.0.0_SA_CVO~O`**: the route
   discover gave names `blackdiamond_list_fees`, and the figure and as-of equal the source object read by VersionId.
   Denominator printed. Then **r6.J1**, Alyssa's cold run, graded against A5. This is the round's one essential wait
   (a person is the instrument, by Andrew's word).
5. **Hygiene cell at the drain** (Z-W21-S15): the gateway suite goes green, or each remaining red test is named with
   its owner. The MX-d-5 assertion is retired per section 3.
6. **Tooling cell** (Z-W21-S23, Z-S57, Z-W21-S7):
   - the deploy wrapper's UTF-8 manifest rewrite and session-resolved halt-gate serial;
   - the channel resolver parses JSON blocks instead of matching a key order;
   - the catalog emitter takes its inputs as declared arguments and refuses, never rewrites, when the census is
     absent.
7. **BD merge path** (Z-S69): retire the Playwright documents' merge step. Criterion: a writer census reads 1 writer
   per BD silver table.

**Stated dependencies, not cells:**
- Slot 4 follows OG-rl-1 (train R1).
- Z-W21-S19 and Z-W19-S13 are NFRA_OPLGTW's.
- `platinum/advi` waits on Andrew's R20 word (G-W).
- FWD-6..FWD-10 enter no earlier than round 7.

## 6. What this analysis does not do

- It deploys, applies and flips nothing. MX-t-12's `cancelled` flip is the issuer's, citing this file.
- It re-measured only the `.owned-paths.yaml` grant (`:1818`). Every other figure is the slug's, the packet's or the
  worker's, as cited, or this seat's own MX-r-7 sign-off reads (@adcbe6b693).
