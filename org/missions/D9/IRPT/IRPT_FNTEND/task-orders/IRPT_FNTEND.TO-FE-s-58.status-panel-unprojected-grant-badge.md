# TO IRPT_FNTEND.TO-FE-s-58 -- StatusPanel renders the carried unprojected_grant, and Global mode is confirmed to inherit it

<to_id>IRPT_FNTEND.TO-FE-s-58</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~8</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-58` (round 9, v0.9, wave B) | **outcome_ref:** FWD-3, FWD-4, FWD-5, FWD-6, FWD-8 (rendering half); FWD-11 (verified, not cut) | **depends_on:** FE-s-57 (merged, workspace `22f8ee08be`, portal `15ceef79`) | **slot:** ~1 | **rows:** R9.2 `FE-s-58`

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-58` -- **round 9's decomposition, `R9.2`, VERBATIM:** *"`state/status.ts`'s `AvailabilityLike` (`:204-212`)
and `TabEnvelope` (`:77-89`) each gain `unprojectedGrant?: UnprojectedGrant | null`; `envelopeFromAvailability`
(`:215-230`) copies `availability.unprojectedGrant` across; `envelopeFromRefusal` (`:258-267`) sets it to `null`
explicitly (a refusal's `publicReasonCode` -- `UNPROJECTED_GRANT` included -- already renders verbatim via the
EXISTING `reason-code` slot at `StatusPanel.tsx:70-79`, confirmed by source read: no new code needed for the
refusal branch). `tabs/StatusPanel.tsx` gains a new slot, `data-slot="partial-disclosure"`, rendered when
`envelope.unprojectedGrant && envelope.unprojectedGrant.count > 0`, showing the count, denominator and kinds
list in the panel's existing visual idiom (a `<p>` beside the reason-code slot, same text sizing, navy ink on
the white panel per portal `CLAUDE.md`'s color law -- never a light-on-light badge). **Acceptance must exercise
Global mode** (`global/useFirmContext.ts` + the shared tab bodies) to CONFIRM F11's coverage is inherited, not
assumed -- a positive control render under a cross-firm selection, count>0, badge visible."*

`FE-s-57` (this cell's dependency) has landed: `contracts/index.ts`'s `Availability.unprojectedGrant?:
UnprojectedGrant | null` exists (`:157`), `UnprojectedGrant` is exported (`:111-115`), and `parseIrEnvelope`
carries it onto every non-refused document's `.availability`. This cell is the RENDERING half only -- it never
re-derives the count, denominator or kinds; it reads what `.availability.unprojectedGrant` already carries.

**Read the PRD's own `unprojected_grant` paragraph** (`org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`,
`CONTRACTS` section) before you start -- it is the ratified spec; where this cell's text and the PRD differ, the
PRD governs.

**EXACT CHANGES, at portal DEV `15ceef79`'s current shape (confirm each line number against YOUR checkout before
editing -- cite what you actually find, not this order's numbers, if they have drifted):**

1. **`state/status.ts`**:
   - `TabEnvelope` (`:77-88`) gains one new OPTIONAL member, mirroring `producerState`'s own established
     pattern exactly: `unprojectedGrant?: UnprojectedGrant | null`. Import `UnprojectedGrant` from `../contracts`.
   - `AvailabilityLike` (`:204-211`) gains the SAME member: `unprojectedGrant?: UnprojectedGrant | null`.
   - `envelopeFromAvailability` (`:215-229`) copies it across in the returned object, mirroring how
     `producerState` is already conditionally spread (`...(availability.producerState === undefined ? {} : {
     producerState: availability.producerState })`, `:228`) -- use the SAME conditional-spread idiom for
     `unprojectedGrant` (never force it onto every call site that doesn't carry one).
   - `envelopeFromRefusal` (`:258-266`) does NOT set `unprojectedGrant` at all (the conditional-spread idiom
     above means an absent member is the correct "not carried" state for a refusal, exactly like
     `producerState` already behaves there) -- confirm this by reading how the function currently omits
     `producerState` on its returned object, and follow the identical omission, not an explicit `null`.
2. **`tabs/StatusPanel.tsx`**:
   - Add a new conditional block, sited immediately after the existing `reason-code` block (`:70-80`) and
     before `safe-actions` (`:82-94`):
     ```tsx
     {envelope.unprojectedGrant && envelope.unprojectedGrant.count > 0 ? (
       <p className="text-xs text-slate-600" data-slot="partial-disclosure">
         {envelope.unprojectedGrant.count} of {envelope.unprojectedGrant.denominator}
         {envelope.unprojectedGrant.kinds.length > 0 ? ` (${envelope.unprojectedGrant.kinds.join(', ')})` : ''} not
         yet projected
       </p>
     ) : null}
     ```
     (Adjust the exact wording/markup to fit this file's own established idiom -- the REQUIREMENT is the
     `data-slot="partial-disclosure"` marker, the `count > 0` gate, and navy-on-white text per `portal/CLAUDE.md`'s
     color law; the JSX above is illustrative, not verbatim-required.)
   - `TabEnvelope` is already imported from `../state/status`; no new import needed for the type itself.

### ACCEPTANCE

<criterion id="F58-AC1" cell_refs="FE-s-58" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F58-AC1` -- the whole portal typechecks.

<criterion id="F58-AC2" cell_refs="FE-s-58" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-58/status-panel-badge.test.ts</invocation><expect>PARTIAL-DISCLOSURE RENDERS WHEN count>0: yes(?![0-9])</expect></criterion>
`F58-AC2` -- a `TabEnvelope` carrying `unprojectedGrant: {count: 3, denominator: 10, kinds: ['positions']}`
renders the `data-slot="partial-disclosure"` node, and its text names `3`, `10` and `positions` verbatim.

<criterion id="F58-AC3" cell_refs="FE-s-58" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-58/status-panel-badge.test.ts</invocation><expect>PARTIAL-DISCLOSURE ABSENT WHEN count=0 OR NULL: yes(?![0-9])</expect></criterion>
`F58-AC3` -- TWO arms: `unprojectedGrant: {count: 0, ...}` and `unprojectedGrant: null` BOTH render no
`data-slot="partial-disclosure"` node. Print both arms, never a subset.

<criterion id="F58-AC4" cell_refs="FE-s-58" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-58/status-panel-badge.test.ts</invocation><expect>REFUSAL PATH: unprojectedGrant ABSENT, reason-code SLOT UNCHANGED: yes(?![0-9])</expect></criterion>
`F58-AC4` -- `envelopeFromRefusal` with a `publicReasonCode` (e.g. one containing `UNPROJECTED_GRANT`) renders
the existing `reason-code` slot verbatim (unchanged behavior) and no `partial-disclosure` slot.

<criterion id="F58-AC5" cell_refs="FE-s-58" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-58/status-panel-badge.test.ts</invocation><expect>GLOBAL MODE, CROSS-FIRM SELECTION, count>0, BADGE VISIBLE: yes(?![0-9])</expect></criterion>
`F58-AC5` -- the positive control the cell text requires: render a tab body reached through
`global/useFirmContext.ts` under a cross-firm (Global) selection, with a document carrying
`unprojectedGrant.count > 0`, and confirm the badge renders -- CONFIRMING F11's coverage is inherited, not
assumed. If Global mode's own wiring makes this render path materially different from the direct
`StatusPanel` render, name exactly what differs in your result file; do not silently substitute a non-Global
render for this criterion.

<criterion id="F58-AC6" cell_refs="FE-s-58" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F58-AC6` -- the whole IRPT_FNTEND suite is green.

<criterion id="F58-AC7" cell_refs="FE-s-58" judgment="true" drives="none"/>
`F58-AC7` -- graded at L9: the badge idiom matches `portal/CLAUDE.md`'s color law (navy ink on the white
panel, no light-on-light text) -- render and read the screenshot per that file's Verification law, cite the
clause number beside your evidence; F58-AC5's Global-mode control genuinely exercises a DIFFERENT code path
than F58-AC2, not a relabeled copy of the same render. RECORD; NO VERDICT.

<expected_criteria>F58-AC1, F58-AC2, F58-AC3, F58-AC4, F58-AC5, F58-AC6, F58-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/`
  and this order's own file.
- ⛔ **NEVER re-derive `count`/`denominator`/`kinds`.** This cell reads `.availability.unprojectedGrant` as
  carried by FE-s-57; it does not compute, default-guess or infer any of the three fields.
- ⛔ **Color law (portal `CLAUDE.md`).** The badge is navy-on-white text on the panel, never light text on
  light background; run `/frontend-dev` (or an equivalent headless render) and read the screenshot before
  reporting F58-AC7.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or
  `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W8-S<k>`; read both investigation files before minting.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Disjoint by file from FE-s-59/FE-s-60** (this cell touches `state/status.ts` and `tabs/StatusPanel.tsx`
  only); the three wave-B cells run concurrently.

<paths>
portal/src/pages/InvestorReporting/state/status.ts
portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-58/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.9, cell `FE-s-58`.
<owned_cells>FE-s-58</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F58-AC1` .. `F58-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~8/IRPT_FNTEND.TO-FE-s-58.status-panel-unprojected-grant-badge.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F58-AC1,F58-AC2,F58-AC3,F58-AC4,F58-AC5,F58-AC6,F58-AC7 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-58.status-panel-unprojected-grant-badge.md`
BEFORE the `complete` flip. `F58-AC7` recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file
`status-panel-unprojected-grant-badge.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED, prd-signoff.py status).
the design: RUN by the issuer -- state/status.ts:77-88,204-229,258-267 and tabs/StatusPanel.tsx:1-97 read at source (portal DEV 15ceef79); FE-s-57's Availability.unprojectedGrant confirmed present at contracts/index.ts:111-115,157.
the spec: RUN -- PRD v0.7/v0.8/v0.9's unprojected_grant paragraph read in full at HEAD (@5fd2dc9ab5), both halves SIGNED.
lane: the <paths> block IS the grant.
</preflight>

Seating: wave B, slot ~1; seated on FE-s-57's drain (workspace `22f8ee08be`, portal `15ceef79`), disjoint by
file from FE-s-59/FE-s-60.
