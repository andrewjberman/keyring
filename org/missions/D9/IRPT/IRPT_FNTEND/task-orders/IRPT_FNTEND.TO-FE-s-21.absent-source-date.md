# TO IRPT_FNTEND.TO-FE-s-21 -- an absent source date is a state, not a defect

<to_id>IRPT_FNTEND.TO-FE-s-21</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-12</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F7; CONTRACTS `StatusEnvelope` consumed) | **Decomp cell:** `FE-s-21` (round 3, v0.3 @38f68b965c) | **outcome_ref:** FWD-5 | **depends_on:** `FE-s-19` (shares `state/status.ts` -- never concurrent) | **slot:** ~1, queue position 2 | **rows:** S29

---

## WORKER FACE

### THE CELL

`FE-s-21` -- **F7 renders "source ages", and under the contract as it now stands an envelope may legitimately carry no source date at all.**

`IRPT_BCKEND` PRD v0.14 (@b8e98d5a4d) made `StatusEnvelope.business_date` STATE-CONDITIONAL:

```
  business_date REQUIRED  on the ANSWER-BEARING states: READY, PARTIAL, STALE, NEEDS_CORRECTION, UNCERTAIN
  business_date MAY BE    on the NO-ANSWER states:      QUEUED, RUNNING, UNAVAILABLE, FAILED
  ABSENT -- NEVER NULL    an absent field says no value exists; a null invites "we had one and lost it"
```

`state/status.ts:170`'s `formatSourceAge(sourceAsOf, now)` and the panels that consume it must render those four as **"no source age yet"** -- a STATE the page is reporting, never an error, never a missing-data defect, and never a fabricated age. The cut is a SUBTRACTION from the printed nine-state enum: 9 minus the 5 answer-bearing = the 4 you handle. Do not enumerate forward from the cases you happen to think of.

⛔ **AN ABSENT FIELD AND A NULL ARE DIFFERENT FACTS AND MUST STAY DIFFERENT.** The contract says ABSENT, never null. If a null arrives on a no-answer state that is a contract violation by the producer and it is a surprise row -- not a case to quietly fold into the same rendering.

This cell is SEQUENCED BEHIND `FE-s-19` because you share `state/status.ts` with it. `FE-s-19` may change what fills `availability`; your worktree is cut AFTER its drain, so you build on the state plane as it lands, not as it is today.

### ACCEPTANCE

<criterion id="F21-AC1" cell_refs="FE-s-21"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F21-AC1` -- the whole portal typechecks.

<criterion id="F21-AC2" cell_refs="FE-s-21"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-21/source-age.test.ts</invocation><expect>NO-ANSWER STATES: 4 of 4</expect></criterion>
`F21-AC2` -- QUEUED, RUNNING, UNAVAILABLE and FAILED, each with `business_date` ABSENT, each render "no source age yet". The test prints the state and the rendered string per case.

<criterion id="F21-AC3" cell_refs="FE-s-21"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-21/source-age.test.ts</invocation><expect>ANSWER-BEARING STATES: 5 of 5</expect></criterion>
`F21-AC3` -- **the other half of the subtraction, and the arm that stops "no source age yet" becoming the answer for everything.** READY, PARTIAL, STALE, NEEDS_CORRECTION and UNCERTAIN each carry a `business_date` and each render a real age, not the absent-state string.

<criterion id="F21-AC4" cell_refs="FE-s-21"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-21/source-age.test.ts</invocation><expect>NO ERROR AFFORDANCE: 4 of 4</expect></criterion>
`F21-AC4` -- on all four no-answer states the rendered markup carries no error styling, no missing-data slot and no retry affordance. The test prints the tokens it scanned for and a positive control showing the scan fires on a genuine error state.

<criterion id="F21-AC5" cell_refs="FE-s-21"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-21/source-age.test.ts</invocation><expect>NULL IS NOT ABSENT: distinguished</expect></criterion>
`F21-AC5` -- a `business_date` of `null` on a no-answer state is distinguished from an ABSENT one and does not silently render as "no source age yet"; the test prints what it does instead.

<criterion id="F21-AC6" cell_refs="FE-s-21"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/fe-s-21_reporting_no_source_age_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-21-queued.json --click Reporting --console "Maximum update depth"</invocation><expect>CLICKED: Reporting</expect></criterion>
`F21-AC6` -- the Reporting tab on a QUEUED envelope at 1440, captured on a MOUNTED view (`FE-s-19` is terminal before you are seated, so the body mounts).

<criterion id="F21-AC7" cell_refs="FE-s-21"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>1 fail</expect></criterion>
`F21-AC7` (BAR CORRECTED BY THE ISSUER, row IRPT_FNTEND-S45 -- it read `0 fail` on the same PREDICTION that F19-AC8 carried and that row S41 already corrected there. `F18-AC3`'s capture collision CANNOT clear in round 3: it needs the three Holdings smoke maps to carry distinct `status` members and no round-3 cell holds the fixtures (row S44). The set reads **exactly one** failure and it IS that one; **print the failing test's name**, and if it is anything else or a second appears, that is a BLOCKING row.) -- the whole Investor Reporting set is green. By the time you are seated, `FE-s-19` and `FE-s-20` have drained and both of this cut's known failures are cleared; if a failure remains that is not yours, that is a BLOCKING row naming it.

<criterion id="F21-AC8" cell_refs="FE-s-21" judgment="true"/>
`F21-AC8` -- graded at L9 from the capture: a reader can tell that the page is reporting a state rather than failing to load. RECORD; NO VERDICT.

<expected_criteria>F21-AC1, F21-AC2, F21-AC3, F21-AC4, F21-AC5, F21-AC6, F21-AC7, F21-AC8</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. You hold `state/status.ts` this wave because `FE-s-19` is terminal; do not undo what it landed there. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **No derivation.** You render what the wire carries or you render its absence. Never compute an age from a different field, never fall back to a fetch time, never default to "today".
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal` as in your identity line. Portal commit pathspec: the files you changed under `src/`, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; kill it before your final report. Routes without a leading slash.
- **Fixture maps name the whole page's needs** and are v1 envelopes. File you add: `fe-s-21-queued.json`.
- ⚠ **`ui-smoke.mjs` prints `DID NOT LAND` on every query-bearing route whether or not anything failed** (row `W1-S36`; `FE-s-22` owns the fix). Your F21-AC6 route carries no query string, so it does not apply -- but do not key any bar on that line.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>` continuing the W1 sequence (read the file for the last W1 id -- `FE-s-19` ran on this slot before you and will have minted some). Re-read immediately before minting; never edit an existing row; keep working.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/state/status.ts
portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx
portal/src/pages/InvestorReporting/tabs/reporting/
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-21/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.3 @38f68b965c, cell `FE-s-21`.
<owned_cells>FE-s-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F21-AC1` .. `F21-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-21.absent-source-date.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F21-AC1,F21-AC2,F21-AC3,F21-AC4,F21-AC5,F21-AC6,F21-AC7,F21-AC8` BEFORE the `complete` flip. `F21-AC8` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `absent-source-date.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; the PRD is UNCHANGED this round and this cell is a CELL INPUT routed by 1.0.0_SA_CTO (96062), never a PRD event. The issuer ruled it OUT of round 2 (row S29) because F7 is not among FE-s-18's PRD rows and that grant was layout-only.
contract: RUN -- IRPT_BCKEND PRD v0.14 @b8e98d5a4d; the state partition is a SUBTRACTION from the printed nine-state enum (9 - 5 answer-bearing = 4), which is how the CTO cut it and how this cell must read it.
symbol location: RUN -- formatSourceAge at state/status.ts:170 (comp-find, DEF band, 5 of 357 hits).
lane: the <paths> block IS the grant; state/status.ts is SHARED WITH FE-s-19 and this cell is SEQUENCED BEHIND IT so the surface is never written concurrently.
</preflight>

Seating: slot ~1, queue position 2; seated when `FE-s-19` is terminal and DRAINED, on a fresh worktree pair cut from the post-drain HEAD, with the `<status>` flip committed BEFORE the worktree is cut (row IRPT_FNTEND-S26).
