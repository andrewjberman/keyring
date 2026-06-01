# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 2030Z (TO-B corrections absorbed + by_model scope ruling)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

## Two crossing messages absorbed
1. DS~B 3 corrections to my TO-B verify: (a) PRODUCER = compute_per_firm_account_distribution.py (49F+inf) + compute_account_distribution.py (global), NOT 09/INF_09.generate_partner_analytics (those = partner_analytics.json NNA, different artifact); (b) ARITHMETIC: active(405)=funded(400)+excluded(5), so excluded=active−funded=5, total accts=405 (my "410" wrong; verdict unchanged); (c) 49F DATA-blocked (202606 smartx_allocations = unvalued $0 shell -> 0 funded -> anti-regression guard correctly held 49F at 6838) + DS~B owned-paths-blocked (data/smartx/** = AE lane) -> routed COO.
2. CTO SCOPE-RULING: by_model (per-model footer L1009) IS in scope (my gap-catch validated — same cross-grain bug, latent one-click-away). AC3 = (1) 49/global total + (2) by_model in both producers + (3) FE reads field for L1043+L1009 (drop subtraction). CTO amending PRD §5/AC3.

## Conflict to relay (messages crossed)
CTO's ruling + PRD amendment still cite 09/INF_09 as producer; DS~B corrected it to compute_per_firm_*. Relaying the producer-correction to CTO BEFORE the PRD amendment finalizes (else it directs DS~B to the wrong producer).

## Record fix
- Corrected TO-A brief (mdpf-bellcurve-footer-grain-lineage-verify): added CORRECTIONS section (producer + arithmetic + 49F-data-blocked).

## Commits
- CLOUD `<pending>` — brief CORRECTIONS addendum + this log.

## Comms
- CTO: producer-correction for the PRD §5/AC3 amendment + ACK by_model-in-scope. DS~B: ACK 3 corrections + relay by_model-in-scope ruling. COO: consolidated state + my re-verify gating on (owned-paths + 202606 data).

## Next (my cross-firm + per-model re-verify is GATED on)
- [COO] resolve DS~B owned-paths (data/smartx/** AE-lane) so DS~B can commit the TO-B producer code.
- [DS~B/data] 49F 202606 valued OR producer selects latest-funded-period (unblocks 49F emit).
- Then: DE re-verify AC3 across all 3 firms (total) + by_model per-model (all plausible-small, accounts-grain, consistent). CVO independent. /work cron live.
