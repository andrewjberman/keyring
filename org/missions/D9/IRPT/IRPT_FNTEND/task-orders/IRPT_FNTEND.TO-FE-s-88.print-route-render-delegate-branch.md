# TO IRPT_FNTEND.TO-FE-s-88 -- the print route admits the counterpart's render-delegate token, on that route ONLY

<to_id>IRPT_FNTEND.TO-FE-s-88</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~38</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2 | **Decomp cell:** `FE-s-88` (round 14, v0.14) | **outcome_ref:** FWD-8 (F9's own PRD row also lists FWD-3, FWD-4, FWD-12) | **depends_on:** none -- READY ROOT | **slot:** ~4 | **rows:** F9 | **base:** workspace = the round-14 issuance commit on CLOUD (your worktree branches from it), portal DEV `467354c9` (round 13's close)

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE
### THE CELL

`FE-s-88` -- PRD v0.10's new CONTRACTS clause (F9, "(v0.10) THE PRINT ENTRY POINT ADMITS THE COUNTERPART'S RENDER
DELEGATE"), owed to `IRPT_BCKEND` v0.17 item 5. **Read the PRD clause in full before anything else**
(`org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`, search "(v0.10) THE PRINT ENTRY POINT") -- it is the
governing text, this cell restates only its shape. **Also read `IRPT_BCKEND`'s own render-identity contract in full**
(`org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`, search "THE RENDER IDENTITY", items 1-6) -- it names the
token's exact claim shape and the two verifiers that accept it; this cell's frontend branch is the THIRD place a
render token is read, and the only one this project owns.

**The problem.** `IRPT_BCKEND`'s headless renderer authenticates with a short-lived RENDER TOKEN whose `firmId` is
the TENANT firm (never `opal-capital`) and whose `role` is `renderer` (never `admin`). The print route
(`App.tsx:576`, `<Route path="/investor-reporting/print" element={<ProtectedRoute requireAdmin requireInternal>...}
/>`) currently gates on BOTH `user?.role !== 'admin'` (`ProtectedRoute.tsx:39`) and `claims?.firmId !== 'opal-capital'`
(`ProtectedRoute.tsx:44`) -- a render token satisfies neither, so the page redirects away and never renders.

**F9 owes ONE branch, on the print route ONLY.** A decoded token whose `aud` is `irpt-render` and whose `role` is
`renderer` is admitted to the print entry point. On EVERY other route the render claims admit nothing and the
existing gates apply completely unchanged -- this is the no-widening arm, and it is load-bearing: `ProtectedRoute`
is shared by every other protected route in the app, and this fix must not touch its behaviour for any of them.
**It is not a security control** (the PRD's own words) -- `IRPT_BCKEND`'s edge and authorizer branches already did
the real verification before this request ever reached the SPA; this branch only decides whether the ALREADY-VERIFIED
claims let the page render.

**Acceptance arms (CTO round-13 analysis, verbatim):**
(a) with a render-claim token, the print route renders from its fixture;
(b) the SAME token on any non-print route is redirected exactly as a non-internal token is today (the no-widening arm);
(c) a human internal token and a human advisor token behave on the print route EXACTLY as before.

**WHAT THIS ORDER DOES NOT SPECIFY, AND YOU MUST DETERMINE:** neither PRD states the WIRE MECHANISM by which the
render token reaches this browser (there is no interactive login for a headless renderer). Read `PrintEntry.tsx`'s
own docstring (`?bundle=`, `?tenant=`, `?scope=`, `?revision=` are already query-param-carried) and
`IRPT_BCKEND`'s CONTRACTS text for anything naming how the render job navigates the headless browser to this URL;
if genuinely silent on the wire shape, the most defensible reading given the existing `?param` idiom on this exact
route is a URL query parameter (e.g. `?renderToken=<jwt>`) that your fix reads once, decodes the PAYLOAD ONLY
(base64, unverified -- this is explicitly not a control, so client-side signature verification is neither required
nor meaningful), and uses for exactly the one admit/no-admit decision described above. State your reasoning and the
mechanism you chose, cited to whatever text supports it, in your result file -- the CVO grades whether that reading
is correct at L9. **If you cannot construct a defensible reading at all, REFUSE and file a surprise row rather than
guess destructively** -- do not invent a mechanism with no textual support and no reasoning trail.

**Your surface.** `App.tsx` (the print route's wrapper element ONLY -- e.g. a new prop on `ProtectedRoute` or a
narrow wrapping check; do not touch any other route), `components/ProtectedRoute.tsx` (the render-claim branch;
every other check in this file must remain reachable and behave identically for every non-render-token case),
`contexts/AuthContext.tsx` and `contexts/AuthContext.context.ts` (ONLY if your chosen mechanism needs the claims
shape extended -- prefer the narrowest change that does not alter the `Claims`/`User` interfaces' meaning for every
other consumer of `useAuth()`), and your own `__tests__/fe-s-88/`.

**HOW (the same for every cell of this round; read once, then do your cell).**

1. **Read first, in full:** `<WS>/portal/DESIGN.md` (clauses `C1`..`C12`) and `<WS>/portal/CLAUDE.md`; the PRD's ENDPOINT/CONTRACTS text your
   cell names (`../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2); the CTO's round-13 analysis
   (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_13_20260922.md` @4bc62712f2); and the slug rows your cell names
   (`org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v10.md`). A finding cites a clause NUMBER beside its evidence.
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 6005-6009 (outside the derived range 5400-5899 the browser-gated tests use,
   and outside rounds 12-13's 5900-5989): `IRPT_FE_DEV_PORT=<n> bun run dev --port <n>` in `<WS>/portal`, in the background, INLINE PREFIX, NEVER
   exported. Test with `curl` first; that number is `<PORT>`. Sibling workers run at the same time: never 5175.
3. **Run each invocation and READ every PNG** it saves. Record per capture: file, viewport, the RAW `FIXTURES-MATCH`/`KEY-VALIDITY`, `EXPECT*` and
   `ASSERT-*` lines verbatim, the DESIGN.md clauses you read it against, and what you saw.
4. **A control is a claim.** Before you trust a passing assertion, run its wrong-state / negative arm and confirm it fails or reads UNMEASURABLE as
   required. If a control passes when it should fail, the assertion cannot tell the states apart: say so and fix it, never report it as met.
5. **Stop your dev server before the whole-suite criterion and verify the port closed** (`curl` returns `000`). Run the suite where
   `IRPT_FE_DEV_PORT` is unset.
6. **C-S176 (this round's own CTO ruling, binding on every criterion below):** every visual criterion carries five controls (wire match, named
   content, wrong-state control, ground-on-actual-container, absent-selector control) unless a control is declared NOT APPLICABLE, WITH REASON,
   IN THIS ORDER, at cut time -- never waived silently in your result. Report DECLARED-KEY VALIDITY (the proof's keys parse) and EXERCISED
   FULFILMENT (n of N controls actually run) as two SEPARATE figures, never conflated. No retroactive N/A: if a control this order declares
   applicable turns out not to run, that is a defect you report, not a silent omission.
7. **Fixes.** A defect on YOUR write surface may be fixed with a BEFORE capture kept and an AFTER beside it, one fix per finding, cited to its
   clause. A defect needing another cell's file is ONE surprise row, never a wider grant. A test inside your grant pinning OLD behaviour you are
   correcting is updated in the same commit and named in your result.
8. **Result file** (`<slug>.result.md` in your deliverables folder), FIXTURE-FED disclosure paragraph first, as every prior round.
9. **Keep your context small:** read at most the PNGs your criteria need; write long outputs to files and read their tails.
### ACCEPTANCE

**Fixture-fed only** (per the PRD: this is not a control, so a SYNTHETIC token you construct in your own test --
`{header}.{payload}.{signature}`, base64url-encoded, signature bytes arbitrary since nothing here verifies them --
is the correct instrument; you do not need real signing keys, which this project does not hold).

<criterion id="F88-AC1" cell_refs="FE-s-88" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F88-AC1` -- the whole portal typechecks.

**Write your test under `__tests__/fe-s-88/`** (a `bun test` unit/integration test is the right
instrument here -- routing/auth branch logic, not a rendered style assertion; use React Testing Library or the
project's existing router-test idiom, matching how other route-guard behaviour is already tested in this repo if
such a precedent exists). Construct at least four synthetic tokens: (1) a valid render-claim token
(`aud: 'irpt-render'`, `role: 'renderer'`, a tenant `firmId`); (2) a human internal token (`firmId: 'opal-capital'`,
whatever shape `user.role === 'admin'` requires); (3) a human advisor token (a partner `firmId`, non-admin role);
(4) a token carrying NEITHER shape (garbage/expired-looking claims), to confirm your branch does not accidentally
admit everything.

<criterion id="F88-AC2" cell_refs="FE-s-88" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-88</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F88-AC2` -- ARM (a): the render-claim token reaches the print route's rendered content (not a redirect) -- asserted by presence of the print entry point's own DOM output or route state, never by absence of a redirect alone.

<criterion id="F88-AC3" cell_refs="FE-s-88" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-88</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F88-AC3` -- ARM (b), the no-widening control: the SAME render-claim token, exercised against a NON-print protected route (e.g. `/market` or `/investor-reporting` without `/print`), is redirected exactly as today's non-internal-token behaviour -- this is the negative control proving the branch is scoped to the print route alone, not a general admit.

<criterion id="F88-AC4" cell_refs="FE-s-88" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-88</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F88-AC4` -- ARM (c): a human internal token and a human advisor token each behave on the print route EXACTLY as they did before this change -- run each against the print route's PRE-existing gating outcome and confirm no regression (an internal admin token still admitted if it was before; an advisor token still redirected if it was before).

<criterion id="F88-AC5" cell_refs="FE-s-88" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-88</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F88-AC5` -- GARBAGE CONTROL: a token carrying neither the render-claim shape nor a recognized human shape is NOT admitted anywhere new -- the branch fails closed on an unrecognized claim, never open.

<criterion id="F88-AC6" cell_refs="FE-s-88" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F88-AC6` -- the whole IRPT_FNTEND suite is green.

<criterion id="F88-AC7" cell_refs="FE-s-88" judgment="true" drives="none"/>
`F88-AC7` -- graded at L9 by the CVO: the chosen wire mechanism (how the render token reaches this SPA) is a defensible reading of both PRDs' text, cited to what supports it; the branch is genuinely scoped to the print route ONLY and does not widen `ProtectedRoute`'s behaviour for any other route or token shape; this is a rendering-enablement branch, never represented as a security control. RECORD; NO VERDICT.

<expected_criteria>F88-AC1, F88-AC2, F88-AC3, F88-AC4, F88-AC5, F88-AC6, F88-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W38-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.
- **`ProtectedRoute.tsx` grant is the render-claim branch ONLY** -- `requireAdmin`, `requireInternal`,
  `requireDev` and the firm-access-matrix check must all remain reachable and byte-for-byte unchanged in their
  OWN behaviour for every non-render-token case; add your branch, do not restructure the existing checks.
- **`App.tsx` grant is the print route's own element line (`:576`) ONLY** -- do not touch any other route.
- **This is NOT a security control.** Never claim or imply client-side signature verification proves anything;
  say explicitly in your result that the counterpart's edge/authorizer are the real controls, per the PRD.
- **If `AuthContext.tsx`/`.context.ts` need a change**, it must not alter what `Claims`/`User` mean for any
  EXISTING consumer of `useAuth()` -- an additive field or a narrowly-scoped new state value only, never a
  redefinition of an existing one.
- **C-S176 declared N/A, with reason, at cut time:** this cell's criteria are routing/auth-branch behavioural
  tests (admit/redirect decisions on synthetic tokens), not rendered visual style assertions -- the five-part
  visual control rule does not apply. Arms (a)/(b)/(c) plus the garbage-token control ARE this cell's control set.
<paths>
portal/src/App.tsx
portal/src/components/ProtectedRoute.tsx
portal/src/contexts/AuthContext.tsx
portal/src/contexts/AuthContext.context.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-88/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.14, cell `FE-s-88`.
<owned_cells>FE-s-88</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F88-AC1`, `F88-AC2`, `F88-AC3`, `F88-AC4`, `F88-AC5`, `F88-AC6`, `F88-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-88.print-route-render-delegate-branch.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F88-AC1,F88-AC2,F88-AC3,F88-AC4,F88-AC5,F88-AC6,F88-AC7 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-88.print-route-render-delegate-branch.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `print-route-render-delegate-branch.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.10 (both L4-R halves SIGNED, prd-signoff.py status ADMITTED).
the design: RUN by the issuer -- REMEDIATION_v10.md @66cf49b513, ADJUDICATION_v5.md's C-S16x..17x rows, and CTO_ROUND_ANALYSIS_IRPT_FNTEND_ROUND_13_20260922.md @4bc62712f2, all read at HEAD.
the spec: RUN -- PRD FWD-12 ENDPOINT row, the F9 CONTRACTS clause (v0.10), and the CTO's round-13 analysis, all read at HEAD.
lane: the <paths> block IS the grant.
</preflight>

Seating: round 14, wave 1, slot ~FE-s-88.
