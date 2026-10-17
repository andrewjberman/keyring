# TCKT_EARLYWARN -- surprise channel, INVESTIGATION v1 (round 1, dell1 fabric)

**Opened by:** `0.7.0_AE_CloudOps~TM1` at TO-EWS-d1 (the order names this file as its channel).
**Id grammar:** a seat's row on the main index is `TCKT_EARLYWARN-D1-S<k>` (the row gate refuses a `W` for a committer that is not a worker). The order text says `TCKT_EARLYWARN-Z-W1-S<k>`; the schema reserves the `Z-` infix for fabric `site-z` and this project's fabric is `dell1`, so `D1-` is used, as in TCKT_MTADTA.
**Append-only.** Never edit an existing row.

```json
[
  {
    "id": "TCKT_EARLYWARN-D1-S1",
    "project": "TCKT_EARLYWARN",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-17T04:58:00Z",
    "one_line": "The one container cannot run its default BRIDGE mode on the cert-only secret scope: HttpTransport raises bearer_not_configured without a gateway bearer, and no bearer secret exists in Secrets Manager.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "n/a (INERT: nothing is deployed; the apply is held until the grant is named)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/client-ops-early-warning/ews/bridge.py bearer_value(): env EWS_MAIL_BEARER, else Secrets Manager id EWS_MAIL_BEARER_SECRET_ID, else empty; HttpTransport.__init__ raises BridgeUnavailable(0, 'bearer_not_configured') on empty",
        "ews/config.py: EWS_MODE defaults to BRIDGE; BRIDGE_BEARER_SECRET_ID defaults to the empty string; GRAPH_APPONLY refuses until the Day 0 Test-ApplicationAccessPolicy read (README, record addendum 4)",
        "aws secretsmanager list-secrets --filters Key=name,Values=opal/ews read 2026-10-17T04:5xZ: exactly one secret, opal/ews/graph-app-cert (denominator 1)",
        "TO-EWS-d1 requirement 3: GetSecretValue on opal/ews/graph-app-cert ONLY; if the deploy needs the BRIDGE bearer, STOP and file a BLOCKING row naming the missing grant"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Deploy the runtime as one always-on container in the default BRIDGE mode with secretsmanager:GetSecretValue on opal/ews/graph-app-cert only, and the task reads RUNNING.",
    "world_is": "In BRIDGE mode the poller cannot construct its transport without a gateway bearer. No bearer secret exists, so the grant the runtime needs (secretsmanager:GetSecretValue on a bearer secret id, plus the EWS_MAIL_BEARER_SECRET_ID value) names a resource that has not been created or chosen. A container started without it exits on its first build_poller call, so a RUNNING read would be a crash loop or a launcher that swallows the refusal; neither is a deployed runtime.",
    "notes": "MISSING GRANT, named: secretsmanager:GetSecretValue on the BRIDGE bearer secret (id not yet chosen; the code reads it from EWS_MAIL_BEARER_SECRET_ID). Needed from the issuer: (a) the secret id and who mints the bearer value (a headless token for the gateway /hx/mail/messages route on Andrew's mailbox, record addendum 4), (b) a ruling that the role's secret scope widens from one secret to two, or that the bearer comes in as a task-definition secret injected by ECS (which needs the execution role, not the task role, to hold the grant). Unblocked work continues meanwhile: registry rows, the Dockerfile, the terraform module and a plan with no apply."
  },
  {
    "id": "TCKT_EARLYWARN-D1-S2",
    "project": "TCKT_EARLYWARN",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-17T04:58:30Z",
    "one_line": "The ews package has no runnable entry point (no __main__, no console script), and the order's grant forbids editing ews/ source.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "n/a (INERT: the Dockerfile carries the launcher inline)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "grep for __main__ and def main over infra/aws/ec2/client-ops-early-warning/ews/*.py: only ews/replay.py main(pkg_dir) matches, and it is the replay, not the poller",
        "ews/bridge.py build_poller(store, mode=None, **kw) and ews/poller.py BasePoller.loop(iterations=None) are the library seam; HttpTransport(base_url, bearer) and SqliteStore(path) are the parts a launcher composes"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The entry point is the poller loop, ews/poller.py / ews/bridge.py build_poller().",
    "world_is": "build_poller() returns a poller; nothing in the package constructs the store, the transport and calls loop(). The Dockerfile CMD therefore has to compose them inline (SqliteStore on the container filesystem, HttpTransport, loop()), without touching ews/. The store is SQLite on ephemeral task storage, so a task restart loses open items; the watermark is re-derived from EWS_INITIAL_CUTOFF.",
    "notes": "Not blocking. Persistence beyond the task's life is not in the order (no S3 write, no table in the role), so the open-items store is ephemeral by the order's own constraints."
  },
  {
    "id": "TCKT_EARLYWARN-D1-S3",
    "project": "TCKT_EARLYWARN",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-17T05:25:40Z",
    "one_line": "ews_check.py iam misfires on dell1 as written: its deny arms pass the lone argument '*' to aws.exe, which Windows expands against the repo-root listing, so simulate-principal-policy exits rc=254 before it can read a decision.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~Q1 (owns the check; the lane did not edit or weaken it)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/TCKT_EARLYWARN_Q1/EWS_CHECKS/ews_check.py iam from the repo root, twice (2026-10-17 05:1xZ and 05:2xZ): EWS-BAD RuntimeError: aws iam simulate-principal-policy --policy-source-arn rc=254, the error tail is the root directory listing (n, design, docs, ..., workflows)",
        "ews_check.py lines 73-76: the deny list carries ('ses:SendEmail', '*'), ('sns:Publish', '*'), ('sqs:SendMessage', '*'); line 59-61 simulate() passes the resource as one --resource-arns argument through bash .tools/aws",
        "AWS_SHIM_DEBUG=1 bash .tools/aws ... --resource-arns '*' prints argv [*] literal: the shim does not expand it, the native aws.exe does",
        "the checker's own functions run with only the aws subprocess cwd changed to an empty directory (.scratch/ews_iam_equiv.py, uncommitted scaffolding): EWS-IAM-OK, rc=0, all 3 allow arms allowed and all 6 deny arms not allowed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "ews_check.py iam prints EWS-IAM-OK for a role that may read the one secret and the two silver prefixes and may not read another secret, write S3, read bronze or send.",
    "world_is": "On this device the check cannot reach a decision: the lone '*' resource is wildcard-expanded by the Windows aws.exe against the current directory, so the call is malformed (rc=254). The role itself grades as ordered when the same code runs from a directory with no files. The check is cwd-dependent on Windows and reads BAD on a correct deploy.",
    "notes": "The lane did not weaken the check. The equivalent run is evidence about the role, not the criterion's own invocation: AC2 as written stays unmet on this device until the check passes the resource without a bare '*' (for example arn:aws:ses:*:*:identity/x) or is graded from a box or directory where the expansion does not occur."
  },
  {
    "id": "TCKT_EARLYWARN-D1-S4",
    "project": "TCKT_EARLYWARN",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-17T05:25:50Z",
    "one_line": "The image answers business days from lib/trading_calendar.py's hardcoded NYSE fallback (covers 2010-2027) because pandas_market_calendars is absent, so the early-warning clock goes wrong at the end of 2027.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~Q1 (a later order: regenerate the fallback or add the calendar package to the Dockerfile)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task log opal-clientops-ews-task stream ews/ews/73ccdcc4753448c68c1dd7156111588a: WARN: trading_calendar: pandas_market_calendars absent; answering from the hardcoded NYSE fallback NYSE/hardcoded-fallback-2010-2027 (covers 2010-2027; regenerate with lib/tests...",
        "ews/clock.py _calendar() imports trading_calendar from lib/ and is_business_day() calls it for every date the SLA clock crosses"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The business-hours clock uses the estate's one calendar (README, clock.py: lib/trading_calendar.py).",
    "world_is": "In the container the estate calendar runs in its offline fallback table, which is correct through 2027 and the image carries nothing to replace it. The package is not a dependency the Dockerfile installs and the order did not ask for it.",
    "notes": "ARMED only for dates after 2027; no action needed for this order. The first image (digest 5d68df7e..) lacked lib/trading_calendar.py altogether and its launcher logged ModuleNotFoundError on the first pass; the second image (2c1aef59..) carries the file and its task replaced the first task (apply 3); the first task's ephemeral store went with it."
  },
  {
    "id": "TCKT_EARLYWARN-D1-S5",
    "project": "TCKT_EARLYWARN",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-17T06:53:00Z",
    "one_line": "The first run_pending has logged no pass line and no failure line 86 minutes after launch, and the launcher logs nothing per date, so a slow replay and a hung one read the same.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~Q1 (owns the order's report; a progress line per date is a Dockerfile launcher change, which needs its own amendment)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task 73ccdcc4753448c68c1dd7156111588a read RUNNING by ecs describe-tasks at 2026-10-17T06:5xZ, startedAt 2026-10-17T01:24:06-04:00 (05:24Z), cpu 256, memory 1024",
        "log group /aws/ecs/opal-clientops-ews-task, 2 streams (denominator); the live stream ews/ews/73ccdcc4753448c68c1dd7156111588a holds 2 events, last at 05:24:12Z (launcher start line) and 05:24:28Z (calendar WARN), read 06:50Z",
        "Dockerfile launcher lines 66-78: the only post-start prints are the run_pending summary and the failure line, both after run_pending returns or raises; daily.py:48-57 run_pending loops every complete date with no log inside"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's report carries the first run_pending outcome (dates processed, items opened) and the COO asked for a row if it has not completed by 60 minutes.",
    "world_is": "86 minutes in, the replay of the complete dates has neither finished nor raised. The log cannot tell a slow S3 replay on a 256 CPU / 1024 MB task from a hang. No criterion grades this; AC1-AC3 read OK.",
    "notes": "The lane changed nothing. Next read: the same stream at the next tick; a pass line prints dates_processed and last_processed, a failure line prints type and place. The task's ephemeral store means a restart repeats the replay from the first complete date."
  },
  {
    "id": "TCKT_EARLYWARN-D1-S6",
    "project": "TCKT_EARLYWARN",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-17T07:05:00Z",
    "one_line": "The proof-of-spec instance for TO-EWS-d1 cannot validate: the order's cell EWS-d-1 is not in project.json, whose decompositions array is empty.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~Q1 (owns the order and the project register; the lane's grant does not cover project.json or the order)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/proof-of-spec-check.py <instance> EWS-d1-AC1,EWS-d1-AC2,EWS-d1-AC3 -> INVALID rc=1, one VIOLATION: alignment: cell_ref 'EWS-d-1' (cited by EWS-d1-AC1, AC2, AC3) does NOT exist in org/missions/D7/TCKT/TCKT_EARLYWARN/project.json; decomp id space = 0 distinct cell id(s)",
        "project.json keys decompositions=[] and prds=[]; the order says FAST-PATH, no decomposition, the cell is the order",
        "trial with decomp_ref.doc set to the order file: a second VIOLATION, the governing TO names project.json, so the instance and its TO disagree; the trial file was deleted"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's proof_of_spec block: the instance validates with proof-of-spec-check.py before the flip.",
    "world_is": "Every other limb passes (schema, 3/3 invocation alignment, 5/5 surprises resolve, vintage resolves); the one violation is the order's cell id against an empty register. No instance written for this order can validate until the order or the register changes.",
    "notes": "The lane did not weaken the checker or edit the order. The instance sits at the named path, INVALID on this one violation. Fix is the issuer's: register EWS-d-1 in project.json, or amend the order's decomp_ref and cell citation."
  },
  {
    "id": "TCKT_EARLYWARN-D1-S7",
    "project": "TCKT_EARLYWARN",
    "fabric": "dell1",
    "surfaced_by": "0.7.0_AE_CloudOps~TM1",
    "surfaced_at": "2026-10-17T09:20:00Z",
    "one_line": "TO-EWS-d2 requirement 1: the builder's state address for the store is in opal-data-49financial, whose DenyForeignFirmPrincipals fence does not admit opal-clientops-ews-role, so the order's role grant alone leaves every Get and Put denied.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "n/a (INERT: nothing is applied; the apply is held until the bucket is ruled)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/opal_naming.py address('schwab','49financial','state','ews_store','current','ews.db') -> s3://opal-data-49financial/schwab/49financial/state/ews_store/current/ews.db; grade(key,'S3Key') -> CONFORMANT (R21: state lives in the bucket of the tenancy; both Schwab masters 08335338 and 08242234 are FIRM scopes homed in opal-data-49financial per infra/logic/registry/scopes.json)",
        "aws s3api get-bucket-policy opal-data-49financial: statement DenyForeignFirmPrincipals denies s3:* to every principal not in its ArnNotLike list (31 entries, read in full); arn:aws:iam::313476888478:role/opal-clientops-ews-role matches none (the only wildcard is role/*-49f-*)",
        "infra/logic/registry/exemptions.json holds no row for the role; every admitted principal carries a CTO and COO never-widen signoff_ref (CLAUDE.md section 5, first NEVER)",
        "aws s3api get-bucket-policy opal-data-assets: 2 statements (DenyParquetUnderBronze17a, AllowMdpfPortalCloudFrontOACRead), no firm fence; builder tier homes put only bronze and silver there for a FIRM scope"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order: the bucket, prefix and key are address() output, and the role widens to that one prefix; AC1 simulates the role against the manifest's key.",
    "world_is": "The builder-correct address sits behind a fence the role is not in. Admitting the role is a bucket-policy change on a firm bucket (exemptions.json row plus a never-widen CTO and COO signoff), which the order's paths do not grant. The simulation in AC1 ignores the resource policy, so AC1 would read EWS-PIAM-OK while the live Put is denied.",
    "notes": "The lane applied nothing. Two ways out, both a ruling: (A) keep the 49financial address and obtain the fence admission with a Get/Put-only scoped exemption on the one key; (B) a registry deviation (R20) homing this state in opal-data-assets. The launcher change (items_opened lines, persist code) is independent of the bucket and proceeds. AC3 must be graded by the object's existence, not by AC1."
  }
]
```
