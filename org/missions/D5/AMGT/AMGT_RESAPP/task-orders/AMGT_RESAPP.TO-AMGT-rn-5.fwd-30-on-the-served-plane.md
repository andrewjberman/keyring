# AMGT_RESAPP task order -- `AMGT-rn-5` -- FWD-30 ON THE SERVED PLANE: the field-by-field comparison re-run against the deployed function's own responses

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rn-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~150</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for writes -- the cell READS one deployed function through the box's own credentials (lambda:InvokeFunction and GetFunctionConfiguration on opal-amgt-scoped-api, the same reads rm-7's lane made); it grants nothing.
comp-adversary: RUN by the issuer over the round-38 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: ONE AWS READ SURFACE -- `lambda invoke` of Opal's own `opal-amgt-scoped-api` (account 313476888478), GET routes only, for BA_US_Equity; no S3 write, no vendor, no server.
</preflight>

## 1. THE CELL -- `AMGT-rn-5` (round 39, decomposition s.47)

`FWD-30` was graded REALIZED with its 162/162 figures, 43/43 cites and 5/5 absences verified IN-PROCESS on the producer before the
deploy; nobody re-ran the comparison against the SERVED response. **Build:** (1) `served_capture.py` under your deliverables:
invokes the deployed function (the event shape `org/tier2_senior/0.7.0_AE_CloudOps~A/deliverables/AMGT_RESAPP_RM4B_20260924/verify_after.py:71-76`
uses -- `rawPath`, `requestContext.http`, `queryStringParameters`) for BA_US_Equity on every route the page reads
(the route table the harness router names, `portal/scripts/ui-smoke.mjs`'s fixture router, and `tabsFixture.BA_US_Equity.json`'s
own top-level keys), writes `served/served_fixture.BA_US_Equity.json` shaped like `tabsFixture.BA_US_Equity.json` with a
`_served` block (`function`, `code_sha256` from GetFunctionConfiguration, `invoked_at`, `routes` list), and writes the served rich
body (`GET .../print?format=rich`) to `served/BA_US_Equity.rich.md`; (2) `exportCompare.harness.cjs` gains `--fixture <path>` so
the page half renders from the SERVED fixture instead of the landed one (default unchanged); (3) run the comparison. A mismatch is
recorded, never repaired: this cell measures.

## 2. BOUNDS

1. **No server; no write to AWS.** Read routes only. Standing: no install, no push, no promote. REFUSE, do not rescue.
2. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-150-portal` at DEV `5e339ffd`. Python from the
   repo root with `PYTHONPATH="$(pwd)"`; AWS through `.tools/aws` or boto3 as `verify_after.py` does.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~150/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rn-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/rn-5.AC1.py org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~150/served/served_fixture.BA_US_Equity.json; echo "exit=$?"</invocation><expect>landed top-level keys: N; served carries N of them; missing: none -- then _served provenance: ... -> OK -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rn-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round39/checks/rn-5.AC2.sh org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~150/served/served_fixture.BA_US_Equity.json org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~150/served/BA_US_Equity.rich.md; echo "exit=$?"</invocation><expect>the harness's own three set lines (figures n/n, cites m/m, absences k/k, each equal) on the SERVED fixture and the SERVED rich body, and exportCompare --rich on the served plane: rc=0, exit=0; a mismatch is the recorded output and a FAIL row, not a repair</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~150/AMGT_RESAPP.TO-AMGT-rn-5.fwd-30-on-the-served-plane.proof_of_spec.json`.
Report names the routes invoked (n of N), the CodeSha256 read, the three set counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER AMENDMENT 1 (2026-09-24 ~19:1xZ, row AMGT_RESAPP-W150-S1):** AC1's expect named words `checks/rn-5.AC1.py` never
prints; it now quotes the script's own line shape. The criterion's substance (every landed key served, provenance complete, exit 0)
is unchanged. Graded on this modification by GATE (viii) (the order declares `<placeholders>` at HEAD); no other limb reads a
modified order.

**ISSUER NOTES:** s.7 item 9. `<risk>SERVED</risk>` declared ABOVE the gate's LOCAL floor because the claim is about served output
(the CTO's read, msg 25671); no judgment criterion, so the CVO's grade reads the issuer's real-run record.

**ISSUER CLOSE, 2.0.0_SA_COO~Z, 2026-09-24 ~19:1xZ, carried on the worker's branch so the chain-end merge carries it.**
Complete AS A MEASUREMENT, which is what the face cut it to be ("a mismatch is recorded, never repaired: this cell measures").
proof-of-spec-check VALID rc=0 on the worker's instance. AC1: the recorded output ("landed top-level keys: 7; served carries 7 of
them; missing: none"; provenance OK; exit 0) meets the criterion; the worker's FAIL was against my face's wording, amended @c89e9febdf
(row W150-S1). AC2: FAIL, recorded verbatim and standing as the cell's finding -- on the SERVED plane FIGURES 162/162 with 17
rich-only, CITES 15/15, page absences covered 4 of 5 (the CIE_DES description line absent from the served rich body); on the LANDED
plane the same harness reads 5 of 5 and OK. Row AMGT_RESAPP-Z-S268 (BLOCKING, ARMED, disarm owner the CTO) carries it, with the
second finding the comparison exposed: on BOTH planes the export publishes 17 figures the page does not show, 10 of them the
IS_DIV_PER_SHR series the page REFUSES, and the harness computes extras without grading them -- so FWD-30's round-38 REALIZED grade
rested on an instrument blind to "NOTHING in the export that is not on the page". Routes invoked 5 of 5 (200); CodeSha256
y5bJBQsP8Q7Lfudb5nwc5wEr72IcH53uS5cz2T8bn/w=; no AWS write. Portal: exportCompare.harness.cjs gains --fixture (6d9e6744).

<status>complete</status>
<round>39</round>
<slot>~150</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
