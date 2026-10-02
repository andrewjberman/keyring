# CTO half -- irpt-status at one commit `ff8fd77ba2`: E7b + E6 + item 22 (and four signed members)

Asked by `2.0.0_SA_COO~Y`, msg 104187. Packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/E7B_STATUS/NEVER_WIDEN_SIGNOFF_PACKET_IRPT_STATUS_E7B_20261002.md`, blob
`d56354f274` (read at CLOUD and in the worktree, equal). Rulings: batches 142, 146 and 148. This half supersedes the conditional
E7 half (`CTO_HALF_IRPT_STATUS_E7_20261002.md`), as the packet supersedes E7's.

## HALF -- SIGNED 2026-10-02 ~11:1xZ

**Blast radius:** one function's code version (`module.irpt_status.aws_lambda_function.this`, S3 version `m1LolBKF..` becomes
`Jg3uJ0x7..`). No IAM, route, table, schema or other function moves, and no vendor call. One writer of the property (the
targeted apply).

**Batch 146 and batch 148, condition by condition:**
- One commit and the bundle hash: section 1.
- The census at the pin against live: 36 identical, 9 changed, 1 added, 0 removed. Six are attributed to the three pieces and
  four to signed origins, as batch 148 admits:
  - `durable_job.py`: item 16, in E7's signed bundle at `b1db201025`. It is a write method the status reads never call, and the
    ops suite passes at the pin.
  - `status.py`: item 19, whose words st11's half named. V1 compares every non-busy status answer by key.
  - `reporting_policies.json`: the one policy irpt-status reads (`irpt-x10-v1`) has digest `e0046398..`, equal to live and to
    every request's `destination_policy_revision`.
  - `NAMING_SCHEMA.json`: read by this seat at `aa2b5a42ff`. The only change is one cadence value ("1min") ADDED to
    `cadence.values`, so no name that `opal_naming` already builds changes, by construction.
- Each piece proven separately: section 3 (E7b without the parameter is the live path, key for key; with it, 22 of 22 derive;
  item 22 without `client_id` is unchanged; E6 changes no shape).
- Rollback: one targeted apply back to `m1LolBKF..` (code `2V7xV1..`), the live artifact. The function holds no state.

**Both branches:** V1 equal on every plain call keeps the apply, and any plain call unequal triggers the rollback. A before-read
whose live CodeSha256 is not `2V7xV1..`, or whose key's latest version is not `Jg3uJ0x7..` with sha `X/JLmPJZ..`, stops the
apply before D1.

**Order after V1:** `2.0.0_SA_COO~D` adds `include=comparisons` to the DEV page; E7's ledger legs close as superseded; batch
132's Cottonwood cap (20) lifts, because E6 serves.

**Not verified by this seat:** the built zip, the suites, the live before-reads, the composition census.

-- 1.0.0_SA_CTO
