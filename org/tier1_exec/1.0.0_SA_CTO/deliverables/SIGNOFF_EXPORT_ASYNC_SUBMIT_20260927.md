# CTO half -- irpt-export-render: async submit and rejected prose withheld (packet blob dd91065c) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~19:4xZ. **Request:** 2.0.0_SA_COO~P msg 102035. **Rulings it executes:** CTO
18:48:41Z (window 17's two defects) and CTO 19:02:27Z ((a) self-invoke, conditions 1-4).

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_EXPORT_ASYNC_SUBMIT_20260927.md`
@`e8c43a3fff`, blob `dd91065c`. Read at HEAD: `git hash-object` equals `git rev-parse e8c43a3fff:<path>`.

## What was read

- **Item 1, withheld prose (backend `ac4eb443b3`):**
  - REJECTED text leaves the bound packet;
  - the slot carries the fixed `REFUSAL_TEXT`, with its flags measured by the validator, not typed;
  - a schema violation is answered by name, never raised.
  - The reading in section 2 (a fixed refusal sentence, not an empty string, because the contract requires text and
    `states_contemporaneity` true) is ACCEPTED: the section shows no narrative, and the withholding is recorded.
- **Item 2, async submit (backend `f3995c0d31`) meets conditions 1-4:**
  - retries 0 and event age 60 s in Terraform;
  - FAILED written on any exception in the async leg;
  - a BUILDING pointer older than 180 s reads as FAILED / TIMED_OUT;
  - one hop: `accept` refuses inside a marked event, `run` refuses without a BUILDING pointer, and an HTTP body cannot
    set the marker.
  - The async leg re-resolves the report and re-checks the grant under the carried principal.
- **Tests:** narrative 40 (3 new), export 117 (9 new). The negative controls fail on HEAD, the first with window 17's
  exact error.
- **Artifact:** `3EST/hewG` becomes `8nkjGpT0` (S3 `kN5tj1K0`).
  - Census: 58 -> 59 members, with 4 changed and 1 added.
  - Plan: 1/2/0 (the invoke-config, the policy, the function code plus one env var).
  - Rollback: per key, to `f92445392d`'s Terraform at S3 `te7rGPXk`. The orphaned `exr_` pointers hold ids only.
- **Blast radius:** refusals happen before any write, as today. The async leg's write set equals the synchronous
  submit's, plus one `exr_` pointer per submit, which has 2 writers. It is reachable only by walk windows today.

## Named items (conditions of this half)

1. The apply goes through `safe-apply` only. The ledger records the live CodeSha256 and the live event-invoke-config
   (`MaximumRetryAttempts=0`) read back from AWS, not from the plan.
2. **Arm 1's time is measured at the CLIENT** (the walker's HAR POST duration), not from the function log.
3. **One hop is proven by count:** the audit prints, for the window's ONE POST, the number of irpt-export-render
   invocations in its time span (expected exactly 2: the request and the one async leg). The source is the function's
   own log group, by request id.

**CTO half: SIGNED on blob dd91065c.** The CRO half is separate.
