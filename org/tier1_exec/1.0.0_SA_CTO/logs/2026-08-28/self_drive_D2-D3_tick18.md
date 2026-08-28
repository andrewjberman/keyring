# /self-drive D2 & D3 — tick 18 (2026-08-28 20:19Z) — state: ARMED

Covers tick 18 (tick 17 logged @7c32c7007d). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: the first PERFRP emission in the
project's history; the campaign clock corrected by its own executor and the bundle boundary
re-ruled; an exec-sum rendered for Andrew and a plain-language stage report given at his ask.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342, 0 claimed-not-member.

## Calls (§1-2)

**Zero.** No adjudicable, no RESERVED.

## Verdicts / rulings since tick 17 (§3)

- **PRF-b-2 BUILT + QA-EMITTED (DS~V 78976 @e94af643b5) — THE FIRST PERFRP EMISSION ON ANY
  PLANE** (AC0 had measured 11 of 11 leaves never emitted): `perfrp_performance_relationship.json`
  3,075 entries / `_account.json` 4,665 entries, fixture-loadable, as_of 2024-11-07, SI window 88
  trading days; the issuer's pin pair + `campaign_ledger_commit` + `dates_complete_of_534` TRAVEL IN
  THE PAYLOAD. The round-1 defect it repairs: `_performance` read ONE `twr_daily` partition (one
  business date) and set `expected_days = len(series)` = 1, so a one-day window scored COMPUTED at
  coverage 1.0 against itself — both halves wrong in the same direction; the contract's status
  classifier was named in a docstring and never implemented (661 null-r_net rows on one date split
  656 / 5 across two reasons with opposite remedies). Fixed: contract-defined windows from the ONE
  trading-calendar frontier (NEVER-4; `max` refuses; YTD clamps to the SI floor), an ABSENT partition
  is a missing day but any other read failure is FATAL, `SI_WINDOW_START_ASSERTED`. Oracle on an
  independent code path over the same substrate: 4,070 of 4,070 at max|delta| = 0 (independence
  stated narrowly — bytes rest on the campaign, AC6). Two of its own arms were wrong and corrected in
  the artifact (the sum-vs-product mutant is the identity when at most one return is non-zero).
  `comp-pipescript deployed` reads the emit core STALE — correct under the build-only cap (no
  build-and-upload; CRLF ruled out). **→ DE~D's re-based re-seat trigger is now satisfiable by
  measurement (note to COO 20:15Z; COO's call).**
- **Campaign clock CORRECTED by ~L (78959) and adopted:** 12.8h of remaining work against a 16.6h
  anchor = a finish ~2026-08-29T08:57Z, **3.8h BEFORE the 12:45Z pause** (the subtraction had never
  been done; CVO 78932 and COO 78917 had carried the wrong clock; both retracted @670537113c and in
  COO's addendum; COO re-verified ~112 s/date → ~09:10Z on its own window). **RULED (78961):** the
  four-item bundle's boundary = CAMPAIGN COMPLETION (the ledger READING 534/534, never the
  projection), the 12:45Z pause as the FALLBACK if one interruption consumes the slack; the
  DocumentVersion pin lands as future-run protection and says so; the OS-journal read is stronger
  at completion; the 534/534-keyed triggers become reachable in the morning; COO's post-campaign
  sitting re-sequenced to ~09:00Z-onward 08-29; the 04:35Z INSURE fire is unaffected (different host).
- **Per-100 #1 grain correction:** the committed ledger @0bc0e8e588 holds 104 lines / 102 dates
  (the report said 103/101 — counted from the tree before the commit; ~L confirmed on the object);
  ~L then found its reconciliation had built the ledger's command_id set from the DATE-KEYED dict,
  dropping exactly the two superseded rows' ids (07659d4a, a38048e8) — right grain for "dates
  complete", wrong for "which sends the ledger references". Per-100 #2 form fixed on four counts
  (commit first + derive from `git show`; join on LINES with a superseded bucket; print the
  send-plane timestamp AND instance; post-commit rows belong to the next report). CVO's own
  ledger↔SSM join (78934 @30aeaf5ad1): every ARTIFACT-COMPLETE row's command = Success, 0
  exceptions / 104 rows. Campaign 120 of 534 in the tree at 20:19Z, 0 non-complete.
- **/exec-sum --macro D2 / D3 rendered for Andrew (20:12Z)** on live grounding (comp-state
  self-test PASS 4/4; telemetry 365,139 rows / 142 files; git 30 min; 16 live). Zero capacity to
  surface; ONE record-drift surface to COO (78979-class): ADVI_INSURE / ADVI_PERFRP `blocking`
  still read "seats CLOSED — re-seat on Andrew's word" and ADVI_49F's phase predates the campaign
  (comp-state BEHIND on the per-100 commit) — superseded today; a refresh at COO's next drive log.
  **Andrew then asked for a plain-language stage report** (no TO references): given at 20:2xZ —
  what the product is, why the portal shows nothing (nothing served by design; the leaves had never
  been emitted until b-2), the PRD §8 definition of done (E2E flip+promote+his smoke; parity to
  EXACT), the six stages and where each stands, ~2-3 working days to a page with real numbers.
  He may re-shape `/exec-sum` on that format — his word pending.
- **Window frames / base seats:** the base seats stay off MSTR's OPEN/CLOSE frames on his word;
  question with Andrew via MSTR. All seven of this seat's commits today ON origin @2afd4ddd4e.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @2afd4ddd4e, ls-remote read 20:19Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · ledger read · campaign ledger
  tree count (distinct dates) · `git ls-remote` + MERGE_HEAD · for the exec-sum: `comp-state
  --self-test` (PASS 4/4) + `comp-state` (triaged: one real drift, the rest lexical), telemetry read
  (python, never jq), `git log --since=30m`, `get_live_agents`, per-project M1 table.
