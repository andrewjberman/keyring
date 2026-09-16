# TO LGIC_ENFORCE.TO-EN-t-8-r3 -- the roots census, evaluated: one root re-planned to its EXTRACT, init flags per root, causes kept

<to_id>LGIC_ENFORCE.TO-EN-t-8-r3</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-16</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.3 (ADMITTED; both halves current) | **Decomp cell:** `EN-t-8` = round-3 cell 8 (decomposition v3.2, section 0c) | **outcome_ref:** FWD-4, FWD-5 | **depends_on:** EN-i-3-r3 (same slot, runs after it)

---

## WORKER FACE

### THE CELL

`EN-t-8` -- the round-2 roots census, evaluated (A-12). The round-2 census is `LIMB_ROOTS_CENSUS.md` (72 roots: 68 planned, 4 NOT planned, each with a recorded plan rc=1 cause); each row's `plan_sha256` is the SHA-256 of the FULL `terraform show -json` document, which was never committed.

**READ THIS BEFORE YOU PLAN ANYTHING (row LGIC_ENFORCE-S59).** Every full plan document carries its own creation `timestamp`, so **no re-plan can reproduce a `plan_sha256`** -- a perfect reproduction would differ. What a re-plan CAN reproduce is the committed EXTRACT (`resource_changes`), which carries no timestamp. That is the bar.

1. **Re-plan ONE planned root** in a throwaway clone, with `terraform init` flags you record and `terraform plan -lockfile=readonly`, then `terraform show -json`. Write the full document to your folder and a record `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/ROOTS_REPRODUCTION.r3.json`: `{"root": ..., "command": "<the exact plan command>", "full_plan": "<repo path of the full document>", "census_path": "<where the round-2 census now lives>"}`. The round-2 census may have MOVED into `0.9.0_WK_LGIC_ENFORCE~3/` if the placement cell has drained; `census_path` tells the checker where.
2. **Write the round-3 census** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/LIMB_ROOTS_CENSUS.r3.md` with the same fenced-json shape as round 2's, every root row now carrying `init_flags`, and every NOT planned root keeping its cause.
3. **Disk (S22): one root at a time.** One initialised root costs about 686 MB of AWS provider here. Remove that root's `.terraform` as soon as its `show -json` is captured, so the footprint stays about one root, never 72.
4. A root that cannot init without fetching a provider from outside Opal infrastructure, or cannot plan, is recorded NOT planned with its reason. **Never fetch off-box.**

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="T8R3-AC1" cell_refs="EN-t-8"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py t8-replan-reproduces-extract org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/ROOTS_REPRODUCTION.r3.json</invocation><expect>PASS-T8-EXTRACT-REPRODUCED</expect></criterion>

<criterion id="T8R3-AC2" cell_refs="EN-t-8"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py t8-init-flags org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LIMB_ROOTS_CENSUS.r3.md</invocation><expect>PASS-T8-INIT-FLAGS-PRINTED</expect></criterion>

<criterion id="T8R3-AC3" cell_refs="EN-t-8"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py regress-t8-unplanned-have-cause org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LIMB_ROOTS_CENSUS.r3.md</invocation><expect>PASS-T8R-UNPLANNED-ROOTS-CARRY-CAUSE</expect></criterion>

<criterion id="T8R3-AC4" cell_refs="EN-t-8" judgment="true"/>

<expected_criteria>T8R3-AC1, T8R3-AC2, T8R3-AC3, T8R3-AC4</expected_criteria>

**AC1 and AC2 read RED at the cut** (no round-3 files). AC1 compares your re-plan's `resource_changes` canonically to the committed round-2 extract for that root, requires `-lockfile=readonly` in the recorded command, and requires the full document's own `timestamp` to be AFTER the round-2 census vintage -- so a copied old document cannot stand in for a run. **AC3 must PASS on your round-3 census.** **T8R3-AC4, for `3.0.0_SA_CVO` at L9:** the per-root cleanup held the footprint at about one root, and any patch you applied to a root tolerated CRLF line endings.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, including `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_en_r3.py`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **A value that must be read from the estate is read with the instrument this order names**, and its denominator is printed beside it.
- **Nothing live moves.** `plan` only, read-only lockfile, never `apply`; no state migration.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.2, round-3 cell 8 (section 0c; the v3.1 and v3.2 amendments).
<owned_cells>EN-t-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `T8R3-AC1`, `T8R3-AC2`, `T8R3-AC3`, `T8R3-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-t-8-r3.roots-evaluated.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> T8R3-AC1,T8R3-AC2,T8R3-AC3,T8R3-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-t-8-r3.roots-evaluated.md` BEFORE the `complete` flip.
Result file `roots-evaluated.r3.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`T8R3-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-3 cut. This cell is gated by G-C and by EN-i-3-r3's drain (same slot).
comp-iam: DECLARED-NOT-APPLICABLE -- read-only plans against existing backends; no principal, policy or resource changes.
comp-adversary: RUN -- the reproduction is the adversarial surface: AC1 rejects a document older than the census and a missing -lockfile=readonly.
lane: the worker's own deliverables folder; the <paths> block adds only the channel.
contention: the worker's own folder; no other round-3 cell writes it.
</preflight>

Seating: slot ~3, queue position 2. Round 3 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND2_20260916.md`); issued by `2.0.0_SA_COO~G`. Decomposition v3.2, section 0c. Rulings carried: A-12, T3R-J1, T3R-AC2, S22, S59.
