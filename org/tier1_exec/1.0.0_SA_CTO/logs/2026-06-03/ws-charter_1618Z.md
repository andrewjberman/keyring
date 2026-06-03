# ws-charter — 2026-06-03 1618Z — 2 doctrine rulings (comp-validate fail-closed + closure 2-step)

**CLASS:** FIX (doctrine ruling + scribe). Triggered by COO RELAY 161218Z (3 governance items).

## (1) comp-validate NO_CONFIG — RULED (a) fail-closed + waiver + phased; scribed

Andrew-direct comp-* "absence != PASS" cleanup. Ruled to DS (161508Z), CC COO+MSTR:
- DEFAULT `NO_CONFIG` -> exit-2 (UNVALIDATED, not a pass). Invert opt-in: `--lenient` restores exit-0 (legacy `--strict` -> no-op alias).
- Explicit auditable WAIVER: config `validation: not_required` + `reason:` -> `WAIVED:` exit-0 (deliberate no-validation decision passes; true NO_CONFIG fails closed).
- KEEP COO's interim LOUD NO_CONFIG message.
- PHASED: ship waiver+message first -> inventory all live-gate NO_CONFIG ids + add config/waiver -> THEN flip default (avoids the §10.1 flip-day-blocks-new-scripts breakage). DS reports inventory before flip.
- Rejected (b) "all callers pass --strict" = cultural, not structural; matches sibling comp-* fail-closed hardening (comp-iam/blast/adapter-audit).
- SCRIBED: `docs/architecture/COMP_VALIDATE_PROTOCOL.md` §10 table (new WAIVED row + NO_CONFIG exit-2 default) + §10.1 rewrite (amendment block, phased rollout); `CLAUDE.md` comp-validate line (NO_CONFIG = UNVALIDATED, never signal SAFE).

## (2) Closure-doctrine 3-step -> 2-step — CONCUR (CVO P3, COO disp (a)); scribed

PRD `Status:` bump is NOT a close-step. `org/projects/{CODE}.json` is the single authoritative close-state. REGISTRY.md §"Closing a project" was ALREADY 2-step (canonical); `org/XXX.md` Closure Discipline had the drifted 3-step. SCRIBED org/XXX.md -> 2-step (JSON + REGISTRY) + explicit "PRDs are NOT a close-step" note + retired the "3-step atomic close" convention; "Why both" + anti-pattern updated. Kills the systemic PRD-Status-lag CVO flagged (fc642aa57).

## (3) v2.1.114 manifest — noted (2 items, HELD)

DEV-ahead of v2.1.113 (PROD 9f890e0f): `3e0ce8d0` xlsx CDN-swap (0.3.2 security) + `858bd374` ModelPortfolios Data Source panel Inflection->Orion (0.4.2 — completes 548c9d7d footnote fix that MISSED the "SmartX Connected" panel + Non-Model footnote, 3 render sites). HELD for Andrew GO + fresh smoke; no promote pressure. Lock manifest when bundle worth shipping.

**Visual-smoke note:** 858bd374 (RD-AI Andrew-LIVE-catch) is a good reinforcement of the visual-smoke-gate — 548c9d7d's source-verified footnote string was correct, but the SIBLING SmartX render sites it didn't touch were invisible to a source-grep; only a live visual pass caught them. Validates accepting CVO's localhost render-smoke for v2.1.113.

## Both doctrine amendments -> MSTR for LD-ratification (touch CLAUDE.md + org/XXX.md non-negotiables).
