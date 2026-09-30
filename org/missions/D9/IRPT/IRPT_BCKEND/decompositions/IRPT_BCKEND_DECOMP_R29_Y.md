# IRPT_BCKEND round 29 -- workstream ~Y (Analysis) decomposition

Issuer `2.0.0_SA_COO~Y`, 2026-09-30 ~14:0xZ, the first issuance after the 07:52Z reboot. **Three cells, ONE issuance,
no edges.** One item is NAMED AND NOT CUT with the CTO-adopted candidate it now carries, and one ARMED row is disarmed
here by record.

## The rectangle, and where each item came from

Not a forward list. Every item is a ruling already recorded, cited at its pin:

| item | source | cut? |
|---|---|---|
| the per-job vendor endpoint ledger persists into `receipt.json` (shapes, never values) | W27 packet W27-4(a) @00f9ef2df8, blob `4c1dbb545f`; CTO half @dbbac713fc condition 8; CRO half @2ab90bf162 | `IB-yr-291` |
| a Playwright HAR of the login capture behind `YC_RECORD_HAR=1`, scrubbed by a check with a planted-value control | W27-4(b); CTO condition 8; CRO condition 4 | `IB-yr-292` |
| `decide()` and the profile projection read `allowedFirmIds` and refuse a `data_firm` outside it | W27-2 limit (3), CTO 103221; CTO half condition 5; **CRO condition 1 (proven BEFORE the window opens)** | `IB-yr-293` |
| S194 half 2 / S213 deeper half: certification passes a Comparison that does not compare | R28 named-not-cut; **CTO analysis @dd4c69b696 section 2: the body-field candidate is ADOPTED first, tested off-window; the certifier change is the fallback** | **NOT CUT -- issuer measurement first, see below** |
| S228: the seam suite lost two producer operations from its population | R28 amendment 1: "cut in round 29 on its own" | **DISARMED BY RECORD, no cell -- see below** |

## THE PREFLIGHT RULE THIS ROUND IS CUT UNDER (CTO 103159, stated as the CTO's analysis @dd4c69b696 asks)

Verbatim: *"Before ~Y issues a criterion, it runs the invocation on the base commit and records the result in the
issuance commit: the printed denominator, and for a fix criterion the red-before state. A criterion whose base run
cannot show the stated cause is recut before issuance. Cost: one run per criterion. Non-application: a criterion
that reads a world state not yet created (a live window); it names its discriminator instead."*

**Every mechanical criterion below is a FILE under `deliverables/2.0.0_SA_COO~Y/R29_checks/`, run at CLOUD HEAD
`a7a6d286f2` before the cut.** The base reading is printed beside each criterion in the issuance commit and on each
order's face. A build check FAILS at base; a control PASSES at base; none did neither.

| criterion | file | base reading at a7a6d286f2 |
|---|---|---|
| Y29-1-AC1 | `check_291_receipt_ledger.py` | **FAIL as expected**: run READY, 1 receipt, 7 evidence records, receipt keys `artifact_key, attempt, template_id, variant`, `vendor_requests` is NoneType |
| Y29-1-AC2 | `check_291_dup_control.py` | **PASS as expected** (control): duplicate `EXISTING_ARTIFACT_REUSED`, `duplicate_vendor_requests 0`, `first_vendor_requests 7` |
| Y29-1-AC3 | pytest `tests/test_receipt_ledger.py` | **FAIL as expected**: the file does not exist |
| Y29-2-AC1 | `check_292_context_options.js` | **FAIL as expected**: `contextOptions is not exported (typeof undefined)` |
| Y29-2-AC2 | `check_292_har_scrub.py` | **FAIL as expected**: `har_scrub` not importable |
| Y29-2-AC3 | `check_292_suite_control.js` | **PASS as expected** (control): five arms, `summary.all_pass true` |
| Y29-3-AC1 | `check_293_allowed_firms.py` | **FAIL as expected**: `2 of 5 cases hold` -- case 1 (restricted row, foreign firm) reads `ALLOWED`: the recorded-not-enforced state the packet names |
| Y29-3-AC2 | `check_293_projection.py` | **FAIL as expected**: the stub's parameter match refuses -- the projection names eleven fields, not `allowedFirmIds` |
| Y29-3-AC3 | pytest two existing files + `tests/test_allowed_firms.py` | **FAIL as expected** on the new file (absent); the two existing files read **87 passed, 8 skipped, 0 failed** in 44.9 s and must stay so |

## The cells

| cell | item | outcome served | risk | worker | depends on | write set (disjoint) |
|---|---|---|---|---|---|---|
| `IB-yr-291` | `receipt.json` carries `vendor_requests`: the transport's own shape records, refused at the write if any record is off-shape | FWD-4 (Andrew's "call those in order": the HAR-equivalent for generation, per job, values-free by construction) | WORLD (infrastructure path) | `~94` | none | `ycharts/generate/job.py`, `ycharts/generate/tests/test_receipt_ledger.py` |
| `IB-yr-292` | `ycharts_session.js` records a Playwright HAR of the login/session capture ONLY behind `YC_RECORD_HAR=1` (path required, bodies omitted), and `har_scrub.py` strips `Cookie` / `Set-Cookie` / `Authorization` values and `cookies[].value`, proven by a planted value scanned on the OUTPUT bytes | FWD-4 (the login and WAF legs the resident's ledger cannot see) | WORLD (a host script) | `~95` | none | `infra/aws/ec2/investor-reporting-ycharts/{ycharts_session.js, har_scrub.py, tests/test_har_scrub.py, README.md}` |
| `IB-yr-293` | the projection carries `allowedFirmIds`; `decide()` refuses `ACTOR_FIRM_NOT_ALLOWED` for a `data_firm` outside it; absent and `ALL` keep today's behaviour | FWD-4 and the W27 window's precondition (CRO condition 1) | WORLD (an authorization decision) | `~96` | none | `ycharts/generate/current_authority.py`, `ycharts/generate/tests/test_allowed_firms.py`, `_scope/canonical_profile_reads.py`, `_scope/tests/test_canonical_profile_reads.py` |

Edges: none. **fanout: 3 of 3 chains, cap 8.** Slots `~94`, `~95`, `~96` (highest prior slot 93, ~M's).

## Issuer rulings inside this decomposition (rule 7)

1. **`IB-yr-293` writes ONE FIELD into a P-lane file, and that is the contract's own shape, not a competing edit.**
   `_scope/**` is `IRPT_LIVE_SCOPE_P` (`.owned-paths.yaml` @HEAD line 1152). CONTRACT.md row 21 (shared
   auth/scope): *"M/Y supply exact patches/examples; no competing edits."* The patch is exact and one-field
   (`allowedFirmIds` appended to `_USER_FIELDS` and `_USER_RETURN_FIELDS`, with the test pin at
   `_scope/tests/test_canonical_profile_reads.py:29` moved to match). MEASURED before the cut: no non-terminal
   `~P` or `~M` order names `_scope/canonical_profile_reads.py` (11 non-terminal orders of 155 scanned, 0 hits).
   The worker's grant is the order (`<paths>`); the drain records the landed hash in `STATUS~Y.md` for `~P` to
   read. No message, per the contract's "no peer ACKs".
2. **The refusal code is `ACTOR_FIRM_NOT_ALLOWED`, and the resident's handling of it is UNCHANGED this round.**
   `resident_worker.py` already retains a `CurrentAuthorityRefused` for retry (the S231 journal line). A
   permanent authority refusal cycling as "retained_for_retry" is S231's own question (a job cannot outlive its
   principal) and is NOT this cell's: its remedy is a terminal state for permanent refusals, cut on its own when
   S231 is dispositioned. This round's discriminator for CRO condition 1 is the JOURNAL LINE naming the code on
   a non-cottonwood job with no vendor call reached, which the window act reads.
3. **The recording is opt-in and refuses a default.** `YC_RECORD_HAR=1` with no `YC_RECORD_HAR_PATH` throws; the
   library never invents a path and never records unless asked. The raw HAR never enters the repo (CRO condition
   4); only the scrubbed file and the census diff against `YCHARTS_GENERATION_ENDPOINT_CENSUS_20260930.md` do.
4. **`IB-yr-291` refuses an off-shape record at the write.** A ledger that could carry a value is a ledger the
   CTO's condition 8 cannot trust; the record shape is the transport's own ten keys, and a record with any other
   key set raises `JobRefused("VENDOR_LEDGER_SHAPE")` before the receipt is written. That is the difference-control
   arm of AC3, not a fourth criterion.

## S228 DISARMED BY RECORD (owner `2.0.0_SA_COO~Y`, R28 amendment 1's "restore the pairs or record why none")

The suite's own re-cut comment, `_contracts/tests/test_seam_paired.py:70-76`, read at HEAD: *"The two operations
the consumer named then and v1 never routed (`submit-correction`, `export-preview`) are no longer in its fixture,
so they are no longer in this table."* **v1 NEVER ROUTED THEM.** There is no producer route to pair, so there is
no pair to restore: the population did not lose two producer operations, it stopped naming two operations that
existed only on the consumer's old list. The seam suite's denominator is the consumer's 12 concrete routes, pinned
(`CONSUMER_SMOKE_ENTRIES = 12`) and checked against the consumer's own fixture by
`test_the_operation_map_covers_the_consumers_own_denominator`, so a drift in either direction fails there. Row
`IRPT_BCKEND-S234` records the disarm.

## `IB-yr-283` is NAMED AND NOT CUT, now with the candidate the CTO adopted

CTO analysis @dd4c69b696 section 2: *"S194's third candidate ADOPTED as the remedy to try first: if the report
body's four section scopes exclude the comparison, the fix is a body field on the Analysis surface, tested
off-window; the certifier change is the fallback."* That is an ISSUER MEASUREMENT before any cut -- read
`recipe.generation_body()`'s section scopes against the COMPARISON template's own document (`templates.json`
14141824) and the retained W22 Y1 PDF that printed only `Opal Long-Term`. The measurement runs this tick after the
spawn; if the body field is the cause, round 30 cuts ONE cell on `recipe.py`; if not, the certifier data path
(R28's finding: `certify()` is never handed the chosen comparisons) is the cell. No worker is handed the question.

## The three `staged` orders (CTO analysis section 2)

`TO-IB-yr-242`, `-261`, `-271` were drained (`589a553074`, `a225440af7`, `3ce99ec90a`) with their workers'
commits and proof instances on CLOUD; their status word lagged the act. Flipped to `pending` in this commit as the
CTO asks; the terminal flip follows the drain's read of each proof-of-spec instance (sweep 5).
