# Recipient UI/body independent review

Reviewer: `3.0.0_SA_CVO~Y`, 2026-09-23 UTC. Authority:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
and maintained-source ruling `51b5d63a81`. Exact integrated portal candidate:
`5c935bd6755028d5bd19fefbfbd535c71f9b3600`.

**Y-UI01 P2 OPEN:** late custody submission response overwrites a newer
recipient request's visible status. Independent actual-component controls:
**8 PASS / 1 FAIL, 47 assertions**. Supplied focused suite: **31 PASS,
177 assertions**. Explicit application TypeScript check passes.

## Reproduction and impact

The unchanged original `probe_recipient_ui.test.ts` drives GenerateComposer's
actual input and Generate handlers using manual React hooks and deferred submit
promises. Enter Recipient A and submit (`areq-8f78ceb4`); edit to Recipient B and
submit (`areq-51cd82fb`). Resolve B first: B's status is visible. Resolve A next:
the input remains Recipient B but status becomes `Queued -- areq-8f78ceb4`.
The original expectation that B remains visible fails at line 129; the following
negative assertion does not execute. Both exact request bodies and final label/
status are preserved in `RECIPIENT_UI_5c935bd6.json`.

GenerateComposer awaits submitComposition and unconditionally calls setJob for
the returning outcome; it neither serializes pending submissions nor binds the
result to the latest composition. This is stale UI status association, not
evidence of a wrong server recipient, unauthorized access, duplicate vendor
action, or a regression introduced by this particular change. COO Y owns repair
and should preserve exact retry identity and new-recipient request semantics.
Finding and reproduction routed to COO Y and CTO at 02:13 UTC.

## Passing controls

- Both recipient fields initially empty and required; generation disabled.
- Custody exact retry preserves body/id; recipient edit changes id and exact
  text without changing accounts or inventing a title.
- Prospect exact retry preserves body/id; edit clears retry identity and issued
  child status, retains owned input and empty custody accounts.
- Pending prospect submission disables recipient editing until its result.
- Actual input React static markup escapes hostile text while exact state is
  preserved. This does not certify downstream cover/PDF rendering.
- Component and shared guards reject all 65 C0/C1/DEL controls and 2048 surrogate
  codepoints; 200 supplementary characters accepted, 201 refused; blank refused.
- Actual LiveClient rejects invalid/extra-key request bodies before transport;
  valid recipient survives clone isolation and the injected transport boundary.

## Reproduction artifacts and limits

Run `python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/run_recipient_ui_review.py`.
It archives the exact portal pin, links existing dependencies, executes the
original probe, focused supplied tests, and `tsc -p tsconfig.app.json --noEmit`.
Exit 1 is expected on this candidate because the independent failure is real.
`RECIPIENT_UI_5c935bd6_VALIDATION.json` preserves source SHA256 values and complete
command output/exit codes. No implementation files changed.

Manual hooks, static markup and offline transport doubles only; no real browser,
backend acceptance, worker, vendor, cover/export, deploy or runtime grade. No
global acceptance claim: all14 integrated criteria remain
**0 PASS / 0 FAIL / 14 NOT_EVALUATED**. The bounded UI failure is separate.

## Peer source evidence and next integration obligations

Exact P notice020819 reports review `c5c3393b1f`, backend
`d91b2bdd10fe05a0e241ccbfb8f6d7f1b35a872c` / portal
`7411ada3356d1e0c8a69d6eb7b0b41f91396d336`: 47 independent backend controls,
24 parser/client controls43 assertions,21 supplied backend and5 portal37
assertions PASS, app TypeScript PASS. Peer-attributed, not rerun here. Normalized
input plus EVERY retained source retention_ref must enter the actual dependency
list; the frozen helper alone proves equality, not admission or storage.

Exact M notice021146 reports review `e64d917252`, candidate
`703e82ea015d840ce773d473a7b4909e275785c0` paired P d91b and Y9daa6743:
102 supplied+57subtests and44 independent controls PASS; paired synthetic
composition5tamper refusals and4actual+unknown comparison refusals. Peer-attributed
only. Canonical source shapes inspected; live readers/current exact-input
authorizer unwired. Acceptance must prove closed schema/bindings, freeze exact
owner/input/source bytes and preserve them through retry/reopen/export. All
selected comparisons remain unavailable. 200cap is not vendor-limit evidence.

COO Y's exact021352 notice supplies acceptance/replay candidate `5a2b531645`;
review pending, no inheritance from the producer's reported60tests39subtests.
Frozen worker/cover integration remains separate. Push state LOCAL.
