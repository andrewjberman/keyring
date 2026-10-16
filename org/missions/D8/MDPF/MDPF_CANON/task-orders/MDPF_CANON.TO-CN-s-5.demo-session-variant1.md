# MDPF_CANON task order -- `CN-s-5` -- THE DEMO-TENANT SESSION DRAWS VARIANT 1 (FWD-9; PORTAL CANDIDATE, CLIENT-FACING AT THE LANDING, HELD FROM PROMOTE ON THE EDGE CALL)


<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-s-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~31</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; two portal source files.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS contact at all (the checks run `bun` on a pure function and read source text).
comp-adversary: RUN by the issuer on DELL1 at the base (portal DEV 39dab87f3b) -- `r11_cn_s_4.py wiring` wiring 4 of 10 (P1 and W5 to W9 red; P2, P3, P4, W10 are controls); a scratch reference reads 10 of 10 (the arms can pass); planted mutants (`trendModeFor` ignoring its second parameter; one of the two stitch reads left on bare `internal`; the stitch memo left on `internal`) each turn their named arm red; `selftest` prints OK.
EGRESS CLASS, declared: none.
</preflight>

**Your worktree:** you are already in it (slot ~31, outer branch `wk-MDPF_CANON-31`, portal branch `wk-MDPF_CANON-31-portal`); this order is handed to you after CN-s-4, whose portal commit is on the branch. CN-s-4's work stays as it is. Start every shell call with `cd` into the outer worktree path.
**Line endings: `src/lib/trendGrouping.ts` and `src/pages/ModelPortfolios.tsx` are CRLF in EVERY line. Keep it.** After your edits run `git -C "<worktree>/portal" diff --stat` and check that no line is LF-only.

## 1. THE CELL -- `CN-s-5` (round 11)

**The cell, verbatim from the decomposition:** the demo-tenant session draws Variant 1 (the same code as the internal session): `trendModeFor(internal, demo)` gains the second parameter and the page defines `demoTenant` and `variant1Session = internal OR demoTenant`, which replace bare `internal` in the two single-firm stitch reads and the stitch memo; everything else on the page keeps `internal`.

**Why (Andrew-direct 2026-10-15 ~16:2xZ):** the demo tenant's Global Trend uses Variant 1 (the full-history view with the single-firm stitch before 2026-05-15), the same as an internal session, so the demo sees what the Global view sees. Today `trendModeFor(internal: boolean)` returns 'variant1' only for an internal session, and the stitch inputs are gated on bare `internal`.

**The exact edits (three, nothing else):**

1. `portal/src/lib/trendGrouping.ts`: `trendModeFor` (one line, near L153) becomes `export const trendModeFor = (internal: boolean, demo: boolean = false): TrendMode => (internal === true || demo === true ? 'variant1' : 'variant2')`. Keep its doc comment accurate (Variant 1 for an internal session or the demo tenant; every other session draws Variant 2). The one-argument call must keep meaning what it meant.
2. `portal/src/pages/ModelPortfolios.tsx`, near where `const internal = isInternal() || isDev()` and `const trendMode = trendModeFor(internal)` are (L386-389): add `const demoTenant = MDPF_GLOBAL_VIEW_FIRMS.has(claims?.firmId ?? '')` and `const variant1Session = internal || demoTenant`, and call `trendModeFor(internal, demoTenant)`. (`MDPF_GLOBAL_VIEW_FIRMS` is the page's existing set, `new Set(['demo'])`, defined at L300 before the component; `claims` is already destructured from `useAuth()`.) Keep the comment about CN-p-2 accurate.
3. Same page: the two `useQuery` calls for the single-firm reads (query keys `['mdpf-per-firm-timeseries', '49financial']` and `[..., 'inflection']`, L453-464) change `enabled: effectiveFirmId === 'global' && internal` to `enabled: effectiveFirmId === 'global' && variant1Session`; the `trendStitch` memo (L538-564) changes its first line `if (!internal) return null` to `if (!variant1Session) return null` and its dependency array `[internal, firm49MdpfData, inflectionMdpfData]` to `[variant1Session, firm49MdpfData, inflectionMdpfData]`. Update the two comments above them so they say "a Variant 1 session (internal or the demo tenant)".

**Do NOT change anything else.** In particular `internal` keeps every other use: `SHOW_BENCHMARK_TOGGLE = internal`, the `effectiveFirmId` derivation, the actions slot, the benchmark and all internal-only UI. The demo tenant gains NO internal-only feature; it gains only the Variant 1 Trend.

**Known and NOT yours to fix (say it in your report if you see it):** the live edge gate (`auth-validator-edge`, CN-q-1) admits a `demo` or firm-less claim to the `global` folder only, so on PROD a demo session's two single-firm reads (49 Financial, Inflection) are REFUSED (403) and the stitch input stays empty. This order wires the page; it never touches the gate, never widens it, and never works around a refusal. The issuer holds this order's commit from any promote until the edge question is ruled.

## 2. BOUNDS

1. You change `portal/src/lib/trendGrouping.ts` (`trendModeFor` only) and `portal/src/pages/ModelPortfolios.tsx` (the three edits above) and nothing else in the portal.
2. The page does NO arithmetic on a served group. Do not widen, bypass or mimic any firm gate.
3. A non-internal, non-demo session must not receive a single-firm value by any route: its stitch stays null, its two reads stay disabled.
4. No AWS contact, no deploy, no push, no `bun install`, no browser launch.
5. **CLIENT DATA:** never print a client figure or an account id in your report, a row or a file.
6. No non-ASCII character in any line you add. Use the Edit tool; keep CRLF.
7. Do not edit the issuer's checks. If a step cannot be done as written, file a row naming the step and stop on that step.
8. Do not run repo-wide hygiene as a criterion (the issuer runs the type check and the real run at the drain).

## 3. SURFACES

<paths>
portal/src/lib/trendGrouping.ts
portal/src/pages/ModelPortfolios.tsx
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-s-5.demo-session-variant1.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~31/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/`.

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-s-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/r11_cn_s_4.py" wiring; echo "exit=$?"</invocation><expect>ROUND 11 CN-S-4 WIRING: 10 of 10 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-s-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/r11_cn_s_4.py" pure; echo "exit=$?"</invocation><expect>ROUND 11 CN-S-4 PURE: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-s-5" judgment="true"/>
</proof_of_spec>

AC1 runs `trendModeFor` under `bun` (four arms) and reads the page as normalised text (six arms); AC2 is the guard that CN-s-4's repair (your branch's first commit) still holds. They cannot prove what a demo session DRAWS or what the edge returns. AC3 is JUDGMENT, graded at the round close (never self-graded): the issuer renders the Global Trend for a demo-tenant claim set at a STATED portal commit on `bun run dev:live --port 5174` and reports what the page draws and what the two single-firm reads return (the edge result named, never widened). You do not render.

## 5. WHEN YOU ARE DONE

1. Commit the two portal files INSIDE the nested repo as ONE portal commit, SEPARATE from CN-s-4's: `git -C "<worktree>/portal" add -- portal/src/lib/trendGrouping.ts portal/src/pages/ModelPortfolios.tsx` (paths relative to the nested repo root: `src/lib/trendGrouping.ts` and `src/pages/ModelPortfolios.tsx`) then `git -C "<worktree>/portal" commit --author "0.9.0_WK_MDPF_CANON~31 <0.9.0_WK_MDPF_CANON~31@opal.agent>" -F <msgfile>` (message file written with the Write tool). If a portal hook refuses, file a row with its text and stop: do not bypass it.
2. Write the proof instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~31/MDPF_CANON.TO-CN-s-5.demo-session-variant1.proof_of_spec.json`, AC3 UNVERIFIABLE-BY-INSTRUMENT with status_reason "graded at the round close". **Flip this order's `<status>` to `complete` in the SAME commit as the instance**, and only when AC1 and AC2 both pass.
3. Commit the OUTER files via `.tools/safe-commit.sh --author "0.9.0_WK_MDPF_CANON~31 <0.9.0_WK_MDPF_CANON~31@opal.agent>" -F <msgfile> -- <paths>` (outer paths only; do not stage `portal`). Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

A row id carries the dell1 infix: `MDPF_CANON-D1-W31-S<k>`, with `surfaced_at` from `date -u +%FT%TZ`.
Report once: the portal commit hash, the diff stat (one line), the output lines of AC1 and AC2, the outer commit hash, and any row. Then STOP: the issuer hands you the next order (CN-s-3) by continuing you.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 11, issuer 2.0.0_SA_COO~D1, on the CTO's round-10 analysis (msg 6731) item 2 (the CTO's words: "CN-s-4b, the demo on Variant 1, per your 4a/4b split"; cut as CN-s-5 because the L6 gate's cell-id grammar takes no letter suffix, and CN-s-4a is cut as CN-s-4). The page was read at DEV @39dab87f3b on 2026-10-16 ~03:5xZ (committed as `ROUND11_RECTANGLE_DRAFT.md` @ba8dca3ec2): `trendModeFor` is one flag; the stitch reads (L456, L462) and the memo (L539) are gated on `internal`; a demo session's `effectiveFirmId` is forced to `'global'` by `MDPF_GLOBAL_VIEW_FIRMS` (L300, L407-411).
- **The edge call (ruling 3 of the v11 section):** the CTO's analysis names "the edge firm gate D1 named" in this cell's scope; the PRD v2.23 line says the cell REPORTS a refusal and never widens the gate. Widening `mdpf_gate.mjs` to admit `demo` on two single-firm leaves is a cross-firm containment decision and a WORLD deploy, so it is queued as an open call for the box CTO rather than built here. Until it is ruled this commit is NOT promoted (CN-s-4's is). With the gate unchanged a demo session on PROD draws Variant 1 with no pre-2026-05-15 stitch.
- **FWD-3 tension, for the CTO:** FWD-3 says a non-internal session cannot reach a single-firm value through the page; Andrew's word gives the demo tenant Variant 1, whose stitch IS the single-firm series. The call carries this.
- **Status staged:** this order stays `staged` until CN-s-4 is terminal, then the issuer flips it to `pending` and continues the worker (the order is non-terminal at HEAD, so the worker's grant already covers its paths).

**Fanout:** chain 1 of 2: `CN-s-4` -> `CN-s-5` -> `CN-s-3`, one worker, slot ~31. `portal_ref:` 39dab87f3b.

<status>staged</status>
<round>11</round>
<to_id>MDPF_CANON.TO-CN-s-5</to_id>
<slot>~31</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
