# AMGT_RESAPP task order -- `AMGT-ba-4` -- THE /freshness PAGE: THE SERVED STALE FLAG AND KEYED DATE, NO COLUMN FOR AN INPUT NOBODY HAS, THE NOTE AT READABLE CONTRAST, THE LISTS' OWNER LINE (FWD-7 RULINGS 1-2, FWD-14)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~270</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one page and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- the page reads one existing route through the existing API client.
comp-adversary: RUN by the issuer at the cut -- on portal DEV the page computes staleness itself (`freshnessRows.ts`) and counts a never-read input as stale, so 95 of 95 rows are flagged; "Last refreshed" shows the NEWEST input while the flag keys on the oldest; the Web search column reads "Not collected" on every row; the not-collected note is set in the muted text colour and reads 2.16:1 on white (row AMGT_RESAPP-Z-W262-S2); no owner line exists.
EGRESS CLASS, declared: NONE. Localhost only; no client data leaves the device.
</preflight>

**Your worktree:** `C:/tmp/r77-270` (branch `wk-AMGT_RESAPP-270`, cut from the issuer's tree, with `--portal-ref 13509c52 --node-modules link`: the portal DEV head, which carries the /freshness page). Work and commit only there. Start every shell call with `cd /c/tmp/r77-270`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout. The page lives in the nested portal repository: commit portal files inside `portal/` on its own branch `wk-AMGT_RESAPP-270-portal`, and name that commit in your report as the CANDIDATE.

## 1. THE ACT -- `AMGT-ba-4` (round 77, decomposition s.85)

CTO round-76 analysis @c8bbeeac10, rulings 1-2 and enrichment item 8. The rule now lives on the SERVER. The page renders
it and no longer decides staleness.

**The served contract** (cells ba-1, ba-2, ba-3 build it; cell ba-11 wires it). `GET /api/scoped/amgt/freshness?view=page`
returns:
- `rows`: the covered companies only, each with `covered`, `name`, `security_key`, `last_refreshed`, `per_input`
  (`bloomberg`, `seekingalpha`, `serp`: a compact UTC stamp, `NEVER` or null), `pack`, and the served rule:
  `stale` (boolean), `stale_inputs` (input names), `keyed_date` (YYYY-MM-DD, the oldest collected input, or null),
  `stale_reason` (plain words), `inputs` (`{<input>: {"state": "fresh"|"stale"|"not_collected", "day", "age_trading_days"}}`);
- `lists`: `{"owner_line": "<sentence>", "out_of_date": "<sentence>"}`;
- `generated_at`, `denominators.covered_read_error`.
Build against this contract with fixtures; the deployed function serves it only after the round's redeploy.

**What the page does.**
1. The client (`portal/src/api/endpoints/amgt-lead-panel.ts`, `getCoverageFreshness` and its two types) asks for
   `freshness?view=page` and types the fields above.
2. **The flag is the served `stale`.** The flags cell lists the served `stale_inputs` with each one's day ("Seeking Alpha
   last read 2026-09-11"). A never-collected input is never flagged.
3. **The date column shows `keyed_date`** (the oldest collected input), in an element with `data-slot="keyed-date"`. Its
   heading says what it is in plain words (for example "Oldest input"). A row with nothing collected reads "Nothing
   collected".
4. **An input no covered name has** (every row's state is `not_collected`) is NOT a column. It is stated once above the
   table, in the BODY text colour, never the muted one (4.5:1 or better). An input some names have and this name does not
   reads "Not collected" in that name's cell.
5. **The summary line** counts what is true: "N of M covered companies have an input older than 7 trading days."
6. **The lists.** Under the summary, the served `lists.owner_line` in an element with `data-slot="lists-owner"` and
   `lists.out_of_date` in one with `data-slot="lists-out-of-date"`. When `lists` is absent, neither element is drawn.
7. **A body with no served rule** (a row without `stale`: the function is not yet redeployed): the page shows the dates,
   flags nothing, and says once "Stale flags are not available yet." It does not fall back to its own rule.
8. The sorts keep working: stalest first orders by `keyed_date` (oldest first, nothing-collected last), then name.

**Tests** in `portal/src/pages/Freshness/Freshness.test.tsx` (`bun test src/pages/Freshness/`). Keep the cases that still
hold; rewrite the ones built on the old rule and say which in your report. Add five, named exactly:
`a never-collected input is not flagged`, `the date column shows the keyed date`,
`an input no covered name has is not a column`, `the lists owner line is shown`,
`the lists out-of-date statement is shown`.

**NOT in this cell:** the `/refresh` control. It is on the Security Analysis page
(`portal/src/pages/SecurityAnalysis/SecurityAnalysis.tsx:72`, `hooks/useLeadPanelApi.ts:130`), which is the DSGN lane's
page. Leave `requestRefresh` in the client file as it is.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W270-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no push of the portal branch, no `App.tsx` or nav edit.
2. Colours come from the design system's tokens only (`portal/DESIGN.md`): the light canvas, white hairline panels, navy ink. No light text off the band.
3. Words a person reads are plain. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
portal/src/pages/Freshness/
portal/src/api/endpoints/amgt-lead-panel.ts
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~270/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba4.py" --crit AC1 --portal portal; echo "exit=$?"</invocation><expect>the five new cases are in the test file by name and `bun test src/pages/Freshness/` reads 0 fail; C1-C2 PASS; R77 BA4 AC1 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba4.py" --crit AC2 --portal portal; echo "exit=$?"</invocation><expect>the client asks for the page view; the page renders the served flag and keyed date; the note is not in the muted colour; the head is drawn from the inputs some name has; the two list slots exist; C1-C5 PASS; R77 BA4 AC2 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ba-4" judgment="true"/>
</proof_of_spec>

AC3 is the read of the rendered page. Render it with `node scripts/ui-smoke.mjs /freshness <out.png> --dist dist --fixtures
<fixtures.json>` after `bun run build` in your portal (no login, no port). Use a fixture body in the contract's shape with
at least one stale row, one not-stale row and one row with nothing collected. Copy the captures and the fixture into
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~270/render/`, and say in the record that the body is a fixture.

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~270 <0.9.0_WK_AMGT_RESAPP~270@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~270/AMGT_RESAPP.TO-AMGT-ba-4.freshness-page-served-flag-and-owner-line.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal` in the outer repository.
Report once:
- the outer commit hash and the portal CANDIDATE commit (its hash, the files, and that it merges clean onto the portal ref you were cut from);
- every criterion's output lines;
- `bun test src/pages/Freshness/` last lines, and `bun run typecheck` last line;
- the existing test cases you rewrote and why;
- the captures and what each shows;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-76 analysis @c8bbeeac10 rulings 1-2 and enrichment items 1 and 8 (page half); row Z-W262-S2 closes here. Wave 1 (staged): the page is built against the contract stated on this face, so it has no build-time edge on ba-1..ba-3; it is staged because its candidate should carry the contract as those cells actually export it, and its DEV exercise (ruling 2: one visit with a stale and a not-stale row) follows the adapter cell ba-11 and the redeploy. Checks dry-run at the base against the portal DEV files (origin/DEV 13509c52 exported): AC1 FAIL as expected (0 of 5 cases), AC2 FAIL as expected (C1-C5 fail). The candidate reaches DEV as a portal change touching product files: the CTO reviews it from the render, then the DEV push is the integrator's on Andrew's word. The /refresh control is NOT here: it is on the DSGN lane's Security Analysis page.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~270</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete -- drained @fb793b7a71; proof VALID (worktree checker); the /freshness page draws the served stale flag and keyed date, drops a column no name has, the owner line and out-of-date sentence; portal candidate 504ddb3d on 13509c52 (branch resapp-r77-ba4-freshness, LOCAL); AC1 17 tests, AC2 5 of 5; AC3 is the CTO's render review</status>
