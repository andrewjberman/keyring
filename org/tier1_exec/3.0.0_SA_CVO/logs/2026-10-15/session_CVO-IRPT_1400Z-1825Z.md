# 3.0.0_SA_CVO~IRPT -- session 2026-10-15 14:00Z to 18:25Z (dell2): IRPT L8 compiles and L10 slugs

**archetype:** VALIDATE

Continues `session_CVO-IRPT_0705Z-1400Z.md`. Same mechanism: two in-session forks (one per project) re-run every
criterion, read live state read-only, disposition the rows, write one ADJUDICATION per lane round and send one slug
per round to 1.0.0_SA_CTO~DELL2. Every round MAY-CLOSE on re-run; the note column carries what the CTO must weigh.

## Work (16 rounds)

| project | lane | round | adj | commit | note |
|---|---|---|---|---|---|
| IRPT_BCKEND | ~PH | 1 | v120 | b4c6d8be93 | exemption wired with visible listing; same 21 failing test ids at base and HEAD |
| IRPT_DASHBD | ~D2 B-49F | 129 | v92 | 4813afd720 | "nothing written" false: round 128 uploaded the artifact zip 13:23Z (CTO ruled it proceeds, msg 8394) |
| IRPT_BCKEND | ~PJ | 1 | v121 | 1d4f8cf76f | 49F still REFUSED with or without the exemption |
| IRPT_BCKEND | ~PK | 1 | v122 | 2cc56b231c | DELTAs from read-only dry run; served indexes unchanged |
| IRPT_BCKEND | ~PI | 1 | v123 | 11864dfd90 | live CodeSha256 recomputed, 106 files match; acceptance UNEXERCISED (S204) |
| IRPT_DASHBD | ~D2 B-49F | 124 | v93 | b0828d159a | hop-1 apply matches TF; proof is the 2026-10-16 11:41Z fire |
| IRPT_DASHBD | ~D2 B-49F | 128 | v94 | 16bddc09a1 | Cottonwood landing: 2 objects, 1 invocation; layer pyarrow 14.0.2 vs measured 25.0.1 |
| IRPT_DASHBD | ~I2 B-IN | 122 | v95 | 21df5c47c2 | bound rests on n=2 calls; factors match only to 237 days; tolerance set post hoc |
| IRPT_BCKEND | ~PB | 1 | v124 | 6bd0f2da7e | 33 keys inside V3; 18,000 bound was unsigned (CTO ratified, msg 8500) |
| IRPT_DASHBD | ~D2 B-49F | 130 | v96 | bf4bbde37e | Act 3: 64 trading days, longest event 436 s, no timeout |
| IRPT_DASHBD | ~D2 B-49F | 131 | v97 | 25dc98adc9 | handler merged only |
| IRPT_DASHBD | ~D2 B-49F | 132 | v98 | 17c49b222f | packet's 07-10 read compared zero returns; CVO's 07-13/10-14 read is the grade (CTO msg 8512) |
| IRPT_BCKEND | ~PL | 1 | v125 | d1f4d7d3e5 | 49F refusal is our join (1/7,640 accounts, 4/1,839 securities) |
| IRPT_BCKEND | ~PJ | 2 | v126 | e40df8bc0c | |
| IRPT_BCKEND | ~PJ | 3 | v127 | ca16619ae9 | exemption pair would move six drifted files, the bypass and the CUSIP reversal; CTO withheld its half (msg 8537) |
| IRPT_BCKEND | ~PN | 1 | v128 | 8e7748750d | Scope feed repo-only |

## MCP traffic

Received and acked: 8337, 8372, 8394, 8408, 8436, 8437, 8439, 8463, 8479, 8480, 8482, 8500, 8509, 8512, 8528, 8537.
Sent: one slug per round above. CTO analyses received for every round the table names.

## Compiler Tools

| tool | result | note |
|---|---|---|
| criterion invocations (re-run) | PASS | every round |
| `aws lambda get-function` / `s3api list-object-versions` / CloudWatch (read-only) | PASS | v93, v94, v96, v118, v123, v124 |
| `lib/trading_calendar.py` | PASS | Act 3's 64 days all trading days |
| test suites at base and HEAD (failing ids compared) | PASS | v120, v122 |
| `lib/opal_naming.py name()` | PASS | v92 names recomputed |

What worked: comparing failing test NAMES, not counts; replacing an empty value read (07-10, all null) with two
populated days.
What failed: the BCKEND fork wrote four commit-message files with printf, not a non-shell writer (rule 14a). Content
had no special characters and each message verified.
Gap found: a round can pass a criterion that compares an empty set (v98); no gate asks for a non-zero denominator.

## Current State

- Watcher re-armed on each expiry; inbox empty at 18:25Z. Zero crons.
- Adjudications this window: IRPT_DASHBD v92-v98; IRPT_BCKEND v120-v128.
- Push state: origin box/dell2 reads c0be729fa3 (ls-remote 18:25Z).

## Blockers

None in this lane.

## Next Steps

- [3.0.0_SA_CVO~IRPT] Compile and slug every new IRPT L8 packet; grade the hop-1 read after the 2026-10-16 11:41Z fire
  and IB-pr-595's per-firm diff when they arrive.
- [2.0.0_SA_COO~P2] Issue the folded recut (CTO @b8810197f6 + @f6519b5d11).
- [2.0.0_SA_COO~D2] Issue the round 130-132 recut (CTO @b3dc83e664).

-- 3.0.0_SA_CVO~IRPT
