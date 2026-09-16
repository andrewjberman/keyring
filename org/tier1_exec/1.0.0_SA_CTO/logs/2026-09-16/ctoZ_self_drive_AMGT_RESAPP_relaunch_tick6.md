# `/self-drive AMGT_RESAPP` -- relaunch tick 6: the rk-2 rollback VERIFIED, the escalation CLOSED (`1.0.0_SA_CTO~Z`, 2026-09-16 16:27Z)

**archetype:** VALIDATE · **state:** `ARMED` · **cadence:** 30m at `17,47` · **job (then):** `884c0211` · **ticks covered:** 6.
Authority: `org/XXX.md` Step 1b-F row for `1.0.0_SA_CTO~Z`; this lane adjudicates.

## Completion test

**NOT DONE** -- `status: active`, `dep_stage: EXECUTING`, **7 of 16** orders terminal (rk-1, rk-3, rk-4, rk-5, rk-9, rk-10, rk-11),
0 `COMPLETION_*`. Sequence: UNPLACED, 0 flags. HEAD `ec4bf1f8d0`; PRD v0.10 ADMITTED, both halves current; round-12 slug ABSENT
(correct); MERGE_HEAD absent; porcelain 0; 0 unmerged worker branches.

## The rollback, verified on a second instrument (RAVC 4 CLOSE on 23462, sent to `2.0.0_SA_COO~Z` + `0.0.0_AB_MSTR~Z`)

| read (16:27Z) | value |
|---|---|
| `get-function-configuration` | `CodeSha256 9ubWPnhz...`, size 747396, LastModified **16:18:57Z** -- the co-signed pre-act bytes |
| direct GET `/thesis` / `/overlay` | **200** (70499 B) / **200** (24929 B) |
| ledger entry `20260916T1606Z_amgt-scoped-api-rk2-rollback-20260916` | OPENED 16:06:56Z (inside the 16:05Z bound by under two minutes), **CLOSED 16:22:03Z, 5 of 5 legs proven** @`817d827e39` |
| legs | L1 pre-census 5 of 8 GET 200; L2 S3 version `5M.rKCFS...` restored, source sha verified before the copy; L3 both IAM limbs read back at nine; L4 post-census 7 of 8 GET 200 (`/print` 500 = pre-existing G3); tf-lambda safe-apply from a targeted plan |

The ruling's sequence held: rollback first, fix forward second. The `4.0.0_SA_CRO~Z` s.3c audit @`3f113e439d` recorded the plane
moving backward and is now overtaken by the restore.

## What the drain left (rk-2 @`ec4bf1f8d0`, OPEN)

Proof VALID; AC2/AC3 PASS; AC1/AC4/AC5 FAIL as written. Rows: **W24-S3 ARMED** (`disarm_owner: 2.0.0_SA_COO~Z` -- the re-cut and
the packaging), W24-S4 (the change-management path wall, an issuer defect the COO owns), **W24-S5** (AC1's `<expect>` regex
`[2-9]\d*` cannot match a writer census of 17 -- the regex-shaped criteria class again). rk-2's order at HEAD still carries 6
criteria and neither `lib/research/rules/` nor `org/critical_paths/change_management/`: the re-cut ruled at 23463 (AC7
non-regression census over the 11-route table, AC8 packaging census, the two grant widenings, module-relative lazy reads, the
data files committed with provenance) is the issuer's next act before `~24`'s successor spawns, with W24-S5's regex in the same
amendment.

## Open calls in scope

| call | class | state |
|---|---|---|
| ESCALATION 23462 | ADJUDICABLE | RULED (co-sign AMENDMENT 2 @`aa97d2ea9f`); rollback VERIFIED; CLOSED this tick |
| 23440 · S120 · S124 · S125 | ADJUDICABLE | RULED and APPLIED; closed |
| CARD 1 (model-block + price pull) · CARD 2 (filings spend; S127 if it calls the vendor) · CARD 3 (portal DEV push) | RESERVED, cited | at Andrew; CARD 3 via `0.0.0_AB_MSTR~Z` |
| SITEZ push / merge leg (LD-0522) | RESERVED | `0.0.0_AB_MSTR~Z` on his word |

No new call this tick. Five adjudicable this session, five ruled, five applied or executed.

## Who owes what

`2.0.0_SA_COO~Z`: rk-2's re-cut + W24-S5 repair + the `~24` successor; W24-S3 disarm; rk-8 on chain A (rk-2's redeploy is no longer
the gate for the page's build, which passed on rk-1); rk-6 after rk-2 drains (its fresh co-sign first); S127's egress measured;
drains; the L8 packet. `3.0.0_SA_CVO~Z`: L8/L9 as completions land (7 terminal now). `0.0.0_AB_MSTR~Z`: CARD 3 + the SITEZ push at
Andrew. This seat: the CTO half of rk-6's co-sign when the COO asks (blast radius = all 11 routes, per AMENDMENT 2); the L10 when
the slug lands.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `.tools/aws lambda get-function-configuration` | sha `9ubWPnhz`, 16:18:57Z | the restore, on a second instrument |
| direct GET x2 (boto3 invoke) | 200 / 200 | the regressed routes, restored |
| ledger entry read + `git log -1` | CLOSED 16:22Z @`817d827e39` | 5 of 5 legs with proof |
| order + channel re-read (python) | rk-2 6 criteria, no rules/ path; W24-S3 ARMED at the COO | the re-cut is still owed |

**Gap found:** none new. The regex-shaped criterion (W24-S5) is the fourth instance of one class this round (rk-8 `:r,`, rk-3 AC3's
body shape, rk-12 AC1's route regex, now rk-2 AC1's `[2-9]\d*`); the issuer's dry run catches what workers reach, and a checker
that grades "regex decides" needs the regex itself run against the expected value at the cut -- carried to the L10 as a
criteria-grammar finding for the round-13 battery.

Push state: **LOCAL on SITEZ.** LD-0522 puts the push with `0.0.0_AB_MSTR~Z`; none requested.
