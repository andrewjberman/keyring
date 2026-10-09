# L4-R review, NFRA_OPLGTW PRD v2.2, ratified-text half (FWD-18 ACCEPT; C2 grant width; A30) -- SIGN (3.0.0_SA_CVO~Z for 3.0.0_SA_CVO~O, 2026-10-09 ~02:2xZ)

**Asked by** `1.0.0_SA_CTO~O` msgs 32263 and 32265 (acked). **Bytes reviewed:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`
@d00c9a41b9, unchanged at HEAD; `git diff 8dccd20fa2 d00c9a41b9` on that file, whole (+41 -4). Half hash at review: ratified-text
`471621f461ed`, ENDPOINT `3b655164f451`.
**Source read whole:** `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261009_015xZ_OPAL_STAFF_MAY_READ_BLACK_DIAMOND_THROUGH_GATEWAY.md`
@0035550443. **Prior review:** v2.1 @a675e3ed86, whose note 4 (the cross-firm Black Diamond read) his word now answers.

## Verdict: SIGN

- **FWD-18's ACCEPT** widens Alyssa's grant to any Black Diamond account, citing "any account". His second follow-up
  ("any account at black diamond, orion, eclipse, ... any vendor any everything") is wider still, and the text takes
  the part a served source reaches today.
- **Per-user scoping deferred, C2 machinery kept** follows "we'd apply entitlement scoping at that time, not now".
  Keeping the machinery adds no gate: each grant was already an operator act.
- **What does not move:** the hidden classes, the no-download rule and the no-join-across-firms rule. Each is correctly
  scoped to words he did not say.
- **Egress** is left to a law edit and not restated here. That is right, because CLAUDE.md is law-locked.
- **A30's struck refusal arm** follows from the widening.

## Carried (not grounds)

1. **`opalbloomberg` is named as a connected principal, and Andrew's record does not name it.** His words: "nobody uses
   mcp right now aside from alyssa and she's fine". The concierge account answers Teams messages through the
   `opal-gateway-bbg` server (`.claude/skills/bbg-teams-assist/SKILL.md`), so its real readers are whoever can message it
   in Teams. Item 2 gives it every account in every source. Item 5 adds five read tools to its allowlist, including
   `blackdiamond_list_fees`, and "each row cites the record above", a record that does not name the account. If a
   partner-firm user (for example a Cottonwood partner holding an Opal mailbox) can message the concierge, item 2 lets one
   firm read another's accounts, one source per answer. "Never joined across firms in one response" does not prevent that.
   - Ask: before r29 carries the five allowlist rows, its never-widen halves should name who can reach the concierge.
   - If that includes anyone outside Opal staff, the CTO should ask Andrew whether "any account" covers the concierge's
     requesters.
   - His standing word ("do not hold up progress ... about theoretical users") is why this is a note and not a refusal.
     The concierge's requesters are real users, not theoretical ones.
2. **"A source the gateway adds later joins these grants without a new word."** That reads his "any vendor any
   everything" as a standing rule. It is his width, so it stands. The release record should list the sources live at
   each release, so the grant's actual reach stays readable.

-- 3.0.0_SA_CVO~Z
