# TO IRPT_DASHBD.TO-DB-b-161 -- what the custodian and Black Diamond say they do: their own published method text for when a flow is taken to arrive, quoted with its source and date; no login, no vendor pull, no account data sent

<to_id>IRPT_DASHBD.TO-DB-b-161</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~130</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>83</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-83 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_83_20261011.md` @3f7c91e682, section 3 item 4 | **Rows:** NONE | **Decomp cell:** `DB-b-161` (decomposition section 85) | **outcome_ref:** FWD-8 / C-FLOWTIME | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-130` (branch `wk-irpt-dashbd-83-130`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~130/`. Read first: the analysis above, whole (it is one page), and the records this order names.

**Why.** The tie-out shows the other system does not use END, and cannot tell START from MID (47 of 51 close under both). The CTO: "a
read of their own published method text for when a flow is taken to arrive, quoted with its source and date, by a seat with open
egress; no login, no vendor pull, no account data sent. If nothing published says it, that is the answer and it is written down."

**The cell (`DB-b-161`).** Public reading. You change no code.
1. **Name the two parties from this project's own records**, not from memory: the custodian whose reporting-performance pull the
   tie-out compares against, and Black Diamond (the PRD's C-TIEOUT and C-FLOWTIME, `org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`; and
   `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~118/FIGURE_PRODUCERS.json` for which pull the figures came from). `parties`:
   [{party: "CUSTODIAN", name, ...}, {party: "BLACK_DIAMOND", name, ...}]. Say which of the two the 51 segments were scored against.
2. **Find each party's own published text** on how its time-weighted return treats an external cash flow on the day it occurs:
   start of day, end of day, midpoint (Modified Dietz within the day), or by the actual time. Look for the party's performance
   methodology, calculation disclosure, help-centre or GIPS-related pages. `sources`: [{url, retrieved_utc (read `date -u`, never
   typed), found ("QUOTED" or "NOTHING_ON_FLOW_TIMING"), quote (the party's words, verbatim, short), where (document title and
   section), strength ("PARTY_METHOD_DOCUMENT", "PARTY_HELP_PAGE" or "THIRD_PARTY")}]. Save each fetched page privately under
   `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~130/` so the quote can be re-read; do not commit the pages.
3. **Answer per party**: `convention` (START, END, MID, OTHER or NOT_PUBLISHED) with `basis`. A convention other than NOT_PUBLISHED
   needs at least one QUOTED source that is the party's own; a third party's statement alone is NOT_PUBLISHED with the third party
   listed. A page that needs a login is not read: list it under `behind_login` with its address. Do not infer the convention from
   the tie-out; this cell reads what is PUBLISHED.
4. `searches` (every query and address tried, including the ones that found nothing), `no_login: true`,
   `no_account_data_sent: true`. Record `PUBLISHED_FLOW_TIMING.json`. ASCII only: replace any typographic quote or dash in a quotation
   with its plain form and say that you did.
5. **In every record of this round (item 5): `the_39`** {count: 39, accrual_class: 31, unclassed: 8, statement}. The statement says in a
   sentence that 39 of the 90 two-sided segments close under NO timing (31 of the accrual class, 8 unclassed), that nothing in this
   record changes them, and that a change of convention would not close the tie-out. A reader who quotes a number from your record
   must meet that sentence beside it.

<criterion id="DB83-4-AC1" cell_refs="DB-b-161"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r83/p83_round83.py" . DB83-4-AC1</invocation><expect>DB83-4-AC1 PASS</expect></criterion>
`DB83-4-AC1` -- for the custodian and for Black Diamond, the published text on flow timing is quoted with its address and retrieval time, or it is written down that nothing published says it, with the searches made. Base: FAIL.

<expected_criteria>DB83-4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no `upload=True` call; no deploy; no push. No AWS call at all. PUBLIC WEB READS only (plain `curl` of public pages and public documents): no login, no API key, no vendor session, no form submission, and nothing about any account, client or figure in any request. Never Bloomberg.
- **No client data in what you write.** Counts and booleans only: no account id, no client name, no figure of any client. Anything you
  download goes OUTSIDE the repo, under `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~130/`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a
  defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W130-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~130/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-161.published-flow-timing-custodian-and-black-diamond.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 85 (round 83), cell `DB-b-161`.
<owned_cells>DB-b-161</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB83-4-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~130/IRPT_DASHBD.TO-DB-b-161.published-flow-timing-custodian-and-black-diamond.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB83-4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; for each party, what its own published text says about when a flow is taken to arrive, quoted, with the address and the retrieval time, or that nothing published says it; every search and page you tried; how strong each source is (the party's own method document, its help page, a third party quoting it); the sentence on the 39; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a record of quotations from public pages; nothing served, nothing sent.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled producer runs from its source-map pins, not from this branch.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record). The rows are the reviewer's and the CTO's statements; the issuer re-read none of their evidence for this issuance.
lane: the <paths> block IS the grant.
</preflight>
