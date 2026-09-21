# TO IRPT_FNTEND.TO-FE-s-60 -- PeriodInContextPage renders the narrative packet's carried unprojected_grant, in both the preview and the printed PDF

<to_id>IRPT_FNTEND.TO-FE-s-60</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~10</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-60` (round 9, v0.9, wave B) | **outcome_ref:** FWD-8 | **depends_on:** FE-s-57 (merged, workspace `22f8ee08be`, portal `15ceef79`) | **slot:** ~3 | **rows:** R9.2 `FE-s-60`

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-60` -- **round 9's decomposition, `R9.2`, VERBATIM:** *"`render/narrative/PeriodInContextPage.tsx`
composes from `NarrativePacket` (`:51`); render the same badge reading `packet.availability.unprojectedGrant`,
on the page itself (this IS the exported-PDF path, so the badge must appear in BOTH the on-screen preview and
the printed PDF -- one render, both consumers, no second copy)."*

`FE-s-57` (this cell's dependency) has landed: `NarrativePacket extends ContractEnvelope`, and
`ContractEnvelope.availability: Availability` (`contracts/index.ts:242-248`) now carries the optional
`unprojectedGrant?: UnprojectedGrant | null` member (`:111-115`, `:157`). This cell is the RENDERING half only
-- it never re-derives the count, denominator or kinds; it reads what `packet.availability.unprojectedGrant`
already carries. **ONE render, both consumers**: `PeriodInContextPage.tsx` is used for both the on-screen
preview AND the exported PDF (per this file's own header, `:14-17`: `render/performance/
PerformanceDocument.tsx` mounts it with `{packet, report}` for the print path) -- do not add a second,
print-only copy of the badge; the ONE JSX node this cell adds must be what BOTH paths render.

**Read the PRD's own `unprojected_grant` paragraph** (`org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`,
`CONTRACTS` section) before you start -- it is the ratified spec; where this cell's text and the PRD differ, the
PRD governs.

**EXACT CHANGES, at portal DEV `15ceef79`'s current shape (confirm each line number against YOUR checkout before
editing -- cite what you actually find, not this order's numbers, if they have drifted):**

1. **`render/narrative/PeriodInContextPage.tsx`**:
   - `PeriodInContextPageProps.packet` is already typed `NarrativePacket` (`:83-84`), which already carries
     `.availability.unprojectedGrant` via `ContractEnvelope`; no prop-type change needed.
   - Inside `PeriodInContextPage` (`:90-217`), add ONE new conditional block reading
     `packet.availability.unprojectedGrant`, rendered ONLY when present and `count > 0`, carrying
     `data-slot="partial-disclosure"` (the SAME slot name `FE-s-58`/`FE-s-59` use, so the three surfaces are
     queryable identically) and `data-block="partial-disclosure"` (matching this file's own convention of
     pairing `data-block` with `data-slot="fe-s-8"` at the section root, `:94`) -- site it near the top of the
     section (e.g. immediately after the `fixed-statement` paragraph, `:96-98`, before the chart), since it is
     a document-level fact about the packet as a whole, not scoped to any one window or citation.
   - Text idiom: reuse this file's existing `ir-note`/`ir-muted` classes (e.g. `:188-190`'s
     `narrative-coverage` paragraph is the closest existing precedent -- a document-level fact rendered as a
     single `<p>`), never a new ad-hoc style; navy-ink-on-white per portal `CLAUDE.md`'s color law (this page's
     `ir-*` classes already resolve to that palette -- confirm by reading `src/index.css`'s `.ir-note` rule
     rather than assuming).
   - **No clock, no randomness** -- this file's own header bound (`:48`) applies to your addition too: the
     badge's count/denominator/kinds come ONLY from `packet.availability.unprojectedGrant`, nothing computed
     from the current time.

### ACCEPTANCE

<criterion id="F60-AC1" cell_refs="FE-s-60" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F60-AC1` -- the whole portal typechecks.

<criterion id="F60-AC2" cell_refs="FE-s-60" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-60/period-in-context-badge.test.ts</invocation><expect>PARTIAL-DISCLOSURE RENDERS WHEN count>0: yes(?![0-9])</expect></criterion>
`F60-AC2` -- a `NarrativePacket` whose `.availability.unprojectedGrant` carries `{count: 1, denominator: 5,
kinds: ['events']}` renders the `data-slot="partial-disclosure"` node, and its text names `1`, `5` and
`events` verbatim.

<criterion id="F60-AC3" cell_refs="FE-s-60" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-60/period-in-context-badge.test.ts</invocation><expect>PARTIAL-DISCLOSURE ABSENT WHEN count=0 OR NULL: yes(?![0-9])</expect></criterion>
`F60-AC3` -- TWO arms: `unprojectedGrant: {count: 0, ...}` and `unprojectedGrant: null` BOTH render no
`data-slot="partial-disclosure"` node. Print both arms, never a subset.

<criterion id="F60-AC4" cell_refs="FE-s-60" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-60/period-in-context-badge.test.ts</invocation><expect>ONE RENDER, BOTH CONSUMERS -- PREVIEW MOUNT AND PDF MOUNT SHOW THE IDENTICAL NODE: yes(?![0-9])</expect></criterion>
`F60-AC4` -- render `PeriodInContextPage` twice with the SAME `count>0` packet: once as it is mounted
standalone (the on-screen preview path) and once as it is mounted via `render/performance/
PerformanceDocument.tsx` (the print/PDF path). Both renders must contain the identical
`data-slot="partial-disclosure"` markup (same text) -- confirming ONE component serves both consumers, no
second copy was added.

<criterion id="F60-AC5" cell_refs="FE-s-60" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F60-AC5` -- the whole IRPT_FNTEND suite is green.

<criterion id="F60-AC6" cell_refs="FE-s-60" judgment="true" drives="none"/>
`F60-AC6` -- graded at L9: the badge idiom matches `portal/CLAUDE.md`'s color law and this file's own `ir-*`
class conventions (cite the specific class read from `src/index.css`, not assumed); F60-AC4 genuinely proves
one shared render path, not two independently-written copies that happen to look the same. RECORD; NO
VERDICT.

<expected_criteria>F60-AC1, F60-AC2, F60-AC3, F60-AC4, F60-AC5, F60-AC6</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/`
  and this order's own file.
- ⛔ **NEVER re-derive `count`/`denominator`/`kinds`.** This cell reads `.availability.unprojectedGrant` as
  carried by FE-s-57; it does not compute, default-guess or infer any of the three fields.
- ⛔ **ONE RENDER, BOTH CONSUMERS.** Do not add a second, print-only copy of the badge in
  `render/performance/PerformanceDocument.tsx` or anywhere else -- the ONE node added to
  `PeriodInContextPage.tsx` must be what both the preview and the PDF path render. If you find the print path
  genuinely cannot reach this component's DOM the same way, STOP and file a row rather than duplicating.
- ⛔ **Color law (portal `CLAUDE.md`).** Navy-on-white text, never light text on light background; render
  and read a screenshot before reporting F60-AC6.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or
  `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W10-S<k>`; read both investigation files before minting.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Disjoint by file from FE-s-58/FE-s-59** (this cell touches `render/narrative/PeriodInContextPage.tsx`
  only, plus `compose.ts` ONLY if the packet's field genuinely needs surfacing there first -- confirm before
  touching it, since `packet.availability` is already reachable directly per the cell text); the three wave-B
  cells run concurrently.

<paths>
portal/src/pages/InvestorReporting/render/narrative/PeriodInContextPage.tsx
portal/src/pages/InvestorReporting/render/narrative/compose.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-60/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.9, cell `FE-s-60`.
<owned_cells>FE-s-60</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F60-AC1` .. `F60-AC6`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~10/IRPT_FNTEND.TO-FE-s-60.period-in-context-unprojected-grant-badge.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F60-AC1,F60-AC2,F60-AC3,F60-AC4,F60-AC5,F60-AC6 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-60.period-in-context-unprojected-grant-badge.md`
BEFORE the `complete` flip. `F60-AC6` recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file
`period-in-context-unprojected-grant-badge.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED, prd-signoff.py status).
the design: RUN by the issuer -- render/narrative/PeriodInContextPage.tsx:1-217 read at source (portal DEV 15ceef79); NarrativePacket extends ContractEnvelope confirmed at contracts/index.ts:242-248,823-836; FE-s-57's Availability.unprojectedGrant confirmed present.
the spec: RUN -- PRD v0.7/v0.8/v0.9's unprojected_grant paragraph read in full at HEAD (@5fd2dc9ab5), both halves SIGNED.
lane: the <paths> block IS the grant.
</preflight>

Seating: wave B, slot ~3; seated on FE-s-57's drain (workspace `22f8ee08be`, portal `15ceef79`), disjoint by
file from FE-s-58/FE-s-59.
