# AMGT_RESAPP task order -- `AMGT-rk-78` -- the Exec Management tab renders a Bloomberg FALLBACK roster as what it is: the source, and the filing roster's own status and failure reason beside the officers, and a Confirmed cell that never says "confirmed from the filing" for an officer Bloomberg supplied; a RESOLVED roster and every ABSENT block render byte-for-byte as today

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-78</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~78</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this order edits one portal tab, its type file and a new static-render
  harness, and reads four served payloads by direct invoke; it arms no cron, alarm, monitor or cadence, reads no
  schedule and writes none, and opens no deploy-ledger entry (it deploys nothing: no push, no DEV or PROD move).
comp-iam: DECLARED-NOT-APPLICABLE -- the only AWS call is lambda:InvokeFunction on opal-amgt-scoped-api for four
  GET leaves (AC1), under the seat's existing credentials exactly as AMGT-rk-74's route census invoked it; no role,
  policy or grant is read or changed, and no S3 object is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- this is a task-order specification, not a produced artifact; the
  validator-context declaration applies to the worker's own deliverable at drain, not to the order that
  specifies it.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~78`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt
(call it `<wt>`). Your first act prints `git rev-parse --abbrev-ref HEAD`, `git rev-parse --show-toplevel` and
`git -C portal rev-parse --abbrev-ref HEAD` from `<wt>`, and tests that `org/`, `.tools/`, `lib/`,
`portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx` and `portal/node_modules/typescript` exist; if any is
absent, STOP with a BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~78;`.
**NEVER RUN AN INSTALL.** Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it
holds an exposed credential.

**YOUR PORTAL CHECKOUT, provisioned by the issuer before your spawn and verified then.** `<wt>/portal` is a
PORTAL-REPO worktree at portal commit `db1c5f64d19880cda50d6969ded3c3af26c92630` (portal `origin/DEV` at the cut)
on branch `wk-amgt-19-78-portal`. `<wt>/portal/node_modules` is a DIRECTORY JUNCTION to the main tree's installed
packages (`typescript`, the `tsc` binary, `react`, `react-dom` resolve through it). **The junction writes through
into a directory other seats depend on: it is NOT a write surface, and a package that reads ABSENT is a row, never an
install.** The superproject's `portal` gitlink NEVER moves (it reads `db1c5f64...` and must still read it at your
completion -- AC5).

## 1. THE CELL, inlined in full -- `AMGT-rk-78` (R19-D)

**The ruling, verbatim (`ledger/ROUND_ANALYSIS.round18.md` @3bfdf0a3a3 s.5, `:93-99`, `1.0.0_SA_CTO~Z`, msg 24019):**
*"**CALL 1 -- R19-D: RULED IN, this round.** `C-EXEC-MANAGEMENT` says the fallback "never hides why the filing
failed", and the page's SERVED branch renders neither `roster_status` nor `roster_reason`. Call 2's served
`source_item` makes the source line true but does not say WHY the filing roster failed. So R19-D renders
`roster_source`, `roster_status` and `roster_reason` on a SERVED fallback block (`src/pages/SecurityAnalysis`).
It is disjoint from A/B/C and sequenced after R19-C drains, since it renders R19-C's fields. It is a DEV push. **Its
PROD promote is carded to Andrew** (below)."* And `:118-119`: *"B first; A once its pair completes; C after B drains,
with its pair; D after C drains."* Msg 24019 adds: *"Its PROD promote is carded to Andrew now; don't promote on the
17:2xZ word alone."*

**The contract, verbatim (`prd/AMGT_RESAPP_PRD.md` @437e219264 v0.15, `C-EXEC-MANAGEMENT` `:738-745`; one
non-ASCII stop glyph before "The fallback" at `:743` is omitted here):** *"When the filing yields no RESOLVED roster,
Bloomberg's `COMPANY_EXEC_OFFICERS` (name and title only, names kept verbatim) fills the officer TABLE and is
labelled on the page as a Bloomberg fallback. Role start, tenure and the pool comparison stay ABSENT, with the reason
that Bloomberg carries no role start. ... Every management object carries `roster_source` = FILING |
BLOOMBERG_FALLBACK. **The fallback never hides why the filing failed:** when a filing roster failed (an empty
officer-section cut, or a section no declared shape reads), its own `roster_status` and `roster_reason` stay on the
object beside the Bloomberg officers, and the page shows them."*

**THE SERVED SHAPE YOU RENDER** comes from `AMGT-rk-77` (R19-C, same round, drained and deployed BEFORE your spawn).
On a SERVED fallback block the adapter serves `management_status "SERVED"`, `absent_because null`, the officers
verbatim with the real `officer_count`, `roster_source "BLOOMBERG_FALLBACK"`, `roster_source_basis "object"`, the
FILING's own `roster_status` / `roster_reason` / `absence_reason_class` / `absence_reason_evidence` verbatim,
`source_item "Bloomberg COMPANY_EXEC_OFFICERS (fallback: no RESOLVED filing roster)"`, `source_accession null`,
`source_key` the Bloomberg raw object, `filing_source_item` / `filing_source_accession` / `filing_source_key`, the
object's `fallback` block verbatim, and `pool_read {"status": "NOT_READ", "reason": "Bloomberg COMPANY_EXEC_OFFICERS
carries no role start, so tenure and the pool comparison are ABSENT"}`. A RESOLVED block gains exactly
`roster_source "FILING"` and `roster_source_basis`. The zero-officer ABSENT block is unchanged. A fourth absent label,
`absent_because "ROSTER_UNRESOLVED_NO_FALLBACK"`, exists and no name carries it today. AC1 reads the live shape
before you edit; if it does not match, STOP (R19-C has not landed).

**THE MEASURED STATE, at portal `db1c5f64` (RE-READ every line at your checkout before editing):**
- `src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx`, 222 lines. `ManagementBody` `:129-188`:
  - the non-SERVED branch `:130-148` prints `Exec Management: ABSENT (<absent_because>) -- <reason>`, and ONLY for
    `absent_because === 'ZERO_OFFICERS'` (`:139-145`) a detail line
    `roster_status ...; roster_reason ...; source_item ...; source_accession ...`;
  - the SERVED branch `:149-187` prints `{n} officer(s) from {source_item ?? 'the filing'}` (`:153-157`), the table,
    the Lusha line, the pool line (`poolLine`, `:63-74`, which prints `ABSENT (${pool_read.reason})` when the pool
    average is null), and `CeoProfile`. **It renders neither `roster_source`, `roster_status` nor `roster_reason`.**
  - `OfficerRow` `:35-61`: the last cell (`:58`) prints `confirmed from the filing` when `officer.confirmed`, else
    `unconfirmed`.
- **The stored fallback officers carry `confirmed: true` and `source: "bloomberg"`** (CSL 14 of 14, 6861 1 of 1,
  measured on `management/v1/<key>/2026-09-19.json`). **Measured at `db1c5f64` by rendering the ACTUAL tab on a
  CSL-shaped served fallback block: 14 officer rows, `confirmed from the filing` 14 times, `roster_reason` rendered
  false, `roster_status` rendered false, status SERVED** -- the page tells a manager that 14 Bloomberg officers were
  confirmed from a filing that failed. Every officer in the 5 committed `tabsFixture.*.json` files is
  `source: "filing"`, `confirmed: true` (48 of 48).
- `src/pages/SecurityAnalysis/types.ts`: `Officer` `:659-670` (carries `source?: string`); `ManagementBlock`
  `:715-743`, whose `absent_because` (`:720`) is `'NO_OBJECT' | 'ZERO_OFFICERS' | null` and which has no
  `roster_source`, `roster_source_basis`, `filing_source_*` or `fallback` field.
- The tab sits in `Panel variant="mixed"`, which resolves to the dark band (portal `CLAUDE.md` "Known divergence"),
  so the tab's existing `text-white/40..70` idiom is legal here. Use ONLY the classes the tab already uses; add no
  colour, no new component, no dependency.
- **Instruments at the cut, measured in a portal worktree provisioned exactly like yours:** `./node_modules/.bin/tsc
  -b --noEmit` rc 0, 0 errors, about 10 s; a planted `const x: number = "..."` file makes it rc 2 with 1 `error TS2322`
  naming that file, and removing it restores rc 0 (the portal `CLAUDE.md` typecheck law: bare `tsc --noEmit` checks
  NOTHING here). The existing `node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs`, run in the MAIN tree at
  `db1c5f64`, exits rc 1 with `CHECKS-WRONG-WAY exec_officers_rendered` (pre-existing: `ceo reading 1 of 5`, because 4
  of 5 committed fixtures predate the CEO reading) and `EXEC officers=48/48 pool_line=5/5`. It needs the workspace
  root around the portal (its short-read arm runs the Python adapter), so ITS SPAWN BASELINE IS YOURS TO MEASURE in
  `<wt>/portal` before you edit (AC4).

**RULED, what you build (portal files only):**
1. **`types.ts`:** `ManagementBlock` gains OPTIONAL `roster_source?: 'FILING' | 'BLOOMBERG_FALLBACK' | null`,
   `roster_source_basis?: string | null`, `filing_source_item?: string | null`, `filing_source_accession?: string |
   null`, `filing_source_key?: string | null`, and `fallback?: ManagementFallback | null` (a new exported interface
   with optional `field`, `label`, `status`, `entries_returned`, `officers_parsed`, `raw_key`, `pulled_at`, `reason`);
   `absent_because` gains `'ROSTER_UNRESOLVED_NO_FALLBACK'`. Nothing else in the file moves.
2. **The SERVED branch, fallback only.** When `management.roster_source === 'BLOOMBERG_FALLBACK'`, render ONE element
   directly under the existing `{n} officer(s) from ...` line, carrying `data-exec-roster-source="BLOOMBERG_FALLBACK"`,
   that states: the table is the Bloomberg fallback, and the filing roster did not resolve, with the served
   `roster_status` and `roster_reason` verbatim (`ABSENT` where a value is null). When `roster_source` is anything
   else (FILING, null, absent), render NOTHING new: **a RESOLVED block's markup is byte-for-byte today's.**
3. **`OfficerRow`'s Confirmed cell.** When `officer.source === 'bloomberg'`, print `per Bloomberg, not the filing`
   (never `confirmed from the filing`). Every other officer prints exactly as today. This is the contract's "labelled
   on the page as a Bloomberg fallback", applied to the one cell that says the opposite (ruled by `2.0.0_SA_COO~Z` at
   L5; named for the CTO in the issuance).
4. **The ABSENT branch:** the detail line that today renders only for `ZERO_OFFICERS` also renders for
   `ROSTER_UNRESOLVED_NO_FALLBACK` (0 names today). A `ZERO_OFFICERS`, `NO_OBJECT` or `READ_FAILED` block's markup is
   byte-for-byte today's.
5. **A new static-render harness `src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs`**, in the idiom of
   `errorEmpty.harness.cjs` (`ts.transpileModule` + `vm` + `react-dom/server` `renderToStaticMarkup`; stub
   `@/ui/components/panels`, `../hooks/useLeadPanelApi` (`useThesisBundle` hands back the fixture), 
   `../components/IdentityLine`; the ACTUAL `ExecManagementTab`). It writes NO file and exits rc 0 only if every
   check holds. Fixtures are CAPTURED ADAPTER BYTES (AC1) written as
   `__harness__/execFixture.<KEY>.json` for `CSL_AU_Equity`, `6861_JP_Equity`, `CAT_US_Equity` and `ASML_NA_Equity`,
   `json.dumps(..., ensure_ascii=True, indent=1)` + newline. Every expected count is READ OFF THE FIXTURE (officer
   count, roster_status, roster_reason) and printed with its denominator, never typed. Checks:
   - `fallback_source_rendered` -- CSL and 6861: exactly 1 `data-exec-roster-source="BLOOMBERG_FALLBACK"`, and the
     fixture's `roster_status` and the first 40 characters of its `roster_reason` both appear in the markup;
   - `fallback_not_confirmed_from_filing` -- CSL and 6861: `confirmed from the filing` 0 times, `per Bloomberg, not
     the filing` = the fixture's `officer_count` times (14, 1), officer rows = `officer_count`;
   - `resolved_unchanged` -- CAT: the markup's sha256 EQUALS the markup of the SAME fixture rendered through the
     PINNED pre-change tab (below), and contains 0 `data-exec-roster-source`;
   - `absent_unchanged` -- ASML_NA: sha256 equal to the pinned render;
   - **`pinned_copy_discriminates`** -- the DISCRIMINATING ARM: load `ExecManagementTab.tsx` from
     `git show db1c5f64d19880cda50d6969ded3c3af26c92630:src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx` (PINNED
     BY HASH -- never HEAD, never a merge-base: a HEAD read names this cell's own code once it merges, row
     `AMGT_RESAPP-Z-S193`) and show that on the CSL fixture it renders `confirmed from the filing` 14 times and NEITHER
     the roster_status NOR the roster_reason -- so checks 1 and 2 discriminate;
   - a final line `EXECFALLBACK CHECKS n/n` and, on any failure, `CHECKS-WRONG-WAY <names>`.

**What this cell does NOT change:** `lib/` (the adapter is R19-C's, deployed); any other portal file, including the
committed `tabsFixture.*.json` and `tabs.harness.cjs`; the header, the pool line's own logic, `CeoProfile`, the
panel subtitle; `package.json` and every dependency. **No push, no DEV or PROD move, no gitlink move.**

**THE VALIDATION BAR:** the three names a manager will open first read true on the tab -- CSL and 6861 name their
source and why their filing failed and never claim a filing confirmed a Bloomberg officer; CAT (RESOLVED) and the
zero-officer names read exactly as today.

## 2. WHERE THIS CAME FROM

**ROUND 19**, decomposition s.27 (cut by `2.0.0_SA_COO~Z`), on `1.0.0_SA_CTO~Z`'s round-18 analysis
`ledger/ROUND_ANALYSIS.round18.md` (s.2 @ac58e01116; s.4 @5f10ddf969; s.5 @3bfdf0a3a3), msgs 24011, 24015, 24019.
Row `AMGT_RESAPP-Z-S194` (the page served CSL/6861 as ZERO_OFFICERS) -- R19-C fixes the adapter half, this cell the
page half. Andrew-direct ~16:5xZ (record @c5532df80a): a functional product ready for the managers' review.
Andrew-direct ~15:12Z: one slug per round.

## 3. SURFACES -- what you may read and write

<paths>
portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx
portal/src/pages/SecurityAnalysis/types.ts
portal/src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/execFixture.CSL_AU_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/execFixture.6861_JP_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/execFixture.CAT_US_Equity.json
portal/src/pages/SecurityAnalysis/__harness__/execFixture.ASML_NA_Equity.json
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~78/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-78.render-fallback-roster-reason.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Reads need no grant. `portal/node_modules` is a junction and NOT a
  write surface; `portal/.tsbuild/` (gitignored, written by `tsc -b`) is tolerated. Scratch is `<wt>/.scratch/r78/`
  only (never committed). The one exception to the walls is the typecheck control file in AC2, which the criterion
  itself creates and deletes; it must not exist at your completion.
- **Collision check, at the cut:** R19-A (`AMGT-rk-75`) writes `lib/research/management/` and re-projects 3
  management objects; R19-B (`AMGT-rk-76`) writes `lib/research/identity/crosswalk.py` + a test; R19-C (`AMGT-rk-77`)
  writes `lib/research/api/scoped_amgt.py` + a test and redeploys the adapter. **None writes a portal path.** The held
  branch `wk-amgt-14-50` touches no portal path (names only). The only shared file is `INVESTIGATION_v1.md`
  (append-only; do not isolate it).
- **COMMITTING PORTAL WORK:** inside `<wt>/portal`, on branch `wk-amgt-19-78-portal`, with
  `git add -- <the portal files you changed> && git commit --author "0.9.0_WK_AMGT_RESAPP~78 <0.9.0_WK_AMGT_RESAPP~78@opal.agent>" -F <msgfile> -- <those files>`
  (paths relative to `<wt>/portal`, message file written by the Write tool). **NEVER PUSH. Never touch the portal
  remote, DEV or PROD.** The issuer integrates your branch into portal DEV at the drain; the PROD promote is Andrew's
  card.
- **COMMITTING SUPERPROJECT WORK** (your instance, rows, the status flip):
  `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~78 <0.9.0_WK_AMGT_RESAPP~78@opal.agent>" -F <msgfile> -- <paths>`,
  never staging `portal`. Never merge, rebase, `checkout --`, `stash` or `clean`.

## 4. BOUNDS

**PORTAL: COMMIT YES, PUSH NO.** No push, no gitlink move, no DEV/PROD merge, no deployment, no `/prod-deploy`. A
local commit on a worker branch is not a publish. **The only AWS act is four read-only `lambda:InvokeFunction` calls**
(AC1); no S3 write, no Terraform, no Lambda change. No vendor call, no other network fetch. **COLLECTION STAYS OFF.**
**NO alarm, monitor, SNS/SES-send, notification or freshness checker.** No secrets are needed. **No non-ASCII** in
anything you write (AC6 counts it). **PUSH: never** (LD-0522).
**THE REFUSAL CLAUSE:** a criterion you cannot satisfy AS WRITTEN is REFUSED with its measurement and a row; never
repaired, widened, or satisfied by a route this order did not name -- never by an install, never by editing a WALL
(the adapter included), never by typing a fixture instead of capturing it, never by relaxing a pinned comparison.
**A COUNT BAR IS READ AT SPAWN AND PRINTS its denominator.**
**SURPRISE ROWS:** `AMGT_RESAPP-Z-W78-S<k>`, `<k>` from 1; `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`; append by
textual splice inside the one fenced JSON array; never edit an existing row. A pure disarm sets
`DISMISSED_WITH_REASON`, never `GRADUATED`; the disposition of `Z-S194` is the CVO's L9 act, not yours.
**MUTATION DISCIPLINE:** snapshot WORKING-TREE BYTES to `<wt>/.scratch/r78/` before editing. Never `git checkout --`,
never `git stash`, never `git show :path`.

## 5. PROOF OF SPEC -- one clause per criterion (every invocation is LITERAL; record it byte-for-byte; each runs under timeout 300; run AC1 and AC4's baseline BEFORE any edit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rk-78"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c 'import boto3, json, io; lam = boto3.client("lambda", region_name="us-east-1"); out = {}
for k in ("CSL_AU_Equity", "6861_JP_Equity", "CAT_US_Equity", "ASML_NA_Equity"):
    ev = {"rawPath": "/api/scoped/amgt/security/%s/thesis" % k, "headers": {"x-firm-id": "bd"}, "requestContext": {"http": {"method": "GET"}}}
    b = json.loads(lam.invoke(FunctionName="opal-amgt-scoped-api", Payload=json.dumps(ev).encode())["Payload"].read())
    inner = json.loads(b["body"]) if isinstance(b.get("body"), str) and b["body"][:1] == "{" else {}
    m = inner.get("management") or {}
    io.open("portal/src/pages/SecurityAnalysis/__harness__/execFixture.%s.json" % k, "w", encoding="utf-8", newline="\n").write(json.dumps({"capture": "lambda invoke opal-amgt-scoped-api GET /api/scoped/amgt/security/%s/thesis -> body.management" % k, "status_code": b.get("statusCode"), "management": m}, ensure_ascii=True, indent=1, sort_keys=True) + "\n")
    print(k, b.get("statusCode"), m.get("management_status"), m.get("absent_because"), m.get("roster_source"), m.get("roster_status"), m.get("officer_count"), "bloomberg_officers", sum(1 for o in (m.get("officers") or []) if o.get("source") == "bloomberg"))'</invocation><expect>four lines, each status 200, reading exactly: "CSL_AU_Equity 200 SERVED None BLOOMBERG_FALLBACK UNRESOLVED-SOURCE 14 bloomberg_officers 14"; "6861_JP_Equity 200 SERVED None BLOOMBERG_FALLBACK UNRESOLVED-SOURCE 1 bloomberg_officers 1"; "CAT_US_Equity 200 SERVED None FILING RESOLVED 1 bloomberg_officers 0"; "ASML_NA_Equity 200 ABSENT ZERO_OFFICERS None UNRESOLVED-SOURCE 0 bloomberg_officers 0" -- the post-R19-C served shape (at the cut, before R19-C, CSL and 6861 read ABSENT ZERO_OFFICERS 0 and CAT carried no roster_source). ANY other line means R19-C has not landed or has landed differently: STOP with a BLOCKING row (disarm_owner 2.0.0_SA_COO~Z) and edit nothing. The four fixture files are written by this invocation and are the harness's only input</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-78"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && ./node_modules/.bin/tsc -b --noEmit > ../.scratch/r78/tsc_clean.out 2>&1; echo "clean_rc $? errors $(grep -c 'error TS' ../.scratch/r78/tsc_clean.out)"; printf 'export const typecheckControl: number = "not a number"\n' > src/pages/SecurityAnalysis/__typecheck_control__.ts; ./node_modules/.bin/tsc -b --noEmit > ../.scratch/r78/tsc_control.out 2>&1; echo "control_rc $? errors $(grep -c 'error TS' ../.scratch/r78/tsc_control.out) naming $(grep -c '__typecheck_control__.ts' ../.scratch/r78/tsc_control.out)"; rm -f src/pages/SecurityAnalysis/__typecheck_control__.ts; ./node_modules/.bin/tsc -b --noEmit > ../.scratch/r78/tsc_after.out 2>&1; echo "after_rc $? errors $(grep -c 'error TS' ../.scratch/r78/tsc_after.out) control_file_present $(test -f src/pages/SecurityAnalysis/__typecheck_control__.ts && echo yes || echo no)"</invocation><expect>three lines: "clean_rc 0 errors 0"; "control_rc 2 errors 1 naming 1" (the planted error is caught, so the clean pass can fail -- measured so at the cut); "after_rc 0 errors 0 control_file_present no". Run AFTER your edits. The form is `tsc -b --noEmit`, never bare `tsc --noEmit` (portal CLAUDE.md: the bare form checks an empty file set and passes on anything)</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-78"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && node src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs; echo "rc $?"</invocation><expect>rc 0; CHECK lines for fallback_source_rendered, fallback_not_confirmed_from_filing, resolved_unchanged, absent_unchanged and pinned_copy_discriminates, each "true (expected true)", each printing its denominator read off the fixture (CSL officers 14, 6861 officers 1); the pinned arm printing "confirmed from the filing" 14 and roster_status/roster_reason rendered false for CSL at db1c5f64d19880cda50d6969ded3c3af26c92630 (measured so at the cut); a final "EXECFALLBACK CHECKS 5/5"; no CHECKS-WRONG-WAY line</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-78"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs > ../.scratch/r78/tabs_after.out 2>&1; echo "rc $?"; grep -E "^CHECKS-WRONG-WAY|EXEC officers=" ../.scratch/r78/tabs_after.out; cat ../.scratch/r78/tabs_spawn.summary</invocation><expect>the rc, the CHECKS-WRONG-WAY line (if any) and the EXEC segment after your edits are IDENTICAL to the spawn baseline you recorded BEFORE editing into .scratch/r78/tabs_spawn.summary with the same command (rc, the grep lines); measured in the MAIN tree at db1c5f64 as rc 1, "CHECKS-WRONG-WAY exec_officers_rendered" (pre-existing, ceo reading 1 of 5) and "EXEC officers=48/48 pool_line=5/5" -- record yours, and a moved line FAILS this criterion. This harness renders the 5 committed RESOLVED fixtures through the edited tab, so an unchanged result is the committed-population half of "RESOLVED renders as today"</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-78"><invocation>cd "$(git rev-parse --show-toplevel)" && git -C portal diff --name-only db1c5f64d19880cda50d6969ded3c3af26c92630..HEAD | sort && echo "--- portal branch $(git -C portal rev-parse --abbrev-ref HEAD) status_porcelain $(git -C portal status --porcelain | grep -v '^?? .tsbuild' | wc -l)" && echo "--- gitlink $(git ls-tree HEAD portal | awk '{print $3}')" && git -C portal log --format='%an | %s' db1c5f64d19880cda50d6969ded3c3af26c92630..HEAD</invocation><expect>exactly 7 paths, sorted: src/pages/SecurityAnalysis/__harness__/execFallback.harness.cjs, the 4 src/pages/SecurityAnalysis/__harness__/execFixture.*.json files (6861_JP_Equity, ASML_NA_Equity, CAT_US_Equity, CSL_AU_Equity), src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx, src/pages/SecurityAnalysis/types.ts; "portal branch wk-amgt-19-78-portal status_porcelain 0"; "gitlink db1c5f64d19880cda50d6969ded3c3af26c92630" (the superproject pointer never moved); every portal commit authored 0.9.0_WK_AMGT_RESAPP~78</expect></criterion>
  <criterion id="AC6" cell_refs="AMGT-rk-78"><invocation>cd "$(git rev-parse --show-toplevel)/portal" && python -c 'import io, subprocess; fs = subprocess.run(["git", "diff", "--name-only", "db1c5f64d19880cda50d6969ded3c3af26c92630..HEAD"], capture_output=True, text=True).stdout.split(); [print(f, "crlf", io.open(f, "rb").read().count(b"\r\n"), "non_ascii_bytes", len(io.open(f, "rb").read()) - len(io.open(f, "rb").read().decode("utf-8"))) for f in fs]; print("files", len(fs))'</invocation><expect>"files 7" and every file printing crlf 0 and non_ascii_bytes 0 (the two edited .ts/.tsx files measured 0 and 0 at db1c5f64; captured fixtures are written ensure_ascii, so an officer name with an accent is escaped, never raw)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR, not a paraphrase.** No judgment criterion on this
order. Also record in your deliverable the full markup the harness renders for CSL's served block (from a scratch run
that prints it), so the CVO can read the sentence a manager will see.

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~78/AMGT_RESAPP.TO-AMGT-rk-78.render-fallback-roster-reason.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by YOUR WORKTREE'S OWN
`python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6` (rc 0 is the verdict); flip `<status>` to
`complete`; commit the superproject files with safe-commit (never staging `portal`). Report once: the four AC1
lines, the portal commit hash(es) on `wk-amgt-19-78-portal` (LOCAL, unpushed), the typecheck and harness results,
the tabs-harness spawn baseline and its after-edit reading, and the CSL sentence a manager will now read.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER PROVISIONING, before spawn (after R19-C `AMGT-rk-77` has DRAINED and its redeploy is verified), measured
feasible at the cut in a probe (`git -C portal worktree add` + a `mklink /J` junction; typecheck rc 0 in 10 s;
probe removed, main `portal/` untouched at `db1c5f64`):**
```
git worktree add C:/tmp/wk-amgt-19-78 -b wk-amgt-19-78 <issuance-or-later SITEZ sha>
git -C portal worktree add C:/tmp/wk-amgt-19-78/portal -b wk-amgt-19-78-portal db1c5f64d19880cda50d6969ded3c3af26c92630
cmd //c mklink //J "C:\tmp\wk-amgt-19-78\portal\node_modules" "<workspace>\portal\node_modules"
```
Verify `C:/tmp/wk-amgt-19-78/portal/node_modules/typescript` resolves and `git -C C:/tmp/wk-amgt-19-78 ls-tree HEAD
portal` reads `db1c5f64...`. Teardown at the drain: `cmd //c rmdir` the junction FIRST (never a recursive delete
through it), then `git -C portal worktree remove`, then the workspace worktree.

**DRAIN:** integrate `wk-amgt-19-78-portal` into portal DEV (the portal DEV push is the integrator's, LD-0522) and
move the superproject gitlink in its own commit; run `/frontend-dev` on the Security Analysis Exec Management tab for
CSL (the portal `CLAUDE.md` verification law: a static harness is not a screenshot) before calling the page ready.
**PROD promote: carded to Andrew by `1.0.0_SA_CTO~Z` (msg 24019) -- not on the 17:2xZ word.**

<status>complete</status>
<round>19</round>
<slot>~78</slot>
<fabric>site-z</fabric>
