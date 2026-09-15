# TO IRPT_FNTEND.TO-FE-s-47 -- a response with no status says why its state is unknown

<to_id>IRPT_FNTEND.TO-FE-s-47</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~3</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F6, F7; CONTRACTS consumed) | **Decomp cell:** `FE-s-47` (round 8, v0.8 @734eb61ac1) | **outcome_ref:** FWD-5, FWD-6 | **depends_on:** none | **slot:** ~3 | **rows:** C-S97 (W3-S35)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-47` -- **a response that carries no status reaches the screen as UNCERTAIN with nothing to explain it, and the portal's own validator refuses the document the adapter built.** This is row W3-S35, graduated by 3.0.0_SA_CVO as C-S97. `1.0.0_SA_CTO` ruled it in the round-7 analysis (msg 96865, item 5): **the ADAPTER supplies the reason, and the validator does not change.**

Measured by the issuer at portal DEV 1f3ce9f0:
- **The refusal.** `contracts/validate.ts:95-96` refuses any availability whose state is not READY or LOADING and which carries neither `partialReason` nor `publicReasonCode`: *"state '...' carries NEITHER partialReason NOR publicReasonCode"*.
- **Where the explicit unknown enters an Availability.** `EXPLICIT_UNKNOWN_STATE` is `'UNCERTAIN'` (`contracts/adapt.ts:167`).
  - `wireEnvelope` (`adapt.ts:227-231`) sets `state: parts.state ?? EXPLICIT_UNKNOWN_STATE` and `partialReason: parts.partialReason ?? null`. No document schema carries a state, so every adapted document starts here as the explicit unknown with no reason.
  - `carryAvailabilityFromStatus` (`adapt.ts:289-293`) is the seam `parseIrEnvelope` calls for every operation (`contracts/envelope.ts:219`). It sets `state: status?.state ?? EXPLICIT_UNKNOWN_STATE`, but `partialReason: current.partialReason`, the document's own.
  - So with no status, the carried document is UNCERTAIN with `partialReason` null, and validate refuses it.
  - `envelope.ts:233` sets the PARSED ENVELOPE's own `state` to the explicit unknown too. That is `IrParsedEnvelope.state`, which has no reason member: it is not an Availability, so it is outside this cell by type.
- **How common the path is.** `RESPONSE_STATUS_REQUIRED` (`contracts/wire/responses.ts:236-249`) makes the status OPTIONAL on 11 of 12 operations; only `analysis-requests` requires one. The comment at `envelope.ts:231` says "ten of the twelve", which is stale by one.
- **No production path runs the validator** (the CTO's read: `validateContract` has 1 definition and 8 test uses). So the defect is on the screen: the state renders UNCERTAIN, and the reason renderers find nothing. They are `render/Page.tsx:160` (`reasonText: nonEmpty(availability.partialReason)`) and `tabs/reporting/AnswerStatus.tsx:56`.
- **The hazard the fix must not create.** `carryAvailabilityFromStatus` carries the DOCUMENT's `partialReason` forward (`:292`). A "no status" reason set in `wireEnvelope` would therefore ride onto a response whose status DOES state a state. The reason belongs to the no-status case only.
- **The issuer's probe.** The minimal change (the carry supplies a reason when no status, or no stated state, arrived) turned 0 tests red in the whole suite: 559 pass, 18 skip, 1 fail of 578. The 1 fail is F41-AC5's control timing out under load, which is FE-s-46's and unrelated.

**THE REMEDY (the CTO's RULING):**
- When the adapter supplies its explicit unknown because the response carried no status, or a status with no state, it also supplies a `partialReason` saying so. That reason is ONE named constant, never re-typed.
- A response whose status states a state never carries that reason.
- `validate.ts` is unchanged. Relaxing it would also admit a producer's reasonless non-READY state, because the validator cannot tell the two apart.

### ACCEPTANCE

<criterion id="F47-AC1" cell_refs="FE-s-47" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F47-AC1` -- the whole portal typechecks.

<criterion id="F47-AC2" cell_refs="FE-s-47" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-47/no-status-reason.test.ts</invocation><expect>A NO-STATUS DIRECTORY BODY THROUGH parseIrEnvelope AND validateContract READS 0 PROBLEMS: yes</expect></criterion>
`F47-AC2` -- W3-S35, the CTO's criterion.
- Build the body from the committed wire instance `fixtures/wire/DirectoryEntry.valid.json['instance']` with its `status` member removed, read with `git cat-file blob HEAD:<path>`.
- Run it through the real `parseIrEnvelope('directory-search', ...)`, then `validateContract('DirectoryEntry', <each adapted entry>)`.
- Print the problems list (empty), the carried state and the carried `partialReason`.

<criterion id="F47-AC3" cell_refs="FE-s-47" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-47/no-status-reason.test.ts</invocation><expect>A STATED STATE NEVER CARRIES THE NO-STATUS REASON: (\d+) of \1(?![0-9])</expect></criterion>
`F47-AC3` -- the control for the hazard above.
- Use the same body with a status that STATES its state. The arms are READY, LOADING, and at least one other state the StatusEnvelope contract admits, stated with its own `publicReasonCode` or reason.
- The carried `partialReason` is exactly what the status and document state in each arm, and never the no-status constant.
- Print each arm.

<criterion id="F47-AC4" cell_refs="FE-s-47" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-47/no-status-reason.test.ts</invocation><expect>THE SAME DOCUMENT WITH ITS REASON STRIPPED IS REFUSED: yes</expect></criterion>
`F47-AC4` -- the arm that can say no. The adapted document from F47-AC2, with `partialReason` set back to null, still gets validate's reasonless-UNCERTAIN refusal. That shows the reason is what makes AC2's 0, and that validate still refuses a reasonless non-READY state.

<criterion id="F47-AC5" cell_refs="FE-s-47" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-47/no-status-reason.test.ts</invocation><expect>validate.ts UNCHANGED FROM DEV 1f3ce9f0: yes</expect></criterion>
`F47-AC5` -- the ruling's other half: `git rev-parse HEAD:<validate.ts>` equals `git rev-parse 1f3ce9f0:<validate.ts>`. Print both blob ids.

<criterion id="F47-AC6" cell_refs="FE-s-47" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-47/no-status-reason.test.ts</invocation><expect>EVERY EXPLICIT UNKNOWN THAT REACHES A RESPONSE'S AVAILABILITY CARRIES ITS REASON: (\d+) of \1(?![0-9])</expect></criterion>
`F47-AC6` -- the reach, BY SUBTRACTION over the corpus (RULING X), from the COMMITTED tree.
- Enumerate every site outside `__tests__/` where `EXPLICIT_UNKNOWN_STATE` (or a literal `'UNCERTAIN'`) can become an Availability's state, and print the denominator.
- Subtract, printed with a reason each:
  - the sites that are not an Availability (`envelope.ts:233`'s parsed-envelope `state`);
  - the sites whose output is always overwritten on a response path before it is read (`wireEnvelope`'s, if it is).
- What remains carries the reason.

<criterion id="F47-AC7" cell_refs="FE-s-47" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-47/no-status-reason.test.ts</invocation><expect>NO STATUS-OPTIONAL OPERATION IS REFUSED FOR A REASONLESS UNCERTAIN: (\d+) of \1(?![0-9])</expect></criterion>
`F47-AC7` -- the class, not the one instance.
- The population is every operation that `RESPONSE_STATUS_REQUIRED` marks false AND whose adapted document carries an availability, from its committed wire instance with `status` removed, through `parseIrEnvelope` and `validateContract`. Print the denominator.
- The bar reads only the reasonless-UNCERTAIN refusal. Any OTHER problem an instance shows is printed, not graded, and is a surprise row.

<criterion id="F47-AC8" cell_refs="FE-s-47" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-47/no-status-reason.test.ts</invocation><expect>THE MOUNTED STATUS PANEL SHOWS THE NO-STATUS REASON: yes</expect></criterion>
`F47-AC8` -- on the screen, which is where the defect is.
- Mount a panel that renders `availability.partialReason` (for example the Reporting tab's `AnswerStatus`) on a document from a no-status body, rendered in memory the way the existing mounted tests render.
- Print the rendered text. It names the reason.

<criterion id="F47-AC9" cell_refs="FE-s-47" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F47-AC9` -- **the whole-suite census of record**, with `IRPT_FE_DEV_PORT` exported to a port you have measured closed. If F41-AC5's control times out under load (FE-s-46's row, not yours), report it and re-run; never edit it.

<criterion id="F47-AC10" cell_refs="FE-s-47" judgment="true" drives="none"/>
`F47-AC10` -- graded at L9: the adapter supplies the reason on the no-status path, the validator is unchanged, and no stated state carries it. RECORD; NO VERDICT.

<expected_criteria>F47-AC1, F47-AC2, F47-AC3, F47-AC4, F47-AC5, F47-AC6, F47-AC7, F47-AC8, F47-AC9, F47-AC10</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **`contracts/adapt.ts` IS YOURS FOR ONE PURPOSE:**
  - the explicit-unknown sites your F47-AC6 census keeps;
  - ONE named constant for the reason, declared once and imported wherever it is used.
  - Nothing else in the file.
- ⛔ **`contracts/validate.ts` IS NOT YOURS AND DOES NOT CHANGE** (the ruling; F47-AC5 reads it).
- ⛔ **NOT YOURS:**
  - `contracts/envelope.ts` (including its stale "ten of the twelve" comment: name it in your result, do not edit it);
  - `contracts/index.ts`, `state/`, `render/`, `tabs/` and every fixture and wire instance.
  - If the reason needs a change there, that is a BLOCKING row.
- ⛔ **THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD** (F47-AC9). The issuer's probe turned 0 tests red with the minimal change. A red test outside your grant is a BLOCKING row with the list, never an edit.
- **The reason's words.** Plain and public:
  - they state that the response carried no status, so its state is unknown;
  - no host, no principal, no internal component, and no code the contract does not name;
  - not a `publicReasonCode`, which is the producer's field, not the portal's.
- **RULING AC.** Every file your tests inspect is read as the committed blob (`git cat-file blob HEAD:<path>`) or the committed tree, or the test says why it reads the working copy.
- **Servers.** No dev server is needed. Export `IRPT_FE_DEV_PORT` on EVERY `bun test` run to a port you have measured closed (5263 is this slot's). A closed loopback port refuses in about 0.3 to 2 s here, so any probe timeout must exceed 2 s. Sibling slots use 5261 and 5265; never touch them.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W3-S<k>`, starting at W3-S36. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-47/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.8 @734eb61ac1, cell `FE-s-47`.
<owned_cells>FE-s-47</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F47-AC1` .. `F47-AC10`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-47.no-status-carries-its-reason.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F47-AC1,F47-AC2,F47-AC3,F47-AC4,F47-AC5,F47-AC6,F47-AC7,F47-AC8,F47-AC9,F47-AC10 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-47.no-status-carries-its-reason.md` BEFORE the `complete` flip. `F47-AC10` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `no-status-carries-its-reason.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round (round-7 analysis, msg 96865, no addendum).
the refusal: RUN by the issuer at portal DEV 1f3ce9f0 -- validate.ts:95-96, a non-READY/LOADING state with neither partialReason nor publicReasonCode is refused.
the explicit-unknown sites: RUN -- EXPLICIT_UNKNOWN_STATE defined adapt.ts:167; into an Availability at adapt.ts:228 (wireEnvelope) and adapt.ts:290 (carryAvailabilityFromStatus, partialReason carried from the document at :292); envelope.ts:233 is IrParsedEnvelope.state, not an Availability.
the status-optional operations: RUN -- contracts/wire/responses.ts:236-249, 11 of 12 false (analysis-requests alone true); envelope.ts:231's comment says ten.
the reason renderers: RUN -- render/Page.tsx:160 reasonText; tabs/reporting/AnswerStatus.tsx:56; render/performance/MethodsAndSources.tsx:173, :242.
the reach: RUN -- the issuer's whole-suite probe (decomp R8.1) with the minimal carry change: 559 pass, 18 skip, 1 fail of 578; the fail is F41-AC5's control timing out (FE-s-46's), so the change turns 0 tests red.
lane: the <paths> block IS the grant; validate.ts, envelope.ts, index.ts, state/, render/, tabs/ and every fixture excluded.
</preflight>

Seating: slot ~3; one wave -- round 8 has no dependency edge, seated on a fresh worktree pair cut from HEAD with the `<status>` flip committed BEFORE the pair is cut (row S26).
