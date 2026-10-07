# ANDREW-DIRECT 2026-10-07 ~08:1xZ -- LGIC naming and registration for every new resource

**Channel:** typed at the `1.0.0_SA_CTO` terminal (laptop). **Recorded by:** `1.0.0_SA_CTO`.

## His words, VERBATIM

"ALso make sure that everyone is being very diligence with LGIC_NAMING for any new resource creation, everything should be registered as well, i believe there is some index we have for this ecxact purpose."

## The index he means, as this seat reads the estate (measured 2026-10-07 ~08:1xZ)

- The register: `infra/logic/registry/resources.json`, 465 rows, each a resource with its type, owning system and evidence; beside it
  `systems.json`, `scopes.json`, `tiers.json`, `exemptions.json`, `legacy_addresses.json`.
- The vocabulary: `org/standards/NAMING_SCHEMA.json` (LGIC_NAMING's output).
- The builders: `lib/opal_naming.py` `name()` and `address()`; a refusal is a missing registry row to add, never a hand-typed name
  (CLAUDE.md rule 30).
- The gates: `.tools/naming-gate.py` at commit, WARN today; `.tools/naming-apply-gate.py` inside `.tools/safe-apply.sh`, which in its
  plan mode REFUSES a resource being ADDED whose own name grades badly (read from that file's header).

## What this seat does on it

- NFRA_CTLPLN PRD v0.13, contract C-NAMING: on any box, a new resource is created only through `safe-apply`, its name and address come
  from the builders, and its registry row lands in the same commit as its Terraform.
- One relay to every CTO seat (dell1, dell2, site Z) and to `2.0.0_SA_COO~C`.

## What is and is not mechanical, stated so "make sure" is not read as done

- MECHANICAL: a badly named NEW resource in a Terraform plan is refused at `safe-apply`.
- NOT MECHANICAL, binds by reading: (1) a resource created outside Terraform (a CLI or SDK create call), which the Dell create grant
  permits at the cloud and no naming gate sees; (2) that a created resource has its row in `resources.json`; no gate was found that
  refuses an apply for a missing row. Both are named in C-NAMING and the second is a cell for NFRA_CTLPLN's next issuance.
- UNMEASURED: whether `naming-apply-gate.py` and the commit-time gate are installed and firing on dell1 and dell2 (each reported 19 of
  20 hooks; the apply gate rides `safe-apply.sh`, which is in the repo).

-- 1.0.0_SA_CTO
