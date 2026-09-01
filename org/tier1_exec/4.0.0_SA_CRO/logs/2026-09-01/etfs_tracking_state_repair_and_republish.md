# 4.0.0_SA_CRO — ETFS partner-ownership: state recon, data + display repair, served republish

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, IMPLEMENT, DEPLOY

**Window:** 2026-09-01 ~15:25Z -> ~17:50Z (session start -> now). First log of this session.
**Serial:** `4.0.0_SA_CRO` (base, no lane). **Registered** 15:2xZ; watcher Monitor `bt72luq1c` armed and
confirmed live by its own `[INBOX]` emission. Zero crons.

---

## 1. What was asked

Andrew-direct, five successive instructions in one thread:
1. *"research the ETFS_CANON and the state of our tracking methodology for partner ETFS ownership. I need to
   present a monthly report for August and July for our CFO with the partner daily holdings and average
   holdings ... i think we need to get establish the state of this system."*
2. *"mathematically, is it more accurate to get the average based on trading day values only or should we
   stick to full calendar day?"*
3. *"I need the final data files, both the CSVs and the presentation files in a folder on desktop including a
   methodology file"* (+ *"Yes July SHould be included"*).
4. *"We shouldnt have coverage gaps"* -> *"you should be able to handle this from opal-data-assets"* ->
   *"there should not be any missing dates when we present"*.
5. Chart-depiction review -> *"ok regenerate the renders"* -> brief + `/log`.

## 2. What was found

- The monthly reporting system was **already live and scheduled** (1st of month ~14:00Z) and had already
  produced both months. The register said `scoping`; the estate said `serving`.
- `ETFS_CANON`'s deferral condition (ETFS_INGEST done) **had fired with nothing watching for it**, which is
  why unaddressed work sat. `gold/ownership_daily/` still does not exist.
- **Data gap:** 5 cottonwood August trading days never produced; 10 July slices landed 4h10m AFTER the July
  render and were never picked up.
- **Display defects:** weekends blank for business-day partners; July rendered 25 of 31 calendar columns.
- **A materially false chart:** August per-ETF PERIOD advertised **DIVZ +$207.9M** against a true **+$9.6M**.

## 3. Acts

| # | Act | Evidence |
|---|---|---|
| 1 | 5 cottonwood August slices backfilled via the producer's OWN dated path | 43/43 trading days x 3 partners, read from S3 |
| 2 | Matrix: universal carry fill + full calendar month columns | `1715af512d`; 31/31 cols, 0 blanks, 372/372 vs CSV |
| 3 | Charts: PERIOD month-boundary seed + false caption corrected | `9ea991b080`; DIVZ day-1 $216.7M vs truth $217.0M |
| 4 | Served reports regenerated, both months, 10 objects | `3c29e9c354`; verified at the re-downloaded artifact |
| 5 | State-of-system deliverable | `a47e9b212c` |
| 6 | Tagged session brief | `e58d676a15` |
| 7 | CFO pack on Desktop (CSVs + avg summary + HTML/PDF + METHODOLOGY.md) | byte-identical to served |

**NO EGRESS PERFORMED.** Andrew offered it for the coverage gaps; the upstream partitions already existed in
`opal-data-assets`, so none was needed and none was used.

**Premise checked before the backfill:** `cot-etf-ownership-daily/lambda_function.py:137-141` deliberately
writes no slice for a day whose holdings are present but entirely UNPRICED. Backfilling such a day would
have FABRICATED data. All five carry 10,958-11,929 priced positions, so the skip contract did not explain
them. The five totals were computed independently BEFORE invocation and matched to the cent.

**Methodology question answered:** calendar-day carry-forward is correct and is not an approximation — AUM
is a stock, so its correct average is the time-weighted mean, and carry-forward IS that mean. Trading-day
averaging would weight a Friday mark equal to a Tuesday's. Matches Andrew's own D1 ruling (2026-06-22).
Sizing: ~7 bps in August ($444,707 on $651.9M).

## 4. Controls that make the numbers trustworthy

- **49financial unchanged in BOTH months; inflection unchanged in August** — three rows that moved $0.00.
  Those series had no gaps, so they must not move.
- **July byte-unchanged by the chart fix** (1 July was a Wednesday) — the fix touched only the broken case.
- **All six daily CSVs byte-identical** across both display fixes — display-only, no figure moved.
- **July's +$497,352 revision reached twice by independent routes** (recompute from source; rebuild through
  the renderer) and agreed.
- **A verification predicate caught failing toward GREEN**: an early blank-detector could not detect a blank
  at all and reported 0 holes. Self-tested against a known-positive before being trusted.

## 5. Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | "where is the ETFS_CANON partner ETF ownership pipeline" | PARTIAL | near-tie across 3 of 81; routed to comp-find |
| `comp-find` | `'ETFS_CANON'`, `--name 'ETFS'`, `--name 'avgcap'`, `'daily/cottonwood'`, `'platinum/reports'` | PASS | located registry, producers, renderer, orchestrator |
| `comp-find` | `'orion_normalize_as_of' -- data/etfs` | PASS | **measured ZERO over 19 files** — the T-1 defect is still unfixed |
| `comp-read` | `ETFS_AVGCAP.md`, `cot-etf-ownership-daily/lambda_function.py`, `render_month_end.py` | PASS | surfaced the D1 ruling and the UNPRICED skip contract — the qualifier a grep would have missed |
| `lib/trading_calendar.py` | Jul=22 / Aug=21 NYSE trading days | PASS | the discriminator for every coverage claim |
| `safe-commit.sh` | 5 commits | PASS | one rc=128 refusal (`cannot do a partial commit during a merge`) — deferred, not forced |

**What worked:** `comp-read` on the producer Lambda surfaced the UNPRICED-day skip contract, which is the
single fact that separated a legitimate backfill from fabricating data. A grep for the date would not have
shown it.
**What failed:** `comp-find` on `'daily/cottonwood'` exceeded the 120s Bash timeout and had to be
backgrounded (197 hits / 142k files).
**Gap found:** nothing in the estate watches for a condition-bounded hold's trigger to fire. `ETFS_CANON`'s
deferral condition was satisfied and the project simply sat until Andrew noticed.

## 6. Blockers

**None blocking the delivered work.** One gate fired and was **respected, not overridden**:
`git push origin CLOUD` is INTEGRATOR-ONLY on the shared branch (LD-0367/LD-0368; only `0.0.0_AB_MSTR` may
push). Consequence recorded in §7.

## 7. Current State

- **Data:** `s3://opal-data-etfs/daily/{49financial,cottonwood,inflection}/` — **43/43 NYSE trading days for
  all three partners across July + August 2026.** Verified by reading S3, not producer self-reports.
- **Served:** `s3://opal-data-etfs/platinum/reports/{2026-07,2026-08}/` — regenerated 2026-09-01T17:38Z,
  10 objects. Both months 31 columns / 0 blank cells; August per-ETF legend `DIVZ +9.6M`, y-floor $84M.
- **Code:** `data/etfs/scripts/presentation/render_month_end.py` — matrix reads the carried series, column
  set is the full calendar month, PERIOD charts seed from the prior month-end, caption corrected.
- **Andrew's CFO pack:** `C:\Users\AndrewBerman\Desktop\Opal_ETF_Partner_Ownership_Jul-Aug_2026\` —
  byte-identical to the served copies. `superseded_original_pipeline_render/` holds the gap-bearing originals.
- **Figures now served:** Jul total **606,095,859.47**, Aug total **651,884,085.14**.
- ⛔ **PROVENANCE GAP:** producing commits `1715af512d` + `9ea991b080` were **LOCAL, not on origin** at upload
  time (push gate above). Self-closing via the hourly integration window — **but if that window does not
  carry them it does not close by itself.**

## 8. Next Steps

1. `[0.0.0_AB_MSTR]` Integration window: carry `1715af512d`, `9ea991b080`, `3c29e9c354`, `e58d676a15`,
   `a47e9b212c` to `origin/CLOUD`, closing the provenance gap on the currently-served bytes.
2. `[Andrew]` Decide whether the month-end email should be re-sent — the recipient has NOT been told the
   July/August figures moved. NOT self-authorized.
3. `[Andrew / 2.0.0_SA_COO]` `ETFS_CANON` remains unbuilt (`gold/ownership_daily/` absent) with its design
   gate RULED; the registry `pipeline` field still describes the OVERRULED DynamoDB architecture.
4. `[ETFS/DS lane]` Orion T-1 label defect: `orion_normalize_as_of` = 0 calls in `data/etfs`. Inflection sits
   on T-1 beside two partners on T inside the file that compares them. ⛔ The $424K correction and the $441K
   staleness delta are DIFFERENT BASES and must not be summed.
5. `[cot-pipeline lane]` Root cause of the cottonwood producer's 5 missed August runs — UNDIAGNOSED.

## 9. MCP traffic

2 inbound at load (both 2026-08-30 closures from `3.0.0_SA_CVO` and `1.0.0_SA_CTO`, nothing owed by this
seat), read and ACKed (`85633`, `85726`). No dispatches issued — CRO does not dispatch, and no fabric
relay was warranted.
