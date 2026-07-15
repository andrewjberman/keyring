# OPAL_TAXSMA — SSAVAIL Content Contract v1.0

**last-verified:** 2026-07-15 (derived from the FULL received corpus: 35 files, 2026-04-06 ->
2026-07-15, profiled server-side via `profile_site_file`; every claim below held on 35/35 —
denominator complete, not sampled). Authority: Andrew-direct #8 (verbatim: ANDREW_DIRECT_20260715
TO, ADDENDUM #8). This contract is what intake VALIDATES against; a file that breaks it is
FLAGGED at intake, never filed canonical.

## The format (FIS SmartLoan short-sale availability, feed 0164)

Fixed-width mainframe layout. Three record types by first character:

```
pos 1     record type: 1=HEADER, 2=DETAIL, 3=TRAILER
HEADER : "1" + "0164" + " " + YYYYMMDD(as-of) + spaces->200
DETAIL : "2" + cusip(9) + " " + cusip(9) + " " + 6 x signed-18-digit qty/rate fields + spaces->200
TRAILER: "3" + "0164" + 15-digit zero-padded RECORD COUNT (== TOTAL lines incl. header+trailer) + spaces->200
```

## Invariants (each one is an intake CHECK; violation => FLAG)

| # | Invariant | Corpus evidence | Flag class |
|---|---|---|---|
| C1 | Every line exactly 200 chars | mode_pct=100.0 on 35/35 | STRUCTURE |
| C2 | Pure ASCII, UTF-8 decodable | non_ascii=0 on 35/35 | STRUCTURE |
| C3 | Line 1 is a `1`-record, feed id `0164` | 35/35 | STRUCTURE |
| C4 | Header as-of date == PRIOR TRADING DAY of the email date (trading-calendar exact — proven through Good Friday 04-03 and July-4th-observed 07-03) | 33/33 non-stub + stubs also carry correct as-of | DATE |
| C5 | Last line is a `3`-record whose 15-digit count == exact total line count | 35/35 tie, including stubs (count=2) | CHECKSUM |
| C6 | All interior lines are `2`-records | 35/35 | STRUCTURE |
| C7 | Detail count within the volume envelope: full files ran 53,484–77,045 lines (10.8–15.6 MB) over Apr–Jul 2026. Check: total lines in [40,000 .. 100,000] hard; WARN outside trailing-20-file p5/p95 | see failure modes | VOLUME |
| C8 | Same-day FINAL(SSAVAIL2) line count >= PRELIM(SSAVAIL) count | 10/10 same-day pairs (delta +959 .. +18,404) | VOLUME |
| C9 | digit_ratio ~0.55 for full files (0.08 = header/trailer-only) | 35/35 | STRUCTURE |

## The two proven failure modes (both FIS-side, both now mechanically detectable)

1. **STUB** — 404-byte file: header (correct as-of) + trailer(count=2), ZERO details. Observed
   4x (06-30 both sends, 07-01 early, 07-10 early); same-date stubs are byte-identical.
   Detection: C7 hard-fail (trailer count == 2). Disposition: file as `{base} {DATE} STUB.ASC`,
   never canonical; expect a corrected re-send later the same day.
2. **TRUNCATED-VALID** — the dangerous one: 07-01 6:47 FINAL had 14,152 lines with a TYING
   trailer (FIS truncated at generation, so its own checksum passes) at ~22% of envelope.
   ONLY C7 (volume envelope) catches this class. FIS re-sent complete (67,236) at 8:20.
   Disposition: FLAG; prefer the fuller same-date re-send pending human word.

## Corpus census (email-date: PRELIM lines / FINAL lines; header as-of in parens)

```
04-06..08, 06-05, 06-24..25 (Yang manual, FINAL only): 61356(0402) 53484(0406) 64341(0407)
                                                        58125(0604) 72856(0623) 73928(0624)
06-29: 64615 / 65690 (0626)      07-08: 66726 / 70117 (0707)
06-30: STUBx2 -> 64665 / 66585 (0629)  07-09: 55912 / 74316 (0708)
07-01: STUB; 14152 TRUNC vs 67236 re-send (0630)  07-10: STUB -> 61712 / 60876; re-send 61685 (0709)
07-02: 58640 / 59895 (0701)      07-13: 62831 / 64234 (0710)
07-06: 57750 / 58749 (0702)      07-14: 71887 / 77045 (0713)
07-07: 59346 / 60311 (0706)      07-15: 62843 / 64030 (0714)
```
Note 07-10: the 8:10/8:14 re-sends carry MORE rows than the 6:47 send (61,685 vs 60,876) —
re-sends are UPDATED SNAPSHOTS, not byte-replays. EXTRA files are never discardable unseen.

## Yang-intent audit (his spec vs the evidence — per the directive, not beyond reproach)

- "two emails every morning": TRUE on 8/12 backfill days; FALSE on re-send days (3 and 4 sends
  observed). Arrival-order naming would have filed a 404-byte stub as canonical 3x in 12 days.
- Naming by receipt date while content is as-of prior trading day: CONSISTENT and now an
  exploitable invariant (C4) rather than an ambiguity.
- His manual practice (FINALs only, sparse dates) under-captures vs his own spec; automation
  follows the spec (both files daily) pending his word.

## Adjudication now content-resolved (for Yang, one item)

07-01: the canonical `SSAVAIL2 20260701.ASC` (6:47) is the TRUNCATED-VALID 14,152-line file;
`SSAVAIL2 20260701 EXTRA-1.ASC` (8:20) is the complete 67,236-line snapshot of the same as-of
date. RECOMMENDATION: swap on Yang's confirmation (rename EXTRA-1 -> canonical, canonical ->
` SUPERSEDED`). Not executed — the no-silent-swap rule holds until his word.

## Implementation map (the guardrail build this contract drives)

- `validate` step in intake: checks C1-C9 server-side (gateway `profile_site_file` output +
  trailing envelope state); verdict PASS -> file canonical; FAIL -> `TAX/Short Sale/Flagged Files/`
  + loud report. Alyssa's runs become verdict-consuming, never judgment-producing.
- Run log: one JSON/markdown line per intake run to the shared SharePoint location + repo record.
- Python-compiled flag report: regenerated per run; establishes flagged features per file
  (stub-by-size, volume-envelope breach, date mismatch, checksum break, structure break).
- Daily schedule: architecture decision with Andrew (EventBridge-driven vs operator cadence).
