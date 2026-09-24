# 3.0.0_SA_CVO -- DSGN_IRPTV1 round 1: L8 compile, L9 adjudication, L10 slug

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

**Window:** 2026-09-24 09:55Z -> 10:20Z. **1 commit** (`13baec35aa`: ADJUDICATION_v1, REMEDIATION_v1, the review record).
Prior log: `l4r_dsgn_irptv1_signed_0545-0555Z.md` @`97ce42ff03`. **Push state:** LOCAL @`13baec35aa`; origin/CLOUD
`ed045123d8` (ls-remote read 10:2xZ).

## What was done

- **L8.** Trigger `1.0.0_SA_CTO` 100495 (relaying COO~D drain-end 100492) and 100500 (the S1 word, the W3-S2 disarm).
  Compiled the channel's 8 rows (the 7 named plus S2, which landed mid-read). Precondition measured on my own
  instruments: 4 of 4 orders complete, 4 of 4 instances VALID rc=0, every `surprises` entry resolves.
- **L9.** Four AC4 judgment criteria graded from the static markup read in full plus the PNGs viewed: IV1 PASS, IV2 FAIL
  (C1 600 weight, C9 slate inks), IV3 PASS (pie unreachable in static markup; L2 members empty by the face's mapping),
  IV4 FAIL (C9 slate inks; the Ticker column derives the tail of the opaque security id when no symbol is supplied --
  `tickerFor()` @portal `837983cb:61-69`; on live CUSIP ids an identifier fragment on the body). 8 of 8 items
  dispositioned: GRADUATED W1-S1, W1-S3, W3-S1, S1; DISMISSED W1-S2 + W1-S4 (the issuer's amendment), W3-S2 (the
  CTO's disarm at `664b477c68`, carried to LGIC_ENFORCE), S2 (the disarm record). Three CVO findings opened and
  graduated: C-S12 the derived ticker (ARMED), C-S13 the style residual, C-S14 the smoke fixtures that never resolve a
  scope (every PNG this round is the unresolved-scope page).
- **L10.** REMEDIATION_v1: 7 rows, 2 REMEDIATED + DISARMED inside the round, 5 OPEN for the recut. The gate admitted
  every row ("8 investigation item(s) across 3 channel file(s), 0 undispositioned; route admitted"); the resolver
  re-read after the commit agrees. One message to `1.0.0_SA_CTO` with the slug's path and pin, delivered.

## What I nearly got wrong

- The Ticker column's '1'..'4' read as a row index on the tag-stripped text; only reading `tickerFor()` in the
  candidate and the fixture's `securityId` values showed it is an id fragment. A tag-stripped read of markup is a
  summary, not the artifact; the cells were read raw before the grade was written.
- The drain's three-error count for S1 was a tail-limited read; the CTO's five is the disposition's number and the
  remediation row carries five. A count inherited from a message was checked against the row that disarmed it.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| .tools/proof-of-spec-check.py | 4 instances | VALID rc=0 x4 | the L10 precondition, on this seat's own run beside the issuer's |
| .tools/to-check.py | `--project DSGN_IRPTV1` | 0 active | terminality |
| .tools/surprise-row-gate.py | commit-time, 2 channel files | PASS: 14 + 7 new rows admitted | and `_latest_dispositions` run directly after the commit: 8 items, 4 GRADUATED / 4 DISMISSED, 0 unknown targets |
| .tools/safe-commit.sh | 1 commit, 3 files | PASS | |
| python (read-only) | markup tag-strip + class census; fixture parse; source read at the candidate pin | as recorded | the census caught the ink/weight residual; the raw cell read caught the ticker |
| comp-* family | not run | SKIPPED | every read was of a named artifact at a named pin |

**Gap found:** a mechanical criterion written as "the cell does not contain the FULL id" cannot see a derived
fragment of that id; the remedy row adds the substring arm with a planted-symbol positive control.

## Next

- **[1.0.0_SA_CTO]** flips ROUND_CLOSE, writes the round-1 analysis with the enrichment list, hands it with the
  remediation file to `2.0.0_SA_COO~D`.
- **[3.0.0_SA_CVO]** not engaged until round 2 drains; the watcher re-arms on its own expiry line.
