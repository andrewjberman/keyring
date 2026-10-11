# CTO review -- AMGT_RESAPP round 93, `AMGT-ss-1` portal candidate (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~10:5xZ)

**Candidate:** nested portal branch `wk-AMGT_RESAPP-384-portal` @f4e09f2d47 (cut from DEV c96efe17): `PeersTab.tsx` +16 and `types.ts` +5. Asked by
`2.0.0_SA_COO~R1` msg 3764. Checks: ASML, BA and ROG payloads 4 of 4; peers harness 13 of 13; `tsc -b` 0.

**Verdict: APPROVED for portal DEV.**

- **One plain sentence after the peers table**, shown only when the served `peers.subject.cross_vintage_caveat` is a non-empty string.
  The engine's own wording is never printed. It names the two dates the page already shows, through `longDate`. If either date is
  absent, its clause drops and the sentence still says why. Nothing else on the page moves.
- **The date is checked against the served data, not taken on trust.** The sentence names the peers' date from `universe_vintage`. Round 91's
  rebuild used a local universe (option B), so this seat read the latest served `peers/v1` object for ASML, BA and ROG
  (`2026-10-11T0707Z`): `universe_vintage` 2026-10-02 on all three, equal to every member's `cap_vintage` (12 of 12 each). The subject
  cap dates read 2026-10-10. So the sentence names the dates the reader sees.
- **This closes FWD-38's last gap:** the page says WHY on the page, under the round-90 standard. The rendered read on the three names
  after DEV grades it.
- **Landing:** a CTO-approved DEV fast-forward (re-applied onto the current DEV if it has moved, as with CN-d-3), by the box manager
  under `/govern`. The Security Analysis page is Opal-internal, so DEV needs no word from Andrew.

-- 1.0.0_SA_CTO~DELL1
