# 3.0.0_SA_CVO -- session log, 2026-08-30 05:20Z -> 09:40Z (addendum 3 to session_cvo_0049-0250Z)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, SCRIBE

Continues `session_cvo_0049-0250Z_two_cells_ruled_and_frozen_and_the_pull_that_could_not_fire.md` (addenda 1-2 @d0a45f4ac0 / @58dee12eff). Same session (c570e726), one context compaction inside the window, one platform-side pause 06:07Z-07:51Z (MSTR 86316/86385: laptop-side, model turns absent, OS loops ran; nothing lost).

## What the window moved (conclusion first)

1. **C02-g-7 CLOSED at the grader, B-1..B-6.** The five never-produced trading days (2026-08-11/12/13/14/17) now have twr_daily partitions, and 2026-08-18 went from 7,315 all-REFUSED rows to 6,382 OK. Graded on MY OWN CONTENT READ of the served partitions (boto3 GET + pandas, 09:09Z): rows to the row on all six, 15 cols, schema 1.2, gross_leg_vintage 946b5c5a3c89, status distributions exact, OK bmv min 1.09; crosswalk stamps present in BOTH carriers on the re-driven dates and absent on the neighbours. G6: the proof instance VALID rc=0 on my unpiped run with the TO's expected set, checker 3948c766a7, instance == 5d4e3c932a.
2. **The a06 HALT** (surprise channel, BLOCKING x ARMED -> DISARMED by ownership same-turn): a06 read the NEWEST allocation map regardless of chain date; the map is header-only every weekend; Sun 08-23 and Mon 08-24 floor fires had ALREADY aborted in production, masked by the 08-29 backfill. Convention ruled (newest POPULATED + map_date/map_carried stamped), fix served 08:42:34Z (ETag == index blob), exercised 5 for 5 on the re-drive + the 08-18 re-emission. NOT REMEDIATED until the 12:45Z fire is read at 12:50Z.
3. **ADVI_BDPARITY:** P2-1 census plan graded PASS on its re-cut @6a99820c40 after three reworks I raised (pass 2 does not batch -- N=50 is ~2.1 h not 5 min; the "corroboration" of 5,309 was my own annotation inheriting the seat's number; the enum was not the harness's declared set); H1-H4 @7dac32ff34 PASS (H3 EXACT closes g-7's condition (1) on a third instrument; 0010083855's entire disagreement was our missing data); P2-1-AE PA-1..PA-4 PASS with PA-4 discriminated on my own live read of the function (CodeSha256 yO0R5J..., LastModified 09:14:51Z, DRY_RUN 0, INSURANCE_EGRESS 1). The Andrew ask is at MSTR citing 6a99820c40.
4. **The silver re-vendor (INF-ONEWRITER remediation):** (iii) PASS on the DOWNLOADED artifact on two oracles -- after I caught that the manifest's LF-normalised sha certifies a CRLF ship by construction (raw CR == 0 now in the plan AND the manifest declaration). The wired gate then FAILED OPEN on the first build (an MSYS path errored in native Python; a two-outcome conditional read the error as "declares nothing"); AE base caught it by grepping the build log for the gate's own signature; my structural addition (the build asserts its own gate signature) adopted as (a'). (iv) plan rows read; (v) on the gate's word.
5. **Channel ledger rows 38-47 written** (`CVO_SURPRISE_CHANNEL_FABRIC_ITEMS_20260826.md`): 38-44 on origin @416a116c8b (is-ancestor reads); 45-47 @05bc7a1114 LOCAL (one commit, three rows; its message is row 47's).

## Grader's own errors, on the record

- **argv[2] = "ids"**: my first run of the proof checker on the g-7 instance returned rc=1 with 8 violations because I passed the literal string "ids" as the expected-criterion list. All eight named the same impossible expected set; I read the checker's argv contract before filing anything and re-ran with B-1..B-6. Disclosed at 87082 and on row 46. Had the first rc been quoted, a VALID instance would have been graded INVALID on a wrong argument.
- **Annotation 2 inherited 5,309** from DS~C's own 17:38Z 08-29 message; the plan cited the annotation as independent corroboration. Measured (Grep for the first appearance), withdrawn as R2, rewritten by the seat with the second carrier's bound stated honestly.
- **Row 37 said "18 tables"**: corrected by citation on row 38 once the two seats' 18s were reconciled to a pinned list of 16 IN / 7 OUT.

## Rulings and adoptions this seat originated (all adopted by the gate/issuer)

| what | where | adopted |
|---|---|---|
| version-count arm over EVERY prefix (IN and OUT), not a five-date presence check | 86440 | CTO 86452 |
| "no island" holds only until Monday's map lands; print stamped vs inferred map_date | 86519 | CTO 86534, COO 86540 |
| P2-1 R1/R2/R3 | 86551 | COO 86582, CTO 86589 |
| dim_calendar `_ingested_at` re-classed at source: Atom 9 by design; a07:352 clock stamp is the incoherence | 86712 | CTO 86727 |
| 534-vs-535: the "campaign window" was derived from the members (tautology); 534 P14 + 1 floor | 86748 | AE~L 86763 (log form) |
| LF-normalised sha is blind to CRLF; raw CR == 0 beside it; (ii) is a control not the rung; APPLIED != EXERCISED | 86655 | AE base 86668, CTO 86674, DS~V @50231665b0 |
| build step asserts its own gate signature (the seam) | 87124 | CTO 87137 as (a') |
| two pre-registrations for the re-drive (island line determined uniform; a07 clock stamp expected, not a finding) | 86789 | held 5/5 |

## Compiler tools

| tool | run | result | note |
|---|---|---|---|
| `.tools/proof-of-spec-check.py` | g-7 instance x3 (bad argv, expected set, 2-arg); P2-1-AE instance x1 | INVALID (my input) / VALID / VALID / VALID | rc read unpiped each time; checker vintage printed beside the verdict |
| boto3 content probes (scratchpad `g7_grade_probe.py`, `g7_probe2.py`, `p21ae_live.py`) | 3 | all read-only, denominators printed | the content axis, distinct from the producers' version-count axis |
| `git merge-base --is-ancestor` after each CLOSE | 4 windows | rows 36-44 ANCESTOR | ls-remote read each time; never equality-to-tip |
| `comp-find` | 0 this window | -- | single-file greps and native Grep only; one Grep census (5,309 first appearance) |
| `.tools/safe-commit.sh -F` | 8 commits | all MATCH | message files by the Write tool |

What worked: reading the served bytes on my own instrument before grading -- every producer figure I checked matched, and the one apparent discrepancy (no `outcome` column) was my column name, resolved before it became a claim. What failed: my own checker argument. Gap found: none in the tools; the gap was in the operator, twice.

## Current state (for a reader with zero context)

- **C02-g-7:** CLOSED at the grader. Deploy ledger 20260830T0554Z CLOSED (AE~L's read). Remaining timed act: the 12:45Z floor fire read at 12:50Z from `gold/advi/_logs/chain_<TS>.log` (never SSM stdout) -- M-4 of the a06 cell C02-g-8, owner `0.4.0_DS_ClientPlatform~N`; expected: a06 line map_date=2026-08-28, 2026-08-29 SKIPPED, map_carried=True, the chain re-producing 08-28 in place (new VersionIds on 08-28 are floor behaviour, not campaign damage). Row 38 moves DISARMED -> REMEDIATED on that read.
- **Open DS-lane items on the channel:** a07:352 clock stamp (own cell after M-4); `bmv` NaN on refusal rows vs the g-5 convention (gate reading: operand RETAINED; DS~N's source read owed); c04's anomalous_return_census NOT WIRED (gate queue 86944).
- **Silver re-vendor:** (v) safe-apply on the CTO gate's word, then (vi) the live read-back (CodeSha256 == zip, LastModified post-apply, downloaded members LF sha == manifest AND raw CR == 0) -- graded on arrival; the EXERCISED arm is the first post-deploy fire (DS~V's pre-redeploy baseline pinned at v=jCldmxzm).
- **ADVI_BDPARITY:** P2-2 fires only on Andrew's word; the ask (two words on one card) is at MSTR citing 6a99820c40. P3 (the eleven still-LARGE cells) at the convention gate.
- **Reserved cards** D2-T69-R2, D3-T73-R3, R5: Andrew's.
- **Inbox hygiene:** every message whose body I read is acked on reading; ~11 cc'd closures this window read by subject only remain un-acked and are stated as such (LD-0480 shape).

## Next steps

- [`0.4.0_DS_ClientPlatform~N`] 12:50Z fire read (M-4); bmv-on-refusal source read; a07 cell after M-4.
- [`0.7.0_AE_CloudOps`] (v) on the gate's word, (vi) live read-back -> grade here.
- [`0.0.0_AB_MSTR`] the P2-2 ask to Andrew citing 6a99820c40.
- [`3.0.0_SA_CVO`] grade (vi) and the 12:50Z read on arrival; row 48 on the fire read; rows 45-47 is-ancestor after the next CLOSE.
