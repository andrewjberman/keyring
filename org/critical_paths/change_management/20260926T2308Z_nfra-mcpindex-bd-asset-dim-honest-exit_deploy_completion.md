# Deploy Completion Record
**Date opened:** 2026-09-26T23:08:40.184747+00:00
**Status:** OPEN
**Deploy:** opal-bd-asset-dim-download exits non-zero on failure, plus ONE ad-hoc vendor-facing fire on Andrew's word (NFRA_MCPINDEX MX-s-4 steps 1-2)
**Authored by:** 0.7.0_AE_CloudOps~I
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: the exit 1 inserted into the failure branch | commit hash |  | OPEN |
| L2 | activation | SSM document opal-bd-asset-dim-download, new DocumentVersion via update-document | describe-document LatestVersion advances and Hash changes from 0be92f2611060f033011ed74ff5647be127f0511ee723ce42f890d3c7a7a30e6 |  | OPEN |
| L3 | verify | the LIVE document content at the version the trigger Lambda will run | get-document shows 'exit 1' inside the DOWNLOAD_RC/MERGE_RC failure branch |  | OPEN |
| L4 | activation | ONE ad-hoc vendor-facing run via Lambda bd-asset-dim-trigger, on Andrew's word 2026-09-26 22:05Z + 22:15Z | the invoke response, the SSM CommandId, and the run ledgered in this lane's deliverables |  | OPEN |
| L5 | verify | the SSM command status for that run (AC4's evidence) | list-command-invocations Status for the CommandId -- Failed if the download fails, which is the honest report the old document could not make |  | OPEN |
| L6 | git | the ledger close | commit hash |  | OPEN |

## Log

- 20260926T230840Z OPENED by 0.7.0_AE_CloudOps~I with 6 leg(s)

## Blast radius and rollback per key (NEVER-2; measured BEFORE the act)

**WRITE SET -- two things, and one of them is a vendor-facing side effect.**

1. SSM document `opal-bd-asset-dim-download`. PRE-ACT, read at 2026-09-26 23:0xZ:
     DefaultVersion 1 | LatestVersion 1 | Status Active
     Hash 0be92f2611060f033011ed74ff5647be127f0511ee723ce42f890d3c7a7a30e6 (Sha256)
     ONE version exists. The change adds version 2; nothing is destroyed.

   >> ROLLBACK IS **NOT** A DEFAULT-VERSION FLIP, AND ASSUMING IT WAS WOULD HAVE LEFT A DEAD
   ROLLBACK IN THIS ENTRY. `bd-asset-dim-trigger/lambda_function.py` calls send_command with
   `DocumentVersion='$LATEST'`, NOT with the default. So `update-default-version 1` would change
   nothing about what actually runs. ROLLBACK = `update-document` again with the v1 content, which
   is `git show 4b3a757410^:infra/aws/ssm/opal-bd-asset-dim-download.json`, creating a version 3
   that restores the old bytes. Read from the producer's own code, not predicted from the API's shape.

2. EC2 `i-0e6f6dc014fdcf1cd` (`bd-assets`), currently STOPPED, will be STARTED by the trigger Lambda
   and shuts itself down 2 minutes after the run. Rollback: none needed; it is the instance's normal
   daily cycle. NOTE the interaction with this very change: on a FAILING run the new `exit 1` returns
   before `shutdown -h +2`, so this instance may be left RUNNING. Measured precedent says it is not a
   leak in practice -- `opal-bd-allocation-download` already uses this exact pattern and has failed
   daily since 2026-06-23 with no bd-* runner in the running-instance list -- but on THIS run the
   instance state is checked afterwards and stopped by hand if it is up. That check is L5's.

**THE VENDOR-FACING SIDE EFFECT, named because it is the part that is not ours.** The run attempts ONE
login to the Black Diamond portal with the existing credential from `opal/bd/credentials`. Andrew's
word, 2026-09-26 ~22:05Z ("rec a approved") and ~22:15Z ("vendor call is fine you have egress"),
covers exactly this: ONE ad-hoc run of the EXISTING producer. It does NOT cover a new credential, an
MFA device, an account change, or any contract. If the run shows the failure needs one of those, this
lane STOPS, files a BLOCKING row and reports -- MX-s-4 step 1's own carve-out.

**NOT TOUCHED:** the EventBridge rule `bd-asset-dim-pipeline-trigger` (read, never changed -- Monday
22:10Z remains the acceptance); the sibling documents `opal-bd-fees-download` (which carries the
IDENTICAL missing `exit 1` and is NOT this order's) and `-allocation`, `-transaction`, `-realized`,
`-unrealized`; any IAM role or policy; any gold or served artifact.

**EXPECTED OUTCOME, BOTH BRANCHES, stated before the act.**
  - EXPECTED (the 70th consecutive failure): the login times out again, the wrapper now exits 1, and
    SSM records **Failed**. That is a PASS for AC4 -- the honest report the old document could not
    make -- and simultaneously leaves AC1 FAILING, because AC1 needs a successful download. Both at
    once is the anticipated result, not a contradiction.
  - SURPRISE (the login succeeds): AC1 becomes reachable, the merge runs, and `silver/assets/` gets a
    new partition. Then the 95-day outage was transient or environmental, and that is a finding worth
    as much as the repair.
  - EITHER WAY the run is ledgered in this lane's deliverables, per MX-s-4's preflight.
