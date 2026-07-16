# 0.4.0_DS_ClientPlatform~B -- eclipse endpoint census: Andrew conflation correction -> exercised census -> WP1 close instrument delivered (2026-07-16 15:00-16:19Z)

**archetype:** VALIDATE
**secondary_archetypes:** EXPLORE, COORDINATE

## Window

Since my 14:58Z log (holdlift_twin_unpause_wp1_adjudication_1245-1458Z.md; its 15:2xZ AMENDED
section @ 6a51e480f is part of THIS window's work).

## Work done

### 1. Andrew-direct correction (my terminal ~15:0xZ) -- recorded verbatim, broadcast same turn
"We already established that there is backfill for eclipse, and that we cannot conflate the
shape of our tool with the shape of the data eclipse offers and endpoint structure. Please talk
to CTO about it and revise the log. If there is confusion, then your task is investigating the
endpoint structure for Eclipse (which we should have laying around via the DATA_PLATFORM and
DATA_ANALYTICS projects)."
- Broadcast to [1.0.0_SA_CTO] 15:16:39Z with my read (the "current-state-only" premise described
  pull_eclipse_portfolios.py's 5 endpoints, not Eclipse's surface).
- Log revised per order: visible AMENDED section, follow-up commit 6a51e480f (no history rewrite).
- CTO FORMAL WORD 15:23:53Z: WP1 07-13..15 no-backfill disposition REOPENED; loss-~nil +
  weekend decomposition SURVIVE un-relitigated; my census = the WP1 close instrument; standard =
  records-MAP then EXERCISED value-discriminated probes on standing grants.

### 2. MAP phase (records)
- Local records enumerate only our tool's shape: endpoints/README.md = the 5 production calls;
  D3:27's own completeness basis concedes the surface was never censused ("NOT every endpoint
  Orion/Eclipse exposes"); DC2 briefs = the browser-crawl discovery path (heavier machinery,
  off-peak ROE -- not needed for REST probes); the 05-14 feasibility brief's HAR forensics
  (.runtmp/*.har) were NEVER ARCHIVED -- verified gone.
- **THE FIND: Eclipse's API catalog is PUBLIC.** https://api.orioneclipse.com/doc/ -- OpenAPI
  3.0.3, full spec embedded in /doc/swagger-ui-init.js (2.57MB). 493 paths / 56 groups incl.
  Audit_and_Logging (21 endpoints), Closed_Trades, Trade_Instances, Reports. The D3 "no vendor
  catalog" premise was an ORION CONNECT statement (ADVI_ORIAPI sec.1) carried onto Eclipse.
  Our productionized coverage: 5/493 = 1.0%.

### 3. EXERCISED census (6 probes ~16:0xZ, standing JWT SM orion/eclipse_jwt/current, 6/6 HTTP 200)
Discriminators extracted from bronze/eclipse/2026-07-16/portfolios_simple.json BEFORE probing:
changed set = 18 edited + 3 created = 21 (matches 074e2530b manifest count; IDs in evidence doc).
- P1 (+) auditlog/portfolio/2?fromDate=2026-07-10&toDate=2026-07-16 -> 1 row, Updated,
  editedOn 2026-07-13T18:10:24Z vs held 18:10:27Z (same edit action; snapshot holds last write).
- P2 (+) auditlog/portfolio/1419 -> 2 rows: Insert 2026-07-15T16:29:24Z + Updated 16:36:17Z --
  BYTE-MATCH to held createdOn/editedOn. Range param honored; cannot hide against this.
- N1 (-) auditlog/portfolio/88 (in-roster, untouched since 2025-08-13; verified before probing)
  -> 0 rows. Separate invocation per Rule 22a.
- M1 (-) auditlog/model/3 in-window -> 0 rows. "Models static" upgraded to EXERCISED grade.
- T1 tradeorder/closedTrades?startDate=2026-07-13&endDate=2026-07-15 -> 2,937 rows w/
  point-in-time portfolio values (totalValue/managedValue at trade time); row 1 cross-ties
  portfolio 468 (one of the 21) to its 07-13T14:24:05Z manual rebalance.
- NOT offered: as-of/date param on /portfolio/portfolios* -- snapshot time-travel does NOT exist;
  the labeled-copies rejection stands.

### 4. Deliverables + findings routing
- Evidence doc ECLIPSE_ENDPOINT_CENSUS_WP1_CLOSE_20260716.md + slim probe artifact
  eclipse_audit_census_probes_20260716.json committed @ e8489fc78, pushed (gate-bearing: CTO
  close instrument; COO 15:52Z push-discipline binding item 1 honored -- raw 15.9MB probe body
  retained in session scratchpad only).
- Findings MCP: [1.0.0_SA_CTO] 16:16:38Z (verdict + rec FILLED-VIA-HISTORY-ARTIFACTS: one-shot
  window pull ~45 calls landed as new bronze history types bronze/eclipse/_history/*; on his GO
  I pull+land); FYI [0.7.0_AE_CloudOps] 16:16:56Z (manifest authorship + their twin >=-token fix
  confirmed permanently right -- no standard-shape 07-1{3,4,5}/ partitions should ever exist).
- Twin first-fire 15:45Z (0.7.0 16:07Z msg): alarmed on eclipse exact-token-vs-hole semantics;
  mechanism TRUE, posture sharpening is 0.7.0->CTO's; nothing mine; my lift stands.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-grep | DC2 (org/ docs/) | PASS | routed to the DC2 briefs + reverse-etl blueprint |
| comp-grep | orioneclipse | PASS | full estate reference sweep; surfaced the 05-14 feasibility brief (the HAR trail) |
| comp-glob | *DATA_ANALYTICS* | PASS | located the A1/A2 records (thin on eclipse -- portal-panel only) |

**What worked:** comp-grep's estate sweep found the feasibility brief whose section 9 named the
HARs -- the trail that led to checking for archives and then to the public catalog.
**What failed:** nothing; the probe harness authenticated first try on the standing JWT.
**Gap found:** the vendor-surface record class has no archival home -- .runtmp HARs died with the
scratch dir; proposed (in the evidence doc) that the public catalog pointer be folded into D3 +
domain docs so the record cannot rot this way again.

## Briefs Written (DS)

| Brief | Issued to | Purpose |
|---|---|---|
| ECLIPSE_ENDPOINT_CENSUS_WP1_CLOSE_20260716.md @ e8489fc78 | 1.0.0_SA_CTO (close instrument); FYI 0.7.0_AE_CloudOps | Exercised endpoint census: hole interior vendor-recoverable as EVENT HISTORY; rec FILLED-VIA-HISTORY-ARTIFACTS |

## MCP traffic

~9 total (excl. broker re-surfaces); significant: Andrew-verbatim broadcast -> CTO (15:16Z);
CTO formal REOPEN word (15:23Z, recv); COO push-discipline binding (15:52Z, recv; applied);
0.7.0 twin first-fire (16:07Z, recv; no action mine); census findings -> CTO (16:16Z) +
FYI -> 0.7.0 (16:16Z).

## Files Modified

See commit messages: 6a51e480f (log AMENDED section), e8489fc78 (census evidence doc + slim
probe artifact). Probe harness eclipse_audit_census_probe.py lives in session scratchpad
(not repo -- one-shot instrument; the evidence doc records its design + params).

## Blockers

None. WP1 disposition awaits [1.0.0_SA_CTO]'s ruling on the census evidence -- pending-input,
not blocked (the census WAS the asked-for close instrument; both fork outcomes are closes).

## Current State (zero-context reader)

- WP1 eclipse 07-13..15: REOPENED->CENSUSED. Evidence @ e8489fc78
  (org/tier2_senior/0.4.0_DS_ClientPlatform~B/deliverables/). Vendor surface: PUBLIC catalog
  api.orioneclipse.com/doc/ (493 paths); auditlog/portfolio+model honor fromDate/toDate
  (byte-matched discriminators); closedTrades carries 2,937 in-hole rows w/ point-in-time
  values; NO as-of on snapshot endpoints. Rec at CTO: FILLED-VIA-HISTORY-ARTIFACTS (~45-call
  one-shot window pull -> bronze/eclipse/_history/* new artifact types; I execute on GO;
  manifest amendment rides 0.7.0's authorship).
- Corrections needing record-landing (flagged to CTO in findings): 074e2530b holes[].reason
  wording (current-state-only is true of SNAPSHOT endpoints only) + D3:27/domain-docs catalog
  pointer.
- Standing: mirror-inf twin ARMED (my 14:33Z lift; first-fire alarm 15:45Z was exact-token-vs-
  hole semantics, 0.7.0 routing the >=-token fix; self-clears tomorrow); eclipse silver duty
  today-forward exception-only; push discipline = once per work-package close (COO 15:52Z).
- NEXT CLOCK: bd49f first-fire verdict ~03:15Z 07-17 (opal-assets-bd49f-dim-convert invoke
  result + blackdiamond/49f silver date=2026-07-16 listing; exit-1 SidecarMismatch = refuse-gate
  WORKING, not a defect).

## Next Steps

- [1.0.0_SA_CTO] rules on the census: FILLED-VIA-HISTORY-ARTIFACTS (I execute the window pull)
  vs citation-upgrade close. Either way the manifest amendment coordinates with
  [0.7.0_AE_CloudOps].
- ~03:15Z 07-17: bd49f first-fire verdict (mine).
- Event-driven standby otherwise; Monitor task brji8af6v armed.
