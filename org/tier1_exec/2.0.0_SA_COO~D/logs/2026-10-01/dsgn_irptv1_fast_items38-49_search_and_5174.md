# DSGN_IRPTV1 FAST items 38-49: footer words, W2-22, IRPT_DASHBD hop 5, search ranking, 5174 cache -- 2.0.0_SA_COO~D

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE

**Date:** 2026-09-30 14:2xZ to 2026-10-01 00:2xZ
**Task Order:** DSGN_IRPTV1 under a FAST lease (/closer-drive body of `/canonical-drive`, cron d49f1666, LIVE_ARMS
DIRECTED row); IRPT_DASHBD workstream F under C-LEASE; no numbered TO
**Status:** IN PROGRESS (portal origin DEV 970d5c75; the 00:20Z tick was stopped by Andrew before any act)

---

## Objective

Continue `/canonical-drive` on DSGN_IRPTV1 after the post-crash relaunch: land the walk-2 enrichment backlog item by
item on portal DEV, pre-stage and start IRPT_DASHBD FWD-1 hop 5, and answer Andrew's direct words at this terminal.

## Work Done

1. **Items 38-41 (W2-19 / W2-19b / W2-01 front residue / vendor words).** Every Holdings footer and the Performance
   footer read source WORDS, never a producer coordinate (portal 775c4261, 1bcda74c); a DEPENDENCY_UNAVAILABLE refusal
   names the missing upstream day and the picker never reads "pending" once answered (b1e18782); the registry vendor
   view `header/vendorDisplayNames.generated.ts` lands (e266a14a, on merge e67a03f4 of origin afa0597d).
2. **Item 42 (W2-22 remainder).** A model picked in the card scopes the map and the table (20f95f79). DEFECT OF THIS
   LANE: iv-e-119 shipped with type errors because typecheck ran before the test was written; 4.0.0_SA_CRO caught it
   (msg 103337); fixed at ffc3c346 (narrow on `status === 'ok'`); the drive log's first attribution of the red CI to
   wire regeneration was corrected. Merge b246014f took origin 29bfec2d (the CRO's MDPF_TAXSMA aum.ts interface).
3. **Item 43 (W2-16 probe).** Next button whole at five viewports, 390-1440 px; not reproduced; closes unless
   Andrew's capture recurs. No code.
4. **Item 44 (IRPT_DASHBD hop-5 plan).** `deliverables/2.0.0_SA_COO~D/item44/IRPT_DASHBD_HOP5_BUILD_PLAN.md`: five
   files, their tests, the real-run bar; nothing built against an invented shape.
5. **Item 45.** Vendor view regenerated over the committed register per CTO 103308 (c98fa91e).
6. **`/next-calls` then Andrew-direct ~21:0xZ "2yes, 1yes, go"** (record
   `deliverables/ANDREW_DIRECT_20260930_210xZ_FCASH_FOLD_YES_PROD_PROMOTE_YES_GO.md` @523c40ab1b). Item 46: FCASH folds
   into the one Cash row of the Securities table (c63553cf). The PROD promote was ROUTED to 0.0.0_AB_MSTR (21:40Z,
   updated 22:05Z); it waits on Andrew's re-smoke.
7. **Items 47 and 48 (IRPT_DASHBD hop 5, plan items 3 and 2)** over the COMMITTED gold contract
   `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` 0.1.0 @10939bbfa4: `dashboard/coverageWords.ts`
   + iv-e-120 (57cf660e); `dashboard/windowMath.ts` + iv-e-121 (63fb6318). The pin caught a 365-day annualization
   floor annualizing a one-calendar-year window across a leap day; fixed to "past one calendar year". No page mounts
   either module yet.
8. **Item 49 (Andrew-direct, search).** "the predictive text search isnt working. Is something rolling back this
   function somehow?" No rollback: 22cccf87 is in DEV and `header/search.ts` is unchanged since. Cause: the tiers ran
   only when an answer LANDED, against that answer's query; rows held while the next answer is in flight kept their
   old order behind "Loading". `ClientSearch.tsx` now stores served rows unranked and ranks them in a memo keyed on
   the live query (never a re-filter). iv-e-122 new, iv-e-47 wiring re-goldened. Portal 970d5c75.
9. **5174 (Andrew-direct, Market Performance import error).** All 76 /src modules behind the page answered 200; a
   fresh headless load reproduced the error: 504 on `/.vite/deps/@visx_text.js` and `@visx_wordcloud.js`.
   `portal/.vite/deps` was ABSENT under the running server (pid 27592, up since 09:33 local) with 34 `deps_temp_*`
   directories beside it. Server restarted (pid 18500); two fresh loads render "Market Overview", 0 module failures.
   Row DSGN_IRPTV1-S42. What removed the directory is NOT identified.
10. **00:20Z tick.** Lease read FAST until 00:50:33Z and the next-list read; Andrew rejected the next tool call and
    invoked `/log`. The tick fired no act.

## Compiler Tools

| Tool | Command | Result | Notes |
|---|---|---|---|
| typecheck | `bun run typecheck` from the portal root, after the last edit of each item | PASS | rc=0 at 970d5c75; one miss at item 42 (run before the test existed) |
| eslint | touched files per item | PASS | 0 errors; 4 warnings already in ClientSearch.tsx |
| bun test | iv-e-116..122 and the re-goldened pins | PASS | item 49: iv-e-122/104/47/37/57/101 green |
| real run | fixture-plane drivers in `portal/.runtmp/` on 5174 | PASS | item 49: fixed lists the typed name FIRST; HEAD component (negative control) LAST; shot read |
| mp-fresh-load | `.runtmp/mp-fresh-load.mjs` | FAIL then PASS | reproduced the import error; clean after the restart |
| drive-mode | `python .tools/drive-mode.py read DSGN_IRPTV1`, own call before each push | PASS | FAST at every push |
| surprise-row-gate | via safe-commit | PASS | S42: 1 new row of 130 checked |
| comp-find rail | one recursive grep denied | WARN | re-run as a per-file loop with `grep -q` |

**What worked:** a real-run negative control by swapping the HEAD bytes of one file under the running dev server and
restoring them; holding a fixture answer 20 s to reproduce an in-flight window.
**What failed:** two headless probes hung on `browser.close()` with a route still pending (fixed with `process.exit`);
a driver's auth stub missed the same-origin `/auth/refresh`; a `/api/` substring match also caught `/src/api/` modules.
**Gap found:** the dev server serves already-transformed packages from memory after its on-disk cache is removed, so
the failure appears only on a page not yet visited; `curl` of a visited package reads 200 and hides it.

## Deployment Sequence + Verification

- Portal DEV pushes by the lease seat, each after a lease read in its own call; VALGATE pre-push passed on each.
  Last: `63fb6318..970d5c75 DEV -> DEV`; `git ls-remote origin DEV` read `970d5c75` (00:2xZ), equal to local HEAD.
- No PROD change (PROD still ba8e971f, v2.1.191). No AWS change. No `.open_deploys/` entry opened by this lane.
- Workspace CLOUD: records 2eba103b88 and earlier are LOCAL; `git ls-remote origin CLOUD` read 85a765dbcd, which does
  NOT contain 2eba103b88 (positive control e87ee23b3f is contained). This lane never pushes CLOUD.

## MCP Traffic (significant)

CTO 103261 (IRPT_DASHBD L4-R admitted; hop 5 cut here) and 103308 (regenerate the vendor view) acted on; CTO 103373
(issuer rule) carried into STATUS.md; CRO 103337 (iv-e-119 type errors) acted on. Sends: the PROD promote route to
0.0.0_AB_MSTR at 21:40Z and a one-line update at 22:05Z. No send in the item 49 window.

## Blockers

None evidence-cited on this lane. Parked with owners in STATUS.md: IRPT_DASHBD plan items 1, 4, 5 (the SERIES
contract, DB-b-2, and the read route, DB-b-4: 2.0.0_SA_COO~P); W2-04/05 and row S40's portal half (2.0.0_SA_COO~Y);
W2-12/14 and W2-20 (2.0.0_SA_COO~M); W2-13, W2-15, W2-06 (1.0.0_SA_CTO).

## Current State

- Portal: origin DEV = local DEV = `970d5c75` (items 36-49 on AF-2 44fd5f42); PROD ba8e971f. 5174 serves the main
  checkout from pid 18500 (detached, PowerShell Start-Process; logs `portal/.runtmp/vite-smoke.log`); a reboot kills it.
- `portal/.vite/` holds a rebuilt `deps/` and 34 older `deps_temp_*` directories, left in place.
- Workspace: `org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md` current to item 49 @2eba103b88 (LOCAL on CLOUD); drive logs
  `drive_log_20260930T22Z_andrew.md` and `drive_log_20261001T00Z_andrew.md` committed there; row S42 in
  `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md`.
- Inbox watcher armed as Monitor bt33b9me3 at ~00:05Z (expires ~00:35Z); loop cron d49f1666 still armed.
- NOT verified: Andrew's exact search spelling against the live directory (needs his signed-in session); the cause
  of the cache directory's removal.

## Next Steps

- [Andrew] Reload 5174 and re-smoke DEV 970d5c75 (search while typing; Market Performance); the PROD promote follows.
- [0.0.0_AB_MSTR] The routed promote now carries 970d5c75 beyond the 63fb6318 named at 22:05Z: one product file
  (`header/ClientSearch.tsx`) plus two tests.
- [2.0.0_SA_COO~P] `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json`, a served `series.json.gz` and the read route
  un-park plan items 1, 4 and 5 here.
- [this lane] Resume the tick on Andrew's word; next-list position 0 is parked, so the tick is a NO-OP until a seam
  lands or Andrew adds an item.
