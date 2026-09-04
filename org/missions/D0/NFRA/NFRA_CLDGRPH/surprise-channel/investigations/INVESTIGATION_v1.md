# NFRA_CLDGRPH -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, folder == project). Lane `ANY` (COO grant
@`bfec7d99b5`) -- the seat that sees it appends its own row; REMEDIATION rows stay `3.0.0_SA_CVO~A`'s.
**Append-only during the round.** Denominator at this write: **58 rows** (S1-S36 with id S11 vacated by the concurrent-append renumber, plus W1-S1..W1-S12 and W2-S1..W2-S11). **S35 -- `1.0.0_SA_CTO`'s row on the drain SWEEP, the mirror of S34 -- LANDED on CLOUD during this very merge**, which is why this header reads 58 where the issuer's first draft of it read 57: the count was written from a read taken minutes earlier and the union's own arithmetic (54 base + 2 ours + 2 theirs) corrected it before anything was committed. That is the header defect this file keeps filing against, caught on itself. Restated 2026-09-04 17:4xZ by `2.0.0_SA_COO~A` at the drain merge of wk-NFRA_CLDGRPH-1 (the reopened TO-CG-D-1) -- the FOURTH textual conflict of the round on this file and the fourth resolved the same way: the append-only UNION reconstructed from the three blobs (base 0df8682fa0, ours, theirs) rather than by editing the conflicted text, under the assertion that each side is exactly base-plus-an-appended-tail so no row can be touched by the resolution, plus the UNSCOPED control that the merged file removes exactly ONE line from base -- the old header. 54 base + 2 ours (S35 by `1.0.0_SA_CTO`, and W2-S11 landed at the D-3 drain) + 2 theirs (W1-S11, W1-S12) = 58, every id unique, no row edited, no id renumbered. THE FOUR CONFLICTS ARE THE EVIDENCE BEHIND NFRA_CLDGRPH-S36: `safe-merge.sh` aborts on exactly this conflict and takes its index guard and its row gate with it, and an append-only channel guarantees the conflict whenever two workers file rows concurrently. Prior restatement: **55 rows**, 2026-09-04 ~16:5xZ by `0.9.0_WK_NFRA_CLDGRPH~2` on appending W2-S11 at the TO-CG-D-3 drain (was 54); before that **54 rows**, 15:1xZ by `2.0.0_SA_COO~A` on appending S36 (was 53); **53 rows**, 14:1xZ at the wk-NFRA_CLDGRPH-2 drain union; **50 rows**, 14:0xZ at the wk-NFRA_CLDGRPH-1 drain union; **48 rows**, 12:5xZ on appending S34 (was 47), which restated the 09:5xZ union of the two worker branches at the first drain (was 39 after wk-NFRA_CLDGRPH-2's merge; the branch's own header read 40). Before that: restated 2026-09-04 09:15Z by `0.9.0_WK_NFRA_CLDGRPH~2` on appending W2-S7 (was 38, restated 2026-09-04 08:39Z by the same seat on appending W2-S1..W2-S6, the first WORKER-coordinate rows in this channel (was 32, restated 2026-09-04 07:0xZ by `2.0.0_SA_COO~A` on appending S32 + S33 (was 30, restated 2026-09-04 06:2xZ by `3.0.0_SA_CVO` on appending S31 (was 29; the CVO's own observation, filed here under lane ANY because a remediation row carries its item's id and the C- coordinate lives only in `../adjudications/`); before that restated 2026-09-03 19:55Z by `1.0.0_SA_CTO` on appending S30 (was 28); the count is restated by each appender because a stale denominator in a channel header is the same two-carrier defect the rows themselves are filed against.
`0.7.0_AE_CloudOps~Q` on the issuer's instruction (93402): the line still read **1 row** while the file held 9, so the
header understated the channel by 9 -- a denominator that ages silently is the defect this project keeps finding in
other carriers. Authorship is per-row in `surfaced_by`, never the header and never the committing author.
**Round 1 task orders:** two live -- `TO-CG-V-1` at `0.7.0_AE_CloudOps~Q`, `TO-CG-V-2` at `0.7.0_AE_CloudOps~P`.

## S1 -- the ADD-CHECKLIST grants on a role that does not exist

```json
[
  {
    "id": "NFRA_CLDGRPH-S1",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~P",
    "surfaced_at": "2026-09-03T07:12Z",
    "one_line": "NFRA_INTEGRATIONS_STANDARD.md s.5 step 4 -- the canonical 5-step ADD-CHECKLIST's IAM step -- instructs granting secretsmanager:GetSecretValue to `m365-mcp-gateway-role`, a role ABSENT from account 313476888478 (216 roles censused, 0 matches for 'm365'); the live gateway instance role is `opal-gateway-role`. Vacuous for AuthKind.NONE (no secret) so CG-s-5 is unharmed; ARMED for the next SHARED_SECRET integration built to the contract.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/architecture/NFRA_INTEGRATIONS_STANDARD.md:99-100 @a1af5d70c2 -- 's.5 step 4. **Grant IAM:** add `secretsmanager:GetSecretValue` on that exact secret ARN to the gateway instance role (`m365-mcp-gateway-role`) **via Terraform**.'",
        "APPLIED plane, docs/briefs/cmpaws-iam-census-20260903.json (comp-iam refresh-census, generated_utc 2026-09-03T06:46:12Z, iam:GetAccountAuthorizationDetails, account 313476888478): role DENOMINATOR 216; 'm365-mcp-gateway-role' ABSENT; roles matching 'gateway' = ['AWSServiceRoleForAPIGateway','opal-gateway-role']; roles matching 'm365' = [] (empty list, not a filtered zero -- the full name list was materialised and searched in-process)",
        "LIVE plane, aws ec2 describe-instances i-07dccb1615503ac99 (2026-09-03 ~06:5xZ): the gateway instance carries instance-profile-backed role `opal-gateway-role`; comp-find --corpus aws 'opal-gateway' (DB built 2026-09-03T00:36:15Z) shows INSTANCE_PROFILE `opal-gateway-profile` and IAM_ROLE `opal-gateway-role`, and NO m365 node",
        "DESIRED plane, comp-iam role opal-gateway-role -> tf_resource `gw`, source infra/aws/terraform/opal-gateway/main.tf, 10 statements -- the Terraform that actually declares the gateway role names it `opal-gateway-role`",
        "NEGATIVE CONTROL on the search itself: the same in-process scan over the same 216-name list returns 2 hits for 'gateway', so the 0 for 'm365' is an ABSENCE and not a broken read"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-V-2 section C scopes CG-s-13 to `registry.py` + `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md` and asks whether the 5-step checklist admits a read-only proxy integration with the framework unmodified -- treating the STANDARD as the accurate canonical contract for what a new integration must do.",
    "world_is": "The checklist's step 4 names a grant target (`m365-mcp-gateway-role`) that does not exist on the APPLIED plane; the real principal is `opal-gateway-role`. The checklist is answerable as asked for AuthKind.NONE only because steps 3-4 are SHARED_SECRET-scoped and therefore vacuous here -- the contract is wrong in a limb this project's cell does not traverse.",
    "notes": "Disarm = correct s.5 step 4 (and any sibling occurrence) to `opal-gateway-role`, or state why the legacy name is retained. Owner set to `1.0.0_SA_CTO~A` because docs/architecture is the ANY_CTO lane and CTO~A is this project's L4 owner; the DOCUMENT belongs to NFRA_INTEGRATIONS, so if 3.0.0_SA_CVO~A routes the remediation to that project instead, this row's owner assignment is superseded by that disposition -- surfaced, not adjudicated. NOT blocking TO-CG-V-2: all seven criteria are unaffected and CG-s-13's verdict does not depend on the misnamed role."
  }
]
```

## S2 -- the incremental engine's own docstring says it is gated OFF; its only caller defaults it ON

```json
[
  {
    "id": "NFRA_CLDGRPH-S2",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~Q",
    "surfaced_at": "2026-09-03T07:27Z",
    "one_line": "kuzu_incremental_refresh.py:27 says the incremental path is 'Gated OFF by default (GLOBGRPH_KUZU_INCREMENTAL_REFRESH=1) pending CTO arch-gate of the design', but its only caller _canonical.py:450 reads that flag with default '1' (ON), _canonical.py:431 documents it as DEFAULT-ON, and NFRA_KUZUSPLIT_PRD.md:22 records the CTO GO as landed ('LIVE default-on'). The engine -- the file a reader opens first -- is the stale carrier; CG-s-2 ports this engine.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/globgrph/kuzu_incremental_refresh.py:27 @aebe0d0a67 -- 'Gated OFF by default (GLOBGRPH_KUZU_INCREMENTAL_REFRESH=1) pending CTO arch-gate of the design.' Blob identity checked, not assumed: git rev-parse aebe0d0a67:<path> == git hash-object <worktree> == 3d33fad758a7d365a469d32f94f808a4ec9b7568, so the worktree read IS the read at the pin",
        "infra/aws/globgrph/_canonical.py:450 @173dd335f4 -- 'if os.environ.get(\"GLOBGRPH_KUZU_INCREMENTAL_REFRESH\", \"1\") != \"0\" and os.path.exists(db_path):' -- the default is \"1\", so absent the env var the incremental path RUNS",
        "infra/aws/globgrph/_canonical.py:431 @173dd335f4 -- 'DEFAULT-ON (GLOBGRPH_KUZU_INCREMENTAL_REFRESH defaults to \"1\"; set \"0\" to opt OUT -> full-only).' -- the caller's own docstring contradicts the engine's",
        "docs/architecture/NFRA_KUZUSPLIT_PRD.md:22 -- 'Andrew-directed 2026-07-08, CTO GO 195732Z, LIVE default-on, **92x faster (3.9s vs 356s)**' -- the arch-gate the engine docstring says is pending is recorded as GRANTED",
        "INSTRUMENT + DENOMINATOR: comp-read infra/aws/globgrph/_canonical.py --enumerate 'GLOBGRPH_KUZU_INCREMENTAL_REFRESH' -> 2 hit(s) across 746 lines / 41 sections scanned, 2 whole-value 0 substring, bands DOCSTRING=1 CODE=1. Both hits are quoted above, so the census is complete rather than sampled",
        "NEGATIVE CONTROL on the search: the same instrument over the same file for 'ensure_fresh|MUTEX_WAIT_S|ORPHAN_LOCK_S|INCREMENTAL_TIMEOUT_S|CANONICAL_DB_PATH' returns 26 hits, so the 2 is a real count and not a broken read"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-V-1 <compiler_tools_mandate> BEFORE WRITE directs `comp-read infra/aws/globgrph/kuzu_incremental_refresh.py --for \"where the full-fallback is triggered, what threshold flips it, and what the incremental path applies\"`, and AC1 requires the incremental entry point and the full-fallback trigger be cited from that read -- treating the engine's own text as the accurate description of the incremental path.",
    "world_is": "The engine's module docstring asserts the path is gated OFF by default pending a CTO arch-gate. Its only caller defaults the same flag ON, documents it as DEFAULT-ON, and the KUZUSPLIT PRD records that arch-gate as already granted. The description a reader meets first is the one that is wrong.",
    "notes": "Disarm = correct the kuzu_incremental_refresh.py module docstring to match _canonical.py:431/:450 and the landed CTO GO, or state why the engine deliberately describes a pre-GO world. Owner set to 2.0.0_SA_COO~A as this round's sequencer because the fix is a repo-source edit that THIS task order is explicitly barred from making; if 3.0.0_SA_CVO~A routes it into CG-s-2's port instead (the natural home -- 'a port is the moment to fix it or to consciously carry it'), that disposition supersedes this owner assignment. No measured value in TO-CG-V-1 depends on this row."
  }
]
```

## S3 -- a temp-path full load still takes a process-wide singleton lock; the TO's bound says it needs none

```json
[
  {
    "id": "NFRA_CLDGRPH-S3",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~Q",
    "surfaced_at": "2026-09-03T07:28Z",
    "one_line": "TO-CG-V-1 BOUNDS say a parallel temp-path run 'needs no lock'; true for _canonical.py's mkdir mutex (bypassed by direct invocation) but FALSE for kuzu_nessie_load.py's own singleton, whose _LOCK_PATH is keyed to the SCRIPT directory (:294) and acquired unconditionally before main() (:401) regardless of --db. EXERCISED: the FULL-1 measurement cleared a stale lock (dead pid 29220) and wrote its own pid 34684 at 07:10:08Z, so each full load serializes device-wide for its duration.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps~Q",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/globgrph/kuzu_nessie_load.py:294 @e445642c5f -- '_LOCK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), \".kuzu_nessie_load.lock\")' -- keyed to the SCRIPT dir, so it is invariant under --db. Blob identity checked: git rev-parse e445642c5f:<path> == git hash-object <worktree> == 8ed0108820852e4be03ee5a06647e4e17a4f251f",
        "infra/aws/globgrph/kuzu_nessie_load.py:401 @e445642c5f -- '_acquire_singleton_or_exit()' is called at __main__ scope, unconditionally, BEFORE main() parses or uses --db",
        "infra/aws/globgrph/kuzu_nessie_load.py:344-348 @e445642c5f -- a LIVE holder prints 'ERROR: REBUILD-ALREADY-RUNNING pid=<n>' and sys.exit(4); a stale (dead-holder) lock is removed and the exclusive create retried",
        "EXERCISED, both directions of the state change: at 07:01:28Z the lock held dead pid 29220 (written 06:49:08Z) -- absent from the Win32 process table, the SAME oracle the engine itself uses (_pid_running:265-291 OpenProcess + GetExitCodeProcess == STILL_ACTIVE), NOT the MSYS `ps` view which reads a different pid space; at 07:19Z, mid-run, the lock held pid 34684 == the measured loader process (Win32 CIM CommandLine confirms 'kuzu_nessie_load.py --db <scratchpad>/full1_db')",
        "NEGATIVE CONTROL on the liveness oracle: the same Win32 read returned ALIVE for pid 34684 while returning absent for 29220 in the same minute, so the 'dead' verdict is discriminating and not a broken probe"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-V-1 BOUNDS: 'The live local copy is not disturbed: temp path only; do not take or steal `_canonical.py`'s lock; do not kill any running rebuild (a rebuild in progress belongs to whoever started it -- wait it out or run to the temp path in parallel, which needs no lock).'",
    "world_is": "A temp-path run of kuzu_nessie_load.py DOES take a lock -- the loader's own script-directory-keyed singleton, unconditionally and independently of --db. The bound is correct about _canonical.py's mkdir mutex (which a direct invocation never touches) and wrong about the loader's singleton, so 'run to the temp path in parallel' is not lock-free as written.",
    "notes": "Disarm = this seat's two AC2 full loads completing (the engine releases the singleton in a finally at :412; the deadline watchdog at :395-401 also releases before os._exit). Recorded rather than worked around because the alternative -- not measuring -- forfeits the cell. NO seat's rebuild was killed and _canonical.py's mutex was never touched by this seat: the stale lock this run cleared was cleared BY THE ENGINE'S OWN dead-holder path, not by hand. Consequence worth carrying into CG-s-2: a cloud worker built from this engine inherits a singleton whose scope is the deployment unit, which is a different concurrency story from one lock per DB."
  }
]
```

## S4 -- two orphaned local rebuilds left mutex + tmp + WAL residue inside 40 minutes, both before this seat ran

```json
[
  {
    "id": "NFRA_CLDGRPH-S4",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~Q",
    "surfaced_at": "2026-09-03T07:29Z",
    "one_line": "Two distinct local rebuild attempts left _canonical mkdir-mutex + tmp + WAL residue inside 40 minutes (mutex observed 06:49:01Z, re-created 07:05:32Z; each tmp/WAL stopped growing within ~40s) with no kuzu process alive at either observation, while _refresh_status.json recorded 'inc-served-labeled-stale, behind-by-27133 nodes' at 06:48:52Z. Both predate this seat's first run (07:10:05Z). WHY they died is NOT established here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/globgrph/kuzu_nessie_db.rebuild.lock -- directory present at 07:01:28Z with mtime 06:49:01Z; present again at 07:23:38Z with mtime 07:05:32Z (a DIFFERENT, later attempt, so this is two events and not one lingering one)",
        "infra/aws/globgrph/kuzu_nessie_db.rebuild.tmp / .rebuild.tmp.wal -- WAL 8,562,878 B mtime 06:49:39Z at the first observation; 6,757,865 B mtime 07:06:11Z at the second: growth stopped ~38s and ~39s after each mutex creation",
        "infra/aws/globgrph/kuzu_nessie_db._refresh_status.json -- {\"failed_at_iso\": \"2026-09-03T06:48:52.030129+00:00\", \"kind\": \"inc-served-labeled-stale\", \"detail\": \"behind-by-27133 nodes; served vintage 2026-09-03T00:36:15.576756+00:00; mode=inc\"} -- the incremental tripped the large-delta gate and handed off to a full reload immediately before the first residue",
        "Win32 process table at 07:01:28Z and 07:23:38Z: zero processes whose CommandLine matches kuzu_nessie_load / kuzu_incremental_refresh other than this seat's own measured run (pid 34684, created 07:10:07Z)",
        "TIMING CONTROL: both mutex events precede this seat's first invocation at 07:10:05Z, so neither was caused by this task order; and this seat's direct invocation never touches the mkdir mutex at all (that lock is _canonical.py's, and _canonical is not in this seat's call path)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-V-1's GO names the L7 first act as re-grounding the task order's premises against live state, explicitly including 'the current lock state', and the BOUNDS anticipate at most a single rebuild in progress belonging to another seat ('wait it out').",
    "world_is": "The live lock state was not one rebuild in progress but the residue of two that had already died, plus a stale loader singleton whose holder pid was absent from the Win32 process table. Nothing needed waiting out.",
    "notes": "INERT because the engine has a designed backstop for exactly this: ORPHAN_LOCK_S=900s absolute steal (_canonical.py:47, :672), a stale-heartbeat steal at HEARTBEAT_STALE_S=90s when liveness is enabled, and TMP_GC_AGE_S=1800s for tmp residue -- and the 07:05:32Z re-creation is consistent with the backstop having worked on the 06:49:01Z one. Surfaced because the decomp records that the engine CG-s-2 ports 'now carries CE-G-5's behaviour (no orphaned rebuild; serve-stale-immediately with the age)' @173dd335f4, landed 2026-09-03T05:14:58Z -- under two hours before these observations. This seat is NOT asserting that contradicts CE-G-5: serve-stale-immediately plainly DID happen (that is what _refresh_status.json records), and 'no orphaned rebuild' may name the serve behaviour rather than zero filesystem residue. Establishing which is a read this task order has no mandate to make."
  }
]
```

## S5 -- V2-AC7's cell_refs are space-separated; the checker splits on comma, so the instance cannot reach rc 0

```json
[
  {
    "id": "NFRA_CLDGRPH-S5",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~P",
    "surfaced_at": "2026-09-03T07:31Z",
    "one_line": "TO-CG-V-2's own V2-AC7 face writes cell_refs SPACE-separated (\"CG-s-11 CG-s-12 CG-s-13\"); proof-of-spec-check.py:562 splits cell_refs on COMMA only, so the whole attribute is read as one phantom cell id that matches none of the decomp's 19 -- the instance is INVALID (rc 1) on that one row and V2-AC7 cannot be satisfied until the issuer amends the face. 1 of 842 cell_refs attributes estate-wide is space-separated; 282 are comma-separated, so this is a single typo against an established convention, NOT a checker defect.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/proof-of-spec-check.py:562 @c765283365 -- 'refs = [c.strip() for c in attrs.get(\"cell_refs\", \"\").split(\",\") if c.strip()]'. VERIFIED NOT IN THE DIRTY DELTA: the checker self-reports 'checker-vintage: c765283365 +DIRTY(8 lines)', so the line was read at the commit via `git show c765283365:.tools/proof-of-spec-check.py` and is BYTE-IDENTICAL to the worktree line -- the cite does not depend on uncommitted changes",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-V-2.reachability-iam-authkind-verified.md:46 @d0c21677c7 -- '<criterion id=\"V2-AC7\" cell_refs=\"CG-s-11 CG-s-12 CG-s-13\"/>' (spaces, no commas)",
        "checker output on the instance: 'VIOLATION: alignment: cell_ref CG-s-11 CG-s-12 CG-s-13 (cited by [V2-AC7]) does NOT exist in .../NFRA_CLDGRPH_DECOMP.md'; 'alignment-forward-2 (cell_ref -> decomp): 3/4 distinct cell_ref(s) resolve'; final verdict INVALID (rc=1). This is the SOLE remaining violation -- the other two (PENDING-COMMIT tokens) were this seat's and are fixed",
        "POSITIVE CONTROL that the parser works and only the separator is wrong: V2-AC1..V2-AC6 all carry single-cell cell_refs and all resolve; 'alignment-backward: 3/3 cell(s) declared in the TO's <owned_cells> are reachable from >=1 criterion', so the DECLARED cell set is correct and only its ENCODING on one row is not",
        "CONVENTION CENSUS over every cell_refs attribute on every task-order face under org/ -- DENOMINATOR 842: 559 single-cell, 282 COMMA-separated (parse correctly), 1 SPACE-separated. The single space-separated instance is this TO's V2-AC7. So the estate's convention is commas at 282 instances and this is one typo, not a systemic gap"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "V2-AC7 requires 'the proof instance VALID (`.tools/proof-of-spec-check.py` rc 0) with every `surprises` entry resolving to a row BEFORE the complete flip, which this seat commits itself.'",
    "world_is": "The instance cannot reach rc 0 by any act available to the ASSIGNEE, because the failing token is on the TO's ISSUANCE half (the <criterion> declaration), not in the instance. The checker's own comment at :328 states 'NOTHING HERE IS DERIVED. cell_refs are read as DECLARED in the TO's issuance half.' All seven criteria are otherwise measured and PASS.",
    "notes": "DISARM = the issuer changing V2-AC7's cell_refs to comma-separated ('CG-s-11, CG-s-12, CG-s-13') on the TO face. The declared cell SET does not change, so this is an encoding correction, not a scope change to a frozen spec. THIS SEAT DELIBERATELY DID NOT MAKE THAT EDIT despite task-orders/** being lane ANY: the TO's own BOUNDS say 'Certifier != author: this seat measures and files; the grade is the L8-L10 seat's on the record', and V2-AC7 is the criterion this seat is graded against -- an assignee editing its own acceptance declaration is the author touching the grading instrument, which is the separation that bound exists to protect. Routed to the issuer in the same turn per the TO's BOUNDS ('A BLOCKING row also goes to the issuer in the same turn'). Everything else in TO-CG-V-2 is complete: A/B/C/D measured, all controls fired, <status> HELD at pending pending this one-token amendment."
  }
]
```

## S6 -- DISARM ACK for S5 (the issuer amended the face in-round; the instance is now VALID)

```json
[
  {
    "id": "NFRA_CLDGRPH-S6",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~P",
    "surfaced_at": "2026-09-03T07:48Z",
    "one_line": "DISARM ACK for NFRA_CLDGRPH-S5: the disarm owner 2.0.0_SA_COO~A amended V2-AC7's cell_refs to comma-separated in-round; proof-of-spec-check.py now returns VALID (rc=0), violations=0, 3/3 cell_refs resolving. S5's blocking condition is GONE IN THE WORLD -- its L9 disposition remains 3.0.0_SA_CVO~A's to set, which this row does not do.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO face now reads '<criterion id=\"V2-AC7\" cell_refs=\"CG-s-11, CG-s-12, CG-s-13\"/>' (commas); the <status> field carries the issuer's own amendment note naming NFRA_CLDGRPH-S5 as the row being disarmed, 'encoding only ... the declared cell set CG-s-11/12/13 is unchanged, no criterion text changed, the spec stays frozen'",
        "MEASURED at this seat AFTER the amendment: `python .tools/proof-of-spec-check.py org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~P/NFRA_CLDGRPH.TO-CG-V-2.reachability-iam-authkind-verified.proof_of_spec.json` -> 'violations=0', 'alignment-forward-2 (cell_ref -> decomp): 3/3 distinct cell_ref(s) resolve', 'alignment-backward: 3/3', 'surprises-frame: 2 entries; 2 resolve to a channel row', VALID (rc=0)",
        "NEGATIVE CONTROL on the amendment's scope, so 'encoding only' is verified and not taken on report: `git diff` on the TO shows exactly 2 changed lines -- the <status> prose and the V2-AC7 cell_refs attribute. No criterion TEXT changed, <expected_criteria> is unchanged, and the decomp cell set named is identical, so the frozen spec was not widened or narrowed",
        "The DISARM was performed by the row's own declared disarm_owner (2.0.0_SA_COO~A), not by the surfacing seat -- author/owner separation preserved on both halves"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_CLDGRPH-S5 asserted that V2-AC7's validity limb could not be satisfied by any act available to the assignee while the TO face carried space-separated cell_refs, and named 2.0.0_SA_COO~A as disarm_owner.",
    "world_is": "The disarm landed in-round: the face is comma-separated, the checker returns rc 0, and the blocking condition no longer exists. Recorded as a NEW row because the channel is append-only -- S5's own text stands unedited.",
    "notes": "This row is a FACTUAL disarm acknowledgement, NOT an adjudication: it deliberately omits `adjudicates` so it does not set S5's disposition. Per CLAUDE.md s.2 remediation rows stay CVO's, and the L9 disposition of S5 (and of ~Q's S2/S3/S4) is 3.0.0_SA_CVO~A's act on the record at L8. A reader resolving S5's live state should read THIS row for the world-state and wait on the CVO for the disposition."
  }
]
```

## S7 -- DISARM ACK for S1 (the disarm owner corrected the canonical integration contract in-round; six tokens of one cutover)

```json
[
  {
    "id": "NFRA_CLDGRPH-S7",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO~A",
    "surfaced_at": "2026-09-03T07:54Z",
    "one_line": "DISARM ACK for NFRA_CLDGRPH-S1 by its disarm_owner: docs/architecture/NFRA_INTEGRATIONS_STANDARD.md v1.3.1 @f9ca7a9309 -- the s.5 step-4 grant principal corrected m365-mcp-gateway-role -> opal-gateway-role, plus the five sibling occurrences of the same 2026-08-14 cutover in that file (three code-tree paths, the s.9.1 venv host, the G4 DESIRED-plane instrument comp-iam service -> comp-iam role). 6 of 6 stale tokens; 0 remain in operative text; no semantic change. S1's hazard is GONE IN THE WORLD; its L9 disposition remains 3.0.0_SA_CVO~A's, which this row does not set.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "docs/architecture/NFRA_INTEGRATIONS_STANDARD.md @f9ca7a9309 (author 1.0.0_SA_CTO~A, lane ANY_CTO; ~A admitted -- measured with .tools/owned-paths-validate.py --check-agent before the edit, rc 0; a worker serial on the same path REFUSED as the negative control): s.5 step 4 now reads 'to the gateway instance role (`opal-gateway-role`) **via Terraform**'; s.10 carries the v1.3.1 change-control paragraph naming the cutover, the six tokens, the surfacing row and the confirmer",
        "EXTENT, before and after, one instrument: comp-read docs/architecture/NFRA_INTEGRATIONS_STANDARD.md --enumerate 'm365-mcp-gateway-role|opal-gateway-role|m365-mcp-gateway' BEFORE -> 6 hits across 261 lines / 52 sections (lines 14, 16, 100, 166, 195, 259); the same instrument on 'm365-mcp-gateway' AFTER -> 2 hits across 273 lines, BOTH inside the v1.3.1 paragraph's own historical citation (lines 258, 261); 0 in operative text. 'opal-gateway-role|infra/aws/ec2/opal-gateway/' AFTER -> 8 hits",
        "THIRD INSTRUMENT on the principal, DESIRED plane (the worker used the APPLIED census, 3.0.0_SA_CVO~A the aws corpus): `comp-iam role opal-gateway-role` returns the role's statements incl. secretsmanager:GetSecretValue; `comp-iam service m365-mcp-gateway` answers 'No service matching' (an EC2 gateway is not a Lambda service under either name -- why G4's instrument was changed verb, not only name; the stale G4 line produced a loud absence, not a false zero, so that sibling was INERT)",
        "PATHS: infra/aws/ec2/m365-mcp-gateway/ ABSENT; infra/aws/ec2/opal-gateway/ PRESENT with INTEGRATION_FRAMEWORK.md and app/integrations/ under it (test -d / test -f at this seat 07:3xZ)",
        "SCOPE ACCEPTED by the L9 seat before this row: 3.0.0_SA_CVO~A 93316 item 4 -- 'sibling occurrence was NOT meant narrower than the file ... Correcting all six tokens of the same 2026-08-14 cutover in that file is the right read'; the G4 verb change 'correctly flagged ... and was INERT'",
        "ORDERING, stated: the disarm commit @f9ca7a9309 (07:4xZ) preceded the channel file's own first commit @9b59f39114 (0.7.0_AE_CloudOps~P, 07:5xZ); this ack row is appended on the file's first committed state rather than into the worker's uncommitted worktree, so the worker's rows land under the worker's author line and this one under its own"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_CLDGRPH-S1 notes: 'Disarm = correct s.5 step 4 (and any sibling occurrence) to `opal-gateway-role`, or state why the legacy name is retained. Owner set to `1.0.0_SA_CTO~A` because docs/architecture is the ANY_CTO lane and CTO~A is this project's L4 owner.'",
    "world_is": "The disarm landed in-round at the named owner: the standard names the live principal on its step-4 line and the five sibling tokens of the same rename are corrected with it; the legacy name is retained nowhere except as the quoted history in the change-control paragraph. Recorded as a NEW row because the channel is append-only -- S1's own text stands unedited.",
    "notes": "This row is a FACTUAL disarm acknowledgement, NOT an adjudication: it deliberately omits `adjudicates` so it does not set S1's disposition (3.0.0_SA_CVO~A 93326 item 2: the adjudicates carrier is the L9 seat's column). DISARMED is not REMEDIATED: whether the round's L10 slug has anything left to route for S1 is 3.0.0_SA_CVO~A's read (its provisional L9 in 93326: DISMISSED_WITH_REASON under the spine v2.4 outside-remedy reading, exit (i)). The one instrument gap this seat states against itself: comp-read's extent count is a substring count on one file; the 6-of-6 is the count of tokens in THIS file, not a claim about the 8,764-hit repo-wide 'm365' population, which 3.0.0_SA_CVO~A bounded as NOT claimed clean."
  }
]
```

## S8 -- the full loader's `_build_manifest.edge_count` overstates the graph's real edge count by 2,256

```json
[
  {
    "id": "NFRA_CLDGRPH-S8",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~Q",
    "surfaced_at": "2026-09-03T07:55Z",
    "one_line": "kuzu_nessie_load.py stamps _build_manifest.edge_count with its MERGE-ATTEMPT count (60,688), not the graph's stored edge count (58,432) -- an overstatement of 2,256 (3.9%) reproduced identically by two independent full loads, while node_count (27,133) agrees exactly and the INCREMENTAL path writes the correct 58,432 for the same graph. The manifest is the provenance record CG-s-3 ports to S3 and CG-s-7 repoints comp-graph status at.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, independent instrument (direct Cypher against the built DB, NOT either engine's own counter): kuzu.Database(full1_db, read_only=True) -> 'MATCH ()-[r:CloudEdge]->() RETURN count(*)' = 58432; same query on full2_db = 58432",
        "The manifests those same two runs wrote: full1_db._build_manifest.json and full2_db._build_manifest.json both carry edge_count=60688, node_count=27133 -- so node_count agrees with the query (27133==27133) and edge_count does not (60688 != 58432, delta 2256)",
        "PRODUCER-SIDE ARITHMETIC that explains it, from the loader's own stdout: 'INFO: ICEBERG_READ nodes=27156 edges=61071' then 'INFO: EDGES_WRITTEN written=60688 skipped_missing_endpoint=383' -- 61071-383 = 60688 exactly, i.e. the field counts MERGE statements executed, and MERGE is idempotent on a repeated (src,dst,edge_type,props) identity",
        "CROSS-PRODUCER CONTROL: the incremental engine's manifest for the same graph (incB_db._build_manifest.json) carries edge_count=58432 -- it stamps a post-apply 'MATCH ()-[e:CloudEdge]->() RETURN count(*)' (kuzu_incremental_refresh.py:227-228) rather than a write counter, so two producers of ONE field disagree by construction",
        "REPRODUCIBILITY: the discrepancy is identical (2256) across two runs 21 minutes apart that produced byte-identical output DBs (46,994,310 B each, same nodes_snapshot_id 1242378212505298814 / edges_snapshot_id 1026441646305052092), so it is deterministic and not a race",
        "NEGATIVE CONTROL that the query instrument is sound: the SAME Cypher session returned nodes=27133, which MATCHES the manifest's node_count -- a broken reader would not agree on one field and disagree on the other"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-V-1 AC2 requires each full load's INPUT SIZES be reported as 'node and edge row counts per table', and the deliverable to identify what a 'projection rebuild' means in each carrier -- treating the build manifest the loader writes as an accurate description of the artifact it stamps.",
    "world_is": "The loader's manifest edge_count is a count of write attempts, not of edges in the artifact. Reporting it as the graph's edge count would have put a 2,256-edge phantom into this deliverable's own input-size table; the correct stored count is only visible by querying the DB or by reading a manifest the INCREMENTAL path wrote.",
    "notes": "Disarm = make the full loader stamp a post-load COUNT(*) the way kuzu_incremental_refresh.py:227-228 already does, or rename the field to say it is a write count. Owner set to 2.0.0_SA_COO~A as this round's sequencer because the fix is a repo-source edit this task order is barred from making; the natural home is CG-s-9/R10 ('the port is the moment') or CG-s-3, which defines the artifact manifest contract -- 3.0.0_SA_CVO~A routes it at L8. This deliverable reports BOTH numbers with their producers named rather than picking one. NOT blocking: no duration or memory figure in TO-CG-V-1 depends on the edge count."
  }
]
```

```json
[
  {
    "id": "NFRA_CLDGRPH-S9",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~A",
    "surfaced_at": "2026-09-03T08:32Z",
    "one_line": "L10 STAMP, round 1: the CVO's adjudication of the five items this slug does NOT graduate. S1, S4, S5, S6 and S7 are DISMISSED_WITH_REASON, each reason given and each grounded on a read this seat made itself rather than on the surfacing seat's instrument. S2, S3 and S8 are GRADUATED by the remediation rows bearing their ids in REMEDIATION_v1.md, landed in this same commit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_CLDGRPH-S1",
      "NFRA_CLDGRPH-S4",
      "NFRA_CLDGRPH-S5",
      "NFRA_CLDGRPH-S6",
      "NFRA_CLDGRPH-S7"
    ],
    "spec_asserts": "The spine's L10 precondition asserts that every task order under the project is terminal, each finished with a valid proof-of-spec instance whose surprises entries resolve to rows, and that every investigation item under the project is dispositioned before any route-carrying row is admitted -- and the L9 output clause asserts that the round's remediations issue as ONE slug at L10, one artifact and one moment, never as a stream of messages during L7 to L9.",
    "world_is": "Both conditions hold as asserted and this seat measured them rather than accepting them on report: both faces read complete at HEAD and both instances re-exercised VALID here, with the coverage limb the checker delegates to the certifier run by this seat at 6/6 and 7/7 exact. The one thing the spec did not anticipate is procedural and is recorded rather than worked around: this row IS the adjudication half of that single slug, so it must land in the same commit as the remediation rows it enables, because the gate's census reads the index and a route-carrying row is refused while any item is undispositioned. The two halves therefore cannot be split across commits, and this row carries no route of its own.",
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S1 (the ADD-CHECKLIST grant on a role that does not exist): DISARMED IN PLACE by its declared disarm_owner 1.0.0_SA_CTO~A at docs/architecture/NFRA_INTEGRATIONS_STANDARD.md v1.3.1 @f9ca7a9309, within that seat's own ANY_CTO lane. Under the spine v2.4 outside-remedy reading this is lawful exit (i), whose test is whether THIS project still owes a cell or a task order. It does not: the defect was vacuous for AuthKind.NONE, CG-s-5 was never harmed, and the contract is now correct. Verified by this seat with a DIFFERENT reader than the row used (python over git show f9ca7a9309:<path>): 2 occurrences of the legacy name remain, both inside the v1.3.1 change-control paragraph as quoted history, 0 in operative text; the corrected principal sits on the step-4 line. SCOPE NOTE this seat states against its own earlier bound: it had bounded the defect at 1 of 1 on the architecture surface for the exact role token, which was NARROWER than the row's own remedy asked; correcting all six tokens of the one 2026-08-14 cutover was the better read, because a half-renamed canonical contract still misleads the next author at a different line. Nothing routes. || S4 (rebuild residue with no live processes): NO DEFECT ESTABLISHED. The surfacing seat correctly declined to say whether it contradicts CE-g-5 and named that as beyond its mandate. This seat's L9 read: it does NOT contradict it -- CE-g-5's claim at its own commit @173dd335f4 is that rebuild children run under a KILL_ON_JOB_CLOSE job object, a claim about PROCESSES; filesystem residue is swept by ORPHAN_LOCK_S 900s and TMP_GC_AGE_S 1800s, different and slower mechanisms. THIS SEAT'S REASON IS RESTATED FROM ITS FIRST FORM AND THE CHANGE IS EVIDENCE, NOT OPINION: it first held the observation NON-DISCRIMINATING in both directions, because zero live processes looks identical to a normal exit. 3.0.0_SA_CVO read an artifact this seat had not -- kuzu_nessie_db.fallback.jsonl, whose completion-path entries are absent across both residue windows -- establishing that both PARENTS died mid-child rather than exiting. An abruptly killed parent leaves its child running unless something reaps it, so with that premise the observation IS discriminating and points toward the process claim having held. The first reading was sound on the evidence this seat had, and no care inside its own instrument would have closed the gap; it took a peer reading a different artifact. Disposition unchanged, reason corrected on the record rather than left standing. Still unestablished and deliberately not chased: what killed the two parents; client-side by construction, and the discriminator is the killed client's log, not the engine's. S4 is INERT and its timing control already excludes TO-CG-V-1. Nothing routes. || S5 (V2-AC7's space-separated cell_refs refused by a comma-only split): DISARMED IN PLACE by its declared disarm_owner 2.0.0_SA_COO~A @ee7c884f29, encoding only -- the declared cell set and every criterion's text unchanged, so the frozen spec was not touched. Verified by this seat at HEAD: the record carries the comma-separated form and the task-orders path is clean in the worktree. THIS SEAT RECORDS TWO THINGS AGAINST ITSELF HERE. (a) Its own convention census returned 0 space-separated against the row's 1 and appeared to refute it; the census read the WORKTREE after the amendment while the row was pinned to its commit, so both counts were right on their own plane and the seat that erred was this one -- it nearly used a live read to contradict a correct claim, which is the DESIRED-versus-APPLIED trap inside its own instrument. (b) It then raised an uncommitted-amendment hazard demanding an ordering; the hazard was real but ALREADY OVERTAKEN, the issuer's commit having landed before the message was sent. This seat prevented nothing and claims nothing. Nothing routes. || S6 (disarm ack for S5) and S7 (disarm ack for S1): FACTUAL ACKNOWLEDGEMENTS asserting no defect of their own and naming no remedy. Both correctly omitted adjudicates so that neither set the disposition of the item it acknowledged, leaving that column to this seat; that restraint is why the channel still resolves cleanly. Nothing routes for either.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRECONDITION verified at this seat and not taken on report: git show HEAD:<face> reads <status>complete for BOTH task orders; proof-of-spec-check re-exercised here at checker-vintage 2bc3679e0b -- TO-CG-V-1 VALID rc 0 (violations 0, 4 artifacts resolved at pin, surprises 4/4) and TO-CG-V-2 VALID rc 0 (violations 0, 2 PENDING co-committed at 9b59f39114, surprises 2/2)",
        "COVERAGE STEP-ZERO, the limb the checker delegates to the certifier in its own output (no expected_criterion_ids given -- COVERAGE UNCHECKED ... the cert consumer runs step-zero): run by this seat on both instances. TO-CG-V-1 expected V1-AC1..V1-AC6 vs present V1-AC1..V1-AC6 = 6/6, zero missing, zero extra. TO-CG-V-2 expected V2-AC1..V2-AC7 vs present V2-AC1..V2-AC7 = 7/7, zero missing, zero extra. An omitted criterion is invisible to every automated rung in the chain and visible only at this read",
        "S1 disarm re-read with a DIFFERENT reader than the disarming seat used (python over git show f9ca7a9309:docs/architecture/NFRA_INTEGRATIONS_STANDARD.md, 274 lines): m365-mcp-gateway occurrences = 2, both at L258/L261 inside the v1.3.1 change-control paragraph's own historical citation; opal-gateway-role at L100 (the corrected step-4 principal), L166, L261, L263",
        "S5 disarm verified at HEAD by this seat: the record carries the comma-separated cell_refs and git status --porcelain on the task-orders path is empty, so the amendment is committed and not a worktree intention",
        "S4's discriminator is 3.0.0_SA_CVO's read of infra/aws/globgrph/kuzu_nessie_db.fallback.jsonl (36 lines; entries 06:47:28Z, 06:47:59Z, 06:48:52Z, then nothing until 07:26:35Z, with both residue windows inside that silence) and is CARRIED AS THAT SEAT'S at that seat's vintage, not re-derived here -- stated so the reader knows which seat's instrument bears the weight",
        "ROUTE-MAP READING APPLIED: 1.0.0_SA_CTO's spine v2.4 clause -- the route enum answers what the remedy needs that does not exist yet in THIS project's chain; a remedy lying outside it is not routed but dispositioned, via disarm in place (exit i) or a brief opening the owning project (exit ii). S1 took exit (i)",
        "NEGATIVE CONTROL on this seat's ancestry probes throughout: the reverse is-ancestor direction was run and returned NOT-ancestor each time, so the probes discriminate rather than answering yes to everything"
      ]
    },
    "notes": "This row is the L10 STAMP's adjudication half and carries NO route, so it is not route-carrying under either shape and does not itself need the precondition it attests. The three graduated items take their disposition from the remediation rows bearing their ids in REMEDIATION_v1.md, landed in this same commit -- the gate's census reads the index, so one slug is one act. DISCLOSURE for any reader using the rollup: comp-surprise resolves dispositions by latest carrier as of @2bc3679e0b, so this round reads closed there; on an older vintage it would read OPEN and ARMED despite the adjudication, and that must not be taken as this round failing to close. This seat is NOT the grader of realization: the outcome grades at the close are 1.0.0_SA_CTO~A's against the exercised artifacts, and the coverage report is 2.0.0_SA_COO~A's."
  }
]
```

## S10 -- the rebuild deadline watchdog's stated "5x headroom" is 1.8x against the measured duration, and the port inherits it

```json
[
  {
    "id": "NFRA_CLDGRPH-S10",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~Q",
    "surfaced_at": "2026-09-03T09:05Z",
    "one_line": "kuzu_nessie_load.py:389-393 defaults KUZU_REBUILD_DEADLINE_S to 1800 s and justifies it in-source as '5x headroom' over 'a full rebuild is ~6min' -- the same figure CG-s-10 measured and falsified. Against the measured 935.500-1001.172 s the real headroom is 1.80x, not 5x. Not failing today; ARMED for the cloud port, whose duration is UNMEASURED and whose watchdog exit is os._exit(3) mid-build, not a graceful degrade.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps~Q",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/globgrph/kuzu_nessie_load.py:389-393 @e445642c5f -- the comment 'Hard-exit past KUZU_REBUILD_DEADLINE_S (default 1800s; a full rebuild is ~6min, so 5x headroom)' and the code '_deadline_s = int(os.environ.get(\"KUZU_REBUILD_DEADLINE_S\", \"1800\"))'. Blob identity checked: git hash-object of the worktree == 8ed0108820852e4be03ee5a06647e4e17a4f251f == the blob at the pin, so this is the read at the pin",
        "MEASURED CONTRADICTION, this seat's own runs at a9aea6f3ce: FULL-1 1001.172 s and FULL-2 935.500 s, 2 of 2, run-to-run spread +/-3.39%. 1800/1001.172 = 1.798x and 1800/935.500 = 1.924x, so the headroom is 1.80x at the worst measured run against a stated 5x",
        "ARITHMETIC THE COMMENT ASSERTS: 5x headroom over ~6 min implies a deadline sized for a ~360 s rebuild (5 x 360 = 1800). The 1800 s constant is therefore DERIVED from the ~6 min figure, not independently chosen -- which is what makes it a carrier of the falsified figure rather than a coincidence",
        "infra/aws/globgrph/kuzu_nessie_load.py:395-401 @e445642c5f -- _deadline_exit prints REBUILD-DEADLINE-EXCEEDED, calls _release_singleton() and then os._exit(3); the comment states os._exit rather than sys.exit is deliberate because a thread blocked in a native Arrow S3 read ignores normal interpreter shutdown. So the failure mode is a hard kill mid-build",
        "NEGATIVE CONTROL on the claim that nothing is failing today: 1800 s DOES exceed both measured runs, and both exited rc=0 with the watchdog armed -- so this row is about MARGIN, not about an observed failure, and says so"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-B-2 B2-AC1 requires the runtime decision to carry 'the memory size with the measured peak beside it' and the visibility timeout '>= the longest step that holds the message, with the number', i.e. every runtime bound derived from CG-s-10's measurements rather than from a document claim (PRD s.6 R5).",
    "world_is": "One runtime bound the worker inherits -- the engine's own rebuild deadline -- is still derived in-source from the ~6 min document figure that CG-s-10 falsified, giving 1.80x headroom where the code claims 5x. It is inherited silently by any caller that does not set the env var, including a task definition written from the face without reading :389.",
    "notes": "Disarm at this port = set KUZU_REBUILD_DEADLINE_S explicitly in the projection task definition from the measured number with the headroom stated in the runtime decision, and re-check it against B2-AC6's CLOUD measurement once that exists (the cloud number is the one the sizing may rest on). The ENGINE-side fix -- re-deriving the default and correcting the comment -- is NOT taken here: this task order's four named fixes are S9, S2, S3 and S8, and quietly widening that set is the scope drift the round-2 face forbids. Surfaced so a later caller does not inherit a stale justification; 3.0.0_SA_CVO~A routes it."
  }
]
```

## S13 (filed as S11; renumbered on a same-minute id collision with ~Q -- see notes) -- the tree cannot produce the adds-only plan B1-AC3 requires, and a bare apply would land an Andrew-EXCLUDED SNS email subscription

```json
[
  {
    "id": "NFRA_CLDGRPH-S13",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~P",
    "surfaced_at": "2026-09-03T09:15Z",
    "one_line": "TO-CG-B-1 B1-AC3 requires an adds-only plan (0 change / 0 destroy) and a 0-diff re-plan, but the globgrph tree CANNOT produce either: a module-wide plan reads 'Plan: 8 to add, 2 to change, 0 to destroy' of which 4 are FOREIGN committed-but-never-applied drift, including aws_sns_topic_subscription.critical_surface_alerts_email to andrew@opalinvest.com -- a resource recorded as an EXPLICIT Andrew EXCLUSION that must not land. NOT APPLIED. Deploy ledger left OPEN/RED (hold correctly refused while an apply leg is open); issuer ruling needed on a -target scoped apply.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform plan -input=false -no-color in infra/aws/terraform/globgrph at 2026-09-03 ~09:0xZ (init OK, validate Success, fmt clean): 'Plan: 8 to add, 2 to change, 0 to destroy'. Enumerated by address: MINE 6 of 6 exactly as the face specifies (aws_sqs_queue.globgrph_projection_events, .globgrph_projection_events_dlq, aws_sqs_queue_policy.globgrph_projection_events, aws_s3_bucket_notification.globgrph_warehouse_marker, aws_iam_role.globgrph_projection_worker, aws_iam_role_policy.projection_worker_sqs) -- all 'will be created'. FOREIGN 4: aws_glue_partition.tool_activity[\"rolling_log\"] and [\"rolling_log_summary\"] updated in-place (adding a frozen_by_retirement parameter), aws_glue_partition.tool_activity[\"routing\"] created, aws_sns_topic_subscription.critical_surface_alerts_email created",
        "THE FOREIGN CHANGES ARE NOT UNCOMMITTED PEER EDITS -- they are COMMITTED DESIRED text never applied. MEASURED: git status --porcelain infra/aws/terraform/globgrph/ returns exactly ONE line, '?? projection.tf' (this seat's own new file). Declaring commits: item2c_surface_alarm.tf @446f00ecaf (0.7.0_AE_CloudOps, 2026-06-17); tool_activity.tf @981719334a (0.8.0_AE_CloudComp, 2026-08-21). So the tree has carried unapplied DESIRED drift for up to ~2.5 months -- CLAUDE.md Rule 22a's DESIRED != APPLIED axis, concrete",
        "THE SNS SUBSCRIPTION IS A RECORDED ANDREW EXCLUSION, not merely unowned: org/tier2_senior/0.7.0_AE_CloudOps/deliverables/ZGATES_PREFLIGHT_VERIFIED_20260714.md:37 -- 'THE EXCLUSION (must NOT land): aws_sns_topic_subscription.critical_surface_alerts_email'; org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-07-14/session_0816-0900Z_Z-gate-opener_gateA-image_gateB-fedobs-producer.md:119 -- 'NOT touched (by design) ... (excluded per Andrew'; 3.0.0_SA_CVO~Z's 2026-07-14 cert log flagged the same module-wide-apply hazard as a P1 apply-leg flag, naming item2c_surface_alarm.tf:30 and the endpoint andrew@opalinvest.com",
        "AN ESTABLISHED HANDLING CONVENTION EXISTS AND IS NOT THIS SEAT'S TO INVOKE UNASKED: org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-06-22/datemode_b_backfill_executed_plus_f1_email_reapply.md:31 records 'safe-apply.sh globgrph -target=critical_surface_alerts_email apply'; org/tier2_senior/0.8.0_AE_CloudComp/task_orders/nfra-toolunify-critical-surface-alerts-email-sub-apply.md:109 instructs scoping with -target. So prior seats worked this tree by TARGETING, which the face of TO-CG-B-1 does not mention",
        "NOTHING WAS APPLIED. safe-apply was never invoked; the plan was written to a plan file and read, never applied. Control: infra/aws/terraform/globgrph working copy still shows exactly one dirty line (the untracked projection.tf), and no ledger leg carries a proof",
        "CONSEQUENCE FOR B1-AC3 AS WRITTEN: even a correct targeted apply of the 6 cannot yield the '0-diff re-plan' the criterion demands, because the 4 foreign items remain in every UNSCOPED plan of this tree by design. The criterion is unreachable in this tree without either landing an Andrew-excluded resource or redefining the re-plan bar"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-B-1 B1-AC3: 'APPLIED UNDER THE PROTOCOL: ledger entry opened before, safe-apply with the plan quoted (adds only; 0 change / 0 destroy), the 0-diff re-plan quoted, ledger entry closed after'; and the deliverable clause 'a non-zero change/destroy count is a STOP and a row'.",
    "world_is": "The module-wide plan is 8 add / 2 change / 0 destroy, not adds-only, and 4 of the 8+2 belong to other cells entirely. A bare safe-apply would land an Andrew-excluded SNS email subscription to a real human address plus three Glue partition changes this task order does not own. The STOP condition the face itself names is MET, so the apply was not run and the row is filed.",
    "notes": "RECOMMENDATION for the disarm owner, offered as a rec and NOT self-executed because an apply is outward-facing and hard to reverse: (1) safe-apply -target on exactly the 6 CG-s-1 addresses; (2) verify NOT with a -target re-plan -- CLAUDE.md Rule 22 names 'a -target apply verified by a -target re-plan' as a specimen of the scoped-check defect -- but with ONE UNSCOPED re-plan asserted to contain exactly the 4 known-excluded foreign items and ZERO of this cell's 6; (3) B1-AC3's '0-diff re-plan' limb re-worded to that bar, since 0-diff is structurally unreachable in this tree. The deploy ledger cldgrph-cgs1-marker-notification-projection-queue is deliberately left OPEN/RED: deploy_ledger.py hold REFUSED it ('a half-landed deploy cannot be HELD') and closing a leg that never ran would put a FALSE CLOSED on the record. Nothing is half-landed -- the deploy never started -- and OPEN is the honest state until the ruling lands. Routed to the issuer in the same turn per the face's BOUNDS. || ID COLLISION, RESOLVED BY RENUMBERING THIS ROW ONLY: this row was first written as NFRA_CLDGRPH-S11 and 0.7.0_AE_CloudOps~Q independently claimed S11 for a different row in the same minute (theirs surfaced_at 09:14Z, this one 09:15Z); the surprise-row-gate refused the commit on the duplicate, which is the gate working. This seat renumbered ITS OWN row to NFRA_CLDGRPH-S13 rather than touching a peer's, which append-only forbids. \u26a0 REFERENTIAL NOTE FOR READERS AND FOR THE L8 SEAT: 2.0.0_SA_COO~A's RULING at msg 93430 is titled 'RULING on NFRA_CLDGRPH-S11' and its subject cites S11 -- that ruling is about THIS row, now NFRA_CLDGRPH-S13. The id S11 in the channel now resolves to ~Q's unrelated OBSERVATION row. Recorded here because a citation that silently retargets is worse than a renumber that is announced."
  }
]
```

## S12 -- TO-CG-B-2 MANDATES a tool that violates TO-CG-B-2's own bound: `comp-blast` rebuilt the canonical DB

```json
[
  {
    "id": "NFRA_CLDGRPH-S12",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~Q",
    "surfaced_at": "2026-09-03T09:14Z",
    "one_line": "TO-CG-B-2's BOUNDS forbid reading or writing infra/aws/globgrph/kuzu_nessie_db while its own compiler_tools_mandate REQUIRES comp-blast on both engine files; comp-blast routes through _canonical.ensure_fresh, which found the DB BEHIND HEAD and REBUILT it at 09:11:51Z (82,661,376 B -> 46,997,504 B, fingerprint 711b0b3c.. -> d64fca39..). The mandate and the bound cannot both be obeyed, and the face's named mtime control had therefore already failed before any port code existed.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-CG-B-2 BOUNDS @585daff578 -- 'No pointer, no deletion, no serving, no local canonical DB. ... infra/aws/globgrph/kuzu_nessie_db is not read or written (mtime control as in TO-CG-V-1).'",
        "TO-CG-B-2 compiler_tools_mandate @585daff578 -- 'BEFORE WRITE: ... comp-blast infra/aws/globgrph/kuzu_nessie_load.py and comp-blast infra/aws/globgrph/kuzu_incremental_refresh.py (every caller of the engine that the port changes ...)'",
        "THE TOOL'S OWN STDOUT, first two lines of the comp-blast run: 'INFO: canonical auto-refresh (BEHIND Nessie HEAD (pin 5527093883275558226 != HEAD 919122196731915390 (writer=incremental_updater, committed_at=2026-09-03T08:32:05.491916+00:00))) -> rebuilding kuzu_nessie_db' then 'INFO: canonical FULL rebuild via the DESIGNED daily ground-truth reset (post-nightly whole-table delta trips the large-delta gate; CTO condition 2, NOT a defect)'",
        "MEASURED BEFORE/AFTER on the same instrument used for TO-CG-V-1's control: size 82,661,376 B at mtime '2026-09-02 20:36:15.505342500 -0400' with listing md5 711b0b3c78f0bfecff7a92bcdcd49193, then 46,997,504 B at mtime '2026-09-03 05:12:21.682472900 -0400' with listing md5 d64fca39dfa47179f7798dcb1b8e2340",
        "THE REBUILD IS ATTRIBUTED, not inferred: kuzu_nessie_db._build_manifest.json now carries built_at 2026-09-03T09:11:51.036107+00:00 with node_count 27135 -- matching the head count in the comp-blast banner (27,135), and 09:11:51Z falls inside the comp-blast invocation window",
        "TIMING CONTROL separating this from TO-CG-V-1: that task order's last control read was 07:52Z and its window closed at 07:51:30Z; this write is 09:11:51Z, i.e. 80 minutes after V-1 was terminal. V-1's four control reads are unaffected and are not being re-claimed here"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-B-2 simultaneously BOUNDS the assignee off `infra/aws/globgrph/kuzu_nessie_db` ('not read or written', with an mtime control 'as in TO-CG-V-1') and MANDATES `comp-blast` on both engine files as a BEFORE-WRITE step.",
    "world_is": "comp-blast reaches the canonical Kuzu graph through _canonical.ensure_fresh, which auto-refreshes a BEHIND database by rebuilding it. Obeying the mandate wrote the file the bound protects, at 09:11:51Z, before a single line of the port was written. The two clauses are not jointly satisfiable by any ordering.",
    "notes": "Disarm = the issuer decides which clause governs: either the bound is narrowed to 'the PORT does not read or write the canonical DB' (the intent I read, and which the port will honour regardless), or the mandate names a comp-blast invocation that does not trigger a refresh, or the mtime control is re-baselined. THIS SEAT PROCEEDS on the narrow reading -- the port itself will not touch the canonical DB, and its control runs from the POST-comp-blast baseline (46,997,504 B, mtime 2026-09-03 05:12:21.682472900 -0400, md5 d64fca39dfa47179f7798dcb1b8e2340), stated in the deliverable so the shifted baseline is visible rather than silent. Classed OBSERVATION and not BLOCKING because no work is stopped: the rebuild is the designed daily path, it left the estate fresher, and the port's own control is stateable from the new baseline. Not messaged to the issuer for that reason (the face routes only BLOCKING rows to a message). Wider than this project: ANY task order that bounds a seat off the canonical DB while mandating a comp-* tool that queries the graph carries this same contradiction."
  }
]
```

## S14 -- B2-AC1 names the TASK as the consumer of record; no Pipe/SQS shape can deliver that

```json
[
  {
    "id": "NFRA_CLDGRPH-S14",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~Q",
    "surfaced_at": "2026-09-03T12:35Z",
    "one_line": "B2-AC1 chose a Pipe to ecs:RunTask and asserted 'the TASK is the consumer of record', rejecting a design that acks on RunTask acceptance -- but a Pipes SQS source exposes only BatchSize and MaximumBatchingWindowInSeconds (no retention, no defer-ack, no on-failure), so the Pipe owns receive/delete and RunTask returns on acceptance. The rejected semantics ARE the chosen design's semantics; no Pipe/SQS shape gives a ~16-minute ECS task SQS-backed redrive. Consequence: ~P's queue reserves visibility_timeout for CG-s-2 to set 'from the measured duration' and the issuer endorsed 2400 s, a number that protects nothing if the worker never holds the message.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps~Q",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, live API surface: `aws pipes create-pipe --generate-cli-skeleton` -> SourceParameters.SqsQueueParameters == {\"BatchSize\": 0, \"MaximumBatchingWindowInSeconds\": 0} and nothing else; TargetParameters.EcsTaskParameters present. Read 2026-09-03 ~12:0xZ",
        "DISCRIMINATING CONTRAST in the same skeleton: KinesisStreamParameters and DynamoDBStreamParameters DO carry retry/bisect/on-failure controls, so the absence under SQS is a real absence of the capability and not an artifact of reading a thin skeleton",
        "THE CRITERION'S OWN TEXT, org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~Q/CG-s-2-9.projection-worker.result.md s.1.2 @18503387b5 -- 'NOT CHOSEN -- Pipe straight to RunTask with the message deleted on invocation ... RunTask returns as soon as the task is ACCEPTED, not when it finishes ... THEREFORE the task itself is the consumer of record'",
        "CROSS-SEAT CARRIER: infra/aws/terraform/globgrph/projection.tf:18-22 (~P, applied @afd94db0ce) -- 'AWS DEFAULT (30s), deliberately. CG-s-2 SETS THIS from CG-s-10's measured full-fallback duration -- the visibility timeout must exceed the worker's runtime'; and issuer msg 93565 endorsing 'your provisional 2400 ... with its derivation from the V-1 duration'",
        "NEGATIVE CONTROL on the reading: ~P's role grants the WORKER sqs:ReceiveMessage / DeleteMessage / GetQueueAttributes / ChangeMessageVisibility -- an IAM shape that only makes sense for a worker that consumes the queue itself, which is exactly the design the API surface says a Pipe cannot provide. Two independent carriers (the IAM grant and the queue comment) both encode the assumption this row falsifies"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-B-2 B2-AC1 requires the queue-to-compute mechanism named with 'the queue's visibility timeout set from the measured numbers (>= the longest step that holds the message, with the number)', and this seat's own B2-AC1 answer names the ECS task as the consumer of record and rejects acking on RunTask acceptance.",
    "world_is": "A Pipes SQS source has no control that defers or suppresses the ack; the Pipe receives and deletes around a RunTask call that returns on acceptance. The longest step that HOLDS THE MESSAGE is therefore the Pipe's own invocation (seconds), not the task's ~16-minute run -- so the criterion's own derivation of the timeout, and the sentence naming the task as consumer of record, do not hold under the chosen mechanism.",
    "notes": "Disarm, and it is this seat's because the mechanism is this face's decision: re-state B2-AC1's mechanism limb on the measured surface -- either (a) keep the Pipe, declare the Pipe the consumer of record, derive the visibility timeout from the PIPE's hold rather than the run, and state the retry property honestly as marker idempotency plus the nightly 02:00Z guarantee rather than SQS redrive; or (b) choose a mechanism where the worker genuinely holds the message, which needs a trigger that does not consume the queue and is a larger change. THE DESIGN IS NOT ASKED TO CHANGE BY THIS ROW and the issuer has not asked for one (93613); what the row refuses is shipping the ASSERTION unchanged. B2-AC1's proof row carries the limb as OPEN, never PASS -- a PASS on a limb I declared open would be the defect this project keeps finding in other carriers. No Terraform is authored until the limb is re-stated; ack semantics I have only recalled are not a foundation for an applied resource."
  }
]
```

## S15 -- the projection queue delivers TWO message shapes, and the second has no `Records` key

```json
[
  {
    "id": "NFRA_CLDGRPH-S15",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~Q",
    "surfaced_at": "2026-09-03T12:36Z",
    "one_line": "The projection queue delivers TWO shapes, not one: the S3 event envelope {\"Records\":[...]} AND a one-off {\"Service\":\"Amazon S3\",\"Event\":\"s3:TestEvent\"} with NO Records key, emitted by S3 when the notification configuration is created. A consumer written from R5's description alone assumes Records and crashes on the TestEvent (0.7.0_AE_CloudOps~P's first parser did). The worker must tolerate both; a TestEvent is deleted, never DLQ'd.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps~Q",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0.7.0_AE_CloudOps~P's CG-s-1 deliverable sections D-E, org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~P/CG-s-1.marker-notification.result.md @afd94db0ce -- both shapes observed on the live queue, relayed by the issuer as msg 93566 item (1)",
        "The real envelope carries s3.object.{key,size,eTag,sequencer}, s3.configurationId 'projection-branch-head-marker' and userIdentity.principalId of the producer (93566 items 1 and 5)",
        "RELAYED, NOT RE-MEASURED BY THIS SEAT, and marked so: the main queue read depth 0 at 11:47Z because the 09:42:42Z stamp expired at retention 3600, so this seat has not itself received either shape. The grounding is ~P's first-party observation carried through the issuer, and B2-AC6's exercise is where this seat meets them directly",
        "PRD v0.4 s.6 R5 describes the trigger as 'an S3 event notification on warehouse/_branch_head.main.json -> an SQS queue with DLQ' and names ONE shape; the TestEvent is not in the spec's description and is not optional -- S3 emits it when the notification configuration is created"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.4 s.6 R5 and TO-CG-B-2 s.2 describe the worker as receiving 'the queue message' from an S3 event notification on the branch-head marker -- one shape, an S3 event envelope whose object key is the marker.",
    "world_is": "The queue delivers that envelope AND a one-off s3:TestEvent with no Records key. A consumer built to the spec's description alone raises on the TestEvent rather than skipping it, which is how ~P's first parser failed.",
    "notes": "Disarm = the worker's consumer tolerates both shapes explicitly, with a control that feeds it a TestEvent body and asserts it is deleted-not-DLQ'd, landing with B2-AC2. Recorded now rather than at the exercise because the consumer is written BEFORE the exercise, and this is the fact that decides its first branch. RELATED denominator, deliberately NOT a row per the issuer: the DLQ baseline is 3, not 0 -- ~P's four receive-polls incremented ApproximateReceiveCount against maxReceiveCount 3. That is disclosed probing, not a spec divergence, and it rides this seat's proof as the before/after denominator; it also means this seat must not receive-message the main queue more than twice before the consumer runs, or it DLQs its own exercise message."
  }
]
```

## S16 -- 2,243 of the 2,256 duplicate edge rows are producer findings, not expected repeated observations

```json
[
  {
    "id": "NFRA_CLDGRPH-S16",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~T",
    "surfaced_at": "2026-09-03T13:58Z",
    "one_line": "The 2,256-edge excess reconciles as 13 expected repeated observations plus 2,243 producer findings. 2,235 semctl C2i->C1 CONTAINS excess rows come from c2_individuate deduplicating motif nodes by member set while emitting the pre-collapse edge list. Eight AWS TRIGGERS excess rows represent two distinct EventBridge target IDs per rule whose Id/Input are dropped by comp_aws_cli, making different configurations one empty-props graph identity.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ-ONLY PyIceberg census at edge snapshot 1026441646305052092: 61,071 rows; 383 missing-endpoint skips; 60,688 eligible MERGE attempts; 58,432 distinct (src,dst,edge_type,props) identities; 2,256 excess across 1,632 duplicate identity groups. Multiplicity: 1,580 groups x2 and 52 groups x14. Every excess row is identical on src_id,dst_id,edge_type,layer,snapshot_ts,props.",
        "MERGE identity source: infra/aws/globgrph/kuzu_nessie_load.py:210-226 @117e539280d678e946f5c74a1f2593e07d41e01a; stored COUNT(*) and collapsed delta: :230-240 at the same commit.",
        "SEMCTL split: 2,235 excess, all CONTAINS, all props.rel_tier=C2i->C1. c2_individuate.py:427-465 @23220a7b20df85b669c6a9711e0ae9d50b3acd1a keys nodes by deterministic member set but appends member edges for every raw detector row; :631 reports collapsed_duplicate_member_sets while :633 emits the uncollapsed edges list. The two static semctl specs each have zero internal duplicate identities and zero cross-spec overlap; none of their identities is in the duplicate group set.",
        "AWS ASSUMES split: 13 excess from one profile->role identity occurring 14 times. comp_aws_cli.py:1382-1398 @59347e4d9ec9603562c6dd7095e13dd1ae630291 emits that relation once inside the EC2 loop; live read-only describe-instances found exactly 14 instances using bd-exporter-profile. This is expected repeated observation of one logical relation.",
        "AWS TRIGGERS split: 8 excess, eight identities occurring twice. comp_aws_cli.py:1500-1516 at the same commit emits only rule ARN and target ARN. Live read-only list-targets-by-rule showed two target IDs for each rule; the news targets carry different or absent Input payloads. Since Id/Input are not emitted into props, semantically distinct target configurations collapse.",
        "Final Iceberg writer: infra/aws/globgrph/derive_runner.py:313,357-376 @ec0408628ac098ddbb0035da1f032964faa8b286 copies graph['edges'] directly into graph_edges with no identity dedup pass."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-B-3 B3-AC4 requires every one of the 2,256 duplicate excess rows to be classified as expected-by-construction or as a finding with a named producer owner; this cell answers and records, but does not adjudicate or fix another producer.",
    "world_is": "13 excess ASSUMES rows are expected-by-construction from 14 EC2 observations of one profile-to-role relation. The remaining 2,243 are findings: 2,235 uncollapsed live C2-instance member-edge emissions owned by 3.0.0_SA_CVO's c2_individuate.py, and 8 EventBridge target configurations made indistinguishable by 0.8.0_AE_CloudComp's comp_aws_cli.py projection. derive_runner persists both lists without deduplication.",
    "notes": "No producer fix is authorized under CG-s-3. 2.0.0_SA_COO~A owns routing/disposition for this round. The named source owners are 3.0.0_SA_CVO for c2_individuate.py and 0.8.0_AE_CloudComp for comp_aws_cli.py; live EventBridge resource owners retain configuration ownership. The B3 artifact contract remains count-correct because both full and incremental manifests must stamp post-load COUNT(*), not attempt counts."
  }
]
```

## S17 -- a Pipe environment-only ECS container override imposed a 4 MiB memory limit

```json
[
  {
    "id": "NFRA_CLDGRPH-S17",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~S",
    "surfaced_at": "2026-09-03T14:20Z",
    "one_line": "The applied EventBridge Pipe's environment-only ECS container override was not memory-neutral: although task definition globgrph-projection-worker:1 declared 16,384 MiB, both first real executions failed before Python with runc attempting a 4,194,304-byte cgroup memory limit. The disarm is to repeat the already-ruled 2048 CPU / 16384 MiB memory in the container definition and Pipe override, then exercise the same real-event path.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps~S",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "APPLIED task definition arn:aws:ecs:us-east-1:313476888478:task-definition/globgrph-projection-worker:1 declared task cpu=2048 and memory=16384; the Pipe target override declared only container name + PROJECTION_EVENT_JSON environment",
        "CloudWatch worker streams projection-worker/projection-worker/7619cf4e95684e24b69bb73681f0f612 and .../cef53f4b52b041ec889194308d5a9ac6 each contain only runc create failed: unable to set memory limit to 4194304; neither contains PROJECTION_EVENT, proving Python never started",
        "Pipe execution ids 6e752e41-36bf-41ef-8ad4-4ec97579cb7a and 4c2350ad-49e7-4d07-854c-a5b82924eb39 both report ExecutionSucceeded in under one second, independently corroborating S14: the Pipe acked RunTask acceptance rather than task completion",
        "Both inputs were real marker writes by principal AWS:AROAUR7FNW6PIZYLEKZRE:opal-globgrph-incremental-updater at 13:23:40.625Z and 13:23:55.540Z; DLQ remained at its disclosed baseline 3, and no projection/ object existed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "B2-AC1 fixes the ECS task at cpu 2048 and memory 16384 from the measured fit table, and B2-AC6 requires the real-event cloud task to run the engine rather than fail before entrypoint.",
    "world_is": "On the first applied Pipe calls, an environment-only container override yielded a 4 MiB cgroup memory request despite the 16 GiB task-level memory declaration, so both containers failed during runc initialization and no engine path ran.",
    "notes": "Disarm in this task: explicitly carry cpu=2048 and memory=16384 on the projection-worker container definition AND the Pipe container override, create task-definition revision 2, update the Pipe target, then show a real-event execution reaches PROJECTION_EVENT and the engine. This repeats the already-ruled sizing; it does not reopen B2-AC1. The two failed deliveries are not recoverable by SQS (S14), but a third real queued stamp remains and the nightly guarantee remains; never manufacture a marker. This row is messaged to 2.0.0_SA_COO~A in the same turn because class=BLOCKING."
  }
]
```

## S18 -- the Pipe's SQS payload is a Records wrapper, so `$.body` was passed literally

```json
[
  {
    "id": "NFRA_CLDGRPH-S18",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~S",
    "surfaced_at": "2026-09-03T14:25Z",
    "one_line": "The EventBridge Pipe SQS source payload is a Records wrapper, not a top-level message: the revision-2 task override carried PROJECTION_EVENT_JSON='<$.body>' literally and Python failed JSONDecodeError before classifying the TestEvent. Pipe execution data locates the value at $.Records[0].body; the dynamic path must be <$.Records[0].body>.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps~S",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "APPLIED task 52cd0f5035934db78e21cd070099cc9e on task definition revision 2 reached Python and exited 1 with PROJECTION_ERROR JSONDecodeError: Expecting value line 1 column 1",
        "aws ecs describe-tasks overrides for that task returns environment [{name:PROJECTION_EVENT_JSON,value:<$.body>}] with cpu=2048 and memory=16384 -- S17 is disarmed and the unresolved expression is literal",
        "Pipe ExecutionStarted payloads are shaped {Records:[{messageId,body,attributes,...}]}; therefore body is measured at $.Records[0].body",
        "TestEvent message id 9bb1988c-45d7-49fe-aaad-a4132967a8fa was consumed from the real queue; DLQ remained at the disclosed baseline 3 and no projection/ object was written"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S15's disarm and B2-AC2 require the worker to receive and classify the queue body, including s3:TestEvent without Records in that body.",
    "world_is": "The Terraform used <$.body>, but the actual Pipes SQS execution envelope nests the message body under Records[0]; the non-resolving expression was delivered to ECS as a literal string and the worker could not parse it.",
    "notes": "Disarm in this task: set the Pipe container override value to <$.Records[0].body>, target-safe-apply the in-place Pipe update, and repeat the TestEvent control until the task exits 0 with test_event_ignored, the main queue is empty, DLQ delta is zero and projection/ remains absent. Messaged to 2.0.0_SA_COO~A in the same turn because class=BLOCKING."
  }
]
```

## S19 -- ECS container environment overrides do not transform either measured JSONPath

```json
[
  {
    "id": "NFRA_CLDGRPH-S19",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~S",
    "surfaced_at": "2026-09-03T14:30Z",
    "one_line": "Pipes delivered both attempted ECS environment JSONPaths literally (<$.body> and <$.Records[0].body>), so per-message container environment is not a dynamic field on this applied target path. The Pipe must own the two-shape branch through an SQS-body filter: TestEvent is deleted without RunTask; only an exact Records marker event launches a task, which reads the mutable marker HEAD oracle directly.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps~S",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Revision-2 TestEvent task 52cd0f5035934db78e21cd070099cc9e carried literal <$.body>; the second task 2617e42c961b4ca288d9de74ab1803dd carried literal <$.Records[0].body>; both exited JSONDecodeError before any S3 call",
        "Both applied task overrides retained cpu=2048 and memory=16384, so these failures are independent of S17's cgroup defect",
        "Pipe execution data itself parses each SQS message as Records[0].body, but neither expression transformed in the ECS environment override; two locations were exercised, both literal",
        "PRD R5/R8 names warehouse/_branch_head.main.json as the HEAD oracle; the task can consume current committed HEAD without an event body, while the Pipe source filter can discriminate body.Records from the no-Records TestEvent before RunTask"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S14 declares the Pipe the consumer of record; S15 requires that consumer to tolerate Records and TestEvent; R5 requires real marker events to start the worker, whose source of truth is the marker oracle.",
    "world_is": "The ECS task cannot receive either attempted dynamic environment value on this applied target. Without a source filter it cannot distinguish TestEvent; with a body.Records marker filter the Pipe can delete TestEvent and invoke ECS only for real marker notifications, after which the task reads current HEAD.",
    "notes": "Disarm in this task: remove PROJECTION_EVENT_JSON from the Pipe target, add an exact SQS body filter for Records[*].s3 bucket/key, keep the 2048/16384 override, and let the task use a pipe-filtered-records sentinel before reading the marker. Repeat the TestEvent: main queue empty, no new ECS task, DLQ delta zero, projection absent. Then wait for a real producer stamp and show it does launch the task. Messaged to 2.0.0_SA_COO~A in the same turn because class=BLOCKING."
  }
]
```

## S20 -- HANDED OFF from NFRA_COMPEFFICACY: the ported deriver reports a failed S3 notification read as a genuine zero (bare except), so the live graph's S3_BUCKET-[TRIGGERS]->LAMBDA edge is EMPTY estate-wide

```json
[
  {
    "id": "NFRA_CLDGRPH-S20",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~A",
    "surfaced_at": "2026-09-03T14:55Z",
    "one_line": "HANDED OFF from NFRA_COMPEFFICACY (row S15 there, dismissed as S21 naming the record): the graph deriver this project ports, org/modules/graph/comp_aws_cli.py derive_edges, swallows a failed get_bucket_notification_configuration read in a bare except, so a failed read equals a genuine zero -- the live graph's S3_BUCKET-[TRIGGERS]->LAMBDA edge is EMPTY estate-wide while Terraform declares real aws_s3_bucket_notification resources with Lambda targets (bd-pipeline, cot-pipeline, inf-pipeline); a forced refresh does not change it. A silent-zero in the engine the cloud worker runs is a silent-zero shipped twice.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO lateral 93697 (14:33Z) and its record org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_HANDOFF_NFRA_COMPEFFICACY_S15_TO_NFRA_CLDGRPH_20260903T142xZ.md at commit b5d228fe62; the measurement is 0.8.0_AE_CloudComp's (NFRA_COMPEFFICACY-S15 at commit a140eed779): MATCH (b:CloudNode)-[e:CloudEdge]->(l:CloudNode) WHERE b.node_type='S3_BUCKET' AND e.edge_type='TRIGGERS' AND l.node_type='LAMBDA' returns 0 rows; opal-data-bd IS an S3_BUCKET node with zero outgoing TRIGGERS edges against three declared targets",
        "cause at source as measured by that seat: org/modules/graph/comp_aws_cli.py:1439-1447 (derive_edges) -- get_bucket_notification_configuration inside a bare except: pass, with the node-property twin at :273-279 in the same shape; RELAYED, NOT RE-MEASURED BY THIS SEAT, and marked so",
        "why this project: the deriver is part of the build CG-s-2 ports to the cloud worker (PRD v0.4 R5), the same class as rows S2/S3/S8 (defects in the thing being ported, routed SPEC_ERROR to the port orders at the round-1 stamp); the surfacing project dismissed its own row naming this record and does not write into this project's loop"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.4 R5 (@25c66d3358) and FWD-2/FWD-4 assume the worker runs the existing engine and that the projection it publishes is the estate's graph; a derived edge count of zero is read by every consumer as a genuine absence.",
    "world_is": "The deriver reports a FAILED notification read as ZERO edges (bare except), so the TRIGGERS edge from S3 buckets to Lambda is empty on the live graph while the Terraform declares the resources; a consumer cannot distinguish that zero from a real absence, and the ported worker would publish the same zero under a fresh vintage every night.",
    "notes": "Mid-round the spec is frozen: no order is amended for this. ISSUER'S ROUTE RECOMMENDATION for the round-2 stamp (3.0.0_SA_CVO~A's disposition): SPEC_ERROR with loop_target 6 and owner 2.0.0_SA_COO~A -- an L6 order against the engine files in a later round (the shape the surfacing seat would recognise: a failed notification read reported as UNREADABLE, never zero; the TRIGGERS edge derived from the declared aws_s3_bucket_notification resources as a second source; a denominator of buckets read versus unreadable on every build). Not a fix under TO-CG-B-2 (the four ruled fixes are S2/S3/S8/S9's) and not under TO-CG-B-3. The disarm this round is this row plus the route; the hazard stays ARMED until the derive reports the read state. Filed by the issuer as the seat that read the lateral, per the base CVO's 93697 (asked of nobody; a row by the seat that reads it)."
  }
]
```

## S21 -- the first post-fix real-stamp projection was deliberately stopped by CG-s-3

```json
[
  {
    "id": "NFRA_CLDGRPH-S21",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~S",
    "surfaced_at": "2026-09-03T16:28Z",
    "one_line": "The first post-fix real producer stamp correctly traversed S3 -> SQS -> Pipe -> projection task, but task 6aa88972790949a5bbe9b315381ec895 was explicitly stopped after about 288 s of engine time with ECS stopCode UserInitiated and stoppedReason 'CG-s-3 prevent pre-contract image collision at released vintage'; exit 137 is the consequence of that external stop, not evidence of a 16 GiB OOM, and B2-AC6 remains unexercised with zero projection artifacts.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Real marker committed_at_iso 2026-09-03T16:21:26.406073+00:00 / writer_id derive_runner / ETag 1e65605ed5ae82abb97dadf94ee0d945 produced SQS message e089eaf4-7544-49d7-9229-9864e5f3e9a3 and Pipe execution 5203b1a7-c5eb-45ca-8c6e-1aa057224557, which launched task 6aa88972790949a5bbe9b315381ec895",
        "ECS describe-tasks: startedBy 'Started by Eventbridge Pipes'; task definition globgrph-projection-worker:2; image digest sha256:3a4e078d2c65c0243f2aac3c2ad033ac7a154c12cc46d7b9998cf37601188486; task and container override cpu 2048 / memory 16384",
        "ECS describe-tasks: startedAt 1788452507.355; stoppingAt 1788452795.641; executionStoppedAt 1788452837.073; stoppedAt 1788452860.647; stopCode UserInitiated; stoppedReason 'CG-s-3 prevent pre-contract image collision at released vintage'; container exitCode 137",
        "The worker log contains PROJECTION_EVENT pipe-filtered-records and no PROJECTION_RESULT or PROJECTION_ERROR; list-objects-v2 under projection/ remains zero, so the external stop left no partial published artifact"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "B2-AC6 requires the full-cold real-stamp run to complete with cloud duration and peak memory, and the decomp places CG-s-3 downstream of this worker's versioned artifact handoff; the issuer separately released CG-s-3 Phase B only on the statement that no further Python edit was pending, not by authorizing termination of B2's running exercise.",
    "world_is": "The real trigger path is proven through task launch, but a user-initiated CG-s-3 stop terminated the B2 task before its engine measurement and artifact publication. This run cannot prove or disprove the chosen memory size and cannot close the exercised criterion or ledger L4.",
    "notes": "Blocking coordination question to the issuer: rule whether this seat retries the exact projection task against the still-real marker HEAD after CG-s-3's collision window is cleared, or waits for another real stamp. Preserve the stopped task as evidence; do not relabel exit 137 as OOM, do not delete or manufacture a marker, and do not close B2-AC6 or the ledger on this interrupted run. Messaged to 2.0.0_SA_COO~A in the same turn."
  }
]
```

## S22 -- the B2 publisher can overwrite an immutable same-vintage prefix

```json
[
  {
    "id": "NFRA_CLDGRPH-S22",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~T",
    "surfaced_at": "2026-09-03T16:33Z",
    "one_line": "The B2 projection publisher checks a target vintage only before its long build, then uses unconditional artifact and manifest uploads; two tasks consuming the same marker can both observe an absent prefix and overwrite the supposedly immutable versioned objects last-writer-wins. The contract requires conditional create and only a byte-identical no-op on collision.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps~T",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/globgrph/projection_worker.py:201-257 @a9ef0f6160b6aa786b0321f1893e5089c08e118a checks both target objects once before the engine run, then calls upload_file for the database and manifest without If-None-Match or a second collision comparison",
        "The authentic derive_runner marker vintage 2026-09-03T16:21:26.406073+00:00 launched B2 task 6aa88972790949a5bbe9b315381ec895 on image digest sha256:3a4e078d... while CG-s-3 task 2c5a8a21ac884253a2b6e2facf8e61e4 later consumed the same current marker on digest sha256:1e1aaa14...; both observed no object under that versioned prefix before their long full builds",
        "Issuer ruling Msg 93788 requires same-vintage immutability: a second publish is refused or a byte-identical no-op, and directs a row if the B2 writer violates that rule",
        "The pending Phase B worktree uses PutObject If-None-Match:* for each versioned object, reads an existing object back after a 412, permits only exact byte identity, and has a four-arm control (identical artifact/manifest no-op; differing artifact/manifest refusal); focused suite 10 of 10 passed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PROJECTION_CONTRACT.md makes every object below a versioned artifact prefix immutable after first write; issuer ruling Msg 93788 sharpens the collision outcome to refusal or byte-identical no-op.",
    "world_is": "The B2 image at a9ef0f6160 can overwrite both same-vintage objects after a stale pre-build absence check. Bucket versioning is OFF, so a non-identical second upload destroys the prior bytes and cannot be reconstructed from S3 versions.",
    "notes": "Disarm in CG-s-3's worktree-only Phase B: conditionally create each versioned object with If-None-Match:*, compare an extant object's exact bytes/hash after a 412, accept only byte identity as a no-op, otherwise refuse. Do not deploy or publish until the issuer relays that ~S's B2 retry produced the first artifact. S21 separately carries this seat's out-of-bounds stop of task 6aa889...; that act is disclosed and is not a disarm for this row. No push."
  }
]
```

## S23 -- the B2 worker advanced the projection pointer owned by CG-s-3

```json
[
  {
    "id": "NFRA_CLDGRPH-S23",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~S",
    "surfaced_at": "2026-09-03T16:46Z",
    "one_line": "The accepted B2 full-cold Pipe task fa5df7737afc48fdbda6a9106d5676b6 advanced projection/current.json at 16:41:58Z even though TO-CG-B-2 explicitly bounds the port off all pointer writes and assigns the pointer to CG-s-3; the complete pointer is disclosed and left in place for CG-s-3's conditional writer to supersede, with no undo by this seat.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps~T",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-CG-B-2 at spec vintage cab640d351ca1ada655b13647c2e65916f5f32cf section 2 says advances NO pointer; B2-AC2 requires the pointer object ABSENT after every run; B2-AC7 hands pointer ownership to CG-s-3; BOUNDS repeat No pointer by the port",
        "infra/aws/globgrph/projection_worker.py @a9ef0f6160b6aa786b0321f1893e5089c08e118a defines POINTER_KEY=projection/current.json and its shared publish path advances that pointer after artifact/manifest readback",
        "CloudWatch result for authentic S3 -> SQS -> Pipe -> RunTask task fa5df7737afc48fdbda6a9106d5676b6: status published, mode full-cold, pointer_written true, pointer_status advanced; S3 head-object timestamps projection/current.json at 2026-09-03T16:41:58Z",
        "Exact canonical pointer body as written: {\"artifact_prefix\":\"projection/2026-09-03T16:27:39.471730+00:00/\",\"manifest_key\":\"projection/2026-09-03T16:27:39.471730+00:00/_build_manifest.json\",\"manifest_sha256\":\"0c2c0052c43ca06ce92bb37fe822a733c4999a0405e2a8b456b015f14d40f101\",\"schema_version\":1,\"vintage\":\"2026-09-03T16:27:39.471730+00:00\"}",
        "Independent readback: the pointer manifest SHA-256 equals the downloaded 1,632-byte manifest hash 0c2c0052c43ca06ce92bb37fe822a733c4999a0405e2a8b456b015f14d40f101; that manifest's artifact hash equals the downloaded 48,046,080-byte Kuzu DB hash 5a449cb4384c5933491d431546136b0053f3d0cc37e6c681d361611a7ba0a12a; direct Kuzu counts equal manifest nodes 27,206 / edges 58,550"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-B-2 section 2, B2-AC2, B2-AC7, and BOUNDS require the B2 port to advance no pointer and leave projection/current.json absent because the pointer object, its atomicity, and the manifest contract belong to CG-s-3.",
    "world_is": "The B2 worker at a9ef0f6160 writes projection/current.json after its artifact/manifest readback; the accepted fa5df7 real-path run exercised that code and advanced the pointer to the 2026-09-03T16:27:39.471730+00:00 artifact.",
    "notes": "Issuer ruling Msg 93807: no undo by this seat. Disarm owner 0.7.0_AE_CloudOps~T; disarm is B3-AC2's pointer writer with the completeness check and conditional create superseding the bare write in the shared publish path. B2-AC7 must disclose the exact pointer body and this crossed bound. No push."
  }
]
```

## S24 -- a valid one-node incremental projection cannot pass the fixed publish-set size band

```json
[
  {
    "id": "NFRA_CLDGRPH-S24",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps~S",
    "surfaced_at": "2026-09-03T17:24Z",
    "one_line": "The authentic one-node incremental arm succeeded at the engine and count guard (27,225 nodes / 58,606 edges / 383 skipped) but produced an 83,617,383-byte publish set, so the shared writer refused it above the fixed 42,294,879..51,693,741-byte contract band; the ruled checkpoint/export/import compaction then measured 34,825,831 bytes including manifest, below the same full-load-derived band, proving B2-AC6's engine arm while routing a mode-specific band to round 3.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps~S",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Exactly-once reversible QA trigger: bucket opal-313476888478-globgrph had the canonical six-tag array read before and after one PutBucketTagging call; the arrays were byte-identical. CloudTrail event 2ef5326a-ad76-4071-8307-d9b8ff5c8bcc at 17:21:01Z caused incremental_updater request 70d9ca80-4548-51f8-865c-a993ebf9cd25 to process the real S3_BUCKET ARN, write one node, and stamp marker 2026-09-03T17:23:22.339410+00:00",
        "Pipe execution 09f97531-1a2c-4b5f-91ce-8ead27b74dbc accepted that SQS event at 17:23:24.109Z and launched ECS task 32d8608dbe8f42f482a5e4114b3e0ace on globgrph-projection-worker:2 / image digest sha256:1e1aaa14df31da756001f3a42b1f5b6c671e4d75586aeb72c96586534a50f01c",
        "Worker log: INCR_NODE_DELTA head=27225 cur=27225 upsert=1 delete=0 (0.0%); edge upsert=0 delete=0; nodes=27225 edges=58606 skipped=383; INCR_RESULT status=incremental; the container then logged PROJECTION_ERROR PublicationRefused: publish set 83617383 bytes is outside 42294879..51693741 and exited 1",
        "Independent post-failure S3 control: projection/2026-09-03T17:23:22.339410+00:00/ contains zero objects, while projection/current.json still names the accepted 2026-09-03T17:01:08.128628+00:00 full-fallback artifact and manifest SHA-256 28ed81e28144fa3db6dc880adf55ff1076c1b376d36b4b8b1d8597d1cc4a8f1c",
        "Issuer Msg 93835 disarm @052a58999a8ba83db4d02279ad0d6765a1e4998a: incremental-only CHECKPOINT plus PARQUET EXPORT/IMPORT into a fresh Kuzu file plus final CHECKPOINT before conformance. Focused suite 9 passed. Local real-data control reclaimed 48,791,552 bytes (83,615,744 -> 34,824,192); canonical manifest 1,639 bytes made a 34,825,831-byte publish set, below the unchanged 42,294,879-byte minimum, so conformance refused locally before any S3 operation",
        "While the disarm was being implemented, producer HEAD advanced naturally to 2026-09-03T17:32:43.452059+00:00 and rev2 Pipe task 03a14222ff914416af24193a4f9f61e7 independently passed a two-node incremental (27,226 / 58,606 / 383) before refusing the same 83,617,383-byte publish set. The exact-marker local safety check aborted before using the superseded 17:23 HEAD; no manual retry was consumed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The contract's diagnostic band assumes full-load sizes: PROJECTION_CONTRACT.md v0.1 refuses every publish set outside the measured full-build baseline +/-10%, 42,294,879..51,693,741 bytes. B2-AC6 simultaneously expects a subsequent real incremental run to publish artifact plus manifest under its real marker vintage with manifest edge_count equal to direct COUNT(*).",
    "world_is": "Kuzu incremental output grew to an 83,617,383-byte publish set on a valid one-node delta, 1.74 times the accepted full load. The incremental engine and its own count guard passed, but the contract gate safely refused before artifact, manifest, or pointer writes; under this fixed full-load-derived band every daytime incremental would be refused, and copying then updating that database could compound the file across nights.",
    "notes": "Issuer Msg 93834 rules the B2-AC6 incremental ENGINE arm PASS on the record and the PublicationRefused outcome the completeness can-fail control firing on a real defect. Msg 93835 puts compaction in this seat's runtime lane; the required local measurement is deterministically below the same full-load band. Final Msg 93848 rules option (d): no revision 3, no cloud retry, and no local marker override; deploy compaction @052a58999a with the round-3 fixed publisher, whose integrity check is counts, hashes, and declared sizes with no byte band or a mode-specific band. Peer 0.7.0_AE_CloudOps~T acknowledged and independently routed the contract divergence. No second QA trigger, no marker write, no contract widening, no manual retry, no push. The previous pointer and prefix remain intact."
  }
]
```

## S25 -- L10 stamp, round 2: two bounded dismissals and twelve graduations

```json
[
  {
    "id": "NFRA_CLDGRPH-S25",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~C",
    "surfaced_at": "2026-09-03T18:04Z",
    "one_line": "L10 STAMP, round 2: all five project task orders are terminal with valid, exact-coverage proofs. S16 and S21 are dismissed with bounded reasons; twelve other round-2 items graduate through REMEDIATION_v2.md, seven completed in-round and five routed SPEC_ERROR to L6 for round 3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CVO re-ran proof-of-spec-check on B-1 @afd94db0ce, B-2 @ebe85fd69e and B-3 @93c26badf8: all VALID rc 0; criterion step-zero is exact at 6/6, 8/8 and 6/6, with every declared cell reachable and every surprise reference resolving.",
        "All five task-order faces under NFRA_CLDGRPH read complete at HEAD; the round-1 V-1/V-2 proof coverage remains 6/6 and 7/7.",
        "S16 @823ea90776 separates 13 expected profile-role repeats from 2,235 C2-instance member emissions and eight collapsed EventBridge-target observations, names their source owners, and establishes that B-3's post-load counts remain correct; neither producer fix belongs to a round-2 face.",
        "S21 @ee51681c45 records an external UserInitiated stop rather than OOM. It is superseded as an exercise blocker by authentic completed tasks fa5df773, 0a53e160, 32d8608d and 03a14222 in the accepted B-2 proof @ebe85fd69e.",
        "REMEDIATION_v2.md in this same commit carries twelve graduations: seven evidenced in-round closures and five SPEC_ERROR routes with the locked loop target 6."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S16 is an outside-remedy producer census, not a missing or failed NFRA_CLDGRPH round-2 criterion: the graph port preserves correct post-load counts, the two upstream source owners are named, and no worker may silently widen its face to repair them. S21 is a one-time cross-seat stop whose classification remains UserInitiated; later authentic runs completed every required B-2 exercise arm, so it establishes no remaining normal-operation defect and routes no remedy.",
    "adjudicates": ["NFRA_CLDGRPH-S16", "NFRA_CLDGRPH-S21"],
    "spec_asserts": "The L10 precondition requires every project task order terminal with a valid proof-of-spec instance, every proof criterion covered exactly, and every investigation item dispositioned before one route slug issues.",
    "world_is": "All five faces are terminal and their proof sets are exact. Of the fourteen round-2 items, seven remedies executed in-round, five require existing L6 cells in round 3, one is an outside-remedy producer census, and one is an externally stopped attempt superseded by completed authentic exercise.",
    "notes": "Zero DECOMP_INVALIDATING and zero SCOPE_CHANGE. The fixed publisher and compaction are committed but not deployed; the live forward pointer was written by the pre-fix image and remains valid. Those applied-versus-desired boundaries are preserved as S22-S24 routes, never flattened into round-2 closure. No push by this seat."
  }
]
```

## S26 -- the user-bin compiler shims deny this Codex seat while the repository-local tools run

```json
[
  {
    "id": "NFRA_CLDGRPH-S26",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~O",
    "surfaced_at": "2026-09-03T18:51Z",
    "one_line": "The three user-bin compiler shims required by TO-CG-C-3 deny this Codex seat before tool execution, while comp-which and the repository-local compiler entry points run; the task continues through the ruled repository-local path without changing user-bin ACLs.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Bare comp-to, comp-read, and comp-find each failed before tool execution with Windows 'Access is denied' at C:\\Users\\AndrewBerman\\bin\\comp-to.cmd, comp-read.cmd, and comp-find.cmd respectively; Get-Acl showed explicit deny entries on the affected user-bin shims.",
        "Bare comp-which executed successfully from C:\\Users\\AndrewBerman\\bin\\comp-which.cmd and routed the focused key-context question to comp-read.",
        "After COO ruling Msg-ID 93884, repository-local entry points were exercised: python .tools/comp-read fully read both ruling files and bash .tools/comp-to set the race-free seat/session TO_ID for NFRA_CLDGRPH.TO-CG-C-3.deriver-read-state.",
        "COO ruling Msg-ID 93885 assigned disarm ownership to 1.0.0_SA_CTO, identified as the launcher owner, and stated that the issuer had already notified that seat."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_CLDGRPH.TO-CG-C-3's compiler mandate names comp-to, comp-read, and comp-find as the required tool surfaces, and the launcher contract says the bare comp-* commands are provided to this Codex PowerShell seat through canonical user-bin command shims.",
    "world_is": "For 0.8.0_AE_CloudComp~O, the user-bin comp-to, comp-read, and comp-find shims carry explicit deny ACL entries and fail with Access is denied before their tools execute, while comp-which runs. The repository-local comp-read and comp-to entry points execute successfully, so the ordered C-3 work proceeds through those ruled entry points rather than collapsing into a stop or an unrecorded workaround.",
    "notes": "Ruling 1 explicitly forbids altering the user-bin ACLs and authorizes repository-local tool entry points; ruling 2 requires this one OBSERVATION row and names 1.0.0_SA_CTO as disarm owner. No ACL was changed, no task surface was widened, and no push is permitted or attempted."
  }
]
```

## S27 -- TO-CG-C-3 names cot-pipeline as Lambda-notification-bearing, but its declaration is EventBridge-only

```json
[
  {
    "id": "NFRA_CLDGRPH-S27",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~O",
    "surfaced_at": "2026-09-03T19:02Z",
    "one_line": "TO-CG-C-3's measured-defect paragraph names bd-pipeline, cot-pipeline, and inf-pipeline as aws_s3_bucket_notification resources with Lambda targets, but cot-pipeline's complete 19-line resource declares only eventbridge=true and its resolved Terraform state contains lambda_function=[], so no honest cot S3-to-Lambda edge exists.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/cot-pipeline/s3-notifications.tf:16-18: the complete aws_s3_bucket_notification.cot_data block names bucket=aws_s3_bucket.cot_data.id and eventbridge=true; the 19-line file has zero lambda_function blocks and zero lambda_function_arn attributes.",
        "The deriver's own _load_all_tfstate() read of aws_s3_bucket_notification.cot_data resolved bucket/id opal-data-cot, eventbridge=true, and lambda_function=[] on the canonical Terraform declared-side state union.",
        "The read-only targeted live exercise produced 14 S3_BUCKET-[TRIGGERS]->LAMBDA edges and 34/0 notification read state; bd-pipeline contributed three provenance=both targets and inf-pipeline contributed two, while cot-pipeline correctly contributed none."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-C-3 THE CELL says the estate declares real aws_s3_bucket_notification resources with Lambda targets in bd-pipeline, cot-pipeline, and inf-pipeline, and DELIVERABLE 4(a) requires the three declared targets to derive non-zero.",
    "world_is": "bd-pipeline and inf-pipeline declare Lambda notification blocks, but cot-pipeline's notification resource is EventBridge-only in both HCL and resolved state. The implementation derives every real Lambda target and does not fabricate a cot Lambda edge; the acceptance arm remains exercisable using three actual bd-pipeline targets.",
    "notes": "Not blocking the bounded implementation: C3-AC3's non-zero three-target arm is met by the three actual bd-pipeline Lambda configurations, with the two inf-pipeline configurations as additional evidence. Disarm by correcting the face's parenthetical or explicitly naming EventBridge as a different target class outside this cell; no Terraform change belongs here."
  }
]
```

## S28 -- the graph deriver fix is committed but the shared cloud image still requires a separately routed rebuild

```json
[
  {
    "id": "NFRA_CLDGRPH-S28",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~O",
    "surfaced_at": "2026-09-03T19:16Z",
    "one_line": "The C-3 graph-engine fix is locally committed and passes a real read-only derive, but the live derive runner receives comp_aws_cli.py through a shared Docker image tagged latest, so cloud runtime application requires a separately routed image rebuild outside this task's no-deploy bounds.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/modules/graph/comp_aws_cli.py and org/modules/graph/tests/test_comp_aws_s3_notification_state.py: local implementation commit b5bc1c8b27; focused and adjacent tests pass 27/27, and the full read-only derive exits 0 with TRIGGERS=188 and S3 notification reads 34/0.",
        "infra/aws/globgrph/derive_runner.py:101 invokes comp_aws_cli.cmd_derive, while infra/aws/globgrph/Dockerfile:56 copies org/modules/graph/comp_aws_cli.py into the image and Dockerfile:206 starts derive_runner.py.",
        "org/critical_paths/change_management/20260826T0008Z_globgrph-derive-runner-c2c3-compose_deploy_completion.md:79-113 records that the shared globgrph :latest image serves five task definitions: derive, comp_learns_producer, cse_producer, fedobs_producer, and resource_summaries_producer."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-C-3 requires the repaired deriver to be exercised read-only against the real AWS control plane, explicitly forbids deploy/resource/Terraform writes by this seat, and directs the assignee to file a surprise row so the issuer can route an image rebuild if one is required.",
    "world_is": "The repository implementation and its local real-AWS exercise are complete, but the running cloud task will retain the prior comp_aws_cli.py until the shared globgrph image is rebuilt and the relevant task definition is refreshed. That deployment has a five-consumer blast radius and is not authorized by C-3.",
    "notes": "This does not block local C-3 completion or its proof. Disarm by routing and proving the shared-image rebuild/deployment through the existing change-management path, preserving the single canonical derive runner and checking all five consumers; this seat must not perform or imply that deployment."
  },
  {
    "id": "NFRA_CLDGRPH-S29",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-03T19:40Z",
    "one_line": "S26's user-bin deny ACEs are FIXED IN THE WORLD by this seat on Andrew's direct order, and the population was 192 of 211 shims, not the three that were tried; the shared dependency the shims resolve to (.tools) was clean at 0 of 252, so the damage was confined to the forwarders.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Andrew-direct 2026-09-03 ~19:3xZ at the 1.0.0_SA_CTO terminal, VERBATIM: \"fix the shim ACLs, then i have a task for you\" -- this supersedes the S26 ruling-1 clause forbidding user-bin ACL alteration, which bound the 0.8.0_AE_CloudComp~O seat's own conduct, not this seat under a later sovereign order.",
        "PRE-STATE, unscoped census of C:\\Users\\AndrewBerman\\bin: 192 of 211 files carried a non-NULL-SID DENY ACE. The three shims S26 names (comp-to, comp-read, comp-find) were members, NOT the population -- comp-read carried AzureAD\\AndrewBerman:(DENY)(RD,REA,X); most .cmd siblings additionally carried NT AUTHORITY\\SYSTEM:(DENY)(X) and BUILTIN\\Administrators:(DENY)(X); ~10 carried Andrew\\CodexSandboxUsers:(DENY)(X).",
        "SHARED-DEPENDENCY CHECK (CLAUDE.md Rule 22, the members-vs-what-they-share limb): the .tools targets every shim forwards to were censused on their own -- 0 of 252 files carry a non-NULL-SID DENY ACE. The defect is in the forwarder layer only.",
        "AUTHOR: no repo file writes these ACEs. comp-find over 148,214 files for 'icacls|CodexSandboxUsers|AddAccessRule|SetAccessRule|FileSystemAccessRule' returned 11 hits, 0 of them in the shim provisioner and 0 naming CodexSandboxUsers -- so cef249b2f7's provisioner is NOT the author and re-provisioning will not re-write them; the author is the Codex runtime's own Windows sandbox, outside the repo.",
        "ACT: icacls /remove:d for AzureAD\\AndrewBerman, NT AUTHORITY\\SYSTEM, BUILTIN\\Administrators and Andrew\\CodexSandboxUsers across all 211 files. REMOVED-CLEAN 192, STILL-DENIED 0.",
        "POST-STATE, re-censused UNSCOPED (never scoped to the 192 that were touched): 0 of 211 files carry a non-NULL-SID DENY ACE. comp-read's DACL now matches comp-which's shape -- comp-which being the control that worked throughout.",
        "REVERSIBLE: byte-exact pre-state saved by icacls /save /t, 212 entries / 139,848 bytes, restorable with icacls /restore."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S26 asserts the hazard is the three user-bin compiler shims TO-CG-C-3 names (comp-to, comp-read, comp-find) carrying explicit deny entries, with comp-which as the working control, and names 1.0.0_SA_CTO the disarm owner.",
    "world_is": "The hazard's EXTENT was 64x the row's reading: 192 of 211 user-bin shims carried deny ACEs, and the three named are simply the three that a seat happened to invoke -- a census scoped to the members that FAILED could not see the size of the population they belong to. All 192 are now clean (0 of 211 residual, unscoped re-read). EXERCISED only at this Claude/MSYS seat, where all six probed shims return rc=0 -- but that same exercise ALSO passed BEFORE the fix, because the DACL was non-canonically ordered (the ALLOW(F) ACE preceded the DENY, so access was granted before the deny was reached). This seat's exercise is therefore NOT the discriminator; the ACL read is. Whether a Codex seat now resolves these shims is UNEXERCISED and needs a Codex launch to settle.",
    "notes": "DISARM of S26 itself is NOT taken here: remediation rows are 3.0.0_SA_CVO~A's by the channel's own header and by CLAUDE.md section 2, and DISARMED is a remediation-plane state. This row is the disarm EVIDENCE the owner owes; the state flip is routed to the CVO by one message. Two residues deliberately left: the NULL SID:(DENY)(Rc,REA,DC) ACE present on every file including the working control (it matches no token and discriminates nothing), and the Codex sandbox's authorship -- if that runtime re-writes deny ACEs at the next seat launch, this is a recurrence, not a regression of the fix, and the durable remedy is at the launcher, not at the ACL."
  },
  {
    "id": "NFRA_CLDGRPH-S30",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-03T19:55Z",
    "one_line": "CORRECTION to S29 by its own author, on 0.7.0_AE_CloudOps~S's negative control: S29's current-world claim that the residual NULL SID DENY sits on every file including the working control is FALSE, and the deny ACEs were never the cause at all -- the discriminator is BROKEN ACL INHERITANCE on 206 of 211 shims, whose explicit DACLs omit the Andrew\\CodexSandboxUsers grant the parent directory hands down.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "REFUTATION, by 0.7.0_AE_CloudOps~S from an active Codex seat post-S29: absolute-path execution of comp-to.cmd, comp-read.cmd and comp-find.cmd still fails 'Access is denied' before tool execution while comp-which.cmd executes -- so the S29 cleanup did not move the symptom.",
        "S29's FALSE CLAIM, re-measured here and conceded: Get-Acl deny counts were comp-which=1 but comp-which.cmd=0, against comp-read.cmd / comp-to.cmd / comp-find.cmd = 1 each. S29's author read the EXTENSIONLESS bash forwarders, found the NULL SID ACE on all of them, and generalised 'on every file including the working control, therefore it discriminates nothing'. The failing runtime is PowerShell, which executes the .cmd plane, and on THAT plane the ACE was present on exactly the failing shims and absent on the working one. The instrument S29 dismissed as non-discriminating was discriminating; the error is WRONG-OBJECT (right name, wrong plane), the class CLAUDE.md Rule 21 limb (ii) names as out of comp-read's scope.",
        "AND THE CORRECTED READING IS ALSO NOT THE CAUSE. After removing every NULL SID DENY (206 of 211 -> 0 of 211, unscoped re-read), 0.7.0_AE_CloudOps~S re-ran the same control: deny_count=0 on all four AND comp-to/comp-read/comp-find still denied, comp-which still executing. Two successive ACL hypotheses, both refuted by the same agent-side oracle.",
        "THE ACTUAL DISCRIMINATOR, measured on the ALLOW side: the parent C:\\Users\\AndrewBerman\\bin grants Andrew\\CodexSandboxUsers:(OI)(CI)(M), inheritable. 206 of 211 files had inheritance PROTECTED (broken) with explicit DACLs omitting that group, leaving a Codex-sandbox token only Everyone:(R) -- read, NOT execute. The 5 files that still inherited are aws.cmd, comp-glob.cmd, comp-grep.cmd, comp-system.cmd, comp-which.cmd: exactly and only the tools that worked.",
        "REMEDY APPLIED: icacls /reset over the 206 protected files, restoring the inherited DACL. Post-state unscoped on all three axes: inheritance PROTECTED 0 of 211 (was 206); lacking a CodexSandboxUsers ALLOW 0 of 211 (was 187); carrying any DENY 0 of 211 (was 206). comp-read.cmd's DACL is now identical in shape to the comp-which.cmd control.",
        "NOT ACCEPTED, and this is the point of the row: 0.7.0_AE_CloudOps~S's seat PREDATES the cleanup, so a process holding launch-time handles cannot be the acceptance oracle for it. The honest discriminator is a FRESH registered Codex seat launched only through canonical ajb2/start-codex-seat.ps1.",
        "PATH, a SECOND and INDEPENDENT defect on the same route: 0.7.0_AE_CloudOps~S reports C:\\Users\\AndrewBerman\\bin absent from its seat PATH, so bare-name resolution fails even with execution repaired. start-codex-seat.ps1:116-121 DOES prepend $env:USERPROFILE\\bin and add .CMD to PATHEXT -- so this is DESIRED-not-APPLIED for an already-running seat, and the fresh-launch probe is what separates 'the launcher never sets it' from 'this seat predates the launcher change'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S29 asserts the user-bin ACL hazard is fixed in the world, that the residual NULL SID DENY sits on every file including the working control and therefore discriminates nothing, and that only a Codex-seat exercise remains outstanding.",
    "world_is": "The hazard is NOT closed and S29's stated reason for dismissing the residual was wrong twice over. The remedy that matches the evidence is inheritance restoration, now applied and measured on three axes at 0. Whether it CLOSES the hazard is still UNEXERCISED: the only sound oracle is an agent-side execution from a Codex seat launched AFTER the repair, and no such seat has run. S26 must not be disarmed on S29's evidence, nor on this row's.",
    "notes": "The general form, which is why this row is worth its bytes: THREE successive states of this investigation each had a self-consistent instrument that agreed with itself and was wrong -- S26 measured three shims and missed 192; S29 measured the wrong plane and called a live discriminator inert; the NULL-SID removal measured clean and moved nothing. Each time the correction came from the ONE oracle none of them held: an agent-side execution by the consumer, supplied by 0.7.0_AE_CloudOps~S. ACCEPTANCE GATE, 0.7.0_AE_CloudOps~S's specification adopted verbatim as this row's bar: user-bin present on PATH; Get-Command resolves all four shims; direct and bare comp-read --help and comp-find --help execute; comp-which as control; comp-to exercised against a designated probe TO and NOT with --help, which mutates attribution. If a FRESH seat still denies or still lacks PATH, the repair belongs in launcher/runtime provisioning and NOT in further DACL mutation -- this seat has now spent two ACL hypotheses and will not spend a third. Routed to 2.0.0_SA_COO~A, who holds the ajb2 launch under this project; this seat did not self-spawn a seat to grade its own repair."
  }
]
```

## S31 -- one `:latest` tag, seven task families: each worker-scoped rebuild of round 2 and round 3 was a deploy its own controls could not see (the CVO's row, lane ANY)

```json
[
  {
    "id": "NFRA_CLDGRPH-S31",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-04T06:18Z",
    "one_line": "Surfaced at L9 while adjudicating S28: TO-CG-B-2 and TO-CG-C-2 each rebuilt 'the worker image' and each build re-tagged opal-globgrph-derive-runner:latest (16:22Z digest 1e1aaa14..., 18:51Z digest 68bd8b93...), the one tag seven ACTIVE task families pull -- so each worker-scoped act was a deploy to the derive runner, four producers and the serving service at their next launch. Both faces' NEVER-2 ledgers and unscoped re-plans were Terraform-address censuses, which cannot see an image-tag move. Nothing broke that this seat can measure; the class is a deploy whose blast radius its own controls cannot observe. Filed in the investigation document under lane ANY because a remediation row carries its item's id and the C- coordinate lives only in the adjudication document.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ECR describe-images opal-globgrph-derive-runner at 2026-09-04T06:0xZ (3.0.0_SA_CVO): 20260903-162203 = sha256:1e1aaa14... (the digest B2-AC2 cites for revision 2, no longer tagged latest); 20260903-185059 = sha256:68bd8b93... (the digest C2-AC3 cites for revision 3, tagged latest today) -- latest moved between the two builds.",
        "ECS ACTIVE task-definition families containing 'globgrph', latest revision's image, read at this seat: globgrph-projection-worker:3, globgrph-derive-runner:6, globgrph-comp-learns-producer:1, globgrph-cse-producer:1, globgrph-fedobs-producer:1, globgrph-resource-summaries-producer:1 and globgrph-serving:1 all reference .../opal-globgrph-derive-runner:latest by tag, none by digest; globgrph-nessie:5 and globgrph-trino:6 reference vendor images.",
        "TO-CG-C-2 face at HEAD, item 2: 'rebuild the worker image from HEAD of infra/aws/globgrph/ (the derive-runner image pattern), register task-definition revision 3, re-target the Pipe; Terraform for every resource, safe-apply -target'; C2-AC3: the unscoped re-plan 'quoted by address list = the four foreign items and none of this cell's' -- a Terraform-plane control; the tag move is an ECR-plane act no plan renders.",
        "org/critical_paths/change_management/20260826T0008Z_globgrph-derive-runner-c2c3-compose_deploy_completion.md:79-84 names the class for the 08-26 deploy: ':latest REACHES FIVE TASK-DEFS ... all run this ONE image and pick up :latest on their next scheduled fire.' The round-2 and round-3 faces inherited the reach without restating it."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-B-2 and TO-CG-C-2 scope their image act to 'the worker image' with a Terraform-address blast-radius control (targeted apply, one unscoped re-plan quoted by address list) and a NEVER-2 ledger of the worker's resources.",
    "world_is": "The worker has no image of its own: it runs the shared derive-runner image by its :latest tag, and each rebuild re-pointed that tag for seven task families. The controls the faces carried were on the wrong plane to see it; the 08-26 ledger named the class and the faces did not carry it forward.",
    "notes": "Adjudicated in the same commit by ../adjudications/ADJUDICATION_v1.md C-S5 (GRADUATED); remediation row REMEDIATION_v3.md S31, owner 1.0.0_SA_CTO. Not a defect of B-2 or C-2: both did what their faces said; the faces were written against an image topology that does not exist."
  }
]
```

## S32 -- DISARM ACK for S27: cot-pipeline's notification is EventBridge-only; CG-s-14's cell text corrected at decomposition v0.3, no Terraform change

```json
[
  {
    "id": "NFRA_CLDGRPH-S32",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~A",
    "surfaced_at": "2026-09-04T07:05Z",
    "one_line": "S27's disarm act taken by its named owner at the round-4 recut: the decomposition's CG-s-14 cell text (v0.3, this issuance) now reads the declared Lambda targets as bd-pipeline's three and inf-pipeline's two, and names cot-pipeline's aws_s3_bucket_notification.cot_data as eventbridge=true with no Lambda target (infra/aws/terraform/cot-pipeline/s3-notifications.tf:16-19); TO-CG-C-3's terminal face is not edited (append-only record); no Terraform change.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md v0.3 (this issuance's commit; v0.2 @70918d5d2b): s.1a CG-s-14 evidence and closes-on columns carry the correction; changelog row 0.3 records it.",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/ledger/ROUND_ANALYSIS.round3.md @2dd381d969 section 2 item 3: 'One text correction in CG-s-14's cell at the recut ... no Terraform change. Route: the decomposition at the recut (v0.3), the COO's act.'",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/adjudications/ADJUDICATION_v1.md @8fc3921769 C-S3 (the CVO's graduation of S27); REMEDIATION_v3.md @8fc3921769 row S27 (remediation OPEN, owner 2.0.0_SA_COO~A) -- the remediation-plane clock flip is 3.0.0_SA_CVO's on this evidence."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S27 asserts TO-CG-C-3's cell paragraph named cot-pipeline among the Terraform-declared Lambda-notification targets and that the disarm is a correction of that text or an explicit naming of EventBridge as a different target class.",
    "world_is": "The correction is made where the cell text lives from this round on: the decomposition (v0.3). The terminal C-3 face keeps its original wording as the record of what the worker was told; the worker's row S27 and this ack are the two carriers of the correction. Implementation derived no fabricated cot edge (C-3 proof C3-AC3, 14 TRIGGERS edges on the targeted exercise, cot contributing none).",
    "notes": "A factual disarm ack, not an adjudication: no adjudicates field; the DISARMED state on the remediation plane is the CVO's flip citing this row. The issuer also carries the corrected reading into TO-CG-D-1 (CG-s-15) so the cloud exercise's TRIGGERS bar names bd-pipeline's three targets, not 'the three declared'."
  }
]
```

## S33 -- ROUTE ACK for S28: the shared-image rebuild is CG-s-15 (decomposition v0.3) under TO-CG-D-1, change-managed, with this project's three families pinned by digest; the disarm completes on that order's VALID proof

```json
[
  {
    "id": "NFRA_CLDGRPH-S33",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~A",
    "surfaced_at": "2026-09-04T07:05Z",
    "one_line": "S28's route, taken by its named owner: the rebuild of opal-globgrph-derive-runner from a HEAD carrying b5bc1c8b27 is cell CG-s-15 (decomposition v0.3) under task order NFRA_CLDGRPH.TO-CG-D-1 (this issuance), issued to worker 0.9.0_WK_NFRA_CLDGRPH~1 as slot 1's first order, ahead of CG-x-2; NEVER-2 ledger with all seven consumers named; the three families of this project pinned by digest; one real cloud derive proving TRIGGERS > 0 on the live graph. S28's hazard stays ARMED until that proof reads VALID -- this row is the ROUTE, not the disarm.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-D-1.shared-image-rebuild-deriver-live.md (this issuance's commit): owned_cells CG-s-15; criteria D1-AC1..AC8 (the moved digest, the build, the three pins, the cloud denominator line, TRIGGERS > 0, the serving deployment COMPLETED, the ledger CLOSED, the COPY diff as judgment).",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/ledger/ROUND_ANALYSIS.round3.md @2dd381d969 section 2 item 2 (the added cell) and item 4 (the digest pin as S31's inside half); ADJUDICATION_v1.md @8fc3921769 C-S4.",
        "Measured at the cut 2026-09-04 06:2xZ: seven task families reference opal-globgrph-derive-runner:latest (derive-runner 6, projection-worker 3, serving 1, comp-learns 1, cse 1, fedobs 1, resource-summaries 1); ECR latest = sha256:68bd8b932689a331928c1c3a6cc00fe124d24e04e7a9b64ba008f1a2d3de10e8 pushed 2026-09-03 18:51:14Z; the fix commit b5bc1c8b27 authored 19:12:54Z."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S28 asserts the C-3 fix is committed locally but the live derive runner receives comp_aws_cli.py through a shared image tagged latest, so cloud application requires a separately routed image rebuild through the change-management path, preserving the canonical derive runner and checking all five consumers.",
    "world_is": "Routed as above; the consumer count is seven, not five (the 08-26 ledger's five plus the projection worker and the serving service added by this project on 2026-09-03); the route carries the CTO's digest-pin requirement for this project's three families so a later build cannot re-point them silently; the four NFRA_GLOBGRPH families stay on the tag and are named in the ledger.",
    "notes": "The disarm act is the worker's VALID proof on TO-CG-D-1; the issuer records it at the drain and the CVO flips the remediation-plane clock. Until then S28 reads ARMED honestly."
  }
]
```
## W2-S1 -- the safe-apply / safe-ec2-deploy HALT gate refuses EVERY spine-v3 worker serial, so the deploy half of a worker task order cannot execute

```json
[
  {
    "id": "NFRA_CLDGRPH-W2-S1",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~2",
    "surfaced_at": "2026-09-04T08:39Z",
    "one_line": "halt_gate_validate_serial (.tools/halt-gate-check.sh:134-154) accepts a serial only if (1) its base matches an agent HOME FOLDER under org/tier{0_exec,0_utility,1_exec,2_senior,3_junior}/*/ and (2) any ~lane suffix is a SINGLE UPPERCASE LETTER; a spine-v3 worker serial 0.9.0_WK_<CODE>~<n> fails BOTH (no home folder exists for any 0.9.0_WK_* seat -- 112 home folders censused, 0 match; the slot suffix is a DIGIT), so halt_gate_check returns exit 3 (fail-closed) and BOTH world-acting wrappers a worker TO must use -- .tools/safe-apply.sh:70-72 and infra/aws/ec2/safe-ec2-deploy.sh:144-149 -- refuse before any apply/deploy. MEASURED, not inferred: safe-apply on this order's saved targeted plan returned rc=3 with the SERIAL-RESOLVES-TO-NO-KNOWN-AGENT banner. The gate offers HALT_ACK (routine, exit 1) and HALT_OVERRIDE (STOP-class, exit 2) but NO override for exit 3, and its own banner says do not override -- so the worker cannot lawfully proceed. Consequence for TO-CG-D-2: the terraform apply (deliverable step 4) and the EC2 deploy (step 6) did not run; D2-AC3, D2-AC4, D2-AC6 and D2-AC9 record the world as it therefore stands.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/halt-gate-check.sh:134-154 @5644fee152 -- halt_gate_validate_serial: `case \"$lane\" in [A-Z]) : ;; *) return 1 ;;` and the home-folder loop `for tier in tier0_exec tier0_utility tier1_exec tier2_senior tier3_junior; do for d in \"${HALT_GATE_REPO_ROOT}/org/${tier}\"/*/ ... case \"$(basename \"$d\")\" in *\"$base\"*) found=1`.",
        "APPLIED plane, this worktree @5644fee152: `ls -d org/tier*/*/` = 112 home folders; 0 contain '0.9.0'; 0 contain 'WK'. So no folder can substring-match the base 0.9.0_WK_NFRA_CLDGRPH.",
        "MEASURED 2026-09-04 08:3xZ: `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply -input=false .build/cgd2-targeted.tfplan` -> rc=3, banner 'HALT-GATE: SERIAL RESOLVES TO NO KNOWN AGENT -- BLOCKED (fail-closed) / Resolved serial: 0.9.0_WK_NFRA_CLDGRPH~2'. The session serial file org/mcp/sessions/<session>.serial (gitignored, .gitignore:423) was written with this seat's own serial first, per the gate's printed remedy; the second banner is the validator, not the resolver.",
        ".tools/halt-gate-check.sh:8-31 exit-code contract: '0 pass | 1 routine-unacked | 2 stop-block | 3 no-serial'; HALT_ACK covers 1 and HALT_OVERRIDE covers 2 only -- there is no audited path for 3.",
        "infra/aws/ec2/safe-ec2-deploy.sh:144-149 @5644fee152 sources the same library and runs `halt_gate_check \"safe-ec2-deploy:$SERVICE_NAME\" || exit $?`, so the EC2 code-delivery path (CLAUDE.md Rule 12, the ONLY lawful route to the box) is closed to the same seat."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-2 orders `bash .tools/safe-apply` for the targeted apply and `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` for the box deploy, issued to 0.9.0_WK_NFRA_CLDGRPH~2, and forbids a bare terraform apply and any non-Rule-12 route to the box.",
    "world_is": "Both wrappers gate on a serial validator that predates the spine-v3 worker seat and cannot resolve one. The commit lane was taught about workers (.owned-paths.yaml worker_grant @e08447ff7d, 'the task order IS the worker's grant'); the HALT gate was not -- the same half-landed-carrier shape this project keeps finding. The gate's protected property is 'the acting agent has no unread STOP addressed to it', and a worker has no inbox and cannot be messaged at all (its own TO says so), so the property is vacuously true for this seat -- but the gate cannot express that and this seat does not get to rule on it.",
    "notes": "Two disarms are conceivable and BOTH are the CTO's, not this worker's: teach halt_gate_validate_serial the worker grammar (base 0.9.0_WK_<CODE>, digit slot) with a documented worker inbox (or an explicit 'no inbox -> vacuous pass' limb), or mint worker home folders. A third -- an exit-3 audited override -- would weaken the gate for every seat and is NOT recommended from here. Nothing was overridden and no bare terraform apply was run."
  }
]
```

## W2-S2 -- the live gateway ALB carries access_logs that NOTHING in the repo declares, so ANY apply in the module (even a -target'ed one) silently disables a security log feed

```json
[
  {
    "id": "NFRA_CLDGRPH-W2-S2",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~2",
    "surfaced_at": "2026-09-04T08:39Z",
    "one_line": "The LIVE opal-gateway ALB has access_logs {bucket=opal-data-security, prefix=waf-logs/alb-opal-gateway, enabled=true} while infra/aws/terraform/opal-gateway/alb.tf declares NO access_logs at all and the token is absent from the entire repo corpus (LIVE-no-DECLARED); because every listener rule's dependency closure reaches aws_lb.gw, even a strictly -target'ed apply planned `~ update aws_lb.gw` with access_logs.enabled true -> false, i.e. the next apply by ANY seat silently turns that log feed off. Guarded (not repaired) in this order's alb.tf edit with `lifecycle { ignore_changes = [access_logs] }` on aws_lb.gw, which leaves the live setting exactly as found and removes the unrelated diff from the targeted plan.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED 2026-09-04 08:1xZ: `terraform -chdir=infra/aws/terraform/opal-gateway plan -target=aws_iam_role_policy.gw_graph_read_secret_read -target=aws_lb_listener_rule.graph_capability` -> 'Plan: 2 to add, 1 to change, 0 to destroy'; the plan JSON's resource_changes (denominator 7) carried ['update'] aws_lb.gw whose ONLY attribute diff was access_logs [{bucket opal-data-security, prefix waf-logs/alb-opal-gateway, enabled True}] -> [{... enabled False}]. Re-planned with -refresh=false: identical, so the enabled=true is in STATE as well as live.",
        "DECLARED plane @5644fee152: `comp-read infra/aws/terraform/opal-gateway/alb.tf --enumerate 'access_logs'` = 0 hits / 280 lines; `comp-find 'access_logs' infra/aws/terraform` = 0 hits across 496 files scanned [corpus=all]; `comp-find 'waf-logs/alb-opal-gateway'` = 0 hits across 28,361 files scanned. The enablement exists in no repo file.",
        "infra/aws/terraform/opal-gateway/alb.tf @this branch: the aws_lb.gw lifecycle block now carries ignore_changes = [access_logs] with the measurement in a comment naming this row id; after it the same targeted plan's ONLY non-no-op rows are the two addresses this order owns."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-2 orders a 'Targeted safe-apply on exactly your new addresses + the ALB rule' -- i.e. the apply touches this order's two addresses and nothing else.",
    "world_is": "Terraform's -target pulls the dependency closure, and inside that closure sits a pre-existing LIVE-no-DECLARED drift on a security-logging attribute, so 'exactly your new addresses' was NOT achievable as written. The guard makes it achievable without touching the live setting or adjudicating whether enabled=true or the config's silence is authoritative -- that adjudication belongs to the ALB's owner.",
    "notes": "Scope of the guard, stated so it is not read as a fix: Terraform now IGNORES access_logs on aws_lb.gw. If the owner rules that access logging should be declared, the durable act is an access_logs block in alb.tf (and then this ignore_changes line should go). If the owner rules it should be off, the ignore_changes line must go FIRST or the apply will not act. Either way the live world today is unchanged by this order."
  }
]
```

## W2-S3 -- the TO's IntegrationSpec construction omits `description`, a REQUIRED field of the frozen framework dataclass

```json
[
  {
    "id": "NFRA_CLDGRPH-W2-S3",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~2",
    "surfaced_at": "2026-09-04T08:39Z",
    "one_line": "TO-CG-D-2 deliverable step 2 names the spec verbatim as IntegrationSpec(id=..., display_name=..., auth_kind=..., tool_prefix=..., read_only=True, min_tier=..., hosts=(...)), but IntegrationSpec (app/integrations/base.py:47-67) declares `description: str` with NO default between auth_kind and tool_prefix, so the literal construction raises TypeError; the framework is READ-ONLY under this order's bound, so the spec was authored WITH a description (the ycharts specimen carries one at integration.py:29-30) and D2-AC1 then returns [].",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/integrations/base.py:52-60 @2781aac326 (byte-identical at 5644fee152, sha256 718246435530d59e853ed7dca99791d59e1b629e2df516b6a98c3146902cf616): the @dataclass(frozen=True) field order id / display_name / description / auth_kind / tool_prefix, with defaults beginning only at secret_id.",
        "infra/aws/ec2/opal-gateway/app/integrations/ycharts/integration.py:26-43 @5644fee152 -- the live specimen passes description=, confirming the field is populated in practice, not vestigial.",
        "MEASURED: `python -c \"...validate_integration_spec(GlobgrphIntegration().spec)\"` -> 'VALIDATE []' with the description present (D2-AC1)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The TO's step 2 spells the IntegrationSpec argument list in full, as if complete.",
    "world_is": "The argument list is missing one required field. Nothing else in the order changes: the added description is a documentation string, it is not an axis validate_integration_spec scores, and no framework byte moved.",
    "notes": "Filed for form, not significance: the divergence is between the ORDER's text and the frozen framework, and the record should carry which of the two the built artifact follows (the framework)."
  }
]
```

## W2-S4 -- the TO's random_password + secret_version instruction needs a provider this module does not carry, and its enabling files sit OUTSIDE the worker's write grant

```json
[
  {
    "id": "NFRA_CLDGRPH-W2-S4",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~2",
    "surfaced_at": "2026-09-04T08:39Z",
    "one_line": "TO-CG-D-2 deliverable step 4 orders a `random_password` (48 chars, no special) -> aws_secretsmanager_secret + aws_secretsmanager_secret_version in a new graph-read.tf, but the opal-gateway module declares only hashicorp/aws in required_providers (main.tf:16-21) and its lockfile pins only aws + archive, so hashicorp/random would require edits to main.tf and .terraform.lock.hcl -- NEITHER of which is in this order's <paths>; the secret VALUE would also enter TF state, which the module's own standing discipline forbids (secrets.tf:6 'METADATA ONLY -- never aws_secretsmanager_secret_version (the value never enters TF state)'). Built instead the way every other gateway secret is built: the 48-character alphanumeric value minted OUT-OF-BAND via boto3 and referenced metadata-only by a data source, with the scoped GetSecretValue grant the TO also names.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/opal-gateway/main.tf:13-31 @5644fee152 -- required_providers { aws }; backend s3 key opal-gateway/tfstate. `comp-read .terraform.lock.hcl --enumerate 'provider \"registry'` = 2 hits: hashicorp/archive, hashicorp/aws. No random provider on either carrier.",
        "infra/aws/terraform/opal-gateway/secrets.tf:6 and ms-ingest.tf:9-10 @5644fee152 -- the out-of-band discipline, stated twice, for exactly this class of gateway secret.",
        "MEASURED 2026-09-04 08:0xZ: boto3 secretsmanager create_secret -> 'CREATED arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/mcp/graph-read-token-MGAqlV', value 48 characters, isalnum()=True; the value was never printed, never written to a file, and is not in this repo, this row, or any commit.",
        "infra/aws/terraform/opal-gateway/graph-read.tf @this branch -- data \"aws_secretsmanager_secret\" \"graph_read_bearer\" { name = \"opal/mcp/graph-read-token\" } + aws_iam_role_policy.gw_graph_read_secret_read scoped to that data source's .arn, copying ycharts-iam.tf's shape."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Step 4 names random_password + aws_secretsmanager_secret + aws_secretsmanager_secret_version as the construction, while the same order's <paths> grants only graph-read.tf and alb.tf inside the terraform module.",
    "world_is": "The named construction is unexecutable inside the grant and contradicts the module's own secret discipline; the out-of-band form is executable, keeps the value out of TF state, and leaves the declared IAM shape the TO asked for byte-for-byte comparable to ms-ingest.tf / ycharts-iam.tf.",
    "notes": "The secret EXISTS and is inert: with the grant unapplied (W2-S1) nothing can read it, and no consumer references it until the deploy lands. It is not a stranded half-deploy, it is the first leg of one -- recorded on the NEVER-2 ledger cldgrph-cgd2-gateway-graph-path leg L2."
  }
]
```

## W2-S5 -- D2-AC9's own invocation can never show a CLOSED ledger: `deploy_ledger.py close` DELETES the sentinel that `list` reads

```json
[
  {
    "id": "NFRA_CLDGRPH-W2-S5",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~2",
    "surfaced_at": "2026-09-04T08:39Z",
    "one_line": "D2-AC9 names invocation `python .tools/deploy_ledger.py list` with expectation `cldgrph-cgd2-gateway-graph-path.*CLOSED`, but cmd_list is a straight delegation to cmd_check (deploy_ledger.py:1240-1242) which reports OPEN / HELD-STALE / BYPASS entries from the sentinel state files, and cmd_close (:353-368) sets status CLOSED, writes the change_management entry and then UNLINKS the sentinel -- so a CLOSED slug is by construction ABSENT from `list` output and the criterion's expectation is unsatisfiable by its own invocation on ANY task order, not just this one. The state that criterion means to assert is carried by the entry FILE's `**Status:** CLOSED` line.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/deploy_ledger.py:1240-1242 @5644fee152 -- `def cmd_list(args) -> int: return cmd_check(argparse.Namespace(window_hours=None, red=False, held_stale_days=DEFAULT_HELD_STALE_DAYS))`.",
        ".tools/deploy_ledger.py:353-368 @5644fee152 -- cmd_close: `state[\"status\"] = \"CLOSED -- nothing stranded\"; ... _write_entry(state); _state_path(args.slug).unlink()`.",
        "MEASURED 2026-09-04 08:0xZ: `python .tools/deploy_ledger.py list` printed 3 OPEN/HELD entries + 8 BYPASS lines + 'SCAN DENOMINATOR: 4 of 4 sentinel(s) scanned' -- every printed row is a non-terminal entry; no CLOSED row appears anywhere in the output shape."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "D2-AC9 asserts that after a proven close, `deploy_ledger.py list` output matches `cldgrph-cgd2-gateway-graph-path.*CLOSED`.",
    "world_is": "`list` enumerates only non-terminal entries; closing removes the slug from its universe. A criterion cut in this shape would read FAIL on a perfectly closed ledger and can only 'pass' while the ledger is still OPEN -- inverted. The sound oracle is `**Status:**` inside org/critical_paths/change_management/<stamp>_<slug>_deploy_completion.md, or `deploy_ledger.py check` returning rc 0 with the slug absent.",
    "notes": "Prospective: the next cut of any TO carrying a NEVER-2 ledger criterion should name the entry file's Status line (or check's rc + absence) rather than a grep of `list`. On THIS order the point is moot in a second way -- the ledger could not be closed at all, because W2-S1 blocked the legs it would have to prove."
  }
]
```

## W2-S6 -- `ps -o args -C python3.11` returns only its header on the gateway box; the running argv is reachable via the unit's MainPID

```json
[
  {
    "id": "NFRA_CLDGRPH-W2-S6",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~2",
    "surfaced_at": "2026-09-04T08:39Z",
    "one_line": "D2-AC7 names an SSM `ps -o args -C python3.11` on i-07dccb1615503ac99; run verbatim it prints the bare header 'COMMAND' and no row (SSM 2b69d667-a3ef-42ad-a7c7-2ea44beef1bc, Status Success), so the criterion's expectation `--workers 1` would read FAIL while the gateway is in fact running with exactly one worker. The unit's MainPID argv is the oracle that answers: MainPID=539593 -> `/opt/opal-gateway/.venv/bin/python3.11 /opt/opal-gateway/.venv/bin/uvicorn app.server:app --host 0.0.0.0 --port 8080 --workers 1`.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "0.9.0_WK_NFRA_CLDGRPH~2",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED 2026-09-04 08:3xZ, SSM CommandId 2b69d667-a3ef-42ad-a7c7-2ea44beef1bc on i-07dccb1615503ac99, Status Success: StandardOutputContent = 'COMMAND\\nactive\\n' -- the ps -C selector matched no process.",
        "MEASURED 2026-09-04 08:3xZ, SSM CommandId 81190559-8075-40a7-b930-7f73b69db6bd, Status Success: PROBE-1 (the same ps -C form) again printed only 'COMMAND'; PROBE-2 printed 'MainPID=539593' then '/opt/opal-gateway/.venv/bin/python3.11 /opt/opal-gateway/.venv/bin/uvicorn app.server:app --host 0.0.0.0 --port 8080 --workers 1'; PROBE-3 'active'.",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/box_workers.sh @this branch -- the script keeps the TO's named ps form as PROBE-1 (so the negative is on the record) and adds the MainPID argv read as PROBE-2."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "D2-AC7 assumes `ps -o args -C python3.11` on the box lists the uvicorn process carrying `--workers 1`.",
    "world_is": "It lists nothing (the selector does not match this process's comm on this box), while the process itself carries --workers 1 unchanged. Disarmed in-place by widening the worker's own script, which is the deliverable the criterion invokes; the criterion's expectation is met by PROBE-2's line in the same output.",
    "notes": "This order deployed nothing (W2-S1), so the argv read is a measurement of the PRE-EXISTING running gateway -- it proves --workers 1 was not touched, and proves nothing about a deploy that did not happen."
  }
]
```
## W2-S7 -- the NEVER-2 ledger's SENTINEL lives outside the task order's write grant, so an OPEN entry cut by a worker cannot travel with its branch

```json
[
  {
    "id": "NFRA_CLDGRPH-W2-S7",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~2",
    "surfaced_at": "2026-09-04T09:15Z",
    "one_line": "deploy_ledger.py writes TWO carriers per entry: the human record org/critical_paths/change_management/<stamp>_<slug>_deploy_completion.md and the machine SENTINEL org/critical_paths/.open_deploys/<slug>.json that `check`/`list` actually enumerate. TO-CG-D-2's <paths> grants org/critical_paths/change_management/ and NOT org/critical_paths/.open_deploys/, and sentinels are TRACKED files (26 of them under git ls-files, not gitignored) -- so this worker committed the entry MD and left the sentinel untracked in its worktree. Consequence: when this branch is compiled, the COO's `deploy_ledger.py check --red` will NOT see this OPEN entry through the sentinel index; it surfaces only through the SECOND limb, the change_management/*.md sweep, as 'BYPASS: UNINDEXED OPEN LEDGER'. The entry still blares, but in the finding class that means 'a ledger with no sentinel' rather than 'an open deploy'.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/deploy_ledger.py:155-156 (_state_path) and :166-169 (_save) + :222-224 (_write_entry) @5644fee152 -- every state change writes both the sentinel JSON and the entry MD; cmd_check enumerates sentinels (its own output line 'SCAN DENOMINATOR: 5 of 5 sentinel(s) scanned') and separately sweeps change_management/*.md for entries with no sentinel, printing them as 'BYPASS: UNINDEXED OPEN LEDGER'.",
        "MEASURED in this worktree 2026-09-04 09:1xZ: `git status --porcelain` after both commits shows exactly one residue line, '?? org/critical_paths/.open_deploys/cldgrph-cgd2-gateway-graph-path.json'; `git check-ignore -v` on it prints NOTHING (not ignored) while `git ls-files org/critical_paths/.open_deploys/` lists tracked sentinels -- so the file is committable in principle and simply outside this order's grant.",
        "org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-D-2.gateway-traversal-integration.md <paths> block: 'org/critical_paths/change_management/' is listed; no other org/critical_paths/ path is."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order binds NEVER-2 ('open a deploy ledger BEFORE the first apply/deploy act with every leg; close each leg with proof; close the entry') and grants org/critical_paths/change_management/ as the write surface for it.",
    "world_is": "The instrument NEVER-2 names writes a second, tracked carrier one directory up, which the grant does not cover -- so a worker can open a ledger it cannot fully commit. Nothing was written outside the grant: the sentinel is left untracked and named here instead.",
    "notes": "Prospective and cheap: add org/critical_paths/.open_deploys/ to the <paths> of any task order that binds NEVER-2, or have the compiling seat run `deploy_ledger.py` state ops in the tree it will merge into. This row is filed for the ROUTE, not as a defect of the tool: two carriers is the tool's design, and the second limb is exactly why the entry is not invisible."
  }
]
```

## NFRA_CLDGRPH-W1-S1 -- safe-apply's halt gate refuses the spine-v3 WORKER serial grammar, so no L7 worker subagent can run any terraform apply

```json
[
  {
    "id": "NFRA_CLDGRPH-W1-S1",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~1",
    "surfaced_at": "2026-09-04T08:32Z",
    "one_line": "TO-CG-D-1 step 3 routes its apply through `bash .tools/safe-apply`, which fires `.tools/halt-gate-check.sh` before terraform. That gate's `halt_gate_validate_serial` refuses `0.9.0_WK_NFRA_CLDGRPH~1` on BOTH of its two limbs -- the `~1` lane suffix is a DIGIT where the gate requires a single `[A-Z]`, and the base `0.9.0_WK_NFRA_CLDGRPH` matches no agent home folder under the five tier dirs it scans (105 folders, 0 matches). The identity refusal returns 3 at :274, BEFORE the `HALT_OVERRIDE` consultation at :360, so no audited override can reach it. terraform is never invoked. The three digest pins (D1-AC3), the apply (L4), the serving rollout (D1-AC6) and the ledger close (D1-AC7) are unreachable by this seat.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/halt-gate-check.sh:134-166 @5644fee152 -- `halt_gate_validate_serial()`: `lane=\"${serial#*~}\"; case \"$lane\" in [A-Z]) : ;; *) return 1 ;; esac` and a `for tier in tier0_exec tier0_utility tier1_exec tier2_senior tier3_junior` loop requiring `*\"$base\"*` to match a home folder basename",
        ".tools/halt-gate-check.sh:259-275 @5644fee152 -- the validator failure renders the 'SERIAL RESOLVES TO NO KNOWN AGENT' banner and `return 3`; .tools/halt-gate-check.sh:360 is where `HALT_OVERRIDE` is consulted, inside the LATER 'Verdict 3: STOP-class present' branch, so line order makes the override unreachable from an identity refusal",
        "MEASURED, EMPIRICAL (a second instrument, not a re-read of the source): `HALT_OVERRIDE=\"probe...\" HALT_ACK=1 bash .tools/safe-apply.sh apply -input=false -no-color -target=aws_ecs_task_definition.derive_runner` -> the identity banner again, rc 3, terraform never invoked. Both env-var escapes set at once and the gate still fails closed.",
        "CENSUS of the exact five tier dirs the validator scans, run with the validator's own `case ... in *\"$base\"*` shape: DENOMINATOR 105 home folders; matches for base `0.9.0_WK_NFRA_CLDGRPH` = 0; matches for any `*_WK_*` or `0.9.0*` folder = 0. POSITIVE CONTROL on the identical loop: `2.0.0_SA_COO` returns 3 (org/tier1_exec/2.0.0_SA_COO/, ~A/, ~X/), so the zero is an ABSENCE and not a broken loop.",
        "The serial itself resolves correctly -- the gate PRINTS 'Resolved serial: 0.9.0_WK_NFRA_CLDGRPH~1' after `org/mcp/sessions/<session>.serial` was written per the gate's own first banner. The failure is VALIDATION, not resolution."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-1 STANDING LAW forbids a bare `terraform apply` and routes every apply through `bash .tools/safe-apply` targeted on named addresses; the deliverable's step 3 and ledger leg L4 are written on the premise that an L7 worker subagent CAN complete that apply. CLAUDE.md rule 27 seats L7 execution in worker subagents serialled `0.9.0_WK_<CODE>~<n>`, whose lane suffix is by construction a DIGIT.",
    "world_is": "The spine-v3 worker serial grammar (`~<n>`, digit, no home folder) and the halt gate's serial contract (`~[A-Z]`, home folder required) are mutually exclusive, and the gate fails closed with no reachable override. Every terraform apply in the fabric is therefore closed to every L7 worker subagent, not just to this one -- the two carriers were authored against different seat grammars and this is the first spine-v3 worker to route an apply through the gate. The gate is behaving exactly as designed (it refuses to scan a nonexistent inbox); the defect is the missing worker limb in its resolver contract, the same limb the `.owned-paths.yaml worker_grant` stanza @e08447ff7d added on the COMMIT plane and that the halt gate has not received.",
    "notes": "NOT an argument for an override: overriding an identity-class refusal means applying while blind to one's own STOP inbox, and the gate says so at :249. Disarm = give `halt_gate_validate_serial` a worker limb that admits `0.9.0_WK_<CODE>~<n>` (digit suffix, no home folder) and points its inbox scan at whatever a worker's inbox is -- or an explicit ruling that L7 workers never apply and the apply limb of a TO belongs to a lane seat. Owner set to `1.0.0_SA_CTO` because the CTO owns the resolver limb the worker_grant stanza @e08447ff7d was cut for and `.tools/` is that lane; if `3.0.0_SA_CVO` routes it elsewhere at L9 this assignment is superseded -- surfaced, not adjudicated. BLAST RADIUS beyond this TO: every future spine-v3 worker TO whose deliverable includes a terraform apply."
  }
]
```

## NFRA_CLDGRPH-W1-S2 -- the targeted apply's address set is 8, not the 4 the TO names; two IAM policies pin the OLD task-definition revisions

```json
[
  {
    "id": "NFRA_CLDGRPH-W1-S2",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~1",
    "surfaced_at": "2026-09-04T08:20Z",
    "one_line": "TO-CG-D-1 names FOUR apply addresses (the three task definitions + `aws_pipes_pipe.projection_worker`). The measured plan shows EIGHT: the four named plus `aws_iam_role_policy.derive_runner_events_ecs`, `aws_iam_role_policy.projection_pipe`, `aws_cloudwatch_event_target.derive_runner_nightly` and `aws_ecs_service.globgrph_serving`. The two IAM role policies hard-code the task-definition ARN AT ITS REVISION (`globgrph-derive-runner:6`, `globgrph-projection-worker:3`) as their `ecs:RunTask` Resource, so a four-address apply would leave the EventBridge nightly rule and the Pipe authorized ONLY for the revisions the same apply just superseded -- the nightly derive and every Pipe-launched projection worker would fail AccessDenied, silently, from the next fire.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "UNSCOPED `terraform plan` (saved at org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/unscoped_plan_pre.txt, run 2026-09-04 08:1xZ against the live S3 backend globgrph/tfstate): 13 resource addresses, `Plan: 5 to add, 8 to change, 3 to destroy.`",
        "unscoped_plan_pre.txt -- `aws_iam_role_policy.derive_runner_events_ecs` diff carries `- Resource = \"arn:aws:ecs:us-east-1:313476888478:task-definition/globgrph-derive-runner:6\"` under `Sid = \"RunECSTask\"`; `aws_iam_role_policy.projection_pipe` carries `- Resource  = \"arn:aws:ecs:us-east-1:313476888478:task-definition/globgrph-projection-worker:3\"` under `Sid = \"RunProjectionTask\"`",
        "TARGETED plan on the eight addresses (targeted_plan.txt): `Plan: 3 to add, 5 to change, 3 to destroy.`, exactly those eight and no foreign address; `Changes to Outputs` = the single output `derive_runner_task_definition_arn`",
        "Every one of the four ADDITIONAL addresses changes ONLY because a task-definition ARN moves: a census of every task-definition ARN line in the plan diff returns 12 lines, all of the form `:6`/`:3`/`:1` -> `(known after apply)`; my own diff (git diff -- infra/aws/terraform/globgrph/) touches ONLY one `locals` entry and three `image` lines and no IAM, event-target or service text",
        "PRECEDENT agreeing: TO-CG-C-2's result (org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~S/CG-s-2.worker-revision-three.result.md `terraform.targets`) applied THREE addresses for one task-definition bump -- `aws_ecs_task_definition.projection_worker`, `aws_iam_role_policy.projection_pipe`, `aws_pipes_pipe.projection_worker` -- i.e. it already carried the IAM policy that this TO's four-address list drops"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-1 deliverable step 1 leg L4 and step 3: `safe-apply` targeted on 'exactly the three task-definition addresses + the Pipe target update', and the BOUNDS clause 'Terraform edits are exactly: one local, three image lines, the Pipe target reference.'",
    "world_is": "The EDIT set the TO bounds is correct and sufficient -- I made exactly those edits and no others. The APPLY set is not: a task-definition replacement drags four dependents that `-target` does not pull in, because `-target` includes a resource's dependencies and never its DEPENDENTS. Two of those four are `ecs:RunTask` grants scoped to the superseded revision. The TO's four-address list would have produced a green apply and a nightly derive that cannot start.",
    "notes": "NOT acted on beyond planning: the apply is blocked by NFRA_CLDGRPH-W1-S1, so the eight-address set is a MEASURED PLAN and not an APPLIED state -- DESIRED, not APPLIED, and this row says so rather than claiming the wider set works. Whoever completes the apply should use the eight addresses, not four; the targeted plan proving all eight and no foreign address is saved at targeted_plan.txt. Owner is the issuer because it is the task order's address list that needs the correction."
  }
]
```

## NFRA_CLDGRPH-W1-S3 -- the globgrph terraform state carries seven root outputs its config no longer declares, residue of the 858554332d targeted teardown

```json
[
  {
    "id": "NFRA_CLDGRPH-W1-S3",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~1",
    "surfaced_at": "2026-09-04T08:20Z",
    "one_line": "An unscoped `terraform plan` on infra/aws/terraform/globgrph shows SEVEN root outputs being removed (`-> null`) that no resource change accompanies -- `freeze_monitor_lambda_arn`, `freshness_alarm_lambda_arn`, `freshness_stale_alarm_arns` (10 ARNs), `parity_drift_alarm_arns` (2 ARNs), `tool_activity_freshness_lambda_arn`, `tool_activity_stale_alarm_arn`, `tool_activity_telemetry_stale_alarm_arn`. They are state residue of commit 858554332d, an authorized freshness teardown applied with `-target`: the RESOURCES were destroyed and the `output` blocks deleted from config, but a targeted apply does not reconcile root outputs, so the state still advertises ARNs for CloudWatch alarms and Lambdas that no longer exist.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/unscoped_plan_pre.txt:561-585 -- `Changes to Outputs:` with seven `- <name> = \"<arn>\" -> null` entries and NO corresponding resource in the plan's 13-address list",
        "comp-find 'output \"(freeze_monitor_lambda_arn|...|tool_activity_telemetry_stale_alarm_arn)\"' over infra/aws/terraform/globgrph -> 0 hits across 27 files; POSITIVE CONTROL on the same alternation instrument, 'globgrph_serving_port|opal-globgrph-derive-runner' -> 28 hits, so the zero is an ABSENCE and not a broken pattern",
        "git log -3 --diff-filter=D -- infra/aws/terraform/globgrph/ -> 858554332d 'teardown(globgrph freshness): remove freshness_alarm.tf + tool_activity_freshness.tf + freshguard_derive_watchdog.tf + item2d_freeze_monitor.tf ... (44 destroy). ... -target apply excludes ~D's COMPSIMILAR resource_summaries creates + the parked andrew@ critical-surface sub (both stay). git-recoverable; CTO GO 235109Z' -- the teardown was AUTHORIZED and its `-target` scope is exactly why the outputs survived",
        "The stale outputs are NOT touched by this order's targeted plan: targeted_plan.txt `Changes to Outputs` carries the single entry `derive_runner_task_definition_arn`"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Nothing in TO-CG-D-1 speaks to these outputs; the order asks only that ONE unscoped plan be saved and asserted by address list to contain none of this seat's addresses beyond the known foreign items. This row is what that control SAW while looking for something else.",
    "world_is": "The module's remote state (s3 opal-313476888478-terraform-state, key globgrph/tfstate) publishes seven output values naming CloudWatch alarms and Lambda functions that the 858554332d teardown destroyed. Any consumer reading this module's outputs -- a remote_state data source, an operator, a graph builder -- reads live-looking ARNs for resources that do not exist, and the read cannot tell the difference. This is the DESIRED-vs-APPLIED split on the OUTPUT plane rather than the resource plane.",
    "notes": "INERT for this order (the targeted apply leaves them alone) but ARMED for the estate: the next UNSCOPED apply in this module silently removes them, and until then any output consumer is misinformed. Disarm = an unscoped apply in this module (removes the seven outputs and also lands the four foreign items already sitting in the plan), or a deliberate `terraform state` reconciliation. Owner `0.7.0_AE_CloudOps` as the module's lane and the author of 858554332d. Do NOT read this row as authorizing an unscoped apply -- the same plan carries a `stitch_produce` buildspec re-render and three glue-partition changes nobody has adjudicated."
  }
]
```

## NFRA_CLDGRPH-W1-S4 -- the deploy ledger has no `exercise` leg kind, and safe-apply is `.tools/safe-apply.sh`

```json
[
  {
    "id": "NFRA_CLDGRPH-W1-S4",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~1",
    "surfaced_at": "2026-09-04T07:56Z",
    "one_line": "Two naming divergences between TO-CG-D-1's deliverable text and the tools it names, both resolved without widening the order: (a) the TO declares legs L5/L6/L7 as kind `exercise`, which `.tools/deploy_ledger.py` refuses -- `LEG_KINDS = {git, s3-prefix, activation, ec2-baked-asset, verify, tf-lambda}` and an unknown kind is a hard `sys.exit`; the three legs were opened as `verify`, the kind whose documented meaning ('post-deploy live-state check') is exactly what the TO describes, with the TO's leg ids and proof text carried verbatim. (b) the TO writes `bash .tools/safe-apply`; the executable is `.tools/safe-apply.sh` and the bare name does not exist.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/deploy_ledger.py:69 @5644fee152 -- `LEG_KINDS = {\"git\", \"s3-prefix\", \"activation\", \"ec2-baked-asset\", \"verify\", \"tf-lambda\"}`; :299-300 -- `if kind not in LEG_KINDS: sys.exit(f\"ERROR: leg kind '{kind}' not in {sorted(LEG_KINDS)}\")`. `exercise` is absent, so the TO's literal text would have failed the `open` call outright.",
        ".tools/deploy_ledger.py module docstring 'Leg kinds' table @5644fee152 -- `verify  post-deploy live-state check (0-diff plan, smoke, served artifact read)`, which is the definition L5/L6/L7 are written to",
        "`ls -l .tools/safe-apply*` -> a single file, `.tools/safe-apply.sh` (17184 bytes); `sed -n '1,60p' .tools/safe-apply` -> `sed: can't read .tools/safe-apply: No such file or directory`, rc 2",
        ".tools/safe-apply.sh:20-21 @5644fee152 -- its own usage line is `.tools/safe-apply.sh [-chdir=DIR] apply [apply-args...]`",
        "The ledger opened successfully with the substitution: `OK: OPENED deploy ledger 'cldgrph-cgs15-shared-image-digest-pins' (7 legs)` -> org/critical_paths/change_management/20260904T0756Z_cldgrph-cgs15-shared-image-digest-pins_deploy_completion.md, with L5/L6/L7 listed as `[verify]`"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-1 deliverable step 1 names seven legs of which 'L5 exercise', 'L6 exercise' and 'L7 exercise' are three; STANDING LAW and step 3 name `bash .tools/safe-apply`.",
    "world_is": "`exercise` is not a leg kind the ledger contract defines, and `.tools/safe-apply` is not a path that exists. Both are surface-naming drift between the cut and the tools, not substantive divergence: `verify` carries the same proof discipline and `.tools/safe-apply.sh` is the same gate. Filed because a worker face is the worker's whole context, so a name in it that the world refuses is a defect in the cut even when the fix is obvious -- and the next worker reading the same TO spends the same two discovery steps.",
    "notes": "INERT: no hazard, no disarm owner needed; both were resolved in-lane at zero cost to the deliverable. Recorded so the issuer can correct the TO template rather than have each worker re-derive it. NOT to be confused with W1-S1, which is the same file family (`.tools/safe-apply.sh`) but a real BLOCKING refusal rather than a name."
  }
]
```

## NFRA_CLDGRPH-W1-S5 -- non-ASCII in 8 of 22 terraform files in the globgrph module

```json
[
  {
    "id": "NFRA_CLDGRPH-W1-S5",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~1",
    "surfaced_at": "2026-09-04T08:10Z",
    "one_line": "CLAUDE.md section 4 states 'No non-ASCII in production code/logs/AWS'. A byte census of infra/aws/terraform/globgrph finds 99 non-ASCII bytes across 8 of 22 `.tf` files -- item2b.tf 35, nessie.tf 23, item2a.tf 17, main.tf 9, vpc_endpoints.tf 6, glue_code_heat.tf 3, iam.tf 3, tool_activity.tf 3 -- em-dashes and arrows in comments and headers, all pre-existing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "In-process byte census over `infra/aws/terraform/globgrph/*.tf`, counting bytes > 127 per file: DENOMINATOR 22 `.tf` files scanned, 8 carry non-ASCII, 99 bytes total. Per file: item2b.tf 35, nessie.tf 23, item2a.tf 17, main.tf 9, vpc_endpoints.tf 6, glue_code_heat.tf 3, iam.tf 3, tool_activity.tf 3.",
        "infra/aws/terraform/globgrph/item2a.tf:342 @5644fee152 -- `# ECS Task Definition -- derive-runner` renders with an em-dash, inside the resource block this order edits at :359",
        "infra/aws/terraform/globgrph/main.tf:2 @5644fee152 -- `# NFRA_GLOBGRPH -- Versioned Global Opal Graph Platform` and :4 an arrow glyph in `EventBridge -> SQS -> Lambda`",
        "The bytes are all in COMMENTS, not in any string that reaches an AWS API: the census location per file is a `#` line in every case inspected, and the module applies cleanly"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md section 4: 'No non-ASCII in production code/logs/AWS -- use OK:/WARN:/ERROR:/SKIP:/BLOCKED:.'",
    "world_is": "The globgrph terraform module carries 99 non-ASCII bytes across 8 of its 22 `.tf` files, entirely in comments, entirely pre-existing. My own edits to three of those files are ASCII-only and `terraform fmt -check` on all three returns rc 0.",
    "notes": "INERT and deliberately NOT remediated: fixing it would be widening this order (two of the eight files are outside this order's PATHS block, and the rule against fixing a neighbouring defect binds). Filed as a census with its denominator so whoever owns the module's hygiene has the whole population rather than the one line I happened to read. No disarm owner named because nothing is armed -- this is a standards observation, not a hazard."
  }
]
```

## NFRA_CLDGRPH-W1-S6 -- sibling worker subagents share ONE scratchpad directory, and a same-named file is silently overwritten between them

```json
[
  {
    "id": "NFRA_CLDGRPH-W1-S6",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~1",
    "surfaced_at": "2026-09-04T08:43Z",
    "one_line": "Worker subagents spawned for the same project share ONE absolute scratchpad directory keyed by the parent session id, not by worker slot. I wrote my five draft surprise rows to <scratchpad>/rows.md; minutes later that exact file held SIX rows all carrying surfaced_by 0.9.0_WK_NFRA_CLDGRPH~2 and none of mine. The overwrite is silent -- no lock, no error, no rename -- and the harness surfaced it only as an incidental 'file changed on disk' notice whose default advice is to ACCEPT the new content as current.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The scratchpad path handed to this seat is C:/Users/ANDREW~1/AppData/Local/Temp/claude/C--Users-AndrewBerman-Desktop-ajb-workspace/3e63c2d6-a07e-4ea6-9780-7be73730e12c/scratchpad -- keyed by the session id 3e63c2d6-a07e-4ea6-9780-7be73730e12c, with NO worker-slot component; the same id also names the halt gate's session serial file org/mcp/sessions/3e63c2d6-....serial, so both workers resolve the same session key.",
        "MEASURED after the overwrite: `grep -oE 'surfaced_by\": \"[^\"]+\"' <scratchpad>/rows.md | sort | uniq -c` -> `6  surfaced_by\": \"0.9.0_WK_NFRA_CLDGRPH~2\"` and ZERO occurrences of ~1. The file I authored minutes earlier held 5 rows, all ~1.",
        "The content that replaced mine is another worker's draft for a DIFFERENT task order (rows NFRA_CLDGRPH-W2-S1..S6, TO-CG-D-2, gateway ALB / opal-gateway module) -- so the collision is across task orders, not merely across two drafts of one.",
        "NEGATIVE CONTROL on the blast radius, run in this worktree: the committed channel file org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md holds 5 rows matching '\"id\": \"NFRA_CLDGRPH-W1-S' and 0 matching '\"id\": \"NFRA_CLDGRPH-W2-S'. The git worktrees are separate and were NOT cross-contaminated; only the shared /tmp-class scratchpad was.",
        "My append to the channel happened BEFORE the overwrite (the append reported 37 row ids and a 1173-line file), which is the only reason no evidence was lost here -- timing, not a control."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The worker face gives each worker its own git worktree and its own deliverables folder as its isolation boundary, and the standing scratchpad instruction says to use the given directory for ALL temporary files -- both of which read as 'this seat has a private working surface'.",
    "world_is": "Isolation is per-WORKTREE, not per-SEAT: the scratchpad is shared by every worker subagent under one parent session. A worker that stages a deliverable, a commit message file, a plan output or a draft row under a generic name in that directory can have it replaced by a sibling between the write and the read, with no error at either end. The failure mode is silent substitution of ANOTHER SEAT'S content under this seat's authorship -- an attribution defect, and the two artifacts would agree with each other while both being wrong about who wrote what.",
    "notes": "MITIGATED here, not repaired: this row was staged to a serial-qualified filename (rows_0.9.0_WK_NFRA_CLDGRPH~1_S6.md) rather than a generic one, and every load-bearing artifact of this order was written directly into the worktree deliverables folder instead of the scratchpad. Recommended disarm for the issuer: instruct workers to qualify every scratchpad filename with their serial, or stage under the worktree only. Owner is the issuer as the spawner of the sibling workers. Note the near-miss class: a commit message file staged in the shared scratchpad under a generic name and then passed to safe-commit -F would commit ANOTHER SEAT'S text under this seat's author line -- CLAUDE.md rule 14a already requires a non-shell writer for that file, but says nothing about a shared path."
  }
]
```

## NFRA_CLDGRPH-W1-S7 -- the silent-zero TRIGGERS defect is an IAM GAP: the cloud derive role cannot read S3 bucket notifications on ANY bucket (read=0 / unreadable=34)

```json
[
  {
    "id": "NFRA_CLDGRPH-W1-S7",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~1",
    "surfaced_at": "2026-09-04T08:49Z",
    "one_line": "The C-3 fix worked exactly as designed and its first cloud run NAMES the cause of S20's silent zero: the ad-hoc derive on the rebuilt image printed `s3 notifications buckets read=0 / buckets unreadable=34` and enumerated all 34 buckets as unreadable. The derive task role `opal-globgrph-derive-runner-task` is granted s3:GetBucketPolicy, GetBucketVersioning, GetBucketLocation, ListAllMyBuckets, GetObject, PutObject, DeleteObject and ListBucket -- and NOT s3:GetBucketNotification, which is the API that yields every S3_BUCKET-[TRIGGERS]->LAMBDA edge. So TRIGGERS on the cloud-derived graph is structurally 0 and will stay 0 on the 02:00Z nightly no matter how many times the image is rebuilt. The laptop derive's 34 read / 0 unreadable and TRIGGERS=188 came from a DIFFERENT PRINCIPAL (the Andrew_Berman IAM user), not from different code.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED plane, CloudWatch /ecs/globgrph/derive-runner stream derive-runner/derive-runner/7286e56c80614ab49fa2fba791bb8b43 (ad-hoc QA derive, task 7286e56c80614ab49fa2fba791bb8b43, imageDigest sha256:1b89853fe44133f10a60dc2b3e7b463c0d3b68b827a2ddff249bf427ecde2778, exit 0, startedAt 1788511057.509 stoppedAt 1788511860.622): `s3 notifications buckets read=0 / buckets unreadable=34; unreadable=opal-313476888478-globgrph,...,opalinvest-portal` -- all 34 named, none omitted.",
        "APPLIED plane, iam get-role-policy over every inline policy of role opal-globgrph-derive-runner-task (list-role-policies DENOMINATOR 4: DeriveRunnerAccountDescribe, DeriveRunnerCWLogs, DeriveRunnerS3, DeriveRunnerSNS; list-attached-role-policies = EMPTY, so the 4 inline documents are the WHOLE grant): the complete S3 action set is s3:GetBucketPolicy, s3:GetBucketVersioning, s3:GetBucketLocation, s3:ListAllMyBuckets (Sid AccountWideReadOnly) and s3:GetObject, s3:PutObject, s3:DeleteObject, s3:ListBucket, s3:GetBucketLocation (Sids GlobgrphWarehouseRW, TerraformStateRead, P4CrossDomainServedRead). s3:GetBucketNotification is absent, and no statement carries a wildcard action.",
        "DESIRED plane: comp-find 'GetBucketNotification' over infra/aws/terraform -> 0 hits across 495 files scanned [corpus=all]. POSITIVE CONTROL on the same instrument and scope: 'GetBucketLocation' -> 15 hits. The zero is an ABSENCE, not a broken pattern -- the grant is declared nowhere in the estate's terraform, so this is a gap in the DECLARATION, not drift between declaration and application.",
        "SERVED plane, before this derive: triggers_query.sh against the live serving process (SSM to i-07dccb1615503ac99 -> projection.opal-globgrph.local:8181/cypher) returned `{\"rows\":[{\"triggers\":0}],\"vintage\":\"2026-09-04T05:53:37.689093+00:00\"}` with the SHAPE CONTROL on the same transport returning `{\"rows\":[{\"nodes\":27244}]}` -- so the 0 is the graph's answer and not a dead transport.",
        "DISCRIMINATION, the reason this is an IAM finding and not a code finding: the identical code read 34 of 34 on the laptop under the Andrew_Berman user (TO-CG-D-1 records TRIGGERS=188, 34 read / 0 unreadable) and 0 of 34 in the cloud under opal-globgrph-derive-runner-task. Same bytes -- the container digest is the same image built from HEAD 5644fee152 -- different principal, opposite result."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-1's cell CG-s-15 closes on 'the served projection at the post-derive vintage answers TRIGGERS > 0 for the declared Lambda targets (bd-pipeline's three; inf-pipeline's two as additional evidence)', and D1-AC5 expects a non-zero triggers count, on the premise that a HEAD carrying the C-3 deriver fix is the only thing standing between the cloud derive and a correct TRIGGERS edge set.",
    "world_is": "The image rebuild was necessary and is not sufficient. The C-3 fix's contribution is real and is exactly what it was cut to do -- it converted an unfalsifiable silent zero into a named, counted, per-bucket read failure -- but the failure it names is an IAM grant the estate has never declared. D1-AC5 cannot pass on any image until s3:GetBucketNotification reaches the derive task role. The pre-fix world would have shown TRIGGERS=0 with no explanation and this order would have had to guess; the post-fix world shows read=0/unreadable=34 with all 34 names, which is why this row can be written at all.",
    "notes": "NOT REMEDIATED, and deliberately so: the grant belongs in infra/aws/terraform/globgrph/iam.tf (aws_iam_role_policy on opal-globgrph-derive-runner-task), which is NOT in this task order's PATHS block -- and the apply route is closed to this seat anyway by W1-S1. Disarm = add s3:GetBucketNotification (account-wide read, alongside the existing Sid AccountWideReadOnly grants) and re-run one derive; the denominator line is now the acceptance instrument and should read read=34 / unreadable=0. Owner 0.7.0_AE_CloudOps as the module's IAM lane. This row is the ANSWER to S20 and the reason S28's disarm cannot complete on an image rebuild alone -- whoever adjudicates S20 should read this row before closing it, because closing S20 on the rebuild would close it on the wrong cause. NOTE the second-order lesson for the estate: an account-wide 'read-only describe' grant that enumerates its verbs will always lag the code that adds a new one, and the lag is invisible until something counts."
  }
]
```

## NFRA_CLDGRPH-W1-S8 -- one of the seven shared-image consumers has NO trigger at all, so "picks it up on its next scheduled fire" is unanswerable for it

```json
[
  {
    "id": "NFRA_CLDGRPH-W1-S8",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~1",
    "surfaced_at": "2026-09-04T09:02Z",
    "one_line": "TO-CG-D-1 instructs recording each of the four NFRA_GLOBGRPH families' next fire time. Three resolve -- comp-learns 04:00Z and fedobs 04:30Z (EventBridge Rules), cse 03:30Z (EventBridge SCHEDULER, a different service that a Rules-only census misses). The fourth, globgrph-resource-summaries-producer, has NO trigger on either service: no rule, no schedule, and the ONLY reference to its task definition anywhere in infra/aws/terraform is a terraform `output`. Its next fire time is not late or misconfigured -- it does not exist, so this family can never pick up a rebuilt image on its own.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "APPLIED plane, EventBridge RULES: `events list-rules` filtered to globgrph gives a DENOMINATOR of 4 rules -- opal-globgrph-cloudtrail-mgmt (no schedule, no ECS target), opal-globgrph-comp-learns-producer-nightly cron(0 4 * * ? *) -> globgrph-comp-learns-producer:1, opal-globgrph-derive-runner-nightly cron(0 2 * * ? *) -> globgrph-derive-runner:6, opal-globgrph-fedobs-producer-nightly cron(30 4 * * ? *) -> globgrph-fedobs-producer:1. No rule targets globgrph-cse-producer or globgrph-resource-summaries-producer.",
        "APPLIED plane, EventBridge SCHEDULER (the second carrier -- a Rules-only sweep reports a FALSE absence here): `scheduler list-schedules` -> the only globgrph entry is globgrph-cse-producer-nightly, `scheduler get-schedule` -> cron(30 3 * * ? *), ENABLED, target arn:aws:ecs:...:cluster/opal-globgrph. So cse IS scheduled, on a service the first census could not see; resource-summaries is on NEITHER.",
        "DECLARED plane @5644fee152: comp-find 'aws_ecs_task_definition.resource_summaries_producer' over infra/aws/terraform returns exactly ONE hit, resource_summaries_producer.tf:188 `value = aws_ecs_task_definition.resource_summaries_producer.arn` -- an output, not a target. comp-read of resource_summaries_producer.tf enumerating 'schedule_expression|aws_scheduler|aws_cloudwatch_event_rule|resource \"' returns 5 resources: a log group, two IAM roles/policies pairs and the task definition. No trigger resource exists in the file.",
        "EXERCISED plane, WEAK BY CONSTRUCTION and stated as such: `ecs list-tasks --family globgrph-resource-summaries-producer --desired-status STOPPED` returned empty. ECS retains stopped tasks for roughly an hour, so this is 'no run in the retention window', NOT 'never ran' -- it corroborates the declared-plane finding and cannot carry it alone."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-1 'MEASURED BY THE ISSUER': the four NFRA_GLOBGRPH families 'stay on `:latest` and pick the new image up on their next scheduled fire; you NAME them in the ledger and record DESIRED with each one's next fire time'.",
    "world_is": "Three of the four have a next fire time and one does not. The premise that a `:latest` consumer necessarily picks a rebuild up 'on its next scheduled fire' holds only for consumers that HAVE a scheduled fire; globgrph-resource-summaries-producer is a fully declared task family -- image, IAM, log group, S3 grants -- wired to nothing. It is a consumer of the shared image in the blast-radius sense (it would run the new bytes if anything ever started it) while being invisible to any 'when does this land' question.",
    "notes": "Recorded in the ledger as 'no trigger declared -- next fire time NONE' rather than left blank, because a blank reads as unmeasured. Not remediated: resource_summaries_producer.tf is outside this order's PATHS block and giving an untriggered family a schedule is a scope decision, not a fix. Disarm = either declare its trigger or retire the family; a third possibility the owner should rule on is that it is deliberately ad-hoc-only, in which case the blast-radius list should say so. NOTE the instrument lesson this row cost: EventBridge Rules and EventBridge Scheduler are two different services with two different list APIs, and a census of one returns a confident, wrong zero for schedules living in the other -- cse would have been reported unscheduled on the first sweep."
  }
]
```

## NFRA_CLDGRPH-S34 -- the drain deletes the NEVER-2 sentinel it never merged: two of round 4's three worker deploys went RED-invisible

```json
[
  {
    "id": "NFRA_CLDGRPH-S34",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~A",
    "surfaced_at": "2026-09-04T12:55Z",
    "one_line": "The v3 drain DESTROYS the NEVER-2 sentinel of a worker's deploy. `deploy_ledger.py open` writes org/critical_paths/.open_deploys/<slug>.json as a side-effect file that no commit pathspec necessarily names; the worker commits the change_management/*.md RENDERING (the visible artifact) and the sentinel stays untracked; the COO's drain then runs `git worktree remove` and deletes the only input the gate reads. Measured over round 4's three worker deploys: 2 of 3 sentinels were lost this way (cgs15, cgd2 -- alive today only because the issuer hand-captured the files before removing the worktrees), 1 survived (cgs16, whose worker happened to name .open_deploys/ in its commit pathspec). All three orders GRANT the directory and the lane is ANY, so this is not a refusal -- it is a pathspec omission with a destructive drain standing behind it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RECORD plane, the two DRAINED worker tips: `git ls-tree --name-only 8b8f2caae2 org/critical_paths/.open_deploys/` and the same at d4ab452051 each return a DENOMINATOR of 5 -- .unindexed_red_state.json, advi-insure-gold-chain-membership.json, advi-insure-iam-insurance-silver-read.json, d12-sms-origination-identity-activation.json, freshguard-leg4-writer-wiring-finish.json. Neither carries cldgrph-cgs15-shared-image-digest-pins.json nor cldgrph-cgd2-gateway-graph-path.json. The same read at HEAD 26da5ec0fa returns the same 5 -- so the two drain merges landed the ledger ENTRIES and not the sentinels, and both tips are ancestors of HEAD (`merge-base --is-ancestor`, 4 of 4 hashes tested).",
        "POSITIVE CONTROL on the same instrument, this round, live: `git ls-tree --name-only wk-NFRA_CLDGRPH-1 org/critical_paths/.open_deploys/` at c64f53339f returns 6 -- the same 5 plus cldgrph-cgs16-derive-role-bucket-notification.json, committed by 0.9.0_WK_NFRA_CLDGRPH~1 in its TO-CG-D-12 leg-L1 commit. A worker CAN and DOES commit a sentinel; the loss is per-commit, not structural to the branch. Variance within ONE round is the tell that this is chance, not design.",
        "DECLARED plane: the <paths> block of TO-CG-D-1, of TO-CG-D-2 and of TO-CG-D-12 each names BOTH org/critical_paths/change_management/ and org/critical_paths/.open_deploys/ at HEAD; and `.owned-paths.yaml` READ WITH `git show HEAD:` (not by path -- the worktree carries other seats' uncommitted edits) maps \"org/critical_paths/**\" to lane ANY at :1327. Neither the RULING-1 grant nor the lane refused the sentinel. Nothing blocked the write; nothing required it either.",
        "CONSEQUENCE, measured with the tool's OWN instrument in the main tree, read-only `python .tools/deploy_ledger.py check` (no --red, so nothing was written), rc=1: `SCAN DENOMINATOR: 4 of 4 sentinel(s) scanned` -- and two Layer-2 lines, `BYPASS: UNINDEXED OPEN LEDGER org\\critical_paths\\change_management\\20260904T0756Z_cldgrph-cgs15-shared-image-digest-pins_deploy_completion.md age=3.2h -- status='OPEN' (not a terminal/closed state)` and the identical shape for 20260904T0803Z_cldgrph-cgd2-gateway-graph-path. Round 4's two open deploys sit in exactly the false-clean class that deploy_ledger.py:902 `_unindexed_open_ledgers` was built to name.",
        "DISCRIMINATION -- why a single-plane read cannot see this: the entry and the sentinel are two carriers of one state and only ONE is the gate's input. deploy_ledger.py:726 says it in its own words: \"The change_management/*.md is a RENDERING of the .open_deploys sentinel; the sentinel is the gate's only input, and `close` unlinks it.\" A reader of change_management/ sees two OPEN CLDGRPH deploys and calls the record complete; the sentinel-only `check --red` scan sees neither and calls the board clean. Both reads are internally consistent and both are wrong about the world, which is why this went a full drain cycle without firing.",
        "LIVE-OWNERSHIP CONTROL, run only because the remediation looked obvious: at 12:5xZ the wk-NFRA_CLDGRPH-2 worktree no longer holds cldgrph-cgd2-gateway-graph-path.json at all (an `ls` of its .open_deploys returns the 4 tracked sentinels only) while `git status` there shows the change_management entry MODIFIED-uncommitted and the branch carries 03b1cb0f7d + 480ffaf58e -- the signature of `deploy_ledger.py close`, which unlinks the sentinel and rewrites the entry. The wk-NFRA_CLDGRPH-1 copy is still present and sha256-IDENTICAL to the issuer's capture. So one of the two deploys is being closed by its owner right now: the sentinel plane is LIVE, not abandoned."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NEVER-2 (CLAUDE.md section 5): a confirmed deploy is never left half-landed, with a \"ledger entry in org/critical_paths/change_management/ opened at start, closed at completion\" -- and deploy_ledger.py's sentinel is the gate's input for that obligation. The spine's L7 drain ends a worker's life with `git worktree remove`, on the premise that everything the worker owed the record is in its commits.",
    "world_is": "The two halves of the same obligation are carried on planes with different durability. The entry is committed and survives the drain; the sentinel is an UNTRACKED working file inside the directory the drain deletes. Nothing in the drain reads a worktree for untracked files before removing it, and nothing in deploy_ledger.py stages what it writes. So every worker deploy is one forgotten pathspec away from a RED state that vanishes at the moment its owner does -- and the half that survives is the half that READS as a complete record, so the loss presents as cleanliness.",
    "notes": "NOT REMEDIATED -- and the attempt is recorded here because its WITHDRAWAL is this row's sharpest edge. The two lost sentinels were re-homed onto the tracked path from the issuer's captured copies and the effect was MEASURED: `python .tools/deploy_ledger.py check` went from `SCAN DENOMINATOR: 4 of 4 sentinel(s) scanned` with two BYPASS lines to `6 of 6` with both deploys reported OPEN and their stranded legs named (cgd2 ['L4','L5','L6'], cgs15 ['L4','L6','L7'], both in-window). The copies were then DELETED and the tree left exactly as found, on the fact the sixth evidence item records: wk-NFRA_CLDGRPH-2's LIVE worker had already unlinked its cgd2 sentinel via `close`, so the re-homed file was a stale OPEN carrier for a deploy its owner was closing -- inserting precisely the second-carrier drift this row is filed against. THE SENTINELS ARE NOT ORPHANED STATE TO BE RESCUED: they are live state owned by running workers, and the place to reconcile them is each order's DRAIN, not the main tree mid-flight. RECOVERY HELD: both captured sentinels are kept off-tree by the issuer, so a worker dying before its close commits is recoverable rather than silent -- that holding is a person's discipline, not a mechanism, and is stated as weak on purpose. DISARM, and it is not this seat's: make the sentinel durable BY CONSTRUCTION -- `deploy_ledger.py open` printing the sentinel path as a REQUIRED commit pathspec, or the L6 cut naming it in the deliverable's commit step. Owner 1.0.0_SA_CTO as the tool's lane. This row deliberately does NOT fold in the eight older BYPASS entries the same scan names (seven D12, one advi, ages 63-82h) -- different origin, different owners, and folding them in would bury the one finding that is about the spine."
  }
]
```

## NFRA_CLDGRPH-W1-S9 -- the statement the order sends this seat to edit is in a file the order does not grant it, so the grant landed at a different terraform address and the role's account-wide S3 reads now have TWO carriers

```json
[
  {
    "id": "NFRA_CLDGRPH-W1-S9",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~1",
    "surfaced_at": "2026-09-04T12:50Z",
    "one_line": "TO-CG-D-12 names `infra/aws/terraform/globgrph/iam.tf` as the file carrying the derive task role's `Sid AccountWideReadOnly` statement and grants exactly that file. The statement is not there: it is `aws_iam_role_policy.derive_runner_describe` in `infra/aws/terraform/globgrph/item2a.tf:129`, and item2a.tf appears in the order's SURFACES as READ ONLY and NOT in its <paths> block. Editing it would have been an out-of-grant write, which is a row and never an override -- so the one granted action landed as its own single-statement inline policy `DeriveRunnerBucketNotificationRead` in iam.tf: same role, same action, same Resource, same blast radius, a DIFFERENT terraform address. The plan therefore read `1 to add, 0 to change, 0 to destroy` where the order expected `0 to add, 1 to change, 0 to destroy`, and the derive role's account-wide S3 read grant now has TWO carriers in one module.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DESIRED plane, `infra/aws/terraform/globgrph/iam.tf` read whole at `c7b6a0d200` (235 lines, the pre-edit vintage): it declares THREE principals -- `aws_iam_role.nessie_task` (:30), `aws_iam_role.nessie_execution` (:99), `aws_iam_role.globgrph_incremental_updater` (:113) -- and five inline policies. It contains no `derive_runner_task`, no `AccountWideReadOnly`, and no reference to the derive runner at all. The order's premise 'its inline policies live in iam.tf' is false of that file.",
        "DESIRED plane, where the statement actually is: `comp-find 'derive-runner-task|derive_runner_task|AccountWideReadOnly' infra/` -- DENOMINATOR 40 hits across 6289 files scanned [corpus=all] -- resolves it to `infra/aws/terraform/globgrph/item2a.tf:56` (`name = \"opal-globgrph-derive-runner-task\"`), `:123` (`role = aws_iam_role.derive_runner_task.id`, resource `aws_iam_role_policy.derive_runner_describe`, policy name `DeriveRunnerAccountDescribe`) and `:129` (`Sid = \"AccountWideReadOnly\"`). Read directly at item2a.tf:120-172: 66 actions, `Resource = \"*\"`, and NO Condition block -- which is why the order's simulate criterion is gradeable at all (a conditioned grant would have read implicitDeny/MissingContext, the false-deny trap).",
        "GRANT plane, the order's own text at HEAD (`org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-D-12.derive-role-bucket-notification-grant.md` @`c7b6a0d200`): the <paths> block names five paths -- `infra/aws/terraform/globgrph/iam.tf`, `org/critical_paths/change_management/`, `org/critical_paths/.open_deploys/`, the channel's INVESTIGATION_v1.md, and the order file itself. `item2a.tf` is named only under SURFACES, explicitly as `(READ: the derive task's run shape)`. The lane gate admits a worker to exactly the paths its non-terminal order names, so the edit the order describes cannot be committed by this seat.",
        "APPLIED plane, what landed instead: `terraform plan -target=aws_iam_role_policy.derive_runner_bucket_notification` printed exactly one address (`aws_iam_role_policy.derive_runner_bucket_notification will be created`) and `Plan: 1 to add, 0 to change, 0 to destroy`; `safe-apply` on that saved plan printed `Creation complete after 0s [id=opal-globgrph-derive-runner-task:DeriveRunnerBucketNotificationRead]` and `Apply complete! Resources: 1 added, 0 changed, 0 destroyed`. The role's inline-policy denominator moves from 4 (DeriveRunnerAccountDescribe, DeriveRunnerCWLogs, DeriveRunnerS3, DeriveRunnerSNS -- the census in row W1-S7) to 5.",
        "DISCRIMINATION -- that the ADDRESS differs and the EFFECT does not: on the live principal, `simulate-principal-policy` for `s3:GetBucketNotification` on `arn:aws:s3:::opal-data-bd` answered `implicitDeny 0` BEFORE the apply (12:2xZ, this seat's own pre-state baseline) and `allowed 1` after, while the write twin `s3:PutBucketNotification` answers `implicitDeny` on the same principal and the same resource after the apply. Had the action landed inside AccountWideReadOnly the same two calls would return the same two answers -- IAM evaluates the union of a role's inline policies, so the placement is invisible to every consumer and visible only to a human reading the source."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-12, MEASURED BY THE ISSUER: 'The role: opal-globgrph-derive-runner-task ...; its inline policies live in infra/aws/terraform/globgrph/iam.tf; row W1-S7 names the Sid AccountWideReadOnly statement to extend. Add s3:GetBucketNotification to THAT statement (resource *, the sibling read actions' scope) -- ONE action added, nothing else.' and 'The apply set is ONE address: aws_iam_role_policy.<the resource that carries that document> -- name it from the file; safe-apply -target on exactly it; expect 0 to add, 1 to change, 0 to destroy.' The cell CG-s-16 repeats it: '(infra/aws/terraform/globgrph/iam.tf, one action added to the role's account-wide read statement)'.",
    "world_is": "The role, its four inline policies and the AccountWideReadOnly statement are all in item2a.tf, not iam.tf; iam.tf carries the nessie and incremental-updater roles only. The order's <paths> grant is therefore one file short of the act it describes, and the two halves of the order disagree with each other: SURFACES marks item2a.tf READ while MEASURED sends the edit into a statement that only item2a.tf holds. The order's substance -- the grant applied, read live, and exercised by a real derive -- is fully executable inside the grant it does give; only the order's stated shape (`0 add / 1 change`, one existing statement extended) is not.",
    "notes": "WHAT THIS SEAT DID AND WHY: took the in-grant route rather than the out-of-grant one. iam.tf is in <paths>, item2a.tf is not, and 'a path you need that the block lacks is a BLOCKING row on that criterion, never an override' -- so the choice was between (a) filing a blocking row and leaving the grant unapplied for a file-path error, with D-1's pins and CG-x-2's night both sequenced behind it, and (b) delivering the identical IAM effect at an address inside the grant. Chose (b), one action, one statement, one role, Resource `*`, no managed policy, no other principal, no bucket policy -- every BOUND of the order honoured except the address. The order's own acceptance is untouched by the choice: D12-AC1..AC6 read the LIVE world (simulate, the derive's denominator line, the served graph, the ledger) and name no terraform address. DISARM (owner 0.7.0_AE_CloudOps, the module's IAM lane, the same owner row W1-S7 names): move `s3:GetBucketNotification` into item2a.tf's AccountWideReadOnly action list and delete `aws_iam_role_policy.derive_runner_bucket_notification` from iam.tf in ONE apply -- IAM sees no gap because the union is unchanged at every instant. THE HAZARD IF IT IS NOT DISARMED is not the grant, it is the READING of it: W1-S7's own closing lesson was that 'an account-wide read-only describe grant that enumerates its verbs will always lag the code that adds a new one, and the lag is invisible until something counts' -- a second carrier makes that lag harder to see, because the next seat extending the enumerated list in item2a.tf has no reason to open iam.tf, and a least-privilege audit that reads the AccountWideReadOnly statement alone will now UNDER-report this role's grant by exactly one action. The mitigation shipped with the act: a 20-line comment above the new resource names item2a.tf, the statement, this row id and the disarm, so the pointer exists in the file a reader lands in. SECOND-ORDER, for the issuer: this is the third order in this project whose named address set was measured wrong at execution (W1-S2 -- four addresses named, eight measured; W1-S3 -- seven state outputs the config no longer declares; this row -- the file that carries the statement). The common factor is that the cut's address facts are derived from a row's PROSE rather than from the file at HEAD; W1-S7's own notes line says 'the grant belongs in infra/aws/terraform/globgrph/iam.tf', which is where this order's path came from, and that sentence was the predecessor's inference about where it OUGHT to live, never a measurement of where the statement IS."
  }
]
```

## NFRA_CLDGRPH-W1-S10 -- the served-graph instrument returns a FALSE ZERO for every WHERE-filtered cypher: the shell re-quoting in the SSM command made the server evaluate `e.edge_type='"TRIGGERS"'`, valid and unmatchable

```json
[
  {
    "id": "NFRA_CLDGRPH-W1-S10",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~1",
    "surfaced_at": "2026-09-04T13:25Z",
    "one_line": "S20's silent zero had a SECOND cause, independent of the IAM gap and still live after it was fixed. `triggers_query.sh` built its SSM command with `json.dumps(q).replace(\"'\", \"'\\\"'\\\"'\")`; the `'\\''` idiom is correct only INSIDE a single-quoted shell word and json.dumps emits a DOUBLE-quoted one, so the host shell handed `curl --data` the text `... WHERE e.edge_type='\"TRIGGERS\"' ...` -- the string literal became the ten-character value `\"TRIGGERS\"` WITH its double quotes. That is a SYNTACTICALLY VALID query which cannot match any row: the server answered `{\"rows\":[{\"triggers\":0}]}`, no error, correct vintage, beside a shape control that passed because `MATCH (n) RETURN count(n)` contains no string literal. EVERY WHERE-filtered read this project has taken through that transport is a false zero, and TO-CG-D-1's D1-AC5 reading `triggers:0` at 08:49Z was measuring the instrument, not the graph. Carried unmangled at the SAME vintage the same three queries answer triggers=171, notifies=41 and the three bd-pipeline targets.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SERVED plane, the contradiction that opened it: at vintage 2026-09-04T12:55:59.236365+00:00 the unfiltered `MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) RETURN count(e)` answered 58589 and `RETURN e.edge_type AS t LIMIT 5` answered NOTIFIES, HAS_POLICY, HAS_POLICY, HAS_POLICY, HAS_POLICY -- while `WHERE e.edge_type='NOTIFIES' RETURN count(e)` answered 0 through the same transport in the same call. A sampled value that its own equality predicate cannot find is not a graph fact.",
        "TRANSPORT plane, the cause reproduced on a SECOND instrument (the local Git Bash 3.6.7 shell, not the gateway's, parsing the byte-identical command string the builder emits): the word that reaches `curl --data` is `MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE e.edge_type='\"TRIGGERS\"' RETURN count(e) AS triggers`. The mangle is deterministic, offline, and independent of AWS, kuzu and the serving process.",
        "SERVED plane, the discriminator: the same three queries carried as BASE64 (alphanumeric + / + =, nothing a shell can reinterpret), decoded into a file on the gateway and posted with `--data-binary @file`, at the SAME vintage, same instance, same endpoint, same call shape: `{\"rows\":[{\"triggers\":171}]}`, `{\"rows\":[{\"notifies\":41}]}`, and the three bd targets bd-allocation-processor / bd-gold-trigger / bd-silver-merge, each echoed as the server received it.",
        "CROSS-PLANE CORROBORATION, a different producer entirely: the derive's own log line for the same run (CloudWatch /ecs/globgrph/derive-runner, stream derive-runner/derive-runner/aeb8dec6982a43bd80fe49a9ed34b871) reads `edges total=3940 ... NOTIFIES=41 ... TRIGGERS=182 ...`. The served NOTIFIES=41 equals the derive's NOTIFIES=41 exactly; the served TRIGGERS=171 is 182 minus edges the projection dropped (`edges_skipped_missing_endpoint: 386` in the build manifest). The zero matched nothing on either plane.",
        "LINEAGE, that this is the right vintage to be reading: the build manifest at projection/2026-09-04T12:55:59.236365+00:00/_build_manifest.json carries nodes_snapshot_id 4492677536813842224, edges_snapshot_id 1732740251598783067 and nessie_commit_hash 4bb3844b5243976ac128dd97ffda29ca1c6157002ed1a32ba49367661bd560eb -- byte-identical to this order's derive log line `OK: MARKER_STAMPED writer=derive_runner hash=4bb3844b... nodes_snap=4492677536813842224 edges_snap=1732740251598783067`. The served answer is this derive's graph and no other."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-12 D12-AC4 names `bash .../triggers_query.sh` with expect `\"triggers\":\\s*[1-9][0-9]*` and calls it, with D12-AC2 and D12-AC3, one of 'the controls that must be able to FAIL'. TO-CG-D-1's D1-AC5 named the same script. Both orders treat that script's zero as the GRAPH's answer, on the strength of a shape control the order itself describes as the discrimination the silent-zero class needs.",
    "world_is": "The shape control could not see this failure: it shares the transport but NOT the hazard, because it carries no string literal. A control has to exercise the same failure mode as the measurement, and this one exercised only reachability. So the instrument answered 0 for the graph in exactly the world where the graph answers 171 -- and it would have gone on answering 0 after the IAM grant landed, converting a REPAIRED estate into evidence that the repair failed.",
    "notes": "REPAIRED IN THIS ORDER, disclosed rather than quietly fixed: both `triggers_query.sh` (inherited, in this seat's own deliverables folder, its write surface) and the new `bd_targets_query.sh` now carry the cypher as base64 and post it from a file with `--data-binary`, and both ECHO each query as the server received it beside the answer, so the evaluated bytes are always in the output and this class cannot hide again. The QUERIES are unchanged. D12-AC4 therefore PASSES on a REPAIRED instrument and the record says so out loud: pre-repair output at the same vintage was `{\"rows\":[{\"triggers\":0}]}`, post-repair `{\"rows\":[{\"triggers\":171}]}`, both in the deliverable. WHAT THE ADJUDICATOR SHOULD NOT CONCLUDE: that the IAM grant was unnecessary. Two independent causes stacked, and the derive-side one is measured on its own plane -- `buckets read=0 / unreadable=34` before the grant and `buckets read=34 / unreadable=0` after it, with TRIGGERS going 0 -> 182 in the derive's OWN edge summary, which never travelled through this transport. Fixing the instrument alone would still have served 0 TRIGGERS, because the edges did not exist to be counted. STILL ARMED, and this is why the row is not closed by the repair: the defect is a SHAPE, not a file. `.tools/comp-kuzu`, `infra/aws/globgrph/c2c3_liveness_acceptance.py` (whose own docstring warns about 're-quoting a cypher literal that itself contains double quotes'), the gateway integration `graph_cypher`, and any future seat that sends a cypher through `ssm send-command` inherit the same trap. The general form: A CONTROL THAT SHARES THE TRANSPORT BUT NOT THE HAZARD CERTIFIES THE WRONG THING, and a mangled query that stays syntactically valid returns a NUMBER, never an error. Owner 2.0.0_SA_COO~A to route the sweep -- this seat repaired only the two instruments its own order names, and widening to the others is not this order's grant."
  }
]
```

## W2-S8 -- G6's SERVED audit record cannot be produced by any seat holding only the capability bearer: the `/graph/*` HTTP path deliberately does not write an audit record, and the MCP surface that does is behind ALB authenticate-oidc

```json
[
  {
    "id": "NFRA_CLDGRPH-W2-S8",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~2",
    "surfaced_at": "2026-09-04T13:15Z",
    "one_line": "TO-CG-D-2 step 8 asks G6 to be grounded on 'the audit record for one ok and one denied call read from the box's audit.jsonl'. After a SUCCESSFUL deploy with globgrph ENABLED, the box's audit.jsonl holds 41,489 records and ZERO containing 'graph_' -- because the only run-path that calls audit.log_call is run_integration_tool on the MCP surface, and this seat cannot reach /mcp (ALB authenticate-oidc, browser Entra login). The two /graph/* HTTP routes are audit-silent BY CONSTRUCTION, exactly as /ms/* and /otp/* are.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "LIVE, SSM AWS-RunShellScript on i-07dccb1615503ac99 2026-09-04 ~13:0xZ, AFTER the deploy that enabled globgrph: 'sudo wc -l < /opt/opal-gateway/audit.jsonl' = 41489; 'sudo grep -c graph_ /opt/opal-gateway/audit.jsonl' = 0. The file is live (11,595,518 bytes, mtime Sep 4 13:00) and its last record's keys are ['args','detail','outcome','tier','tool','ts','user'] -- a POSITIVE control that the read reached a real, currently-written audit file, so the 0 is an ABSENCE and not a broken read.",
        "SOURCE, infra/aws/ec2/opal-gateway/app/server.py @03b1cb0f7d: the /graph/* handlers are `_graph_guard` (:596-604) + `graph_cypher` (:607-636) + `graph_health` (:638-647), mounted in the plain route table (:682-683) OUTSIDE the /mcp Mount; comp-read --enumerate 'graph' over that file returns 31 hits / 0 of them an audit.log_call. The same is true of the /ms/* (:526-582) and /otp/* (:462-517) precedents this path was built from.",
        "SOURCE, app/integrations/base.py:93-148 @03b1cb0f7d (byte-identical to the cut, sha256 718246435530d59e853ed7dca99791d59e1b629e2df516b6a98c3146902cf616): run_integration_tool IS wired to audit.log_call on the denied, error and ok branches -- so G6's mechanism is present and source-grounded; what is missing is a CALLER, not the wiring.",
        "LIVE, the box's startup integration report (journalctl, uvicorn[552785], Sep 04 12:52:31): globgrph -> {'tools': ['graph_cypher','graph_status'], ...} -- the two tools ARE registered on the live MCP surface, so the first authenticated MCP caller will mint exactly the records G6 wants."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-2 step 8: 'G6 the audit record for one ok and one denied call read from the box's audit.jsonl' -- i.e. that this order's own seat can produce a served audit record for a graph_ call once the integration is enabled and deployed.",
    "world_is": "Enablement + deploy are NECESSARY but not SUFFICIENT for a graph_ audit record: the record is minted only by an MCP tool invocation through run_integration_tool, and the MCP surface requires an ALB authenticate-oidc session (a human Entra login) that a worker subagent holding AWS credentials plus the static capability bearer cannot complete. The HTTP capability path this order also built is audit-silent by design and by precedent. G6 is therefore recorded PARTIAL: mechanism source-grounded, tools live-registered, served record awaiting the first authenticated MCP caller.",
    "notes": "Not blocking: G6 lives inside D2-AC10, which is judgment=true and carries NO verdict from this seat. Two candidate closures for whoever adjudicates -- (a) an authenticated MCP call by a seat that HAS an OIDC session (Andrew's client), which needs no code; (b) if the estate wants the HTTP capability path itself audited, that is a NEW requirement on server.py's /graph/* handlers and, by the same reading, on the /ms/* and /otp/* precedents -- a change to three paths, not one, and outside this order. Surfaced, not adjudicated."
  }
]
```

## W2-S9 -- safe-ec2-deploy.sh resolves its HALT-gate identity against the MAIN worktree, so a worker in a `git worktree` must write its session serial OUTSIDE the tree its task order grants

```json
[
  {
    "id": "NFRA_CLDGRPH-W2-S9",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~2",
    "surfaced_at": "2026-09-04T13:15Z",
    "one_line": "The halt gate resolves its principal from ${HALT_GATE_REPO_ROOT}/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial, and safe-ec2-deploy.sh sets HALT_GATE_REPO_ROOT to the MAIN worktree by design. A worker executing in wk-NFRA_CLDGRPH-2 therefore had to create that file in C:/Users/AndrewBerman/Desktop/ajb_workspace -- a path no <paths> block names -- or the wrapper exits 3 IDENTITY UNRESOLVED and, past the gate, refuses to record an unattributed deploy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/halt-gate-check.sh:52-57 @d5ce612d16 -- halt_gate_resolve_serial reads `local sess_file=\"${repo_root}/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial\"` where repo_root=\"${HALT_GATE_REPO_ROOT}\" (:38).",
        "infra/aws/ec2/safe-ec2-deploy.sh @d5ce612d16, the MAIN_TREE block: 'Runtime state (agent inbox, session serial, .comp-graph markers) ALWAYS lives in the MAIN worktree, never in an ephemeral `git worktree add` build checkout' -> HALT_GATE_REPO_ROOT=\"$MAIN_TREE\" resolved via `git rev-parse --git-common-dir`. This is DELIBERATE (it fixes the stale-worktree-inbox hazard), not a bug.",
        "MEASURED both ways, this session (id 3e63c2d6-a07e-4ea6-9780-7be73730e12c): with the serial written ONLY in the worktree, `HALT_GATE_REPO_ROOT=<main tree> bash .tools/halt-gate-check.sh` printed the IDENTITY UNRESOLVED banner; after `printf '%s\\n' 0.9.0_WK_NFRA_CLDGRPH~2 > <main tree>/org/mcp/sessions/3e63c2d6-....serial` the SAME command printed 'HALT-GATE: worker 0.9.0_WK_NFRA_CLDGRPH~2 has no inbox; scanning its issuer 2.0.0_SA_COO~A' and returned 0. The predecessor in this slot recorded the un-fixed form as row W2-S1's second failure mode.",
        "RECORD IMPACT NIL, verified: .gitignore:423 ignores org/mcp/sessions/, and `git ls-files org/mcp/sessions/` returns EMPTY -- the file is untracked runtime state in both trees, so nothing entered any commit and no other seat's serial could be overwritten (the filename is keyed to THIS session's unique id).",
        "The wrapper then attributed correctly: EC2_MANIFEST.json recorded deployed_by=0.9.0_WK_NFRA_CLDGRPH~2 and the wrapper's own safe-commit landed 480ffaf58e under that author."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-2: 'Your write surface is exactly the PATHS block below plus <deliverables>. A path you need that the block lacks is a BLOCKING row on that criterion' -- and Rule 12 requires the deploy to go through safe-ec2-deploy.sh, whose PATHS entry is the deploy script, not the session store.",
    "world_is": "The wrapper's identity contract points at the MAIN tree ON PURPOSE, so the one file a worker must write to satisfy it can never be inside the worker's worktree, and therefore can never be inside any <paths> block a worktree-scoped order writes. Filed as OBSERVATION rather than BLOCKING because the write touches no tracked byte: the store is gitignored, the filename is session-unique, and the deploy attributed to the correct serial. But the general form -- 'the L7 worker face grants paths in a worktree; a required wrapper reads runtime state only from the main tree' -- is a gap between two live mechanisms, not this order's local difficulty.",
    "notes": "Cheapest durable fix for the issuer, if wanted: name the session-serial write in the STANDING LAW section of any worker face whose order runs safe-ec2-deploy.sh (it is runtime state, not a repo edit, so it needs a sentence rather than a <paths> entry). Alternative for the tool owner: have safe-ec2-deploy.sh accept an explicit AGENT_NAME for attribution AND let the halt gate fall back to $OPAL_AGENT_SERIAL for principal resolution -- but that second half weakens a gate that deliberately refuses to guess, so it is named here and NOT recommended. Surfaced, not adjudicated."
  }
]
```

## W2-S10 -- the opal-gateway terraform tree carries FOUR non-no-op addresses of pre-existing drift, two of them DELETES of live WAF IP sets; an unscoped apply in this module would destroy them

```json
[
  {
    "id": "NFRA_CLDGRPH-W2-S10",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~2",
    "surfaced_at": "2026-09-04T13:15Z",
    "one_line": "The C-1 control -- ONE unscoped `terraform plan` after this order's targeted apply -- shows this order CONVERGED (both its addresses no-op, 0 to add) and, in the same read, FOUR non-no-op addresses belonging to nobody in this project: `aws_instance.gw` [update], `aws_wafv2_web_acl.gw` [update], and `aws_wafv2_ip_set.opal_blocked_ips_regional_v4` + `_v6` [DELETE]. An unscoped apply by any seat in infra/aws/terraform/opal-gateway would destroy two live WAF IP sets.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.7.0_AE_CloudOps",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform v1.9.8 `plan -input=false -lock=false -out=.build/cgd2-unscoped-postapply.tfplan` in infra/aws/terraform/opal-gateway, run 2026-09-04 ~13:0xZ AFTER this order's apply; rc=0; headline 'Plan: 0 to add, 2 to change, 2 to destroy'.",
        "The plan JSON read by address list: resource_changes DENOMINATOR 66; non-no-op rows = 4 -- aws_instance.gw ['update'], aws_wafv2_ip_set.opal_blocked_ips_regional_v4 ['delete'], aws_wafv2_ip_set.opal_blocked_ips_regional_v6 ['delete'], aws_wafv2_web_acl.gw ['update'].",
        "THIS ORDER'S OWN ADDRESSES ARE NOT AMONG THEM: aws_iam_role_policy.gw_graph_read_secret_read and aws_lb_listener_rule.graph_capability both appear in the same 66 and both read ['no-op'] -- which is what makes the same read simultaneously this order's C-1 PASS and this row's finding.",
        "The 2 destroys are ip-set resources the module DECLARES but the plan says must be removed, i.e. a declared-vs-live divergence that pre-dates this order: this order applied only its two addresses (targeted plan '2 to add, 0 to change, 0 to destroy'; apply 'Resources: 2 added, 0 changed, 0 destroyed'), touched no WAF or instance file, and left the drift EXACTLY as found.",
        "SIBLING, already on the record: NFRA_CLDGRPH-W2-S2 found the SAME class of divergence on aws_lb.gw (live access_logs enabled, declared nowhere) and disarmed it for this order only, with a lifecycle ignore_changes guard the CTO ruled KEPT. That guard is scoped to access_logs and does nothing for these four."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-2 step 4 treats the unscoped plan purely as a CONTROL on this order ('asserted BY ADDRESS LIST to contain none of your addresses'), which presumes the rest of the plan is somebody's already-managed business.",
    "world_is": "The control passes and, on its own output, the module is NOT converged: four addresses drift, and two of them are deletions of live security infrastructure. Nothing in this order created, worsened or acted on any of the four; they are reported at the vintage this order measured them because a plan read is perishable and the next seat to run an unscoped apply in this tree is the one who eats it.",
    "notes": "ARMED because the trigger is a routine act (an unscoped `safe-apply` in this module) and the consequence is a delete, not a diff. disarm_owner set to the cloud-ops lane that owns infra/aws/terraform/opal-gateway; if 3.0.0_SA_CVO~A routes it elsewhere that disposition supersedes this assignment. NOT remediated here: the WAF/instance files are outside this order's <paths>, and a lifecycle guard on somebody else's resource would be exactly the widening this channel exists to prevent. Surfaced, not adjudicated."
  }
]
```

## NFRA_CLDGRPH-S36 -- safe-merge.sh aborts on the conflict that every concurrent drain produces, so its index guard and its row gate are absent exactly when they are needed

```json
[
  {
    "id": "NFRA_CLDGRPH-S36",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~A",
    "surfaced_at": "2026-09-04T15:10Z",
    "one_line": "safe-merge.sh's two protections are both LOST in exactly the case they were built for. It refuses and ABORTS when the merge conflicts (:82-85), so the drain must be finished with a raw `git merge` -- which has neither its index guard (:73-79, refusing a merge whose index carries another seat's staged work) nor its row gate on the merged index (:100-110). And the conflict is not the exception: the append-only channel file conflicts on EVERY concurrent drain, because both sides append at the same place and both restate the header. 3 of 3 of round 4's drains conflicted, so the abort path IS the drain path.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MECHANISM, read at HEAD with `git show HEAD:.tools/safe-merge.sh` (142 lines, not the worktree copy): :73-79 refuses BEFORE the merge when the index carries staged changes, \"possibly another seat's\"; :82-85 on a failed `git merge --no-commit --no-ff` prints \"REFUSED -- git could not produce a clean merged index (conflicts). Aborting.\" and runs `git merge --abort`; :100-110 grades the MERGED index with the row gate fed the staged set. The abort at :84 is what makes :73-79 and :100-110 unreachable for a conflicted drain -- the guard is not weak here, it is ABSENT.",
        "EXERCISED, this turn, not read from the source: `bash .tools/safe-merge.sh wk-NFRA_CLDGRPH-1 -m ...` printed exactly that refusal on the TO-CG-D-12 drain and aborted, leaving the tree as found and the drain unperformed. The drain was then completed by hand, as the two before it were.",
        "FREQUENCY -- the denominator that makes this a mechanism and not a mishap: 3 of 3 of round 4's drain merges conflicted on org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md (wk-2 at the first drain, wk-1 at the second, and both of this pair). The cause is structural, not incidental: an append-only file takes every side's rows at the same offset and every side restates the header line, so two concurrent workers ALWAYS collide there. Any project whose workers file rows has this property.",
        "MEASURED CONSEQUENCE, same day, on a commit of this seat's: `git diff --name-only b687429234^1 b687429234` returns a DENOMINATOR of 15 files, of which 14 are the CG-s-16 worker's and exactly ONE is foreign -- org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260904_142xZ_ALL_APPROVED_ENDPOINT_CONFIRMED_FWD1_FWD8.md, left STAGED in the shared index when that seat's safe-commit hit git's refusal of `--only` during a merge. `git log -- <that file>` names b687429234 as its ONLY commit, so the record carries it under this seat's authorship. Nothing refused: owned-paths-check's merge exemption deliberately skips per-file lane checks on a merge. The limb that WOULD have refused is safe-merge.sh:75, and it never ran.",
        "DISCRIMINATION -- why this is a missing guard and not a bad procedure: the SECOND drain 57b6750101, done by hand the same way twenty minutes later, returns 7 files and ZERO foreign. Same seat, same method, same shared tree; the only difference is that 1.0.0_SA_CTO had begun holding its commits by then. The outcome is decided entirely by whether another seat happens to be mid-commit, which is exactly what a guard exists to stop being a coin toss.",
        "SCOPE CONTROL, so this is not read as wider than it is: the row-gate limb was NOT lost in practice -- this seat ran `surprise-row-gate.py` against the merged index by hand before each of the three hand-merges and all three passed (2 new of 50, 3 new of 53, and the earlier union). That limb survived on discipline. The index guard did not, and it is the one with a measured failure behind it."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The /dispatch skill's Step 5: \"USE THE REFUSER, NOT THE RAW MERGE\", and safe-merge.sh exists so that \"remember to check\" becomes \"one command that checks -- that is smaller than a gate and larger than a paragraph, and the difference matters when you are tired\".",
    "world_is": "The command that checks refuses to run in the case it was built for. A drain that conflicts -- which on an append-only channel is every concurrent drain -- has to be finished by hand, and by hand means without the index guard, in a shared worktree where another seat's half-committed file is a normal condition. The protection is present exactly when it is not needed and absent exactly when it is.",
    "notes": "NOT REMEDIATED; the fix is a BUILD act in 1.0.0_SA_CTO's lane and this seat carries the ask rather than asserting it. DISARM, in the order the evidence puts it: (a) move nothing -- safe-merge.sh:73-79 already runs BEFORE the merge and is correctly placed; the failure is only that a conflicted drain never reaches it, so the cheapest real fix is a `--continue` limb -- on a conflict, keep the merge OPEN, hand the conflict back to the operator with the file named, and re-enter to run the index guard, the row gate and the commit once it is resolved; (b) failing that, a standalone pre-flight the operator can run before a hand merge would recover the index guard alone, which is the limb with the measured failure. INTERIM DISCIPLINE AT THIS SEAT, stated as weak because it is: `git diff --cached --name-only` must read empty before any hand-merge begins, and `git diff --name-only <merge>^1 <merge>` must be read after it with the foreign entries named. Both were done on the second and third drains of this round and neither was done on the first, which is how the sweep happened. RELATION TO THE NEIGHBOURING ROWS: NFRA_CLDGRPH-S34 is the same fact from the other side -- the drain DESTROYS a file it never merged -- and 1.0.0_SA_CTO's reserved S35 is the absorb half seen from the swept seat. All three come from one property: a drain commits an INDEX, and in a shared worktree the index is not only the drain's."
  }
]
```

## NFRA_CLDGRPH-W2-S11 -- the graph-call manifest advisory still routes every reader to "the canonical persisted Kuzu DB", which is the surface CG-s-6 just stopped reaching

```json
[
  {
    "id": "NFRA_CLDGRPH-W2-S11",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~2",
    "surfaced_at": "2026-09-04T16:34Z",
    "one_line": "The commit gate's MANIFEST-ADVISORY fires 5 ERROR-labelled findings on this order's battery with the remedy text \"Route graph queries through comp-kuzu so they hit the canonical persisted Kuzu DB (manifest cloud.* / xlayer.*)\". After TO-CG-D-3, comp-kuzu reaches the SERVED projection over HTTPS and opens no local database at all, so the advisory's stated reason is now false at HEAD; and the 5 hits are Cypher STRINGS inside stubbed test fixtures that are never sent to any graph, which is a class the detector cannot distinguish from a real ad-hoc query.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~A",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED this turn, the whole invocation and its verdict: `bash .tools/commit-gate.sh infra/aws/globgrph/kuzu_cli.py infra/aws/globgrph/projection_client.py .tools/tests/test_cg6_thin_client_battery.py` printed `MANIFEST-ADVISORY: 5 graph-access finding(s) (5 would block in blocking mode). Advisory -- not blocking.` and then `OK: pre-commit gate clean for 3 of 3 file(s)`, rc=0. Denominator: 5 of 5 findings are in .tools/tests/test_cg6_thin_client_battery.py (lines 127, 145, 164, 184, 237); 0 of 5 are in either shipped module.",
        "WHAT EACH HIT ACTUALLY IS: every one is a Cypher string handed to the CLI while projection_client.query is monkeypatched to a local stub (the battery's `_stub_query` context manager). No socket is opened by any arm; the line the advisory quotes at :237 is LITERAL_STATEMENT, a fixture that exists to prove the byte-for-byte transport property of row NFRA_CLDGRPH-W1-S10.",
        "WHY THE REMEDY TEXT IS NOW FALSE: at this branch's HEAD, kuzu_cli.py names no engine import, no local seam and no local path -- `python .tools/comp-read infra/aws/globgrph/kuzu_cli.py --enumerate 'import kuzu|_canonical|_provenance|CANONICAL_DB_PATH|ensure_fresh|kuzu_nessie_db'` returns `ENUMERATE: 0 hit(s) across 169 lines / 8 section(s) scanned`. comp-kuzu POSTs to https://mcp.opalinvest.dev/graph/cypher and prints the SERVICE's vintage. Routing a query \"through comp-kuzu so it hits the canonical persisted Kuzu DB\" is no longer a thing comp-kuzu can do.",
        "THE PROMOTION IS DECLARED, which is why this is filed rather than shrugged at: org/modules/graph/graph-call-manifest.yaml:6 @`dffbee781c` reads `Gate: comp-manifest-check (advisory -> blocking)`. The gate's own line already counts the finding twice -- `5 graph-access finding(s) (5 would block in blocking mode)` -- so the day that flip happens, this battery is refused by a rule whose stated justification no longer describes the tool it names.",
        "SCOPE, so this is not read wider than it is: the advisory is ADVISORY at this vintage and the gate exited 0, so nothing was blocked, bypassed or overridden by this order, and D3-AC7 passed on its own words (`pre-commit gate clean`). This row changes nothing and asserts nothing about the other 33 files that reference the local DB."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "org/modules/graph/graph-call-manifest.yaml's C_adhoc_reimplementation rule asserts that comp-kuzu is the route to \"the canonical persisted Kuzu DB\", i.e. that a graph answer comes from a LOCAL persisted database that a raw Cypher call would bypass.",
    "world_is": "For comp-kuzu that premise expired with this order: the canonical answer now comes from the served cloud projection and comp-kuzu holds no database. The rule's DIRECTION (ask the tool, not the raw engine) survives intact and is arguably stronger; only its stated reason and its remedy sentence are stale. Separately, its detector reads Cypher-shaped strings in a test file as graph access, so a battery that stubs the transport scores 5 of 5 findings while making 0 graph calls.",
    "notes": "NOT REMEDIATED and NOT MINE TO REMEDIATE: org/modules/graph/ is outside this order's <paths> and is explicitly named in the BOUNDS as CG-s-8's surface (\"the other consumers of the LOCAL DB are NOT yours\"). Filed at the vintage measured because the manifest edit is a natural part of CG-s-8's repoint -- the cell that retires the local copy is the cell that should re-word the rule that describes it, and this row is the input to that edit rather than a separate ask. INERT rather than ARMED on a deliberate reading: today the gate prints and exits 0, so no routine act fires anything; the trigger is the declared advisory->blocking promotion, which is an owned configuration act and not a routine one. disarm_owner names the issuing seat only so this reaches the cell that owns the surface; if 3.0.0_SA_CVO routes it elsewhere at L9 that disposition supersedes this assignment."
  }
]
```

## NFRA_CLDGRPH-S35 -- a failed `--only` during another seat's merge leaves the file STAGED, and the next drain commits it under the DRAINING seat's name; the swept seat's own rc says nothing landed

```json
[
  {
    "id": "NFRA_CLDGRPH-S35",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "1.0.0_SA_CTO",
    "surfaced_at": "2026-09-04T17:28Z",
    "one_line": "THE SWEPT SEAT CANNOT TELL THAT IT WAS SWEPT. When `git commit --only` is refused during another seat's merge, safe-commit has ALREADY staged the file, and it returns rc 128 -- a code from its NOTHING-LANDED family. The seat correctly believes nothing landed. The residue then sits in the SHARED index until the next drain merge commits it under the DRAINING seat's authorship, and nothing announces that. Measured: this seat's Andrew-direct ratification record was committed by 2.0.0_SA_COO~A in b687429234 and `git log` on that file names exactly one commit and one author, neither of them this seat's.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE SWEEP, measured this turn at HEAD: `git diff --name-only b687429234^1 b687429234` returns a DENOMINATOR of 15 files, of which 14 are the CG-s-16 worker's and exactly ONE is foreign -- org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260904_142xZ_ALL_APPROVED_ENDPOINT_CONFIRMED_FWD1_FWD8.md. `git log -1 --format='%an' b687429234` = 2.0.0_SA_COO~A, 2026-09-04 10:37:06 -0400.",
        "THE ATTRIBUTION CONSEQUENCE, which is this row's own contribution and not S34's or S36's: `git log -- <that file>` returns b687429234 as its ONLY commit. So the record of an ANDREW-DIRECT RATIFICATION carried by the CTO lane exists in git under the COO lane's authorship, with no second carrier anywhere that says otherwise. The true author is recoverable only by reading the drain's denominator and noticing that one of fifteen files does not belong to the branch being merged -- which nothing prompts anyone to do.",
        "THE PRODUCING MECHANISM, read at source: git refuses `commit --only <paths>` while a merge is in progress, and safe-commit.sh reaches its `git commit` only AFTER its gate stages the pathspec. So the refusal arrives with the file already in the shared index, and the failed run leaves it there. rc 128 belongs to the file's NOTHING-LANDED-TRY-AGAIN family, so the return code actively misinforms the seat that just ran it.",
        "THE PRODUCING HALF IS NOW CLOSED AT THIS SEAT, and this row says so rather than reporting a hazard already fixed: .tools/safe-commit.sh @59c3163a96 adds a MERGE_HEAD guard at :208-235, placed immediately after the AGENT extraction and BEFORE the mutex and the staging, so the refusal now happens with NOTHING staged. It resolves MERGE_HEAD with `git rev-parse --git-path` (a linked worktree keeps its own), names the merge and the staged count, writes a MERGE-REFUSED audit line and exits 3. No override. EXERCISED both ways: RED -> rc 3 with the index unchanged and the target file absent from `git diff --cached`; GREEN -> once the merge was aborted the identical command committed (3e4fce6f53).",
        "WHY THE ROW IS STILL ARMED RATHER THAN CLOSED BY THAT FIX -- the guard is one writer's, and the index is shared. It closes the path where THIS wrapper stages during a merge; it cannot close a raw `git add`, a tool that stages on its own, an older safe-commit on another device, or the residue of any run that dies between staging and committing. The ABSORBING half -- the drain committing an index it did not fill -- is not this row's and is filed as NFRA_CLDGRPH-S36 by 2.0.0_SA_COO~A: safe-merge.sh:73-79 would refuse a dirty index, but :82-85 aborts on a conflicted merge before reaching it, and an append-only channel conflicts on EVERY concurrent drain (3 of 3 in round 4).",
        "DISCRIMINATION -- why this is a carrier defect and not one seat's bad luck: the SECOND drain of the same round, 57b6750101, done by the same seat by the same hand-merge method twenty minutes later, returns 7 files and ZERO foreign. The only difference is that 1.0.0_SA_CTO had begun holding its commits by then. Whether a seat's work is attributed to itself is decided by whether another seat happens to be mid-commit."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md 14a and ADHC_OWNPTH: a commit's AUTHOR is the seat whose lane owns the path, enforced by safe-commit's lane refusal and the owned-paths hook, with GIT_COMMIT_AUTHOR_OVERRIDE as the audited and SINGULAR escape. The estate's whole attribution story is that authorship is checked at the commit.",
    "world_is": "Authorship is checked at the commit and then decided by the INDEX, which no single seat owns. A merge commits whatever the index holds; owned-paths-check exempts merges by design; so a foreign file crosses into the record under another seat's name with every lane control passing and no override written. The audited escape was not bypassed -- it was never reached, and an unaudited attribution change is exactly what that escape exists to prevent.",
    "notes": "FILED LATE AND ON PURPOSE, which is itself the row's smallest lesson: the id was reserved at 94187 and 2.0.0_SA_COO~A deliberately skipped it when appending S36 rather than closing the gap, because writing into this file while a drain merge held it is the very hazard the row is about. Allocation re-measured at HEAD in the turn of the write (`git show HEAD:` across all three planes), never carried forward from the earlier read. NOT REMEDIATED HERE: the attribution of b687429234's foreign file is not repaired by rewriting history on a shared branch -- this row IS the second carrier, and it is the correct remedy for a record already in the log. THE OPEN LIMB is S36's `--continue` ask, whose disarm_owner is this seat: on a conflicted drain, keep the merge OPEN and re-enter to run the index guard and the row gate, rather than aborting past both. RELATION: S34 is the same property seen a third way (a drain DESTROYS a file it never merged); S35 is the absorb half seen from the SWEPT seat; S36 is the missing guard. All three come from one fact -- a drain commits an INDEX, and in a shared worktree the index is not only the drain's."
  }
]
```

## NFRA_CLDGRPH-W1-S11 -- the halt gate reads a session-keyed FILE and never OPAL_AGENT_SERIAL, so a worker's first safe-apply is rc 3 IDENTITY UNRESOLVED on a path no order grants

```json
[
  {
    "id": "NFRA_CLDGRPH-W1-S11",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~1",
    "surfaced_at": "2026-09-04T16:15Z",
    "one_line": "The halt gate's spine-v3 WORKER limb (@68f22f74f5) admits this seat -- but only AFTER a step no task order names. safe-apply's FIRST invocation returned rc 3 'HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed)': the gate resolves WHICH principal it is running as ONLY from org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial, and it does NOT read OPAL_AGENT_SERIAL, which is the one identity carrier every worker face mandates on every Bash call. The refusal is the IDENTITY-UNRESOLVED banner, a DIFFERENT verdict from the 'SERIAL RESOLVES TO NO KNOWN AGENT' one row W1-S1 filed: W1-S1's fix landed the worker GRAMMAR, and this row is about the worker having no way to declare its serial that the gate reads. Writing that one file admitted the seat and the apply landed rc 0.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, first invocation: `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/globgrph apply -input=false -no-color -auto-approve -target=<eight addresses>` with OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~1 exported on the same Bash call -> rc 3, banner 'This gate could not determine WHICH AGENT it is running as from any session-keyed source. It will NOT guess.' plus the one-line FIX naming org/mcp/sessions/3e63c2d6-a07e-4ea6-9780-7be73730e12c.serial. Saved whole at deliverables/0.9.0_WK_NFRA_CLDGRPH~1/targeted_apply.txt at that moment (since overwritten by the successful run, which is why the banner is quoted here).",
        ".tools/halt-gate-check.sh:57 @f497b7d71b -- `local sess_file=\"${repo_root}/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial\"` is the resolver's session-keyed source; a comp-read --enumerate 'OPAL_AGENT_SERIAL' over the same file returns 0 hits across 1 file, so the env var every task-order face mandates is not consulted by this gate.",
        "DISCRIMINATOR (the fix is the only variable): `printf '%s\\n' \"0.9.0_WK_NFRA_CLDGRPH~1\" > org/mcp/sessions/3e63c2d6-a07e-4ea6-9780-7be73730e12c.serial` and NOTHING else changed -- same command, same eight targets, same shell -> rc 0, 'Apply complete! Resources: 3 added, 5 changed, 3 destroyed.' The spine-v3 worker limb then resolved the issuer 2.0.0_SA_COO~A from this order's own <issued_to>/<issued_by> at HEAD and scanned THAT inbox, exactly as @68f22f74f5 designed.",
        "GRANT PLANE: `git check-ignore -v org/mcp/sessions/<session>.serial` -> `.gitignore:423 org/mcp/sessions/`. The path the gate requires is GITIGNORED, so the write can never enter a commit and cannot reach the record through this branch; `git status --short org/mcp/` after the write is EMPTY. That is why this seat wrote it rather than filing a BLOCKING row and stopping -- but the file is NOT in this order's <paths>, and the order does not mention the step at all.",
        "NOT a duplicate of W1-S1: that row's banner is 'SERIAL RESOLVES TO NO KNOWN AGENT' from halt_gate_validate_serial (a serial that RESOLVED and then failed validation), and its disarm landed at @68f22f74f5. This row's banner is 'IDENTITY UNRESOLVED' from the resolver ABOVE the validator, which fires when no serial resolves at all. Both were hit by the same order, in that sequence, one pass apart."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-1 STANDING LAW: 'Every Bash call begins export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~1' and 'The halt gate admits you while this order is non-terminal at HEAD (@68f22f74f5); an rc=3 from safe-apply is a BLOCKING row quoting its whole output.' The face therefore asserts that exporting the serial is the seat's identity act and that the gate's admission follows from the order's non-terminal status alone.",
    "world_is": "Two identity carriers exist and only one is read. The task-order face and the commit lane read OPAL_AGENT_SERIAL; the halt gate reads a session-keyed FILE and refuses, correctly and loudly, when it is absent. A worker subagent is spawned with the env var set and the file unwritten, so EVERY spine-v3 worker whose order contains an apply meets rc 3 on its first attempt -- and the face instructs it to treat that rc 3 as BLOCKING and stop. A seat that obeys that sentence literally halts one file short of a working gate; a seat that writes the file is acting outside its <paths>. Neither reading is comfortable, which is what makes it a row rather than a preference.",
    "notes": "NOT AN ARGUMENT FOR AN OVERRIDE and no override was used: the gate's refusal is sound -- an agent that cannot name its principal must not deploy blind to its own STOPs, and this seat's STOPs are its ISSUER's by the same commit @68f22f74f5. The write was the gate's own prescribed FIX, printed by the gate, onto a GITIGNORED runtime path that cannot enter the record. DISARM, cheapest first: (a) have halt-gate-check.sh accept OPAL_AGENT_SERIAL as a session-keyed source when it is set and matches the worker grammar -- the same value the commit lane already trusts for authorship; or (b) have the worker spawn write the session serial file, which makes it a fabric act rather than a worker act; or (c) name the file in every worker face that contains an apply, which is the weakest of the three because it costs a line in every future order. Owner 1.0.0_SA_CTO as the .tools/ lane that owns the resolver limb; if 3.0.0_SA_CVO routes it elsewhere at L9 this assignment is superseded. BLAST RADIUS: every spine-v3 worker task order whose deliverable includes safe-apply or safe-ec2-deploy -- the same population W1-S1 named, one layer further in. Related but distinct: W2-S9 (safe-ec2-deploy resolving its identity against the MAIN worktree); here HALT_GATE_REPO_ROOT resolved to THIS worktree correctly and the missing thing was the file, not the root."
  }
]
```

## NFRA_CLDGRPH-W1-S12 -- the ledger's pinned-derive leg was closed on pass 1 against the UNPINNED run, and a closed leg cannot be reopened for pass 2

```json
[
  {
    "id": "NFRA_CLDGRPH-W1-S12",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_CLDGRPH~1",
    "surfaced_at": "2026-09-04T17:10Z",
    "one_line": "The deploy ledger's leg L5 -- 'derive family next launch on the pinned revision' -- was CLOSED on the first pass against a derive that ran on globgrph-derive-runner:6, the UNPINNED revision, and its own proof text says so ('NOTE the pin is NOT in force').  The pinned derive this order actually required is a DIFFERENT task (4a1baae562c8496983eb068146ae33d5 on globgrph-derive-runner:7, buckets read=34 / unreadable=0), and it has no leg: a closed leg cannot be reopened and the change_management/*.md is never hand-edited. The CLOSED ledger therefore reads as if the derive family's pinned launch were proven by a run that predates both the pin and the IAM grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/critical_paths/change_management/20260904T0756Z_cldgrph-cgs15-shared-image-digest-pins_deploy_completion.md, row L5, closed 20260904T085617Z: 'task-definition globgrph-derive-runner:6 ... Task 7286e56c80614ab49fa2fba791bb8b43 ... buckets read=0 / buckets unreadable=34 ... NOTE the pin is NOT in force: revision 6 references :latest'. Its `proof_required` reads 'ONE ad-hoc run-task exits 0 with its buckets read=N unreadable=M line', which that run DID satisfy -- the leg is not falsely closed, it is closed on a weaker fact than its own TARGET line names.",
        "THIS pass, measured: ecs run-task on globgrph-derive-runner:7 -> task 4a1baae562c8496983eb068146ae33d5, describe-tasks lastStatus STOPPED, exitCode 0, taskDefinitionArn .../globgrph-derive-runner:7, containers[0].imageDigest sha256:1b89853fe44133f10a60dc2b3e7b463c0d3b68b827a2ddff249bf427ecde2778, startedAt 1788539432.975 = 2026-09-04T16:30:32Z, stoppedAt 1788540008.657.",
        "The two runs differ in BOTH variables the leg exists to certify: the revision (6 unpinned vs 7 pinned) and the denominator ('s3 notifications buckets read=0 / buckets unreadable=34' vs 's3 notifications buckets read=34 / buckets unreadable=0', both read from /ecs/globgrph/derive-runner, streams derive-runner/derive-runner/7286e56c... and .../4a1baae5...).",
        "MECHANISM, not an oversight: deploy_ledger.py exposes open / close-leg / close / hold / check / list and NO reopen-leg or amend verb (`python .tools/deploy_ledger.py --help`), and CLAUDE.md forbids hand-editing the rendered entry. A leg closed on pass 1 cannot be corrected by pass 2 even when pass 2 is the same seat on the same order."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-CG-D-1 step 1 leg manifest: 'L5 exercise = the derive family's launch: ONE ad-hoc run-task on the pinned revision exits 0 with its buckets read=N / unreadable=M line in CloudWatch', and step 1 of the reopened face: 'close each remaining leg with deploy_ledger.py close-leg --proof ... Per the sentinel as restored, L1, L2, L3 and L5 are CLOSED and L4, L6 and L7 are still STRANDED.' The face treats L5 as settled.",
    "world_is": "A multi-pass task order and a single-pass ledger disagree about what 'closed' means. The ledger is append-and-close-once by design -- which is the right design for the failure it was built against (a stranded leg) -- but it has no way to say 'this leg was proven against an earlier world and re-proven against the current one'. The record that survives is the CLOSED entry; the correcting fact lives only in this row and in the deliverable beside it. A later reader auditing the pin by the ledger alone would cite task 7286e56c... as the pinned-derive proof, which it is not.",
    "notes": "INERT, not ARMED: nothing in the world is wrong -- the pins are applied, the pinned derive ran and exited 0, and the denominator is 34/0. The hazard is to a READER of the ledger, and this row plus the deliverable's closing section 'Ledger leg L5 -- read it with its date' are the correction. NOT REMEDIATED and deliberately so: reopening L5 would mean hand-editing a change_management/*.md, which this order forbids outright, and inventing an eighth leg after the entry is CLOSED would be worse. WHAT A FUTURE FACE COULD DO instead: when a task order is REOPENED, re-open its ledger legs whose target names an artifact the reopened pass will re-produce, or open a NEW entry for the second pass rather than inheriting the first pass's. Surfaced, not adjudicated; the significance of this is 3.0.0_SA_CVO's call at L9, not this seat's."
  }
]
```
