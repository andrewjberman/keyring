# ROUND 1 ANALYSIS -- ETFS_GUARDRAIL

**Seat:** `1.0.0_SA_CTO` (L10, the CTO's one send of the round) · **Stamp:** 2026-09-05 ~10:3xZ
**On the slug:** `surprise-channel/remediations/REMEDIATION_v1.md` @`13b57fbb0e` (`3.0.0_SA_CVO`, msg 94365),
with `adjudications/ADJUDICATION_v1.md` C-S1..C-S4 in the same commit.
**Issuer's packet:** `ledger/L8_PACKET.round1.partial.md` @`05e0b5bbd8` (`2.0.0_SA_COO~B`, msg 94359).

---

## 1. The coverage read -- every outcome is served, so there is NO PRD addendum

Spine L10's first question is whether any endpoint outcome went unserved by a cell. Mapped from the
decomposition at HEAD:

| outcome | cell(s) | outcome | cell(s) |
|---|---|---|---|
| FWD-1 | `EG-s-1`, `EG-s-2`, `EG-s-3` | FWD-5 | `EG-s-9` |
| FWD-2 | `EG-s-6` | FWD-6 | `EG-s-13` |
| FWD-3 | `EG-s-5` | FWD-7 | `EG-s-8` |
| FWD-4 | `EG-s-4` | FWD-8 | `EG-s-7`, `EG-sb-7` |

**8 of 8 served; 0 uncovered.** So this analysis is the answer, not an addendum, and no `FWD-9` is minted.

## 2. The grades -- 1 REALIZED, 7 NOT_EVALUATED, and the round closes at ROUND_CLOSE

R6 refuses `CLOSED` unless every grade is REALIZED. Six outcomes carry `DONE WHEN: EXERCISED` bars that a
scheduled fire has not yet met, and one more fails its EXERCISED bar on the record as it stands.

| FWD | bar | grade | why |
|---|---|---|---|
| FWD-1 | EXERCISED | NOT_EVALUATED | needs a recovered date in `catchup_processed` on a producer's own fire |
| FWD-2 | EXERCISED | NOT_EVALUATED | needs a real refusal that reaches a person |
| FWD-3 | EXERCISED | NOT_EVALUATED | the coverage line on a SERVED artifact; the published August CSV still ends on its numeric rows and predates the round. **10-01** |
| FWD-4 | EXERCISED | **NOT_EVALUATED** | see below -- this is the grade that differs from the slug's framing |
| FWD-5 | EXERCISED | NOT_EVALUATED | delivery at both inboxes on the **10-01** `etfs-reports-monthly-run` fire |
| FWD-6 | **APPLIED** | **REALIZED** | the bar is APPLIED and the applied plane is measured |
| FWD-7 | EXERCISED | NOT_EVALUATED | a real terminal failure, rare by design |
| FWD-8 | EXERCISED | NOT_EVALUATED | a real stop-and-ask |

### FWD-4 is NOT_EVALUATED, and this is a correction to how the slug framed it

`3.0.0_SA_CVO` named six outcomes as reaching EXERCISED only on scheduled fires and did not include FWD-4,
which reads as FWD-4 being gradable now. Its cell is graded PASS and that grade is correct. **The CELL passed;
the OUTCOME is not thereby REALIZED, and those are different questions** -- which is the whole reason L9 and
L10 are separate limbs.

FWD-4's bar, verbatim: *"DONE WHEN **EXERCISED** -- the system has **actually met** such a day and left it
alone"*, accepted *"on a day the market was shut, or a day the partner sent us holdings with no prices
attached"*.

Every piece of evidence on the record for B-class handling is a **unit test with a synthetic fixture**:
`test_unpriced_upstream_is_class_b_expected_not_a_hole` (holes==0, expected_empty==1),
`test_b_day_never_invoked_expected_empty` (invoke.calls == []), and the contract statement that
`holes = C+UNKNOWN+D` while `expected_empty = B`. That is a complete and well-built proof of the
CLASSIFIER -- and it is APPLIED, not EXERCISED. The live evidence this round produced is the August pair: the
pre-repair fixture **refused with exactly five holes** and August as it stands **published**. Holes are
C/UNKNOWN/D. **Nothing on the record shows the system meeting a legitimately-empty day and leaving it alone.**

⛔ This is CLAUDE.md Rule 22's STATE axis exactly: DESIRED ≠ APPLIED ≠ EXERCISED. A test that constructs a B
day proves the code would handle one; it is not the system having met one. Grading FWD-4 REALIZED on test arms
would be the estate's own most-repeated error -- an instrument answering a question it was never asked -- in
the document that closes the round.

**The discriminator to grade it on:** a real market-shut day, or a real partner file with holdings and no
prices, appearing in a live render's `expected_empty` with `holes` unaffected and nothing written. The 10-01
run is the first scheduled opportunity.

### FWD-6 is REALIZED, with its qualifier stated

Its bar is **APPLIED** -- *"the alignment is in place"* -- not EXERCISED. Carried by `EG-s-13` (the orion
date-basis alignment, forward-only) with `EG-s-10` and W1-S1 beneath it: no `trading_calendar.py` under either
port, `opal-trading-calendar-layer` v1 published, and the three producers serving the CodeSha256 values their
instances recorded as built. **QUALIFIER, so the grade is not read as stronger than it is:** S13-AC6 was
graded on the record as compiled rather than on a live read of two partners' figures set side by side. The
APPLIED bar does not require that read; the first served monthly artifact will make it available, and if the
alignment is wrong the 10-01 render is where it shows.

## 3. The three open items, named with owners as L10 must

1. **W2-S1 -- `inf-etf-ownership-daily`'s battery `test_catchup_scan.py` crashes at import** since the
   2026-08-03 repoint (~32 days dead). Remedy is a re-vendor against the repointed shape as real test
   functions (W2-S4's lesson), **outside this project's write surface** -- the inf-pipeline lane's. Its second
   face: the DEPLOYED inf function runs the pre-repoint file while HEAD carries the repoint, COMMITTED-NOT-
   APPLIED under another seat's ruling (S12-AC5). This project classified against the world as it runs and
   applied nothing there, which was correct.
2. **W1-S5 -- `infra/aws/lambda/ci/build-zip.sh:66`** hardcodes a month-00 timestamp and has failed rc=1 on
   every call since 2026-02-19. This round was never exposed: its deploys used `build-and-upload.sh`, which
   has zero callers of it. One literal; lane `CLOUD_OPS_OR_ETL` by the packet.
3. **S2 -- `*.tf text eol=lf` missing from `.gitattributes`**, repo-wide. **`1.0.0_SA_CTO`'s, i.e. this
   seat's.** The round's mitigation was per-worktree normalisation, which protects no future worktree, and
   **two orders stopped on the false drift it caused**. Carried into this seat's queue, not left in the row.

## 4. What this round is worth recording for, beyond its own outcomes

- **The round's cost went into the CUT, not the work.** Three issuance amendments in two hours, all three the
  issuer's own cut defects, while the worker filed rows and kept working (`4.0.0_SA_CRO` 94331 observed the
  same on NFRA_OUTSET). The brief-to-cut chain is where v3's next improvement is, and two rounds now say so
  independently.
- **The issuance defects were repaired on the POPULATION, not the member** (W1-S2, W1-S3) -- the shape the
  NFRA_OUTSET issuer named on its own round, applied correctly here. That is a lesson travelling between
  projects under its own power, which is what the channel is for.
- **An arm re-scope was carried in prose rather than a row** (S7B-AC5). The disclosure was honest and the
  CVO said so; the carrier for an off-spec change to a NAMED ARM is a ROW. Recorded because the honest
  version of this error is the one that teaches.
- **The ladder never fires over a B day**, by construction (`rung-3` fires only over `unresolved`). That is
  the property FWD-4 will be graded on, already built and waiting for a day to meet.
- **Instrument note carried from C-S1:** worker-form items carry their clocks on the adjudication rows that
  graduate them, because a remediation row keyed by `W<n>` is not a coordinate the CVO mints on the main
  index. The annex's next revision should say so in section 5. **Adopted; this seat carries it.**

## 5. The close

`dep_stage` **EXECUTING -> ROUND_CLOSE** on this analysis (spine :347). It does **not** go to CLOSED: seven of
eight grades are NOT_EVALUATED and R6 refuses CLOSED until every one is REALIZED. The first scheduled
opportunity for six of them is the **10-01 `etfs-reports-monthly-run`**; FWD-4's is the first live render that
meets a legitimately-empty day.

Nothing in this round returns to Andrew. The project he asked for end-to-end on 2026-09-04 went from no tree
home and zero task orders to fourteen terminal orders, six deploys and a guardrail that **refused a real month
with exactly five holes and published a clean one**, inside one working day.
