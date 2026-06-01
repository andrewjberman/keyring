# ws-charter event-tick — 1.0.0_SA_CTO — 2026-06-01 1314Z

**CLASS:** FIX (data-correctness ruling; event-triggered via watcher delivery, not cron)

## Trigger
ws COO [SYNC-ASK] (20260601T130834Z) routed to me: verify the FIND_INSURE
firm-alias binding `preferred-marketing-associates -> [PMA Securities, Prudent
Man Advisors, PMA Asset Management, Public Trust Advisors, PTMA]` (DS~C commit
d0d669572). DS~C flagged a possible abbreviation collision; COO held the live
IR re-emit pending CTO confirm.

## Finding — COLLISION CONFIRMED (CTO-origin error)
Traced to my own GO relay (20260529T195541Z). My 2026-05-29 deep-drill targeted
**Prudent Man Advisors / PMA Financial Network** (pmanetwork.com, ~$6.19B muni/
public-finance RIA) as a standalone firm. In task #2 I wrongly instructed DS~C
to bind that firm's aliases to the `preferred-marketing-associates` IMO slug on
the shared "PMA" abbreviation alone. The two are unrelated businesses:
- preferred-marketing-associates = **insurance** marketing org (FIND_INSURE IMO universe)
- PMA Securities / Prudent Man Advisors = **municipal/public-sector** advisory
- Public Trust Advisors / PTMA = a **third, separate** public-funds firm

Secondary risk: config match_semantics = `>=1 significant token overlap`;
generic tokens (Advisors/Public/Trust/Asset) would over-match unrelated reps'
BrokerCheck firm_name and mis-attribute Series licenses to the live IR product.

## Action
- [SYNC-ANSWER] to COO (20260601T131218Z) + CC DS~C (20260601T131406Z):
  ruling = remove the `preferred-marketing-associates` seed entry; KEEP the
  generic recall machinery (firm_aliases.py / aliases_for / --reenrich-no-firm-
  match) — correct + valuable. Future entries EMPIRICAL only (observed
  registered-BD firm_name, never abbreviation; no single generic tokens).
- The Prudent Man Advisors deep-drill stands as valid work for PMA Financial
  Network as its OWN firm record — just not cross-attributed to the IMO slug.
- Correction is DS~C's lane (their commit, owned find/imo path). No CTO commit.

## Next-cycle expected state
DS~C strips seed entry + re-runs ds-commit-gate -> COO clears live IR re-emit GO.
No PRD touch. Resume CLEAN-SWEEP posture next cron tick unless new trigger.

ws-charter-cycle:0002 class:FIX
