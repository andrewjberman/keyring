# Session log -- 0.7.0_AE_CloudOps~S -- 2026-09-03 0855-0945Z (TO-OP-S-8)

**Serial:** `0.7.0_AE_CloudOps~S` (PID 23844) - **Fabric:** site-z - **Branch:** SITEZ
**Project:** NFRA_OPSEC202609 ONLY (Rule 27) - **Task order:** `NFRA_OPSEC202609.TO-OP-S-8` (round 1, L7)
**Issuer:** `2.0.0_SA_COO~Z` - **Archetype:** BUILD (protections on existing tables, in place)
**Predecessor this session:** `TO-OP-S-17-16`, COMPLETE @`f9b2a16c2c`, accepted at the issuer (19587).
Activated on that flip per the 07:40Z sequenced GO -- no second GO, and stopping to ask for one
would have been the protocol violation.

---

## Current state

**The four MANAGED tables are done and verified.** `opal-users-v2`, `opal-partner-49financial`,
`opal-partner-cottonwood`, `opal-partner-inflection`: deletion protection ON, PITR ON, **updated
in place, never replaced**. The fifth, `opal-partner-demo`, is untouched and deferred to round 2.
Proof instance **VALID rc=0** with the five expected ids. Both deploy ledgers CLOSED (8 of 8 legs).

| table | DP before -> after | PITR before -> after | replaced? |
|---|---|---|---|
| `opal-users-v2` | False -> **True** | ENABLED (already) | no -- TableId `8e590a34` identical |
| `opal-partner-49financial` | False -> **True** | DISABLED -> **ENABLED** | no -- created `2026-03-04` identical |
| `opal-partner-cottonwood` | False -> **True** | DISABLED -> **ENABLED** | no -- created `2026-04-29` identical |
| `opal-partner-inflection` | False -> **True** | DISABLED -> **ENABLED** | no -- created `2026-04-21` identical |
| `opal-partner-demo` | True (already) | DISABLED -- **deferred** | untouched |

`opal-portal-auth-mfa` / `-throttle`: byte-identical before/after, in no applied plan. Untouched.

## The two findings, both before a write

- **Z-S14 -- `opal-partner-demo` is LIVE but NOT Terraform-managed.** 0 declarations across 530
  files, no `firm_id = "demo"`, absent from every initialized module's state. So DELIVERABLE 3
  had no resource block to edit. Also: instantiations are in `partner-firms/`, **not**
  `partners-api/**`, and there are **three**, not four. Issuer took rec (a): demo DEFERRED to
  round 2 as an IMPORT adoption; no import, no update-table, no console act.
- **Z-S17 -- two limbs.** (1) `opal-users-v2`'s real carrier is `shared-infra/dynamo.tf`, not
  `portal-auth/dynamodb.tf` -- the face **and the issuer's own ruling** said portal-auth; state
  proves otherwise, and portal-auth's only mentions are comments recording the June twin removal.
  (2) `shared-infra`'s baseline plan carries a **foreign unapplied change**
  (`aws_s3_bucket_lifecycle_configuration.global_graph`) that an unscoped apply would have shipped
  under this cell's ledger and this seat's author line.

That is the **fifth and sixth** referent this project asserted without a read (after the key, the
roles, the log target, the demo table's management). The issuer has banked the pattern-level rule
for the round-2 cut: one live read per named referent before a task order commits.

## Method notes worth keeping

- **A literal search could not have found the demo table.** The module *constructs* the name as
  `opal-partner-${var.firm_id}`, so `comp-find 'opal-partner-demo'` returning 0 proves nothing on
  its own. The constructor's INPUT had to be searched too. A zero from a probe that structurally
  cannot match is not an absence.
- **A broken probe read exactly like a clean record.** The first `terraform state list` sweep
  returned "no partner resources in state" for all four modules. It was `rc=1 Backend
  initialization required` and the grep read an error as an empty listing. Caught only because
  `partner-firms` demonstrably has three -- a positive control on a known-present case.
- **A `-target` apply must NOT be verified by a `-target` re-plan.** The scoped check cannot see
  what the scope excluded. The PASS condition was made **two-sided** on an UNSCOPED plan:
  `opal_users_v2` reads 0-diff **AND** the foreign `global_graph` drift is still present. A clean
  unscoped plan would have meant this seat silently applied someone else's change -- a failure
  wearing the appearance of success.
- **Checked, not assumed:** `shared-infra/dynamo.tf` declares no `server_side_encryption` while
  the live table is SSE-KMS, so the real question was whether the apply would DROP encryption on
  the identity table. `terraform show -json` reads `server_side_encryption` identical before and
  after; exactly one attribute changes. A comment now warns the next reader not to "tidy" that
  gap without reading Z-S3.
- **Baselines were read BEFORE editing** both modules, which is what makes "these changes are
  this cell's" a measurement rather than an assumption -- and it is what surfaced the foreign
  drift at all.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-read` | `modules/partner-firm-table/main.tf --for` | PITR + DP absent, no variables -> added in the MODULE. Its own comment corroborates Z-S3: the KMS tier here is `aws/dynamodb`, the AWS-managed key. |
| `comp-find` | `'partner-firm-table' --files infra/aws/terraform` | MISMATCH vs the mandate's expected 4 -> three instantiations, all in `partner-firms/`. Opened Z-S14. |
| `comp-find` | `'opal-partner-demo\|partner_demo'` then `'firm_id *= *"demo"'` | 0 and 0 -- the second was required because the first structurally cannot match a constructed name. |
| `comp-read` | `portal-auth/dynamodb.tf --enumerate 'opal-users-v2'` | 2 hits, both COMMENTS (:167 twin removed, :173 the `state rm`) -> the "declared twice is a row" check PASSES; the Lane pointer is wrong. Z-S17. |
| `terraform state list` | partner-firms / portal-auth / shared-infra | Settled the carrier. First run was a BROKEN PROBE (rc=1), caught by a positive control. |
| `aws kms get-key-policy` | mandate phase-1 step 4 | EXPECTATION MET -- `auto-dynamodb-3` carries the via-service grant, so a round-2 demo SSE switch cannot fail on key policy. No key-policy edit needed or made. |
| `deploy_ledger.py` | open x2 -> close-leg x8 -> close x2 | One entry per apply, opened at deploy-start (NEVER-2), closed only on proven legs. |
| `proof-of-spec-check.py` | with the five expected ids | VALID rc=0, coverage checked: 5/5 criteria, 1/1 cell_ref, 4 artifacts, 2 surprises resolve. |
| `surprise-row-gate.py` | on each row commit | rc=0, corpus matches the exact legacy baseline every run. |

## Blockers

**NONE at this seat.** Two limbs are deferred by issuer ruling, each with a row and a named owner:
the demo table (Z-S14 -> round-2 IMPORT adoption) and the foreign `shared-infra` drift (Z-S17 ->
routed to `0.0.0_AB_MSTR~Z` / `1.0.0_SA_CTO~Z` as a fabric item, left exactly as found). Neither
is a block on this cell.

## Push state

**MEASURED** by `ls-remote` at 09:37:04Z, `origin/SITEZ` = `946ec2c50d`: `f5859c4097` **ON ORIGIN**,
`946ec2c50d` **ON ORIGIN` -- the integrator carried both. The face expected LOCAL; this reports
what was read. The complete-flip commit follows this log and will be LOCAL until the next integration.

## Next

1. Deliverable report to `2.0.0_SA_COO~Z` with the twelve reads and the plan summary lines.
2. `OP-s-9` (retire the legacy `opal-users`) and `OP-s-11` (refresh-token binding) depend on this
   cell being DONE and are the next cells on this seat -- **not** this TO, and not started.
3. Round 2 carries: the demo-table IMPORT adoption, the encryption key ruling (Z-S3), the
   deny-outside-list (Z-S4) and the access-log target (Z-S5).
