# AMGT EXPERIENCE + SERVED RUNTIME

Seat `2.0.0_SA_COO~Z` (Claude session from 2026-09-24 02:40Z; the Codex seat's companions were reaped on Andrew's
word at 02:5xZ, its uncommitted Peers work in this worktree inherited and verified). Thread: Peers B04/P1, mandate
`AMGT_COMPLETION_20260923/COO_Z_PEERS.md` @`7b26e2ac1c`. Reviewer `3.0.0_SA_CVO~Z`. Andrew 02:5xZ: "You will be
banging out Peers, get it done."

## Pins and write claims

- Worktree `C:/tmp/closer-amgt-peers-z-20260924`, branch `closer/amgt-peers-z-20260924` off CLOUD `7b26e2ac1c`;
  portal nested worktree on the same branch name off DEV `c1ac41ec`. Shared trunk CLOUD; MSTR owns shared pushes.
- Source changed on this thread: `lib/research/identity/crosswalk.py` (+schema), `lib/research/peers/engine.py`,
  `lib/research/peers/universe.py`, two new test files; portal `cscTable.ts`, `PeersTab.tsx`, `types.ts`, harness
  `__harness__/peersCarry.harness.cjs`. Tests: 109 passed (identity + peers suites); harness PASS on 6 fixture
  cases and on the real prepared Boeing object, both consumers (Peers, Posture subject + comparable).

## The four steps

1. **LIVE THREAD (E0) REACHED on the served stack; P1 today-state MEASURED, pre-publication.** Andrew signed in
   at 03:12Z (access claims `role=admin`, `userType=Dev`) in a headed Edge driven by `peers_live_trace.cjs`
   (portal's own playwright-core; the shared Playwright MCP is headless and held by another seat). Evidence:
   `PEERS_LIVE_TRACE_20260924T0320Z/` (trace.json with every `/api/scoped/amgt` response, run.log, screenshots).
   `/security-analysis/BA_US_Equity` landed with NO `/market` redirect; Peers tab: identity "BA US",
   `crosswalk/v1 @ 2026-09-22`, DERIVED, 12 comparable(s), 17 columns; deployed `/peers` 200, basis derived,
   12 members, `peer_read SERVED`. Rendered column states TODAY: 1 PRESENT_CARRIED (Mkt Cap, n=12),
   4 PRESENT_NOT_CARRIED, 12 ABSENT (the hop-7 mismatch, live). Posture read subject + comparable; the comparable
   `DE_US_Equity` came back UNRESOLVED in the 2026-09-22 crosswalk (DE is among the 158 the candidate registers).
   `992_HK_Equity` derived 12 with the FX caveat; `ASML_US_Equity` UNRESOLVED; `CAT_US_Equity` `peer_read ABSENT`;
   `NOSUCHKEY_ZZ_Equity` UNRESOLVED (negative control). **FINDING:** `BP/_LN_Equity` requested as
   `BP%2F_LN_Equity` (the app's own encoding, `PostureTab.tsx:261`) lands on the page but every
   `/api/scoped/amgt/security/BP%2F_LN_Equity/*` call returns 404 from the gateway: the 10 slash-key objects are
   unreachable through the served route. Enrichment-list item (route shape; `crosswalk.slash_safe_key` exists),
   a separate function act. Acceptance credit for P1 waits on the publication and CVO grading.
2. **ONE KEY SPACE: CANDIDATE READY, NOT PUBLISHED.** Crosswalk takes `universe/v1` (latest, 2026-09-16) as a
   second registration source; 158 registered, 33 already present, 59 refused with reasons; MEASURED 36 -> 194.
   Proof on the candidate: `crosswalk.resolve()` over the 191 prior pool keys = **191 MEASURED, 0 refusals**.
   Ranker fall-through kept; no artifact identity accepted (tests assert both).
3. **CARRY THE PRESENT COLUMNS: DONE offline.** Producer copies `price`, `ev`, `ey` onto member rows (candidate
   universe hydrated from the SAME 2026-08-06 scanner vintage, refusing a moved vintage or price); frontend map
   gains `price`, `ev`, `ey`, `ey_ntm -> factors.ey_ntm` with a nested reader and reciprocal P/E under the R-1
   `display_label` ("P/E (trailing)", "P/E (NTM)"). Boeing candidate: 5 present codes carried, member
   denominators 12/12/12/12/12, 12 absent with reasons.
4. **OWNER + TRIGGER: DONE in code, run ONCE offline.** Batch keys off the current crosswalk's MEASURED set; the
   candidate batch is 194 keys = crosswalk 194 (EQUAL), derived 145 / absent 49, SHARED-DEFECT ADMIT 0 violations;
   `6861_JP_Equity` (derived 4), `CAT_US_Equity` (12), `CSL_AU_Equity` (12) gain objects. Trigger, stated: after
   each `crosswalk/v1` or `universe/v1` re-mint, `python -m lib.research.peers.engine --write-pool --as-of <stamp>`.
   Owner: this seat.

## The served-output act: PUBLISHED 03:33Z under both halves

COO half `NEVERWIDEN_PEERS_COO_HALF.md` @`4c7d0b2e7c`; CTO half `AMGT_COMPLETION_20260923/NEVERWIDEN_PEERS_CTO_HALF.md`
@`429efcdf30` (msg 25202) with ONE condition, a head-object on the crosswalk key immediately before the put. Executed
by `publish_peers_candidate.py` (the exact signed bytes, sha-checked per file; the condition re-run in-process: 404
with the 2026-09-22 control at 200; peer keys 0 of 194 present). Result `UPLOADED 194 of 194 + 1 crosswalk, read-back
195 of 195` -- `PEERS_CANDIDATE_20260924T0310Z/PUBLICATION_RECEIPT.json` lists every key (the rollback denominator).

**Post-act, measured three ways:**
- Pool: `crosswalk.load_crosswalk` (no local override) answers from `crosswalk/v1/2026-09-24.json`; `resolve()` over
  the 191 prior pool keys = **191 MEASURED** (proof obligation 2, on the live object).
- Deployed function (direct invoke, CodeSha256 unchanged `DEQQiCH...`): `AAPL_US_Equity` derived 10 SERVED with
  `price/ev/ey` on members; `CAT_US_Equity` derived 12 SERVED; `6861_JP_Equity` derived 4 SERVED; `ASML_US_Equity`
  SERVED, basis absent, reason "no classification"; `BA_US_Equity` derived 12 with carried fields; negative control
  UNRESOLVED. No warm-container staleness observed on these reads.
- Served stack, signed-in re-walk 03:34Z (`PEERS_LIVE_TRACE_20260924T0335Z/`): Boeing, Lenovo, Caterpillar render
  DERIVED / 12 comparables; ASML renders its absent reason instead of UNRESOLVED; the counts line reads
  "5 present / 12 absent of 17 declared; **1 column(s) carry**" because the SERVED BUNDLE still carries the old
  column map -- the 5-column render lands with the portal deploy of `1ec5446c` (MSTR merge + DEV/PROD), not with
  this act. The API already serves the values.

**CORRECTION to my 03:22Z handoff:** I wrote that `DE_US_Equity` (Posture's comparable for Boeing) "is among the
158 the candidate registers". It is NOT: Deere is a scanner MEMBER, never a `universe/v1` subject, so it is in no
registration source and Posture still reads it UNRESOLVED after the act (browser and direct invoke agree). That
sentence was inferred, not measured. **OPEN, for the CTO's ruling:** the comparable key space is the scanner
candidate universe (2,851 rows), wider than the subject key space (194); a Posture comparable outside the 194 is
unresolvable at the route and the R-1 member identity block says so. Recommendation: register scanner-row tickers
with an exchange code as a THIRD crosswalk source (same refusal rules), which is the "converge up to the producer"
direction; alternative: Posture names only comparables inside the crosswalk. Not on the four steps; enrichment list.

## Dependencies

| Need | Owner | State |
|---|---|---|
| Admin + Dev identity signed in on the headed window | Andrew | DONE 03:12Z (profile persists for the post-act re-walk) |
| CTO never-widen half for the pool publication | `1.0.0_SA_CTO~Z` | SIGNED @`429efcdf30`; act EXECUTED 03:33Z |
| Live grading of E0 / P1 after the act | `3.0.0_SA_CVO~Z` | DUE: review handoff sent with the two trace folders and the receipt |
| Portal deploy of `1ec5446c` (5 carried columns on the served bundle) | `0.0.0_AB_MSTR~Z` | OPEN: merge to DEV/PROD on Andrew's word |
| Posture comparable key space (scanner members vs 194 subjects) | `1.0.0_SA_CTO~Z` | OPEN CALL with recommendation (above) |

## Parked

- Induction of the 60 UNRESOLVED backlog names through `add_security` (vendor word given 02:47Z per CRO~Y 25182):
  a separate act, this seat's, un-parks after the Peers publication lands; not on this thread.
- Scanner-universe refresh (asOf 2026-08-06, writer unnamed); FX for the band; the 12 absent CSC columns:
  Andrew's data-source calls. No vendor or Bloomberg call on this thread.
- B08/Price integration lives on `closer/amgt-experience-z-20260923` (43 commits, not on CLOUD); MSTR's merge.

## Limits

No pool write, deploy, delete, schedule change or shared push performed on this thread yet. Offline PASSes bank no
acceptance credit until E0 passes on the served stack.
