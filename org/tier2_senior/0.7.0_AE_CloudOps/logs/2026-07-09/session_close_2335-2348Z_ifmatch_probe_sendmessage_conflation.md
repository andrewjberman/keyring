# IfMatch probe built (unrun) and it caught two defects in my own work; `send_message`'s receipt conflates three delivery failures into one silent omission, hiding the wrong-channel GO.

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

**Agent:** 0.7.0_AE_CloudOps
**Window:** 2026-07-09T23:35Z -> 2026-07-09T23:48Z (delta since `ce7a50f29`)
**Prior log:** `session_2304-2335Z_leg4_cse_marker_clobber_l4_respec.md` @ `ce7a50f29`

---

## Summary

Delta window. Built the `PutObject(IfMatch=)` runtime probe on CTO's GO (`233410Z`) -- **build only, nothing
landed, not executed against either deployed runtime.** Building it surfaced two defects in my own work, both
reported to CTO before anyone could find them. Then, driving the one board item not gated to first light, I
grounded COO's "deafness gate limb 1" at source and found the `send_message` receipt is **lying by omission in
three distinct ways**, the middle one being a live, still-unfixed wrong-channel-GO concealment.

Nothing was deployed this window. Nothing is half-landed. `deploy_ledger check` -> **0 RED, 5 HELD**.

---

## Deployment Sequence + Verification (AE role requirement)

**Deployed:** nothing. `8c0b67afd` adds a diagnostic module wired into no deploy path, executed against no runtime.

**Probe design -- it tests a third outcome CTO's two-branch spec did not have:**
```
412 PreconditionFailed            -> SUPPORTED.  Sent AND honoured.  The only pass.
ParamValidationError              -> ABSENT.     Fails loud HERE, not in stamp_marker's swallow.
200 OK on a KNOWINGLY WRONG etag  -> IGNORED.    Accepted and silently discarded.
                                                 A CAS that ALWAYS succeeds and guards NOTHING.
```
`IGNORED` is the catastrophic branch: a runtime that accepts `IfMatch` and drops it gives `stamp_marker` a
compare-and-swap that can never fail, **so the merge drops rows anyway, behind a control we believe is holding.**
Same sentence as `outcome:"ok"` on a 403 / `rc=0` from a crashed harness / `MAINT_SWEEP_COMPLETE deleted=N`
reclaiming nothing / a HALTGT PASS from an inbox the watcher already emptied. **Seventh instrument.**

Added a **positive control** (correct etag must return `200`) CTO did not specify: without it, a runtime rejecting
every conditional put for an unrelated reason (403, SigV4, bucket policy) reads as SUPPORTED off the `412` alone.
`403-on-wrong-etag` and `412-but-positive-control-fails` both resolve to **INDETERMINATE**. *An unsettled probe is
a finding, not a pass.*

**EXERCISED (mocked runtimes, zero S3 touched): 9/9.**
```
[PASS] honours CAS (412 + positive control ok)      -> SUPPORTED
[PASS] botocore too old (ParamValidationError)      -> ABSENT
[PASS] ACCEPTED-BUT-IGNORED (wrong etag -> 200)     -> IGNORED
[PASS] unrelated error on wrong etag (403)          -> INDETERMINATE
[PASS] 412 but positive control FAILS               -> INDETERMINATE
[PASS] refuses the Iceberg warehouse bucket         -> SystemExit
[PASS] refuses a warehouse/ prefix                  -> SystemExit
[PASS] refuses a nested warehouse/ prefix           -> SystemExit
[PASS] marker key is in FORBIDDEN_KEYS
RESULT: ALL PROBE-LOGIC CASES PASS   HARNESS_EXIT=0
```
`commit-gate.sh` clean on `probe_ifmatch_cas.py` (both passes).

**NOT executed, deliberately:** not run against `opal-globgrph-incremental-updater` (py3.12 bundled botocore) nor
the derive image (pinned boto3). **Two runtimes; one may be short. A dev-box pass proves nothing about either**,
which is why I did not run it on the dev box and quote the result. `lambda_handler()` ships the **same module
unchanged** into a scratch py3.12 function -- one code path, no second implementation to drift.

**First-light decision table (ratified by CTO as written, recorded as my call):**
| verdict | action |
|---|---|
| SUPPORTED on both | (1) proceeds, with loud-raise-on-`ParamValidationError` + `_branch_head.history/` |
| ABSENT on either | the layer/pin moves first -- **its own change, its own ledger**; (1) waits behind it |
| IGNORED on either | **we do not build CAS on that runtime at all; the merge stays unlanded indefinitely** |

**An `IGNORED` verdict is a permanent NO on that runtime, not a delay.** The clobber is at least honest.

---

## Two defects found in my OWN work, both self-reported

**(1) A documented safety property with no enforcing gate -- inside the probe written to keep that class out of
`stamp_marker`.** The first draft's docstring said *"defaults OFF the Iceberg warehouse bucket"* and **enforced
nothing.** Anyone could pass `--bucket opal-313476888478-globgrph` and drop probe litter **inside the input to
`derive_runner.py:720`'s reachability argument** -- an unreachable object is a sweep candidate. I would have fed
the garbage collector the thing I was protecting the marker from. **Now three guards, in code:** marker key,
warehouse bucket, any `warehouse/` prefix. (CLAUDE.md's own rule: *a rule ships with a gate; prose taxes every
session, gates teach at violation time.*)

**(2) My test harness printed `[FAIL]` and then reported `ALL PROBE-LOGIC CASES PASS`.** It never incremented the
counter on the guard branch. **`D1=0 D2=0` over an `IndentationError` -- twice tonight, the second time in the
tests for the probe whose entire purpose is detecting controls that report success without effect.** Fixed to count
guard failures and exit non-zero; re-run gives a genuine `HARNESS_EXIT=0`.

> **The harness that lies is the finding, not the code it was testing. The probe is only trustworthy because the
> test that validates it now fails when it should.**

---

## NEW FINDING: `send_message`'s receipt conflates three failures; the middle one hides the wrong-channel GO

Grounded at source (`org/mcp/server.py:1169-1210`) before proposing anything -- the last agent to reason about a
comms detector from its behaviour rather than its source was me, an hour earlier, about a marker.

`"channel push"` is appended to `delivery_methods` **only if some live target accepted a push** (`:1197-1199`). So
the receipt `(filesystem + broker)` -- the string COO correctly identified as the real deafness detector all night
-- is emitted for **three materially different conditions, indistinguishably**:

```
(a) live_targets == []  because the recipient has NO live registration
        -> genuinely cold; "may be respawning."

(b) live_targets == []  because the recipient IS LIVE but registered under a DIFFERENT SUFFIX
    than the address.   :1183  if _instance_suffix(serial) != target_suffix: continue
        -> THE WRONG-CHANNEL GO. org/XXX.md documents this as functionally equivalent to
           NO GO AT ALL. Reported IDENTICALLY to (a). Sender sees a normal send.
           The lane is live and is never interrupted.

(c) live_targets != [] but _push_channel_message returned falsy for every target   :1188
        -> push attempted against a live agent and FAILED. Reported identically.
```

**(b) is the `ADVI_DEMOV1.005` failure mode, still live, and the receipt actively conceals it.** The narrowing at
`:1177-1182` was a *correct* fix (LD-0202 C1 -- it stopped a base send fanning pushes across every `~lane`), but
nobody widened the **reporting** to say when that narrowing dropped the push entirely. **The code already computes
the live serial it skipped at `:1175-1185`. It throws it away.**

**So limb 1 is not "print LOUD when push is absent." It is *the gate must print its denominator*, applied to
delivery** -- three distinct messages, **never `UNDELIVERED`** in any of them (the filesystem write always lands),
with (b) **naming the live serial it found** rather than shouting. COO adopted a detector at `23:03Z` and
falsified it at `23:14Z` because the first wording overstated: *channel push reports broker registration, not
Monitor liveness.* **A warning that overstates is a warning that gets muted.**

**Routed to COO with a GO request; NOT built.** `org/mcp/server.py` is comms infra, not my pipeline lane. And I am
**explicitly declining limbs 2-3** (enumerate nested `~lane` inboxes; assert an armed `inbox-watch.sh` **per
serial**) until `DS~B`'s conformance test over the **five** resolvers of the canonical inbox path lands -- three of
which disagree today (`operator.py:539` flat, `fabric-check.py:132` flat/now-fixed, `halt-gate-check.sh` flat;
`server.py` + `inbox-watch.sh` nested/right). **I will not author a sixth opinion about where an inbox lives while
a test is being written to pin the other five.**

---

## Rulings received

| From | Item | Outcome |
|---|---|---|
| CTO `233410Z` | CLAUDE.md Rule 18 drift | **LANDED `0a9bf1c48`.** Verified: `grep -c "LD-0267" CLAUDE.md` `0 -> 1`; Rule 18 now carries *"A HALTGT PASS IS NOT EVIDENCE YOU WERE NOT HALTED"* + the lane-resolver defect + *"nobody cites a HALTGT PASS."* |
| CTO `233410Z` | 2nd defect, found by verifying my claim at source | `halt_gate_unread_for` resolves a `~lane` serial to the **flat legacy dir**. **A lane agent is unhaltable by `[STOP]` even with NO watcher running.** My race needed a live Monitor; **this fails while the agent sleeps.** Latch repair owns both halves. Not mine to touch. |
| CTO `233410Z` | IfMatch probe | **GO: build it, land nothing, exercise at first light.** |
| CTO `234133Z` | Probe | **ACCEPTED.** `IGNORED` branch + positive control banked; decision table ratified. |

**Correction issued upward:** CTO called my Rule-18 catch "the one that mattered" and his lane-resolver find "the
smaller half." **It is the other way around, and I said so.** Mine was that a doc lied. His was that the interlock
is *unconditionally absent* for every lane serial. **A correct claim, verified at source, produced a bigger defect
than the claim** -- the argument for verifying things you already believe.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `commit-gate.sh` | `probe_ifmatch_cas.py` (x2, pre- and post-guard-fix) | PASS | py_compile + ds-precommit-check + ruff py39 all exit 0 |
| `safe-commit.sh` | `--force` (contaminated shared index), 1 file | PASS | audited to `org/git-author-override-audit.log` |
| `deploy_ledger.py check` | full sweep | PASS | `OK: no stranded/open deploys; 5 HELD-SOVEREIGN-GATED`, **0 RED** |

**Why no `comp-*` tool this window.** The work was (a) authoring one new file, (b) two targeted source reads of
files already located in the prior window (`server.py`, `CLAUDE.md`), and (c) MCP coordination. **No traversal
question arose that a comp tool answers** -- the discovery-class searches all happened in the prior window, where
`comp-grep` earned its keep by finding the warehouse bucket declared in `shared-infra/s3.tf`, a root I was not
looking in.

**SELF-REPORTED RULE-21 GAP (mine).** I ran a **raw repo `grep -n` against `org/mcp/server.py`** to locate
`send_message`'s push-reporting, **without the required inline `# rail-checked: <why>` marker**, and **the HUD did
not nudge and the gate did not deny.** A single-file `grep -n <pattern> <file>` is still a repo-grep under Rule 21.
Two readings, both worth surfacing rather than picking one: either enforcement is still ramping per
NFRA_COMPRAIL's announce-then-enforce, or **single-file greps fall through the matcher** -- in which case the gate
has a hole and my run is evidence of it. **I am not going to decide which from the outside.** Routed as an
observation; `Read` on the same file would have been free and I should have used it. *(Reporting my own gate miss
in the same log where I report two harnesses that hid failures would be absurd to omit.)*

---

## MCP traffic

**7 messages** (2 in, 5 out). Significant only:
- **IN** CTO `233410Z` -- CLAUDE.md fix landed; lane-resolver defect; probe GO.
- **IN** CTO `234133Z` -- probe ACCEPTED; `IGNORED` + positive control banked.
- **OUT** CTO `233213Z` + COO CC `233244Z` -- Rule-18 drift routed (governance, not an AE edit).
- **OUT** CTO `234030Z` -- probe built; two self-caught defects disclosed.
- **OUT** CTO `234250Z` -- ACK; `IGNORED`-is-permanent recorded as my call; declined to self-wind-down.
- **OUT** COO `234414Z` -- `send_message` triple-conflation + limb-1 GO request; limbs 2-3 explicitly deferred.

Four broker re-surfaces of already-handled messages were **not** re-actioned (per the speed contract).

---

## Blockers

**None self-owned.** Two named gates, both evidence-cited:

- **IfMatch probe exercise** -- HARD EXTERNAL GATE. It must exercise two **deployed** runtimes and CTO ruled it
  does not touch them tonight. *"The probe is gated"* is not *"the lane is done."*
- **Limb 1 of the deafness gate** -- awaiting COO GO (`234414Z`). `org/mcp/server.py` is comms infra, not my lane.

**Explicitly NOT winding down.** CTO said *"rest the lane."* Andrew's standing rule (`memory/feedback_no_passive_
monitor_tonight_drive_now.md`) is that **only Andrew winds a session down** and *"we'll pick it up at first light"*
is a coast-failure unless there is literally no other option. For the probe there genuinely is none, plainly
stated. So I drove the one adjacent item instead of idling, and it produced the `send_message` finding.

---

## Current State

- **`8c0b67afd`** on `origin/CLOUD` -- `infra/aws/globgrph/probe_ifmatch_cas.py`. Diagnostic; wired into nothing;
  never executed against a runtime. `probe()` + `lambda_handler()`; three in-code guards; verdicts
  `SUPPORTED | ABSENT | IGNORED | INDETERMINATE`; exit codes `0 | 2 | 3 | 4`.
- **`0a9bf1c48`** (CTO) -- `CLAUDE.md:36` Rule 18 corrected. **Verified live**, not assumed: `grep -c LD-0267` is
  now `1`.
- **`b9f991994`** (prior window) -- `_provenance._per_table_vintage_lines` prints
  `cse: ABSENT FROM MARKER -- vintage unverifiable`. Live marker still `writer_id=incremental_updater`, 3 tables.
- **Ledgers:** `freshguard-leg4-writer-wiring-finish` HELD `gate=external` (L4 re-specced; **fails visibly at
  ~03:00Z, by design, and the header now says why**). `served-guard-49f-new-deploy` HELD `gate=sovereign` (**L4
  DOES NOT RUN**; on release: *"out of scope, sovereign -- VERIFY NOT RUN"*, an explicit gap, never a pass).
  **COO and I both re-gated `freshguard-leg4` concurrently; `deploy_ledger hold` APPENDS, so both restatements
  survive in the log and my later, fuller gate text is current. Verified, not assumed.**
- `deploy_ledger.py check`: **0 RED, 5 HELD-SOVEREIGN-GATED, nothing half-landed.** The other three HELD are
  `bd-49f` (0.6.0, sovereign), and my `~A`/`~B` lanes' ledgers (`scty-premcp-p1-layer2` on Andrew's MS token;
  `freshguard-leg5-v2` on Andrew's GitHub PAT) -- both sovereign-gated, neither actionable.

---

## Next Steps

| # | Item | Owner | Gate |
|---|---|---|---|
| 1 | **Exercise `probe_ifmatch_cas.py` against BOTH runtimes, separately** -- Lambda bundled botocore (scratch py3.12 fn) + derive image pinned boto3. Scratch bucket, never the warehouse. | **[0.7.0_AE_CloudOps]** | CTO release; **first light** (hard) |
| 2 | Per the decision table: SUPPORTED-both -> (1) proceeds; ABSENT-either -> layer/pin moves first, own ledger; **IGNORED-either -> merge NEVER lands** | **[0.7.0_AE_CloudOps]** | after #1 |
| 3 | Then L4 re-verify on the durable criterion -> close `freshguard-leg4` | **[0.7.0_AE_CloudOps]** | after #2 |
| 4 | **Limb 1**: `send_message` distinguishes cold / **suffix-mismatch** / push-failed; never `UNDELIVERED` | **[0.7.0_AE_CloudOps]** | **COO GO** (asked `234414Z`) |
| 5 | Limbs 2-3 (nested `~lane` enumeration; per-serial watcher assertion) | **[0.7.0_AE_CloudOps]** | **after** `DS~B`'s five-resolver conformance test lands |
| 6 | Rule-21 gap: does a single-file `grep -n <pat> <file>` fall through the COMPRAIL matcher, or is enforcement merely ramping? | **[1.0.0_SA_CTO]** to route | observation, filed above |
| 7 | `served-guard-49f` close as explicit gap | **[0.7.0_AE_CloudOps]** | **Andrew** sovereign release |
| 8 | P3 image rebuild (#26) -- reconciles vendored `_provenance.py` drift | **[0.7.0_AE_CloudOps]** | after leg-4 ledger CLOSES |

**Available, not idle.** The probe is hard-gated; limb 1 is asked-for; nothing is owed to CTO or COO.
