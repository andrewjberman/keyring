# TO NFRA_FIDUPL.TO-FU-s-1 -- the Quo reader that returns the Wealthscape text-message code

<to_id>NFRA_FIDUPL.TO-FU-s-1</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-uploader</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-1` (`decompositions/NFRA_FIDUPL_DECOMP.md` v1.0) | **outcome_ref:** FWD-1 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

**FU-s-1** -- The Quo reader: given the line id and the Fidelity sender, returns the newest code inside a recency window opened at the SMS-send step; never logs it; a distinct result for "no code arrived". Seam probe against the real Quo (read only). Contract rows: C-SIGNIN (code leg), PRD ruling 5.

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (the facts, interfaces and handoff contract every cell shares; it is part of your context) and the cell text above. The project is NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning with nobody signing in; round 1 builds one thread end to end on fixtures and a few real read-only seams, and FU-x-1 proves the live sign-in.

### WHAT TO BUILD

Build `infra/aws/ec2/canonical-fidelity/quo_otp.py` and `tests/test_quo_otp.py` to the interface in the reference section 9 (`CodeResult`, `QuoOtpReader`, `default_api_key`, CLI `--probe`) and the facts in reference section 2.

1. `QuoOtpReader.read_code(since, window_seconds=120, poll_seconds=2.0)` polls `GET /v1/messages?phoneNumberId=<line>&participants[]=<sender>&createdAfter=<since ISO>&maxResults=10`, accepts ONLY a message whose creation time is later than `since`, extracts the single 6-digit token from its text, and returns `CodeResult("OK", code)`. When the window ends without a fresh message it returns `CodeResult("NO_CODE", None)`: a distinct value, never an exception and never an empty string.
2. The line id and the sender are constructor arguments with the measured defaults; the Operations line id is the only one ever put in a request (the Primary line `PNme8YAybw` must appear in no request).
3. The request carries the raw key in `Authorization` (no Bearer) and a browser-shaped `User-Agent`.
4. The code is never logged, printed, put in an exception message or placed in a repr; nothing the reader writes to a log or to stdout contains the six digits.
5. `--probe` calls the REAL Quo read-only: `GET /v1/phone-numbers` (assert the line id resolves) and one `/v1/messages` read with the sender filter, then prints exactly `QUO-PROBE-OK line=PNEJ5tafLm sender_messages=<n>`; on any failure it prints `QUO-PROBE-FAIL <reason>` with no secret and no message text, and exits non-zero. The key comes from Secrets Manager id `quo/api-key` through `default_api_key()` (boto3, us-east-1).
6. Tests (all with an injected fake `http` and fake clock; no network): `test_reads_only_configured_line_and_sender`, `test_ignores_messages_before_window_opens`, `test_returns_code_for_fresh_message`, `test_no_code_result_is_distinct_after_window`, `test_code_never_logged_or_printed` (capture stdout, stderr and the logging records and assert the six digits are absent), `test_sends_browser_user_agent_and_raw_key_header`, `test_other_line_never_read` (assert no request contains `PNme8YAybw`).

### ACCEPTANCE

<criterion id="FU1-AC1" cell_refs="FU-s-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu1</invocation><expect>R1-FU1-OK passed=\d+</expect></criterion>
`FU1-AC1` -- the seven named tests exist and pass.

<criterion id="FU1-AC2" cell_refs="FU-s-1"><invocation>python infra/aws/ec2/canonical-fidelity/quo_otp.py --probe</invocation><expect>QUO-PROBE-OK line=PNEJ5tafLm sender_messages=\d+</expect></criterion>
`FU1-AC2` -- the reader's seam against the real Quo, read only.

<expected_criteria>FU1-AC1,FU1-AC2</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FU1-AC1` base: FAIL as expected.
Dry-run at the base (HEAD of box/dell1 at the cut): `FU1-AC2` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Tests use SYNTHETIC data. The real Wealthscape export files hold client names and account numbers and are never read into a test, a log or a commit.
- **No secret, no alert.** No secret value anywhere (file, log, environment, command line, surprise row); no SNS, SES or notification of any kind.
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece. A premise that fails against live state is a surprise row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).

Reads (outside the grant):
- `org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py` lines 14-130 (the existing Quo poll)

<paths>
infra/aws/ec2/canonical-fidelity/quo_otp.py
infra/aws/ec2/canonical-fidelity/tests/test_quo_otp.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1), cell `FU-s-1`.
<owned_cells>FU-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU1-AC1,FU1-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~1/NFRA_FIDUPL.TO-FU-s-1.quo-otp-reader.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU1-AC1,FU1-AC2` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches the schedule (FWD-2); denominator 0 schedules created by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- reads one existing secret and one vendor API; no grant is written and no IAM file is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; runs on the enrichment round that touches this surface.
lane: the paths block.
</preflight>

Source: PRD v0.4.3 (@37a9865739) and the CTO's rulings through msg 8514; decomposition round 1 cell FU-s-1; worker reference.
