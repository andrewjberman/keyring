# drive log -- 2.0.0_SA_COO~G2, 2026-10-09 15Z-16Z (IRPT_YCDGEN FWD-1 window 3; irpt-status rev 4 outage)

- ~Y2 release 1 rev 4 (reader registers OPAL_RESEARCH_REVISION) CTO half @080347139a; landed 15:43:11Z (R0, R2 MET @4a611a8e5f).
- Census (CTO msgs 3630, 3647): today's 108 files and 385 tracked files at HEAD -- 0 client data; reported.
- Window 3: laptop ADD 16:08:46Z; W1 16:17:09Z; the first read timed out polling; a one-shot read at 16:22:43Z returned HTTP 500 for
  status and sections. irpt-status CloudWatch: TypeError build_retained_repositories() unexpected kwarg additional_policy_revisions
  at status_installed.py:137, 52 events from 16:17Z, every caller: rev 4 shipped split (composition.py at an older pin). ARMED row
  D2-S22 @692715f228; escalated to ~Y2 and the CTO at 16:24Z. The CTO ordered Branch B (msg 3678). ~DELL2 restored the rev-3 bytes
  (@21cad53292); AR2 applied. Live t6OJTCcm at 16:43:21Z, 0 crashes since. D2-S23 resolves S22 @f551980c99.
- Window 3 closed: W2 16:24:05Z (svc cottonwood), laptop REMOVE 16:33:06Z, ledger CLOSED 16:36:57Z. Secret reads ~16:17Z and
  16:22:43Z reported.
- FWD-1 waits on ~Y2's re-cut rev 4 (composition.py co-staged, row IRPT_ANLREQ-D2-S16), then one more owner read.
