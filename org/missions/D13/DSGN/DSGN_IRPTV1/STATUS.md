# DSGN_IRPTV1 -- status (FAST lease)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.5
@1cccbe6bc6. Reviewer `3.0.0_SA_CVO` (grades each landed pin after the fact). Mode: FAST under
`org/mcp/drive-mode.log` line 1 (Andrew-direct ~17:4xZ blast mode), lease to 2026-09-24T21:14:14Z (re-armed 18:16:59Z, drive-mode.log line 5). Build place:
the main portal checkout on DEV (Andrew-direct ~18:3xZ). Design direction: Andrew-direct ~19:4xZ,
`org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260924_194xZ_IRPT_DESIGN_NOTES/`.
As of 2026-09-24T22:0xZ. The lease extends 30 minutes past Andrew's latest prompt (presence rule, `.tools/drive-mode.py`).

## Pins

| What | Value |
|---|---|
| Working tree | the main portal checkout `C:/Users/AndrewBerman/Desktop/ajb_workspace/portal`, branch DEV |
| Portal pin | `d99516cd` = origin DEV (ls-remote read after the push, via gh credentials -- see Parked) |
| This session on DEV | P candidate 8 `237bdfda`; S6 `92d16efc`; firm tab + exact amounts `a65a8db5`; S7 `c1d7aefe`, `9902bf25`; breadcrumb `d6288d80` (merged over site Z as `c82f0bbb`); header `93b28880`; Analysis upload lane `088386fe`; Analysis declutter `68f46e18`; Holdings footers `c75a0fc9`; Performance footer `af66ed43`; drill table `f338e693` (merged over site Z as `06f079f5`); model colours `08a04fe2`; asset-class colours `86561aef`; models dialog `721170ca` (merged over site Z as `d99516cd`) |
| Deployed | DEV CI deploys opalinvest.dev from DEV; PROD `a0690a03` untouched (gated) |
| Screen | `localhost:5174` from the main checkout (`bun run dev --port 5174`, its `.env.local`), log `C:/tmp/portal-main.vite5174.log` |
| Workspace push state | CLOUD LOCAL |

## Live thread

NOT LIVE END TO END. Andrew's HAR at ~18:3xZ exercised the signed-in API journey at all three firms (M's record
`ANDREW_DIRECT_20260924_184xZ_IRPT_FIRM_TAB_FILTER_AND_10K_ROUNDING.md`); hop 6's `spread` is not served.

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| S6 (black tiles, CUSIP as a name) | CANDIDATE @92d16efc | row S8; `deliverables/2.0.0_SA_COO~D/s6.fast-run.png` |
| Firm tab FIRM_BINDING; $10K rounding | CANDIDATE @a65a8db5. Directory rows Global 4 -> 49financial 2 (NARROWS); 4 -> 0 before | `ad184x.fast-run.*`, `firm-filter.run.txt` |
| S7 (8 legacy failures) | 4 FIXED @c1d7aefe + @9902bf25; 4 re-scope on CTO 100865 (own call) | row S9 |
| Breadcrumb root id | CANDIDATE @d6288d80 | `breadcrumb.fast-run.png` |
| Header: chip flood, account bubbles, white input, tab scrollbar | CANDIDATE @93b28880 | `design-notes-1.fast-run.{png,txt}` (OS dark mode) |
| Analysis upload on the served template lane (Y BLOCKER 100869, edits 1-3) | CANDIDATE @088386fe; edit 4 (wire regen) blocked by gen-wire's missing oneOf rule | `upload-lane.fast-run.{png,txt}`, `upload-lane-driver.mjs` |
| Analysis: no id checkbox list, no request panels, no backend strings | CANDIDATE @68f46e18 | `analysis-declutter.fast-run.{png,txt}`, `analysis-probe-driver.mjs` |
| Holdings footers: timestamp + source only; facts in the header help tip | CANDIDATE @c75a0fc9 | `footers.fast-run.{png,txt}`, `footer-probe-driver.mjs` |
| Performance headline footer: timestamp + source only; Details facts in the header help tip | CANDIDATE @af66ed43 | `perf-footer.fast-run.{png,txt}`, `perf-footer-probe-driver.mjs` |
| Drill table: Name, Amount, % of total, Supervision, Advisory; facts on the row hover | CANDIDATE @f338e693 | `drill-table.fast-run.{png,txt}`, `drill-table-probe-driver.mjs` |
| P 100893: 49F provider OPAL_ENGINE renders (no runtime enum check) | VERIFIED on 5174 @06f079f5 | `opal-engine.fast-run.{png,txt}` |
| Drill pie: canonical Opal primary-model colours (Ultra Long Term red) | CANDIDATE @08a04fe2 | `model-colors.fast-run.{png,txt}`, `model-colors.fixture.json` |
| Securities map + table: canonical asset-class colours (Opal ETF classifier; Unclassified grey otherwise) | CANDIDATE @86561aef | `asset-class.fast-run.{png,txt}`, `asset-class.fixture.json` |
| Models dialog: one column, members coloured by asset class (IRPT only; additive `breakdown` prop) | CANDIDATE @721170ca | `models-dialog.fast-run.{png,txt}`, `models-dialog.fixture.json`, `models-dialog-probe-driver.mjs` |

Nothing here is CVO-graded yet.

## Write claims

- `portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx` (the drill stops at the model level; the security
  drill lives on the Securities map)

## Next proof

The drill pie stops at the model level (no security-level slices); the security drill lives on the Securities map.
One real run on 5174 with a many-security model, screenshot read.

## Next-list (Andrew's design notes first, most broken first)

1. Panel footers: DONE (Holdings @c75a0fc9, Performance @af66ed43).
2. Holdings drill table: DONE @f338e693.
3. Canonical Opal primary-model colours: drill pie DONE @08a04fe2; the Asset Category Views hero cards still grey
   (CategoryViewTree's own category colours; next with item 4).
4. DONE for the map and table @86561aef (Opal ETF classifier). Remaining: the models dialog (item 5) and the drill pie's
   security level. Canonical asset-class colours (gold commodities, orange alternatives, pink structured hedge, green fixed income
   and cash, blue equities) on the treemap, the Securities table and the models dialog, from the positioning page's
   classifier; the security-level drill moves to the Securities map with the positioning treemap's tooltip.
5. Models dialog: DONE @721170ca.
6. Client picker: the platform's dropdown design, no truncation; a paginated client list with a search bar.
7. Performance: a sample view before a client is chosen; the "Basis: not supplied" chip.
8. Analysis design: three variant cards (solo, vs one model, vs several Opal models) in the philosophy-card
   style; a cleaner upload step; the comparison key input in advisor words.
9. Progressive disclosure page-wide: toggles and dialogs to cut the scroll.
10. S7's last 4: fe-s-5 controls' per-tab Export retired (FWD-9), fe-s-5 fields re-scoped (CTO 100865).
11. gen-wire.ts: render oneOf object alternatives, then regenerate AnalysisUpload{Request,Result} and drop the
    bridge type in tabs/analysis/prospect.ts (P's contract is on CLOUD @aa21133b67).
12. FWD-11 sweep ("OK [code not defined by the v1 contract]" off the bodies); PRD backlog 7-11.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| IRPT portal candidates | `2.0.0_SA_COO~P`, `~M`, `~Y` | one message: branch, tip, suites run | P 8 CONSUMED |
| Template upload lane | `2.0.0_SA_COO~Y` / `2.0.0_SA_COO~P` | Y spec @194ee0dc4b; P's contract @aa21133b67 (CLOUD, LOCAL) | CONSUMED @088386fe; regen is this seat's (next-list 11) |
| `spread` served | `2.0.0_SA_COO~P` | performance contract | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Asset class for every IRPT-held security (Andrew: extend the Opal ETF classifier to all of them) | `1.0.0_SA_CTO` to route | a data owner is named |
| Supervision / Advisory read "withheld" on live data (Andrew: a data issue) | `2.0.0_SA_COO~M` | M names the producer field |
| DEV CI does not run `bun test` | `1.0.0_SA_CTO` | a ruling on ci.yml |
| No `.owned-paths.yaml` row for `org/missions/*/*/*/STATUS.md` | `1.0.0_SA_CTO` | the row lands |
| Site Z edited an IRPT file's comment on DEV (`ExportModal.tsx`, AMGT-rn-3 `02e04083`) | `0.0.0_AB_MSTR~Z` | if IRPT files must stay single-writer |
| Git's credential manager (`credential.helper=manager`) now refuses non-interactively on this box; `gh` is logged in as the same account, and pushes run with `-c credential.helper='!gh auth git-credential'` for that command only | Andrew | he re-signs the credential manager, or says to keep the gh route |
| `lib/modelPortfolioColors.getModelColor` partial match: "Opal Ultra Long Term" hits "long term" first (worked around in DrillTree only) | the shared-library owner via `1.0.0_SA_CTO` | a ruling to prefer the longest key |
| Leftover folders `C:/tmp/dsgn-irptv1-fast`, `-base` | Andrew | his OK for a recursive delete |

## Limits

Nothing landed this session is CVO-graded. Real runs use the stubbed-auth smoke fixture and the server-captured wire,
not a signed-in session. PROD, deploys and vendor egress stay under their normal gates.
