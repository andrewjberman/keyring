# NFRA_CLDGRPH round 4 -- L8 PACKET (PARTIAL, and the word is load-bearing)

**Compiled by** `2.0.0_SA_COO~A` 2026-09-04 ~19:1xZ, on the `/drive` obligation "terminal orders -> L8 compile NOW".
**Handed to** `3.0.0_SA_CVO` for L9. **This is NOT the L10 slug** -- the slug goes once, after EVERY order is terminal
and EVERY row is dispositioned, and six orders are still open. This packet exists so the CVO's L9 work on what IS
terminal can run across tonight's wait instead of queueing behind it.

---

## 1. WHY PARTIAL, and the date that decides it

Six of twelve round-4 orders are terminal. The other six are not late -- they are behind **one calendar fact**:
TO-CG-D-1's digest pins landed ~17:2xZ on 2026-09-04, so **CG-x-2 (TO-CG-D-9) cannot be exercised before the 02:00Z
fire on 2026-09-05** ("a night under pre-fix bytes is not the night FWD-2 means", ROUND_ANALYSIS.round3.md s.2 item 2).
TO-CG-D-10 needs one cycle after D-9; TO-CG-D-11 needs D-9 merged; **TO-CG-D-7 (CG-s-8) is LAST by ruling R7** behind
D-9/D-10/D-11, and TO-CG-D-8 closes the run. TO-CG-D-5 is open for a different reason, given in s.4.

## 2. THE SIX TERMINAL ORDERS, each with the instance the checker graded

Every instance below was re-validated **at the issuer's seat with COVERAGE CHECKED** -- the expected criterion ids
taken from the ORDER at HEAD and passed as the checker's third argument, which the workers' own runs did not all do.

| order | cell | instance | checker | drained at |
|---|---|---|---|---|
| TO-CG-D-4 | CG-s-7 | `deliverables/0.9.0_WK_NFRA_CLDGRPH~3/...TO-CG-D-4...proof_of_spec.json` | rc=0, 7/7 PASS | earlier round-4 |
| TO-CG-D-12 | CG-s-16 | `deliverables/0.9.0_WK_NFRA_CLDGRPH~1/...TO-CG-D-12...proof_of_spec.json` | rc=0, 7 rows, 0 violations | `b687429234` |
| TO-CG-D-2 | CG-s-5 | `deliverables/0.9.0_WK_NFRA_CLDGRPH~2/...TO-CG-D-2...proof_of_spec.json` | rc=0, 10 rows, 0 violations | `57b6750101` |
| TO-CG-D-3 | CG-s-6 | `deliverables/0.9.0_WK_NFRA_CLDGRPH~2/...TO-CG-D-3...proof_of_spec.json` | rc=0, 8 rows, 0 violations | `2ca8e882f2` |
| TO-CG-D-1 | CG-s-15 | `deliverables/0.9.0_WK_NFRA_CLDGRPH~1/...TO-CG-D-1...proof_of_spec.json` | rc=0, 8 rows, 12/12 surprises resolving | `c5b54680a9` |
| TO-CG-D-6 | CG-x-5 | `deliverables/0.9.0_WK_NFRA_CLDGRPH~2/...TO-CG-D-6...proof_of_spec.json` | rc=0, 4 rows, 0 violations | `291551ca2f` |

## 3. THE FIVE JUDGMENT CRITERIA -- THIS IS THE L9 WORK

Each carries **no verdict** and is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
A `PASS`/`FAIL` on any of them is INVALID. They are graded at L9 and were never self-graded.

- **D12-AC7** (CG-s-16) -- the SCOPE reading on the IAM grant: account-wide `*` chosen over a 34-bucket enumeration,
  three reasons given, blast radius measured at one principal.
- **D2-AC10** (CG-s-5) -- the eight-item architecture gate: G1/G2/G3 GROUNDED-live, G4 GROUNDED on the applied plane,
  G5 N/A-by-construction, **G6 PARTIAL** (0 of 41,489 audit records carry `graph_`; row W2-S8), G7 GROUNDED on
  deployed bytes both sides, **G8 SIGNED and quoted verbatim from `1.0.0_SA_CTO` msg 94158** with all six conditions.
- **D3-AC8** (CG-s-6) -- the RENDERING choice: why the disclosure line puts the service's `age_line` verbatim first
  and the machine fields after, with both CLI surfaces side by side and 10 removed switches named.
- **D1-AC8** (CG-s-15) -- the COPY-source DIFF: `649164d75b -> HEAD` over 37 zip sources = **ONE file**,
  `org/modules/graph/comp_aws_cli.py` +168/-18, one commit `b5bc1c8b27`, reaching `globgrph-derive-runner` only;
  `5644fee152 -> HEAD` = EMPTY. Plus the projection family's launch on the pinned digest.
- **D6-AC4** (CG-x-5) -- the fresh machine's answer beside the laptop seat's. **THE ISSUER'S HALF IS TAKEN** and lives
  in `STEP_LOG.2.0.0_SA_COO~A.round4.json` row 11, which TO-CG-D-6 names by path: both at vintage
  `2026-09-04T16:38:39.485910+00:00`, 58 rows and 27,295 CloudNodes each, **row arrays IDENTICAL**, same normalised
  digest `cedb5abceb26e607`. ⛔ **GRADE IT UNDER `NFRA_CLDGRPH-S37`:** both seats now read the SAME served projection,
  so they agree BY CONSTRUCTION and the comparison can no longer fail. The discriminating version (a local-DB reader
  against a served one) is takeable only until TO-CG-D-7 deletes the local copy.

## 4. WHAT IS OPEN, AND ONE OF THEM IS THE ISSUER'S FAULT

- **TO-CG-D-5 (CG-x-1)** -- the cell is EXERCISED on the substance (a never-compiled seat asked and was answered in
  7.668 s with the three bd-pipeline lambdas and no build; D5-AC1/AC2/AC3 PASS-by-output, each with a live arm, the
  process detector proven by a planted decoy). **D5-AC4 FAILED on an ISSUER DEFECT**: its enumerate pattern carried
  `--mode`, which matches the docstring DOCUMENTING that `--mode` is gone -- DOCSTRING=1, CODE=0, so the expectation
  was unsatisfiable while the property held. **Amended at `88c4db9dd4`** (pattern narrowed; measured 0 hits on the thin
  client and 5 hits / CODE=4 on the pre-CG-s-6 file, so it can still fail). The worker had a PASS available by dropping
  the optional `expect` field, **refused it**, filed BLOCKING row W3-S1, and left the order open. Evidence merged at
  `309c1bb511`; the re-run owes D5-AC4 only. **D5-AC5 is a judgment criterion that will join s.3 when this closes.**
- **TO-CG-D-9, -D-10, -D-11, -D-7, -D-8** -- blocked on the night and its successors, per s.1.

## 5. THE ROW CENSUS -- 61 rows, 42 ARMED, and the issuer owns 16 of them

Parsed from every fenced block in `surprise-channel/investigations/INVESTIGATION_v1.md` at HEAD (61 rows, 61 unique
ids). **11 BLOCKING rows:** S5, S13, S17, S18, S19, S21, S24, W1-S1, W1-S7, W2-S1, W3-S1.

| disarm owner | n | ids |
|---|---|---|
| `2.0.0_SA_COO~A` | **16** | S2 S5 S8 S12 S13 S16 S20 S21 S27 S28 W1-S2 W1-S6 W1-S10 W2-S5 W2-S7 W3-S2 |
| `1.0.0_SA_CTO` | 8 | S26 S31 S34 S35 S36 W1-S1 W1-S11 W2-S1 |
| `0.7.0_AE_CloudOps` | 6 | W1-S3 W1-S7 W1-S8 W1-S9 W2-S2 W2-S10 |
| `0.7.0_AE_CloudOps~Q` | 4 | S3 S10 S14 S15 |
| `0.7.0_AE_CloudOps~S` | 4 | S17 S18 S19 S24 |
| `0.7.0_AE_CloudOps~T` | 2 | S22 S23 |
| `1.0.0_SA_CTO~A` | 1 | S1 |
| `3.0.0_SA_CVO` | 1 | S37 |

⛔ **THE ISSUER'S 16 ARE THIS SEAT'S OWN NEXT WORK, not the CVO's**, and they are named here so the count is not
discovered at L10. Several are candidates for disarm on THIS ROUND'S exercises rather than on any build -- **S20 and
S28** (the silent TRIGGERS zero) are answered by D-1's `TRIGGERS=171` and D-12's grant together; **W1-S2** (the
unapplied pins) by the eight-address apply; **W1-S10** (the false-zero instrument) by the repaired script and the
`LAMBDA=203` control. Each of those must be disarmed **on the exercise and by reading the row's own disarm text**, one
at a time, not swept as a batch -- and this seat will not disarm a row of its own on a build. Two ARMED rows carry a
warning that outlives this round and belongs in the L10 slug whatever happens: **W2-S10** (the unscoped plan carries
two DELETES of live WAF IP sets, owned by nobody in this project) and **W1-S8** (`globgrph-resource-summaries-producer`
has no trigger on EventBridge Rules OR Scheduler -- a declared task family wired to nothing).

## 6. WHAT THIS PACKET DOES NOT CLAIM

It does not claim the round is finishable tonight; s.1 says why. It does not claim any FWD is REALIZED -- that is the
CTO's grade at L10, on the CVO's stamp. It does not disposition a single row: the ARMED census in s.5 is a **statement
of standing with owners**, not an adjudication, and the remediation plane stays `3.0.0_SA_CVO`'s.

---

# ADDENDUM 1 -- 2026-09-04 ~20:5xZ, appended by `2.0.0_SA_COO~A`

The body above was READ by `3.0.0_SA_CVO` at 19:20:39Z (`get_delivery_state`, id 94262). It is not edited; what
changed since is recorded here so the version the CVO already read stays intact.

## A1.1 TO-CG-D-5 IS NOW TERMINAL -- the count is 7 of 12, not 6

The re-hand pass closed it (`drain 9d79c728d3`; worker commit `bdd7dbaa08`). The amended **D5-AC4 PASSES**:
`ENUMERATE: 0 hit(s) across 169 lines / 8 sections`, every band 0 -- re-run at the issuer's seat. **Its failure
control was run by the WORKER and independently by the ISSUER**, both on the pre-CG-s-6 file `@c7b6a0d200`: 5 hits,
`CODE=4`, including `import kuzu` and `_canonical.ensure_fresh(`. The narrowed pattern still fails on what it exists
to catch, so the amendment did not soften the bar. Instance VALID rc=0, 5 rows, 0 violations, coverage checked
against the order's own five ids. **The worker filed no new row and did not close W3-S1 itself** -- that row was
disposed of on the issuer's plane by the amendment `@88c4db9dd4`, which is the correct separation.

## A1.2 THE JUDGMENT SET IS NOW SIX, NOT FIVE

**D5-AC5** joins s.3: *"in the time an ordinary lookup takes"*. It carries a measurement the CVO should see before
grading it -- **the time to answer roughly DOUBLED between the two passes**, 7.802 / 8.497 / 7.668 s (mean 7.99)
on the first, 17.058 / 16.372 s (mean 16.72) on the re-hand, against the 11.55 s `comp-find --corpus aws`
comparator the order names. The first pass sat below that comparator; the re-hand sits above it. The two passes read
DIFFERENT projections (`c3ba0330e306` @16:38:39Z vs `a78b6836265e` @18:11:48Z). **The worker proved the rebuild was
not its own act** (engine-process count 0 before/during/after every run; its first ask already read the later
vintage) and then **declared an exclusion rather than guessing**: it holds no measurement separating a slower client
from a larger projection from a slower link, and did not run one because the order names no such act. That is the
honest shape of the row and the CVO grades it as it stands.

## A1.3 THE ARMED CENSUS IN s.5 IS STALE, BY THE ISSUER'S OWN ACTS

Two rows have been DISARMED by ACK since the body was written: **S20** (ack `NFRA_CLDGRPH-S38` @`83fa8ee04e`) and
**S28** (ack `NFRA_CLDGRPH-S39`). ⛔ **The channel is APPEND-ONLY, so a disarm CANNOT clear the armed row's own
`hazard_standing` field** -- S20 and S28 still read `ARMED` in their own JSON and always will. **A census over that
field therefore over-counts by the number of standing ACKs**: it returns 16 for this seat where the truth is 14, and
42 estate-wide where the truth is 40. **The fix is a READING RULE, never an edit**: subtract the ACKs, which are
identifiable by `disposition: DISMISSED_WITH_REASON` plus a `dismissal_reason` naming themselves as an ACK. Editing
S20 or S28 would break the append-only rule the whole channel rests on. Carried to the CVO as msg
`20260904T204152Z` in the tick that caused it.

Still ARMED and still this seat's: **W1-S2** (the eight-address apply, DESIRED-then-APPLIED) and **W1-S10** (the
false-zero instrument, repaired and exercised) both read as met-by-exercise and each is owed its own reading and its
own ACK. **Twelve** of this seat's rows remain beyond those two.

## A1.4 WHAT DID NOT CHANGE

The five judgment criteria of s.3 stand exactly as handed, including D6-AC4 and its S37 caveat. No row is
dispositioned by this addendum. The five orders still open (D-7, D-8, D-9, D-10, D-11) are unchanged and remain
behind the 02:00Z 2026-09-05 derive.
