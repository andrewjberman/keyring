# TO LGIC_ENFORCE.TO-EN-s-25-r4 -- the census run to the END on both planes, judged + carded == nameable

<to_id>LGIC_ENFORCE.TO-EN-s-25-r4</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>superseded -- NOT met and NOT flipped to complete. Criteria measured from its own proof instance by 2.0.0_SA_COO~G on 2026-09-19: AC1 PASS, AC2 PASS, AC3 FAIL, AC4 judgment. AC3's FAIL IS LGIC_ENFORCE-W2-S13's ORIGIN -- '1411 of 3237 judged rows carry a literal { in canonical' -- and that population is now owned by ROUND 13's cell EN-p-37, which re-measured it at 1303 of 3264 (registry 9f4a569d7a54b53c, 2026-09-19T07:33:40Z) and attributed it to five producers in two classes. Superseded BY that cell; no work is owed on this order.</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-s-25` = round-4 cell 25 (decomposition v3.3, section 0d) | **outcome_ref:** FWD-5 | **depends_on:** EN-c-23-r4 and EN-h-24-r4 (spawns after that queue drains)

---

## WORKER FACE

### THE CELL

`EN-s-25` -- R-32's cell 25, and the cell FWD-5 closes on. **You write your own deliverables only; you edit no shared file.**

**WHY.** Rounds 1, 2 and 3 each ran `python lib/opal_naming.py census` and each stopped early, because a name the grading rule cannot place raises and the run halts. Round 4's campaign cells (EN-c-23-r4, EN-h-24-r4) closed that population ahead of you: every name on round 3's measured list is now either resolvable by the registry or recorded NOT-JUDGED with an owner card. **Your job is the run those cells made possible, and the run is the outcome.**

1. **RUN IT TO THE END on both planes.**
   `python lib/opal_naming.py census --live --repo --not-judged <the carded file> --report org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/NAMING_CENSUS_REPORT.r4.md`
   The carded file is `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/NOT_JUDGED_R4.json`, the list slot ~1 wrote (plus round 3's `.../0.9.0_WK_LGIC_ENFORCE~4/NOT_JUDGED_S6.r3.json` entries if they are not already in it -- carry both, never drop a carded name). A name in that file is not graded, does not stop the run, and is counted as CARDED.
2. **THE BAR, and it is not "zero carded".** The report's fenced json must read, on BOTH planes:
   `judged_live + carded_live == live_nameable` and `judged_repo + carded_repo == repo`, with every denominator printed, and `stopped` null. **A carded name is a named gap with an owner, which is what FWD-5 promises; a run that stops early is not.** If the run stops on a RAISE that is NOT in the carded file, that is a name the campaign missed: file ONE surprise row naming it, add nothing to the registry yourself (that surface is not yours), and report -- the criterion stays RED and the round answers it.
3. **STATE THE LIVE PLANE'S VINTAGE.** The live plane is read through `comp-find --corpus aws`, whose CloudNode DB carries its own `built:` line. That vintage goes in the report (the `vintage` field already carries the census's own "Built from the estate as of ..." line -- keep it, and state the AWS corpus's `built:` beside it). A live count with no vintage is a number with no clock.
4. **NO PLACEHOLDER reaches a report row** (W2-S10's rule): no row's `canonical` may contain `{`.
5. **WRITE THE COMPARISON** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/NAMING_CENSUS_COMPARISON.r4.md` over the REAL hand populations -- LGIC_NAMING's N2 worked cases (45) and N6 grader rows (88) -- with the same fenced-json shape round 3's comparison used (`census`, `against.N2`, `against.N6`, each with `hand_population`, `compared`, `uncompared_hand_rows`), the census block copied from YOUR report. Every hand row left uncompared carries a stated reason.

**Read:** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~4/NAMING_CENSUS_REPORT.r3.md` and `NAMING_CENSUS_COMPARISON.r3.md` (round 3's shapes, and the numbers you must beat: judged_live 21 + carded 2 of 1828, judged_repo 0 of 1878, `stopped` non-null); `lib/opal_naming.py` (`census`, `census_judge`, `census_report` -- its `--not-judged` handling is already built); slot ~1's `NOT_JUDGED_R4.json` and `OWNER_CARDS_R4.md`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="S25R4-AC1" cell_refs="EN-s-25"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py s25-live-complete</invocation><expect>PASS-S25-LIVE-COMPLETE</expect></criterion>

<criterion id="S25R4-AC2" cell_refs="EN-s-25"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py s25-repo-complete</invocation><expect>PASS-S25-REPO-COMPLETE</expect></criterion>

<criterion id="S25R4-AC3" cell_refs="EN-s-25"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_en_r4.py s25-no-placeholder</invocation><expect>PASS-S25-NO-PLACEHOLDER</expect></criterion>

<criterion id="S25R4-AC4" cell_refs="EN-s-25" judgment="true"/>

<expected_criteria>S25R4-AC1, S25R4-AC2, S25R4-AC3, S25R4-AC4</expected_criteria>

**Measured at the cut, by the issuer, against this tree:** AC1, AC2 and AC3 all read FAIL -- the round-4 report does not exist yet, and the arms say so as a FAIL verdict rather than a traceback. AC1 additionally refuses a run whose `stopped` is non-null and a report with no `built:`/"Built from the estate" vintage; AC3 refuses an EMPTY row set, so the arms cannot be satisfied by pointing them at nothing. **S25R4-AC4, for `3.0.0_SA_CVO` at L9 (no verdict from you):** every hand row the comparison leaves uncompared carries a stated reason, and the live plane's stated vintage is the one the run actually read.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **THE REGISTRY IS NOT YOURS THIS ROUND.** `systems.json`, `resources.json`, `exemptions.json`, `scopes.json` and `remediations.json` are all outside your grant. A RAISE that needs a row is a surprise row naming it, never an edit -- the campaign cells own that surface and the round answers a miss.
- **Fixed inputs are read-only**, everything under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/`, and slot ~1's carded list is READ-ONLY to you as well. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot). **Append at the END of the existing JSON array, keeping every existing row's bytes and indentation.** Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Nothing live moves.** The live plane is READ through `comp-find --corpus aws` only; no AWS write, no Terraform apply, no `generate`.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.3, round-4 cell `EN-s-25` (section 0d).
<owned_cells>EN-s-25</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `S25R4-AC1`, `S25R4-AC2`, `S25R4-AC3`, `S25R4-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-s-25-r4.run-to-the-end.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> S25R4-AC1,S25R4-AC2,S25R4-AC3,S25R4-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-s-25-r4.run-to-the-end.md` BEFORE the `complete` flip.
Result file `run-to-the-end.r4.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`S25R4-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-4 cut. This cell is gated by slot ~1's queue (EN-c-23-r4 then EN-h-24-r4) draining to CLOUD.
comp-iam: DECLARED-NOT-APPLICABLE -- a read-only census; no principal, policy or resource changes.
comp-adversary: RUN -- DENOMINATOR 2 planes (live_nameable and repo, each with its own judged + carded arithmetic) and 3 arms; adversarial shapes covered 4 of 4 (a STOPPED run reading clean: refused on non-null `stopped`; an arithmetic that closes over an incomplete census: refused; a missing live-plane vintage: refused; an EMPTY row set: refused rather than vacuously passing). BLIND to whether the live plane's own corpus was stale when the run read it -- the arm reads the stated `built:` vintage, it cannot re-derive it, which is why the vintage is stated rather than trusted.
lane: the worker's own deliverables folder; the <paths> block adds only the channel. The registry is deliberately OUT of this cell's grant.
contention: no other round-4 cell writes this worker's folder; disjoint from LGIC_LGCTFM round 1 entirely.
</preflight>

Seating: slot ~2, queue position 1. Round 4 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-3 analysis @`969f89b0e7`; issued by `2.0.0_SA_COO~G`. Decomposition v3.3, section 0d. Rulings carried: R-32, R-29 (the carded-counts-toward-done bar), W2-S10, A-4.
