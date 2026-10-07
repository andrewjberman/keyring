# TO NFRA_CTLPLN.TO-CT-d-7 -- round 4 CT-d-7: the round-close registry read -- every resource a round created, against the registry, N of N

<to_id>NFRA_CTLPLN.TO-CT-d-7</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~10</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-d-7` (`decompositions/NFRA_CTLPLN_DECOMP.round4.md`) | **outcome_ref:** FWD-10 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-d-7`, PRD v0.13 C-NAMING, next-issuance cell (a): "one read at each round's close, by the round's COO: every resource the round
created, against `resources.json`, N of N printed, a missing row filed as a row (a read at the drain, not a standing checker)".
C-NAMING clause (3): a new resource's "row lands in `infra/logic/registry/resources.json` in the same commit as its Terraform".
Andrew's word behind it: "everything should be registered as well". You build the read, run it over this project's rounds 2 and 3, and
add the rows it finds missing for THIS project's own resources. You call no AWS API and apply nothing.

**Measured at the cut** (issuer, a text count over `infra/logic/registry/resources.json`, 465 rows): the names
`cloudops-dell-agent-create-policy`, `cloudops-dell-agent-deploy-policy`, `cloudops-dell1-agent-user`, `cloudops-dell-agents-group` and
`agentbus-global-dell1-queue` each occur 0 times. So this project's own Dell resources are unregistered; your read establishes the
full list.

**What exists:** `infra/logic/registry/resources.json` (`_about` describes the row shape; `resources` is the list; a row has at least
`name`, `type`, `system`, `evidence`), the other registry files beside it (`systems.json`, `scopes.json`, `tiers.json`, ...),
`lib/opal_naming.py` (`name()` and its refusals), `.tools/naming-apply-gate.py` and `.tools/naming-gate.py` (read both headers: what
each grades and in which mode). This project's Terraform roots: `infra/aws/terraform/nfra-ctlpln-identity/` (round 2 @002f93bacd,
round 3 through eda2919e6b) and `infra/aws/terraform/nfra-ctlpln-agentbus/` (round 2 @c649197dd0).

**Build:**

1. `org/devices/round_created_resources.py --since <commit> --until <commit> [--root <dir> ...] [--registry <file>]`:
   - For each Terraform root (default: every directory under `infra/aws/terraform/` with a `.tf` file changed in the range; `--root`
     narrows it), list every `resource "<kind>" "<label>"` block that exists at `--until` and did not exist at `--since` (by resource
     address, read from `git show <commit>:<file>`, never from the working tree).
   - For each, resolve its NAME: the literal `name` (or `function_name`, `bucket`, `queue_name`, `table_name`, per kind) when it is a
     literal or resolves from locals and module outputs declared in the same root (the identity root names its resources through the
     `opal_name` module: read how, and resolve those). A resource kind that has no name of its own (an attachment, a membership) is
     `NAMELESS` and is not expected in the registry. A name you cannot resolve is `UNRESOLVED` and counted.
   - For each named resource: `REGISTERED` when a registry row carries that exact `name`, else `MISSING`.
   - Print one line per resource and, LAST, `ROUND-RESOURCES since=<c1> until=<c2> roots=<r> created=<n> nameless=<a> named=<m> registered=<g>/<m> missing=<x> unresolved=<u> ok=<True|False>`
     with `ok=True` only when `x == 0` and `u == 0`.
2. Run it over this project's two roots from the commit BEFORE round 2's first root commit to the trunk HEAD of your worktree
   (`git log --diff-filter=A --format=%H -- <root>/main.tf | tail -1` gives the adding commit; `--since` is its parent). Save the
   output in your deliverables folder as `ROUND_2_3_CREATED_RESOURCES.txt`.
3. Add the MISSING rows for these two roots' resources to `infra/logic/registry/resources.json`, in the shape `_about` gives, each with
   `evidence` naming the `.tf` file, line and commit that declares it, `system` read from the registry's own vocabulary (find the
   system the `cloudops` and `agentbus` name prefixes belong to in `systems.json` / `scopes.json`; if no system fits, do NOT invent
   one: leave that row out, list it in your report and file ONE surprise row -- a missing vocabulary row is the registry owner's to
   add). Keep the file's formatting, ordering convention and line endings; add rows only, change none.
4. `org/devices/test_round_created_resources.py`: cases on a temporary repository and a temporary registry: a root gaining two named
   resources with one registered -> `registered=1/2 missing=1`; an attachment -> `NAMELESS`, not counted as missing; a resource removed
   in the range -> not listed; an unresolvable name -> `unresolved=1 ok=False`; a range with no `.tf` change -> `created=0 ok=True`.
   LAST line `ROUND-RESOURCES-TEST cases=<k>/5 ok=<True|False>`.

### ACCEPTANCE

<criterion id="CT4d7-AC1" cell_refs="CT-d-7"><invocation>python org/devices/test_round_created_resources.py</invocation><expect>ROUND-RESOURCES-TEST cases=5/5 ok=True</expect></criterion>
`CT4d7-AC1` -- the read counts created, nameless, registered and missing resources correctly on stand-ins; the missing and unresolved
arms are its controls.

<criterion id="CT4d7-AC2" cell_refs="CT-d-7"><invocation>python org/devices/round_created_resources.py --since b119ace91b --until HEAD --root infra/aws/terraform/nfra-ctlpln-identity --root infra/aws/terraform/nfra-ctlpln-agentbus</invocation><expect>unresolved=0</expect></criterion>
`CT4d7-AC2` -- the seam probe on the REAL roots and the REAL registry after your rows: every named resource of the two roots resolves.
Record the whole last line; if `missing` is not 0 it is because step 3 left a row out for want of a system, and your report and row
say which. (`b119ace91b` is the round-2 issuance commit, measured at the cut to predate both roots: neither directory exists in its tree.)

<expected_criteria>CT4d7-AC1,CT4d7-AC2</expected_criteria>

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No AWS call, no apply, no edit to any `.tf` file.** In `resources.json` you ADD rows for these two roots only; no row is changed
  or removed, and no other registry file is edited.
- The commit gates run a naming check: if a commit is refused, do not override; record the refusal lines, file a BLOCKING row, stop.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W10-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
org/devices/round_created_resources.py
org/devices/test_round_created_resources.py
infra/logic/registry/resources.json
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: every other file under `infra/logic/registry/`, `lib/opal_naming.py`,
`.tools/naming-apply-gate.py`, `.tools/naming-gate.py`, both Terraform roots and the `opal_name` module they call.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round4.md</decomp_doc> (round 4), cell `CT-d-7`.
<owned_cells>CT-d-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT4d7-AC1, CT4d7-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~10/NFRA_CTLPLN.TO-CT-d-7.round-created-resources-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT4d7-AC1,CT4d7-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines; the per-resource table for rounds 2 and 3 (address, name, class); the rows you added (name, type,
system); every row left out and why; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule (PRD v0.13: a read at the drain, not a standing checker).
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a read that counts an unresolvable name as registered or as absent (UNRESOLVED counted and fails ok); a wrong-domain zero (created is printed, with roots and range, so an empty range is visible); a registry row invented to pass (system read from the registry's vocabulary, never invented; a missing vocabulary row is left out and rowed); another project's rows edited (add-only, these two roots only); BLIND: a resource created outside Terraform (the cloud permits it for a Dell; C-NAMING clause 1 has no gate) -- this read cannot see it.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.13 @4cea56993a ADDENDUM v0.13 C-NAMING, cell (a); Andrew-direct record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_081xZ_LGIC_NAMING_DILIGENCE_AND_REGISTRATION_FOR_EVERY_NEW_RESOURCE.md`;
CTO msg 106067; decomposition round 4. Base dry-run at the cut: CT4d7-AC1 and CT4d7-AC2 base FAIL as expected (neither file exists).
