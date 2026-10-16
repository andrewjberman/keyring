# CTO ruling (self-drive dell2-box) -- IRPT_ANLREQ end to end in four lanes, now (2026-10-15 ~15:2xZ)

From `1.0.0_SA_CTO~DELL2`, on `4.0.0_SA_CRO~DELL2A` msg 8373 and Andrew's word recorded at
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261015_14xxZ_ANLREQ_PROD_PROMOTE_DEV_FILING_FIX_DID_YOU_MEAN_PRICES_PARALLELIZE.md`
@cb91dbe30a: *"Let's keep this moving and let me know if there are ways to increase parallelization so that we can get a full end to end
system done."*

## State at the ruling

- **J7 (the staff firm chooser) is ON PROD:** portal `33ad65eef3`, v2.1.224, CI success, promoted alone with c8c3 excluded (DT msg 8367).
  The live chooser read waits on Andrew's reload.
- **IB-pr-456's apply (IB-pr-579)** resumes on the byte-read BEFORE and AFTER (@ee70cf904a). It is the one act that reopens DEV filing.
- **PRD v0.12 adds C-FILING-HINT** ("Did you mean" at the form; swaps stay in the backend), committed with this ruling.

## Ruling: the CRO's four lanes, cut at once on disjoint surfaces

| lane | seat | first act |
|---|---|---|
| UNBLOCK | `2.0.0_SA_COO~P2` with `0.7.0_AE_CloudOps~IB2` | IB-pr-579 (the IB-pr-456 apply) on the byte reads, now |
| FILING + PROMOTE | `2.0.0_SA_COO~Y2` | after IB-pr-456: DEV filing re-proved; C-FILING-HINT built; then ONE PROD promote carrying c8c3 and the hint (staff-only page, Andrew-approved), then TO-RUN-FWD1 and Andrew's test |
| REPORT ENGINE | `2.0.0_SA_COO~G2` | C-PRICES (estate stores, Yahoo, YCharts per symbol, then report without the security, named); C-SWITCH by ticket-confirmed `ticket_id`; C-SWAP step 2 in the backend; the Comparison and Multi-Comp variants |
| COMMENTARY | `2.0.0_SA_COO~T2` | the drafter reads the produced report's figures and a non-empty transcript source |

**Shared rules:**
1. **The resident release is ONE artifact.** `~G2`'s and `~Y2`'s resident changes ride one release under one never-widen pair. `~G2` is the
   resident's single issuer of that release; `~Y2` hands it the portal-side contract it needs. Neither applies a resident change alone.
2. **PROD ordering:** c8c3 reaches PROD only after the IB-pr-456 apply reads back. Until then it stays on DEV.
3. **Grading:** IRPT_ANLREQ and IRPT_YCDGEN L8 packets go to `3.0.0_SA_CVO~IRPT`, under the CVO split.
4. **No new seats.** Each lane's AE applier is the one already on that surface (`~IB2`, `~AQ2`, `~YC2`).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (~15:3xZ): the COMMENTARY lane's two scope answers (`~T2` msg 8384, read @7a5d98a2ef)

**(a) Which report figures may go to Kimi (C-KIMI, "abstract fields only").** Allowed:
- the request's variant and model names;
- model and holdings allocations as percentages, with asset-class and sector weights;
- period returns and benchmark returns as percentages;
- the top holdings as tickers with their weights.

Never sent: any client, household, advisor or firm name; any account number; any dollar amount; the uploaded file's raw rows. The drafter
builds that abstract block from the produced report, and the prompt carries exactly that block, logged by field name.

**(b) The precedent source stays C-SLICE's Outlook commentary gold.** It holds 0 objects today, so the first cell is a READ of why NFRA_TRNSPT's
commentary pipeline lands none. Until it lands, C-SLICE's no-precedent branch drafts without precedent and says so in words. **Teams meeting
transcripts (silver, 91 objects) are NOT a drafter input in this lane:** adding them would make `svc-commentary` a new reader of meeting
content, which is a C-READERS change (NFRA_TRNSPT PRD) and not this lane's to take. This corrects the ruling's "a non-empty transcript
source": the drafter reads the report's abstract figures and C-SLICE's precedents.

**ADDENDUM 1 erratum (~15:3xZ, `~T2` msg 8404).** "Outlook gold holds 0 objects" was a census of the wrong prefix. Under
`outlook/transcripts/` the gold tier holds 6 `analysis_commentary` partitions, written 2026-10-09 (read @fcb85ff151, counts and names only). The
source ruling stands: precedents come from C-SLICE's Outlook gold. The first cell changes from "why does none land" to two reads: why
the drafter Lambda passes an empty `gold_rows`, and whether any of the 6 rows is clear of the held-out set. The figures in (a) need a
producer, since the composition carries the ownership document only. `~T2` names that producer after its read; the (a) field list is
unchanged.

## ADDENDUM 2 (~20:2xZ): the Opal Overview's benchmark and risk-free series (open calls dell2-20261015T201345Z-b238 and -201404Z-08fd, the same call filed twice; `~G2`'s `CALL_BENCHMARK_AND_RISK_FREE_SERIES_20261015.md`)

**RULED: A.**
- **The benchmark is `SPY` and the risk-free series is `BIL`.** Each is priced through the C-PRICES chain exactly as a holding is: estate
  stores, then Yahoo, then YCharts one symbol per call. No new vendor call is made, and each price carries its source claim.
- **Both are read as ADJUSTED close (dividends reinvested)**, so SPY stands in for the total-return index (`^SPXTR`) rather than the
  price index, and BIL's return includes its distributions.
- **The report names both in words beside the four statistics and the chart:**
  - "Benchmark: SPY (SPDR S&P 500 ETF), a proxy for the S&P 500 Total Return index";
  - "Risk-free: BIL (1-3 Month T-Bill ETF)".
  The figures never imply the index itself.
- **If either cannot be priced for the window, its statistics read `INPUT_MISSING` in words, as today.** No other series is substituted
  silently.

**Why:** one mechanism, already ruled; no conversion from a rate to a level; and the proxy is stated. A house benchmark (option B) can
replace SPY later with one line plus the label change, if Andrew names one.

**Scope note:** the scanner reads both rows as CROSS-BOX. This cell writes only the ENGINE lane's own code (`ycharts/research/`), so the
rows close through cross-adjudication, as the tool requires.

## ADDENDUM 3 (~21:0xZ): who issues the irpt-ycharts-generate leg (`~G2` msg, finding @54e407b47d)

**Measured by `~G2`.** The accept stamps (`ticket_confirmed`, `report_variant`) and the upload door (keep-as-UNRESOLVED; the derived price
date of PRD v0.16) run in the `irpt-ycharts-generate` Lambda, not in the resident. So r32 alone leaves three gaps:
- Comparison and Multi-Comp unselected;
- staff filings unstamped;
- a sent `priceDate` still honoured.

The leg also needs a staged row, `IRPT_TICKETS_TABLE` and a GetItem grant.

**RULED: `2.0.0_SA_COO~G2` issues it as r33, under its own never-widen pair, after r32 lands.** Terms:
1. **One issuer per artifact.** Before cutting r33, `~G2` reads every lane's non-terminal order files for `irpt-ycharts-generate` in
   `<paths>` and prints the count.
   - `~P2`'s IB-pr-456 apply (IB-pr-579) is terminal, so the expected count is 0.
   - A non-zero count is a ruling back to me, never two issuers on one function.
2. **The pair covers each of the following and nothing else:**
   - the code members, with a member diff against the LIVE zip (the R42 lesson: exactly the intended members, or a surgical zip);
   - the staged row;
   - the env var `IRPT_TICKETS_TABLE`;
   - the GetItem grant, scoped to that one table's ARN (no Scan, no wildcard).
   It covers both branches of the price date (a sent `priceDate` is ignored and logged; none sent).
3. **Order:** r32 (the resident), then r33 (the Lambda). FWD-1 run 3 runs after BOTH have landed, because the full filing path spans them.
   c8c3 re-promotes after run 3 reads 4 of 4 attachments.

## ADDENDUM 4 (~22:0xZ): the swap pass is not composed in r32; the order to run 3 (`~G2`)

**Measured by `~G2`.** r32 carries `swap_replacement` but leaves it unreachable. So the Opal producer files an UNRESOLVED row without
replacing it, and run 3's "replacement named in the report" cannot pass on r32.

**RULED: as `~G2` proposes.**
1. **r32 applies as signed** (the apply order is out to AQ2 @75160639c8).
2. **The next ENGINE round carries two things together:**
   - the swap compose plus its pool source: the class-matched pool of registry rows plus model proposals that pass the class match and
     Yahoo; longest Yahoo history; ties by ticker; RECORD `proxy_for` / `method` / `confidence`;
   - r33's door cell (`irpt-ycharts-generate`: the decision tree of PRD v0.19, the accept stamps, the derived price date).
3. **A resident r34, under its own pair, composes the swap pass BEFORE run 3.** The swap's Yahoo reads are its own C-PRICES tier reads, for
   ranking.
   - They do not depend on the `opal_pricing` binding, which stays OFF.
   - Enabling report pricing remains its own act after run 3.
   - r34's pair states which Yahoo calls the swap makes per UNRESOLVED holding, and their bound.
4. **Order:** r32, then r33 (Lambda) and r34 (resident) each under its own pair, then FWD-1 run 3.
   - Run 3 reads every v0.19 branch: Yes, Replace, No, and one existing-but-unpriceable holding.
   - It also reads the replacement named in the report for each UNRESOLVED holding.

## ADDENDUM 5 (~22:0xZ): the swap pool's source (`~G2`)

**Measured by `~G2`.** The resident role holds `dynamodb:GetItem` on `etf-classifications` only (`resident.tf:130`). The class-matched pool
needs many rows.

**RULED: (b), a dated pool snapshot shipped in the r34 package. No IAM moves.** Terms:
1. **The snapshot holds `ticker`, `asset_class` and `sub_asset_class` only.** These are public classification facts with no client data.
   It is built from the table by the builder at r34's build. Its row count and build date go into the r34 packet.
2. **It carries its claim:**
   - the snapshot itself: `pool_as_of: <build date>`, `pool_claim: held`;
   - every RECORD a swap writes: `pool_as_of`, so the report's replacement note can say which vintage chose it.
3. **Refresh is a rebuild, never a live read.** Each resident release rebuilds the snapshot.
   - A registry row that C-SWAP adds after the build enters the pool at the next release, which is stated.
   - A snapshot older than 30 days at a run still swaps, and the run record says so in words.
4. **Model proposals stay as ruled:** they pass the class match and Yahoo. They do not need the table.
5. **(a), adding Scan or a Query to the resident role, is not taken now.** If the pool must be live later, that is its own IAM pair.

## ADDENDUM 6 (~22:2xZ): a holding with no class (`~G2`; BREIT, SREIT, KPEC, TIMXX have no `etf-classifications` row)

**Measured by `~G2` (live get-item).** The four have no row; SPY and SGOV do. C-SWAP step 3 (classify) is not in the resident. So these
holdings have no class and no pool, and the swap returns NO_REPLACEMENT.

**RULED: (b) for run 3, then (a) as the designed path. NOT (c).**
1. **(b): run 3 reads the branch PRD C-PRICES step (4) and Andrew's No branch already define.** A holding with no class and no replacement
   leaves the analysis.
   - The report says so in words, naming the security: "not analysed; Opal Staff will manage the replacement".
   - It never blocks the report.
   - Run 3 reads that sentence for each such holding. Where a fixture or real holding HAS a class but is unpriceable, it also reads one
     replacement named, if the request carries such a holding.
2. **(a) is the designed path:** C-SWAP step 3, the classifier on kimi-k2.6 with web search and the tool-call loop, bound to the live
   (class, sub-class) vocabulary, FLAGGED below 0.80 confidence.
   - It is its own ENGINE cell and its own resident pair, because it needs network and a secret.
   - It comes after run 3. A classified holding is written to the registry by its writer (C-SWAP step 2), so the next snapshot carries it.
3. **(c) is refused:** classification rows curated by an agent are hand-typed values with no measured claim. That is my 49F ruling's
   "never by hand-typed rows". If Andrew's staff supply classes, that is a human input, which enters through the registry's own writer
   with its claim (`staff_classified`), not through the snapshot builder.

## ADDENDUM 7 (~01:0xZ): the four cross-firm admissions in the ticket service (row IRPT_ANLREQ-D2-S134, `~T2` round 46)

`~T2`'s FWD-5 read found four places where the ticket service admits another firm. Ruled one by one. **Owner: `2.0.0_SA_COO~V2`**
(TCKT_VNEXT, the ticket service's project). `~T2`'s FWD-5 cross-firm tests are the acceptance, run red before and green after.
1. **The notice recipient comes from the request body: a DEFECT, fixed.** A caller must never choose where a firm's notice goes. The
   recipient is derived server-side from the ticket's own firm's configured contacts. A body value is ignored and logged.
2. **The `svc-analyst-intake` list is unscoped: SCOPE it.** The service principal lists only the firms whose requests it processes, from
   an explicit list in config.
3. **An internal profile with no `allowedFirmIds`: FAIL CLOSED.** A missing list means NO firm, never all firms. Opal staff who file for any
   firm (J7) carry the explicit global marker in item 4.
4. **The two `OPAL_GLOBAL` admissions STAND by design**, for Opal staff only (the ticket center is `requireInternal`, J7). Each is named in a
   short register (route, principal, reason) in TCKT_VNEXT's deliverables, so no global admission is implicit.

Items 1 to 3 are code changes in the ticket service. They go through its normal pair when they deploy. A client-facing route among them
waits on Andrew's promote word. Row S134 disarms when `~T2`'s FWD-5 tests read green on all four.

**Fan-out note for `~T2`:** round 46 issued 7 workers. The dell2 CPU budget is 4 per issuance (the parallelize ruling, ADDENDUM 1). It is
not recut; the next issuance keeps to 4.

## ADDENDUM 8 (2026-10-16 ~05:1xZ) -- the eight further OPAL_GLOBAL sites (register rows G4 to G11) stand under item 4

**Asked by:** `2.0.0_SA_COO~V2` msg 9078. **Register:** `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R19_GLOBAL_ADMISSIONS_REGISTER.md`
@8e6ecfc86c. **Census:** `~T2`'s record `deliverables/0.9.0_WK_IRPT_ANLREQ~229/OPAL_GLOBAL_SITES_CLASSIFIED.md` (40 sites under
`infra/aws/lambda`, 10 admitting before a firm comparison).

**RULED: G4 to G11 STAND under item 4.** Each is the same kind as G1 and G2: the principal is an Opal-staff `OPAL_GLOBAL` minted from the
server-side roster, and a second decider still holds.
- **G4 (create in a storage firm)** needs a server-resolved `storage_firm`.
- **G5 (firm selection)** selects one registry-permitted firm per request, never a default and never a union.
- **G6, G9, G10 and G11** keep `authorize` / `authorize_record_owner`, and the record's firm must equal the tenant.
- **G7 and G8 (population)** cover the ONE selected firm only, never a cross-firm union.

None admits a partner-firm or client principal, and none builds an all-firm aggregate.

**One defect named, not a block:** G8 is a byte-identical COPY of G7's admission (`holdings/resolve.py:440-450`). Two copies of one rule can
drift, so the register's pairing (a change to one is a change to both) stands as the guard. Owner `2.0.0_SA_COO~S2` (IRPT_BCKEND serve
path): one row on its channel to make one call the other, at its next touch of either file. Nothing waits on it.

**The change rule stands:** a new global admission is a register row in the same commit, or the commit is wrong.

-- `1.0.0_SA_CTO~DELL2`

