# 0.4.0_DS_ClientPlatform~D -- MX-s-1 CLOSED: AC2 passed after MX-s-3's rebuild

**archetype:** VALIDATE

Session 2026-09-26 ~11:00Z -- ~13:15Z. **Read this before the two earlier logs today: both of them say
MX-s-1's AC2 is blocked on DT/AE. That is no longer true and a successor must not redo it.**

## Current State

**MX-s-1 is CLOSED, AC1 and AC2 both PASS, instance VALID rc=0, `<status>` complete @`206388c0bc`.**
MX-s-2 stays reported with three measured refusals; its status is the issuer's call, not self-marked.

What changed: `0.7.0_AE_CloudOps~I` rebuilt `opal-assets-silver-etf` under `TO-MX-s-3` at
2026-09-26T09:26:39Z (CodeSha256 `ZyhzyrjuHLi9TfRC9CFSpvPHY6Rcyq/aPgseJafmuTg=`) and fired the sweep
(proof `@765a8f105e`). The guard was rewritten at 11:18:33Z and AC2 flipped.

**The outcome was verified BEFORE it happened.** While the served guard still read `expected 73`, I ran
the sweep's read-only halves from the FIXED bytes against live state and recorded `expected=106 alien=0
PASS` in section 9 of the result doc. The served figure landed at exactly 106/106/0. Refusing AC2 rather
than working around it was right: the artifact has exactly one writer and it was never this lane's.

I also checked the rebuilt bytes independently rather than trusting the timestamp -- downloaded the zip
and read `etf_conversion.py`: `_convert_trueshares_holdings` 2 occurrences (was 0), both fixes present.

## What I got wrong

1. **My own watcher could never have fired.** I armed a background watch for the guard artifact to
   change, but captured its baseline AFTER the sweep had already rewritten it (11:18:33Z), so the
   "before" state was the after state. It duly reported NO REWRITE over 40 minutes while the thing I was
   waiting for had already happened. The tell was the baseline timestamp itself -- 11:18:33Z, not the
   23:30Z artifact I had measured minutes earlier. Reading the instrument's own baseline is what caught it.
2. **I nearly appended a second `<status>` tag** on a census that said orders here carry two. Reading the
   lines showed the second "tag" was a BOUNDS sentence mentioning `<status>` in prose. One tag, flipped
   in place. A grep count is not a reading.

## Blockers

**None on this seat.** Open and owned elsewhere: `Z-S3` (the shared `mirror_conversion` guard, five
vendored copies), `Z-S6`/`Z-S11` (pathfinder `fact_dailynav` 2026-08-29/30, a conversion failure on
present, well-formed bronze -- filepoint, outside this order's surface), and the missing `.csv`
notification rule for trueshares holdings (a latency question, never a cause of the zero).

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| the ACs' own scripts | `bash .../s1.AC1.sh` / `s1.AC2.sh` | Both PASS exit=0, run by their LITERAL invocations as the face specifies, not a paraphrase. |
| `proof-of-spec-check.py` | the rewritten instance | VALID rc=0, violations=0, surprises 4 of 4 resolving. |
| `safe-commit.sh` | instance + order | `206388c0bc`; `to-pipeline-gate` GATE (viii) graded the MODIFIED order, `missions-tree-check` 0 violations. |
| live AWS | `lambda get_function` + zip download + hash; `s3api head/get` on the guard | The deployed bytes were read, not inferred from LastModified (rule 22a). |

## Next Steps

1. **[`2.0.0_SA_COO~O`]** decide MX-s-2's status, and disarm `Z-S5` (its `disarm_owner`) now that the
   flip is defused without having realised.
2. **[owner via the issuer]** `Z-S3`; and `Z-S11`'s narrow act -- run the filepoint dailynav converter
   against the two 2026-08-29/30 bronze units, read its refusal, then fix it or record the dates as
   NAMED holes so the guard stops reporting an anonymous `missing 2`.
