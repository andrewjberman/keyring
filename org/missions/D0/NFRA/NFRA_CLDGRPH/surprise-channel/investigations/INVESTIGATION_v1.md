# NFRA_CLDGRPH -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, folder == project). Lane `ANY` (COO grant
@`bfec7d99b5`) -- the seat that sees it appends its own row; REMEDIATION rows stay `3.0.0_SA_CVO~A`'s.
**Append-only during the round.** Denominator at this write: **10 rows** (S1-S10). Corrected 2026-09-03 09:0xZ by
`0.7.0_AE_CloudOps~Q` on the issuer's instruction (93402): the line still read **1 row** while the file held 9, so the
header understated the channel by 9 -- a denominator that ages silently is the defect this project keeps finding in
other carriers. Authorship is per-row in `surfaced_by`, never the header and never the committing author.
**Round 1 task orders:** two live -- `TO-CG-V-1` at `0.7.0_AE_CloudOps~Q`, `TO-CG-V-2` at `0.7.0_AE_CloudOps~P`.

## S1 -- the ADD-CHECKLIST grants on a role that does not exist

Surfaced while executing **CG-s-13** (the AuthKind read), which the TO scopes to `registry.py` +
`NFRA_INTEGRATIONS_STANDARD.md`. The AuthKind question itself resolved cleanly (`AuthKind.NONE`); this is the
mismatch found beside it.

`NFRA_INTEGRATIONS_STANDARD.md` §5 step 4 is the IAM step of the **mandated 5-step ADD-CHECKLIST** -- the canonical
contract every new gateway integration is built against. It instructs the author to grant
`secretsmanager:GetSecretValue` on the new secret's ARN **to `m365-mcp-gateway-role`**. That role does not exist in
account `313476888478`. The live gateway instance role is `opal-gateway-role`, and it is the role the gateway
instance actually carries.

**Why it is ARMED rather than inert, and why it is NOT blocking THIS task order:** for `AuthKind.NONE` -- the kind an
agent graph traversal fits, and therefore the kind CG-s-5 will build -- steps 3 and 4 are vacuous by the checklist's
own parenthetical (`(SHARED_SECRET)` / "on that exact secret ARN"), because a `NONE` integration provisions no secret.
So CG-s-5 is unharmed and nothing here changes this TO's verdicts. The harm lands on the **next SHARED_SECRET
integration**: an author following the canonical contract literally writes Terraform against a principal that is not
there. That is the future-normal-operation test the `ARMED` standing exists for.

⚠ **The defect is in `NFRA_INTEGRATIONS`'s document, not in this project's surfaces.** This seat SURFACES and does not
adjudicate the routing; `3.0.0_SA_CVO~A` reads this file at L8 and disposes.

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

Surfaced while executing **CG-s-10**'s mandated `comp-read` of `kuzu_incremental_refresh.py` (TO-CG-V-1
`<compiler_tools_mandate>`, BEFORE WRITE). The full-fallback trigger and threshold resolved cleanly
(`:174`, `FALLBACK_MIN_ABS=4000` / `FALLBACK_FRACTION=0.25`); this is the mismatch found beside them.

The engine's module docstring closes with *"Gated OFF by default (`GLOBGRPH_KUZU_INCREMENTAL_REFRESH=1`)
pending CTO arch-gate of the design."* Its **only** caller reads that same flag with a default of `"1"` --
i.e. ON -- and its own docstring says so in as many words. `NFRA_KUZUSPLIT_PRD.md` records the CTO GO as
landed (`195732Z`, "LIVE default-on"). **Two carriers of one quantity disagree, and the stale one is the
file a reader opens FIRST.**

**Why ARMED rather than inert:** `CG-s-2` ports this exact engine to the cloud worker. A seat reading the
engine to establish whether the incremental path is live concludes it is not -- and a port carries the
stale claim with the code, which is precisely the "QUALIFIED verdict travels with the code" shape the
brief's F4 already flags for this file's sibling. **Not blocking THIS task order:** AC3 invokes the
script *directly*, and the flag is read only at `_canonical.py:450`, so no measured number here depends
on it.

⚠ This seat SURFACES and does not adjudicate the routing, and it is barred by its own BOUNDS from editing
repo source ("No edit to any repo source. The engine is invoked, not changed.").

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

Surfaced while re-grounding TO-CG-V-1's premises before measuring (the L7 first act the GO names).

The TO's BOUNDS say a parallel temp-path run "needs no lock". That is **true of `_canonical.py`'s mkdir
mutex** -- invoking `kuzu_nessie_load.py` directly bypasses `_canonical` entirely, so this seat never
touches `kuzu_nessie_db.rebuild.lock`. It is **false of the loader's own singleton**: `_LOCK_PATH` is keyed
to the **script's directory**, not to `--db`, and `_acquire_singleton_or_exit()` runs unconditionally
before `main()`. So a temp-path full load serializes against every other full load on the device.

**Why ARMED, and why it is nonetheless the right thing to have run:** for the duration of each measured
full load, a concurrent `_canonical` rebuild is refused `rc=4` and the caller serves the existing DB
**labeled stale** -- the engine's own designed fail-safe (no corruption, no wrong DB), and the singleton
invariant Andrew ordered 2026-07-30. The hazard is bounded by the run and disarms when the measurement
completes. AC2 requires two full loads; there is no temp-path form of this engine that avoids the lock,
so the alternative to accepting it is not measuring at all.

⚠ **This is a correction to the TO's premise, not a defect in the engine.** The singleton is behaving
exactly as designed and as documented at `:295-327`.

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

Observed while establishing the live-state baseline that TO-CG-V-1 requires before measuring ("the current
lock state"). Recorded as a **residue observation, not a diagnosis**: this seat did not establish WHY the
rebuilds died and is not claiming a defect in the CE-G-5 layer.

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

Surfaced at the **final** step of TO-CG-V-2, validating the proof instance V2-AC7 itself demands. Every measurement
in the task order is done and passing; this is a one-token encoding defect on the TO's issuance half that no act
available to the assignee can clear. **Filed BLOCKING and routed to the issuer in the same turn, per the TO's BOUNDS.**

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

The disarm owner named in S5 acted before this seat reported, so S5's blocking condition is gone in the world.
Recorded as a NEW row because the channel is append-only. **This is an acknowledgement, not an adjudication --
S5's disposition stays `3.0.0_SA_CVO~A`'s at L9.**

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

The disarm owner named in S1 (`1.0.0_SA_CTO~A`) acted at @`f9ca7a9309` before the channel file's first commit, so S1's hazard is
gone in the world. Recorded as a NEW row because the channel is append-only. **This is an acknowledgement, not an adjudication --
S1's disposition stays `3.0.0_SA_CVO~A`'s at L9.** Scope of "sibling occurrence" = every token of the same 2026-08-14 rename in
the same file, accepted by the L9 seat (93316 item 4) before this row was written.

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

Found by AC2's own measurement: both full loads produced byte-identical DBs, and the manifest each wrote
disagrees with the DB it describes. **`node_count` agrees exactly; only `edge_count` is wrong**, and the
INCREMENTAL path writing the same field for the same graph gets it right. The full loader increments its
counter once per `MERGE` executed (61,071 read - 383 skipped endpoints = 60,688 merges), but `MERGE`
collapses duplicate `(src, dst, edge_type, props)` identities, so 2,256 of those merged onto an edge that
already existed. It then stamps the merge-attempt count as `edge_count`.

**Why it matters to THIS project rather than being a local curiosity:** `CG-s-3` (FWD-3, FWD-7) is
*"S3 versioned artifact + `_build_manifest` + ONE pointer object"* -- the manifest IS the provenance
record a cloud consumer reads, and `CG-s-7` repoints `comp-graph status` at that manifest. A port carries
this field to the cloud, where a consumer comparing a manifest `edge_count` against a live graph count
would read a 3.9% phantom drift that is an artifact of the producer, not of the data.

⚠ **This seat surfaces and does not fix** -- BOUNDS bar editing repo source, and CG-s-9/R10 already own
the loader's node/edge key handling at the port.

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

Found while gathering the runtime-sizing inputs for `B2-AC1` (TO-CG-B-2), reading the loader's own
watchdog block rather than a document about it.

`kuzu_nessie_load.py:389-393` sets `KUZU_REBUILD_DEADLINE_S` to a default of **1800 s** and justifies
that number in-source: *"a full rebuild is ~6min, so 5x headroom"*. **That justification rests on the
same ~6 min figure `CG-s-10` measured and falsified.** Against the measured full load (935.500 s and
1001.172 s, 2 of 2 runs) the real headroom is **1.80x**, not 5x. Nothing is failing today -- 1800 s
still exceeds 1001 s -- which is exactly why it is worth a row rather than a shrug: the margin is a
quarter of what the code says it is, and the number was never re-derived when the duration changed.

**Why ARMED, and why it lands on THIS port:** `B2-AC1` sizes a cloud worker that runs this loader, and
the cloud number is UNMEASURED (that is `B2-AC6`'s job) with a NAMED reason to expect it to differ --
`CG-s-10`'s memory-pressure caveat cuts both ways. A cloud full load only **1.8x** slower than the
laptop's would hit the watchdog, and `_deadline_exit` is not a graceful degrade: it calls
`os._exit(3)` after releasing the singleton, so the run dies mid-build and the caller falls back. A
worker inheriting an un-restated 1800 s default would be sized against a comment, not a measurement --
which is the precise failure mode `PRD s.6 R5` exists to forbid ("decided by the MEASURED full-fallback
duration, not the document claim").

**Disarm is this seat's, at this port:** set `KUZU_REBUILD_DEADLINE_S` EXPLICITLY in the task
definition from the measured number with its headroom stated, rather than inheriting the default, and
say so in the runtime decision. Recorded as a row first because the finding is about the ENGINE and
outlives my task definition -- a later caller that does not set it still inherits 1800 s justified by a
stale comment.

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
