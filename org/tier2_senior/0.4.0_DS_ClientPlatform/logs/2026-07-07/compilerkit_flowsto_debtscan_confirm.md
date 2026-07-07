# COMPILERKIT FLOWS_TO recognizer + DEBTSCAN cleared-count confirm + CVO Orion-endpoint pointer

**archetype:** MIXED (primary: IMPLEMENT; secondary: VALIDATE, COORDINATE)
**agent:** 0.4.0_DS_ClientPlatform~A | **date:** 2026-07-07 | **window:** continuation of
compilerkit_p2_config_recognizers.md, same session (Andrew steer mid-window: "just keep driving compilerkit")

## Summary
Three threads this window, all driven to a clean state:
1. **COMPILERKIT compiler #2 FLOWS_TO recognizer** (the anchor recognizer -- field-grain lineage + the
   EdgeKind discriminator that catches the spread-bug regex can't see). Built against cse_schema 0.2,
   validated 9/9 against the REAL 961-edge live_flowsto.json. Grounding surfaced a load-bearing catch:
   50% of edges would fail-closed without a slash->underscore kind normalization.
2. **DEBTSCAN reachability cleared-count confirm to CVO** (my close-role). 0.8.0-base resumed wiring +
   found the real root cause (a lam() Lambda-name-matcher naming-drift bug, deeper than my recognizer #3),
   residual 19->14. I independently ground-confirmed the MECHANISM (source-confirmed the committed fix),
   attributed the count honestly to 0.8.0's in-session re-scan (no committed artifact), and gave CVO a
   grounding-scoped confirm rather than parroting an unreproducible number.
3. **CVO Orion assets-dim endpoint pointer** (Andrew-direct ad-hoc via CVO). Corrected a wrong premise
   (my 46 reports are gold-only, don't cover the bronze/API pull) then gave the real, cross-verified
   pointer. Andrew steer surfaced the gold-script docstrings THEMSELVES carry the API lineage -- traced
   INF_B_00 gold -> positions_mv silver -> Orion REST endpoint, a second independent confirmation.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-which (x3: config-file discovery, doc-pointer for Orion endpoint, debtscan residual scan) | routed searches per the rail | all 3 near-tie/no-fit -> fell to native Read/Grep per comp-which's own no-dead-end fallback (confirmed no tool fit each exact use before going raw) |
| comp-secrets get orion/jwt/current | ground the Orion JWT secret is LIVE (not just declared-in-source) for the CVO pointer | PASS (firm=inf, exists, ver 2be269cf) -- confirmed the SM key backing the endpoint auth |
| git show 393a8b723 (source-confirm) | ground the DEBTSCAN lam() mechanism fix independently before confirming to CVO | PASS -- the _->- + opal-prefix normalization is real + committed; mechanism is proof-grade, count is not (rests on 0.8.0 in-session scan) |
| python (direct exec) | FLOWS_TO harness vs REAL 961-edge live_flowsto.json; PyYAML compose() probe earlier | 9/9 PASS; the harness independently re-derived the source kind-distribution from the raw file (337/142/482) rather than trusting the recognizer's own count |
| .tools/ds-commit-gate.sh + safe-commit + push | FLOWS_TO recognizer commit | gate clean, committed cc983b78a, pushed |
**Worked:** grounding-against-real-output is now 3-for-3 at catching real impedance mismatches that
synthetic fixtures would have masked -- batch-1 (locus off-by-one), batch-2 (firm-collision), and now
FLOWS_TO (the "recompute/guarded" slash vs "recompute_guarded" underscore, which the validator REJECTS ->
482/961 edges = 50% would silently fail-closed). Also: verify-don't-trust applied to the DEBTSCAN confirm
-- I did NOT relay 0.8.0's residual=14 as my own proof; I source-confirmed only the mechanism and
attributed the count to their in-session scan, flagging that no durable artifact grounds it (recommended
CVO have the scorecard regenerated+committed if they want a durable count for the close record).
**Failed/caught:** a P2 test-oracle false-fail earlier (naive regex counted a comment-line s3:// doc
example); nothing broken in the FLOWS_TO recognizer itself. **Gap:** the DEBTSCAN residual count has no
committed durable artifact (0.8.0's re-scan is session-ephemeral) -- flagged to CVO, not a tool gap but a
close-record grounding gap.

## Deliverables / commits
| Commit | What |
|---|---|
| cc983b78a | FLOWS_TO recognizer + __main__ harness (9/9 vs real 961-edge output) |
| `deliverables/COMPILERKIT_recognizer_flowsto.py` | the recognizer |

## MCP traffic
~7 messages. CVO Orion-endpoint ask (answered w/ corrected premise + cross-verified pointer + a follow-up
gold->API lineage trace prompted by Andrew's steer); 0.8.0-base DEBTSCAN residual-19->14 + Blocker-2
verified (ACKed, then sent the grounding-scoped cleared-count confirm to CVO); 0.8.0~D FLOWS_TO wiring
handoff w/ the critical normalization flag. No open RAVC on me.

## Blockers
None. Open async items (none blocking): (1) ~D batch-1 MODULE-ref firm-scope alignment confirm; (2) ~D
decision on fixing extractor_full.ts:373 slash at source vs holding it at my _KIND_MAP seam; (3) CVO's
DEBTSCAN close decision (my confirm delivered, ball in their court); (4) ~D's 2 P2 FrontEnds (for me to
re-run P2 against real parsed trees). NFRA_MOTIF.P1 graph-lane slice still queued (DE gated on it, no
urgency).

## Current State
COMPILERKIT-P1 recognizer set is now COMPLETE on my authoring side: batch-1 (dispatch pair, ~D) + batch-2
(S3-key pair, mine, wired+parity-verified 115 edges) + FLOWS_TO (compiler #2 anchor, mine, 9/9 vs 961
real edges). P2 config pair (mine) also done. Everything awaiting ~D's framework wiring + the full-corpus
AC2 parity passes; no authoring work is blocked on me. cse_schema 0.2 EdgeKind is now exercised end-to-end
by a real recognizer (was the last decision-dependent stub in the SDK).

## Next Steps
- **[0.4.0_DS_ClientPlatform~A -- me]** re-run P2 config recognizers against ~D's real FrontEnd trees when
  they land; extend batch-2 S3-key recognizers to cot/inf if ~D wants that before P1 close (flagged as a
  real next-step by 0.8.0, not a P1 blocker); MOTIF.P1 graph-lane slice when COMPILERKIT reaches a pause.
- **[0.8.0_AE_CloudComp~D]** wire FLOWS_TO + run the 961/961 AC2 parity (heed the slash-normalization
  flag); confirm batch-1 MODULE-ref firm-scope alignment; decide extractor:373 fix-at-source vs my seam;
  land the 2 P2 FrontEnds.
- **[3.0.0_SA_CVO]** DEBTSCAN close decision on my grounding-scoped cleared-count confirm.
