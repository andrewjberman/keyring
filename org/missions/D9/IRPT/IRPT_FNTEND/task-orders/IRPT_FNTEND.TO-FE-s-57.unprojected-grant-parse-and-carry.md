# TO IRPT_FNTEND.TO-FE-s-57 -- unprojected_grant is parsed off the response envelope and carried onto every adapted document's availability

<to_id>IRPT_FNTEND.TO-FE-s-57</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~7</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-57` (round 9, v0.9, ROOT of wave B) | **outcome_ref:** FWD-3, FWD-4, FWD-5, FWD-6, FWD-8, FWD-11 (carrying half only; no rendering) | **depends_on:** none | **slot:** ~8 | **rows:** PRD v0.7/v0.8/v0.9 `CONTRACTS` section, `unprojected_grant` paragraph

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-57` -- **the PRD's `unprojected_grant` paragraph (v0.7/v0.8/v0.9, `IRPT_FNTEND_PRD.md` `CONTRACTS`
section) is a NEW envelope-level field the counterpart ships on the SERVED RESPONSE ENVELOPE, `{count,
denominator, kinds}`, top-level and NON-OPTIONAL, PRESENT-AT-ZERO on every non-refused response, ABSENT BY
DESIGN on a refusal.** This cell CARRIES the field from the wire into every adapted document's `.availability`;
it renders NOTHING (FE-s-58/59/60, wave B, render it once this cell lands).

**Read the PRD's own text before you start** (`org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`, the
long `unprojected_grant` paragraph in `CONTRACTS`) -- it is the ratified spec and this cell text summarizes it;
where the two differ, the PRD governs.

**EXACT CHANGES, at portal DEV be8cf21874's current shape (confirm each line number against YOUR checkout
before editing -- cite what you actually find, not this order's numbers, if they have drifted):**

1. **`contracts/index.ts`** (`Availability` interface, `:110-134`): add one new exported type,
   ```ts
   export interface UnprojectedGrant {
     readonly count: number
     readonly denominator: number
     readonly kinds: readonly string[]
   }
   ```
   and one new member on `Availability`: `unprojectedGrant: UnprojectedGrant | null`. Disjoint from every
   existing member; do not touch `partialReason`, `publicReasonCode`, or any other field.

2. **`contracts/adapt.ts`**:
   - `EnvelopeParts` (`:188-213`) gains `unprojectedGrant?: UnprojectedGrant | null`.
   - `wireEnvelope()` (`:220-258`): the `availability` object it builds (`:236-247`) gains
     `unprojectedGrant: parts.unprojectedGrant ?? null` -- the explicit-unknown default (null = "not yet
     attached"), so EVERY existing call site (all ten document adapters) is UNCHANGED by this addition; only a
     caller that explicitly passes the new part is affected.
   - A NEW function, mirroring `carryAvailabilityFromStatus`'s (`:291-320`) shape EXACTLY -- same array/object
     recursion, same null-safety:
     ```ts
     export function carryUnprojectedGrant<T>(view: T, grant: UnprojectedGrant | null): T {
       if (Array.isArray(view)) return view.map((member) => carryUnprojectedGrant(member, grant)) as unknown as T
       if (view === null || typeof view !== 'object') return view
       const current = (view as { availability?: Availability }).availability
       if (current === undefined) return view
       return { ...(view as object), availability: { ...current, unprojectedGrant: grant } } as T
     }
     ```
     (Adjust import list / exact typing to match this file's own conventions; the shape above is the
     REQUIREMENT, not verbatim-required source text.)

3. **`contracts/envelope.ts`**:
   - `IrEnvelopeField` (`:69`) gains `'unprojected_grant'`.
   - `parseIrEnvelope()` (`:180-237`): the REFUSED branch (`:195-208`) is UNCHANGED -- absence there is by
     design, `data` is already `null`. On the non-refused branch, AFTER `const data =
     carryAvailabilityFromStatus(adapt(body.data), status)` (`:219`), read `body.unprojected_grant`; if it is
     not shaped `{count: number, denominator: number, kinds: string[]}` (a plain runtime shape check -- no new
     dependency), throw `new EnvelopeMismatch('unprojected_grant', operation)` (mirrors this file's own
     established idiom for every other contract violation); else call `data = carryUnprojectedGrant(data,
     grant)` before the `return`.
   - ⛔ **THIS THROW MUST NOT FIRE ON THE `irpt-holdings` ROUTE.** Per PRD v0.9: that route's forked module
     always sends `{count: 0, ...}` (present, just structurally zero) -- it never omits the key. So the throw
     only fires on a route that omits the key ENTIRELY, which the PRD calls a genuine backend defect on every
     route including holdings. Your test (F57-AC3) must exercise a holdings fixture with `{count: 0, ...}`
     PRESENT and confirm it does NOT throw.

### ACCEPTANCE

<criterion id="F57-AC1" cell_refs="FE-s-57" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F57-AC1` -- the whole portal typechecks.

<criterion id="F57-AC2" cell_refs="FE-s-57" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-57/carry.test.ts</invocation><expect>UNPROJECTED_GRANT PRESENT-AT-ZERO CARRIED ON 12 of 12 OPERATIONS(?![0-9])</expect></criterion>
`F57-AC2` -- for EACH of the 12 `RESPONSE_OPERATIONS` (`contracts/wire/responses.ts:217-230`), construct a
minimal well-formed non-refused response body carrying `unprojected_grant: {count: 0, denominator: <n>, kinds:
[]}` and confirm `parseIrEnvelope(...)`'s returned `data.availability.unprojectedGrant` equals it exactly.
Print `12 of 12`, never a subset.

<criterion id="F57-AC3" cell_refs="FE-s-57" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-57/carry.test.ts</invocation><expect>HOLDINGS ROUTE, count:0, NO THROW: yes(?![0-9])</expect></criterion>
`F57-AC3` -- the `holdings-snapshot` operation specifically, with `unprojected_grant: {count: 0, ...}` present,
parses cleanly with no exception (the v0.9 carve-out, confirmed rather than assumed).

<criterion id="F57-AC4" cell_refs="FE-s-57" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-57/carry.test.ts</invocation><expect>MISSING KEY ON A NON-REFUSED RESPONSE THROWS EnvelopeMismatch\('unprojected_grant'\): yes(?![0-9])</expect></criterion>
`F57-AC4` -- a non-refused response body with NO `unprojected_grant` key at all throws
`EnvelopeMismatch('unprojected_grant', operation)`.

<criterion id="F57-AC5" cell_refs="FE-s-57" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-57/carry.test.ts</invocation><expect>REFUSED RESPONSE: unprojectedGrant KEY ABSENT, NO THROW: yes(?![0-9])</expect></criterion>
`F57-AC5` -- a refused response (a dispatcher refusal code, or `public_reason_code: 'UNPROJECTED_GRANT'`
specifically) carries no `unprojected_grant` key at all and does NOT throw -- absence there is by design, per
the PRD.

<criterion id="F57-AC6" cell_refs="FE-s-57" drives="none"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-1 src/pages/InvestorReporting/__tests__/fe-s-14</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F57-AC6` -- every existing adapter/envelope test is UNCHANGED (the new part is optional, defaulted to null,
and no existing call site passes it).

<criterion id="F57-AC7" cell_refs="FE-s-57" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F57-AC7` -- the whole IRPT_FNTEND suite is green.

<criterion id="F57-AC8" cell_refs="FE-s-57" judgment="true" drives="none"/>
`F57-AC8` -- graded at L9: `carryUnprojectedGrant` genuinely mirrors `carryAvailabilityFromStatus`'s shape (no
divergent null-handling), and this cell renders nothing -- confirm no `.tsx` file changed in this commit.
RECORD; NO VERDICT.

<expected_criteria>F57-AC1, F57-AC2, F57-AC3, F57-AC4, F57-AC5, F57-AC6, F57-AC7, F57-AC8</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/`
  and this order's own file.
- ⛔ **THIS CELL RENDERS NOTHING.** No `.tsx` file changes. FE-s-58/59/60 (wave B) do the rendering, once this
  cell's field exists to render.
- ⛔ **THE THROW ON A MISSING KEY BINDS EVERY NON-REFUSED RESPONSE, HOLDINGS INCLUDED** -- holdings is exempt
  from the COUNT being MEANINGFUL, never from the KEY being PRESENT. Do not special-case holdings in
  `parseIrEnvelope`; F57-AC3 already proves the general rule handles it correctly (key present, value 0).
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or
  `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>`; read both investigation files before minting.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- ⛔ **THIS IS THE ROOT OF WAVE B (FE-s-58, 59, 60 depend on it).** Report your commit hash clearly in your
  final message so the COO can seat wave B against it without re-deriving it.

⛔ **AMENDMENT 1 (2.0.0_SA_COO~F, 2026-09-21 ~14:15Z; row IRPT_FNTEND-W7-S1 ARMED, disarm owner this seat; this
order is REOPENED; ~15 test directories added to the grant, none removed).** Your first pass built exactly what
BOUNDS demands (the unconditional throw) and correctly made `unprojectedGrant` OPTIONAL on `Availability` rather
than forcing a premise your own typecheck disproved -- both calls stand. The genuine gap your own measurement
found: the PRD's own premise is that the backend ALREADY ships `unprojected_grant` PRESENT-AT-ZERO on every
real, non-refused response; the ~15 pre-existing test directories that build a response body BY HAND without
that key are what is STALE, not your throw. **The remedy is to update those fixtures to match production
reality, not to weaken the parser.**

- Your grant now includes every one of the test directories your own F57-AC6/AC7 runs named as failing:
  `fe-s-1, fe-s-14, fe-s-19, fe-s-25, fe-s-26, fe-s-30, fe-s-31, fe-s-33, fe-s-34, fe-s-35, fe-s-39, fe-s-41,
  fe-s-42, fe-s-48, fe-s-49` (see `<paths>` below for the exact directory list -- re-run F57-AC6/AC7 first and
  use YOUR OWN fresh failure output as the authoritative list of files/lines to touch, since a re-run may
  surface a slightly different set than your first pass if anything shifted upstream).
- For EVERY hand-built response body in those directories that is NON-REFUSED (carries `data`, no dispatcher
  refusal code) and currently lacks `unprojected_grant`, add `unprojected_grant: { count: 0, denominator: <a
  real, sensible value for that fixture's own shape -- e.g. the count of items the fixture itself enumerates,
  or 0 if none apply>, kinds: [] }` at the SAME level as `data`/`status`/`contract_version` in that body.
  **Never add it to a REFUSED body** (one that carries a dispatcher refusal code and no `data`) -- absence
  there is correct per F57-AC5's own rule; if a file mixes both shapes, touch only the non-refused ones.
- **Do not touch test ASSERTIONS unless a test explicitly asserts on the ABSENCE of `unprojected_grant`** (which
  would now be wrong) -- most tests assert on other fields and simply need the fixture body completed, not the
  assertions rewritten.
- Re-run F57-AC6 then F57-AC7 after each directory or in batches; do not wait until all ~15 are done to run
  either for the first time -- if one directory's fix reveals a DIFFERENT, unrelated failure, STOP on that
  directory, file a row, and continue with the rest.
- Once F57-AC6 and F57-AC7 both read `0 fail`, flip `<status>` to `complete`, file your proof-of-spec instance,
  commit, and send your FINAL WORKER REPORT once. **Still report your final portal commit hash clearly** --
  wave B seats against it.

<paths>
portal/src/pages/InvestorReporting/contracts/index.ts
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/contracts/envelope.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-57/
portal/src/pages/InvestorReporting/__tests__/fe-s-1/
portal/src/pages/InvestorReporting/__tests__/fe-s-14/
portal/src/pages/InvestorReporting/__tests__/fe-s-19/
portal/src/pages/InvestorReporting/__tests__/fe-s-25/
portal/src/pages/InvestorReporting/__tests__/fe-s-26/
portal/src/pages/InvestorReporting/__tests__/fe-s-30/
portal/src/pages/InvestorReporting/__tests__/fe-s-31/
portal/src/pages/InvestorReporting/__tests__/fe-s-33/
portal/src/pages/InvestorReporting/__tests__/fe-s-34/
portal/src/pages/InvestorReporting/__tests__/fe-s-35/
portal/src/pages/InvestorReporting/__tests__/fe-s-39/
portal/src/pages/InvestorReporting/__tests__/fe-s-41/
portal/src/pages/InvestorReporting/__tests__/fe-s-42/
portal/src/pages/InvestorReporting/__tests__/fe-s-48/
portal/src/pages/InvestorReporting/__tests__/fe-s-49/
portal/src/pages/InvestorReporting/fixtures/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.9, cell `FE-s-57`.
<owned_cells>FE-s-57</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F57-AC1` .. `F57-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~7/IRPT_FNTEND.TO-FE-s-57.unprojected-grant-parse-and-carry.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F57-AC1,F57-AC2,F57-AC3,F57-AC4,F57-AC5,F57-AC6,F57-AC7,F57-AC8 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-57.unprojected-grant-parse-and-carry.md`
BEFORE the `complete` flip. `F57-AC8` recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file
`unprojected-grant-parse-and-carry.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED, prd-signoff.py status).
the design: RUN by the issuer -- contracts/index.ts:110-134, contracts/adapt.ts:188-320, contracts/envelope.ts:69-237 all read at source (portal DEV be8cf21874); the mirrored carryAvailabilityFromStatus pattern is a real, existing precedent in this file, not invented.
the spec: RUN -- PRD v0.7/v0.8/v0.9's unprojected_grant paragraph read in full at HEAD (@5fd2dc9ab5), both halves SIGNED.
lane: the <paths> block IS the grant; renders nothing.
</preflight>

Seating: wave A, slot ~8; ready root, no dependency edge with 50-56. IS THE DEPENDENCY for wave B (58, 59, 60) --
the COO seats those only after this order's commit is confirmed present.
