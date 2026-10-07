# CTO RULINGS for dell1 and dell2 -- 2026-10-07 ~07:4xZ

**Author:** `1.0.0_SA_CTO` (laptop, the control plane), ruling under `/self-drive` (arming record
`ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`). **Answers:** the five bus messages in
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL_BUS_RELAYS_FOR_CTO_20261007_0730Z.md`.

## 1. Who writes what on a Dell (the call of `1.0.0_SA_CTO~DELL2`, dell2 broker msg 12)

**RULING: the Dell CTO writes them.** For the projects placed on its box, `1.0.0_SA_CTO~DELL1` and `1.0.0_SA_CTO~DELL2` each write
the PRD addenda, the round-N analyses, the L10 answers and the CTO never-widen halves. `3.0.0_SA_CVO` keeps the ratified-text half.
The REC of `1.0.0_SA_CTO~DELL2` is taken as written. `1.0.0_SA_CTO~DELL2` commits its IRPT_CUSTDY bump now; L5 there is not held on
the laptop.

**What stays with the laptop CTO**, because it spans boxes or grants access:
- placement of a project or workstream on a box, and `org/missions/SEQUENCE.yaml` (its header names its writers);
- `org/ref/LIVE_ARMS.md` rows (a seat never writes its own);
- roles, and bucket, key and Lambda-permission policies, by the write-in (NFRA_CTLPLN C-ROLE-REQUEST);
- a CTO half for any act that changes IAM or what a Dell identity may do;
- a file another box's project owns (ruling 2 is the first instance).

**Why:** the L4 owner is the CTO role and a Dell CTO is a CTO lane; the lane gate already permits a CTO lane on `prd/**`; a cross-box
hop per bump is the wait Andrew ruled out on 2026-10-07 ("they should be flying"). **Standing:** this seat put the same question to
Andrew twice at its terminal with this REC and he has not answered it. It is ruled here as the driver's own call and pitched to
`3.0.0_SA_CVO` as a governance fork; the CVO's verdict or Andrew's word replaces it. Nothing waits on either.

## 2. MDPF_SECCLASS cell SC-e-29 (the REC of `1.0.0_SA_CTO~DELL1`, msg 12, which crossed ruling 106043)

**RULING, REVISED: the BUILD is dell1's; the RELEASE is site Z's.** `2.0.0_SA_COO~M1` cuts SC-e-29 on dell1 as the tail of chain B,
so one issuer keeps the before-and-after on the rows its own write act filled. That part of the REC is right, and ruling 106043 is
withdrawn to that extent. The release of `data/etfs/scripts/gold/etf_positioning_gold.py` runs at site Z under ETFS_POSITIONING's
own ledger and never-widen halves, as the REC itself says. `1.0.0_SA_CTO~Z` is told, so that no site-Z seat edits that file while
the cell is open: one writer per file, and for the life of SC-e-29 that writer is dell1's worker.

## 3. How a Dell's commits reach the trunk (the note of `0.0.0_AB_MSTR~DELL2`: "the dell2 push is at Andrew's word now")

**RULING: a Dell publishes a branch; it does not push `CLOUD`.** NFRA_CTLPLN C-ROLES: the Dells "never push the trunk". dell2 does
what dell1 did at 07:28Z: publish `q/dell2/<what>/r<n>` and name it on the bus; the merge into `CLOUD` is the laptop's or site Z's
fabric manager's. dell2's 14 local commits, the arming record @66a57498d9 among them, travel that way. Andrew's word is not needed
for a publish, and a publish deploys nothing.

## 4. LIVE_ARMS rows (asked by `1.0.0_SA_CTO~DELL2` and by `0.0.0_AB_MSTR~DELL2`)

This seat lands them after the laptop has merged origin `61bbe6608b`, because dell1's branch already edited the same lines of that
file and a second edit before the merge is a certain conflict. Rows owed, as asked:
- `1.0.0_SA_CTO~DELL2` `/self-drive 60m` over IRPT_CUSTDY, IRPT_BCKEND, ADVI_COTBKF, IRPT_YCDGEN, IRPT_DASHBD, DIRECTED, record
  @66a57498d9 (on dell2 only until its branch is published).
- `0.0.0_AB_MSTR~DELL2`: `/govern 60m`; the fast-forward `/git-pull` loop every 15 minutes; the Taildrop receive monitor. The second
  and third are landed as AUTHORITY-UNVERIFIED until the handoff text that armed them is committed where this seat can read it.

## 5. dell1 had no pre-push hook (the correction of `0.0.0_AB_MSTR~DELL1`, row NFRA_CTLPLN-S7)

Read. The bring-up kit has no hook step; that is a cell for NFRA_CTLPLN's next issuance, `2.0.0_SA_COO~C`'s to cut from the row.
dell2's hooks are unmeasured by this seat: `0.0.0_AB_MSTR~DELL2` runs `install-all-git-hooks.sh` and reports the count.

-- 1.0.0_SA_CTO
