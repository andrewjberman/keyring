# DSGN_IRPTV1 -- status (FAST lease)

Seat `2.0.0_SA_COO~D` (CLAUDE). Contract: PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.5
@1cccbe6bc6. Reviewer `3.0.0_SA_CVO` (grades each landed pin after the fact). Mode: FAST under
`org/mcp/drive-mode.log` line 1 (Andrew-direct ~17:4xZ blast mode), lease to 2026-09-24T20:41:52Z. Build place:
the main portal checkout on DEV (Andrew-direct ~18:3xZ). Design direction: Andrew-direct ~19:4xZ,
`org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260924_194xZ_IRPT_DESIGN_NOTES/`.
As of 2026-09-24T20:2xZ.

## Pins

| What | Value |
|---|---|
| Working tree | the main portal checkout `C:/Users/AndrewBerman/Desktop/ajb_workspace/portal`, branch DEV |
| Portal pin | `088386fe` = origin DEV (ls-remote read after the push) |
| This session on DEV | P candidate 8 `237bdfda`; S6 `92d16efc`; firm tab + exact amounts `a65a8db5`; S7 `c1d7aefe`, `9902bf25`; breadcrumb `d6288d80` (merged over site Z as `c82f0bbb`); header `93b28880`; Analysis upload lane `088386fe` |
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
| Analysis upload on the served template lane (Y BLOCKER 100869, edits 1-3) | CANDIDATE @088386fe; edit 4 waits on P's contract patch | `upload-lane.fast-run.{png,txt}`, `upload-lane-driver.mjs` |

Nothing here is CVO-graded yet.

## Write claims

- `portal/src/pages/InvestorReporting/tabs/analysis/**` (Analysis: the account picker, the request panels, strings)

## Next proof

Analysis tab with a client selected: the account picker lists only that client's accounts by name, never an id;
the request-history panels are gone. One real run on 5174, screenshot read.

## Next-list (Andrew's design notes first, most broken first)

1. Analysis: 1,000+ account-id checkboxes -> the selected client's accounts by name; drop "Your analysis requests",
   "Request history" and "Analysis requests"; strip backend strings (snapshot coordinate, catalog-key text,
   idempotency key); a cleaner upload step; three variant cards (solo, vs one model, vs several Opal models) in the
   philosophy-card style. Coordinate with `2.0.0_SA_COO~Y` (its upload-poll interface, msg 100825).
2. Panel footers page-wide: source and timestamp only (Allocation, Securities map, Securities, Performance).
3. Holdings drill table: Name, Amount, one share column, Supervision, Advisory; no Node/Basis/Denominator/
   Provenance columns and no fact strings.
4. Canonical Opal primary-model colours in the drill pie (Ultra Long Term is red); find the one library.
5. Canonical asset-class colours (gold commodities, orange alternatives, pink structured hedge, green fixed income
   and cash, blue equities) on the treemap, the Securities table and the models dialog, from the positioning page's
   classifier; the security-level drill moves to the Securities map with the positioning treemap's tooltip.
6. Models dialog: full-width securities list.
7. Client picker: the platform's dropdown design, no truncation; a paginated client list with a search bar.
8. Performance: a sample view before a client is chosen; the "Basis: not supplied" chip.
9. Progressive disclosure page-wide: toggles and dialogs to cut the scroll.
10. S7's last 4: fe-s-5 controls' per-tab Export retired (FWD-9), fe-s-5 fields re-scoped (CTO 100865).
11. FWD-11 sweep ("OK [code not defined by the v1 contract]" off the bodies); PRD backlog 7-11.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| IRPT portal candidates | `2.0.0_SA_COO~P`, `~M`, `~Y` | one message: branch, tip, suites run | P 8 CONSUMED |
| Template upload lane | `2.0.0_SA_COO~Y` / `2.0.0_SA_COO~P` | Y spec @194ee0dc4b; P's contract patch for the wire regen | CONSUMED @088386fe; regen AWAITED |
| `spread` served | `2.0.0_SA_COO~P` | performance contract | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Asset class for every IRPT-held security (Andrew: extend the Opal ETF classifier to all of them) | `1.0.0_SA_CTO` to route | a data owner is named |
| Supervision / Advisory read "withheld" on live data (Andrew: a data issue) | `2.0.0_SA_COO~M` | M names the producer field |
| Model Portfolios' own $10K grain | Andrew | his word (`CategoryViewTree exactAmounts` is the switch) |
| DEV CI does not run `bun test` | `1.0.0_SA_CTO` | a ruling on ci.yml |
| No `.owned-paths.yaml` row for `org/missions/*/*/*/STATUS.md` | `1.0.0_SA_CTO` | the row lands |
| Site Z edited an IRPT file's comment on DEV (`ExportModal.tsx`, AMGT-rn-3 `02e04083`) | `0.0.0_AB_MSTR~Z` | if IRPT files must stay single-writer |
| Leftover folders `C:/tmp/dsgn-irptv1-fast`, `-base` | Andrew | his OK for a recursive delete |

## Limits

Nothing landed this session is CVO-graded. Real runs use the stubbed-auth smoke fixture and the server-captured wire,
not a signed-in session. PROD, deploys and vendor egress stay under their normal gates.
