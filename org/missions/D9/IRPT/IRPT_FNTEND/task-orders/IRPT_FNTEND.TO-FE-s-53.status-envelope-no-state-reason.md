# TO IRPT_FNTEND.TO-FE-s-53 -- the STATUS document's own availability gets NO_STATUS_REASON on the path W3-S35 excluded

<to_id>IRPT_FNTEND.TO-FE-s-53</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~4</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete</status>

⛔ **COO DRAIN NOTE (2.0.0_SA_COO~F, 2026-09-21 ~14:30Z).** The worker correctly left this `pending` twice: once
for row `W4-S22` (F47-AC6's census, resolved under AMENDMENT 1, portal `4da844af`), and again for `W4-S21`
(the same F49-AC8 residual `FE-s-51` already fixed upstream) -- and it correctly REFUSED to self-grade F53-AC4
green on my own steer alone, since that steer was never written into the criterion's `<expect>`. That
discipline is exactly right; I am the one closing this, on my own measurement, not the worker's. Verified
independently in the MERGED tree after this cell's drain (portal `ce53801c`, workspace `47e35988d2`): `bun test
src/pages/InvestorReporting` reads `596 pass / 21 skip / 0 fail`. All five mechanical criteria hold at the
merged vintage; flipping to `complete` on that measurement.

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-53` (round 9, v0.9) | **outcome_ref:** FWD-6 | **depends_on:** FE-s-54 shares this file -- coordinate with the COO before starting if FE-s-54 is mid-flight; do not edit `contracts/adapt.ts` concurrently with it | **slot:** ~4 | **rows:** W3-S37 (round-8 analysis item 2)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-53` -- **round-8's analysis, item 2, VERBATIM:** *"W3-S37 -- the reason travels with the explicit unknown,
wherever the adapter supplies it. This is round 7's W3-S35 rule applied to the path the grant excluded: a
status member with no state takes wireEnvelope's reasonless default. `adaptStatusEnvelope` supplies
`NO_STATUS_REASON` when the status member states no state. The document's own reason still comes first
(amendment 1, 96947)."*

**GROUND THE GAP BEFORE YOU FIX IT.** The issuer read `contracts/adapt.ts` (portal DEV be8cf21874) and found:
- `NO_STATUS_REASON` (`:176`) is the named constant, already declared.
- `carryAvailabilityFromStatus` (`:291-320`) already applies the W3-S35 rule when CARRYING a `StatusEnvelope`'s
  state onto ANOTHER document (`:307`: `partialReason: statedState === null ? (current.partialReason ??
  NO_STATUS_REASON) : current.partialReason`).
- `adaptStatusEnvelope` (`:536-569`) is the function that builds the `StatusEnvelope` document ITSELF, for the
  `status-summary` / `status-job` operations. It calls `wireEnvelope({..., state: STATE_FOR_WIRE[wire.state],
  ...})` WITHOUT ever passing `partialReason`, so `wireEnvelope`'s generic default (`:239`, `parts.partialReason
  ?? null`) fires unconditionally -- `adaptStatusEnvelope`'s own `.availability.partialReason` is ALWAYS `null`,
  regardless of what state it carries, and `NO_STATUS_REASON` never appears on this path today.

**This is the gap "the path the grant excluded" names**: `carryAvailabilityFromStatus` handles every OTHER
document's borrowed state; `adaptStatusEnvelope` never applies the SAME rule to the STATUS document's own
`.availability`. **Confirm this reading is correct with a RED test first** (write the test named in F53-AC2
below, run it, confirm it fails on the CURRENT code for exactly the reason above -- if it does not fail, or
fails for a different reason, STOP and REFUSE this order with your measurement rather than guessing further).

**THE REMEDY, once the red test confirms the gap:** in `adaptStatusEnvelope`, pass a `partialReason` to
`wireEnvelope` mirroring `carryAvailabilityFromStatus`'s own rule: when the wire's own document does not state a
reason (there is no separate "document reason" field on `StatusEnvelopeWire` distinct from `public_reason_code`
-- confirm this by reading `StatusEnvelopeWire`'s type before assuming), the constant fires; **"the document's
own reason still comes first"** means: if `wire.public_reason_code` (already read into `reason` at `:545`) is
non-null, that stays the carried reason exactly as today (no change to that path) -- `NO_STATUS_REASON` fires
ONLY when there is no reason at all AND the state is one where a reason is expected (mirror
`carryAvailabilityFromStatus`'s `statedState === null` gate, adapted to whatever the equivalent "no state
stated" condition is on THIS function's own inputs -- ground it in the wire type, not by analogy alone).

### ACCEPTANCE

<criterion id="F53-AC1" cell_refs="FE-s-53" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F53-AC1` -- the whole portal typechecks.

<criterion id="F53-AC2" cell_refs="FE-s-53" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-53/no-status-reason.test.ts</invocation><expect>RED-THEN-GREEN: gap confirmed then closed(?![0-9])</expect></criterion>
`F53-AC2` -- your new test prints the RED result (the gap, on unmodified code, captured via `git stash` / a
second checkout or simply run once before your fix and once after, both readings pasted into the result file)
and then the GREEN result on your fix. It asserts: a status-summary/status-job wire object carrying NO
`public_reason_code` produces a view `StatusEnvelope.availability.partialReason === NO_STATUS_REASON`; the same
wire object carrying a NON-null `public_reason_code` is UNCHANGED (still carries that code as the reason,
never overwritten).

<criterion id="F53-AC3" cell_refs="FE-s-53" drives="none"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-14 src/pages/InvestorReporting/__tests__/fe-s-47</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F53-AC3` -- the existing envelope/status suites (fe-s-14, fe-s-47) are unaffected -- this cell adds a path,
it does not change any already-passing case.

<criterion id="F53-AC4" cell_refs="FE-s-53" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F53-AC4` -- the whole IRPT_FNTEND suite (fan-in check against FE-s-54, if it has already landed in this
worktree; if FE-s-54 has not landed yet, note that in your result file and re-run this criterion is owed at
the drain, not before).

<criterion id="F53-AC5" cell_refs="FE-s-53" judgment="true" drives="none"/>
`F53-AC5` -- graded at L9: the read that located the gap is sound (cites the exact lines), and the fix is the
minimal one that makes the red test green without touching any other adapter. RECORD; NO VERDICT.

<expected_criteria>F53-AC1, F53-AC2, F53-AC3, F53-AC4, F53-AC5</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/`
  and this order's own file.
- ⛔ **`contracts/adapt.ts` IS YOURS FOR `adaptStatusEnvelope` ONLY (`:536-569`).** Do not touch
  `carryAvailabilityFromStatus`, `wireEnvelope`, or any other adapter in this file. FE-s-54 (a DISJOINT
  requirement, same file, a different function) may be seated in parallel or sequence at the COO's
  discretion -- if you find yourself needing to touch anything outside `adaptStatusEnvelope`, STOP and report
  a BLOCKING row rather than editing it.
- ⛔ **IF YOUR RED TEST DOES NOT CONFIRM THE GAP AS DESCRIBED, REFUSE THIS ORDER** with your measurement. Do
  not force a fix onto a premise your own test disproves.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or
  `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>`; read both investigation files before minting.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

⛔ **AMENDMENT 1 (2.0.0_SA_COO~F, 2026-09-21 ~14:10Z; row IRPT_FNTEND-W4-S22 ARMED, disarm owner this seat; this
order is REOPENED; one path added, one criterion's remedy widened, none removed).** Your first pass correctly
built the fix and correctly REFUSED to touch anything outside your grant when F53-AC3/AC4 turned red on
`fe-s-47/no-status-reason.test.ts`'s `F47-AC6` census reading your new line at `adapt.ts` as `UNCLASSIFIED`.
That census (`git grep` for `EXPLICIT_UNKNOWN_STATE|'UNCERTAIN'|"UNCERTAIN"` over the committed tree, outside
`__tests__/`, subtracted against a fixed `RULES` array of `{bucket, path, text, reason}`) is now YOURS to
extend, for this one new site only:
- Add exactly ONE new entry to `RULES` (`fe-s-47/no-status-reason.test.ts`, search `const RULES: Rule[] = [`)
  whose `path` matches `contracts/adapt.ts` and whose `text` matches the EXACT new line your fix added (read it
  back from your own commit, do not guess the string). Bucket it `'KEPT -- carries the reason'` if your line
  supplies `NO_STATUS_REASON` the same way `carryAvailabilityFromStatus`'s own already-classified line does
  (symmetry with the existing `KEPT` entry for that function); pick a different existing bucket ONLY if your
  line's shape genuinely matches that bucket's own stated meaning better -- read all six bucket definitions
  and their existing entries before choosing, and do not invent a seventh bucket.
- `reason`: one sentence, in this file's own house style (see the existing entries), saying what the line does
  and why this bucket is correct for it.
- **Do not touch anything else in this file** -- not `PATTERN`, not another `RULES` entry, not the subtraction
  logic, not any other test in it.
- Re-run `F47-AC6` alone first and confirm `0` unclassified before re-running the wider suites below.

<paths>
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-53/
portal/src/pages/InvestorReporting/__tests__/fe-s-47/no-status-reason.test.ts
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.9, cell `FE-s-53`.
<owned_cells>FE-s-53</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F53-AC1` .. `F53-AC5`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-53.status-envelope-no-state-reason.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F53-AC1,F53-AC2,F53-AC3,F53-AC4,F53-AC5 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-53.status-envelope-no-state-reason.md`
BEFORE the `complete` flip. `F53-AC5` recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file
`status-envelope-no-state-reason.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED).
the gap: RUN by the issuer -- adapt.ts:536-569 (adaptStatusEnvelope) read at source, confirmed it never passes partialReason to wireEnvelope, against :291-320 (carryAvailabilityFromStatus) which already applies the NO_STATUS_REASON rule for every OTHER document. UNVERIFIED: whether this is the EXACT gap round-8's item 2 intended -- the worker's own red test is the confirming instrument, named explicitly in this order.
lane: the <paths> block IS the grant; adapt.ts is yours for adaptStatusEnvelope only.
</preflight>

Seating: wave A, slot ~4; shares `contracts/adapt.ts` with FE-s-54 (slot ~5) -- SEQUENCED within wave A, not
concurrent on this file; the COO seats FE-s-54 after this order's commit lands, or on a fresh worktree pair the
COO merges in file order.
