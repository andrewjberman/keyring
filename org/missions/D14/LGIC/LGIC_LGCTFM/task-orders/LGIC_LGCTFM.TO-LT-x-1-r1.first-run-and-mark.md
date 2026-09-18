# TO LGIC_LGCTFM.TO-LT-x-1-r1 -- the first real run on blackdiamond / 49financial, the MARK, and FWD-10's before/after

<to_id>LGIC_LGCTFM.TO-LT-x-1-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-x-1` (decomposition v1.1) | **outcome_ref:** FWD-1, FWD-7, FWD-10 | **depends_on:** LT-e-3, LT-p-1, LT-r-1 and LT-h-1 all drained (the first real run needs the whole instrument)

---

## WORKER FACE

### RE-HAND -- READ THIS FIRST. THIS CELL HAS BEEN RUN ONCE AND THE ISSUER REFUSED ITS OWN COMPLETE FLIP.

**What happened, measured, not summarised.** The first hand ran the engine at 20:25Z and its run directory
`workflows/legacy_transform/blackdiamond-49financial/20260917T202556Z-bb29248/` is in the tree. But `.tools/naming-gate.py`
(ENFORCE mode) refused five of its six JSON artifacts wholesale -- 1719 REFUSE lines -- so only `VINTAGE.json` and the four
`.md` files committed. Ruling **R-35** then exempted a minted run directory, and the four refused files WERE later added --
**by a different cell's commit.** `git log --diff-filter=A` names `a5fca30175` (cell `LT-e-4`) as the ADD commit for
`contract.json`, `plan.json`, `PLANT.json` and `PLANT_UNTYPEABLE.json`, and `git hash-object` shows them BYTE-IDENTICAL to
that amendment's own 23:31Z run `20260917T233115Z-a89fd61` (`contract.json` is `84d4d1e62b` in both, `95b04ca692` in the
flag-on run). The directory's `VINTAGE.json` still declares `run_id 20260917T202556Z-bb29248` at `repo_head bb292483994d`.
`MARK.json` was never committed at all and the worktree that held it is gone, so it exists nowhere on this device.

**So `X1R1-AC1` reads PASS on bytes this cell's run did not produce, and `X1R1-AC2` is not reproducible at all.** That is
filed as `LGIC_LGCTFM-S3` and it is the ISSUER's defect, not the first hand's: the criterion reads the run directory and
never asks who wrote it. **You are not fixing someone's mistake; you are producing the one coherent run the record needs.**

**WHAT YOU DO DIFFERENTLY, and it is the whole point of this hand:**

1. **Mint a FRESH run directory.** Do not touch, move, delete or re-write `20260917T202556Z-bb29248` or either
   `a89fd61` directory. They stay exactly as they are -- the 20:25Z one is the historical record of the refused first run.
   `run_home.py` refuses to overwrite an existing run directory, so a new run mints a new id by construction.
2. **`MARK.json` IS COMMITTED THIS TIME.** R-35 exempts a minted run directory, so the commit that refused 1719 times
   now lands. If it refuses again, that is a BLOCKING row with the gate's own output quoted, never a workaround.
3. **RULING R-40 BINDS THIS CELL** (`1.0.0_SA_CTO`, 2026-09-18, msg 97741, record `SELF_DRIVE_LGIC_RULINGS_20260917.md`
   @`233f5fd5e4`): *a criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH beside
   the run id, and is graded against that hash.* So your run directory also carries **`HASHES.json`**, written at
   production time:
   ```
   {"run_id": "<your run id>", "repo_head": "<git rev-parse HEAD at the run>",
    "produced_at": "<UTC ISO>", "instrument": "git hash-object",
    "files": {"contract.json": "<sha>", "flow.current.md": "<sha>", "flow.desired.md": "<sha>",
              "plan.json": "<sha>", "plan.md": "<sha>", "VINTAGE.json": "<sha>",
              "MARK.json": "<sha>", "FWD10.json": "<sha>"}}
   ```
   Exactly those EIGHT keys, no more and no fewer -- the new arm compares the declared set to the required set in BOTH
   directions, so a manifest that omits a file does not pass either. Hash each file AFTER you finish writing it.
   `HASHES.json` does not hash itself.
4. **A LABEL IS NOT AN IDENTITY.** Anywhere your result doc or proof instance names this run, name it by run id AND by
   the `contract.json` hash from `HASHES.json`. That is what makes a later replacement detectable instead of silently
   satisfying the criterion.

**The 20:25Z directory's provenance is NOT yours to correct** -- it is `LGIC_LGCTFM-S3`'s subject and the issuer's row. Do
not add a note to it, do not amend its `VINTAGE.json`, and do not file a second row about it; it is already filed.

### THE CELL

`LT-x-1` (PRD T10, DEC-9, DEC-13, DEC-15). **You write the run directory under `workflows/legacy_transform/blackdiamond-49financial/` and append MARK rows to the three registries.** You edit no code: an engine defect is a BLOCKING row.

1. **Before.** Read the live plane with `comp-find --corpus aws` (record `nodes_scanned` and the DB's own `built:` line) and the served portal's routes from the served plane (the live CloudFront distribution's behaviours and origins, sorted, hashed to `routes_sha256`).
2. **Run.** `python lib/opal_lgctfm.py run --subject 49financial --run-home-subject blackdiamond-49financial --seed <the 49financial buckets, as the ledger's plane rows name them> --root workflows/legacy_transform` -- the run directory is `workflows/legacy_transform/blackdiamond-49financial/<run-id>/`.
3. **Mark (DEC-9).** Append, under project `ADVI_FIRMBKTS`, only to `infra/logic/registry/remediations.json` (surface kinds `bucket-alias`, `s3-prefix`), `org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json` (served paths, measured with request site) and `infra/logic/registry/scopes.json` (bucket aliases). Record every appended entry in `<run-id>/MARK.json` as `{"marks": [{"file": <one of the three paths>, "project": "ADVI_FIRMBKTS", "entry": <the exact JSON value appended>}]}`. An entry already present is recorded and disclosed, not appended twice. **Commit the marks through `safe-commit` (the naming gate runs), and paste the output of `python lib/opal_naming.py targets` into that commit's message (ruling R-16: a registry edit re-stamps generated views -- the `TARGETS:` line must be in the message).** Do NOT run `generate`.
4. **After.** Re-read both planes; write `<run-id>/FWD10.json`: `{"aws": {"instrument": "comp-find --corpus aws", "before": {"nodes_scanned", "built"}, "after": {"nodes_scanned", "built"}, "delta_outside_run": [<every live node that changed and is not this run's>]}, "served": {"before": {"routes_sha256"}, "after": {"routes_sha256"}}}`.

The run directory holds `contract.json`, `flow.current.md`, `flow.desired.md`, `plan.json`, `plan.md`, `VINTAGE.json`, `MARK.json`, `FWD10.json` and **`HASHES.json`** (the R-40 manifest, above), and its contract validates against `org/standards/LGCTFM_CONTRACT.schema.json`. **The only paths this branch changes** are under `workflows/legacy_transform/`, the three registries, and `org/missions/D14/LGIC/LGIC_LGCTFM/`.

**Read:** `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` DEC-9, DEC-13, DEC-15 and the plane note under the ENDPOINT; `infra/logic/registry/remediations.json` `_about`; `.tools/naming-gate.py` (the DEC-6 matrix); `org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_LGIC_RULINGS_20260916.md` R-16.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="X1R1-AC1" cell_refs="LT-x-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x1-run-dir</invocation><expect>PASS-X1-RUN-DIRECTORY-COMPLETE</expect></criterion>

<criterion id="X1R1-AC2" cell_refs="LT-x-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x1-marks</invocation><expect>PASS-X1-MARK-ROWS-IN-THE-THREE-REGISTRIES</expect></criterion>

<criterion id="X1R1-AC3" cell_refs="LT-x-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x1-fwd10</invocation><expect>PASS-X1-LIVE-PLANE-ZERO-DELTA</expect></criterion>

<criterion id="X1R1-AC4" cell_refs="LT-x-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x1-footprint</invocation><expect>PASS-X1-REPO-FOOTPRINT-BOUNDED</expect></criterion>

<criterion id="X1R1-AC5" cell_refs="LT-x-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x1-r16</invocation><expect>PASS-X1-MARK-COMMIT-PRINTS-TARGETS</expect></criterion>

<criterion id="X1R1-AC6" cell_refs="LT-x-1" judgment="true"/>

<criterion id="X1R1-AC7" cell_refs="LT-x-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x1-hashes</invocation><expect>PASS-X1-RUN-ARTIFACTS-BOUND-TO-THEIR-HASHES</expect></criterion>

<expected_criteria>X1R1-AC1, X1R1-AC2, X1R1-AC3, X1R1-AC4, X1R1-AC5, X1R1-AC6, X1R1-AC7</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **X1R1-AC6, for `3.0.0_SA_CVO` at L9 (no verdict from you):** FWD-10 on the LIVE plane (R-17): the before and after reads were taken with the named instruments at the vintages recorded, and every live change in the window is attributed; FWD-1: the contract lets the 49 Financial migration's opener learn what the pipeline is made of without listing it by hand.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, everything under `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, appended to the last JSON array in the file, id `LGIC_LGCTFM-W<n>-S<k>` (`<n>` your slot; `<k>` ONE ABOVE the highest `LGIC_LGCTFM-W<n>-S` id already present in ANY document under `org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/`). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Nothing live moves (DEC-13).** Every instrument you call is read-only against AWS; the portal is read, never written. No Terraform apply, no AWS write, no deploy, no rename of a live resource.
- **Disk on this box is tight.** Keep scratch small; delete any temporary worktree you create before you report.
- **The MARK rows are ADVI_FIRMBKTS's rows** in files LGIC_ENFORCE and LGIC_NAMING own; append only, never edit or reorder an existing entry.
- **Stop before any act that is not a read or one of the three appends.** A live change you did not cause, seen in the after-read, is recorded in `delta_outside_run` and filed as a row -- never explained away.

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
workflows/legacy_transform/blackdiamond-49financial/
infra/logic/registry/remediations.json
infra/logic/registry/scopes.json
org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-x-1` (sections 3 and 10).
<owned_cells>LT-x-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `X1R1-AC1`, `X1R1-AC2`, `X1R1-AC3`, `X1R1-AC4`, `X1R1-AC5`, `X1R1-AC6`, `X1R1-AC7`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-x-1-r1.first-run-and-mark.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> X1R1-AC1,X1R1-AC2,X1R1-AC3,X1R1-AC4,X1R1-AC5,X1R1-AC6,X1R1-AC7 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-x-1-r1.first-run-and-mark.md` BEFORE the `complete` flip.
**THE INSTANCE AT THIS PATH IS THE FIRST HAND'S AND YOU REPLACE IT WHOLE** -- its `AC1` FAIL and its `AC2` PASS were both
measured against the run directory this hand supersedes, and the issuer's note on `AC2` says so. Every criterion is
re-measured at YOUR run; nothing is carried forward.
Result file `first-run-and-mark.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`X1R1-AC6` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-1 cut: the run READS both trigger APIs (read-only). No schedule is created.
comp-iam: RUN at the round-1 cut: the run READS identity through comp-iam and CloudFront config read-only; no grant moves.
comp-adversary: RUN at the round-1 cut: FWD-10 is the adversarial read -- a before/after on the live plane with its denominator, so 'moves nothing' is measured, never asserted.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: the three registry files are written by no other open order at the cut (LGIC_ENFORCE round 3 writes systems.json and exemptions.json; census of every open order's <paths>). LT-x-3 reuses the subject directory on this slot, after this cell drains.
</preflight>

Seating: slot ~2, level 5. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
