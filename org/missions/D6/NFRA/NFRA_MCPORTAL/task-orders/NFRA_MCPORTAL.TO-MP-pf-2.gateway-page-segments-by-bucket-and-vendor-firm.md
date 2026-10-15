# NFRA_MCPORTAL task order -- `MP-pf-2` -- WORKSTREAM PF ROUND 1: the Gateway page shows each bucket as a clear segment and each assets/bd vendor-firm pair as a sub-segment

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pf-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pf-2</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~33</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a front-end bundle; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- a front-end bundle; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (a firm that is multi, none or unresolved; a bucket with no segments; a wide tool table).
EGRESS CLASS, declared: none. Every fetch in a test is a stub.
</preflight>

## 1. THE CELL -- `MP-pf-2` (workstream PF round 1, decomposition section PF.2)

You have two worktrees, nested:
- the workspace worktree `C:/tmp/mp-pf-33`, branch `wk-NFRA_MCPORTAL-pf-33`;
- inside it, the mcportal worktree `C:/tmp/mp-pf-33/mcportal`, branch `wk-NFRA_MCPORTAL-pf-33-mcportal`, based on mcportal `2fdfb607d7` (the commit live on origin DEV today).
  `node_modules` is linked. Do not run `bun install` or `bun add`.

All your code changes are in the mcportal worktree. Commit them there with plain `git commit`, author `0.9.0_WK_NFRA_MCPORTAL~33 <0.9.0_WK_NFRA_MCPORTAL~33@opal.agent>`.
mcportal is its own repo, outside the workspace's safe-commit lanes. Your proof-of-spec instance and any surprise row are committed in the workspace worktree via
`.tools/safe-commit.sh`. Never push either repo. Make NO network call of any kind.

**What Andrew asked for** (his words): "making sure everything is extremely legible, clean, and well-designed, using the opalinvest.com website design fixtures, as well as making sure
that everything is readable by human eyes and not wrapped or squished on text and segments. The most important thing is really that each displayed tool segment is very clearly
segmented, i recommend this being by bucket, and in the case of opal-data-assets, by client/vendor pairs."

**Today's page** (read first): `src/pages/gateway/GatewayView.tsx`, `gateway.css`, `gateway.test.tsx` (its way of rendering with `renderToStaticMarkup`, its fixtures) and `src/api/admin.ts`. It shows a
header line, a summary table and one section per `channels[]` entry. A channel of kind `bucket` is an AWS bucket (its `id` and `name` are the bucket name, e.g. `opal-data-harvest`).

**The server's contract** (fixed; build against it exactly). A `channels[]` entry whose `id` is `opal-data-assets` or `opal-data-bd` MAY carry `segments`: a list of
`{ "vendor": string, "firm": string, "tools": string[] }`, one entry per (vendor, firm) pair, already in display order, each tool name listed once, in the channel's `tools[]` too. Any other
channel has NO `segments` key. The server fills it later; until then you build against a checked-in fixture. Vendor values: `schwab`, `blackdiamond`, `orion`, `eclipse`, `smartx`,
`commonwealth`, `gateway`, `market`, or `unresolved`. Firm values: `49financial`, `cottonwood`, `inflection`, `multi`, `none`, `unresolved`. Any other value is shown as given.

Build:
1. **`src/api/admin.ts`**: `GatewayChannel` gains `segments?: GatewaySegment[]`, with `export interface GatewaySegment { vendor: string; firm: string; tools: string[] }`. Optional, so a response of today still parses.
2. **A fixture file `src/pages/gateway/gateway.cgroup.fixture.ts`** exporting `CGROUP_BREAKDOWN: GatewayBreakdown` (use the existing breakdown type; copy the field shapes of the existing test fixture): channels, in this order,
   `opal-data-assets` (kind `bucket`, with segments Schwab/49financial, Schwab/cottonwood, Black Diamond/cottonwood, Commonwealth/cottonwood, SmartX/multi, Market/none, and one unresolved/unresolved; 2 to 4 tools in each, real-looking
   names such as `schwab_get_positions`), `opal-data-bd` (segment Black Diamond/49financial), `opal-data-harvest` (no segments), then one `integration` channel, the `m365` `native` channel, and the `undeclared` channel.
   Give the channels holders and ratings like the existing fixture so the page has data. The tests and the issuer's screenshots both use this fixture.
3. **`GatewayView.tsx`** (and `gateway.css`):
   - **Words.** Vendor words: `schwab` `Schwab`; `blackdiamond` `Black Diamond`; `orion` `Orion`; `eclipse` `Eclipse`; `smartx` `SmartX`; `commonwealth` `Commonwealth`; `gateway` `Tax SMA`; `market` `Market data`;
     `unresolved` `Vendor not resolved`; any other value as given. Firm words: `49financial` `49 Financial`; `cottonwood` `Cottonwood`; `inflection` `Inflection`; `multi` `Several firms`; `none` `No firm`;
     `unresolved` `Firm not resolved`; any other as given.
   - **A bucket WITH `segments`.** Inside its section, after the facts line, one sub-section per segment, in the order received, as an element with `id="gateway-<channel id>--<vendor>--<firm>"` and `data-segment`,
     with a heading `<vendor words> / <firm words>` (for example `Schwab / 49 Financial`) and its tool count (`3 tools`, `1 tool`), then that segment's own tools table: the rows of the channel's `tools[]`
     whose names are in the segment's `tools`. A segment whose firm is `multi` shows one line under its heading: `One object mixes firms; the tools filter rows by firm.`; `none`: `Not a client source.`;
     `unresolved` (firm or vendor): `The catalog did not resolve a firm for these tools; a gap, not a firm.` in the existing `gateway-gap` red class. A bucket's own tools table is NOT shown a second time.
   - **A bucket WITHOUT `segments`** renders exactly as it does today.
   - **Summary table.** Keep one row per channel. Under a segmented bucket's row add one indented row per segment: the Group cell is a link `<a href="#gateway-<channel id>--<vendor>--<firm>">` with the segment heading,
     Kind reads `Segment`, Tools is the segment's count, Holders is empty. The header line's group count stays the number of channels (segments are not groups).
   - **Not squished, not wrapped.** Every tools table sits inside a `<div className="gateway-scroll">` with `overflow-x: auto`; tool and index names are `white-space: nowrap`; at 390 px width the PAGE never scrolls
     sideways (the table scrolls inside its box). A section or segment heading may wrap between words only (`overflow-wrap: normal; word-break: normal`). Each segment has clear space around it: a hairline-bordered panel
     inside its bucket panel, `margin-top` of one grid step, a heading line above the table. No text is cut off with an ellipsis.
   - **Design.** Follow `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md` (READ it; read-only; it is outside your worktree) and the existing page: light canvas, white hairline panels, navy ink `#163372` (tokens only:
     `var(--color-ink, #163372)` style), one band per page. Links in the summary table keep the navy ink with underline (`.gateway-summary a`). No new colour, no new font, no new dependency, no timer, no alert, no write.

**Tests**, by these exact names (bun 1.3.x prints a name only on FAILURE, so the check reads the names from your sources; put each name as the literal first argument of its `test(...)`), in
`src/pages/gateway/gateway.test.tsx` using `renderToStaticMarkup` and `CGROUP_BREAKDOWN`:
- `a segmented bucket renders one sub-section per vendor and firm`: the `opal-data-assets` section holds one `data-segment` element per fixture segment, in the fixture order, each with its `id`;
- `a segment heading reads vendor words slash firm words`: the markup holds `Schwab / 49 Financial`, `Black Diamond / Cottonwood`, `SmartX / Several firms` and `Market data / No firm`;
- `multi none and unresolved firms are labelled segments with their reason`: the three reason lines appear once each, and the unresolved line sits in an element with the class `gateway-gap`;
- `the summary table lists each segment under its bucket with a link`: each segment has a `href="#gateway-opal-data-assets--<vendor>--<firm>"` in the summary table and a section with that same `id`, and the header still reads the
  channel count of the fixture;
- `a bucket with no segments renders as before`: `opal-data-harvest` has no `data-segment`, and its tools table is present once;
- `every tools table sits in a scroll container`: every `<table` of a tools table in the markup is inside `gateway-scroll`, and `gateway.css` holds `overflow-x: auto` for `.gateway-scroll` and `white-space: nowrap` for the tool name cell class you use.
The existing gateway tests and `routes json equals the app routes` must still pass. If an existing assertion pins markup this contract changes, change only that assertion to the new truth and name each change in your report.

**AMENDMENT 1 (issuer, after rendering your build at 1280 px and 390 px and LOOKING at it; these are my spec's faults, not yours; you are re-seated on this branch with your commits `89dd5f5` (mcportal) and `6f5b1d9b4d` (workspace) as inherited state).**
   At 390 px the text is squished letter by letter: the summary table's headers read `To ol s` and `Hol der s`, `Commonwealth` breaks mid-word, `no one` breaks into three lines, and a segment's tools table breaks `Access` and `Data class` and every `transactions` cell one letter per line.
   My spec only made tool and index NAMES non-wrapping and put no scroll box around the summary table. Fix, in `gateway.css` and `GatewayView.tsx` only:
   a. **Every table on the page keeps each cell's text on one line.** In `gateway.css`, `.gateway-scroll th, .gateway-scroll td` take `white-space: nowrap`; `.gateway-scroll table` takes `min-width: max-content` (and keeps `width: 100%`), so a narrow screen scrolls the box and never squeezes a column. This applies to the tools tables, the holders tables and the summary table.
   b. **The summary table sits in a `<div className="gateway-scroll">` too** (it is the one table that does not today). Its Group links never break inside a word (they are cell text, so rule a covers them).
   c. **Section and segment headings may wrap between words only** (as the order already says); check this at 390 px and change nothing if it already holds.
   d. **The page title.** Read `C:/tmp/mp-pf-33/portal/DESIGN.md` for the page-title style (size, weight, ink) and make the `Gateway` `<h1>` use it, with the existing tokens only. Today it renders as the browser's default 2em black heading while every section heading is navy. If DESIGN.md names no page-title style, make it the same navy ink as the section headings at one size larger than them and say so in your report. Do not touch the Refresh button.
   e. **Tests.** Add ONE test, named exactly `every table cell keeps its text on one line`: `gateway.css` holds `white-space: nowrap` for `.gateway-scroll th, .gateway-scroll td` and `min-width: max-content` for `.gateway-scroll table`; and every `<table` in the fixture markup (summary, tools, holders) is inside `gateway-scroll`. The test `every tools table sits in a scroll container` keeps its name and meaning. AC1 now reads SEVEN named tests and 68 or more pass.
   Re-run AC1, `tsc --noEmit -p tsconfig.app.json` and `bun run build`, re-write the instance, run `proof-of-spec-check.py` on it, commit as before, and report once. The check script and the proof lines are the issuer's; do not edit them.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `package.json`, `bun.lock`, any gateway (Python) file, Terraform or the manifest. Make no deploy and no network call.
2. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion.
3. Standing rules: no push and no vendor call. Commit the mcportal files with plain `git commit` in the nested worktree and the workspace files via
   `.tools/safe-commit.sh`, each with your serial as author (CLAUDE.md 14a). If you cannot meet a criterion as written, REFUSE it with its measurement.

## 3. SURFACES

<paths>
mcportal/src/pages/gateway/
mcportal/src/api/admin.ts
mcportal/src/api/admin.test.ts
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~33/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other mcportal file, `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/DESIGN.md`, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W33-S<k>` (k from 1).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your WORKSPACE worktree root `C:/tmp/mp-pf-33` after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pf-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/pf2.AC1.sh; echo "exit=$?"</invocation><expect>named tests present in sources 7 of 7.*fail=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pf-2" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~33/NFRA_MCPORTAL.TO-MP-pf-2.gateway-page-segments-by-bucket-and-vendor-firm.proof_of_spec.json`
(AC2 is a judgment criterion: record it under UNVERIFIABLE-BY-INSTRUMENT with no verdict).
Report once, with:
- the check output;
- the mcportal commit hash or hashes, and the workspace commit hash;
- every existing assertion you had to change (file, test, old, new), or none;
- `tsc --noEmit -p tsconfig.app.json` in the nested worktree (rc) and `bun run build` (rc);
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PF issuance (decomposition v12) from PRD v0.9 @532d1e68bb and the CTO's GO (msg 34553), Andrew's word of ~19:2xZ. Done by 2026-10-16 ~22:00Z. The drain runs `bun run build` and `tsc -b` once, then I
render the fixture at 1280 and 390 px with headless Edge, one screenshot per segment, and look at each. Check dry-run at the base: AC1 FAIL as expected (`mcportal/src/pages/gateway` absent in the issuer's checkout; the base in the worker's
nested tree reads 0 of 6 names). The segments appear on the live page only after MP-pf-1 and MP-pe-1 are released by 2.0.0_SA_COO~O and MCPINDEX's first C-GROUP catalog release lands.

<status>pending</status>
<round>1</round>
<workstream>PF</workstream>
<slot>~33</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
