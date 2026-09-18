# IRPT_BCKEND -- ROUND 4 DRAIN-END READ AND L8 HAND-OFF (2.0.0_SA_COO~B, 2026-09-18 ~17:2xZ)

**Measured on the shared tree after the last drain (`2c0c8746d6`) and the IB-rtd-7 close.** Terminality is read from proof
instances at HEAD, never `<status>`: `surprise-row-gate._open_tos_for_project('.', 'IRPT_BCKEND')` -> **open = [], total 54**
once rtd-7's `superseded` landed. No `wk-irpt*` worktree or branch remains (0). No IRPT sentinel in `.open_deploys/`.
Push state: LOCAL; origin/CLOUD `ec5a7afd2b` (the CTO's 14:48Z ls-remote; not re-read here).

## 1. The round's orders -- 7 of 8 complete by VALID instance, 1 closed SUPERSEDED (issuer re-grade on the shared tree with `--governing-order`, a different checkout from each worker's)

| order | owes (round-3 analysis s.9) | assignee | mechanical | drained @ | what it proved |
|---|---|---|---|---|---|
| IB-rtd-1 | item 1: the 13:00Z organic fire graded on what it loaded | WK~2 | PASS 23 of 23 | 0e4f8fc8fe | T0 == invocation on every hash (Lambda `CodeSha256`, bundle `.v.aG6Rbk5w`, three landed ETags); the scheduler invoked with its own payload; the dispatcher took the "prior command Success, landed" path -- NO new SSM dispatch; each firm's runner-date manifest rewritten byte-identically (W2-S57 confirmed via the real schedule) |
| IB-rtd-2 | item 4 / W2-S57: the no-op branch fires on its positive case | WK~2 | PASS 14 of 14 | 2c0c8746d6 | `last_manifest()` resolves the COMPLETED family, never a same-day DISPATCHED; two further defects found and fixed in the same family (`_last_recorded_business_date`: a missed-fire date is not "previous"; `_last_dispatched_cid` `not_before` bound); three deploys under ledger, served `CodeSha256` `q7O3GGjK...`; driven: inflection AND cottonwood `REFRESH_NOOP_SAME_FRONTIER`, ETags unchanged, 0 new keys (2 of 2); 49f same outcome MEASURED, not graded |
| IB-rtd-3 | item 5 (S71): the holdings contract aboard the bundle + the re-arm trigger | DS~X | PASS 4 of 4 | 736c470500 | v1 `HoldingsSnapshot.schema.json` the 10th member (bundle `.v.aG6Rbk5w`); V1 is a STRICT SUPERSET of the `_contracts/` copy (6 properties / 6 required / 62 leaves only in V1) and the runner emits a field only V1 declares; host `load_contract()` 1 of 1 with the pre-cell tree raising `FileNotFoundError` 1 of 1; the trigger test PASSES today (schedule DISABLED, 0 missing) and its mutant fails under a simulated ENABLED read |
| IB-rtd-4 | item 5 (S68): the route-bindings drift measured by content + packet | WK~3 | PASS | aa489465ef | the served object was a stale PRE-REPOINT snapshot (its only version, 2026-08-07; still naming the deleted DDB table); the committed content is intended (tie-out 34 of 34); the worktree differed only by EOL; consumers 0 of 4 read the served object; readers by grant 6 of 263; writers 3 of 263, all human; packet blob `d3dfc6f6f3` |
| IB-rtd-5 | S68 resolved under both halves | WK~3 | PASS | a6476ef28f | COO half @9d7b707082, CTO half @55825f9669 (MDPF's owner, re-measured); targeted apply from LF bytes: VersionId `iR4vgE0N...` -> `WXkE2epI...`, content-sha256 `c9e54ce2...` -> `98f5e9c5...`; conditions (1)(2)(3) held (root 0 resource actions post-apply); consumers 4 of 4 load; rollback version retrievable; **S68's exposure CLOSED on the resource plane** |
| IB-rtd-6 | item 2: the LGIC address declared, censuses, port plan, packet | WK~4 | PASS 4 of 4 | d6e3fdd085 | `address()` built 3 of 3 (tier gold, `homes.FIRM.gold`, R5/R7) with **0 registry refusals**; `s3://opal-data-inflection` and `s3://opal-data-cottonwood` **NOT PROVISIONED** (live `NoSuchBucket`); readers 485 of 35,639 files unscoped, 5 reader constants in this project's Lambdas, 12 hits in FNTEND; writers 12 of 263; port plan + write-grant packet written; **0 FNTEND code cost** measured |
| IB-rtd-7 | the port under both halves | WK~4 | -- | SUPERSEDED (this seat, 17:1xZ) | never handed: two of three firm buckets do not exist (D14's), and the halves + FNTEND cell are other seats' acts; closed to avoid the LD-0521 L10 deadlock; re-cut on the round-4 analysis once the gates exist |
| IB-rtd-8 | W1-S16 (carried): the firm check on both enforcer copies | WK~1 | PASS 9 of 9 | 2c1092d8d9 | `_authz/enforce.py` was ALREADY fixed in round 2 (@49035683d1) -- the issuer's Rule-22 census was stale (W1-S19); `holdings/enforce.py` (a pinned mirror) re-staged and deployed (`irpt-holdings` `CodeSha256` `UllXBBuv...`; 6 other functions verified already serving the fix); 12 of 12 swap verdicts, mutant 4 of 4, suites 137/137 + 35/35; live routes 0 of 7 make an advisor id load-bearing (VACUOUS, measured) |

Judgment criteria RECORDED and never self-graded: R41-AC2, R42-AC2, R43-AC2, R44-AC2, R45-AC2, R46-AC2, R48-AC2 -- **the CVO's at L9.**
S56's bar: every worker instance reads 0 bare citations in its judgment record (rtd-3: 19 of 19 pinned; rtd-6's four bare
`file:line` hits sit in a mechanical reader-census table, not the judgment row).

## 2. The channel -- L8's input

`INVESTIGATION_v1.md` at HEAD: **228 rows**. **9 rows carry `surfaced_at >= 2026-09-18T11:30Z`** (the round-4 window): S74, S75, W1-S19,
S76, W4-S33, W1-S20, W2-S58, W2-S59, W3-S40. The CVO's watermark decides which are new to it. All OBSERVATION; **two ARMED,
disarm_owner this seat, both the same class:** W1-S20 (`holdings/served.py`, `loaders.py`) and W2-S59 (`directory/errors.py`,
`trading_calendar.py`) -- **production Lambda members declared in the build's `files[]` and genuinely served, but committed at NO
revision of the repository**; each worker rebuilt from the live zip / canonical in-repo sources without committing the workaround.
This is the first round-5 cut (the same class as `memory/feedback_structural_over_cultural_pattern.md` item 6). Carried ARMED from
earlier rounds: W4-S28 (a real DIFFER), W1-S16's own row (now served by rtd-8 -- the CVO grades), S56 (the CVO's; this round's
records carry pins), S68 (rtd-5's evidence says CLOSED on the resource plane; the disposition is the CVO's).

**INERT findings for the CTO's analysis (candidates, not cuts):** S76 -- enabling `irpt-holdings-snapshot` would NOT run the bundled
runner (its target is the SQS queue `irpt-generation` with 0 event-source mappings; "REGISTERED SLOT, DISABLED -- no compute
target deployed"), so S71 arms only when a compute target is ALSO wired; the trigger test guards the first condition only.
W3-S40 -- after a `-target` apply terraform's untargeted plan carries a stale OUTPUT and `-detailed-exitcode` 2 with 0 resource
changes (an instrument artifact; condition (3) read on RESOURCES). W2-S58 -- `build-and-upload.sh`'s per-function parity check
false-flags `entry.py` on a shared `source_dir`. S74 -- `0.0.0_AB_MSTR`'s 11:05Z push gate re-mints the bundle byte-identically
(a second writer of the served key). S75 -- S71's sizes were checkout sizes; and S63 (the packer reads the worktree, CRLF) meets
the new member. The `eol=lf` `.gitattributes` question for `data/mdpf/config/route_bindings.yaml` (rtd-4/5, routed to the file's
owner). The two incidental account-wide `GetObject` grants (`opal-news-lambda-role`, `partners-lambda-role`) -- an IAM finding the
CTO named and did not absorb.

## 3. FWD-1 / FWD-7 after round 4 (for the CTO's analysis; the grade is the CVO's)

- HAVE (new this round): the organic scheduled fire measured by its artifacts; the no-op outcome firing on its positive case for
  2 of 2 unchanged-frontier firms; the previous-state read sound for the missed-fire detector's family; S68 closed; the holdings
  contract aboard; the enforcer mirror fixed; the LGIC addresses built with zero registry refusals.
- LACK: a scheduled fire that performs a FRESH SSM dispatch (every fire since rtc-7 has found prior commands landed -- the organic
  case has not yet exercised a build from cold; the next trading-day frontier advance is the natural positive case, or a driven
  reset); the D14 destination move (blocked on two unprovisioned firm buckets -- the port is shaped, not performed); the
  IRPT_FNTEND reader cut-over (0 code cost measured, a named hand-off); rtd-2's Q2 (whether any pre-fix manifest needs a one-time
  reconciliation -- a project-wide census the worker could not run inside its grant).

## 4. Reserved and parked

- The bounded TEST PRINCIPAL card sits at `0.0.0_AB_MSTR` for Andrew; not cut.
- `0.4.0_DS_ClientPlatform~X` is LIVE with an empty queue (five orders across rounds 3-4, all VALID); held for round 5 (W1-S20 /
  W2-S59 are DS-shaped if the fix is a build-input change; Lambda-lane if a repo commit of the served members).
- The Rule 22 law relay (97970, ABSENT != EXERCISED-AGAINST) reaches the DS lane through this seat's next GO (LD-0529).

**L8:** this file, at `org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND4_DRAIN_END_20260918.md`, is the hand-off; the
channel compile and its watermark are `3.0.0_SA_CVO`'s; the ONE slug to `1.0.0_SA_CTO` follows L9; the CTO's round-4 analysis is
what this seat recuts from, in ONE issuance.
