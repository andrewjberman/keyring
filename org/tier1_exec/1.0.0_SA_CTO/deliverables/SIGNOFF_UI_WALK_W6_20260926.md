# SIGN-OFF (1.0.0_SA_CTO half) -- WINDOW 6: the Analysis chain once, end to end

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W6_20260926.md`
blob `fffdca65d0ecbd88c69017b1082372266a3df3d4` @`e9c283801f` (2.0.0_SA_COO~P msg 101601).
**Orders met:**
- CTO 101441/101466: one window runs the WHOLE chain, not hop by hop, and Analysis export stays out.
- CTO 101355: the no-principal proofs come first. They are pinned: hops 3 and 5-7 offline, hop 7 READY on real vendor
  PDFs, hops 8-9 4/4 served.

**Signed:** 1.0.0_SA_CTO, 2026-09-26 ~23:1xZ, under the self-drive arm @`ce6aa15a17`.

## SIGNED, as the packet reads

**Acts, in order:**
- K4: ~Y's ONE upload, to NORMALIZED;
- K5: ~Y's ONE Overview submission on K4's NEW input, to READY;
- K10: ~D's page reads (sections, status, history, request read).

Plus K1, K1-CRED and K2 as v10, and K3 retained.

**The write set, accepted as measured:**
- the cottonwood rows and objects as section 2 lists them;
- ONE `_opal` `PROVIDER_OPERATION#` lease row, the only write outside the firm tenant, named in the audit;
- one SQS message, deleted at READY.

**Vendor calls, named** (the host-workflow authorization CTO 100667 (1) and the session egress CTO 101098, each
ledgered with the resident journal line as its receipt):
- K4's `securities_info` GET;
- K5's reads, and one each of holdings_upload, portfolio_create, report_create and the PDF download;
- at most 5 checkpointed redeliveries, where a repeated create is branch (d);
- nothing else.

**Branch (e) accepted:** a chain that stops short of READY is the result, with no retry and no second POST. The
principal is deleted on schedule, and the terminal state is read afterwards by read-only table reads.

**The route audit:** as section 4. Any `/export`, any `/auth/admin/`, or a second `/analysis(/inputs)` POST is branch
(d).

**What this window grades:** FWD-1's Analysis hop, taken to a rendered, served result. The CTO reads the combined
log (~D's HAR plus ~Y's act log) at the next analysis.

## Second half

**4.0.0_SA_CRO.**

## Amendment (2.0.0_SA_COO~P msg 101632, ~23:4xZ): ~D's C25 re-walk on the idle window-6 principal -- ADMITTED

**The CTO half admits** ~D's read-only C25 re-walk on principal `irpt-uiwalk-1790464832` until its 00:20Z delete. The
walk uses a 49F 3-account client on local DEV `c3d422a3` and window 5's route classes. This avoids a second principal
create.

**Named, because v6's key list lacks it: K9**, the retained Performance reports the page's GETs compute (REPORT#,
ARTIFACT# and RETENTION# plus blobs, the human-read path, RETAINED), exactly as window 5 `4b68468e` K9. Nothing else
widens:
- the same route classes (section 4), with any `/export` or `/auth/admin/` request as branch (d);
- the same radius;
- the same delete time.

**This needs 4.0.0_SA_CRO's half too.** Until the CRO admits it, ~D does NOT walk on this principal.

## Ruling (2.0.0_SA_COO~Y msg 101672, 2026-09-27 ~00:53Z): branch (e) is STRUCK; a window keeps its principal until its jobs are terminal

**Finding, verified at the bytes:** `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py:274-281`.
`principal("start")` replays the refresh decision on the submitter's CURRENT profile row before any grant is used. A
job whose submitter was deleted therefore cannot be claimed. After the 00:21:32Z delete, receives 2 and later of job
`REQ-3a1b73a8` raise and are retained with the row untouched, and the job reaches the DLQ at about 01:12Z. Receive 1
(00:12:08Z) failed in the host capture for a cause not yet read. No vendor write happened.

**Ruling (1.0.0_SA_CTO), binding every future UI-walk window packet:**
1. The delete leg runs only after every job the window started reads terminal.
2. A packet that reaches its deadline with a non-terminal job states that job's disposition before the delete.
3. Branch (e), "the job continues server-side after the principal is deleted", is struck.

**Window 6 residue:** 2.0.0_SA_COO~P reads job `REQ-3a1b73a8`'s row at DLQ time. If the row stays non-terminal, ~P
brings a one-line packet amendment naming how the row is closed, or that it is left and why. This half signs it the
same tick.

**Not authorized here:** the receive-1 diagnostic wrapper run is a live YCharts call and waits on Andrew's word. It
gates no open act.
