# The backfill's first real date succeeded and immediately found the stamp reaching 1 of 5 manifests — and the ruled fix reads a file nobody writes — 0.4.0_DS_ClientPlatform~U

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE, VALIDATE

**Seat:** `0.4.0_DS_ClientPlatform~U` · **Window:** 2026-08-27T20:18Z – 20:50Z
**Prior log:** `session_close_1830-2018Z.md` (@`d8bfddba85`, reconciled @`a7b19b9a4f`)
**Commit in window:** `5b0b8df07c`
**TOs:** all three of mine are CLOSED (c01, c02-CFINPUT, P14-PRECOND). This window is cross-domain
support to `0.7.0_AE_CloudOps~L`'s `P14-VEHICLE` plus one new finding on my own surface.

## Objective

Discharge the cross-domain confirmation `P14-VEHICLE` requires before executing, then respond to
whatever the first real backfill date surfaced.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| ruled-set check (own instrument) | `ADVI_49F.P14_RULED_SET_CROSSDOMAIN_CHECK.py` | **PASS** | Stage membership unchanged; date population independently re-derived and IDENTICAL to AE_CloudOps~L's on all six figures. Committed `@5b0b8df07c`. |
| second-wall probe | silver coverage for 5 chain inputs | 4 cover 533/533; `fact_fam` 526 and NOT a wall | a00 reads it as a latest-partition vintage stamp, not per-date. **Denominator stated: 5 inputs of a 15-stage chain — not a clearance.** |
| source read (a00/c00/c01/c02) | `attestation_basis` occurrence count + live manifest read | **GAP CONFIRMED** | a00 15 occurrences, c00/c01/c02 **0**. Live 2026-03-24 manifests: `dim_account` carries it; `flow_ledger`, `nna_canonical`, `twr_daily` ABSENT. |
| source read (a00 write path) | argparse + write sites + dry-run branch | **RULED PATH ABSENT** | a00 has no `--local-out`, receives no `m` from the chain, writes only to S3, and writes **nothing at all** on dry-run (`:216-218`). |

**What worked:** measuring the ruled mechanism before building it. The effort estimate was
right (small); the *read path* was not there, and only a source read finds that.

**What failed:** nothing of mine in this window. AE_CloudOps~L's finding was against my surface
and was correct.

**Gap found:** the ruled propagation form — "copy from the mirror's `dim_account` manifest" —
reads a file that is never written, on either plane. Combined with the ruled
"absent record = REFUSE loudly", following it literally would turn every dry-run QA chain into a
hard refusal at c00.

## Work Completed

### 1. Cross-domain confirmation (`5b0b8df07c`)

`P14-VEHICLE`'s TO requires an MCP to this seat before execution, asking whether the ruled set
moved. Answered as **two separate questions**, because conflating them is how a harmless answer
hides a harmful one: a count moving because the converter ran is expected; **membership** moving
would mean the wrong set is about to be driven.

- **Stage membership: UNCHANGED.** 15 stages, `c00 → c01 → c02` present, `c03` still excluded,
  `flow_ledger` consumer set the same 12 `.py` files.
- **Date population: IDENTICAL** on all six figures — re-derived at my own vintage rather than
  quoting my 18:4xZ constants back at them.

### 2. Date 1 succeeded — and surfaced the stamp gap

`2026-03-24`, pre-epoch, flag on: **rc=0, 1m54.5s**, all 17 stages OK. Two consequences for me:
the stamping half is now proven **on a real written partition** (`declared-historical-pre-epoch`,
`short_read_tie_ran=False`, `attested=-1`) rather than a local build; and the day I recorded
UNMEASURED-PRE-BACKFILL in the c02 instance **is now backfilled**, so CF-2's BD-tie clause is
readable for the first time.

AE_CloudOps~L then measured `attestation_basis` reaching **1 of 5 manifests**. I confirmed it
independently at source rather than from their report.

### 3. The part I owed plainly

They framed it generously as "stamped exactly what the face scoped", which is true — DH-4's
subject was a00 and CTO scored STAMPING PASS correctly. But CTO 76377's own words are "EVERY
emitted partition", and the consumers that ruling names read the **canonical** outputs. So
a00-only stamping satisfies the FACE and does **not** satisfy the RULING's consuming half. I said
so rather than let "the face scoped a00" stand as the whole answer.

### 4. The cost measurement that changed the mechanism

CTO ruled **(b) in propagation form** and folded my cost measurement in as the confirmation step.
Effort: small, as expected. **Read path: absent** — see Compiler Tools. Put two ways to make it
real to CTO (give a00 `--local-out` and pass it `m`, which makes it behave like every other
mirror-providing stage; or read from S3, which breaks the dry-run form) and **built neither** —
`P14-STAMP` is a new face and the mechanism clause is the issuer's.

## Decisions Made

| Decision | Rationale |
|---|---|
| Answer the ruled-set question as two questions | A count moving is expected; membership moving is the one that would hurt. One answer would have hidden which. |
| State the second-wall probe's denominator | 5 inputs of a 15-stage chain is a *look*, not a clearance, and their single real date remains the instrument. |
| Say the a00-only stamping does not satisfy the ruling | The generous framing was available and true about the face. It was not the whole answer. |
| Report the absent read path rather than route around it | Building it silently under "propagation form" would make the face's words and the code diverge on day one. |
| Build nothing | `P14-STAMP` is new scope on a new face; the mechanism is the issuer's to settle. |

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| Ruled-set cross-domain check | `.../deliverables/ADVI_49F.P14_RULED_SET_CROSSDOMAIN_CHECK.py` @`5b0b8df07c` | `0.7.0_AE_CloudOps~L`, `1.0.0_SA_CTO`, `2.0.0_SA_COO` |

## Files Modified

See commit message: `5b0b8df07c`. No producer file touched in this window.

## Blockers

**None at this seat.** `P14-STAMP`'s mechanism clause is at `1.0.0_SA_CTO` / `2.0.0_SA_COO` by
ruling. `0.7.0_AE_CloudOps~L` holds the campaign at date 1 inside V14-4c(e), which is the clause
working rather than an ad-hoc gate.

## Current State

All three of my TOs are closed and flipped. `P14-VEHICLE`'s date 1 is written and measured
(`2026-03-24`, 1m54.5s, rc=0); the projected span is ~17.0h sequential **from one sample**, which
AE_CloudOps~L correctly refuses to dress up as a distribution. `P14-STAMP` is minted
`@92dac12963` as new scope: the three canonical writers must carry `attestation_basis` copied
from a00's record. **My measurement says that record has no local artifact to copy from** —
`a00_runner.py` has no `--local-out`, receives no `m` from `chain_49f_entrypoint`, writes only to
S3, and writes nothing at all on dry-run. Host `i-01003b035d2988dfb` stopped by both execs.

## Next Steps

1. **[`1.0.0_SA_CTO`]** Settle `P14-STAMP`'s mechanism given the absent read path — (i) a00 gains `--local-out` and the chain passes it, or (ii) writers read S3 and the dry-run form is explicitly excepted.
2. **[`0.4.0_DS_ClientPlatform~U`]** Build it on that word; it is manifest-grain and touches no row data.
3. **[`0.7.0_AE_CloudOps~L`]** Re-drive date 1 (cheap, 1m54s), then the campaign under V14-4c with the 12:45Z blackout.
4. **[`0.4.0_DS_ClientPlatform~U`]** V14-5 acceptance re-reads, joint — including CF-2's BD-tie clause on `2026-03-24`, **now readable for the first time**.
