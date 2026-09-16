# TO LGIC_NAMING.TO-LN-g-1-r5 -- the rule at v1.10: the two held worked cases from the builder, and the adjacency step stated

<to_id>LGIC_NAMING.TO-LN-g-1-r5</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.10 @592ff7a5de (ADMITTED; both halves current) | **Decomp cell:** `LN-g-1` (round 5, decomposition v7.1 section 0f) | **outcome_ref:** FWD-5 | **depends_on:** none -- one of three independent chains | **slot:** ~1, queue position 1

---

## WORKER FACE

### THE CELL

`LN-g-1` -- `GRADING_RULE.md` at `NAMING_SCHEMA.json` v1.10. **You edit ONE file: `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md`.** Three things, from the round-4 analysis s.3 items 1, 3 and 5 (@5a12d0b97c):

1. **The two held worked cases, re-verdicted FROM THE BUILDER (row LGIC_NAMING-S22, RULING R-5).** The rule's `worked_cases` json fence carries two cases the builder disagrees with, and the suite fails on exactly those two. Set each to what `grade()` returns, and say WHY in the rule's own words -- naming the `systems.json` row, R2 and R1.c:

   - `globgrph-serving` / `ECS_TASK_DEFINITION` -> **OUT-OF-PATTERN**, canonical `globgrph-serving-task`
   - `opal-globgrph` / `ECS_CLUSTER` -> **OUT-OF-PATTERN**, canonical `globgrph-cluster`

   Those two forms are `grade()`'s OUTPUT, measured at the cut, never values typed by the issuer (Rule 30). **Verify them yourself before writing** by calling `grade()` on both names at your tree. **If the builder disagrees with this order, THE BUILDER WINS and you file a BLOCKING row.**

2. **The `alias_adjacency` step (A-3, landed in v1.10).** `GRADING_RULE.md` must STATE the step that reads `alias_adjacency` -- the analysis names it **R3** -- as a step line carrying the field or its parent key, and print its coverage as `N of N`. A field the rule does not name is not covered, whatever prose mentions it elsewhere.

3. **State the `registry_hash` decision either way** (analysis item 1): whether the rule pins a registry hash or deliberately does not, with its reason, in one line.

**THE SUITE MUST READ 82 of 82.** Today it reads 2 failed / 80 passed, and both failures are the two cases above.

```
NOT YOURS: lib/opal_naming.py and lib/tests/test_opal_naming.py are NOT in your <paths>.
You re-verdict the RULE to match the BUILDER; you cannot change the builder to match
the rule. That exclusion is this cell's design (decomposition v7.1 section 0f), because
a worker holding both can make them agree by construction.
```

**Read:** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md`; `org/standards/NAMING_SCHEMA.json` (v1.10, the `alias_adjacency` key); `infra/logic/registry/systems.json` (the `globgrph` row); `lib/tests/test_opal_naming.py:25-34` (how the worked cases are read -- `_RULE` points at GRADING_RULE.md and `_worked_cases()` parses its json fence, which is why this is a RULE edit and not a code edit); the round-4 analysis s.3 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND4_20260916.md` @5a12d0b97c).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="G1R5-AC1" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_ln_r5.py g2-suite</invocation><expect>VERDICT: PASS-SUITE-ALL-GREEN</expect></criterion>

<criterion id="G1R5-AC2" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_ln_r5.py g1-adjacency</invocation><expect>VERDICT: PASS-ADJACENCY-STATED</expect></criterion>

<criterion id="G1R5-AC3" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_ln_r5.py g1-forms</invocation><expect>VERDICT: PASS-FORMS-NO-REGRESSION-AT-V110</expect></criterion>

<criterion id="G1R5-AC4" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r5/check_ln_r5.py g2-globgrph</invocation><expect>VERDICT: PASS-GLOBGRPH-FROM-BUILDER</expect></criterion>

<criterion id="G1R5-AC5" cell_refs="LN-g-1" judgment="true"/>

<expected_criteria>G1R5-AC1, G1R5-AC2, G1R5-AC3, G1R5-AC4, G1R5-AC5</expected_criteria>

**G1R5-AC5, for `3.0.0_SA_CVO` at L9 (no verdict from you):** the DISCRIMINATING ARM for item 2 -- show that a doctored field the rule does NOT cover makes the coverage line read `N-1 of N` and FAIL, recorded with BOTH readings. An arm that only ever passes on the true tree proves nothing: six of this seat's own instruments were found reading the wrong object this session, and the checker's docstring names all six. Record both readings in your result file; do not leave the doctored file behind.

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. **`lib/` is NOT yours** -- that exclusion is this cell's design, not an oversight. A path you need that is not named is a BLOCKING surprise row, never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Nothing live moves.** No cell of this round renames a live name, writes to AWS, or runs Terraform. Every `.py` you touch passes `.tools/commit-gate.sh` (safe-commit runs it).
- **Fixed inputs are read-only.** `fixed_inputs/r5/check_ln_r5.py` is round 5's checker, which every criterion calls. Never edit it. If you believe it is wrong, that is a BLOCKING surprise row -- say so rather than working around it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md`, ONE row each, id `LGIC_NAMING-W1-S<k>`. Keep working after filing.
- **The preloaded context.** Every worker starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12). Judge from the files this order names and cite them, never the preloaded text.
- **Numbers** here are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v7.1, cell `LN-g-1`, round 5 (section 0f).
<owned_cells>LN-g-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `G1R5-AC1`, `G1R5-AC2`, `G1R5-AC3`, `G1R5-AC4`, `G1R5-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~1/LGIC_NAMING.TO-LN-g-1-r5.rule-at-v110.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> G1R5-AC1,G1R5-AC2,G1R5-AC3,G1R5-AC4,G1R5-AC5` BEFORE the `complete` flip.
Result file `rule-at-v110.r5.result.md` beside it -- the round is in the name, so no earlier round's result is replaced. **Pin every artifact by the commit that carries it: commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `G1R5-AC5` is a JUDGMENT criterion -- record it `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the recut -- round 5 is the CLOSING round. Gates: G-A DISCHARGED, G-B met at round 1, G-C worker admission checked at spawn. This cell is gated by G-C only; the v1.10 landing gate cleared when L4-R read ADMITTED (both halves current, prd-signoff.py status read at the cut, not assumed).
comp-iam: DECLARED-NOT-APPLICABLE -- measured on this cell's write set: one markdown rule file and the channel. No operation, policy, principal or resource is added.
comp-adversary: DECLARED-NOT-APPLICABLE -- this cell introduces no external citation; the two canonical forms in item 1 are BUILDER OUTPUT measured at the cut and independently re-derived by 1.0.0_SA_CTO in R-20. The order tells the worker to verify them at its own tree and to let the builder win on disagreement, so a stale value in this order cannot become a wrong rule.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). lib/ is deliberately excluded so the rule cannot be made to agree with the builder by editing the builder.
contention: derived from the issued <paths>. LN-g-1 writes GRADING_RULE.md; LN-f-1 writes exercises/r5/f1-gaps.r5.md; LN-f-2 writes exercises/r5/f2-live-fence.r5.md. No two cells share a write surface. Decomposition v7 had LN-g-1 and LN-g-2 BOTH writing GRADING_RULE.md -- measured at the cut by reading lib/tests/test_opal_naming.py:25-31, and removed at v7.1 BEFORE this issuance.
</preflight>

Seating: slot ~1, queue position 1. Round 5 of LGIC_NAMING, the CLOSING round, the recut of `1.0.0_SA_CTO`'s round-4 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND4_20260916.md` @5a12d0b97c, msg 97396); issued by `2.0.0_SA_COO~G`. Decomposition v7.1, section 0f.
