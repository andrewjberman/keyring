# TO LGIC_ENFORCE.TO-EN-c-28-r5 -- the placeholder campaign: 1411 rows judged against a string no resource can equal

<to_id>LGIC_ENFORCE.TO-EN-c-28-r5</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-18</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves current) | **Decomp cell:** `EN-c-28` (decomposition v3.4 s.0e) | **outcome_ref:** FWD-5 | **depends_on:** `EN-h-29-r5` and `EN-c-31-r5` drained -- your census must read a registry whose known-defective bytes have already been repaired

---

## WORKER FACE

### THE CELL

`EN-c-28` (ruling **R-38**). **This is the cell FWD-5 has been waiting four rounds for, and it is a CAMPAIGN, not a
run.** Round 4's census reached the end of both planes for the first time -- and the same run showed that **1411 of
3237 judged rows carry a literal `{system}` / `{scope}` / `{cadence}` placeholder in `canonical`**. Forty-four percent
of the judged population was graded against a template no resource can ever equal. **The bar is `judged + carded ==
nameable`, and its whole point is that a JUDGED row carries a NAME.**

**FOUR ACTS, in order.**

1. **MEASURE YOUR OWN START POPULATION.** Parse
   `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/NAMING_CENSUS_REPORT.r4.md` -- ONE json
   fence, a dict whose `rows` list holds 3237 dicts of `{current, canonical, verdict, type, plane}` -- and count the
   rows whose `canonical` carries a literal `{`. **Do not take 1411 from this order.** The arm `c28-population`
   refuses a declared start that disagrees with a fresh parse, and it exists because an inherited count is a subset
   measurement until you ask what population it enumerated.
2. **RESOLVE what can be measured.** For every row whose `{system}` / `{scope}` / `{cadence}` substitution can be
   MEASURED from a declared source -- `lambda-source-map.json`'s `source_dir`/`tf_file`, `EC2_MANIFEST.json`'s
   `source_path`, the Terraform tree that declares it -- resolve it, with `owner_claim: inferred` and the citation as
   `owner_basis`.
3. **CARD the rest, with owner and reason.** A carded row is a NAMED GAP WITH AN OWNER, which is what the outcome
   promises. Every carded entry carries an `owner` and a `reason` or the arm refuses it. **"Zero carded" was never the
   bar and is not the bar now.**
4. **RE-RUN THE CENSUS and re-grade.** Write `NAMING_CENSUS_REPORT.r5.md` in YOUR OWN deliverables folder, in the same
   shape as the r4 report (one json fence, `rows` plus its `denominators`, `vintage` and `stopped`). The arm
   `c28-ac3` then re-runs round 4's AC3 against the closed population: a row still carrying a brace is admitted ONLY
   if your campaign carded it.

**YOUR CAMPAIGN RECORD** is `PLACEHOLDER_CAMPAIGN_R5.json` in your own deliverables folder:

```
{"resolved": [ {"current": "...", ...}, ... ],
 "carded":   [ {"current": "...", "owner": "<serial or directive>", "reason": "<why>"}, ... ],
 "denominators": {"population_at_start": <int>, "population_at_close": <int>,
                  "instrument": "<how you counted, both times>"},
 "denominator_delta_note": "<required ONLY if the two populations differ>",
 "stopped_on_timebox": <bool>,
 "delta_riding_next_round": {"count": <int>, "owner": "2.0.0_SA_COO~G"}   <- required only if you stopped
}
```

**THE TWO BOUNDS THAT ARE RULINGS, not guidance:**

- **R-29's FENCE GUARD, verbatim: a row whose mint would change a GENERATED POLICY on an APPLIED resource is NOT
  minted** -- it is carded **BLOCKING** for never-widen sign-off (`1.0.0_SA_CTO` + `2.0.0_SA_COO`).
  `infra/logic/registry/exemptions.json` is the applied fence's registry source, so a row THERE is exactly the mint
  the guard forbids. The arm `c28-fence` requires that file byte-identical to the pinned base, and an unreadable
  baseline is a FAIL -- a guard that cannot read its own baseline certifies nothing.
- **R-33's TIMEBOX: past your start population + 25 MEASURED resolutions, STOP, file the delta, and let the remainder
  ride round 6.** Stopping is not failing. The arm grades BOTH branches: over the bar without stopping FAILS, and
  stopping without a well-formed delta record FAILS too.

**THE DENOMINATOR MOVES UNDER YOU AND THAT IS EXPECTED.** 1411 is a count at ONE VINTAGE of a report this campaign
replaces; a row can leave the placeholder class while you work. So you print `population_at_start` AND
`population_at_close` with the instrument named, and if they differ you say why in `denominator_delta_note`. **A
record that carries only one number reads as measured while being inherited.**

**DO NOT:** run `generate`; add a row to `exemptions.json`; touch `NAMING_CENSUS_REPORT.r4.md` or
`NAMING_CENSUS_COMPARISON.r4.md` (they are `0.9.0_WK_LGIC_ENFORCE~2`'s and the lane gate will refuse you); or mint
`security` (R-39 -- and `EN-c-31-r5`, ahead of you in this queue, has already carded it as `TOKEN_COLLISION`).

**Read:** the r4 census report's fence; `infra/logic/registry/` `_about` blocks; decomposition v3.4 s.0e; rows
`LGIC_ENFORCE-W2-S13` and `LGIC_ENFORCE-W1-S29` on the project's investigation channel; ruling R-29's text in the
round-4 section of the decomposition.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="C28R5-AC1" cell_refs="EN-c-28"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py c28-population</invocation><expect>PASS-C28-START-POPULATION-MEASURED</expect></criterion>

<criterion id="C28R5-AC2" cell_refs="EN-c-28"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py c28-covered</invocation><expect>PASS-C28-EVERY-PLACEHOLDER-ROW-RESOLVED-OR-CARDED</expect></criterion>

<criterion id="C28R5-AC3" cell_refs="EN-c-28"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py c28-redenominator</invocation><expect>PASS-C28-DENOMINATOR-RE-MEASURED-AT-WRITE-TIME</expect></criterion>

<criterion id="C28R5-AC4" cell_refs="EN-c-28"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py c28-fence</invocation><expect>PASS-C28-APPLIED-FENCE-UNCHANGED</expect></criterion>

<criterion id="C28R5-AC5" cell_refs="EN-c-28"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py c28-timebox</invocation><expect>PASS-C28-R33-TIMEBOX-RESPECTED</expect></criterion>

<criterion id="C28R5-AC6" cell_refs="EN-c-28"><invocation>cd <WS> && timeout 600 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_en_r5.py c28-ac3</invocation><expect>PASS-C28-NO-JUDGED-ROW-GRADED-AGAINST-A-TEMPLATE</expect></criterion>

<criterion id="C28R5-AC7" cell_refs="EN-c-28" judgment="true"/>

<expected_criteria>C28R5-AC1, C28R5-AC2, C28R5-AC3, C28R5-AC4, C28R5-AC5, C28R5-AC6, C28R5-AC7</expected_criteria>

**AT THE CUT:** AC1, AC2, AC3, AC5 and AC6 read **FAIL** (their inputs do not exist yet). **AC4 reads PASS and is a
GUARD, not a target** -- the applied fence must STAY unchanged, so that arm refuses your work only if you touch it.

**`C28R5-AC7`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether a RESOLVED row's substitution was genuinely
MEASURED from a declared source rather than inferred from the token's shape, sampled across the resolution kinds; and
whether the carded rows' reasons are the kind a later census can act on.

`<WS>` is your worktree's absolute path. Every invocation runs from your worktree root.

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row, never an override.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only.** If an arm is wrong, file a BLOCKING row naming the arm and the evidence -- round 4's campaign arm WAS wrong and a worker filing a row is how it was found.
- **Surprises** go to the project's `INVESTIGATION_v1.md` as ONE row each, appended to the last JSON array, id `LGIC_ENFORCE-W<n>-S<k>` with `<k>` one above the highest already present in ANY document under that channel. Keep working after filing.
- **Judge from the files this order names and cite them** (`path:line @commit`).
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values.** Re-measure at your own tree -- that is AC1.
- **Commit before you grade.** The checker reads the tree it runs in.
- **Nothing live moves.** Every AWS read is read-only through the `.tools/aws` shim. No apply, no write, no deploy, no rename.
- **Disk on this box is tight.** Keep scratch small; delete any temporary worktree you create before you report.

<paths>
infra/logic/registry/systems.json
infra/logic/registry/resources.json
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.4, round-5 cell `EN-c-28` (section 0e).
<owned_cells>EN-c-28</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `C28R5-AC1` through `C28R5-AC7`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-c-28-r5.placeholder-campaign.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> C28R5-AC1,C28R5-AC2,C28R5-AC3,C28R5-AC4,C28R5-AC5,C28R5-AC6,C28R5-AC7 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-c-28-r5.placeholder-campaign.md` BEFORE the `complete` flip.
Result file `placeholder-campaign.r5.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`C28R5-AC7` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape, and print both denominators in it.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-5 cut: the campaign reads declared sources and creates no schedule.
comp-iam: RUN at the round-5 cut: no grant moves. The fence guard exists precisely because a mint COULD change a generated policy on an applied resource, and that case is carded BLOCKING rather than minted.
comp-adversary: RUN at the round-5 cut: the denominator is the adversarial read -- the cell measures its own start rather than inheriting one, re-measures at write time, and prints both, so "the population" is measured twice by construction rather than asserted once.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: systems.json and resources.json are written by no other open order in either LGIC project at the cut, EXCEPT EN-h-29-r5 earlier in THIS SAME QUEUE (resources.json), which is why this cell is third. LGIC_LGCTFM's open LT-x-1 writes scopes.json and remediations.json, disjoint from both. No round-5 cell runs `generate`, so the two opal_name test fixtures stay at their round-3 stamp -- an ISSUER act after both this cell and LT-x-1 drain, recorded in the decomposition so it is not later discovered as drift.
</preflight>

Seating: slot ~1, level 2, THIRD and last of the queue (`EN-h-29-r5` -> `EN-c-31-r5` -> `EN-c-28-r5`). Round 5 of LGIC_ENFORCE, issued by `2.0.0_SA_COO~G` on decomposition v3.4 s.0e, from `1.0.0_SA_CTO`'s round-4 analysis @`b74ffb43ae`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/` (`check_en_r5.py`, `R5_BASE.json` pinning `95fb561677`). Rulings carried: R-38, R-29, R-33, R-39, R-40.
