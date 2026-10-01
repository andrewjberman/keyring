# Amendment 5 (c)-(h) implemented and the calibration re-measured: the 214x tolerance tail and the -91% return tail were both instrument artifacts, and they are gone -- 0.4.0_DS_ClientPlatform~S

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Date:** 2026-10-01 06:20Z to 07:30Z
**Task Order:** `IRPT_DASHBD.TO-DB-b-1` (pending), amendment 5 @`f4f57b6fe4` + amendment 6 @`34ae583549`
**Status:** IN PROGRESS -- (a)-(h) in the producer; the `guard_state` contract proposal and the emit remain
**Workspace CLOUD commits:** `fab8294675` (rulings 20-21), `8fbdd5a183` (c, d), `3e36bdde2e` (f, g),
`7096c354c2` (e), `6be02af162` (h + derived ceiling). All LOCAL; origin/CLOUD `0abf99fcd4`.

---

## Objective

Amendment 6 said "nothing is waiting on this seat: proceed with (c)-(h)." Nine clauses of method
text, each correcting the order against the PRD it names. Implement them and re-measure.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| commit-gate | 9 runs across the edits | PASS | clean each time |
| safe-commit + naming/surprise/missions gates | 5 commits | PASS | see the defect below |
| comp-read `--enumerate` | on the order and the producer | PASS | |
| comp-find word-boundary census | the proposed `guard_state` members | IN FLIGHT | 6 sequential full-corpus scans; slow by design |

**What worked:** verifying each clause by the CLAIM it makes rather than by the code running.
Four of the six clauses had a number that could only come out right if the implementation was
right, and one of them (e) matched an independently computed figure to six decimals.

**What failed -- MY OWN TOOLING DISCIPLINE, twice:** a `safe-commit` wrapped in a `| tail` pipe
reported nothing useful and the commit did NOT land, both times. The pipe swallowed the result and
I read the hook's reminder text instead of the outcome. CLAUDE.md already forbids composing a
report of an act in the same call as the act, and I did it anyway. Caught both times only because
I asked the REPOSITORY (`git log -1`) rather than the tool. From here: `safe-commit` runs alone,
output to a log, verified with `git log`.

---

## Work Completed

### Rulings 20-21 (`fab8294675`)

ONE short-position member, because `leveraged` and `negative_value` selected the same 390 rows
element for element -- two members of one axis that cannot disagree (Rule 24 (ii)/(iii)). Both
signals are still read, so a future divergence still means a short is present; a row where both
are absent returns NO_COVERAGE rather than being read as "no short".

Ruling 20's census: per account, short-position days whose flow exceeds the tolerance. **I had to
correct my own first report of this number** -- see below.

### (c) The account boundary (`8fbdd5a183`)

`F_t` is now every CASH leg that crosses the MEASURED account: class EXTERNAL, plus a leg resolved
INTERNAL by pair-match or text-counterpart. A same-account-type-transfer stays out. Provenance is
recorded where it is DECIDED, because the class alone cannot answer an account-grain question.

**A missing stage, found while wiring it:** `_TEXT_COUNTERPART_RE` was defined at module level and
NEVER APPLIED. A compiled regex that nothing calls reads exactly like an implemented stage.
Implementing it moves no money -- every leg it claims was already reaching `F_t` as
external-by-default -- so only the route label changes.

**And I got the stage ORDER wrong on the first cut.** I put text-counterpart before the pair
matcher; measured on `date=2026-09-25` that drove `resolved_pair-match` to ZERO while
text-counterpart took 7 legs. No money moved, but the census the issuer reads to judge the matcher
would have reported that the matcher never fires. Pair-match OBSERVES a matching leg; text-counterpart
reads a number out of free text. Reordered: pair-match 8, text-counterpart 1 on the same partition.

### (d) The fee basis (`8fbdd5a183`)

FEE-MANAGEMENT enters `F_t` as capital out, which makes `V_t - F_t` ADD THE FEE BACK -- what turns
the arithmetic gross of advisory fees, as `fee_basis GROSS_ONLY` always claimed. FEE-ADMIN stays
inside the return.

**Verified by the claim, not the sign**, on `date=2026-07-10`, two runs differing only in whether
the fee leg is admitted, 69 accounts affected: gross < net on **0**, gross > net on **69**. The two
largest are the defect class itself -- `0074251873` reads `r_NET` **-0.99995919** and `0018374770`
**-0.98749658** against `r_GROSS` **0.00000000** for both. A fee emptying a closing account was
being served as a 99.996% performance collapse.

### (e) Valuation intervals (`7096c354c2`)

The return is compounded across every custodian valuation in `(t-1, t]`: intervening POSITIVE
valuations in order, then day t whatever its value. With no intervening valuation the chain is
`[t]` alone and this reduces EXACTLY to the endpoint formula, which is why it is inert on an
ordinary day. The valuation day set is BALANCE partitions, not transaction partitions -- conflating
them is how a closed day's deposit reached the wrong interval.

**Verified against an independently computed figure**, account `0093614544`, 2025-01-10:

| | |
|---|---|
| 2025-01-09 is a custodian BALANCE day | True |
| 2025-01-09 is a TRADING day | False |
| V(01-08) / V(01-09) / V(01-10) | 1,995,191.90 / 3,120,191.90 / 3,114,480.00 |
| sub-period flows | `[('2025-01-09', 1,125,000.00), ('2025-01-10', 0.00)]` |
| **linked r_t** | **-0.183062%** |
| review's linked figure | -0.183062% (six decimals, matched) |
| review's endpoint figure | -0.286283% |

This is the arithmetic half of `IRPT_BCKEND-S237`, where the retiring engine read the same deposit
as +56.10%. That row's SERVED remediation is still the issuer's.

### (f) Unknown input is a sized state; SOURCE_LAG emitted at last; durable inception (`3e36bdde2e`)

The unknown-cash record carries `{rows, abs, malformed}` rather than a count, because the issuer's
rule is a BOUND and a count cannot answer it -- one unknown cent and one unknown million are the
same count. Malformed is UNCONDITIONAL: an unparseable amount has no value to compare against the
tolerance and contributes 0.00, so letting that 0.00 clear the bound would be the `fillna(0.0)`
defect one level up.

`SOURCE_LAG` is emitted for the first time (an ABSENT transaction partition, separated from one
that exists and is empty). The state was declared in `DAY_QUALITY` and produced by nothing.

Inception is now the ACCOUNT's, via `first_data_dates()` over the whole history up to the request
end. **Verified, with the order as the control:** durable inception for the six is 2024-07-08,
2026-03-16, 2026-03-26, 2026-07-08, 2026-03-19, 2026-05-18; a window-local scan over 2026-09-21..25
returns 2026-09-21 for **all six**. The five roster accounts span 2026-03-16..2026-07-08, and
ISSUER AMENDMENT 1 independently recorded "first positive value 2026-03-16 .. 2026-07-08" before
this function existed. Matching an externally recorded range exactly is evidence the scan is
right, not merely that it runs.

### (g) Foreign tax (`3e36bdde2e`)

A WD row is excluded from `F_t` as well as income, whatever class the shared table gives it -- it
had to be, because that table marks FTP/FC/WD and FTR/FC/WD EXTERNAL, so a tax payment was
entering `F_t` as a withdrawal and a reclaim as a deposit. Verified on `date=2026-07-09`: 69 rows,
$860.34, all 69 classed EXTERNAL, now out of both terms. The shared table is NOT edited -- CRO's
file, served engine reads it.

### (h) The re-measure and the derived ceiling (`6be02af162`)

Full history over the six accounts.

| | quarantined (contaminated) | re-measured |
|---|---|---|
| tolerance | 0.010677 | **0.001244** |
| tolerance max | **214.579843** | **0.012024** |
| large_flow_share | 0.000001 | **0.002535** |
| observed r p0.1 | **-0.912047** | **-0.091352** |
| observed r p99.9 | 0.044193 | 0.044193 |

**The upper tail is unchanged and that is the control.** F01 inflated flows, so it depressed
returns and could only have moved the LOWER tail. A repair that had moved both tails equally would
have been suspicious rather than reassuring.

Derived ceiling (amendment 6): `tolerance / max(|band|)` = 0.001244 / 0.5 = **0.002488**, barring
**8 of 1,098** account-days (0.73%), counted separately from the short-position member because a
day can fail both. Denominators: 1,098 account-days with a neighbour, **708** inside the domain --
the 390 difference is exactly the short-position population.

---

## The correction I owe on ruling 20's count

I reported **0 of 390** short-position days with a flow above the tolerance. On the full history
with the re-measured tolerance it is **5 of 390**. Both figures are right for what they measured:
the first was a narrower window (2026-03-01..09-28) under a looser tolerance (0.00307), the second
is the full history at 0.001244. A tighter tolerance necessarily admits fewer days, so the number
had to rise. 5 of 1,105 account-days is 0.45%, so the CTO's trigger -- "if it is large, a daily
instrument over the SIGNED basket is the next enrichment" -- is still answered NOT LARGE.

**The lesson is the one already on this channel twice:** I quoted a number without its window. A
figure measured over a different population and a different threshold is a different figure, and
the denominator beside it is what makes that visible. It was visible here only because I re-ran it.

---

## Blockers

None at this lane. The `guard_state` 0.2.0 contract proposal is in flight (its token census is
running); the emit then needs the issuer to land the contract, since `org/standards/` is lane
ANY_EXEC (row S2).

---

## Current State

The producer implements amendment 5 (a)-(h) and PRD rulings 17-21. It refuses an emit three ways
(no thresholds, a SUPERSEDED thresholds file, no comparability ceiling), never substitutes a
different population's return, grades only inside a measured domain, checks the value it emits,
reads no unknown as a zero, links through real custodian valuations, treats an advisory fee as
capital and foreign tax as neither, and derives its inception from the account rather than the
request. Row S3's quarantine is lifted by the (h) pass. Nothing is in S3; the ledger is not opened.

---

## Next Steps

1. **[`0.4.0_DS_ClientPlatform~S`]** The `guard_state` 0.2.0 contract: five proposed members with
   the rule-24 four-postulate record and the token census; written UNCOMMITTED for the issuer.
2. **[`2.0.0_SA_COO~P`]** Land the 0.2.0 contract (lane ANY_EXEC) and the three remaining round-1
   checks (the guard check already self-tests 11 of 11).
3. **[`0.4.0_DS_ClientPlatform~S`]** Then: open the change-management ledger, emit, grade
   `DB-1-AC1`/`AC2`/`AC3`, then `TO-DB-b-3`.
