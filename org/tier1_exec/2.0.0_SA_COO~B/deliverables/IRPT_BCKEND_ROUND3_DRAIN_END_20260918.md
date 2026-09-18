# IRPT_BCKEND -- ROUND 3 DRAIN-END READ AND L8 HAND-OFF (2.0.0_SA_COO~B, 2026-09-18 ~10:3xZ)

**Measured at HEAD `5eb167d37f` on the shared tree.** Terminality is read from proof-of-spec instances at HEAD (spine :487-488),
never from `<status>`: `surprise-row-gate._open_tos_for_project('.', 'IRPT_BCKEND')` -> **open = [], total 45** (the note names
`IB-rt-6` as terminal-by-VALID-proof with a non-terminal status word, as it has since round 2). No `wk-irpt*` worktree or
branch remains (`git worktree list` -> 0). Push state: LOCAL; origin/CLOUD `88b80ac07d` (last ls-remote read 23:53Z).

## 1. The round's orders -- 10 of 10 terminal, every instance VALID at HEAD with `--governing-order` (issuer re-grade on the shared tree, a different checkout from each worker's)

| order | cell | assignee | mechanical | drained @ | what it proved |
|---|---|---|---|---|---|
| IB-rtb-1 | round-2 carry | WK~1 | PASS | 8cb0364800 | replay authenticated 12 of 12 routes |
| IB-rtc-1 | rt5-ac2 host reading | WK~1 | PASS | adda105895 | the sibling cell's host reading answered |
| IB-rtc-2 | bundle closure + re-mint (AMENDMENT 1, R-45) | DS~X | PASS | 74d8367e75 | 8-file closure, member-level DISTRIBUTION flag, two-leg consistency + one-leg mutant |
| IB-rtc-3 | refresh builds for inflection + cottonwood (AMENDMENTS 2, 3) | WK~2 | PASS (22 of 22) | 5eb167d37f | dispatch passes no explicit `--as-of`; inf + cot landed 2 of 2 (byte-identical to rtc-7's fire the same day); 49f recorded, not graded |
| IB-rtc-4 | instrument hygiene | WK~3 | PASS | 68dc51340c | -- |
| IB-rtc-5 | renderer across-inputs control | WK~4 | PASS | 799ffd91bc | the renderer varies with its input |
| IB-rtc-6 | 49F principal DECLARED + sign-off packet (R-44) | DS~X | PASS (nothing applied) | 119fda050a | packet blob `bb92a81c69`, plans 2/1/0 and 0/2/0, writers 12 of 262 |
| IB-rtc-7 | 49F principal APPLIED under both halves, fenced, third directory | WK~1 | PASS (5 of 5 arms) | 9196f164cf | role `irpt-49f-directory-read-role`; directory 2/1/0, mdpf-pipeline TARGETED 0/1/0 (K3 32->33); fence 3 of 3 DENIED + 1 of 1 READ-OK from the host, name 0 of 4; **3 of 3 directories landed** (49f 4562 entries FIRST MINT, cot 259, inf 291); writers 12 of 263 same membership |
| IB-rtc-8 | K5 bundle mint | DS~X | PASS (4 of 4) | d0d4c6065f | `q8myxeHd...`, only the runner's stamp moved |
| IB-rtc-9 | runners validate under the host's jsonschema 3.2.0 + re-mint (row W2-S56) | DS~X | PASS (4 of 4) | c022677a9c | tolerant caller at both sites, 68 of 68 tests with a mutant-environment control, `0XLkiPt4...`, pre-cell tarball raising AttributeError 4 of 4 on the host |

Judgment criteria RECORDED and never self-graded: R33-AC2, R37-AC2, R38-AC2, R39-AC2 (and the round's earlier ones) -- **the CVO's at L9.**

Served identities at drain-end (from the workers' instances, R-40): Lambda `irpt-directory-refresh` CodeSha256
`JkY/lBc2Wucz/XIPzyH0zmJt22ucItxjDehbKJko6i4=`; bundle `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`
VersionId `0XLkiPt4wljdniLnF2fkPKN4qAIkjUbc` ETag `4c942a76f990874838e33e37f24ed69a`; role trust sha256 `7ce5283b...`, K2 policy `ab11263f...`,
`mdpf-runner-scoped` `aa94eeb6...` (33 statements); directories under `s3://opal-data-bd/investor-reporting/directory/2026-09-16/`
-- 49financial ETag `fcdf90de...`, cottonwood `264e0fbe...`, inflection `782324f9...`.

## 2. The channel -- L8's input (spine: "new investigation rows ... and no others")

`INVESTIGATION_v1.md` at HEAD: **218 rows** (three json fences; every appender since S57 writes into the first fence's array).
**25 rows carry `surfaced_at >= 2026-09-17T23:30Z`** (the round-3 window), ids: S54, S55, S56 (the CVO's own), S57, W3-S39, W4-S32, S58,
S59, S60, S61, S62, S63, S64, W2-S54, W2-S55, S65, S66, S67, S68, S69, S70, W2-S56, S71, S72, W2-S57. The CVO's watermark decides
which of these are new to it; the issuer's count is a denominator, not the CVO's.

**Disarms this round (evidence rows, each naming the ARMED row and its disarm_owner; disposition stays the CVO's):** S54 -> W1-S17;
S55 -> W1-S18; S61 -> W4-S32; S72 -> S65. S57 is the owner's intake over the 37 ARMED rows this seat owned at round start:
21 DISARMED, 2 in-round, 14 carried (the row is the authority; its commit message mis-stated 23/2/12 and was disclosed).

**Still ARMED and NOT this round's to close (carried):** S68 -- `aws_s3_object.mdpf_route_bindings` drift, deployed `56a03a14` vs
committed `650f893a` / CRLF `f94e8e4c`; accepted by `1.0.0_SA_CTO` as MDPF's owner (97865), NOT absorbed by rtc-7's targeted apply.
W4-S28 -- a real DIFFER on `irpt-ycharts-generate` (W3-S39 re-measured it NOT-COMPARABLE on bytes). W1-S16 -- the first round-4 cut
(S57). The CVO's S56 (GRADUATED, `disarm_owner` this seat "to route the pin convention to the round's cells"): ROUTED -- every
round-3 face cut after S56 cites its line ranges WITH a vintage (`:801-813 @a4db909717`, `:1148-1157 @a4db909717`, `:24-30`,
`:567-696`), which is the convention; the CVO grades whether that discharges it.

**INERT findings for the CTO's analysis (no cell served them; candidates, not cuts):** S71 -- `holdings_snapshot.py` loads its
contract from `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`, which is NOT a bundle member, so any holdings
fire from the bundle dies at `load_contract()` (the `irpt-holdings-snapshot` schedule is DISABLED; a guard edit adding the member
precedes any enable). W2-S57 -- `REFRESH_NOOP_SAME_FRONTIER` never fires against a real manifest history: `last_manifest()`'s
calendar-day backward walk finds the same-day `REFRESH_DISPATCHED` manifest (keyed by clock date) before the later COMPLETED one
at the runner's business date, so a same-day re-fire reports `REFRESH_COMPLETED_WITH_ADDITIONS` on an unchanged artifact (traced
on two live manifests). S63/S64/S66/S67/S69/S70 -- face-vs-world corrections the DS filed and worked through, none blocking.

## 3. What FWD-1 / FWD-7 now have and still lack (for the CTO's round-3 analysis; the grade is the CVO's)

- HAVE: three firms' directories built by the deployed dispatch through IB-rt-6's mechanism, on a real fire, from a repo-shaped
  bundle whose runners validate on the host; the 49 Financial read through a fenced, signed principal.
- LACK: the SCHEDULED organic fire (`irpt-directory-refresh`, `cron(0 9 ? * MON-FRI *)` America/New_York, next 13:00Z today --
  the first fire that meets the fixed runners, the K5 env and the principal together; its outcome is the negative arm the
  manual fires cannot replace); the D14 destination move (49f landed under legacy `opal-data-bd`, as the packet states); the
  per-firm as-of consequence (each firm's frontier picks its own date -- `2026-09-16` for all three today -- which IRPT_FNTEND's
  packet must carry); the no-op outcome's correctness (W2-S57).

## 4. Reserved and parked

- The bounded TEST PRINCIPAL card (FWD-1/2/5/11 bar at a live session) sits at `0.0.0_AB_MSTR` for Andrew; not cut.
- The DS lane `0.4.0_DS_ClientPlatform~X` is LIVE with an empty queue after four round-3 orders; held for the round-4 cut
  (W1-S16, S71 are DS-shaped) rather than released and cold-started.

**L8:** this file, at `org/tier1_exec/2.0.0_SA_COO~B/deliverables/IRPT_BCKEND_ROUND3_DRAIN_END_20260918.md`, is the hand-off;
the channel compile and its watermark are `3.0.0_SA_CVO`'s; the ONE slug to `1.0.0_SA_CTO` follows L9; the CTO's round-3
analysis is what this seat recuts from, in ONE issuance.
