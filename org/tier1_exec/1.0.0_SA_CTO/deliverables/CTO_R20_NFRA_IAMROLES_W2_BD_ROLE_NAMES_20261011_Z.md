# CTO R20 -- NFRA_IAMROLES202609 w-2: the two legacy Black Diamond IAM role names, adopted under their live names

**By:** `1.0.0_SA_CTO~Z`, 2026-10-11 ~03:3xZ. **Register row:** X17 (`infra/logic/06_CONFORMANCE_LEDGER.md` section 6, written
by the register's lane). **Gate entries:** `NFRA-IAMROLES-R20-01` and `NFRA-IAMROLES-R20-02` in
`org/standards/NAMING_LEGACY_READS.json`, kind `r20_exception`.

## Andrew's acknowledgement (decider: Andrew)

Andrew-direct 2026-10-11 ~03:2xZ at the laptop `0.0.0_AB_MSTR` terminal. Item 4, VERBATIM: *"Yes we can make the
exception for now."* He was answering call `sitez-20261011T003538Z-5bdf`: *"Acknowledge an R20 declared exception for
the two legacy Black Diamond IAM role names (bd-merge-daily-lambda-role, bd-pipeline-task-role) so IAM-w-2 can adopt them
into Terraform under their live names (NFRA_IAMROLES202609)."* Record:
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261011_032xZ_OPEN_CALLS_ANSWERED_ITEMS_1_TO_9.md` @`5e10dd2dc5`
(on origin/CLOUD). His yes came after this seat's withdrawal
(`CTO_RULING_IAMROLES_W2_R20_WITHDRAWN_20261011_Z.md` @`9d98eeac1e`), so it supersedes that withdrawal.

## The departure

| field | value |
|---|---|
| file | `infra/aws/terraform/bd-pipeline/zz_adopt_family_a.tf` (today `.tf.proposed` @`d27dec64c2`; the step-5 rename carries the same bytes) |
| literals | `bd-merge-daily-lambda-role` (`NFRA-IAMROLES-R20-01`), `bd-pipeline-task-role` (`NFRA-IAMROLES-R20-02`) |
| occurrences | **3 each** in the file text, counted by `str.count`, the gate's rule: the resource `name`, the `import` `id`, and one header comment |
| what departs | Rule 30 / LGIC naming. The gate's carrier limb refuses the `bd` firm token in a hand-kept IAM role name (row Z-S34). The canon names (`{system}-49f-...`) need a create-plus-delete rename of two LIVE roles: `bd-merge-daily-lambda-role` was created 2026-01-15 and `bd-pipeline-task-role` 2026-01-29, and the second is used by ECS tasks |
| what does NOT depart | no new resource is named; no role is renamed, created or deleted; policies, trust and tags are as the w-2 never-widen pair signs |
| scope | ADOPTION only: these two literals, in this file, at this count. A fourth occurrence, another file, or a new role carrying `bd` is outside this entry |

## Grant

**CONDITIONAL, cutoff 2026-12-31** ("for now"). It ends at the first of three events:
- LGIC_ENFORCE PRD v1.4 FWD-8 (@eed4828f9d, dell1) is served, after which the gate reads adopted live names as EXISTING
  and these entries are retired;
- the roles' own R19 migration renames them;
- the cutoff passes.

Owner: `1.0.0_SA_CTO~Z`.

-- 1.0.0_SA_CTO~Z
