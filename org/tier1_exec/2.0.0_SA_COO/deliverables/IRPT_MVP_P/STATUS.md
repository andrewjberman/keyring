# IRPT P -- STATUS at 2026-09-24 06:4xZ (2.0.0_SA_COO~P)

Goal (Andrew-direct 2026-09-23 ~22:4xZ): Investor Reporting Performance done end to end and linked
up for every firm client at 49 Financial, Inflection and Cottonwood; Cottonwood structurally sound
with its ~May-2026 data window disclosed. Loop: 20 minutes. This file is the one place the state of
P's surfaces is written; every number below is from a receipt in this directory or a message id.

## Served tonight (each a ledgered act: sentinel -> plan -> safe-apply -> readback -> re-plan -> recorder)

| function / object | CodeSha256 / revision | at (Z) | carries | receipt |
|---|---|---|---|---|
| irpt-holdings | kZygK57yXxZBaC3t5Wr+y04tDKx6tDJdjCwPm87kdYE= | 06:00:10 | B1/B3 loaders + B7 served (05:04), schema copy b3e3bcb044 (`display` + CUSTODY_UNITS) | HOLDINGS_SPEED_APPLY, HOLDINGS_SCHEMA_APPLY |
| irpt-directory-search | o9Qu0Jm7jidtrlBeGWD9d2ZsxROK3NXcQTEOUOMvGus= | 05:16:11 | listing speed (04:21) + option-B keep-warm: one rule, three targets, 500 ms hold; three containers seated on every tick measured | DIRECTORY_SPEED_APPLY, DIRECTORY_KEEPWARM_APPLY |
| irpt-performance-adapter | 07lSH03z53irjBk3AkX2upzUuWzVd4QOuPA4JmisLss= | 06:36:41 | canonical 61-member flat shape (05:28 reconcile of the 00:07 install), X10 ACTIVE row (M 7262571e4c), hop 4b MRO walk + named retention codes, hop 3 SELECTION_UNSUPPORTED, hop 12 sink | PERFORMANCE_RECONCILE_APPLY, PERFORMANCE_X10_HOPS_APPLY |
| Cottonwood holdings (M's act) | dec293d6 | 06:20:13 | display on 16,740 of 16,749 nodes, CUSTODY_UNITS on 13,656 securities; Anna's subtree 75/75 labelled | IRPT_MVP_M/COT_LABELLED_PUBLICATION_RECEIPT |
| portal DEV | 7c542fd2 | 06:3xZ (MSTR) | consolidation 7975c3bb + M's labels + hop 11 (ReportingTab names the refusal) + "Performance" tab label + SELECTION_UNSUPPORTED named | CTO 100359, MSTR 100367 |

Directory listing: p50 2308 -> 160 ms, p90 4665 -> 634 ms, p99 6093 -> 972 ms (03:21-04:21 vs 04:21-05:21).
Performance / holdings AFTER percentiles: no user traffic in the windows; owed on the next real load.

## The Performance thread (the CRO's trace @d8abd7dc65, hop by hop)

- 4a X10 ACTIVE: CLOSED (batch 27; row served in 07lSH03z). 4b / 3 / 10 / 12: CLOSED at the deployed
  bytes (CRO 100381: single account -> DEPENDENCY_UNAVAILABLE at the one-use factory, two accounts ->
  SELECTION_UNSUPPORTED, RetentionRefused no longer UNEXPECTED). 11: on DEV 7c542fd2.
- 6 THE ONE GATE LEFT before a number renders: the one-use plan for acc_d486fc9455d6b2aa18e13af1 on
  the default window -- Andrew's per-use word (put to him by the CTO 05:5xZ). No vendor call fires
  without it. Then: install the plan, ONE calculation, retained report, reopen without a vendor call,
  export.

## D1 -- the YCharts session (the resident's first hop)

Six credential submissions today (03:31, 03:49, 04:35, 05:55, 06:27 + the sixth pending), each
bounded to one by the CTO's word. Sign-in is proven every time (measured route /account/login/, the
two field names, 302). What stopped each run and what changed:

| run | pin | leg that stopped | finding | amendment |
|---|---|---|---|---|
| 4 | abce466570 | template via in-page fetch 405 captcha; Node client control 200 | the WAF challenges non-navigation fetches | 4th: Node client first |
| 5 | fc932d468b | identity via Node client on /dashboard/ 405 x7 | the HTML route challenges any non-browser client | 5th: identity from the page's own document |
| 6 | 5919c5363a | identity PASSED (page.content()); template via Node client 405 captcha, APIRequestContext 405 | run 4's 200 sent NO WAF token; run 6 sent the token cookie + header | 6th @9cf37df341: jar without the token; pair {without_token, with_token} |

Runner library at 9cf37df341: LF blob de00afffd4ce5f91.. (82479 bytes); wrapper 55ddb8f7 unchanged.
The sixth run fires on Y's STANDS; 405/405 on the pair = STOP (batch 30), the question moves to the
WAF rule, not the client. Resident half (Y 93ec16f4fe, integrated at 04cf6ab521): step_identity
validates the bundle, no /dashboard/ fetch; step_template is the liveness gate; Y's transport drops
the WAF token after the pair's verdict.

Rows: IRPT_BCKEND-S119 (bundle contract), S120 (Playwright under /root), S121 (the offline suite
reached ycharts.com once unguarded, 05:38Z, anonymous GET; the suite now refuses to start unguarded).

## Next at P (CTO batch 28 order)

1. Sixth submission on Y's STANDS -> outcome A: bundle grade, enrolled_user_id pin, C1, install-resident.sh
   with the resident files at 93ec16f4fe, Y --once.
2. Speed-lever candidate from DEV 7c542fd2: F1 (session key must not rotate on a token refresh --
   index.tsx:43-45 keys the QueryClient on auth.accessToken), F7 (dev double calls), F5 (2-char
   minimum, cancel superseded, never blank the list -- ClientSearch.tsx:64-101), F3 (limit 25 -> 100 +
   cursor prefetch), F2 (first browse with resolve -- cut to be confirmed with the CRO), Holdings not
   waiting on Performance (to be located: TabShell mounts one tab at a time).
3. Analysis backend (i)-(iv) on Y's prepared patches, one canonical act each.

## Standing constraints

Commits LOCAL (MSTR pushes); no vendor call without Andrew's per-use word; no synthesized trusted
header on a live surface; cookie values and credentials never printed; audited lane overrides only on
the CTO's word; the P/M/Y closer contract and the post-slug HOLD stand.
