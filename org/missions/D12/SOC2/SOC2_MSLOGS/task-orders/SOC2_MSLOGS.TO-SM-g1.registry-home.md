# TO SOC2_MSLOGS.TO-SM-g1 -- the registry home: m365-metadata owned by D12, the X18 departure retired, targets regenerated

<to_id>SOC2_MSLOGS.TO-SM-g1</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.9.0_WK_SOC2_MSLOGS~4</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Risk note:** WORLD only by the gate's path floor (an infrastructure path is in `<paths>`); the cell calls nothing live.

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-g-1` (`decompositions/SOC2_MSLOGS_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SM-g-1`. The naming registry (`infra/logic/registry/`, built by `lib/opal_naming.py`) has a SOURCE row `m365-metadata` that still names the closed Ticket Center project as its owner, and the
conformance ledger row X18 records a departure that is now retired. Make two record edits and regenerate. READ first: `infra/logic/registry/systems.json` (the row with `"key": "m365-metadata"`),
`infra/logic/06_CONFORMANCE_LEDGER.md` (the line starting `| X18 |`), PRD `org/missions/D12/SOC2/SOC2_MSLOGS/prd/SOC2_MSLOGS_PRD.md` rows C-HOMES and C-RAW. Andrew-direct words you cite, VERBATIM:
"I want this all under a new macro called SOC2_MSLOGS" (2026-10-16 ~16:1xZ) and "everything should be in the trino audit bucket ... Silver is just formatted bronze in parquet for query" (same message);
record `org/tier1_exec/2.0.0_SA_COO~S1/ANDREW_DIRECT_20261016_1559Z_REFRAME_M365_LOGS_AS_SOC2_COMPROMISE_EXPOSURE_MACRO_SOC2_MSLOGS.md`. No network, no AWS.

### THE EDITS

1. **`systems.json`, the `m365-metadata` row:** set `"owner_directive": "D12"`; rewrite `owner_basis` so it states the project SOC2_MSLOGS (`org/missions/D12/SOC2/SOC2_MSLOGS/project.json`, a D12 mission-tree project)
   and cites the Andrew-direct record above; keep `owner_claim` `measured`; the text names no Ticket Center project except as "formerly" at most once. Change nothing else in the file.
2. **`06_CONFORMANCE_LEDGER.md`, the X18 row:** keep the row and the table shape. Departure (1) (bronze held only eight accounts after field levers, not the raw blob) is RETIRED: say so in the row,
   citing SOC2_MSLOGS and Andrew's words VERBATIM: "if any opal user is hacked, we want to be able to know the exposure" (Andrew-direct 2026-10-16 ~16:1xZ, same record), and that bronze for source `m365-metadata` is now the
   raw audit pull of every account (the table `audit_records`). Departure (2) (the KMS key alias `alias/opal-data-trino`) is UNCHANGED and still in force. Keep the acknowledger statement for (2).
3. **Regenerate the generated targets:** `python lib/opal_naming.py generate --out <a scratch directory outside the repository>` then copy into the repository ONLY the generated files whose bytes differ from the
   committed ones among the sixteen listed in `<paths>` (the portal targets are not yours: do not copy anything under `portal/`). Never edit a generated file by hand.

Hard limits: ASCII only in anything you write; change no other row of any file; no other file.

### ACCEPTANCE

<criterion id="SM1-g1-AC1" cell_refs="SM-g-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_g1.py rows</invocation><expect>G1-ROWS-OK</expect></criterion>
`SM1-g1-AC1` -- the registry validates, the `m365-metadata` row is owned by D12 citing SOC2_MSLOGS, the `audit_records` address resolves to the ruled key, and every non-portal generated target matches a fresh generation.

<criterion id="SM1-g1-AC2" cell_refs="SM-g-1"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R1_CHECKS/s1_check_g1.py ledger</invocation><expect>G1-LEDGER-OK</expect></criterion>
`SM1-g1-AC2` -- the X18 row says departure (1) is retired by SOC2_MSLOGS on Andrew's word for a raw audit pull, and departure (2) for the KMS alias still stands.

<expected_criteria>SM1-g1-AC1,SM1-g1-AC2</expected_criteria>

Dry-run at the base 2026-10-16 ~17:0xZ: AC1 `G1-ROWS-REFUSED owner_directive is 'D7', not D12; owner_basis does not cite SOC2_MSLOGS; targets stale n=3 ...`, AC2 `G1-LEDGER-REFUSED X18 lacks ['SOC2_MSLOGS', 'retired', 'raw audit pull']` -- each FAIL as expected.
Run each from the repository (worktree) root. The three stale targets at base differ from a fresh generation by their registry-hash stamp only; regenerating after your row edit refreshes every stamp.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **LOCAL; NOTHING is called live.** The registry and ledger are records; no AWS call, no network.
- **Refusal clause.** If a criterion cannot be met as written (for example `validate` refuses after your edit), stop, write the reason in your report and a surprise row (id `SOC2_MSLOGS-D1-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing,
  in the investigation file below), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_SOC2_MSLOGS~4 <0.9.0_WK_SOC2_MSLOGS~4@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
infra/logic/registry/systems.json
infra/logic/06_CONFORMANCE_LEDGER.md
.tools/ds-precommit-check.py
data/firm_registry.json
data/assets/scripts/gold/investor_reporting/directory_runner.py
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py
data/black_diamond/scripts/bronze/_asset_dim_rest_pin.py
data/black_diamond/scripts/gold/lib/platinum_dest_view.py
data/mdpf/config/bronze_homes.json
infra/aws/lambda/exec-summary-generator/platinum_dest_view.py
infra/aws/lambda/investor-reporting/_authz/loaders.py
infra/aws/lambda/portal_data_proxy/firm_page_access.py
infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/platinum_dest_view.py
infra/aws/lambda-edge/_shared/firm-config.mjs
infra/aws/terraform/modules/opal_name/generated_locals.tf
infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl
infra/aws/terraform/modules/opal_name/tests/vectors.json
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP.md</decomp_doc> (round 1), cell `SM-g-1`.
<owned_cells>SM-g-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SM1-g1-AC1, SM1-g1-AC2. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.9.0_WK_SOC2_MSLOGS~4/SOC2_MSLOGS.TO-SM-g1.registry-home.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SM1-g1-AC1,SM1-g1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two check lines, the list of generated files you copied (and the count that already matched), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- records only.
lane: the <paths> block IS the grant; the registry and ledger are the LGIC owner's surfaces, granted to this order by the issuer (decomposition ruling, PRD C-HOMES).
</preflight>

Source: PRD v0.2 C-HOMES, C-RAW; CLAUDE.md rule 30 (R20 departures are ledger entries); decomposition round 1 cell SM-g-1.
