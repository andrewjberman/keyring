# TO POSN_ASTTAX.TO-V3-1 -- APPLY the round-4 preserve-don't-clobber patch to `seed_canonical_securities.py`, so a routine re-seed can no longer revert the retag; prove it on a scratch copy, never the live table (AT5-s-3, B3; FWD-5 durability)

<to_id>POSN_ASTTAX.TO-V3-1</to_id>
<project>POSN_ASTTAX</project>
<issued_to>0.9.0_WK_POSN_ASTTAX~21</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-14</issued_date>
<status>staged</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.7** @`99cc431075`
(C-CUTS: only the seeder guard stays) - **Decomp cell:** `AT5-s-3` - **Issuance:** round 5, wave 1. **GATES `AT5-s-8` (R1).**

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_ASTTAX~21`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_ASTTAX~21;`. First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`. Commit only via
`bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_ASTTAX~21 <0.9.0_WK_POSN_ASTTAX~21@opal.agent>" -F <msgfile> -- <paths>`,
msgfile by the Write tool, PURE ASCII. Never push, merge, rebase, `checkout --`, `clean`.

## THE CELL

Round 4's `TO-U3-1` (`0.9.0_WK_POSN_ASTTAX~16`) measured that ONE re-seed of
`data/black_diamond/scripts/classification/seed_canonical_securities.py` reverts **4 of 4** carried five-class members
(VXX/UVXY Structured->equity, QBER Structured->fixed_income, PDBC Commodities->equity), wrote the fix as a unified diff, and did
NOT apply it (its grant did not include the file). The diff is
`org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~16/u3_proposed_patch.diff` (+57/-2); its hand-off note is
`u3_ac2_handoff.md` beside it; `git apply --check` read rc=0 at HEAD on 2026-09-14 ~17:4xZ. The mechanism is the SIBLING writer's
(`infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py` `merge_item():72-120`): a pre-read of the live row,
per-field disagreement returned as a CONFLICT, the run REFUSING with rc=1, `--force` the only way past. A FIRST MINT still mints.

**Your grant is the file itself.** `.owned-paths.yaml:1730` grants `data/black_diamond/**` to lane POD4; the worker grant is
ADDITIVE (`owned-paths-validate.py:112-147`, self-test `:458-459`): you are admitted to exactly the paths this order names. You
apply the patch, gate it, prove it on a SCRATCH copy of the table, and commit. **NEVER run the seeder against the live table:
`--upload` is never passed in this cell.**

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route.

## SURPRISE ROWS

ONE row per off-cell finding, `POSN_ASTTAX-Z-W21-S<k>`, appended to
`org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md`; keep working.

## CRITERIA -- structured, one clause each

<criterion id="V3-AC1" cell_refs="AT5-s-3"><invocation>timeout 60 git apply --check org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~16/u3_proposed_patch.diff</invocation><expect>rc=0, then `git apply` of the same diff, then `git diff --stat -- data/black_diamond/scripts/classification/seed_canonical_securities.py` reading +57/-2 (or the exact figure the patch carries -- print it). NEGATIVE CONTROL: the same diff with one context line corrupted is REFUSED by `git apply --check`.</expect></criterion> `V3-AC1` -- THE PATCH APPLIES, AND THE CHECK DISCRIMINATES.

<criterion id="V3-AC2" cell_refs="AT5-s-3"><invocation>timeout 180 bash .tools/commit-gate.sh</invocation><expect>clean on the CHANGED file data/black_diamond/scripts/classification/seed_canonical_securities.py (py_compile + ds-precommit + ruff py39), output cited; the criterion's subject is that changed .py and nothing else (C-S93). Both ASCII limbs read and named.</expect></criterion> `V3-AC2` -- THE GATE ON THE CHANGED .PY.

<criterion id="V3-AC3" cell_refs="AT5-s-3"><invocation>timeout 60 python -c "import sys; p='data/black_diamond/scripts/classification/seed_canonical_securities.py'; b=open(p,'rb').read(); print(p, len(b)-len(b.decode('utf-8')))"</invocation><expect>prints the path and 0 (pure ASCII). FIRING CONTROL, REQUIRED (C-S92): the same expression on a file known to carry non-ASCII (e.g. CLAUDE.md) prints a number greater than 0 -- an instrument that reads 0 on everything is not an instrument.</expect></criterion> `V3-AC3` -- ASCII, BY AN INSTRUMENT THAT SELECTS THE FILE AND CAN FIRE.

<criterion id="V3-AC4" cell_refs="AT5-s-3"><invocation>timeout 600 python <U3_MUTANT_CONTROL_RE></invocation><expect>a row seeded with a five-class value SURVIVES the re-seed (REFUSED rc=1, printed as [PRESERVED] with table-wins), AND a record absent from the scratch copy is still MINTED by the same run (the positive control -- a script that refuses everything would pass the first half and be worthless). Name the scratch target so a reader sees the live table was never opened for write.</expect></criterion> `V3-AC4` -- THE GUARD FIRES AND THE FIRST MINT STILL MINTS.

<criterion id="V3-AC5" cell_refs="AT5-s-3"><invocation>timeout 600 python <SAME_EXERCISE_PRE_PATCH> or the U3 scratch), same input&gt;</invocation><expect>the pre-patch script REVERTS the five-class value on the same input -- the two arms DIFFER. If both arms read the same, the control is not discriminating: report that, not the result.</expect></criterion> `V3-AC5` -- THE NEGATIVE ARM: THE OLD SCRIPT STILL CLOBBERS.

<criterion id="V3-AC6" cell_refs="AT5-s-3"><invocation>timeout 180 .tools/aws dynamodb scan --table-name etf-classifications --filter-expression "ticker IN (:a,:b,:c,:d)" --expression-attribute-values '{":a":{"S":"VXX"},":b":{"S":"UVXY"},":c":{"S":"QBER"},":d":{"S":"PDBC"}}' --projection-expression "ticker, asset_class, sub_asset_class" --no-paginate --output json</invocation><expect>Count 4 with ScannedCount printed, and the four rows' values IDENTICAL to a read of the same command taken BEFORE V3-AC4 ran (paste both) -- the live table did not move during this cell.</expect></criterion> `V3-AC6` -- THE LIVE TABLE, UNTOUCHED, PROVED BY A BEFORE/AFTER READ.

<criterion id="V3-AC7" cell_refs="AT5-s-3" judgment="true"><invocation>JUDGMENT -- no invocation; graded at L9</invocation><expect>Whether the guard as applied would refuse a re-seed that changes ONLY sub_asset_class or name (the YANG_OWNED_FIELDS tuple) -- i.e. whether the fields the guard owns are the fields R1 writes. Record the readings and offer NO verdict.</expect></criterion> `V3-AC7` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9.**

<expected_criteria>V3-AC1, V3-AC2, V3-AC3, V3-AC4, V3-AC5, V3-AC6, V3-AC7</expected_criteria>

<placeholders>SAME_EXERCISE_PRE_PATCH, U3_MUTANT_CONTROL_RE</placeholders>

<paths>
org/missions/D4/POSN/POSN_ASTTAX/task-orders/POSN_ASTTAX.TO-V3-1.apply-the-seeder-guard.md
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~21/
org/missions/D4/POSN/POSN_ASTTAX/surprise-channel/investigations/INVESTIGATION_v1.md
data/black_diamond/scripts/classification/seed_canonical_securities.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_ASTTAX/decompositions/POSN_ASTTAX_DECOMP_round5.md</decomp_doc> round 5, cell `AT5-s-3`.
<owned_cells>AT5-s-3</owned_cells>
Read-dependencies, NOT claimed: round 4's `AT4-s-3` (TO-U3-1) produced the patch and both controls -- READ them, do not re-derive
the measurement. DOWNSTREAM: `AT5-s-8` (R1) runs your guarded seeder's dry run after the retag and expects 0 PRESERVED.
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no job, schedule, monitor or deploy is built or changed; a repository .py edit.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or Terraform touched; the live table is READ (two scans) and never written.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) the issuer verified `git apply --check` rc=0 at HEAD on
2026-09-14 ~17:4xZ but not on your worktree's HEAD -- V3-AC1 is the read that binds; (2) the issuer has NOT run the U3 mutant
control since 2026-09-13 -- V3-AC4/AC5 are its first re-run on the applied file; (3) the fields the guard owns vs the fields R1
writes is the judgment in V3-AC7, unread by the issuer.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_ASTTAX/deliverables/0.9.0_WK_POSN_ASTTAX~21/POSN_ASTTAX.TO-V3-1.apply-the-seeder-guard.proof_of_spec.json
</proof_of_spec>
