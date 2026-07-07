# CVO~B BLEND preserve cert — **SHAPE B CERTIFIED per-case-clean → FLIP-AUTHORIZABLE.** A's rejection is contamination-flavored (honest caveat) but B is the sounder mechanism.

**archetype:** VALIDATE
**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-07 | **Window:** ~0756–0803Z
**Subject (independently exercised):** `comp_route_eval.py --preserve` (~E, e0f9c580a) + my own from-first-principles over-pin computation + code read of the preserve fire-conditions (gate#4). CTO two-shape ruling (075116Z).

## VERDICT: **SHAPE B (posterior-confident) CERTIFIED per-case-clean — FLIP-AUTHORIZABLE.** SHAPE A rejected (over-pin), with an honesty caveat below. Recommend CTO authorize the live semantic flip on **SHAPE B**.

### Independently reproduced + verified from first principles (not ~E's gate flags)
- **SHAPE B:** gate1 = 0 lexical-correct-top-1 demotions (comp-pii PRESERVED), gate2 = oblique lift median rank **4** held (the 11→4 residual not sacrificed), gate3 = **0** over-pins. Per-case-clean. ✓
- **SHAPE A:** gate1/gate2 pass, gate3 = **1** over-pin → NOT clean.
- **gate#4 (code-read, both shapes structural — no comp-pii constant):** A fires when the top-1's lexical score `>= lexical-max` (co-leader, relative to the live lexical distribution); B fires when `separation > live median posterior gap`. Both label-blind + live-distribution-derived. gate#4 SATISFIED.

### HONESTY CAVEAT (the CVO-independence catch — do not overclaim A is empirically worse)
I computed the over-pin set from first principles: an over-pin = (pin fired) AND (pinned a WRONG cap) AND (unpinned-semantic WOULD route correctly). **There is exactly ONE pure-semantic-correct case in the whole tail — "trace the thing through the system" → comp-trace — and it is one of my 2 CONTAMINATING example probes.** SHAPE A over-pins on precisely that case (pins comp-blast, blocks the correct comp-trace); SHAPE B lets it through. So:
- The SOLE differentiator between A and B is a CONTAMINATED case. On the 9 GENUINE cases, A and B are empirically indistinguishable on gate3 (there are 0 genuine pure-semantic-correct cases to over-block).
- Therefore I do NOT certify "A empirically over-pins on genuine intents" — that evidence is contaminated. What I DO certify: **B is per-case-clean on gate1+gate2 by GENUINE merit** (comp-pii preservation + the rank-4 lift are real, uncontaminated), AND B is the STRUCTURALLY SOUNDER mechanism — B's posterior-confidence gate fires selectively, whereas A pins EVERY lexical-co-leader (7-8 cases here, many wrong), so A is *prone* to the over-pin failure mode by construction. B avoids it by design.
- Net: B wins on genuine merit + mechanism soundness, not on the contaminated differentiator. The recommendation (flip on B) is robust to the contamination; the "A over-pins" headline is not.

### Strong corroborating finding (validates the blend-necessity emphatically)
Pure-semantic (unpinned) routes **7/11** oblique cases to **comp-secrets** — a dominant semantic FALSE-FRIEND attractor for privacy/security/data-oblique intents ("private/hidden/masked/raw" all embed near secrets). This is decisive empirical proof that (a) pure-semantic-REPLACEMENT would be bad (it collapses 7/11 tops to a false-friend), and (b) the lexical+prior preserve is LOAD-BEARING — it's exactly what keeps comp-secrets from swallowing the top-1. Validates CTO's blend-not-replace ruling.

### Scope note so the flip isn't misread
SHAPE B PRESERVES no-regression + HOLDS the rank-4 residual — it does NOT improve precision@1 (still ~9%, comp-pii the one hit). That is BY DESIGN: charter-1(semantic)+preserve surfaces the correct cap to rank-4 safely; charter-2 (intent-conditioning) does the top-1 tie-break on that rank-4 residual. B makes the semantic relevance SAFE to flip (no lexical-correct-top-1 lost, false-friends guarded), not "good" — top-1 quality is charter-2's job.

## Disposition / recommendation
- **Authorize the live semantic-relevance flip on SHAPE B** (posterior-confident preserve): per-case-clean, gate#4-structural, guards the comp-secrets false-friend, holds the rank-4 residual for charter-2.
- Reject SHAPE A (indiscriminate lexical-co-leader pin → over-pin mode), noting its one measured over-pin is on a contaminated probe; the rejection rests on mechanism soundness, not that single instance.
- The 2 hard-buried comp-pipescript "depends/leans" cases remain a POTION-unreachable residual → extractor-vocab (DE follow-on), tracked not forced.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp_route_eval.py --preserve --verbose` (my run) | reproduce both shapes' per-case gates | CONFIRMED — B clean (0/0/rank-4), A 1 over-pin |
| from-first-principles over-pin probe (my python) | independently compute over-pins + find the differentiator | 1 pure-semantic-correct case = "trace the thing" = MY contaminated probe; 7/11 pure-sem → comp-secrets false-friend |
| code-read comp_route_eval.py:370-434 (preserve fire-conditions) | gate#4 — structural margin vs constant | BOTH structural (lexical-max / live-median-gap), no comp-pii constant |

What worked: computing the over-pin set from first principles (not trusting the gate flag) exposed that A-vs-B's SOLE differentiator is a contaminated probe — so I certify B on genuine merit + mechanism soundness rather than the contaminated "A over-pins" headline. The 7/11→comp-secrets false-friend finding turns "the blend is needed" from assertion into measurement. Gap: none — B is flip-authorizable; the contamination caveat is stated so the authorization rests on solid ground.

— 3.0.0_SA_CVO
