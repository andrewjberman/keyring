# COT_SUPERVISED G4/G4b acceptance — verify + close on the FRI 11:30Z fire

**archetype:** VALIDATE
**Agent:** 0.6.0_AE_PartnerETL · **Window:** 2026-08-21 0843Z–1330Z · **TO:** COT_SUPERVISED.G4-ACCEPT-HANDOVER.friday-1130z-verify-and-close (@6ae5a5dd7a)

## Verdict

**G4/G4b ACCEPTED on the scheduled fire — belt verifier 12/12, rc=0 (unpiped), with ONE ROUTED
FINDING (row delta +37, dispositioned as data movement, below).** The seat inherited the leg from
the closed 0.6.2 seat via the TO + CTO annex @65aff2c124 and re-derived nothing already measured.

## The read, criterion by criterion

- **V1 CLOCK, both planes, read fresh this session:** DESIRED
  `infra/aws/terraform/cot-pipeline/schedule-et.tf:89-90` = `cron(30 7 * * ? *)`
  `America/New_York`; APPLIED `aws scheduler get-schedule cot-bd-session-daily-et` = same
  expression + tz, `State: ENABLED`, window OFF. 07:30 ET = 11:30Z (EDT).
- **V2 LANDING:** watch armed 0846Z as the session's first substantive act (Monitor `boo34xyaa`,
  emitting LANDING / OVERDUE-past-13:00Z-every-15m / rate-limited non-404 POLL-ERROR; instrument
  positive-controlled on the present 08-19 key and negative-controlled on the then-absent 08-20
  key). LANDING fired: `HOLDINGS_DAILY_2026-08-20.xlsx` LastModified **2026-08-21T11:32:01Z**
  (s3api, UTC), 1,368,202 B — inside the observed 11:31–11:32Z cadence. OVERDUE limb never fired.
- **V3 SERVED-BYTES:** +2 supervised columns exactly (19 → 21, both `Holding Supervised` +
  `Account Supervised` present); holdings sidecar + attributes sidecar both
  `basis=land_time_measured has_data_rows=1`; bronze sentinel `overall=success` carrying
  `account_attributes` among 6 tables. All timestamps via boto3/s3api (UTC). **RE-PIN SETTLED:
  sha256-only, by SOURCE READ, not by re-pin** — the belt verifier @d4a86a84e1 carries NO
  LastModified limb against the 18:06:50Z code-object pin (it never reads
  `cot_bronze_ingest.py`; its only timestamp reads are the landing artifacts' hour-window
  checks), so there was nothing to re-pin in code and the identical-bytes rewrite at 01:04:18Z
  cannot fire anything falsely. CTO's byte verification (sha256 `c8764a43c1fe7189` == pin ==
  repo) stands as the code-currency ground; not re-derived per the TO.
  - **ROUTED FINDING (per the TO: "a row-count change is a FINDING, not a pass"): rows
    18,051 → 18,088, delta +37.** The verifier's own row check passes on `len>0` and only
    *prints* the delta — caught pre-fire by source read; my read overrides that PASS to a
    routed finding. **Frame:** baseline pair was FLAT (08-18: 18,051; 08-19: 18,051 — measured
    directly on the served bytes this session), so +37 on the 08-20 as-of is the first movement
    in three business days. **Disposition offered (COO validates): genuine position/account
    movement on the new as-of day, NOT a template-amendment artifact** — a column-add cannot
    mint rows, the per-row invariant is clean over the full 18,088, and the supervised value
    counts (17,708 + 380) sum to the new total. 0.2.0_DS may corroborate from their half.
- **V4 BELT'S FIRST REAL TEST:** per-row Holding-vs-Account supervised disagreement =
  **0 disagreeing rows over DENOMINATOR 18,088 comparable (0 blank/absent, 18,088 total)**.
  Negative controls intact (author's 8/12 pre-fire run + my own two controls below).
- **V5 PROOF + CLOSE:** instance at
  `org/tier2_senior/0.6.0_AE_PartnerETL/deliverables/COT_SUPERVISED.G4-ACCEPT_PROOF_OF_SPEC.json`,
  validated by `.tools/proof-of-spec-check.py` with expected set V1,V2,V3,V4,V5, **rc read
  UNPIPED**. RAVC close to 2.0.0_SA_COO cc 1.0.0_SA_CTO + 0.2.0_DS_PortfolioAnalytics.

## Controls run at MY seat (not inherited)

- **Mutant:** verifier `--asof 2026-08-21` (key absent by construction) → `[FAIL] holdings
  artifact ABSENT`, `VERDICT: NOT YET ACCEPTABLE`, **rc=2 unpiped**. (First capture was piped
  through `tail` and read rc=0 — the exact V5 trap; discarded and re-captured unpiped.)
- **Determinism:** second same-input run → identical sha256
  `706c822019b6331ddfc1fdcdd98ea647d6196191f25561bca5b0a7b09d160d66`, identical 12/12, identical
  delta +37. STABLE.

## G4b

`ACCOUNT_ATTRIBUTES_DAILY_2026-08-20.xlsx` landed **11:31:09Z** (schedule window, not hand),
24,904 B, 5 cols / 943 rows; sentinel carries the table; chain advanced.

## Also this session (pre-fire window)

- Startup per org/XXX.md (registered PID 15576; watcher Monitor `bsj9xend0`; PATH 97/102 +
  exercised; serial file; comp-to set; owned-paths hook present).
- COO route 63372 closed: bd-API `endpoints/README.md` clone-not-update fix @4394ca0df0
  (owned-paths POD4 refusal → audited `GIT_COMMIT_AUTHOR_OVERRIDE=POD4` on COO's explicit
  routing; lane mismatch surfaced to COO, not adjudicated).
- CRO B-0012 closed: brief PoC pointers annotated ARCHIVED @75c992ef57.
- Both rode MSTR's 0910Z integration push (CLOUD @cf11d6afbc, MSTR-verified); merge-window
  hold ACKed and honored.
- MSTR startup hint 64669 ACKed; stranded 0.6.2 inbox messages (64051, 64066) read from disk,
  not drained.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-find | `--name README.md data/black_diamond` + `"v1/template" data/black_diamond/API` | located the routed doc target; DENOMINATOR 6/176 + 15/19 printed |
| comp-to | `comp-to COT_SUPERVISED.G4-ACCEPT-HANDOVER...` | session TO context set (race-free per-session file) |
| comp-which | `"how do I grep the repo"` (A.3 exercise) | forwarder RAN (banner produced) — PATH probe scored on output |
| proof-of-spec-check | `<instance> V1,V2,V3,V4,V5` | VALID rc=0 unpiped (see V5) |

No comp-tool covers the S3 served-bytes read (comp-freshness is trading-frontier freshness, not
row/column content verify) — the belt verifier + boto3/s3api is the TO-mandated instrument there.

## Post-close triage + ADVI_BDAPIMIG.P1 re-ground (1330-1400Z addendum)

**archetype:** DIAGNOSE

- **TO triage routed to COO+CTO (64682/64683):** ADHC_GLDINC.P1 flipped superseded by ISSUER
  @bd6195b34e (its shadow+standing-comparator mechanism is the 08-04 Andrew veto class; the I/O-cut
  need survives for a sanctioned re-form). NIGHTLY-VERIFY + SS4c recommended supersede/re-confirm
  to COO (dead 02:00Z premise / parent-program supersede). L4-GUARD flagged: staged deliverable is
  moratorium-class, needs issuer re-confirmation before any GO. DC-OSINT + CUTOVER-1 parked as
  queued/staged.
- **ADVI_BDAPIMIG.P1 re-ground (read-only, all planes named):**
  - `comp-freshness chain bd` returned an EMPTY table under a sovereign-hold config note — an
    emptiness that must not carry a verdict; grounded on s3api instead.
  - **Runner healthy + self-protecting:** fires nightly at ~00:0xZ off `bd-49f-session-daily`
    (00:00Z, ENABLED) → `bd-49f-session-complete` (event rule; `bd-49f-runner-daily` cron(0 2)
    DISABLED since 06-29 by CTO ruling). transactions + realized land DAILY (08-20/08-21 as-ofs
    current, T-1 correct). auth_dead=False every run.
  - **FINDING (vendor-side, NOT a pipeline defect — NEVER#1 discipline applied):** since the
    07-09 stub fix, BD returns 0-DATA-ROW header-only snapshot exports for EVERY weekday as-of on
    allocations + unrealized; the FIX-1 REJECT guard refuses them nightly (logs, 3/3 days read:
    `REJECT: allocations @2026-08-1[8,9,20] export has 0 DATA ROWS (455x bytes)`), and the ONLY
    full-size landings for 6 straight weeks are FRIDAY as-ofs written on the SUNDAY 00:1xZ run
    (07-10, 07-17, 07-24, 07-31, 08-07, 08-14 — 124/68 dated xlsx enumerated, full pagination).
    Same bearer lands transactions in the same invocation, so auth is refuted as the cause.
    **Downstream implication: allocations/unrealized-derived silver rides a Friday snapshot all
    week (up to 4 trading days behind intra-week).** Whether BD moved to weekly snapshot posting
    or per-firm reporting cadence changed is NOT resolvable from our side -- routed, no action.
  - **Phase-2 frontier:** all 4 scrape boxes (bd-allocations/transactions/assets/fees) exist and
    are STOPPED, not decommissioned — EBS still held, EC2_MANIFEST rows live. Decommission stays
    destructive + separate-GO.
  - Trigger-shape surface (not adjudicated): the runner's ONLY trigger is another chain's
    completion event; the chain ROOT is scheduled (00:00Z), so whether this satisfies the
    production-pipelines-must-be-scheduled rule is CTO's read.

## Surprises (channel: one line to COO, no action taken)

- The belt verifier's row-count check structurally passes on any nonzero count (`len(data)>0`,
  verify_g4_belt_acceptance.py:100) — fine for this run since the TO ordered a human read of the
  delta, but a successor reusing the verifier without the TO's framing inherits a check whose
  name says "intact" and whose predicate says "nonempty".
- `.owned-paths.yaml` `data/black_diamond/**` catch-all is POD4 while COO route 63372 called the
  API-doc subtree "YOUR bd tree" — surfaced to COO in the route close.
