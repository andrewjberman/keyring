# TO IRPT_FNTEND.TO-FE-s-50 -- the wire-header hash is independent of checkout line endings

<to_id>IRPT_FNTEND.TO-FE-s-50</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-50` (round 9, v0.9 @<this commit>) | **outcome_ref:** FWD-1, FWD-11 (evidence) | **depends_on:** none | **slot:** ~1 | **rows:** S68 (round-8 analysis item 6), C-S108

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-50` -- **`gen-wire.ts`'s `sha256Of()` hashes the raw file bytes it read from disk, so the "Source sha256:"
comment stamped into every generated `contracts/wire/*.ts` file differs depending on whether the checkout's
line endings are CRLF or LF, even though the schema's MEANING is unchanged.** Measured by the issuer
(`2.0.0_SA_COO~F`, row S68, round 8): `F25-AC8` read this exact difference as a real drift and it was ruled a
line-ending artifact, not a schema change (CTO ruling 97020, PROCEED).

Four call sites read the raw file text and hash it with no normalization, at `portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts`:
- `:107-109` -- `sha256Of(text)`, the function itself.
- `:293` -- `renderModule()`: `const digest = sha256Of(schemaText)`, the per-document wire header.
- `:365` and `:373` -- `renderResponses()`'s per-operation loop: two calls to `sha256Of(text)` for the same
  response schema text (the header comment and the `pins` array entry).
- `:487` -- `generate()`'s main loop: `text = readFileSync(schemaFilePath(name), 'utf8')` then
  `sha256Of(text)`, for every document schema in `WIRE_CONTRACTS`.

**THE REMEDY:** normalize CRLF to LF before hashing, at the ONE place text enters this file's hash path, so all
four call sites are fixed by one change. Add a small helper, `stableTextForHash(text: string): string { return
text.replace(/\r\n/g, '\n') }`, and call `sha256Of(stableTextForHash(text))` (or `stableTextForHash(schemaText)`
at `:293`) at every one of the four sites. **`sha256Of` itself is UNCHANGED** -- it is a pure hash function and
is reused elsewhere in this file for other purposes the cell does not touch; only its CALLERS in the four
named lines gain the normalization. The rendered TypeScript body (the actual generated interface/type code) is
NOT changed by this cell -- only the "Source sha256:" comment value changes, and only when the checkout's line
endings actually differ from what produced the currently-committed value.

**Then regenerate and commit:** run the generator (`generate()`'s entry point -- find it via `package.json`'s
script that invokes this file, or run it directly with `bun run` against the file's own CLI entry if one
exists; if none exists, invoke `generate()` via a one-line `bun run` of a scratch script under
`<WS>/.scratch/` that imports and calls it) and commit the regenerated `contracts/wire/*.ts` files if their
hash comments changed on THIS checkout. If they do NOT change (this checkout's line endings already match what
produced the committed hashes), that is a valid, reportable outcome -- do not force a change.

### ACCEPTANCE

<criterion id="F50-AC1" cell_refs="FE-s-50" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F50-AC1` -- the whole portal typechecks.

<criterion id="F50-AC2" cell_refs="FE-s-50" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-50/hash-stability.test.ts</invocation><expect>SAME HASH AT CRLF AND LF: (\d+) of \1(?![0-9])</expect></criterion>
`F50-AC2` -- your new test, one case per one of the four call sites (so the denominator is 4): for each, build
the SAME schema/response text twice -- once with its real line endings, once with every `\n` replaced by
`\r\n` -- call the fixed code path on both, and assert the two produced digests are IDENTICAL. Print the
denominator as `4 of 4`.

<criterion id="F50-AC3" cell_refs="FE-s-50" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-13</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F50-AC3` -- the existing fe-s-13 generator suite (content-pins, request-corpus, gen-consumed) is unaffected.

<criterion id="F50-AC4" cell_refs="FE-s-50" drives="none"><invocation>cd <WS>/portal && git status --porcelain src/pages/InvestorReporting/contracts/wire/ && git diff --stat src/pages/InvestorReporting/contracts/wire/ | tail -5</invocation><expect>.*</expect></criterion>
`F50-AC4` -- print whatever the regeneration changed (may legitimately be empty on this checkout). Report the
`git diff --stat` output in your result file whichever way it reads; an empty diff is not a failure here.

<criterion id="F50-AC5" cell_refs="FE-s-50" judgment="true" drives="none"/>
`F50-AC5` -- graded at L9: the fix is at the read boundary (one normalization point), not scattered per-callsite
logic, and the regenerated headers (if any changed) are the ONLY diff in `contracts/wire/`. RECORD; NO VERDICT.

<expected_criteria>F50-AC1, F50-AC2, F50-AC3, F50-AC4, F50-AC5</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and
  this order's own file.
- ⛔ **`gen-wire.ts` IS YOURS FOR THE HASH-INPUT NORMALIZATION ONLY.** Add the helper and call it at the four
  named lines. Do not change `renderType`, `renderIndex`, `routeRows`, or any other function's logic.
- ⛔ **`contracts/wire/*.ts` FILES ARE GENERATED OUTPUT.** You may only regenerate them by running the
  generator, never hand-edit a hash comment.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed,
  named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or
  `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>` -- read the WHOLE channel plane
  (both `INVESTIGATION_v1.md` and `_v2.md`) before minting a fresh number; an INERT row OMITS `disarm_owner`;
  write with `newline='\n'` and read the diffstat of your own commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-50/
portal/src/pages/InvestorReporting/contracts/wire/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.9, cell `FE-s-50`.
<owned_cells>FE-s-50</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F50-AC1` .. `F50-AC5`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-50.gen-wire-crlf-independent-hash.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F50-AC1,F50-AC2,F50-AC3,F50-AC4,F50-AC5 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-50.gen-wire-crlf-independent-hash.md`
BEFORE the `complete` flip. `F50-AC5` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at
L9. Result file `gen-wire-crlf-independent-hash.result.md` beside it. Flip only when every mechanical criterion
PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED, prd-signoff.py status).
the defect: RUN by the issuer, round-8 analysis item 6 (S68) + CTO ruling 97020 (PROCEED, a line-ending artifact) -- gen-wire.ts:107-109, :293, :365, :373, :487 read via source inspection at portal DEV be8cf21874.
lane: the <paths> block IS the grant; gen-wire.ts is yours for the normalization only.
</preflight>

Seating: wave A, slot ~1; ready root, no dependency edge with any other round-9 cell.
