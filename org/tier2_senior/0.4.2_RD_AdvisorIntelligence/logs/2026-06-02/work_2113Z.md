# work cycle — 0.4.2_RD_AdvisorIntelligence~C — 2026-06-02 ~2113Z

## ADVI_INFPRM P2 — advisors-branch isFirmAdmin guard re-add (opportunistic fold)

### Context + decision-flip
CVO + CTO both flagged: W4f incidentally reverted the advisors-branch isFirmAdmin guard along with the (correct) distribution un-guard. NOT a live leak (advisors unreachable for non-admins: nonAdminTabs hardcoded [distribution,profile] + advisors.enabled=false), but advisors is admin-only content (multi-advisor nav) -> should keep the guard as defense-in-depth (mirror Books :266).

I initially DEFERRED to post-promote (avoid re-staling the CVO-PASS'd head c009f98c). CTO then gave a sharper call: OPPORTUNISTIC fold — land it before Andrew's full-pass green (free, since Andrew's Joe smoke is the long pole), else ship-on-green + ride next deploy. Never gates GO. Andrew hadn't greened -> I took the window.

### Done (portal DEV 23982a8c)
- Re-added `&& isFirmAdmin` to the advisors render branch (inflection/index.tsx, mirror Books :266). Distribution stays un-guarded (W4f, Andrew's shared model); Books guard kept; Profile + nonAdminTabs untouched.
- Strictly additive (advisors branch only); no live behavior change (advisors unreachable for non-admins) — structural 3rd-layer backstop vs a future advisors.enabled flip / nonAdminTabs change.
- tsc -b + eslint green. ci.yml GREEN (run 26848295466, gh run watch exit 0).

### Promote impact
DEV head c009f98c -> 23982a8c. Flagged CTO (211354Z) for the head-fold decision (GO target -> 23982a8c; Andrew's Joe re-smoke surface is IDENTICAL — advisors invisible to non-admin smoke) + CVO confirm-request (211359Z, strictly-additive). Pre-stage re-warmed: 23982a8c clean+pushed+ci-GREEN, 15 ahead of PROD, rollback a33c230f unchanged.

### State
INFPRM FE: W1/W2-FE/W4b/W4c/W4f all PASS + this P2 hardening. GO gate = CTO head-choice (c009f98c vs 23982a8c) + Andrew Joe re-smoke + CVO confirm-of-this-fold. Promote warm. Nothing blocked on me.
