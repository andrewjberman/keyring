# NFRA_OPLGTW -- surprise channel, REMEDIATION v12 -- THE SLUG (rounds 25 and 26)

Author: 3.0.0_SA_CVO~Z. Round: v12. Fabric: site-z. Recorded: 2026-10-07T15:00:00Z. **Reader:** `1.0.0_SA_CTO~Z`
(ruling msg 30783; `1.0.0_SA_CTO~O` is not live).

6 rows, graduated by `adjudications/ADJUDICATION_v17.Z.md` C-S47. Rounds 25 and 26 have no L9 grade. All 5 orders are
complete; release r26 @feddb37244 is live. This seat re-ran the 9 checks: 8 PASS; rl12.AC1 reads FAIL only on its
live..CLOUD conjunct, because round 26's two cells are built and not released.
- **OPEN, for the CTO (4):**
  - **Z-W28-S17: a Schwab master account id is in 52 committed files, and those commits are on origin.** This is the
    one that should be read first.
  - Z-W28-S18: the AWS account id is in saved deploy output.
  - Z-S66 (ARMED): two drains raced in the shared tree; one commit took one seat's message and the other's tree.
  - Z-W28-S16: a forced head move in a linked worktree leaves no audit record.
- **OPEN, for the issuer (2):** Z-W28-S19 (ARMED: the manifest's release note breaks the naming gate at r27);
  Z-W28-S14 (the rehearsal runner's file filter).

**Advanced in place this slug (C-S49), REMEDIATED:** Z-S65 (`REMEDIATION_v11.md`). **Still OPEN from v11:** Z-S64 and
Z-W28-S13 (their cells are built, not released); Z-W28-S11 (at the CTO). **Still OPEN from v10:** Z-S61, Z-W28-S9.
**From v9:** Z-W28-S2.

```json
[
 {
  "id": "NFRA_OPLGTW-Z-W28-S17",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The host's real-holder run prints a Schwab master account id as a held-count key. The runner redacted only the tenant and object ids, so the id was saved and committed: the worker counted 254 matches in 52 files under this project's deliverables. The r26 outputs are redacted from here on; the older files are in git history, and site-Z's commits to fad25b1527 were pushed to origin on 2026-10-07. No commit gate caught it.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S17",
   "adjudications/ADJUDICATION_v17.Z.md#NFRA_OPLGTW-Z-C-S47"
  ],
  "remedy": "OPEN: the CTO rules three things. (1) Whether a master account id is inside the order bound 'never print or commit an account id'. (2) Whether the 52 files are redacted going forward only, or the history is rewritten; a history rewrite on a shared branch is a destructive git act and is Andrew's word. (3) Whether a commit-time check for this identifier shape is wanted; proposing it is legal, building it needs his word. This seat did not re-count the 52 files and did not open them.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v12",
  "remediation": {
   "state": "CLOSED_UNREMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v12",
   "closure": {
    "reason": "NOT_A_DEFECT",
    "pointer": "org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round26.md ADDENDUM 1 @51572f8092 (R38 withdrawn: a Schwab master account id is outside the bound, restated as a client account identifier); census deliverables/2.0.0_SA_COO~O/R38_WHOLE_TREE_CENSUS_20261007.md @48e547c6f9 (the value in 1,314 of 62,041 tracked files, production code and S3 key segments among them)"
   }
  },
  "closed": true
 },
 {
  "id": "NFRA_OPLGTW-Z-W28-S18",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "safe-ec2-deploy.sh and deploy-to-ec2.sh echo the artifact bucket name, which embeds the 12-digit AWS account id. A worker that saves the deploy output as its evidence commits the id; r25's saved output carries it 4 times. The r26 output was redacted before its commit.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S18",
   "adjudications/ADJUDICATION_v17.Z.md#NFRA_OPLGTW-Z-C-S47"
  ],
  "remedy": "OPEN: ruled with Z-W28-S17, as the same class. Either the bound is restated so an account id inside a resource name is outside it, or the deploy wrapper redacts the bucket name in what it prints. The wrapper is outside a worker's paths.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v12",
  "remediation": {
   "state": "CLOSED_UNREMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v12",
   "closure": {
    "reason": "NOT_A_DEFECT",
    "pointer": "org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round26.md R39 @c474e2d3f3 (an AWS account id inside a bucket name is outside the bound; no redaction of deploy output is asked)"
   }
  },
  "closed": true
 },
 {
  "id": "NFRA_OPLGTW-Z-W28-S16",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The head-move guard admits FORCE_HEADMOVE=1 in a linked worktree outside the workspace and prints that it cannot resolve the audit log, so the override leaves no record while the guard's own text says a forced move is logged. The one act it covered here was directed by the order and stays reachable by sha.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S16",
   "adjudications/ADJUDICATION_v17.Z.md#NFRA_OPLGTW-Z-C-S47"
  ],
  "remedy": "OPEN: fabric-wide, so the CTO routes it to the guard's owner. The guard resolves the shared workspace's audit log from a linked worktree (the common git dir names it), or refuses the override when it cannot write the record.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v12",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v12"
  },
  "closed": true
 },
 {
  "id": "NFRA_OPLGTW-Z-S66",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Two safe-merge runs overlapped in the shared tree. Commit 9f146f853a carries 2.0.0_SA_COO~X's subject and branch parent, 2.0.0_SA_COO~O as author, and the tree of OG-au-2. The AMGT_CORPUS branch reads merged with none of its 4 files at HEAD. safe-merge detected it only after the commit (exit 5) and printed the repair to the seat whose content had landed. A whole-index commit while the stale entries stood would have deleted three files.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S66",
   "adjudications/ADJUDICATION_v17.Z.md#NFRA_OPLGTW-Z-C-S47",
   "remediations/REMEDIATION_v10.md#NFRA_OPLGTW-Z-S61 (an earlier drain that left the shared index at the pre-drain tree; still OPEN)"
  ],
  "remedy": "OPEN and ARMED: any two seats draining in the shared tree at once can repeat it. The issuer's candidate is a lock taken before `git merge --no-commit` and held to the commit. safe-merge.sh is in the .tools lane, so the CTO routes it. Until it lands, the disarm is procedural: one drain at a time in the shared tree, announced as the integrator's merge windows are. The 4 AMGT_CORPUS files are 2.0.0_SA_COO~X's to land.",
  "owner": "1.0.0_SA_CTO~Z",
  "round": "v12",
  "disarm": {
   "state": "DISARMED",
   "owner": "1.0.0_SA_CTO~Z",
   "at": "2026-10-07T14:59Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~Z",
   "round": "v12"
  },
  "closed": true
 },
 {
  "id": "NFRA_OPLGTW-Z-W28-S19",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The hand-recorded manifest's release_note is a cumulative chain of every release's note. At r26 it passed 32,000 characters; the naming gate tries any slash-bearing string as a tracked path with `git cat-file -e HEAD:<value>`, and the argument exceeded the Windows command-line bound (WinError 206). The worker trimmed the three oldest segments by hand. The next release re-hits it.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S19",
   "adjudications/ADJUDICATION_v17.Z.md#NFRA_OPLGTW-Z-C-S47"
  ],
  "remedy": "OPEN and ARMED until one of two lands: a length guard in the naming gate (a value of thousands of characters is not a path), which is the gate owner's; or the release form's manifest step keeps the note to the current release and moves the chain to the ledger entry, which is the issuer's and can land before r27.",
  "owner": "2.0.0_SA_COO~O",
  "round": "v12",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~O",
   "at": "2026-10-07T16:57Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~O",
   "round": "v12"
  },
  "closed": true
 },
 {
  "id": "NFRA_OPLGTW-Z-W28-S14",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The host rehearsal runner stages only app/ and deploy/ files into the rehearsal copy. r26 was the first release to ship a gateway-root file (the allowlist); on the r25-form runner its row would have been rehearsed on the installed allowlist and read DENIED. The r26 copies add that one filename. A later release that ships any other gateway-root file needs the filter widened again.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W28-S14",
   "adjudications/ADJUDICATION_v17.Z.md#NFRA_OPLGTW-Z-C-S47"
  ],
  "remedy": "OPEN: at the next form edit the runner stages the release's own shipped set, read from `git diff --name-only <live> <release>` filtered by what the deploy tarball carries, with no filename typed into the filter.",
  "owner": "2.0.0_SA_COO~O",
  "round": "v12",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~O",
   "round": "v12"
  },
  "closed": false
 }
]
```

-- 3.0.0_SA_CVO~Z
