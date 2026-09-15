# TO POSN_ASTTAX.TO-W3-1 -- THE POSITIONING SUMMARY DERIVES ONE PRESENCE SET PER RENDER (legend, Asset Class rows, count and bars list only the classes a drawn column holds); the third percent label rounds; the Satellites mode's footer names Black Diamond and `holdings.json`'s as_of; the subtitle and notices stop describing the removed blend; committed on the round's drain ref (AT6-s-3, F5; C-PRESENT-CLASSES, C-SUMMARY-COPY; FWD-6, FWD-3)

<to_id>POSN_ASTTAX.TO-W3-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~26</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-15</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.11** @`ab2ee8052a`
(C-PRESENT-CLASSES, C-SUMMARY-COPY as clarified at v0.11; FWD-6's DONE WHEN carries the presence rule; AMENDED ~04:1xZ -- act 2 and
the label clauses of W3-AC5 / W3-AC6, Z-S138 / Z-S140) - **Decomp cell:** `AT6-s-3` - **Issuance:** round 6,
wave 1, slot `~26` -- runs in PARALLEL with `TO-W1-1` and `TO-W2-1`; your files are DISJOINT from F4's by construction.

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~26`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~26;`. Your workspace worktree is
`/c/tmp/wk-posn-6-26` (branch `wk-posn_asttax-6-26`, a sparse cone; do NOT re-create it). Your portal worktree is
`/c/tmp/wk-posn-6-26/portal`, a linked worktree of the portal repo on YOUR branch `wk-posn-6-26-portal`, PRE-CUT by the COO FROM
`refs/drains/posn-6-portal` (verify with `git -C portal rev-parse --abbrev-ref HEAD` and `git -C portal merge-base --is-ancestor
refs/drains/posn-6-portal HEAD`); its `node_modules` is a junction to a sibling worktree's install (playwright-core 1.62.1 present; do
not touch package.json). First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`. Workspace
commits via safe-commit.sh under your serial; portal commits inside `portal/` on your branch under your serial. Never push, merge,
rebase, `checkout --`, `clean`; never `git add portal`. Append your branch line to `ledger/PORTAL_REFS.md` at your first portal
commit. After every commit re-pin every PENDING-THIS-COMMIT row and validate STAGED (Z-S105).

## THE CELL

Andrew ~00:4xZ: *"There is no need to display the different legend categories if they do not appear in the view"*; ~02:1xZ: *"if none of
the models/ETFs/satellites have a given asset class (e.g. Alternatives) then no Alternatives row should be shown ... showing all the
floats"*. **C-PRESENT-CLASSES:** ONE presence set per render -- the classes with a non-zero value in ANY column the current view draws --
and the legend, the Asset Class rows and the section count list exactly that set, in `ASSET_CLASSES` order and colours (keyed by class
name, so hiding a class shifts no colour); per mode, never across modes; the zero-row design comment goes with the behaviour.
**C-SUMMARY-COPY:** the third percent label rounds like its siblings; the Satellites mode's footer names `holdings.json`'s `as_of` and
Black Diamond as the source, Models and ETFs unchanged; the Satellites subtitle and unresolved notice stop describing the removed blend.

**Measured at `dd1d33c6db` (the issuer; read it back at your ref):** `src/pages/Positioning/panels/PositioningSummary.tsx` (1385 lines):
`ASSET_CLASSES` :79-92 (five entries; `color: ASSET_CLASS.<key>` from `src/lib/chartColors.ts:115-126`, keyed by class name);
the enumeration sites -- the N/A rows :252, the Asset Class rows :578-582 (the zero-row comment :575-577), the section count :850
(`section.rows.length`), the bars :925-943 (relative), :952-961 (stacked), :966-976 (ghost), the labels :988/:993 (`Math.round`,
the Custom pair), :1002-1004 (`toFixed(1)`, the signed relative delta), :1010-1011 (`{data[c.key]}%` RAW), the legend :1159-1170;
the drawn columns -- `books` :627-629, values `getAllocationData(id, mode)` :660-681 (portfolio; benchmark :669; relative :672-676),
`getClassValues` :262-282, the custom column `withCustom` :230-242 (`'--'` on an invalid blend), gated by `caps` :623 and
`viewSupported` :697-699; the footer :1382 `<SmartPanelFooter sourceKey="model_pkl" content="Source: Bloomberg." />` HARDCODED for
every mode (`src/ui/components/panels/SmartPanelFooter.tsx:49-84` for its props). `src/pages/Positioning/Positioning.tsx` (645 lines):
`MODE_DESCRIPTIONS.satellites` :123-125 (*"...each a weighted blend of Opal model portfolios"*); the `models-unavailable` notice copy
:219-221 (*"blended from"*); the unresolved notice :616-622 (*"...blended over their remaining legs only"*); `dataAsOf` :481 =
`activeData.data_as_of` = `holdings_as_of` for satellites (`satelliteAdapter.ts:336, :366-369`); `REGISTERS_YANG_AS_OF.satellites =
false` :491-495 (unchanged -- the Yang registry is not the satellites' clock).

**Your act:**
1. `PositioningSummary.tsx`: ONE exported pure helper, e.g. `presentClassKeys(columns: Record<ClassKey, number>[]): ClassKey[]`, over
   every column the current view draws -- the `books` portfolio values; the benchmark values when the Benchmark or Relative view is on;
   the custom column when the blend is valid -- returning the `ASSET_CLASSES` keys (in order) with a non-zero finite value in ANY of them;
   computed ONCE per render and applied to the Asset Class rows (:578-582), the section count (:850 follows the rows), the bars and
   their labels (:925-1011), and the legend (:1159-1170). `ASSET_CLASSES`, its order and colours UNTOUCHED; sub-category rows UNTOUCHED;
   Management Style / Characteristics sections UNTOUCHED. The comment :575-577 REMOVED with the behaviour. A mode whose every drawn column
   is zero for every class renders the existing no-data state, never an empty section.
2. `PositioningSummary.tsx` :1011 (v0.11, C-SUMMARY-COPY clarified; "like its two siblings" WITHDRAWN, Z-S138): the single-bar percent
   label renders the value at NO MORE THAN TWO DECIMALS, TRAILING ZEROS DROPPED -- the defect is the IEEE artifact of summing served
   two-decimal weights (`62.589999999999996%`); the fix keeps the precision the served rows carry (Satellites `62.59%`, `29.82%`,
   `90.24%`; Models and ETFs labels BYTE-IDENTICAL to today: `82.6%`, `17.4%`). One small pure formatter (e.g. `String(Number(v.toFixed(2)))`
   or equivalent yielding `62.59`, `82.6` and `90` for 90.00), applied at :1011 only; the Custom pair (:989/:994) and the relative delta
   (:1004) untouched. Never `Math.round` here.
3. `PositioningSummary.tsx` :1382: the footer chosen by `mode` -- satellites: `content="Source: Black Diamond, holdings as of <data_as_of>"`
   with NO manifest key (the models PKL clock is not this mode's); models and etfs: byte-identical to today.
4. `Positioning.tsx`: `MODE_DESCRIPTIONS.satellites` names Black Diamond holdings and no blend; the unresolved notice (:616-622) names a
   satellite with no served holdings and no blend; the `models-unavailable` copy (:219-221) likewise -- a third string describing the
   retired blend in the same file under the same constraint (state it once in your report; a reader who wants it out of scope files a row).
5. Nothing else: `HoldingsTab.tsx` and the adapter files belong to `TO-W2-1` (F4) on a sibling branch.

**HAND-OVER FACTS:** (a) fixtures for the renders are built from the SERVED bytes (six keys, the shape of
`deliverables/0.9.0_WK_POSN_ASTTAX~19/build_fixtures_v8.js`; each key's VersionId printed; `holdings.json` at
`67GP52SdV1rw6QFVNPytU6ec4TvhwJh3` or later -- the POST-R2 labels: GLD commodities/Metals, VXX structured/Hedge); (b) `scripts/ui-smoke.mjs`
(:10-11 usage; `--fixtures` :16-20; `--click` :224-251 in argv order; the view toggles are buttons named Benchmark / Relative / Custom
gated by `caps`) against your dev server on `<PORT>`; (c) the Models mode holds no Commodities and no Alternatives in any book today
(the CTO's read at L10: three classes present); the Satellites mode after R2 holds four; (d) the ETFs mode is read and printed with
no expectation beyond "no class outside the five, no zero row".

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, `POSN_ASTTAX-Z-W26-S<k>` (start at S1), appended to
`org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working.

## CRITERIA -- structured, one clause each

<criterion id="W3-AC1" cell_refs="AT6-s-3"><invocation>timeout 120 bash -c "git -C portal rev-parse refs/drains/posn-6-portal; git -C portal merge-base --is-ancestor refs/drains/posn-6-portal HEAD && echo REF-IS-ANCESTOR; .tools/aws s3api head-object --bucket opal-data-cot --key platinum/satellites/holdings.json --query '{v:VersionId,lm:LastModified}' --output json; python3 .tools/prd-signoff.py status POSN_ASTTAX"</invocation><expect>your portal HEAD descends from refs/drains/posn-6-portal (which is dd1d33c6db or a descendant); the served holdings.json VersionId is 67GP52SdV1rw6QFVNPytU6ec4TvhwJh3 or later (printed); the PRD reads ADMITTED at the pinned hash. Any other reading: STOP with a row.</expect></criterion> `W3-AC1` -- THE REF, THE SERVED LABELS, THE PIN.

<criterion id="W3-AC2" cell_refs="AT6-s-3"><invocation>timeout 60 git -C portal diff --stat refs/drains/posn-6-portal -- src</invocation><expect>exactly two files changed: src/pages/Positioning/panels/PositioningSummary.tsx and src/pages/Positioning/Positioning.tsx; the unscoped `git -C portal status --porcelain` shows the same two and nothing else; nothing under shared/, tabs/ or src/api (F4's files).</expect></criterion> `W3-AC2` -- TWO FILES, DISJOINT FROM F4.

<criterion id="W3-AC3" cell_refs="AT6-s-3"><invocation>timeout 300 bash -c "cd portal && bun <PRESENCE_UNIT_CONTROL>"</invocation><expect>a script in your deliverables that imports the exported helper and runs it over CONSTRUCTED column sets (a unit control on a pure function, not a render fixture): (a) a class non-zero ONLY in the benchmark column is PRESENT; (b) a class zero in every column is ABSENT; (c) the result preserves ASSET_CLASSES order; (d) a non-finite value counts as zero; (e) an empty column list returns an empty set; every case printed PASS with its input, and a deliberately wrong expectation printed FAIL (the control that the harness can fail).</expect></criterion> `W3-AC3` -- THE PRESENCE RULE, EXERCISED ON ITS EDGES.

<criterion id="W3-AC4" cell_refs="AT6-s-3"><invocation>timeout 600 bash -c "cd portal && bun run tsc -b"</invocation><expect>exit 0 with the checked-file count; POSITIVE CONTROL: an injected type error fails the same command, then reverted.</expect></criterion> `W3-AC4` -- THE BUILD, WITH AN INSTRUMENT THAT CAN FAIL.

<criterion id="W3-AC5" cell_refs="AT6-s-3"><invocation>timeout 600 bash -c "cd portal && node scripts/ui-smoke.mjs positioning .scratch/w3_models.png --port <PORT> --fixtures <FIXTURES> && node scripts/ui-smoke.mjs positioning .scratch/w3_models_bench.png --port <PORT> --fixtures <FIXTURES> --click 'Benchmark' && node scripts/ui-smoke.mjs positioning .scratch/w3_etfs.png --port <PORT> --fixtures <FIXTURES> --click 'ETFs'"</invocation><expect>fixtures from the SERVED bytes (VersionIds printed); screenshots READ: Models -- the legend and the Asset Class rows list exactly Fixed Income, Equity, Structured (3), the section count reads (3), no zero row, no Commodities, no Alternatives; the Benchmark view -- the set printed and EXPLAINED from the fixture's benchmark allocations (a class present only in the benchmark column appears; if none exists in today's bytes, say so -- W3-AC3 carries that edge); ETFs -- the set printed, every class one of the five, no zero row; every single-bar percent label in the TEXT dump matches ^[0-9]+(\.[0-9]{1,2})?%$ (the label count and the match count printed, equal; zero labels with three or more decimals); the Models labels (82.6%, 17.4% and the rest) BYTE-IDENTICAL to a dump of the same view taken at refs/drains/posn-6-portal before your edit (the control, both dumps kept in your deliverables).</expect></criterion> `W3-AC5` -- MODELS AND ETFS: ONLY THE CLASSES A VIEW HOLDS; NO RAW FLOAT.

<criterion id="W3-AC6" cell_refs="AT6-s-3"><invocation>timeout 600 bash -c "cd portal && node scripts/ui-smoke.mjs positioning .scratch/w3_sats.png --port <PORT> --fixtures <FIXTURES> --click 'Satellites'"</invocation><expect>the screenshot READ: the legend and the Asset Class rows list exactly Fixed Income, Equity, Structured, Commodities (4) in ASSET_CLASSES order with the same colours as the Models render for the shared classes (the two PNGs compared by eye and the DOM's colour tokens printed); the section count reads (4); the Satellites single-bar labels read to two decimals trimmed (62.59% / 29.82% / 90.24% for the fixture's served sums, or whatever the served rows sum to, printed beside the raw sum); the footer text carries `Black Diamond` and `2026-09-14` (holdings.json's as_of at the fixture's VersionId) and NOT `Bloomberg`; the subtitle and every notice text carry no `blend`; the Models render's footer is byte-identical to the pre-change text (the control).</expect></criterion> `W3-AC6` -- SATELLITES: FOUR CLASSES, THE MODE'S OWN FOOTER AND COPY.

<criterion id="W3-AC7" cell_refs="AT6-s-3"><invocation>timeout 60 git -C portal log --format='%H %an %s' refs/drains/posn-6-portal..wk-posn-6-26-portal</invocation><expect>your commit(s) only under 0.9.0_WK_POSN_ASTTAX~26; the superproject gitlink UNMOVED read two ways at the worktree root: `git ls-tree HEAD -- portal` prints 160000 commit e85f6eb84f3a1771a37011a7e77e372570bad02a portal and `git diff --cached -- portal` is EMPTY; PORTAL_REFS.md carries your branch line.</expect></criterion> `W3-AC7` -- COMMITTED FROM THE REF; THE GITLINK UNMOVED.

<criterion id="W3-AC8" cell_refs="AT6-s-3" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether an absent class row reads to an analyst as "this book holds none" (Andrew's intent) rather than "this class does not exist", now that the zero row is gone; and whether Math.round on the single-bar label loses a distinction a 0.4% sleeve carried. Record the readings and offer NO verdict.</expect></criterion> `W3-AC8` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>W3-AC1, W3-AC2, W3-AC3, W3-AC4, W3-AC5, W3-AC6, W3-AC7, W3-AC8</expected_criteria>

<placeholders>FIXTURES, PORT, PRESENCE_UNIT_CONTROL</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-W3-1.positioning-summary-presence-rounding-footer-copy.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~26/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D4/POSN/POSN_ASTTAX/ledger/PORTAL_REFS.md
portal/src/pages/Positioning/panels/PositioningSummary.tsx
portal/src/pages/Positioning/Positioning.tsx
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round6.md</decomp_doc> round 6, cell `AT6-s-3`.
<owned_cells>AT6-s-3</owned_cells>
Read-dependencies, NOT claimed: `AT5-s-5` (the colour registry), `AT5-s-6` (the five-class page you filter), `AT5-s-7` (the Satellites
adapter's data_as_of). Sibling on the same ref, DISJOINT files: `AT6-s-2` (F4).
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- source edits inside the frozen submodule; no deploy, no promote, no monitor.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the issuer has not read whether the bars' column alignment
(`books` order, :1202-1213) survives a class filter -- a mis-aligned bar is a row and a fix inside this cell; (2) SmartPanelFooter's
props are read by you, not the issuer -- if it cannot render without a manifest key, a row and the honest fallback (a plain footer
line) inside this cell; (3) whether the Custom view's `'--'` string (:238) reaches the presence helper as NaN is unexercised -- W3-AC3(d)
is the control.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~26/POSN_ASTTAX.TO-W3-1.positioning-summary-presence-rounding-footer-copy.proof_of_spec.json
</proof_of_spec>
