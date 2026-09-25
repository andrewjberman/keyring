# IRPT Analysis hops 2-3 built, handed over, served; the live 12.03 run staged -- 2.0.0_SA_COO~Y

**Date:** 2026-09-24 (17:50Z) to 2026-09-25 (01:35Z)
**Task Order:** ad-hoc -- goal record `ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md`, IRPT_BCKEND~Y
**Status:** IN PROGRESS
**archetype:** IMPLEMENT

---

## Objective

Blast-mode return (CTO 100784/100798): build the resident half of RESOLVE_UPLOAD (CTO 100667 shape 2) and drive the
Analysis journey toward `/verify` SOUND, on the 20m goal loop that reads the `IRPT_BCKEND~Y` lease each tick (C11, CTO
100819).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `'UploadServiceRequired\|...\|generate_installed' investor-reporting --files` | PASS | 13 hits over 386 files; found the one docstring-only reference |
| comp-read | `--enumerate` on test_operation_lease.py, envelope.ts, ProspectComposer.tsx, prospect.ts, responses.ts | PASS | located the sys.modules replacement (:12-15) and the portal's legacy body (:30) |
| comp-find | `'NEEDS_CORRECTION\|NORMALIZED\|input_id' portal/.../InvestorReporting` | PASS | 82 hits over 529 files, banded |
| comp-which | IAM question, where-does-M's-build-run question | PASS | routed to comp-iam-usage; routed to comp-pipescript |
| comp-iam-usage | `reach-check` on the runner and generate roles | PASS | allowed on PutItem/SendMessage; control DeleteTable implicitDeny |
| comp-pipescript | `deployed .../holdings_snapshot.py` | PARTIAL | searched the mdpf tree only (SUBJECT_ABSENT, scoped) |
| comp-find --corpus aws | `'investor-reporting/analysis'` | PARTIAL | vintage 12:51Z predates today's routes; the live get-routes read answered it |

**What worked:** comp-read `--enumerate` with denominators on single files; the comp-iam-usage reach-check with a separate
negative control.
**What failed:** comp-find over the aws corpus was stale for the same day's route changes.
**Gap found:** no comp-tool names the runtime that runs the `investor_reporting` gold bundle.

---

## Work Completed

### 1. RESOLVE_UPLOAD, both halves (Y `bb1eb7f92b`, fix `10a16bd89d`, lookup `d16b7c8743`)
- **Upload POST:** retains the file, publishes `NORMALIZATION#` as RESOLVING, and sends one closed `resolve_upload`
  message. A re-send is bounded to once per 960 s by a conditional write.
- **Resident (`ResidentAssembly.resolve_upload`):** re-grades the actor, then resolves with one lease-fenced
  `securities_info` GET, freezes, publishes `INPUT#`, and flips the row once. A lost race returns the winner. A
  refusal is written as NEEDS_CORRECTION, by name. A provider outage answers RETRY.
- **Attribution fix:** an ordinary owner's absent `home_firm_id` now reads as its `firm_id`.

### 2. Exact P patches, applied and served
- `P_UPLOAD_COMPOSITION_20260924` covers hops 2+3. It exposed the lost viewer seam (P restored it at `19b38e2f22`),
  and a test-pollution red that Y fixed at `522afcfd17`.
- P deployed the resident `f624e8a72f` first, then generate `LdjdnnLh` (19:49Z).
- Y verified the deployed bytes against source, the live route, and the grants.

### 3. Contract and portal
- The portal sent the legacy body and threw on RESOLVING. The published schemas admitted neither the template body
  nor RESOLVING.
- `P_UPLOAD_CONTRACT_20260924.patch`: P landed it at `a47102cc8f`.
- `D_UPLOAD_TEMPLATE_LANE_SPEC_20260924.md`: ~D landed it at portal DEV `088386fe`, which is what 5174 serves.

### 4. Coverage and prep
- Y2 deferred arms (`58280c8dd4`).
- Hops 1-7 offline on the v2 input: the vendor upload carries AAPL 10.01 and VNQ 2.02 (`a9fba2f3e9`).
- Runbook revised (`f2cba3871e`).
- Custody decoder rung-2 read (`70c464cec9`).
- Shares prices: CTO ruled (c), refused by name for v1 (100887).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Built the Lambda half as well as the resident half | P's own docstring names the upload composition Y's surface |
| Stored findings capped at 500 + `findings_total` | DynamoDB's 400 KB item limit |
| No `--once` against the live queue | the service is the one consumer; a second one could take the job |
| Handed P and M the seam merge instead of resolving it | 8 hunks of auth semantics in P's `_scope` |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `intake/uploads.py`, `intake/upload_resolution.py`, `ycharts/generate/resident_worker.py` + 4 test files | RESOLVE_UPLOAD | Yes -- Y branch, LOCAL |
| `ycharts/session/tests/test_operation_lease.py` | one module identity | Yes -- `522afcfd17`, LOCAL |
| `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~Y.md`, the runbook, the P patches, the ~D spec, the decoder read | records | Yes -- CLOUD, LOCAL |

---

## Blockers

None BLOCKED. Waiting on others:
- Andrew: the live 12.03 upload. It was still 0 upload rows at 01:32Z (control: SELECTION# = 14).
- P: the custody composition.
- M: the comparison policy consumer.

---

## Current State

Hops 2+3 are SERVED and verified from deployed bytes. The portal DEV `088386fe` on 5174 and the contract
`a47102cc8f` carry the template lane and RESOLVING. The live thread's next act is Andrew's upload of
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/aapl-vnq-12.03.csv`. Y then reads the rows, the queue and the
resident journal against the runbook. Y branch tip `a9fba2f3e9`, LOCAL; the loop cron is `87624362`.

---

## Next Steps

1. **[Andrew]** Upload the 12.03 template as an Opal viewer, then Generate Overview.
2. **[2.0.0_SA_COO~Y]** Read UPLOAD#/NORMALIZATION#/INPUT# and the queue; walk runbook hops 1a-10; record digests.
3. **[2.0.0_SA_COO~P]** The custody composition, after the decoder read and the refusal spellings.
