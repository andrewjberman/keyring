# The globgrph derive caller stops presenting a permanent bearer, and the fallback is what makes that safe — 0.8.0_AE_CloudComp~W

**Date:** 2026-09-10
**Task Order:** ad-hoc — NFRA_OPSEC202609 caller-migration ask (globgrph NFRA_MSGRAPH derive), no TO cut; seated by `0.0.0_AB_MSTR~Z`
**Status:** COMPLETE (code); deploy ROUTED and gated

---

## Objective

Msg 20780 from `2.0.0_SA_COO~Z` recorded that the globgrph NFRA_MSGRAPH derive caller presents a
static 32-byte bearer with no `exp` on `/ms/*`, from a single-slot secret that has never rotated,
while a `/ms/token` exchange is now live. It requested nothing and set no date — the decision was
this lane's alone. The objective was to decide, and then to actually land the decision rather than
report on it.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find 'ms-ingest-token\|MS_INGEST_BEARER\|/ms/site_children\|/ms/health' --limit 60` | PARTIAL | Correct hits, but a full-repo sweep exceeded 120s and had to be backgrounded; native `Grep` answered the same question in ~2s. |
| comp-find | `comp-find --name 'NFRA_OPSEC202609*'` | FAIL | Gated by its own HUD when piped to `sed` (census-into-receiver rule), so it never ran; a plain `ls -d` glob found the project dir immediately. |
| comp-pipescript io | `comp-pipescript io infra/aws/globgrph/ms_cloud_extract.py` | WARN | Correct and honest: OUT-OF-GRAPH, "DENOMINATOR: 0 recognized I/O call site(s)" with an explicit note that a measured zero is not a claim of inertness. |
| owned-paths-validate | `--check-agent 0.8.0_AE_CloudComp~W` | PASS | rc=0 on both target paths; rc=1 + VIOLATION on a foreign path, so the instrument was shown to discriminate before it was trusted. |
| to-check | `to-check.py --all --assignee 0.8.0_AE_CloudComp~W` | PASS | `total=0 ... scanned=2377`. |

**What worked:** `owned-paths-validate` with a negative control settled write authority in one call.
`comp-pipescript io` printing its own denominator and disclaiming it is the behavior that stopped me
reading a zero as "no I/O".

**What failed:** Nothing returned a wrong answer. Two `comp-find` invocations cost more time than the
native tool they exist to replace — one on latency, one on its own HUD gate.

**Gap found:** `comp-pipescript io`'s recognizer set has no HTTP limb. This module's entire I/O
surface is `httpx` calls to the gateway, and the manifest reads `READS (0) / WRITES (0)`. The tool
says so plainly, so this is a coverage gap and not a defect — but for a container that talks only
HTTP, the I/O manifest is structurally empty and cannot become non-empty.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Ground the finding at HEAD, not at its cited vintage | Cited `@97b8103069`; measured `otp.py` +56/-12 and `ms_ingest.py` +50/-10 vs HEAD. Substance holds, line anchors stale. |
| 2 | Read the exchange contract from source | `POST /ms/token` -> `{capability_token, token_type, expires_in, aud:"gw:ms"}`; `/ms/*` dual-accepts (`server.py:_ms_guard` -> `ms_ingest.authorize`). |
| 3 | Confirm the caller is live, not dark | `ms_enabled()` defaults OFF; live task-def `globgrph-derive-runner` rev 9 ACTIVE carries `GLOBGRPH_MS_ENABLED=1`. Declared and applied agree. |
| 4 | Verify `/ms/token` is really deployed | 401 `{"error":"unauthorized"}` from the app vs 302 from the ALB default on an unmatched path. |
| 5 | Isolate per Rule 14b | `git worktree add ../aecc-w-msgraph -b aecc-w-msgraph-caller-exchange` |
| 6 | Implement exchange-then-present + refresh + 401 retry + static fallback | `infra/aws/globgrph/ms_cloud_extract.py` |
| 7 | Write the acceptance artifact | `infra/aws/globgrph/tests/test_ms_cloud_caller_auth.py`, 9 tests |
| 8 | Rule 14 commit gate | "pre-commit gate clean for 2 of 2 file(s)"; 2 non-ASCII chars I introduced were removed, re-censused to 0. |
| 9 | Commit | `6eca45d986` (2 files, +385/-7), author `0.8.0_AE_CloudComp_W` |
| 10 | Drain | `.tools/safe-merge.sh` -> `f87a2eaadf` on SITEZ; worktree and branch removed |
| 11 | **Image build / ECR push / task-def revision** | **NOT DONE — routed to `0.0.0_AB_MSTR~Z`. See Blockers.** |

---

## Verification

```
=== new tests ===
9 of 9 passed

=== SAME test file against the PRE-CHANGE module @063549eb73 ===
FAIL: test_401_on_data_call_remints_and_retries_once
FAIL: test_capability_token_is_not_the_static_bearer
FAIL: test_exchange_happens_and_capability_token_is_presented
FAIL: test_persistent_401_surfaces_rather_than_looping
FAIL: test_token_is_reminted_when_it_expires_mid_run
FAIL: test_token_is_reused_before_the_refresh_margin
OK:   test_exchange_down_falls_back_to_static_and_call_succeeds
OK:   test_exchange_exception_falls_back_to_static
OK:   test_needs_login_503_still_surfaces
3 of 9 passed

=== sibling SS4 catastrophic-floor acceptance ===
OK: 13 passed, 0 failed

=== merged bytes at SITEZ HEAD ===
f87a2eaadf is in HEAD's history
MS_TOKEN_EXCHANGED markers: 1
_REFRESH_MARGIN_S:          2
NEGATIVE CONTROL - old single-header line: 0   (absent, as required)
```

The 6 tests that flip between old and new bytes are the migration markers. The 3 that pass on both
are regression guards asserting what must NOT change, and are not offered as evidence the migration
landed — the split is written into the test file's own docstring so a later reader cannot mistake a
9-of-9 for nine proofs.

---

## Decisions Made

1. **The static bearer stays as bootstrap AND fallback.** Every failure on the exchange path
   degrades to the static bearer rather than raising. Dual-accept is live and re-exercised, so this
   migration can improve attribution and by construction cannot make the derive worse than before it
   landed. A migration that hard-fails an unwatched 02:00Z nightly for an auth-plumbing reason would
   be worse than not migrating.
2. **Refresh on a monotonic deadline, not once per caller lifetime.** `CAPABILITY_TOKEN_TTL` is 300s
   while the MS extract is an unbounded paged enumeration (6172 nodes / 12307 edges on today's run),
   so one token cannot cover one run. 30s margin covers flight time plus the gateway's deliberately
   small 5s validation leeway.
3. **Exactly one 401 retry.** Enough to answer a token that died in flight or a retired dual-accept;
   not enough to spin against a gateway that 401s everything. There is a test for the second half.
4. **Stop at code; route the deploy.** Reasoning in Blockers.

---

## Files Modified

| File | Change |
|------|--------|
| `infra/aws/globgrph/ms_cloud_extract.py` | `HttpMsGatewayCaller` exchanges at `/ms/token` and presents the capability token; `_exchange`, `_auth_headers`, `_static_headers` added; `_get` gains a 401 re-mint-and-retry. |
| `infra/aws/globgrph/tests/test_ms_cloud_caller_auth.py` | New: 9 tests over a fake `httpx` injected into `sys.modules`, offline. |

Drain `f87a2eaadf`. **Push state: LOCAL** — `origin/SITEZ` read `93ab120af1` via
`git ls-remote origin refs/heads/SITEZ`; `f87a2eaadf` is not an ancestor of it.

---

## Blockers

Not blocked on anything this seat can move. The deploy is gated, and the gate is objective rather
than a judgment call:

1. **The commit is LOCAL.** Building a production image from unpushed bytes puts running bytes ahead
   of the shared record — the state that defeats every downstream currency check. The push window is
   BLOCKED-SOVEREIGN on Andrew's word per `0.0.0_AB_MSTR~Z`'s own broker summary, and shared-branch
   push is not this seat's act regardless.
2. **It is an IMAGE act**, so CLAUDE.md's NEVER block requires a change-management ledger entry
   naming every task family that pulls what it moves. None is open.
3. **The derive was exercised six times tonight** (03:0xZ–05:2xZ on the CloudWatch streams), so a
   credential-path change landing mid-exercise could confound another project's measurements.
   Sequencing, not a blocker.

Routed to `0.0.0_AB_MSTR~Z` with a recommendation, per msg 20780's own closing paragraph: an order
for this is cut in `0.8.0_AE_CloudComp`'s home, and where no issuer is live, `0.0.0_AB_MSTR~Z`
routes it. No issuer for this home was live at 05:47Z — the three live COO lanes are scoped to
NFRA_OPSEC202609, NFRA_REPORT and NFRA_IAMROLES202609.

---

## Current State

The caller code is migrated and merged on local SITEZ. Production is unchanged and will stay
unchanged until an image build plus a task-def revision — the gateway's `gw_cred_observe` artifact
will keep showing `class=capability` on a static bearer until then. That absence is expected, and
`2.0.0_SA_COO~Z` was told so directly, because the artifact reads in the wrong direction: "no
exchange traffic" would otherwise look like a failed or declined migration rather than an undeployed
one.

## Next Steps

- **[`0.0.0_AB_MSTR~Z`]** route an order for the deploy when the push window opens: image build,
  ECR push, task-def digest revision via `safe-apply`, change-management entry opened at start and
  closed at completion. This seat can execute all four on a GO.
- **[`0.8.0_AE_CloudComp~W`]** execute that order on GO; nothing else outstanding.
- **[Andrew]** nothing open at this seat.

---

## Instrument notes worth carrying

- **The derive's CloudWatch timestamps cannot measure any phase inside it.** The container flushes
  stdout at exit, so every line in a run shares one timestamp — `MS_EXTRACT_START` and
  `MS_EXTRACT_COMPLETE` both read `1789007298616`, and the entire tail of the newest run reads
  `1789009400183`. Anyone timing a phase from this log group will get zero and believe it. The
  design here was deliberately made independent of the duration rather than resting on a number this
  instrument cannot produce.
- **`to-check.py --all --assignee` prints a THIRD-POPULATION footer that is identical regardless of
  assignee.** Tailing the output makes two different queries look byte-identical and reads as "the
  filter is broken". The header carries the real answer (`total=0 ... scanned=2377`). Read the head,
  not the tail.
