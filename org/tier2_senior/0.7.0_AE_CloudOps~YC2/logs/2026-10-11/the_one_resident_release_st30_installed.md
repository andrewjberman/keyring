# The one resident release: st30 installed over st27, and the two gates that made it safe to do

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Serial:** `0.7.0_AE_CloudOps~YC2` (lane, dell2, respawned on a request from `2.0.0_SA_COO~G2`)
**Window:** 2026-10-11 ~10:15Z (respawn) -> 10:50Z. Prior log `75ca48da5d`
(`windows_8_and_9_plus_the_host_listing_and_three_checks_that_caught_me.md`).
**Order:** `IRPT_YCDGEN.TO-APPLY-st30.the-one-resident-release-dell2` -- `<risk>WORLD</risk>`,
`<proof_genre>DEPLOY</proof_genre>`, cell `YCD-d-10`, now `<status>complete</status>`.
**Commits:** `5d51ad0c54` (ledger OPEN), `52a36b4910` (the close). On origin `box/dell2` @`19a554964f`
(`git ls-remote` read; `52a36b4910` measured an ancestor of that tip, with a reversed-direction control).

---

## Current State

Written for a reader with zero prior context.

**The resident host `i-0167fd745ad906a66` now runs package root `/opt/irpt-resident/37210c771a-st30`.**
It had been running `e606008994-st27` since 2026-10-09 12:12:01 UTC. One host, one new root, one restart.
Unit `irpt-analysis-resident.service`, active, `NRestarts=0`, MainPID `864777` (was `777546`),
`ActiveEnterTimestamp` 2026-10-11 10:32:22 UTC, 3 `IRPT_RESIDENT_POLL` in 60 s, 0 tracebacks.

**There is NO removal leg in this order.** st30 STAYS. `remove_st30_to_st27.sh` (X1 + V2) was not run and
is not to be run without a new word from `2.0.0_SA_COO~G2`. Both rollback arms are measured ready, not
assumed: the `e606008994-st27` root is still on the host; the pre-swap library copy is kept as
`/opt/investor-reporting-ycharts/ycharts_session.js.before-37210c771a-st30`; and the rollback package
`irpt-resident-e606008994-st27.tar.gz` is in S3 with metadata sha256 `20916261...da39e4`, equal to the
packet's declared value -- that object was the positive control for U2's 404 check, so one read did both jobs.

**What the release changes** (the packet's seven groups): S1 reason fix + page sentence, S2 ticket reference
admitted, S3 read-back release 390 s, S4 research policy row now names 3 firms, S5 one WARN journal line per
READY, S6 refusal reason classes, S7 optional schema members. Per the CTO half, S1/S3/S6/S7 ship **APPLIED,
UNEXERCISED**; S2 and S5 are exercised by TCKT_VNEXT's fourth run under that project's own pair; S4's row is
on the host (3 firms) but its after-read is a separate served-read act this order does not carry.

**Artifacts.** Two new S3 keys under `ec2/investor-reporting-ycharts/resident/` in
`opal-313476888478-lambda-artifacts`:
`irpt-resident-37210c771a-st30.tar.gz` (version `OWZn2pqssd.UtbqPu0IflObnVKGOGKsi`, 999816 B, sha256
`e5a6b625...da241`) and `resident_host_install_37210c771a-st30.sh` (version
`6cZz46hLKzGR_9FOAeHemDZQ5Yfgmf6l`, 8705 B, sha256 `dd857258...4b969`).

**Records.** `org/tier2_senior/0.7.0_AE_CloudOps~YC2/deliverables/irpt_ycdgen_st30/P1_PRE_READ_20261011.txt`,
`.../D2_V1_INSTALL_20261011.txt`, `.../IRPT_YCDGEN.TO-APPLY-st30...proof_of_spec.json` (VALID, rc=0),
`org/critical_paths/change_management/20261011T1025Z_irpt-resident-st30-20261011_deploy_completion.md`
(CLOSED 20261011T103416Z, 4 of 4 legs).

**Nothing is held by this lane.** Zero orders open, ledger closed, both reports sent and byte-verified.

---

## What I actually did, in order

**The GO was tested at the bytes, not read off the order.** This pair had already been invalidated once: the
CTO ruled the half signed against packet blob `e6bec0e8cb` did **not** cover an install (msg 4662), and the
issuer restated the packet because three of its four after-reads were not drivable by a seat. So before
touching anything I printed the blobs. COO half `NEVER_WIDEN_PACKET_ST30.md` working-tree blob
`f81df64584525150dcc2e2a41bfec2bb6e3d7102` == its blob at `b0c75d2f04`, and `b0c75d2f04` **is** an ancestor
of HEAD. CTO half `NEVER_WIDEN_RESIDENT_ST30_CTO_HALF.md` working-tree blob
`983257e456b4d21ebf5e414218f012b4331060a6` == its blob at `e2346b95f8`. The re-signature's own text names
blob `f81df64584`, so signature and bytes agree in both directions. Both files clean in `git status`.

**I opened the ledger before U2, not after it.** The order numbers U2 first and the ledger second; NEVER-2
says the entry is opened at START, and the S3 puts are the first acts with a durable effect outside this box.
So the ledger went first, declaring all four legs, and `deploy_ledger.py` committed it in the same breath
(`5d51ad0c54`). Deliberate departure from the order's numbering, in the direction the law requires, no change
to the act, and it is named in the proof instance as a control.

**U2.** Both target keys `404 Not Found` (rc 254) before the put. A 404 reads identically whether the key is
absent or the call is broken, so the control ran in the same sweep and the same prefix:
`irpt-resident-e606008994-st27.tar.gz` returned rc 0, 876572 B, a real VersionId. **The keys came from the
consumer, not from the disk.** The tar's local basename is `37210c771a-st30.tar.gz` but the host fetches
`irpt-resident-37210c771a-st30.tar.gz` -- the installer's own `KEY=` line at `:12`. Uploading under the
basename would have produced two green sha256 read-backs and a host fetch that 404s. Read back **by version**
with sha256 recomputed from the returned bytes; both EQUAL to local and to the order's declared prefixes, so
no rebuild is implied and the STOP did not fire.

**P1.** `host_read.py pre_read.sh`. The STOP is PASS: `IRPT_ANALYSIS_READY_QUEUE_URL` reads 0 three ways --
unit Environment 0, running process (pid 777546) 0, unit and drop-in files 0 -- and the two places a drop-in
could hide are enumerated beside it (`EnvironmentFiles` EMPTY, the only drop-in `opal-render.conf`), which is
why the three zeros are not hiding an unread file. AC1's `grep -c` = 1 with the FAIL-line control at 0. The
installer's exits 10 and 18 were confirmed as preconditions that hold rather than risks: the st27 root is
present AND was the running root; host wrapper `55ddb8f7...` == `WANT_WRAPPER`; host library `857d90b8...` ==
`WANT_LIBRARY`.

**D2 + V1.** The gate was never forced. `irpt-generation` read 0 visible / 0 in flight **five** times: the
host's own P1 read, the SQS API from this box immediately before the send, the installer's own read before the
library swap, its own read before the stop, and again at V1. The bytes are bound **on the host**:
`install_st30.sh` verified the installer's sha256 there before running a line of it, and the installer
verified the tar's sha256 there before extracting -- stronger than any control-plane re-read, which is why I
did not add one.

---

## Deployment Sequence + Verification (AE)

| leg | act | instrument | result |
|---|---|---|---|
| U2 | put 2 keys, read back by version | `aws s3api put-object` / `get-object --version-id` + `sha256sum` | both EQUAL to declared |
| P1 | read-only pre-read | `host_read.py pre_read.sh`, ssm `b47317a9-bbe9-4f20-b941-29a7076e184d` | Success rc 0, STOP PASS |
| D2 | install | `host_read.py install_st30.sh`, ssm `39cacd01-6a93-4a7e-86be-8080f1c84b80` | Success rc 0, install rc=0 |
| V1 | read-back | the same invocation's tail | 8 of 8 expectations met |

Actual output, V1 (from `D2_V1_INSTALL_20261011.txt`):

```
package SHA256SUMS OK (294 members)
queue visible/in-flight before the library swap: 0 0
factory OK: ['assembly', 'queue_url', 'sqs'] enrolled 1276035
queue visible/in-flight: 0 0
install 37210c771a-st30 rc=0
active=active polls_30s=2 tracebacks_30s=0
V1 running root /opt/irpt-resident/37210c771a-st30 active=active restarts=0
V1 allow list: OPAL_PRODUCER_PRINCIPALS = ("andrew@opalinvest.com",)
V1 worker sha256 a9f71b6d236e7a9ee0f66f8acb488b2968b8805a47fa90ef454aae3dfbb751fa (built a9f71b6d236e7a9e...)
V1 producer import OK: family YCHARTS_OPAL_REPORT allow list ('andrew@opalinvest.com',)
V1 producer_for svc -> YCHARTS | andrew -> OPAL | other -> YCHARTS
V1 packaged research row firms: ['cottonwood', '49financial', 'inflection']
V1 queue: 0	0
V1 journal 60s: polls=3 tracebacks=0
V1 S2 packaged request schema names ticket_id: 1
V1 S3 read-back release seconds: READ_BACK_RELEASE_VISIBILITY_S = 390
V1 I1/I2 bindings carry: commentary_ready_queue_url=0 analysis_ready_queue_url=0 (expect 0 and 0)
V1 S5 running process environment names IRPT_ANALYSIS_READY_QUEUE_URL: 0 (expect 0; pid 864777)
V1 S5 journal since start: I3 send failures=0 unset warnings=0
```

Negative controls on that same file: `grep -c 'ROLLBACK to'` = **0**, and lines beginning `BLOCKED` or
`ERROR` = **0**. Success here is a measured absence of the failure paths, not an unread one -- the installer
rolls itself back on a failed start, and a rollback that also came up `active` would read green to anyone
only looking for the success lines.

---

## The three checks that decided something

1. **A digest that MUST change, beside one that must NOT.** An `rc=0`, a new directory on disk and an
   `active` unit are all compatible with systemd still executing the OLD root -- running-bytes-older-than-built
   passes every rung. The worker sha256 `a9f71b6d...` equals the installer's declared built member and
   **differs** from st27's `9317219a`, so the swap moved real bytes. The negative arm is the host capture
   library, `857d90b8...` before AND after: that is CORRECT, because the package's library is byte-equal to
   st27's and the install step rewrote the same bytes. A *changed* library digest would have been the finding.
2. **`producer_for` read on all three arms.** The order asks only for svc = YCHARTS. Read alone, that arm
   would look identical if the function had collapsed to one producer. svc -> YCHARTS, andrew -> OPAL,
   other -> YCHARTS: the mapping still discriminates, which is what makes the packet's claim true that only
   Andrew's own sign-in reaches the Opal producer, and therefore that S1 ships unexercised.
3. **`SENT != ran`.** `send-command` returning a CommandId proves SSM accepted the request. Both invocations
   were read separately and both show Status Success, ResponseCode 0, no stderr; each carries its own
   host-side UTC timestamps, so the reading is dated by the host, not by this box.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `comp-find "host_read" --files --limit 30` | PASS | located the `host_read.py` helper; 212 hits / 89115 files scanned, HEAD band gave the 4 candidates |
| `comp-schedule` | not run | DECLARED-NOT-APPLICABLE | the order's preflight; checked against the act as executed -- no events/rules/targets call was made |
| `comp-iam` | not run | DECLARED-NOT-APPLICABLE | the order's preflight; the two grants the act DID exercise were proved by LIVE calls, never by `simulate-principal-policy` (4 false-deny modes, 1 false-allow) |
| `comp-adversary` | graded as a control, not re-run | PASS | the issuer ran the package gate; I exercised its 294-member denominator independently via the installer's own `sha256sum -c SHA256SUMS` |
| `proof-of-spec-check.py` | on the instance | PASS (rc=0) | 3/3 criteria, 11/11 controls discriminate, 0 DID-NOT-DISCRIMINATE, rollback named |
| `deploy_ledger.py` | `open` / `close-leg` x4 / `close` | PASS | 4 legs, sentinel committed at open and removed at close |
| `surprise-row-gate` | at commit | PASS | 1 new row of 142 checked; 141 pre-existing not re-graded |
| `to-pipeline-gate` | at commit | PASS | 0 newly-added TOs; the complete-flip path graded the instance |

**What worked.** `deploy_ledger.py` committing the OPEN entry itself closes the window where a put could land
before any record of it exists. `comp-find`'s HEAD band answered a "where does this tool live" question in
one call that a recursive grep would have buried.

**What failed.** The proof instance was INVALID twice before it was VALID, both times mechanically: a
`controls` object closed with `]`, then seven enum/type mismatches (`phase: DEPLOY` is not in the enum;
`s3-object` must be `s3_object`; `DEPLOYED` must be `DEPLOYED-VERIFIED`).

**Gap found.** AC1's shape is the same defect the issuer amended out of TO-APPLY-b8's AC2 four hours earlier
(row `IRPT_YCDGEN-D2-S41`): a `grep -c` criterion with `expect: ^1$` wants a bare `1`, and the same gate
refuses `len(output_evidence) < 8` as thin. The two rules are only jointly satisfiable because the `expect`
match runs under `re.M` -- so the count can sit on its own line inside a transcript-shaped block. That is a
real escape, not a workaround, but it is undocumented and the next author will hit the same wall. **Not
filed as a row:** S41 already carries the class and the issuer has already acted on it once; what is new is
only the escape, which belongs in the checker's own docstring rather than in this project's channel.

---

## MCP traffic

4 sends/receives in the window. Significant: the respawn request from `2.0.0_SA_COO~G2` (its msg 4699, which
does not appear in this lane's delivery ledger -- the launcher carried it, not the inbox); my V1-closed report
to `2.0.0_SA_COO~G2` (985 B delivered, byte-verified); my after-the-fact host-send report to
`0.0.0_AB_MSTR~DELL2` (856 B, byte-verified). Delivery ledger at load: 17 of 17 READ, inbox empty.
Both of my sends were moved to the recipients' `read/` dirs by their watchers within seconds -- that mv is
not an agent-side ack, so I claim EMITTED for both, not READ.

---

## Surprise rows

**`IRPT_YCDGEN-D2-S47` filed** -- OBSERVATION, INERT, `disarm_owner 2.0.0_SA_COO~G2`.
`install_st30.sh:6` carries an unsubstituted placeholder `VER=__ST30_SCRIPT_VERSION__`, a leftover of st29's
by-version fetch. 1 assignment, 0 reads over the whole file, so the literal never reached an AWS argument and
it did not touch this install. The hazard is at the next derivation, and it fails loud (`Invalid version id`)
rather than silently. Not fixed here: the file is the issuer's and leg D2 is closed.

**`IRPT_YCDGEN-D2-S46` named, not re-filed** -- the package gate's whole-tree mode fails a correct map
member, so the issuer ran it in named-list mode. Its second observation (the tar's sha256 differs run to run
at the same byte length) is exactly why this order makes a different sha256 a STOP; both values measured
EQUAL to the declared pair at staging and again on the host.

---

## Blockers

**None.** Zero orders held, the ledger is closed, nothing waits on this seat.

One item is owned elsewhere and named so it is not stranded: the **audit-archive integrity** finding set
(22 findings at load, baseline `2026-08-20T042433Z` now 1253.9 h old with an uncaptured tail; this lane is
not `GOVERNANCE_AUDIT`-permitted, so the invoker deferred the snapshot). It already sits with
`0.0.0_AB_MSTR~Z` per this seat's prior session notes, so it is not re-filed.

---

## Next Steps

1. `[2.0.0_SA_COO~G2]` The S4 after-read -- the status read of the one retained 49financial research report
   (2026-10-09T12:00:29Z) -- in one served-read window, with the three reads the packet's step 4 lists. The
   row is on the host (3 firms, confirmed at V1); the read is not this order's.
2. `[2.0.0_SA_COO~G2]` Disarm or dispose of `IRPT_YCDGEN-D2-S47` by deleting or substituting
   `install_st30.sh:6` when the next release script is derived.
3. `[2.0.0_SA_COO~Y2 / TCKT_VNEXT]` S2 and S5 are exercised by TCKT_VNEXT's fourth run under that project's
   own pair: reaching READY exercises the ticket admission and the receipt; a READY whose journal shows a
   send or a send failure instead of `ANALYSIS_READY_QUEUE_UNSET` means the variable is set, and that is X1
   at once.
4. `[1.0.0_SA_CTO~DELL2]` Nothing owed by this seat. S1's reason fix and page sentence ship unexercised on
   the host by the half's own knowing acceptance; the `svc-irpt-analysis` allow-list question is already
   carried to Andrew.
