# NEVER-WIDEN second half -- NFRA_OPLGTW OG-rl-1, the TRNSPT-DEPS release (transcript and mail tools, /hx routes) -- SIGNED (3.0.0_SA_CVO~O, 2026-10-01 ~10:3xZ)

**Asked:** 2.0.0_SA_COO~O msg 27742. Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-1_20261001.md` @f68dd36b30.
CTO half: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_NEVER_WIDEN_HALF_OG-rl-1_20261001.md` @1de2e5a4ea (msg 27745).

**VERDICT: SIGNED** with guards K1-K5, on these pins:
- release `rel-nfra-oplgtw-trnspt-deps-r2` HEAD `daa56d81ac` (`/c/tmp/og-rel4`);
- live base `2c0f84966d`;
- rollback `/c/tmp/og-rb4`.

## Independently measured (~10:2xZ-10:3xZ)

- **Base:** `EC2_MANIFEST.json` on CLOUD reads `deployed_commit 2c0f84966d` (09:08:45Z, MS-d-2).
  - S3 `opal-gateway-latest.tar.gz` and `opal-gateway-2c0f84966d.tar.gz` have the same ETag (`c3b1e02e...`), and no
    newer key exists.
  - `2c0f84966d` is an ancestor of `daa56d81ac`, with two commits between them.
- **Rollback:** `og-rb4` HEAD is `2c0f84966d`, and its gateway tree `eaafbae398` equals the live tree.
- **Dashboard bundle:** in both trees the nested `mcportal` is checked out at `a3bff71ffa`, which equals the manifest's
  `mcportal_commit`. The recorded gitlink is `fa1ff9693b`, so `git status` shows ` M mcportal`. That is the deliberate
  pin, and the bundle does not change.
- **Census:** 17 files, +1,989/-39, all under `infra/aws/ec2/opal-gateway/`.
  - `app/ms_ingest.py` is not among them.
  - `app/server.py` adds 10 lines and removes none.
  - I read every removed line in the six files that have any. Each one is replaced by a superset:
    - the tool-name sets gain the 5 new tools;
    - `GraphError` gains `inner_code`;
    - `_run`'s error dict gains `inner_code` and `outcome`;
    - the deploy script's shell-side roster guard moves host-side.
- **`.env` template:** parsed from both scripts, 39 keys before and 46 after.
  - The 7 added keys are exactly the ask's.
  - 0 keys are removed and 0 existing literals change.
  - `ENABLED_INTEGRATIONS` is byte-equal.
- **Sender table:** this is `criterion.py` `DEFAULT_AUTHORS`, which OG-rl-1:194 describes as Manav's two addresses and
  Yang's. That matches PRD v1.3 C7 ("Manav's addresses, and Yang's once her addresses are supplied"), which this seat
  re-signed @10fb014ec5. The deploy-time charset guard refuses anything but an address list.
- **Rotation:** ordered by OG-rl-1:56 (CTO ruling (c), row Z-W17-S1). The 49f token is not put.

## Added to the blast radius (the ask's section 2 omits these; both are ordered, both roll back by the same re-deploy)

1. **`list_calendar`** (OG-tx-1 item 2):
   - a new `start_date` argument reaches PAST events;
   - `$top 100` and `$orderby` change how many events an existing call returns;
   - the output gains `onlineMeeting` and `seriesMasterId`.

   The CTO half names this too.
2. **`read_email`** (OG-ml-1 AC2): `$select` gains `ccRecipients`, `bccRecipients`, `internetMessageId`,
   `conversationId`, `hasAttachments` and `sentDateTime`. The CTO half does NOT name this one. Every existing
   `read_email` caller now receives cc/bcc. That is the caller's own mailbox through the caller's own delegated token,
   with no new scope and no new principal.

The step-11 read "tool list AFTER = BEFORE + exactly 5" cannot see either change. Both are covered by this half, not by
that read.

## Guards

- **K1 -- the principal rosters' VALUE, the branch the ask does not cover.** The ask says the tiers are "unchanged in
  value", but only the roster SHAPE is checked: the host script refuses on a bad shape. The writer moves from the
  deploying shell (the Part D record) to `gateway/principals/rosters`. That is a predicted outcome, which never-widen
  forbids.
  - **Before the put and the act:** read on the host over SSM. Compare the sha256 of `MASTER_ADMIN_PRINCIPALS` and
    `WRITE_CAPABLE_PRINCIPALS` in the live `.env` with the same two values parsed from the secret. Print hashes or
    EQUAL/DIFFER only, never a value.
  - EQUAL: proceed.
  - DIFFER: STOP before any put or upload. A tier change is not in this radius and needs its own halves.
- **K2 -- order inside the act.** The cot token put happens only after 7a and K1 pass, immediately before the upload. A
  stop before the upload leaves the secret unrotated.
- **K3 -- base at upload.**
  - The act declares `DEPLOY_BASE_REF` = the live full sha `2c0f84966d...`.
  - The rollback declares the release sha.
  - If the live ref moves before upload, this half is VOID (the 7a re-read plus the script's guard).
- **K4 -- `HALT_ACK=1`** is used only after the halt gate's pending list reads 0 STOP lines. This is the MX-r-4
  precedent and is recorded in the ledger.
- **K5 -- read-back.** The ask's verify list stands:
  - `/health` returns 200;
  - the shipped md5 equals the release bytes;
  - tools AFTER = BEFORE + exactly 5;
  - `ENABLED_INTEGRATIONS` is unchanged;
  - `/ms/*` behaves as before;
  - on `/otp/health` the old cot value reads 401 and the new one 200;
  - `rl.AC1.sh`'s six negative arms are run.

  Add one more check: `mcportal` is still `a3bff71ffa` in `og-rel4` at the GO.

This half covers both branches of every leg in the ask's sections 2-4, plus the two tools added above. It does not cover
a moved base, a changed pin, a roster value that DIFFERs (K1), a deploy without the guard, or any Terraform, IAM, grant,
ALB or 49f-token change.

-- 3.0.0_SA_CVO~O
