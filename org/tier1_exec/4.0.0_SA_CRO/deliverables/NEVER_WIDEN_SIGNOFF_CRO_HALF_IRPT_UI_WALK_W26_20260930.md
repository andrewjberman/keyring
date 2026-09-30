# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 26: Andrew's three-variant automated-submission proof, one principal that outlives its jobs

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W26_20260930.md`
blob `0b209ba626` (at `d052be1db4`; the working file's hash equals the committed blob, 2026-09-30 ~05:5xZ).
- **Word diff:** window 25's text (blob `f3273476`, this seat's half `NEVER_WIDEN_SIGNOFF_CRO_HALF_IRPT_UI_WALK_W25_20260930.md`)
  with these deltas: three bodies, one per variant (Y1 Overview, Y2 Comparison `opal_long_term`, Y3 Multi
  `opal_short_term,opal_intermediate_term`), same CSV, cottonwood, serialized on the `irpt-jobs` terminal (cap 3 submissions,
  W25 had 1); cap 150 minutes (W25: 60); credoff moves from `2.0.0_SA_COO~P` to `0.0.0_AB_MSTR`; and K1 is deleted only when
  all three jobs are terminal, not at window close, retained past the cap if a job is still live.
- **Asked by:** 2.0.0_SA_COO~Y, msg 103175. **Other half:** 1.0.0_SA_CTO. **This seat is not in the act.**

## VERDICT: SIGNED on blob 0b209ba626, with six conditions

The window creates one admin-shaped principal, runs one login and three vendor jobs for one firm under it, and moves nothing
served for any other user. The one substantive change, keeping the principal alive until its jobs are terminal, closes the
cause of S231 (deleting K1 over a live job left REQ-86f1ce70 unrunnable) and adds no reach: the credential is deleted before
the vendor call, so a retained K1 cannot log in. The window is larger than W25 (three vendor submissions, 150 minutes), each arm
is independent, and Y3 can be dropped at a cost of the MULTI measurement only, as the packet says.

### Read here (measured by this seat, 2026-09-30 ~05:5xZ)

- **The pins, live:** irpt-ycharts-generate LastModified 2026-09-29T15:00:32Z, CodeSha256 `inrij6hL...`, equal W26-1.
  irpt-generation-dlq 1 visible / 0 in flight, the packet's baseline.
- **The queue is NOT 0/0 now.** `irpt-generation` reads **0 visible / 1 in flight**. The packet's own text says the stranded REQ-86f1ce70
  "can keep cycling harmlessly" (W26-4) and also that `irpt-generation` "must be 0/0 before each K5" and "no non-principal job is
  live" (W26-1, W26-2). Both cannot hold while the stranded message cycles: the gate as written may never open, or may open only
  by chance in the seconds the message is visible. That is condition 1.
- **The record of Andrew's word:** the packet quotes his ~04:4xZ direct ("we need to do a test to actually prove an automated
  ycharts submission for each of the three variants right now ad hoc") and cites the 04:3xZ record for the owner
  (`ANDREW_DIRECT_20260930_043xZ_YCHARTS_OWNER_IS_COO_Y.md`, present). I found no file recording the 04:4xZ direct itself in
  `2.0.0_SA_COO/deliverables/` (only the 043xZ owner record). W25 had one. Condition 2.
- **The restart ledger:** `irpt-resident-restart-3variant-20260930` has its completion record
  (`org/critical_paths/change_management/20260930T0511Z_...`); the resident hash and pid are the packet's and ~Y's host reading,
  READ by this seat and not re-measured.

## Conditions

1. **Restate the solo gate so it can be tested.** Before create, ~Y writes in the ledger the exact read that proves solo given the
   stranded message: for example, `irpt-generation` shows 0 visible, and the ONLY in-flight message is REQ-86f1ce70 (its jobs row
   state unchanged, refused at `current_authority` before any capture, no vendor call), read twice around the K5. If that
   cannot be shown, the window does not open. A "0/0" that the stranded message prevents is not a gate. If the stranded job is
   moved or removed, that is its own act under its own record (the packet says it is neither revived nor deleted here) and the
   DLQ baseline of 1 changes only with a stated new baseline.
2. **Andrew's ~04:4xZ direct is committed verbatim as a record** (channel, time, his words) before the window opens, and the
   packet's scope is read literally from it: three variants, one submission each, no retry, ad hoc now. Nothing wider is covered.
3. **The second-seat credoff is accepted, not assumed.** `0.0.0_AB_MSTR` must have acknowledged the role (a broker message or a
   ledger note naming it) before create; `walk_principal.py --kind=uiwalk credoff <epoch>` and the `ParameterNotFound` read-back
   are that seat's act and its timestamp goes in the ledger. If MSTR has not accepted, the window does not open and the credoff
   does not fall back to `~Y`.
4. **The retained-principal deadline.** If K1 is retained past the cap, the ledger names an owner and an hour by which its jobs
   are terminal and K1 deleted (consistent read finding no item), and states in one line what K1 can and cannot do while it
   exists (no credential, cannot log in, exists only for the resident to resolve a job's recorded owner). An admin-shaped
   principal with no owner and no clock is not covered by this half.
5. **Pins re-read at create, including the resident root and worker hash by SSM**, and the users census (count and digest) and
   `walk_window_census.py` before and after; DLQ growth over the stated baseline is a BLOCKING row the same tick.
6. **Per body, the terminal state by name from the rows themselves** (`irpt-jobs` state and `job_detail.code` by consistent Query;
   for a READY job the `ORIGINAL_VENDOR_PDF` object and the certified report), the journal as corroboration only; a vendor refusal
   is recorded as the result. The remaining arms still run after a failed arm, as the packet says; no retry of any body.

## Named items (not refusal grounds)

1. Three vendor submissions in one window is a wider live vendor act than W25's one. It is covered only by Andrew's word as
   condition 2 reads it; a fourth body, a retry or a second window needs its own word.
2. A three-body run of about 110 minutes leaves the cap's margin as the packet's own arithmetic; a window that reaches the cap
   with an arm unrun records it as unrun, never as a verdict.
3. The packet's "first two questions already answered" (not the shape, not the credential) rest on S230 and S231; this seat read
   the packet's account of them and did not re-open the rows.

## What this half signs against

Packet blob `0b209ba626`; W25's text (`f3273476`) with its conditions as narrowed; rows S230 and S231 as the packet cites them;
Andrew's two directs as the packet quotes them; the pins in W26-1; the three bodies, counts and serialization in W26-2; and the
interval, second-seat credoff and principal-outlives-its-jobs clause in W26-3, as conditioned above.

## Addendum 1 (2026-09-30 ~06:0xZ) -- RE-AFFIRMED on the amended blob `1c88bb4968` (@`628d7e7602`), with condition 7

- **The delta, read (`git diff d052be1db4 628d7e7602`):** W26-1's queue row and W26-2's solo bullet now point to a new W26-5, the SOLO GATE
  (a scan of `irpt-jobs` for non-terminal jobs, minus this window's arms and two named stranded jobs, remainder empty; queue depth printed as
  context). The working file's hash equals the committed blob `1c88bb4968`. It is a narrowing and adds no arm, login, retry or reach; it answers
  this half's condition 1.
- **Measured by this seat (2026-09-30 ~06:0xZ, read-only `dynamodb scan` of `irpt-jobs`, projection `job` and `state` only, 17 items scanned,
  no `LastEvaluatedKey`):** the four-state filter the amendment names returns exactly two jobs, both SUBMITTING: `REQ-3a1b73a8dead02a17a09043b`
  and `REQ-86f1ce7062356bc5c109ce12`, the two the amendment names. Its two-jobs claim holds at this time.
- **A gap in the gate as written.** The amendment scans for `QUEUED`, `CLAIMED`, `SUBMITTING`, `SUBMITTED`. The job state machine is
  `RECEIVED, CLAIMED, SUBMITTING, SUBMITTED, UNCERTAIN, DOWNLOADING, EXTRACTING, CERTIFYING, READY, FAILED, ATTENTION`
  (`infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py:16`). `QUEUED` is not a state; `RECEIVED`, `UNCERTAIN`, `DOWNLOADING`,
  `EXTRACTING` and `CERTIFYING` are non-terminal and are not in the amendment's list, so a job in one of them (a download from the vendor is
  work with the vendor) would pass the gate unseen. Nothing sits in them today; the scan by complement (state not in READY, FAILED, ATTENTION)
  returned 4 items: the same 2 SUBMITTING plus 2 rows with no `state` attribute (non-job rows).
- **Condition 7 (added; conditions 1-6 carry, with condition 1 met in form by W26-5 subject to this one):** the solo gate is the COMPLEMENT
  scan: every `irpt-jobs` item whose `state` is not READY, FAILED or ATTENTION and which HAS a `state` attribute, minus this window's arms and
  the two named ids; the remainder must be empty, read immediately before each K5 and printed with the scan's item count and whether it returned
  a `LastEvaluatedKey`. Rows with no `state` attribute are named in the ledger as non-job rows, not counted.

**RE-AFFIRMED** on blob `1c88bb4968`, with condition 7.

## Addendum 2 (2026-09-30 ~06:2xZ) -- RE-AFFIRMED on the amended blob `a4ba10a9d4` (@`38bf9a5c1b`); condition 7 is FULFILLED

- **The delta, read (`git diff 628d7e7602 38bf9a5c1b`):** one section, W26-6 (amendment 2). It derives the non-terminal job states from
  `durable_job.py:16` (the 11-member frozenset), subtracts the three terminal (`READY`, `FAILED`, `ATTENTION`), and prints the eight that block
  (`RECEIVED, CLAIMED, SUBMITTING, SUBMITTED, DOWNLOADING, EXTRACTING, CERTIFYING, UNCERTAIN`), with `UNCERTAIN` blocking fail-closed. It states
  that `QUEUED` is a public label from `owned_status.PHASES`, not a durable state, and re-measures: 17 of 17 rows scanned, 2 matched, exactly the
  two named stranded jobs. The working file's hash equals the committed blob `a4ba10a9d4`. It adds no arm, login, retry or reach.
- **Condition 7 (the complement scan, count printed):** met in substance by W26-6. Its printed denominator is "17 of 17 rows scanned", which
  covers the item count; the `LastEvaluatedKey` line (whether the scan was single-page) is asked to be recorded in the ledger with each read,
  not as a refusal ground. The two rows with no `state` attribute this seat found at 06:0xZ are not job rows and do not enter the count.
- **Placement:** this half was on the seam branch `cro-w26-half` while the shared tree was mid-merge; it is now on CLOUD HEAD, so the packet's
  "opens once both halves are at HEAD" holds for this half.

**RE-AFFIRMED** on blob `a4ba10a9d4`. Conditions 1-7 carry.
