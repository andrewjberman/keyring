# TO POSN_ASTTAX.TO-W2-1 -- THE SATELLITES ADAPTER ATTACHES EACH HOLDING'S SERVED MEASURES (fee, aum, active, yield, duration, credit, beta, returns) FROM `characteristics.json`'s `tickers` BLOCK -- pass-through, NO arithmetic; a NULL renders blank, never "NO"; committed on the round's drain ref (AT6-s-2, F4; FWD-7 rendered)

<to_id>POSN_ASTTAX.TO-W2-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~25</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-15</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.10** @`59113e257a` (FWD-7,
C-HOLDING-MEASURES) - **Decomp cell:** `AT6-s-2` - **Issuance:** round 6, wave 2, slot `~25` -- **you start this order only after
`TO-W1-1` is `complete` at HEAD AND the served `characteristics.json` carries `tickers`** (the COO names the hash and the VersionId at
hand-over; W2-AC1 reads both back).

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~25`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~25;`. Your workspace worktree is
`/c/tmp/wk-posn-6-25` (branch `wk-posn_asttax-6-25`, a sparse cone; do NOT re-create it). Your portal worktree is
`/c/tmp/wk-posn-6-25/portal`, a linked worktree of the portal repo on YOUR branch `wk-posn-6-25-portal`, PRE-CUT by the COO FROM
`refs/drains/posn-6-portal` (verify with `git -C portal rev-parse --abbrev-ref HEAD` and `git -C portal merge-base --is-ancestor
refs/drains/posn-6-portal HEAD`); its `node_modules` is a junction to a sibling worktree's install (playwright-core 1.62.1 already
present; do not touch package.json). First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`.
Workspace commits via safe-commit.sh under your serial; portal commits inside `portal/` on your branch under your serial. Never push,
merge, rebase, `checkout --`, `clean`; never `git add portal`. Append your branch line to `ledger/PORTAL_REFS.md` at your first
portal commit. After every commit re-pin every PENDING-THIS-COMMIT row and validate STAGED (Z-S105).

## THE CELL

Andrew ~02:1xZ: *"no characteristics or performance in the 'Holdings Breakdown' panel"*. **FWD-7 ACCEPT:** an analyst opens a
satellite's Holdings Breakdown and sees each fund's fee, size, yield, beta and returns the way a model shows them -- blank only where
nothing prices that holding, never a blank column. **C-HOLDING-MEASURES:** the adapter attaches each row's served values to that row --
no arithmetic, no borrowing from another artifact.

**Measured at `dd1d33c6db` (the issuer; read it back at your ref):** the row type is `CurrentHolding` (`src/api/portal-proxy.ts:1062-1109`:
`fee?, aum? (millions), active? (0|1), yield?, duration?, credit?, beta?, returns?{1D,WTD,MTD,1M,1Q,QTD,YTD,1Y,3Y,5Y,SI}`); the
Satellites adapter's row literal `src/pages/Positioning/shared/satelliteAdapter.ts:262-282` carries EXACTLY FIVE keys (`ticker, name,
asset_class, sub_asset_class, weight`) -- every measure OMITTED; the book-level `characteristics` :314-320 IS served (`servedScalar`
:163 maps non-finite to null). The table `src/pages/Positioning/tabs/HoldingsTab.tsx:1166-1812` draws for satellites 7 characteristic
columns (`CHARACTERISTIC_FIELDS.satellites = {fee, duration, credit}` at `shared/bookSet.ts:447-456`; `charColCount` :888-889) and 8
performance windows; cells: Fee :1551 `(fee*100).toFixed(0)` else `-`; MC :1557 `(aum/1000).toFixed(1)` else `-`; Active :1561-1565
`active === 1 ? YES chip : NO` (**an undefined `active` renders "NO"** -- indistinguishable from a measured 0); Yield :1569; Duration
:1576 (`-` for Equity); Credit :1583; Beta :1590 (`-` for Fixed Income); performance :1597-1616 (`getHoldingPerformance(ticker)[period]`,
an em dash on null at :1604). The read `src/api/endpoints/satelliteRegistry.ts:232-269` joins the three artifacts; `SatelliteCharacteristicsResponse`
:168 carries no `tickers`; contract types in `shared/satelliteSet.ts:142-184`.

**Served input (schema READ BACK from the served bytes, never from this text):** `characteristics.json.tickers.<TICKER> = {fee, aum,
active, yield, duration, credit, beta, returns: {<window>: number|null}, source}` (TO-W1-1); `aum` in the same unit as Yang's
(millions); `active` 0|1|null; a NULL is "nothing prices it".

**Your act:**
1. `satelliteSet.ts`: the served `tickers` contract type beside the characteristics type (type-only; membership never hand-copied).
2. `satelliteRegistry.ts`: `SatelliteCharacteristicsResponse` gains `tickers` (REQUIRED once B6 is served -- a body without it THROWS
   like a null `as_of`, the honest branch; no default, no fallback).
3. `satelliteAdapter.ts`: the row literal ALSO carries `fee, aum, active, yield, duration, credit, beta, returns` read from
   `tickers[row.ticker]` -- pass-through, unit as served, a null or non-finite served value -> `undefined` (the same `servedScalar`
   discipline), `returns` copied per window; a ticker absent from `tickers` -> every measure `undefined` and the ticker COUNTED into
   `coverage` (disclosed, never guessed). **No `*`, `/`, `Math.`, `toFixed`, sum or blend anywhere in the attach** (W2-AC3 enumerates).
4. `HoldingsTab.tsx`, ONE hunk at :1561-1565: `active === 1` -> YES chip; `active === 0` -> NO; `active == null` -> `-` (blank, like
   its siblings). Models and ETFs rows always carry 0|1 today, so they render unchanged (W2-AC5 prints a Models row as the control).
5. `HoldingsTab.tsx`, the Satellites mode's OWN clock on the Holdings panels (C-SUMMARY-COPY's plain text: *"the Satellites mode's
   footer names holdings.json's as_of and Black Diamond as the source"* -- the mode draws TWO panel footers and two panel headers,
   all pinned to the models PKL clock today: :1085-1087 and :1169-1171 read `useDataSourceTimestamp('yang')` (:726); :1162 and :1811
   render `<SmartPanelFooter sourceKey="model_pkl" content="Source: Bloomberg." />`): in the Satellites mode ONLY, both footers read
   `Source: Black Diamond, holdings as of <satelliteData.as_of>` with no manifest key and both headers show that date and source;
   Models and ETFs byte-identical to today. The ISSUER'S READING, recorded as row `POSN_ASTTAX-Z-S136`: the CTO's L10 lists only the
   Summary's footer (F5, its own file); the same constraint's text reaches this panel and this file is yours -- a reader who holds the
   narrower reading files a row, and the change stays (it removes a false clock from the mode Andrew is reading tonight).
6. Nothing else: `PositioningSummary.tsx` and `Positioning.tsx` belong to `TO-W3-1` (F5) on a sibling branch; `bookSet.ts` unchanged.

**HAND-OVER FACTS:** (a) the fixtures for W2-AC5/W2-AC6 are built from the SERVED bytes (six keys, the shape of
`deliverables/0.9.0_WK_POSN_ASTTAX~19/build_fixtures_v8.js`; each key's VersionId printed; `characteristics.json` at its POST-B6
VersionId, `holdings.json` at `67GP52SdV1rw6QFVNPytU6ec4TvhwJh3` or later); (b) `scripts/ui-smoke.mjs` (:10-11 usage; `--fixtures`
:16-20 longest-substring wins; `--click` :224-251 in argv order; `--pick`/`--select` :285-287 for the satellite selector that exists
only after the click) runs against your dev server on `<PORT>`; the inert token 401s every `/api/*` (fixtures fill them); (c) the page
renders eight satellites (Opal Satellite 98 hidden by `Positioning.tsx:156`); (d) the edge caches the leaf for 60 s -- fixtures make
that irrelevant here.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, `POSN_ASTTAX-Z-W25-S<k>` (start at S1), appended to
`org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working.

## CRITERIA -- structured, one clause each

<criterion id="W2-AC1" cell_refs="AT6-s-2"><invocation>timeout 120 bash -c "f=\$(ls org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-W1-1.*.md); grep -o -m1 '<status>[^<]*</status>' \$f; .tools/aws s3api get-object --bucket opal-data-cot --key platinum/satellites/characteristics.json /c/tmp/wk-posn-6-25/.scratch/char_served.json --query '{v:VersionId,lm:LastModified}' --output json && PYTHONUTF8=1 python3 -c \"import json; d=json.load(open('/c/tmp/wk-posn-6-25/.scratch/char_served.json', encoding='utf-8')); t=d.get('tickers') or {}; print('tickers', len(t), 'sources', sorted(set(v.get('source') for v in t.values())))\"; git -C portal rev-parse refs/drains/posn-6-portal; git -C portal merge-base --is-ancestor refs/drains/posn-6-portal HEAD && echo REF-IS-ANCESTOR"</invocation><expect>TO-W1-1 reads `complete`; the served characteristics.json carries a non-empty `tickers` block (count and sources printed, VersionId printed); your portal HEAD descends from refs/drains/posn-6-portal. Any other reading: STOP with a row.</expect></criterion> `W2-AC1` -- THE UPSTREAM, READ BACK FROM THE SERVED BYTES.

<criterion id="W2-AC2" cell_refs="AT6-s-2"><invocation>timeout 60 git -C portal diff --stat refs/drains/posn-6-portal -- src</invocation><expect>exactly four files changed: src/pages/Positioning/shared/satelliteAdapter.ts, src/pages/Positioning/shared/satelliteSet.ts, src/api/endpoints/satelliteRegistry.ts, src/pages/Positioning/tabs/HoldingsTab.tsx (the Active cell hunk and the four Satellites-mode footer/header hunks, each named); the unscoped `git -C portal status --porcelain` shows the same four and nothing else; nothing under src/pages/Positioning/panels/ or Positioning.tsx (F5's files).</expect></criterion> `W2-AC2` -- FOUR FILES, DISJOINT FROM F5.

<criterion id="W2-AC3" cell_refs="AT6-s-2"><invocation>timeout 60 comp-read portal/src/pages/Positioning/shared/satelliteAdapter.ts --enumerate 'blendByIndex|renormal|positioning_data|toFixed|Math\.|\* *100|/ *100'</invocation><expect>ZERO hits for blendByIndex / renormal / positioning_data / toFixed / Math. in the attach path (the ENUMERATE denominator printed); any remaining hit is the existing pctToFraction or a comment, cited by line. The adapter computes no measure.</expect></criterion> `W2-AC3` -- NO ARITHMETIC IN THE ATTACH, BY ENUMERATION.

<criterion id="W2-AC4" cell_refs="AT6-s-2"><invocation>timeout 600 bash -c "cd portal && bun run tsc -b"</invocation><expect>exit 0 with the checked-file count; POSITIVE CONTROL: an injected type error fails the same command, then reverted.</expect></criterion> `W2-AC4` -- THE BUILD, WITH AN INSTRUMENT THAT CAN FAIL.

<criterion id="W2-AC5" cell_refs="AT6-s-2"><invocation>timeout 600 bash -c "cd portal && node scripts/ui-smoke.mjs positioning .scratch/w2_sat15.png --port <PORT> --fixtures <FIXTURES> --click 'Satellites' --pick 'Opal Satellite 15' && node scripts/ui-smoke.mjs positioning .scratch/w2_sat80.png --port <PORT> --fixtures <FIXTURES> --click 'Satellites' --pick 'Opal Satellite 80' && PYTHONUTF8=1 python3 <CELL_COMPARE> .scratch/w2_sat15.txt .scratch/w2_sat80.txt"</invocation><expect>the fixtures built from the SERVED bytes (six keys, VersionIds printed, characteristics.json POST-B6); both screenshots READ; the DOM's Holdings Breakdown rows dumped (the TEXT/DOM read the way W19's v8_ac10_dom_read did) and compared by <CELL_COMPARE> to the served tickers block under the renderer's own formatting: for EVERY row of Opal Satellite 15 and Opal Satellite 80 the 7 characteristic cells and 8 performance cells EQUAL the served value formatted as the table formats it (printed served vs rendered per cell, mismatches 0 of N with N printed); a NULL renders `-` (or the em dash for a return), never `NO` and never a raw float; CASH blank in every measure; GLD's return cells blank iff served null; ONE Models row printed as the control (Active still YES/NO for a 0|1). If the page's selector control is not a --pick target, read `ui-smoke.mjs:224-300`, use --select/--clicktext, and state which.</expect></criterion> `W2-AC5` -- THE RENDER, CELL BY CELL, AGAINST THE SERVED BLOCK.

<criterion id="W2-AC6" cell_refs="AT6-s-2"><invocation>timeout 600 bash -c "cd portal && PYTHONUTF8=1 python3 -c \"import json,sys; f=json.load(open('<FIXTURES>', encoding='utf-8')); k=[x for x in f if x.endswith('/satellites/characteristics.json')][0]; f[k].pop('tickers'); json.dump(f, open('<FIXTURES_NO_TICKERS>','w', encoding='utf-8'))\" && node scripts/ui-smoke.mjs positioning .scratch/w2_neg.png --port <PORT> --fixtures <FIXTURES_NO_TICKERS> --click 'Satellites' --pick 'Opal Satellite 15'"</invocation><expect>the DISCRIMINATING PAIR: with the tickers block REMOVED from the served-bytes fixture by a scripted key deletion (never a hand-written body) the read THROWS (the honest branch from step 2) and the page shows the error notice, not blank cells -- OR, if the COO's hand-over states the type stays optional, every measure cell renders `-`; state which branch the code takes and why. Either way the pair DIFFERS from W2-AC5, so the equality there is the attachment, not the renderer's default.</expect></criterion> `W2-AC6` -- THE NEGATIVE CONTROL: WITHOUT THE BLOCK, NO VALUES.

<criterion id="W2-AC7" cell_refs="AT6-s-2"><invocation>timeout 60 git -C portal log --format='%H %an %s' refs/drains/posn-6-portal..wk-posn-6-25-portal</invocation><expect>your commit(s) only under 0.9.0_WK_POSN_ASTTAX~25; the superproject gitlink UNMOVED read two ways at the worktree root: `git ls-tree HEAD -- portal` prints 160000 commit e85f6eb84f3a1771a37011a7e77e372570bad02a portal and `git diff --cached -- portal` is EMPTY; PORTAL_REFS.md carries your branch line.</expect></criterion> `W2-AC7` -- COMMITTED FROM THE REF; THE GITLINK UNMOVED.

<criterion id="W2-AC8" cell_refs="AT6-s-2"><invocation>timeout 600 bash -c "cd portal && node scripts/ui-smoke.mjs positioning .scratch/w2_footer_sats.png --port <PORT> --fixtures <FIXTURES> --click 'Satellites' && node scripts/ui-smoke.mjs positioning .scratch/w2_footer_models.png --port <PORT> --fixtures <FIXTURES>"</invocation><expect>in the Satellites run the TEXT dump's Holdings panel footers and headers carry `Black Diamond` and holdings.json's as_of at the fixture's VersionId (2026-09-14 or the served date, printed) and NOT `Bloomberg` for those two panels; in the Models run the same two footers and headers are byte-identical to the pre-change text (the control, diffed against a dump taken at refs/drains/posn-6-portal before your edit).</expect></criterion> `W2-AC8` -- THE HOLDINGS PANELS' CLOCK IS THE MODE'S OWN.

<criterion id="W2-AC9" cell_refs="AT6-s-2" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether attaching a fund-level fact (aum, fee) from Yang's row to a Black Diamond position row reads honestly to an analyst as "the fund's" and not "the position's"; and whether `-` for "nothing prices it" and `-` for "the column does not apply to this class" (Duration on Equity, Beta on Fixed Income) should stay one glyph. Record the readings and offer NO verdict.</expect></criterion> `W2-AC9` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>W2-AC1, W2-AC2, W2-AC3, W2-AC4, W2-AC5, W2-AC6, W2-AC7, W2-AC8, W2-AC9</expected_criteria>

<placeholders>CELL_COMPARE, FIXTURES, FIXTURES_NO_TICKERS, PORT</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-W2-1.satellites-adapter-attaches-per-ticker-measures.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~25/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D4/POSN/POSN_ASTTAX/ledger/PORTAL_REFS.md
portal/src/pages/Positioning/shared/satelliteAdapter.ts
portal/src/pages/Positioning/shared/satelliteSet.ts
portal/src/api/endpoints/satelliteRegistry.ts
portal/src/pages/Positioning/tabs/HoldingsTab.tsx
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round6.md</decomp_doc> round 6, cell `AT6-s-2`.
<owned_cells>AT6-s-2</owned_cells>
Read-dependencies, NOT claimed: `AT6-s-1` (the served tickers block -- read from the served bytes), `AT5-s-7` (the adapter you extend, on
the ref), `AT5-s-9` (the route, DEPLOYED). Sibling on the same ref, DISJOINT files: `AT6-s-3` (F5).
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- source edits inside the frozen submodule; no deploy, no promote, no monitor.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform; the reads go through the deployed route (B5's grant, not yours).
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the issuer has not read how getHoldingPerformance (HoldingsTab) resolves
a ticker's returns -- if it reads a map the adapter must ALSO populate, that map is in your grant only through the row's `returns`; a
second carrier is a row, not a silent widening; (2) the unit of `aum` in the MC column (`aum/1000`) is the renderer's, unchanged -- a
served aum in a different unit is a row against B6, never a conversion here; (3) whether `--pick` reaches the satellite selector is
unexercised by the issuer -- the fallback flags are named in the hand-over facts.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~25/POSN_ASTTAX.TO-W2-1.satellites-adapter-attaches-per-ticker-measures.proof_of_spec.json
</proof_of_spec>
