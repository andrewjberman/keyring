# TO NFRA_TRNSPT.TO-TR-g1 -- registry rows outlook and sharepoint, validated, targets regenerated

<to_id>NFRA_TRNSPT.TO-TR-g1</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~3</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-g-1` (`decompositions/NFRA_TRNSPT_DECOMP.md`) |
**outcome_ref:** FWD-6, FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-g-1`, communications item 1a (PRD section 3): "Registry rows `outlook` and `sharepoint`". C-SOURCES: "`outlook` and
`sharepoint` are NOT registry rows today ... Nothing is written to a path until both rows exist and `lib/opal_naming.py validate`
passes." Measured at the cut: `address('outlook', ...)` raises `ValueError source 'outlook' is not a systems.json key`.

**The file and its precedent (read):** `infra/logic/registry/systems.json`, key `systems`, row shape per its `_about`
(`key, class, long, owner_directive, owner_claim, owner_basis`). The `teams` row (landed 2026-09-29 by the integrator from the
CRO's branch) is the template: `{"key":"teams","class":"VENDOR","long":"microsoft-teams","owner_directive":"D9","owner_claim":"inferred",
"owner_basis":"..."}`. Class rules and refused tokens: `org/standards/NAMING_SCHEMA.json`.

**Build (LOCAL: records and generated files):**
1. Add two rows to `systems.json` in key order beside `teams`: `outlook` (class `VENDOR`, long `microsoft-outlook`, owner D9,
   owner_claim `inferred`, owner_basis citing PRD C-SOURCES `org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md:107` and
   Andrew-direct 2026-09-30 "This should just hit my mailbox daily" in
   `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_03xxZ_TRNSPT_OPEN_CALLS_ANSWERED_TICKET_CENTER_OWN_INGESTION.md`),
   and `sharepoint` (class `VENDOR`, long `microsoft-sharepoint`, owner D9, `inferred`, basis PRD C-SOURCES and the L1 brief
   addendum A1, `docs/briefs/nfra-trnspt-opal-transcript-database-brief-20260929.md`). If `validate` refuses a class or a
   token, the refusal text is your report and a surprise row; never bend the schema.
2. `python lib/opal_naming.py validate` -> exit 0.
3. Regenerate the generated targets at the new registry hash: `python lib/opal_naming.py generate --out .` (the 12 files
   `python lib/opal_naming.py targets` lists; all are in your grant below). Commit every file that changed; hand-edit none.
   Report the list of changed files and, for each, that the diff is the hash/comment line only.
4. `python lib/opal_naming.py targets` after the generate: every target reads in sync.

### ACCEPTANCE

<criterion id="TR1-g1-AC1" cell_refs="TR-g-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_registry_check.py rows</invocation><expect>REGISTRY-OK</expect></criterion>
`TR1-g1-AC1` -- `validate` passes and the builder produces an address for both new sources.

<criterion id="TR1-g1-AC2" cell_refs="TR-g-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R1_CHECKS/r1_registry_check.py targets</invocation><expect>TARGETS-IN-SYNC</expect></criterion>
`TR1-g1-AC2` -- a fresh generate into a temp dir is byte-identical to the committed targets.

<expected_criteria>TR1-g1-AC1,TR1-g1-AC2</expected_criteria>

Dry-run at the base 2026-09-30 14:0xZ-14:4xZ: AC1 REGISTRY-REFUSED (source 'outlook' is not a systems.json key) -- FAIL as
expected. AC2 at the base reads `TARGETS-STALE n=12 moved=[all 12]` -- FAIL as expected, and NOT because of your rows: the
committed targets are stamped `registry@5576b01fd4684bfa` while the registry at HEAD hashes `ffa41913935c3281` (the site Z merge
0146e0c954 landed the `rivalfunds` row d451070fb1 without a laptop regenerate; row `NFRA_TRNSPT-S3`). Your regenerate therefore
restamps all 12 targets for two reasons at once (the pre-existing drift and your two rows); report both. The check regenerates
IN PLACE and asks git; after your commit it reads TARGETS-IN-SYNC.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **Records only (WORLD by the gate's path floor: `infra/logic/` reads as infrastructure; nothing is applied).** No S3, no Terraform, no deploy. The regenerated targets are deployable files whose only change is the
  registry hash line: the issuer names the restamp to the IRPT seats before the drain lands (their signed packets pin blob
  hashes); you do not.
- **The mail bronze cell (TR-b-1) is the next order in your queue** and needs `address('outlook', ...)` to build.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W3-S<k>`), and do not weaken the test to pass.

<paths>
infra/logic/registry/systems.json
data/firm_registry.json
infra/aws/lambda-edge/_shared/firm-config.mjs
data/assets/scripts/gold/investor_reporting/directory_runner.py
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
infra/aws/lambda/investor-reporting/_authz/loaders.py
data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py
.tools/ds-precommit-check.py
data/black_diamond/scripts/bronze/_asset_dim_rest_pin.py
portal/src/pages/InvestorReporting/header/firmDisplayNames.generated.ts
infra/aws/terraform/modules/opal_name/generated_locals.tf
infra/aws/terraform/modules/opal_name/tests/vectors.json
infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The `portal/` target lives in the nested
portal repository: if `generate` writes it, commit it inside `portal/` on your worktree's nested branch and name that commit
in your report; if your worktree carries no portal checkout, that is a surprise row, not a stop.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md</decomp_doc> (round 1), cell `TR-g-1`.
<owned_cells>TR-g-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR1-g1-AC1, TR1-g1-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~3/NFRA_TRNSPT.TO-TR-g1.registry-rows.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR1-g1-AC1,TR1-g1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two rows verbatim, the validate line, the changed-target list with the one-line diff nature, the two check lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- records.
comp-iam: DECLARED-NOT-APPLICABLE -- records; no principal.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the restamp hazard (CTO placement 2026-09-29 step 1) is the issuer's at the drain.
lane: the <paths> block IS the grant; infra/logic/registry/** is PLATFORM_LOGIC_DOCS (CRO base and ~A-~D) -- the worker grant admits the order's paths, and the drain follows the 2026-09-29 precedent (rows prepared on a branch, landed by merge, the restamp named to ~P/~M).
</preflight>

Source: PRD v0.1 C-SOURCES, S02, section 3 communications item 1; decomposition round 1 cell TR-g-1.
