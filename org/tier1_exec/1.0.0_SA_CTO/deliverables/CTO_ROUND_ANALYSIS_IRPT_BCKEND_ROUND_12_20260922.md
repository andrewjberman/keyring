# CTO ROUND ANALYSIS -- IRPT_BCKEND round 12 -- 2026-09-22 ~06:5xZ

**Input:** `3.0.0_SA_CVO~B`'s L10 slug `surprise-channel/remediations/REMEDIATION_v6.md` @`5a9a7eed81`.
- L9 is `ADJUDICATION_v9.md` (C-S178..C-S187).
- The reproducer is `IRPT_BCKEND_R12_CAPTURE_FAILURE_DIAGNOSTIC.cjs`.

This is the second of the three L10 acts. Round 13 is cut by `2.0.0_SA_COO~B` in ONE issuance.

## Coverage read -- round 12 closes; no PRD addendum

**The round is terminal.** 0 of 96 orders are open and 0 of 342 items are undispositioned.

**R112-AC3 FAILs on limb (iii).** The repair itself was not missing. The two findings:
- **C-S170 and C-S171 are genuinely fixed** on the published bytes (blob `82abe684`, sha256 `b6f75a20`). I read those bytes back from S3 myself at tick 30.
- **C-S179 (ARMED) is the decisive new counterexample.** `capture-session.cjs:404` classifies a retryable timeout by matching `/timeout/i` against the error MESSAGE text. A non-timeout error, such as a certificate failure, therefore becomes retryable whenever the word "timeout" appears anywhere in the message. One example is a same-origin URL or query containing `timeout=1`. This violates the round-11 retry taxonomy (c). `3.0.0_SA_CVO~B` states it is a mock counterexample, not an observed live TLS event. It is still a real classification bug and cheap to fix.
- **C-S180 (INERT).** When the post-rename recheck fires and `unlink` fails (EPERM), the file stays on disk while stderr claims it was deleted. It is not reachable in normal operation and was not used to fail the grade. The report is still untruthful, so it must be fixed.

**Outcomes.** FWD-2 and FWD-11 remain NOT_REALIZED. No PRD addendum is needed.

## Round 13 -- ONE issuance

### 1. Capture helper, fifth repair (C-S179, C-S180; C-S153/C-S127 remain armed until it passes)

**(a) Classify errors by TYPE, never by message text.**
- A timeout is recognised only as `error.name === 'TimeoutError'`, i.e. Playwright's `errors.TimeoutError`, or as the tool's own deadline firing.
- A 5xx is the response status. A missing marker is the tool's own readiness result.
- Everything else is terminal, including any `net::ERR_*` navigation error, and prints its cause.
- No regular expression over free text decides whether to retry.

**(b) Report cleanup failure truthfully.** If the latch fires after the rename and deleting the file fails:
- print `ERROR: session file could NOT be removed: <path> (<errno>) -- delete it manually before any use`;
- exit with a distinct non-zero code;
- the README names that code and the manual step.

The contract is a truthful report plus a bounded residual state. It is not a claim of infallible I/O.

**(c) Acceptance.**
- `3.0.0_SA_CVO~B`'s R12, R11, R10, R9 and R8 diagnostics run unmodified.
- R12's `ERR_CERT_AUTHORITY_INVALID` with `timeout=1` in the message must now be terminal.
- R12's actual-timeout positive must still recover, and its HTTP 404 control must stay terminal.
- A single-difference pair each for (a) and (b), each with a positive control.

**(d) Delivery.** A new packet and both halves. The README hash is updated in the publish act. No host start. No MFA automation.

**(e) THE BAR, stated finitely** (this seat's criterion prerogative, prospectively). The R112 successor grade is the conjunction of these FOUR invariants:
1. No bytes on disk unless the latch is clear after the in-memory capture.
2. Only main-frame navigation to a foreign origin latches.
3. Retry only on the three TYPED causes.
4. Every failure is truthfully reported.

A future counterexample FAILs the grade if it defeats one of those four. One that defeats none opens a row and does not by itself hold the capture. The JUDGMENT grade remains `3.0.0_SA_CVO~B`'s.

### 2. Metadata (no publish replay)

**C-S174.** Correct the `controls.mutant.observed` text so the evidence is described accurately:
- `fffef738` was the worker's original CRLF/checkout-grain value.
- `f03666ef` is the git-object sha256.
- Neither should be called a "packet-only typo" if the JSON and the result say otherwise.

**C-S187.** Re-pin the result to the post-publish HEAD, and scope the "no real S3" exclusion to the pass it applies to.

### 3. S117 and worker hygiene -- ruling

This seat concurs with the slug. **Before a worker tree is removed:**
- the worker's final report is required;
- termination is confirmed;
- dirty work is reconciled.

A commit is not end-of-turn. `2.0.0_SA_COO~B` owns this for every drain.

## Carried

- The capture ask is HELD at `0.0.0_AB_MSTR` until the R112 successor reads PASS and the S3 readback of the new packet matches.
- rti-6 stays PARKED.
- W10-S2 is parked.
- External items are unchanged.
- 168 older rows: no bulk close.

**PUSH STATE:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
