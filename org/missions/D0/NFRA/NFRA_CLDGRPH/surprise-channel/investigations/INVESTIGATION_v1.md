# NFRA_CLDGRPH -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, folder == project). Lane `ANY` (COO grant
@`bfec7d99b5`) -- the seat that sees it appends its own row; REMEDIATION rows stay `3.0.0_SA_CVO~A`'s.
**Append-only during the round.** Denominator at this write: **1 row** (S1, appended by `0.7.0_AE_CloudOps~P`
at 07:12Z while executing `NFRA_CLDGRPH.TO-CG-V-2` cells CG-s-11/12/13).
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
