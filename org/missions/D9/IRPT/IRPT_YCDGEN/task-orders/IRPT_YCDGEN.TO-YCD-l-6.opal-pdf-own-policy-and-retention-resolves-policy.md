# IRPT_YCDGEN task order -- `YCD-l-6` -- ROUND 6 (THREAD): THE OPAL PDF UNDER ITS OWN POLICY ROW, AND RETENTION RESOLVING THE POLICY FROM THE REFERENCE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6D.md</decomp_doc>
<owned_cells>YCD-l-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-l-6.opal-pdf-own-policy-and-retention-resolves-policy</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~3</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; the resident host's role is proved by the issuer's close run
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-l-6` -- the opal pdf under its own policy row, and retention resolving the policy from the reference (hops 7 Persist (policy); FWD-1)
- `infra/logic/registry/reporting_policies.json` and `lib/tests/test_irpt_destination.py`: R12 (1).
- `ycharts/research/opal_producer.py`, `ycharts/generate/publisher.py`, `ycharts/generate/publication_worker.py` and their tests: R12 (2).
- `reports/retention.py` and `reports/tests/test_retention.py`, and any other file under `reports/` that the policy lookup forces: R12 (3).
- Keep every existing test in those files passing.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R12 The Opal PDF under its own policy row; the retention check resolves the policy from the reference** (the CTO's ruling, RULINGS.md batch 269). (1) Family `OPAL_REPORT_PDF` is REMOVED from the policy `irpt-x10-v1` in `infra/logic/registry/reporting_policies.json`: the policy reads exactly as it did before cell i-6, its `policy_sha256` is the value the base before i-6 computed (it begins e0046398; read the full value from the test constant in `git show 14eb4d115d^:lib/tests/test_irpt_destination.py`), and `lib/tests/test_irpt_destination.py` returns to its pre-i-6 family census and `ACTIVE_ROW_SHA` for that policy. No other row of the registry changes. (2) The Opal PDF is retained through the repository under policy revision `irpt-ycdgen-research-v1`, family `YCHARTS_OPAL_REPORT` (an existing registered row; do not register a new one); the producer, the publisher and the publication worker name that family where they named `OPAL_REPORT_PDF`. The Opal document's spill stays on the v1 family `EXTRACTION_EVIDENCE`. (3) `reports/retention.py` resolves the policy from the reference's own `policy_revision` against the set of ACTIVE registered revisions, in place of the pinned constant `POLICY_REVISION = "irpt-x10-v1"` (line 17; the uses at 50-63, 90-93 and 108-113). A v1 reference validates exactly as today; an Opal reference validates against its own row; a revision that is not registered, or is registered but not ACTIVE, is refused (`RetentionRefused`). Every existing retention test passes untouched. The row `irpt-ycdgen-research-v1` is PENDING_ENFORCEMENT today and is not yours to flip: a test makes it ACTIVE in a fixture registry only.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: RULINGS batch 269 in `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` (the ruling this cell implements); worker row IRPT_YCDGEN-W3-S14 in `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md`; `infra/aws/lambda/investor-reporting/reports/retention.py` (17, 50-63, 90-93, 108-113) and how the repository builds and checks a reference (`reports/repository.py` and the other files under `reports/`); the registry's three policy rows (`irpt-x10-v1` ACTIVE, `irpt-dashbd-x10-v1` and `irpt-ycdgen-research-v1` PENDING_ENFORCEMENT); the merged persist path from g-6 and i-6.
- Code lives under `infra/aws/lambda/investor-reporting/` except the registry and `lib/`. The registry file is validated by a refusing validator: run its own tests. Retention and registry digests are the point of this cell: print the v1 policy's `policy_sha256` before and after your edit and show it equals the pre-i-6 value.
- Writer read: no non-terminal order of any seat names `reports/retention.py`, `reports/tests/test_retention.py`, the registry file or the lib test file (4,241 order files scanned); `reports/retention.py` is `2.0.0_SA_COO~P`'s lane and this order is its only writer this round.
- Tests use fakes; no live AWS call (the live read of a stored v1 row is the issuer's act).
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W3-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/logic/registry/reporting_policies.json
lib/tests/test_irpt_destination.py
infra/aws/lambda/investor-reporting/reports/retention.py
infra/aws/lambda/investor-reporting/reports/tests/test_retention.py
infra/aws/lambda/investor-reporting/reports/*.py
infra/aws/lambda/investor-reporting/reports/tests/*.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/generate/publisher.py
infra/aws/lambda/investor-reporting/ycharts/generate/publication_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publisher.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publication_worker.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the irpt-x10-v1 policy's policy_sha256 equals its pre-i-6 value and carries no OPAL_REPORT_PDF family (tests -k v1_policy_digest_unchanged, >= 1 passed)
- **AC2** -- the retention check resolves the policy from the reference's own policy_revision (tests -k resolves_policy_from_reference_revision, >= 1 passed)
- **AC3** -- a v1 reference validates exactly as before (tests -k v1_reference_validates_unchanged, >= 1 passed)
- **AC4** -- a revision that is not registered, or not ACTIVE, is refused (tests -k unregistered_or_inactive_revision_refused, >= 1 passed)
- **AC5** -- the producer retains the PDF under irpt-ycdgen-research-v1 family YCHARTS_OPAL_REPORT (tests -k retains_pdf_under_ycdgen_research_policy, >= 1 passed)
- **AC6** -- the whole retention test file passes untouched (tests, all, no failure)
- **AC7** -- the whole publisher test file passes (tests, all, no failure)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-l-6"><invocation>python -m pytest lib/tests/test_irpt_destination.py -q -p no:cacheprovider -k v1_policy_digest_unchanged</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-l-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/reports/tests/test_retention.py -q -p no:cacheprovider -k resolves_policy_from_reference_revision</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-l-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/reports/tests/test_retention.py -q -p no:cacheprovider -k v1_reference_validates_unchanged</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-l-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/reports/tests/test_retention.py -q -p no:cacheprovider -k unregistered_or_inactive_revision_refused</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC5" cell_refs="YCD-l-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py -q -p no:cacheprovider -k retains_pdf_under_ycdgen_research_policy</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC6" cell_refs="YCD-l-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/reports/tests/test_retention.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
  <criterion id="AC7" cell_refs="YCD-l-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publisher.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~3/IRPT_YCDGEN.TO-YCD-l-6.opal-pdf-own-policy-and-retention-resolves-policy.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-l-6.opal-pdf-own-policy-and-retention-resolves-policy`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~3`, third order (after g-6 and i-6, merged); addendum D cell (decomposition IRPT_YCDGEN_DECOMP_R6D.md), the implementation of the CTO's ruling batch 269 (msg 105429) on row W3-S14. AC1 runs in lib/tests/test_irpt_destination.py, AC5 in test_opal_producer.py and AC7 in test_publisher.py. Runs BEFORE k-6. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-06 ~00:0xZ):** worker 0.9.0_WK_IRPT_YCDGEN~3 @f60e6f1d2a, merged 6e4e325b5d; l-6.AC1-AC7 PASS on the merged tree (lib test_irpt_destination 73 passed; test_retention 21 passed, 18 existing untouched plus 3 new; publisher 25 passed), instance VALID. The irpt-x10-v1 policy_sha256 is e0046398e23951451498c0fcfec29154db5b26d4c70d80c4121f50fd3dfc8c85, printed from `opal_naming.reporting_policy('irpt-x10-v1')` after the edit and equal to the pre-i-6 ACTIVE_ROW_SHA; the registry and the lib test were byte-restored from e923e0f463^. retention.py resolves the policy from the reference's own policy_revision among ACTIVE registered revisions (`_registered`), POLICY_REVISION kept as the default for new reservations (composition.py and ops/pdf_link.py import it); repository.py binds against the reference's revision; composition.build_retained_repositories takes an opt-in additional_policy_revisions. The Opal PDF is retained as YCHARTS_OPAL_REPORT under irpt-ycdgen-research-v1. Row W3-S14 DISARMED. W3-S17 ARMED (resident_worker.py:122 and :429 still put the PDF as OPAL_REPORT_PDF; four d-6 tests in test_resident_worker.py are red on CLOUD until k-6; the installer does not pass the research revision) -> DISARMED by cell YCD-k-6. W3-S18 INERT, accepted (the pre-existing `extract` import failure, identical on the base). CTO batch 269 items 4-6 remain: the live read of one stored v1 row and the deployed-versus-built v1 digest are the issuer's acts at the close; the research row goes ACTIVE only on the CTO's acceptance; everything ships with d-6 and g-6 in one packet.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<workstream>R6D_POLICY</workstream>
<slot>~3</slot>
<fabric>laptop</fabric>
