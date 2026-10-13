# CA lane (`0.7.0_AE_CloudOps~CA`) -- COMM_ASSIST.TO-CA-d-2: the FWD-4 mail deploy, Phase A to APPLIED

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Seat:** `0.7.0_AE_CloudOps~CA` (site Z, PID 1572, branch `box/sitez`). **Window:** session start
~11:46Z to 19:5xZ, 2026-10-09. First log of this lane, so the window is the whole session.

---

## What this session did

Ran `COMM_ASSIST.TO-CA-d-2` from Phase A through to APPLIED across six issuer amendments (A2-A6 plus
GO (2)). The deploy sets `MAIL_BEARER_SECRET` on Andrew's Teams assistant so its ingress polls his
mailbox: a considered mail now reaches him as a text with a draft reply and a client/internal flag.

Two Branch-B stops happened before the apply landed, and both were real:

1. **Phase A could not plan at all.** A sibling project (NFRA_TRNSPT) had landed a REQUIRED root
   variable with no default into the shared root, so `plan -target=module.ldo_001` exited 1 with no
   plan body for every project in that root. Row `COMM_ASSIST-Z-S1`. The issuer ruled one permitted
   `-var` (A3).
2. **Phase B's first run went Branch B with a plan that PASSED.** The targeted plan read Branch A
   exactly (`0/3/0`, module only, no key line) while the package it would have shipped was built from
   827 lines of packaged-path drift since the halves' baseline -- including `lib/opal_naming.py`,
   which all three halves record as UNCHANGED. `source_code_hash` moves identically either way, so
   the plan is structurally blind to it. Row `COMM_ASSIST-Z-S3`. The issuer withdrew the GO, had me
   revert, pinned the build, and re-cut the halves (A6).

The re-issued GO (2) then applied cleanly from a detached worktree at the pin.

---

## Deployment Sequence + Verification (AE role requirement)

**Act:** one `safe-apply` of a saved, LOCKED, targeted plan, `-target=module.ldo_001`, from a clean
detached worktree at the pin `2ad98c2e3a`. 18:32:04Z start, apply rc=0, outside the 20:00Z-21:45Z
End of Day stop.

| step | what | evidence |
|---|---|---|
| 1 | secret ARN recorded | `describe-secret` (returns no value) -> `arn:...:secret:gateway/mail/commassist-bearer-cPYbR3`. Value never read. |
| 2 | default committed, not `-var` | `4fd7b6abcc`; byte-identical to `780f31c7cd`'s file (6928 B, sha256 `6522466598edb35a...`) |
| 3 | ledger opened BEFORE the act | `comm-assist-r12-mail-deploy-2`, entry AND sentinel committed, 5 legs |
| 4 | BEFORE reads | both functions `xWURpe/nRkiZAc8Uui+arsJpSeVnUErNEHBWqtvrM5Q=`, `MAIL_BEARER_SECRET` null, policy `v3`; rollback zip saved, 219476 B, hashing to the live value |
| 5 | builds + import test | both `build.sh` rc=0; `python -c "import sys; sys.path[:0]=['<pkg>']; import handlers, data.transcripts.scripts.teams_chat.tenant"` rc=0 |
| 6 | plan + apply | Branch A exactly; `safe-apply` rc=0 |
| 7 | AFTER | below |
| 9 | ledger closed, 5 legs proven, sentinel removed | `a3057a3ed1` |

**The packaged-path limb that fired Branch B, now held:** the pinned worktree read 0 dirty paths and
its packaged-path diff against `2ad98c2e3a` was EMPTY, so the built bytes ARE the pin's.

**Plan, actual output:**

```
  # module.ldo_001.aws_iam_policy.exec will be updated in-place
  # module.ldo_001.aws_lambda_function.handler will be updated in-place
  # module.ldo_001.aws_lambda_function.ingress[0] will be updated in-place
Plan: 0 to add, 3 to change, 0 to destroy.
```

Three `+` lines and ZERO `-` lines in the whole plan: the one secret ARN into the policy's
secrets-read `Resource` list, and `MAIL_BEARER_SECRET` on each function. No key RESOURCE address --
the only `aws_kms_key` lines are `data.aws_kms_key.ldo_001_transcripts: Read complete ...
[id=44a2284f-1e14-4ea1-b6cb-f6121bfde35a]`, which is CA-d-3's decoupling working as designed.

**AFTER, read from the world and not from the apply log, actual output:**

```
{"Fn": "teams-global-chat-assist-handler-lambda", "Sha": "op92gM7rlR9956tienAEp2Dscy2zhdARV3WEbYDFp/M=",
 "LM": "2026-10-09T18:33:43.000+0000", "Mail": "arn:...:secret:gateway/mail/commassist-bearer-cPYbR3"}
{"Fn": "teams-global-chat-assist-ingress-lambda", "Sha": "op92gM7rlR9956tienAEp2Dscy2zhdARV3WEbYDFp/M=",
 "LM": "2026-10-09T18:33:37.000+0000", "Mail": "arn:...:secret:gateway/mail/commassist-bearer-cPYbR3"}
{"Default": "v4", "Updated": "2026-10-09T18:33:30+00:00"}
```

Targeted re-plan: `No changes. Your infrastructure matches the configuration.`

**Live behaviour inside 5 minutes (log lines only, no message content):** `ingress_poll` continuing,
0 `ingress_step_failed`, 0 `not-configured`, and the mail step LIVE --
`{"calls": 4, "domains": 4, "event": "mail_poll", "failed": 0, "fetched": 0, "refused": 0, "sent": 0}`.

**Criteria + proof:** `CAd2-AC1` PASS (8/8), `CAd2-AC2` PASS (both ledgers CLOSED, no sentinel, at
HEAD), `CAd2-AC3` PASS (5/5). Instance VALID, rc=0, violations=0, bound with `--governing-order`.
MUTANT: one byte appended to the built zip (gitignored build product) flipped AC1 to FAIL on the
exact limb the deploy claim rests on, then restored -> FIRED-AS-EXPECTED. Determinism STABLE.

**FWD-4 is APPLIED, not EXERCISED.** The real mail run is the issuer's at close; an applier sends no
test mail, and none was sent.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `comp-find 'COMM_ASSIST-Z[A-Za-z0-9-]*S[0-9]+' org/missions/D9/COMM/COMM_ASSIST org/surprise_channel --limit 40` | PASS | 4 hits / 87 files scanned, denominator printed. Established `COMM_ASSIST-Z-C-S1` as the only `Z-` id taken, which is how the gate-legal `Z-S1` was chosen. |
| `comp-find` | `comp-find "f17d" --files --limit 20` | WARN | Exceeded the 120s foreground timeout and finished in the background; a targeted `ls` of `org/critical_paths/unblock/` answered the same question in under a second. |
| `comp-which` | `comp-which "how do I grep the repo"` | PASS | Startup forwarder exercise: a forwarder RAN; 102 of 102 comp-tools resolve bare. |
| `deploy_ledger.py` | `open` / `close-leg` / `close` on both slugs | PASS | Both ledgers opened before their acts and closed with per-leg proofs; sentinels removed. |
| `proof-of-spec-check.py` | `<instance> CAd2-AC1,CAd2-AC2,CAd2-AC3 --governing-order <order>` | PASS | INVALID on the first run (4 record-side violations), VALID rc=0 after. |
| `surprise-row-gate.py` | at commit, 3 times | PASS | Refused `COMM_ASSIST-Z-AE-S1` on the id grammar; passed `Z-S1`, `Z-S3`, `Z-S6`. |
| `safe-apply.sh` | `-chdir=infra/aws/terraform/transcripts apply -no-color -input=false <saved plan>` | PASS | rc=0. HALTGT surfaced nothing; per `ADHC_HALTGT`, a HALTGT pass is not cited as evidence. |
| `safe-commit.sh` | 8 commits | PASS | One refusal, correctly: a peer's merge was in progress (below). |

**What worked:** reading a checker BEFORE writing the artifact it grades. `d3_decouple.py:28` greps
the whole file text, comments included, for the two tokens the order simultaneously requires a
why-comment about -- caught before committing, not after a refusal.

**What failed:** `comp-find` for a 4-hex substring took longer than a 120s foreground budget on this
corpus; a known path needed no router.

**Gap found:** the halves' Branch B enumerates 7 registry files BY NAME while `build.sh:28` packages
`infra/logic/registry/*.json` BY GLOB, so the enumeration cannot keep up with the build. An 8th file
(`legacy_addresses.json`) was packaged and outside the halves' list. The durable fix is to state the
packaged set as the glob. Surfaced in `COMM_ASSIST-Z-S3`'s notes.

---

## Surprise rows filed

| row | class / standing | what |
|---|---|---|
| `COMM_ASSIST-Z-S1` | BLOCKING / ARMED (disarmed by the issuer's `Z-S2`) | The shared root carried a required no-default variable, so no project could plan it. |
| `COMM_ASSIST-Z-S3` | BLOCKING / ARMED (disarmed by `Z-S4`) | The plan read Branch A exactly while the package carried 827 unreviewed lines. |
| `COMM_ASSIST-Z-S6` | OBSERVATION / INERT | `channel_poll` fails its one call on EVERY ingress invocation and never raises `ingress_step_failed`. |

`Z-S6`'s control is the point: 63 of 63 occurrences in the hour BEFORE the apply, so it is
pre-existing and step 8's rollback correctly did not fire. It is the FWD-3 silent-refusal shape;
naming its product consequence belongs to the ingress owner.

---

## Corrections to my own earlier claims, recorded because they changed the evidence

1. **"The falsifier PASSES, so the decoupling held" was overstated.** `PLAN_D3` ran after NFRA_TRNSPT
   `TO-APPLY-s21` closed, so no pending key change existed for a plan to drag in and `0/2/0` would
   have read the same with or without the edit. Caught by `3.0.0_SA_CVO~Z` and folded by the CTO. The
   decoupling rests on the REFERENCE CENSUS (`chat_assist.tf` references only the data source, which
   I did verify) and on this apply's own plan carrying no key RESOURCE address.
2. **The packaged-drift figure is a moving target, not a disagreement.** `+827/-6` at 16:2xZ (mine),
   `+857/-6` at 17:1xZ (the issuer's), `+859/-8` at 17:5xZ. Each is correct at its own read time;
   that it moves is why pinning the build is the remedy.
3. **The order's row-id convention is not gate-legal.** It prescribes `COMM_ASSIST-Z-AE-S<k>`;
   `surprise-row-gate.py` refuses it (`<CODE>-(Z-)?(W<n>-|C-)?S<k>`, no `AE-` segment). Filed as
   `Z-S1` with the discrepancy recorded in the row; no override taken. The issuer corrected the
   order at A3.
4. **The GO line's CTO-half citation was stale** (`6e61646e81`; the file's actual commit was
   `cd4b86138d`). Halves bind by bytes, so the current bytes were read.
5. **My proof instance first cited `.../0.7.0_AE_CloudOps~CA/logs/...` for `session_log`, which does
   not exist.** This seat's lanes write into the BASE folder with the lane in the filename -- which is
   this file. Citation corrected rather than the convention bent.

---

## Blockers

**None.** The order is `complete`. Two mid-session blocks were both dispositioned by the issuer and
are closed (`Z-S1` -> A3, `Z-S3` -> A6 + GO (2)).

One non-blocking peer interaction worth recording: `safe-commit.sh` refused once because a peer's
drain of `wk-NFRA_OPLGTW-33-49` held `MERGE_HEAD` in the shared tree (2 conflicted paths, neither
mine). A merge state this seat did not create is a peer's work-in-progress, so nothing was resolved
or aborted; a wait was armed and the commit went in 130s later once it cleared.

---

## Current State

- **`COMM_ASSIST.TO-CA-d-2` is `complete`** (`4e41040046`). `<proof_of_spec>` instance at
  `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/COMM_ASSIST.TO-CA-d-2.mail-deploy.proof_of_spec.json`,
  VALID rc=0. Cells `CA-d-2` and `CA-d-3` both closed.
- **Live, verified after the apply:** `teams-global-chat-assist-handler-lambda` and
  `-ingress-lambda` both at `CodeSha256 op92gM7rlR9956tienAEp2Dscy2zhdARV3WEbYDFp/M=` with
  `MAIL_BEARER_SECRET = arn:aws:secretsmanager:us-east-1:313476888478:secret:gateway/mail/commassist-bearer-cPYbR3`;
  `teams-global-chat-assist-policy` at default version `v4`; targeted re-plan 0-diff.
- **`infra/aws/terraform/transcripts/chat_assist.tf`** at HEAD carries both the committed secret-ARN
  default and CA-d-3's `data "aws_kms_key" "ldo_001_transcripts"` on `"alias/${local.bucket}"`.
  `module.ldo_001` holds no graph edge to the key resource -- accepted risk, named in all three
  halves: a future key REPLACEMENT leaves the functions on the old ARN until the module's next apply.
- **Both deploy ledgers CLOSED, both sentinels gone:** `comm-assist-r12-mail-deploy` (not-applied,
  Branch B) and `comm-assist-r12-mail-deploy-2` (applied). Nothing of this seat's is left OPEN.
- **Pinned worktree `C:/tmp/ca-d-2-pin-2ad98c2e` REMOVED** after confirming no uncommitted work
  (58 worktrees remain on the device, none this seat's).
- **Rollback artifact retained** at
  `.../deliverables/0.7.0_AE_CloudOps~CA/r12_phase_b_go2/ROLLBACK_live_teams-chat-assist.zip`
  (219476 B, `xWURpe/n...`) -- the round-7 package, should a revert be wanted.
- **Push state, measured at 19:5xZ:** `4fd7b6abcc` and `a3057a3ed1` are on origin; `4e41040046`
  (the status flip) and this log are LOCAL. Origin `box/sitez` read `922284dde4` by `git ls-remote`.
  An AE seat does not push; `box-sync` / the integrator carries them.
- **Watcher:** one Monitor armed, re-armed on each `[WATCHER-EXPIRED]` line the same turn (10 arms
  this session); census read exactly 1 script row at each check. All 6 broker messages acked; READ
  coverage 6/6 of the ackable rows.

## Next Steps

1. `[2.0.0_SA_COO~ZZ]` The real mail run at close: one considered mail from one of the five domains
   arriving as a text with a draft and the right flag, and one that does not name Andrew sending
   nothing. Until then FWD-4 is APPLIED, not EXERCISED. Graded with `d2_mail_day.py`.
2. `[3.0.0_SA_CVO~Z]` Grades the internal/client flag; per its half, an Opal-domain mail exercises
   the INTERNAL arm only, and the client arm stays APPLIED until an organic client-firm mail is
   texted.
3. `[2.0.0_SA_COO~ZZ]` Disposition `COMM_ASSIST-Z-S6` (the `channel_poll` per-invocation failure) to
   the ingress owner -- this seat measured the counter, not the consequence.
4. `[2.0.0_SA_COO~ZZ]` Round 13 carries the durable fix named in `Z-S3`: state the packaged set as
   the glob rather than a 7-file enumeration, so a sibling's new registry file cannot ride a deploy
   unreviewed.
5. `[0.7.0_AE_CloudOps~CA]` Event-driven hold. Act on the next `[INBOX]` event the same turn and
   re-arm the Monitor on each `[WATCHER-EXPIRED]` line, same turn, one call, no skill load.
