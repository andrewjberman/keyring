# Gateway finish plan -- every contracted table on a typed tool, indexed and legibly displayed, by EOD Friday 2026-10-16

**archetype:** COORDINATE

- **Author:** 4.0.0_SA_CRO~Z, 2026-10-15 ~19:0xZ. Analysis for 1.0.0_SA_CTO~Z to fold into NFRA_MCPINDEX, NFRA_OPLGTW and
  NFRA_MCPORTAL.
- **Builds on:**
  - the census `GATEWAY_DATA_CONTRACTS_20261014/` (308 contracts);
  - the CTO directive `CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` @06ae2a3485;
  - OPLGTW PRD v3.11, MCPINDEX v0.16, MCPORTAL v0.8.
- **Measured:** 2026-10-15 ~18:3xZ-19:0xZ (catalog at HEAD, the three projects' order files, the broker's live roster).

## Andrew-direct, verbatim (site Z session of 4.0.0_SA_CRO~Z, 2026-10-15 ~18:4xZ)

> "Yes I want to make sure that we have a very clean and tight process to get this completely done by end of day tomororw.
> We have the compute necessary to handle it on this box and it's not complicated work. Here is what it looks like: COO~MI
> focuses on getting those data contracts indexed in MCP channels. This should include everything in opal-data-harvest,
> every vendor/firm combo in opal-data-assets, opal-data-etfs using whatever we use for the monthly
> reconciliation/accounting, wherever the served rivalfunds outputs live, opal-data-portal-v2 for whatever is served to
> the portal not including advisor intelligence and investor reporting surfaces. We need to push through this
> aggressively so we may want to have 2 COOs ~MI and ~MI2 and they split that workload. While this is happening, we have
> COO~O handle whatever opalgateway server infrastructure needs to be done to accomodate and managing entitlements/access,
> through NFRA_OPLGTW. While this is happening we have COO~MP there doing passes on the /gateway page of the
> mcp.opalinvest.dev making sure everything is extremely legible, clean, and well-designed, using the opalinvest.com website
> design fixtures, as well as making sure that everything is readable by human eyes and not wrapped or squished on text and
> segments. The most important thing is really that each displayed tool segment is very clearly segmented, i recommend this
> being by bucket, and in the case of opal-data-assets, by client/vendor pairs. I want to figure out how we pull any
> possible parallelization lever to get this done, so keep that in mind as you put together your analysis."

## GO -- Andrew-direct, verbatim (same session, 2026-10-15 ~19:2xZ)

> "We have usage, run it now"

This clears section 6's usage-limit risk and section 7's ask 4. The plan runs now: 4.0.0_SA_CRO~Z relayed the GO to
0.0.0_AB_MSTR~Z, 1.0.0_SA_CTO~Z, 2.0.0_SA_COO~MI, 2.0.0_SA_COO~O and 2.0.0_SA_COO~MP.

## 1. Done means (one finish line, three checks, all by 2026-10-16 ~22:00Z)

1. **INDEXED:** every in-scope table has a catalog row that carries `bucket`, and for opal-data-assets also `vendor` and
   `firm`, plus a `read_tool`. opal_describe / opal_discover return it by plain words.
2. **SERVED:** each row's `read_tool` is live on the gateway and answers one real Opal principal's driven call. Client-data
   tools are admitted by the firm's data grant only (OPLGTW v3.1 Ruling 2 / v3.2).
3. **LEGIBLE:** `/gateway` on mcp.opalinvest.dev shows the tools segmented by bucket, with opal-data-assets segmented by
   vendor/firm pair, in the opalinvest.com design fixtures, with no wrapped or squished text. It is checked by one rendered
   screenshot per segment at desktop and narrow widths.

## 2. Scope, measured against the catalog at HEAD (catalog v0.5, built at eb80f77d65)

| bucket (Andrew's list) | in scope | catalog rows today | typed tools today |
|---|---|---|---|
| opal-data-harvest | everything (gold, silver, Bloomberg bronze; plumbing stays on harvest_read) | 78 | LIVE (OG-ap-18) |
| opal-data-assets | every vendor/firm pair | 111, among them Schwab 08242234 / 08335338 / 08403355 (15 / 16 / 14), BD cottonwood 14, smartx/platform 13, commonwealth/cottonwood 12, BD 49f 4 + 49financial 3, orion/inflection 4 + 4698 1, eclipse/inflection 4, Tax SMA gateway/global 1; plus opal-data-bd 8 (live 49F BD, OPLGTW v3.6) | BUILDING: OG-cl-1..6 (workers 103-108) |
| opal-data-etfs | the monthly reconciliation set: daily/{partner} ownership slices, config/etf_universe.json, platinum/reports, platinum/etf_ownership_dashboard.json (the inputs and outputs of etfs-reports-orchestrator, G5) | 36 in all, 14 of them rivalfunds/ | wave A LIVE (OG-ap-20) |
| rival funds served outputs | rivalfunds/etfs/gold/* + platinum/page manifest (G5r) | the 14 rivalfunds/ rows | PENDING: OG-ap-22 |
| opal-data-portal-v2 | served to the portal, EXCLUDING advisor intelligence and investor reporting | 41, of which 3 touch advi/irpt and come OUT (2 platinum/advi/49financial rows, 1 mdpf row to re-check) | LIVE (OG-ap-19, G3) |

Out of scope by Andrew's word: advisor intelligence and investor reporting surfaces, M365, YCharts, the Kuzu graph.

## 3. The three tracks (disjoint write surfaces, so they run at once)

| track | owner | writes | does | depends on |
|---|---|---|---|---|
| **A-assets** | `2.0.0_SA_COO~MI` (NFRA_MCPINDEX, workstream ASSETS) | the opal-data-assets and opal-data-bd source files under `workflows/atom_decomposition/catalog_entries/` | adds `bucket` / `vendor` / `firm` / `read_tool` to every client row; links each row to its `client_*` tool as OG-cl-* lands | contract C-GROUP (below) |
| **A-research** | `2.0.0_SA_COO~MI2` (NEW seat; NFRA_MCPINDEX, workstream RESEARCH) | the harvest_, etfs/rivalfunds and portal source files under the same folder (disjoint file sets) | the same fields for harvest, ETF reconciliation, rival funds and portal-v2; drops the 3 advi/irpt rows | C-GROUP |
| **B-serve** | `2.0.0_SA_COO~O` (NFRA_OPLGTW) | gateway app + IAM/Terraform | lands OG-cl-1..6 and OG-gp-1 / OG-gf-1, then the releases (ap-17, ap-21, ap-22, the G2 release) and the firm data grants | appliers (lever 1) |
| **C-display** | `2.0.0_SA_COO~MP` (NFRA_MCPORTAL, workstream PE) | the mcportal `/gateway` view | segments by `bucket`, then by `vendor`/`firm` for opal-data-assets; opalinvest.com fixtures; no wrapping | C-GROUP (builds against a fixture until the catalog carries it) |

**The one coupling is CONTRACT C-GROUP, cut FIRST (one hour, by 1.0.0_SA_CTO~Z):**
- every catalog row carries `bucket` (always);
- opal-data-assets and opal-data-bd rows also carry `vendor` (schwab | blackdiamond | orion | eclipse | smartx | commonwealth | gateway) and `firm` (49financial | cottonwood | inflection | `multi` for SmartX and Tax SMA, whose objects mix firms, Z-S109);
- the `/gateway` view groups on exactly those fields.

Measured today: silver rows carry no bucket / vendor / firm field (their keys are entity, business_meaning, ..., read_tool, nl_tags). Without the contract, the display track has nothing to segment on, and the two index COOs would invent two spellings.

## 4. Parallelization levers, ranked by hours saved

1. **Unblock the applier queue.** Measured: ap-17, ap-21, ap-22, mg-1 and eg-3 are all issued to `0.7.0_AE_CloudOps~Z`, while ~MQ, ~ZQ, ~ZS and ~ZW are IDLE.
   - Gateway code releases share one host and must stay one-at-a-time ("one actor per host"). So BATCH them: one release carries every code cell that is ready (cl-*, gp-1, gf-1, ap-22's rival tools) instead of five sequential one-file releases.
   - IAM/Terraform grants (the firm data grants, the rival-funds grant) are a different surface. Put them on a SECOND applier (~ZW or ~ZS) in parallel with the code release.
   - Catalog releases (MX-r-*) are a third surface, on `0.7.0_AE_CloudOps~MI`.
   - Result: three appliers on three surfaces, never two on the same host at once.
2. **Seat `2.0.0_SA_COO~MI2` now** (MSTR spawn) on the RESEARCH workstream. Two issuers on one project are legal with disjoint workstreams and disjoint files (CLAUDE.md rule 27), and the catalog's per-entity source files make the split conflict-free. Only the release cell runs the emitter.
3. **Cut C-GROUP before anything else,** so C-display starts on a fixture at hour 0 instead of waiting for the catalog.
4. **Fan out workers to the cap (8 per COO).** Index work is per-file and mechanical: one worker per vendor/firm pair on A-assets (about 9 pairs) and one per bucket on A-research (4). Both batch into one catalog release per COO per half-day.
5. **Proportionate sign-off.** Every change here is CONTRACTS-side under existing outcomes (FWD-22 in both PRDs), so no ENDPOINT moves and no half re-opens. The CTO writes ONE addendum per project now, and later group lists ride as enrichment.
6. **Keep the pipeline-defect cells off the critical path:** the 49f OOM (Z-S110), the Eclipse stall (Z-S111), the ETF canon fan-in (Z-S112), the Sept report coverage (Z-S113) and the rival coverage timing (Z-S124). Each tool states its freshness in trading days; the fixes run beside the work, not in front of it.

## 5. Critical path and a schedule (UTC)

| when | A-assets / A-research | B-serve | C-display |
|---|---|---|---|
| 10-15 19-21Z | C-GROUP cut; ~MI2 seated; workers fanned out per pair / bucket | ap-17/21 batch release on ~Z; firm grants on ~ZW | build segmentation on the C-GROUP fixture |
| 10-16 morning (until 14Z) | all rows carry C-GROUP; catalog release 1 | OG-cl-1..6 + gp-1 + gf-1 land; ONE G2 release; ap-22 rival release | render passes, desktop + narrow, per segment |
| 10-16 14-20Z | catalog release 2 (links to the live client_* tools); opal_discover checks per bucket | driven call per group (FWD-22 PROOF), negative arms (no-firm, two-firm, ambiguous last-4) | final pass on the live catalog; screenshots |
| 10-16 20-22Z | close | close | close |

The critical path is B-serve's G2 build and grant: six client cells, then one release, then firm grants. Levers 1 and 4 shorten exactly that path.

## 6. Risks that would move Friday

- **Usage limits:** 0.0.0_AB_MSTR~Z reports 6 QUIET seats as likely usage-limit freezes. More seats need headroom; the RESERVED usage-credits item at Andrew is the gate.
- **Firm grants are never-widen acts,** each with its CTO + COO halves. Pre-state the CTO half (as for OG-yr-1) so signing is not a queue.
- **SmartX and Tax SMA mix firms in one object** (Z-S109). Their tools filter rows in code, with a two-firm negative arm; that test must be in the cell, not after it.
- **Box health:** the site Z Python 3.14 outage today (an MSP patch). IT has been asked to exclude Python. Recurrence would halt every track.

## 7. Asks (each one act)

1. **[0.0.0_AB_MSTR~Z]** Spawn `2.0.0_SA_COO~MI2` on NFRA_MCPINDEX, workstream RESEARCH.
2. **[1.0.0_SA_CTO~Z]** Cut CONTRACT C-GROUP and one addendum per project (MCPINDEX: the two workstreams; OPLGTW: batch releases plus a second applier for grants; MCPORTAL: segmentation on C-GROUP).
3. **[2.0.0_SA_COO~O]** Re-issue the IAM/grant cells to an idle applier (~ZW or ~ZS); keep code releases on ~Z, batched.
4. **[Andrew]** Usage headroom for the added seats, if the freezes are limits.

-- 4.0.0_SA_CRO~Z
