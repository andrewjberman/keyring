# AMGT_RESAPP task order -- `AMGT-yy-2` -- /THESIS PASSES THE DOSSIER'S SERVED FIELDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-yy-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~177</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for this cell's own acts. The Lambda already reads the dossier (s3:GetObject on amgt/harvest/gold/research_dossier/, granted round 48); this cell must call no new AWS action.
comp-adversary: RUN by the issuer at the cut -- AC1 compares the payload to read_dossier field by field on four names, the ABSENT branch included; AC2 is the API and print suites (the bound).
EGRESS CLASS, declared: NONE beyond Opal's own S3, read-only.
</preflight>

## 1. THE CELL -- `AMGT-yy-2` (round 50, decomposition s.58)

`GET /api/scoped/amgt/security/<key>/thesis` (`lib/research/api/scoped_amgt.py`, `read_thesis_bundle` and the thesis route) reads
the research dossier through `lib.research.corpus.dossier.read_dossier(key)` but passes ONLY the team's cases (`model.team_cases`,
`_team_cases` ~`:3105-3132`). The dossier's `document.fields` also hold, measured at the cut on AZN_LN_Equity:
- `thesis_pillars` -- a list; each pillar carries its text, a `citation` and `terms`;
- `management`, `fund_of_record`, `last_stated_position` -- each `{"value": ..., "citation": {...}}` or `{"absent": "<reason>",
  "value": None}`.
On the four names AZN_LN, IMB_LN, AMD_US, ADBE_US the dossier holds 15 pillars; /thesis serves 0.

**Build:** the /thesis payload gains ONE top-level object `dossier_fields`, read from the SAME single `read_dossier` call the team
cases already use (no second read):
- `dossier_fields.thesis_pillars` -- every dossier pillar, in order, as the dossier holds it (text, citation, `terms`), none dropped,
  none re-worded;
- `dossier_fields.management`, `.fund_of_record`, `.last_stated_position` -- each as the dossier holds it: when the dossier's
  `value` is not null, `{"status": "SERVED", "value": <verbatim>, "citation": <verbatim>}`; when null,
  `{"status": "ABSENT", "value": null, "reason": <the dossier's own absent text>}`;
- a dossier that cannot be read -> `dossier_fields` is `{"status": "READ_FAILED", "reason": ...}`, never an empty object, and the
  rest of /thesis is unchanged.
Nothing else in the payload moves. Tests (stubbed dossier) pin: pillars verbatim with terms, each scalar's SERVED and ABSENT branch,
READ_FAILED distinct from ABSENT, and every pre-existing /thesis key byte-unchanged.

## 2. BOUNDS

1. **The adapter only.** No page file, no export file, no Terraform, no S3 write, no new AWS action.
2. No deploy, no server. Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
3. Python from the repo root with `PYTHONPATH="$(pwd)"`. Another order on your slot (yy-3) edits `scoped_amgt.py` after you.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~177/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-yy-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_thesis.py --plane local --what fields; echo "exit=$?"</invocation><expect>plane local: pillars 13 of 13 over 4 names (the dossier's LIST count; AMD_US's pillars field is ABSENT and serves [] + thesis_pillars_absent), no BAD line, /THESIS PASSES THE DOSSIER'S FIELDS: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-yy-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/api-suite.sh; echo "exit=$?"</invocation><expect>pytest reports N passed and 0 failed (plus your new tests) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the built pass-through against the real dossier; AC2 the bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~177/AMGT_RESAPP.TO-AMGT-yy-2.thesis-passes-the-dossier-fields.proof_of_spec.json`. Report once: what you changed, the payload shape, the counts, the commit hashes, and any row. Then wait: your slot continues with yy-3.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-49 analysis s.4 row 2 (CORPUS FWD-10/11/12/15/16/18 render halves, round-48 s.4b). Base: AC1 FAIL (pillars
0 of 15, no dossier_fields), AC2 PASS. SERVED at yy-5.

**AMENDMENT 1 (2026-09-29 ~23:5xZ, issuer 2.0.0_SA_COO~Z):** the check counted an ABSENT pillars object (`{absent, value}`) as len(dict) = 2 pillars, so AC1 read 15 where the dossier holds 13 (AZN 5, IMB 6, ADBE 2, AMD 0 -- AMD's field is ABSENT: 'no class A report for this security'). Row Z-W177-S1 (the worker's, BLOCKING/INERT). Ruled: pillars are counted from a LIST only; an absent field serves `thesis_pillars: []` plus `thesis_pillars_absent: {status: ABSENT, reason}` (the worker's shape, adopted). Check file and expect amended. Gate: GATE (viii) grades this modified order (it declares `<placeholders>`).

<status>pending</status>
**ISSUER CLOSE (`2.0.0_SA_COO~Z`, 2026-09-29 ~23:5xZ):** drained @5941a98591 (worker f0cce70bfa + 80432a6294; 5 files, 0 dropped/foreign). The worker's AC1 read FAIL on the CHECK's miscount (an ABSENT pillars object counted as 2), not on the build -- ruled in AMENDMENT 1 @41b61bd72e. Instance graded in the worker's tree: VALID rc=0 (it records AC1 FAIL against the pre-amendment check). The issuer re-ran both criteria on the MERGED full tree under the amendment: AC1 PASS (pillars 13 of 13 over 4 names), AC2 PASS (338 passed). SERVED at yy-5. Worker ~177 continues with yy-3.
<status>complete</status>
<round>50</round>
<slot>~177</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
