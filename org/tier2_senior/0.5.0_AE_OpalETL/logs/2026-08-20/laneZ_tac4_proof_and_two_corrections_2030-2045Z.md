# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-20 2030–2045Z

**archetype:** MIXED (VALIDATE → SCRIBE)
**Project:** D7 (TAC-4 proof instance) + two corrections I owed the record

## Summary

**TAC-4 authored and landed @6e5670fed2 — the TO-AC flip is unblocked.** The declared instance
path was ABSENT (2.0.0_SA_COO~Z measured zero over 26,798 files) and it was the last criterion
gating a workstream whose other three were done. Authored from this seat's own efforts across the
whole workstream: TAC-1 from the TO-A discovery @69f5f82004, TAC-2 from the water test, TAC-3 from
the live task, TAC-4 self-validating. Validator run **positional with rc captured unpiped**:
`rows=4, violations=0, VALID`, rc=0.

**The instance's own instrument was controlled.** A validator that cannot fail proves nothing
about the instance that passed, so I ran the same file against an expected set naming a criterion
it does not carry: rc=1, `violations=2`, *"criterion 'TAC-9' … has NO instance row (silent
omission)"*, INVALID. Recorded as M4 in the instance's `controls.mutant`, which the TAC-4 row
points at. The green is a discriminated result.

## Two corrections I owed — both are the same class, caught in opposite directions

1. **A control that does not exist was being credited.** 0.0.3_BG_BBGTerminal's readback credited
   "AE~Z's ensure_ascii doing its job" for the buzz body being pure ASCII. Exercised at source
   rather than argued: the composer performs **zero** ASCII coercion, and a fixture ticket with a
   client's smart quotes and em dash composes to a buzz carrying `0x2014 0x2019 0x201c 0x201d`;
   `json.dumps` escapes them on the wire but the server decodes them back — **transport escaping
   is not a content filter.** Today's body was ASCII because 0.4.0_DT_ClientPlatform~Z typed
   ASCII. A coincidence of today's input had been written down as a standing property, and the
   falsification would have arrived from a client typing a curly apostrophe. Retracted in full at
   BG's seat within minutes.
2. **A 200 that cannot fail.** Proving TAC-2's "link opens the board" clause, I fetched the deep
   link and got HTTP 200 — and my nonexistent-route control returned **200 as well**. The SPA
   catch-all answers 200 for any path, exactly as comp-routes' own coverage line warns ("a
   catch-all match is a DEFAULT, not a resolution"). The render clause went in as a **declared
   exclusion**, not a PASS; the gate's actually-ruled bar (the link CARRIES the param) is what the
   instance proves. The control cost one extra request and prevented a false clause.

## Andrew-direct: full serials — adopted, and my own half owned

Andrew-direct ~2036Z (received and recorded by 0.4.0_DT_ClientPlatform~Z @9e1e94c4f4): agents
refer to other agents by FULL SERIAL. My TAC-2' step-2 report went to four seats and **omitted
0.4.0_DT_ClientPlatform~Z — the one seat blocked on it**; they made the mirror error resolving a
bare "AE~Z" to the wrong live serial. Two seats, one window, opposite directions. Adopted at this
seat immediately, prose included (the half no recipient-field lint can reach). My addition to the
class, folded into the shared memory entry: **the failure is asymmetric in who can detect it** —
the sender sees DELIVERED, and the only party positioned to notice received nothing and therefore
holds no evidence.

**And I forked the memory doing it.** I wrote a new memory file for the rule without checking
first; 0.4.0_DT_ClientPlatform~Z's entry had landed seconds earlier. Two files, one rule — the
exact fork class the store contract legislated this hour ("resolution precedes creation").
Resolved: my distinct insight folded into their canonical entry, my duplicate file and its
MEMORY.md pointer deleted, one entry remains (verified by count).

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-find --name "*TO-AC*"` | 1 hit / 26,801 files — located the TO carrying the criteria + declared instance path | PASS |
| `python .tools/proof-of-spec-check.py <instance> TAC-1..TAC-4` (positional, rc unpiped) | rows=4, violations=0, VALID, rc=0 | PASS |
| Same, + TAC-9 (discrimination control) | rc=1, violations=2, names the omission, INVALID | CONTROL FIRED |
| Live AWS + gateway reads | lambda get-policy (api base), describe-table, describe-secret + real GetSecretValue (value never printed), read_channel_messages | PASS |
| Live HTTP + negative control | deep link 200 **and** nonexistent route 200 → instrument does NOT discriminate; recorded as such | CONTROL FIRED (usefully) |
| `safe-commit` + risk-reflex | @6e5670fed2 under one audited TIER0_EXEC override (the declared path is in MSTR~Z's folder — the seam 2.0.0_SA_COO~Z named); reflex CLEAN measured | PASS |

## Blockers

None I hold. TAC-2' close sits with 1.0.0_SA_CTO~Z (0.4.0_DT_ClientPlatform~Z's step 3 is theirs);
that close is the trigger for the channel-leg P1, then W-A (amendments @0968e3833f re-read: WA-9's
three at-the-table decisions, WC-2b/2c, the W-D two-audiences note). Per 2.0.0_SA_COO~Z's 2826 I
am **not** pre-encoding any terminal-state value in W-C/W-D until 1.0.0_SA_CTO~Z rules the ticket
axis — and the two WITHDRAWNs are different axes wearing one word, so the memory-side filing
commits nothing there. Runner live and clean on its cadence.
