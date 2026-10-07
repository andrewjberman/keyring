# Never-widen CTO half -- NFRA_TRNSPT C3 (TR-p-4): one scheduled fire reaching 2026-08-11

Signer `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~15:3xZ.

**Packet:** `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/C3_DRIVEN_POSITIVE_ARM_PACKET_20261007.md` @5eaf7966af
(COO half SIGNED). **Authority:** round-3 analysis @c2b5eb89a4 section 4 item C3.

## SIGNED, for exactly this act

**The act:**
- APPLY 1: `-target=aws_lambda_function.mail_pull`, re-planned at apply; the plan must read 0 / 1 / 0.
- **Code:** the build of CLOUD `8f82af6281`, CodeSha256 `VGIq85Xxm5KVLCnv16BASS63RsPMHScMEwZJP5SuMNY=`, 48 members.
- **Environment:** `WINDOW_DAYS` "7" -> "60".
- APPLY 2, after the graded 2026-10-07T23:30Z scheduled fire: `WINDOW_DAYS` "60" -> "7", code unchanged.

A plan that reads anything other than 0 / 1 / 0, or a CodeSha256 other than `VGIq...` read back after APPLY 1, is outside this half.

## What I read at signing

- **Writers of the named property:** `WINDOW_DAYS` has 1 writer, `mail_pull.tf` (N = 1, the packet's read, consistent with round 3's
  packet).
- **The outcome, read from the producer's rule, not predicted from the input:**
  - `pull.run(..., admitted_only=True)` lists the window as spans of at most 31 days (C1).
  - It skips any message whose sidecar is already in bronze.
  - It writes a near miss not at all.
  - It writes an admitted message under a new key named by its `internetMessageId`, refusing to overwrite a different sidecar.
  - So the fire writes only new keys.
- **Both branches are covered by the packet's table:**
  - lands at least one message: new bronze keys, one new silver date per landed date, and the run records;
  - lands nothing: the run records only.

  A refused listing raises and writes nothing.
- **Expected candidates in the window, from the round-2 record:** 2026-08-11 (Manav, the target) and 2026-09-02. Landing both is the
  rule's output, not a widening.

## Conditions on this half

1. **Rollback of a landed key is a DELETE, and an S3 delete needs Andrew's word** (CLAUDE.md, Agent Autonomy). This half signs the
   apply, the fire and APPLY 2. It does NOT pre-authorize deleting landed keys. If a landed object must go, the key list goes to
   Andrew first.
2. **The ledger spans tonight's fire.** If APPLY 2 is not executed, the residual is that later fires list 60 days, not 7. Already
   landed messages are skipped by the sidecar rule, so the residual is wider listing, not new writes of known mail. That residual is
   accepted for at most one extra fire. The ledger names the seat that executes APPLY 2 and its time.
3. **No content read from dell2** (laptop ruling A). Grading leg (2) is a laptop FILE through the fenced-read path. Keys and
   LastModified may be listed from dell2.
4. **Which machine applies:** dell2 may apply this act, which is a function's code and one environment value. If the apply is
   refused for a permission (NFRA_CTLPLN Deny set), it goes to the laptop applier under this same half, unchanged.

-- 1.0.0_SA_CTO~DELL2
