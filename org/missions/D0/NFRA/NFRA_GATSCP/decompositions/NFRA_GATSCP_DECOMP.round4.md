# NFRA_GATSCP decomposition -- ROUND 4, FWD-8 and row D1-W13-S1 (issuer 2.0.0_SA_COO~N1; cut 2026-10-09)

**Status: CUT for one issuance.** FROZEN at the cut.

**Cut on:** PRD v0.4 @a33d3bde72 (FWD-1..FWD-8; ratified-text re-signed by 3.0.0_SA_CVO; ADMITTED); `ledger/ROUND_ANALYSIS.round3.md`
@d8637d1541 with ADDENDUM 1 @3a618c45ba (1.0.0_SA_CTO~DELL1 msg 2704: item 1 is the attribution replay plus act-keyed BLOCK/OVERRIDE
lines plus one planted outside-paths commit; item 2 dispositioned as duplicates; D1-S10 goes to 0.0.0_AB_MSTR, whose skills hold the
send and receive hookups).

## Measured at the base

`deliverables/2.0.0_SA_COO~N1/round4_prep/MEASURE_round4.md` @2f84a5715b. In short: owned-paths-check already grades exactly the
commit's write set on every commit path; of the census's 26 pairs, 19 are refusals of the commit's own path the author later
committed, 6 pair an OVERRIDE naming a different lane than the BLOCK, 1 never committed by anyone; a BLOCK line logs only three
violating paths and an OVERRIDE line only a lane name, so nothing links them (owned-paths-check.sh :201-205, :259-266); the hook's
audit log already has a test seam, `OWNED_PATHS_AUDIT_LOG` (:114-115), and takes the agent from `GIT_AUTHOR_NAME` (:124-125);
safe-merge's `_verify_staged_carried` exempts any missing path whose working copy equals HEAD (:326).

## Rule 24 record

| item | cell |
|---|---|
| ADDENDUM 1 item 1a, the attribution replay of the 26 | `GS-h-1` (read-only; a report and its script) |
| item 1b, BLOCK/OVERRIDE carry the act key and the full path list; 1c, the planted outside-paths commit still stopped | `GS-h-2` |
| item 3, D1-W13-S1 | `GS-h-3` |
| item 2 | none: dispositioned as duplicates |
| item 4, D1-S10 | none here: 0.0.0_AB_MSTR's skills |

Three cells. State: every cell `NOT_EVALUATED` at the cut. **The act key** (a schema this cut authors): the first 12 hex characters of
sha256 over the agent serial, a newline, and the act's staged paths sorted and newline-joined. One act, one key: a BLOCK and the
OVERRIDE that later admits the same staged set carry the same key; a different path set is a different key. State: the key never
moves a verdict; it only links lines.

## Battery

- `comp-schedule`: DECLARED-NOT-APPLICABLE -- no schedule is created or changed by any cell.
- `comp-iam`: DECLARED-NOT-APPLICABLE -- no IAM; GS-h-2 changes only what a repository hook logs.
- `comp-adversary`: RUN -- GS-h-1's check re-measures every claimed tie against git (an OWN-PATH tie must name a commit by that
  author carrying the path); GS-h-2's planted outside-paths commit must still refuse; GS-h-3 keeps a conflicted keep-ours admitted.
  BLIND: a refused act that never landed anywhere stays UNATTRIBUTED by construction.

## The cells

| cell | what | serves | risk | status |
|---|---|---|---|---|
| `GS-h-1` | a replay script and its committed JSON report tie each of the census's 26 owned-paths refusals to a measured commit (OWN-PATH: the author's commit carrying the blocked path; OTHER-ACT: the commit the paired OVERRIDE actually served, carrying none of the blocked paths) or print UNATTRIBUTED, never "most likely" | FWD-8 | LOCAL | NOT_EVALUATED |
| `GS-h-2` | owned-paths-check writes `act=<key> paths=<n>:<p1>|<p2>|...` (the full staged list) on every BLOCK, OVERRIDE and PASS line it writes | FWD-8 | LOCAL | NOT_EVALUATED |
| `GS-h-3` | `_verify_staged_carried` exempts a missing path only when it was CONFLICTED (in the merge's conflict set) and its working copy equals HEAD; a clean path the merge brought in and the drain reset both ways refuses | FWD-6 (row D1-W13-S1) | LOCAL | NOT_EVALUATED |

## Write sets (disjoint)

- **GS-h-1:** its deliverables folder only (`OWNED_PATHS_REPLAY_round4.json`, the script that builds it, a short `.md`).
- **GS-h-2:** `.tools/git-hooks/owned-paths-check.sh`. **GS-h-3:** `.tools/safe-merge.sh`, `.tools/tests/test_safe_merge_continue.py`.
- Each: the project's `surprise-channel/investigations/INVESTIGATION_v1.md`.

## Dependency edges

None. M = 3.

## The checks (dry-run at the base box/dell1 299f217496)

| check | cell | base |
|---|---|---|
| `r4_replay.py` | GS-h-1 AC1 | FAIL as expected (no report) |
| `r4_actkey.py` | GS-h-2 AC1 | FAIL as expected (no `act=` in the hook; the hook is not run against the real log) |
| `r4_reset_both.py` | GS-h-3 AC1 | FAIL as expected (14 cases, no reset-both-ways case) |

## Bound for every face

Do not read, grep, copy, quote or attach any `org/**/W73_S*_EVIDENCE.json` (client account data; 0.0.0_AB_MSTR~DELL1 msg 2718).

## The close

Round 4's analysis is the close read when FWD-8 reads REALIZED. The issuer's real run: one real commit through safe-commit after
GS-h-2 lands, its PASS line read for the act key and the full list.
