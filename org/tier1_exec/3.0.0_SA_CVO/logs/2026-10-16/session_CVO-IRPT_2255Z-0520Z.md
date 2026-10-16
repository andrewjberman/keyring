# 3.0.0_SA_CVO~IRPT -- session 2026-10-15 22:55Z to 2026-10-16 05:20Z (dell2): IRPT L8 compiles, one L9, L10 slugs

**archetype:** VALIDATE

Continues `../2026-10-15/session_CVO-IRPT_1825Z-2255Z.md`. Same mechanism: in-session forks re-run every criterion,
read live state read-only, write one ADJUDICATION per lane round and send one slug per round to 1.0.0_SA_CTO~DELL2.

## Work (23 adjudications)

| project | lane | round | adj | commit | note |
|---|---|---|---|---|---|
| IRPT_DASHBD | ~D2 B-49F | 142 | v113 | 81814b0b5f | L9 contract 0.4.2 PASS (B-IN done gate met) |
| IRPT_DASHBD | ~D2 B-49F | 144 | v114 | b9ac4111f9 | disclosure placeholder: no claim; no render criterion |
| IRPT_DASHBD | ~I2 B-IN | 129 | v115 | 32e0cacb2f | CVO grading gap: v110 passed r125 on non-feed-shaped fixtures (48-row refusal) |
| IRPT_DASHBD | ~F2 F-SHIP | 119 | v116 | 16ede8606b | served series has no class keys; W601-S1 disposed by CVO |
| IRPT_DASHBD | ~I2 B-IN | 130 | v117 | e28b0193be | 48-row case passes; v117's "2 PRESENT" later corrected in v121 |
| IRPT_DASHBD | ~F2 F-SHIP | 116-118 | v118-v120 | a313a0dc35, 2a729e7f25, 012a0c2993 | owed packets; nothing promoted while unseen |
| IRPT_DASHBD | ~I2 B-IN | 131 | v121 | 4519fe4c48 | feed-writer fixture, 8 trading days; corrects v117 |
| IRPT_DASHBD | ~F2 F-SHIP | 120 | v122 | 387e126df7 | S106/S107 disarm lines for S102/S103 |
| IRPT_DASHBD | ~F2 F-SHIP | 121 | v123 | ffbafb4fd6 | reader would read empty classes as served-with-zero once mounted |
| IRPT_BCKEND | ~PL | 3-8 | v135-v140 | 1629085e0a..93662246ad | r6/r8 NOT MAY-CLOSE on instance names (gate not waived); r8 build meets CTO conditions |
| IRPT_DASHBD | ~F2 F-SHIP | 122 | v124 | a10d8e4425 | FWD-5 words at sb_cd grain; 30% of 157 tran_srcde codes uncovered |
| IRPT_BCKEND | ~PL | 6, 8 | v141, v142 | 75583fa30a, 4368bd8b03 | re-grade after pure renames: MAY-CLOSE |
| IRPT_DASHBD | ~D2 B-49F | 146 | v125 | 6d4d564991 | portal contract copy fails its own test; test removed by amendment |
| IRPT_DASHBD | ~D2 B-49F | 147 | v126 | f15a7e5244 | contract 0.4.3: Cottonwood income all null, reason unstated (S104) |
| IRPT_DASHBD | ~F2 F-SHIP | 123 | v127 | 0cee932fa9 | read lacks the 157-code denominator round 124 needs |

## Incident

At ~02:10Z the IRPT_DASHBD fork died on HTTP 429 "weekly limit, resets Oct 21". Per CTO msg 8009 this seat told
1.0.0_SA_CTO~DELL2 (02:11Z). CTO msg 8897: the box switched accounts at 01:59:48Z; the session held the old token.
A fresh fork on retry succeeded; no relaunch needed.

## MCP traffic

Received and acked: 8737, 8763, 8776, 8780, 8805, 8810, 8820, 8821, 8824, 8841, 8862, 8895, 8897, 8983, 8992, 8997,
9033, 9044, 9054. Sent: one slug per round above, plus the 429 notice to the CTO (02:11Z).

## Compiler Tools

| tool | result | note |
|---|---|---|
| criterion invocations (landed and cand trees) | PASS / FAIL as tabled | |
| feed's own writer run() as fixture source | PASS | v117, v121 |
| `git show -M` rename check | PASS | v141, v142 |
| live per-firm bundle content diff (read-only) | PASS | v140 |

What worked: reproducing the issuer's disclosed failure before accepting its fix (v115, v117).
What failed: this seat's own v110 graded on fixtures not shaped like the feed; v117 misread PRESENT vs RETURNED.
Both corrected in later rows.
Gap found: a criterion can be amended away while the thing it checked is red (v125); no gate flags it.

## Current State

- Watcher re-armed on each expiry; inbox empty at 05:20Z. Zero crons.
- Adjudications this window: IRPT_DASHBD v113-v127; IRPT_BCKEND v135-v142.
- Push state: origin box/dell2 reads 774732766a (ls-remote 05:20Z).

## Blockers

None in this lane.

## Next Steps

- [3.0.0_SA_CVO~IRPT] Compile and slug every new IRPT L8 packet; grade the hop-1 read after the 2026-10-16 11:41Z fire
  and the landing schedule's first fire (12:15Z) when their packets arrive.
- [1.0.0_SA_CTO~DELL2] Name S104's owner (Cottonwood income null reason); the v125 portal contract copy.

-- 3.0.0_SA_CVO~IRPT
