# NFRA_MCPINDEX task order -- `MX-o-1` -- the operations lead's trade reconciliation: find its served source by census, then serve it in the fixture's row shape, or ship a GAP

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-o-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-o-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~30</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; a reader answers on call.
comp-iam: DECLARED-NOT-APPLICABLE at the cut -- the reader reads served objects under the gateway role's existing grant. If the surviving source sits outside that grant, that is a BLOCKING row naming the prefix, never a policy edit.
comp-adversary: DECLARED-NOT-APPLICABLE -- the battery dry-run is the control (o1.AC1-AC3 read FAIL at base, census absent).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 reads).
</preflight>

## 1. THE CELL -- `MX-o-1` (round 9; PRD v0.8 @0eff9e0e6d FWD-19, v0.8 addendum contracts 1-3; decomposition section ROUND 9)

**What the user sees at the base.** The operations lead reconciles trades by hand. He compares Opal's view of each
trade with the custodian's. Claude cannot answer "did the custodian settle our trades": discover reads NOT_CATALOGUED.
The ops kit on dell2 (NFRA_OPSWKF) ships fixture rows from `tools/ops_kit/fixtures/trade_rec.json`, a top-level
`as_of` plus 12 `rows`. Each row has the fields `account custodian trade_date symbol side quantity opal_status
custodian_status matched`. FWD-19 makes this answerable in Claude from one server. The fixture is the SHAPE and a test
input only. A fixture value is never served as data (contract 1).

**The act:**
1. **The census first (contract 2: found, never assumed).** Write
   `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~30/census_trade_rec.json` in the shape
   `ops_census.py` documents (its docstring is the contract):
   - every candidate producer of a per-trade Opal status and a custodian status, each with its own denominator and
     `denominator_of`. The PRD names two candidates, and they are candidates only: the trade engine's statuses, and
     the custodian silver transactions (Schwab and Black Diamond silver `transactions` under the served buckets).
     Look for others too.
   - `served` true only for a producer whose objects are SERVED today (a scheduled producer writing a served
     prefix), not a one-off file.
   - a verdict:
     - SERVED: the surviving source, read ONCE, with `read_once_at`, `rows_read` and the `probe_scope` the live probe
       reads.
     - GAP: no served source carries both statuses. Name the `owner` (the project that would have to produce it, or
       `unowned`). Then build NO reader. The census and the row are the cell's output, and FWD-19 is not done.
2. **SERVED branch -- the reader.** Write `infra/aws/ec2/opal-gateway/app/integrations/ops_trade_rec/` (an
   `__init__.py` plus `integration.py`), modelled on `app/integrations/blackdiamond/integration.py`:
   - `TOOL = "<name>"` -- the tool name is builder output or validated by the gateway's tool-name rule (rule 30,
     C3). If the naming gate refuses, that is a BLOCKING row with the gate line, never a hand-typed workaround.
   - `read(s3, principal, scope, date_from=None, date_to=None) -> dict` returning exactly
     `{scope, as_of, as_of_claim, completeness, rows}`:
     - `rows` carry exactly the fixture's nine fields.
     - `as_of` is read from the served object at answer time, `as_of_claim: "measured"` (contract 3, C4).
     - `completeness` states what fraction of the scope's accounts the rows cover, with its denominator.
   - **C7 isolation:** one firm or master scope per call. A principal outside that scope is refused. Nothing is summed
     across firms or masters.
   - Register the tool the way the blackdiamond integration does (its `register(...)`), but do NOT edit `registry.py`
     or any `.env` or `ENABLED_INTEGRATIONS`. The registry hookup line is added at the drain (C10), and enabling is
     MX-r-10's.
   - Tests in `infra/aws/ec2/opal-gateway/tests/test_ops_trade_rec.py`, offline, with the fixture as the INPUT: the
     three named in o1.AC2, plus anything else you need. Every existing gateway test outside your files is untouched.

## 2. BOUNDS

1. Read only. No alert, notification or monitor (contract 4, moratorium). No write to AWS. No grant, role or policy
   change. No Terraform. No deploy (MX-r-10 releases this). No push.
2. You never edit the catalog: the entry is MX-c-7's, cut from your census.
3. Never another firm's data in a pipeline tree (bucket or key-prefix). Read the custodian silver of the asked scope
   only.
4. REFUSE a criterion you cannot meet as written, and report it with its measurement.
5. A naming-place refusal may switch on at the next trunk take. A new infra name the canon cannot place BLOCKS the
   commit. Report the gate line; never use the override.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/ops_trade_rec/
infra/aws/ec2/opal-gateway/tests/test_ops_trade_rec.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~30/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W30-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp, never a placeholder.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-o-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round9/checks/o1.AC1.sh; echo "exit=$?"</invocation><expect>census trade_rec: candidates n (n >= 2), each with a denominator n of n; verdict SERVED or GAP; violations 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-o-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round9/checks/o1.AC2.sh; echo "exit=$?"</invocation><expect>SERVED: pytest rc=0; named tests passed 3 of 3; failed/error tests 0. GAP: no reader built -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-o-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round9/checks/o1.AC3.sh; echo "exit=$?"</invocation><expect>SERVED: rows n (n >= 1), fixture keys n of n rows exact; as_of stated, claim measured; completeness stated; violations 0. GAP: PASS by branch -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~30/NFRA_MCPINDEX.TO-MX-o-1.ops-trade-rec-reader.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`, then flip `<status>` to complete and commit the instance,
deliverables and flip together. Report once, naming the census table (producer, denominator, served), the verdict, and
on SERVED the tool name and the probe's row count and as-of. After this order the issuer continues you with MX-c-7.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 9, chain [MX-o-1 -> MX-c-7 -> MX-r-10]. STAGED UNISSUED 2026-10-09 ~10:2xZ,
per 1.0.0_SA_CTO~Z's ruling @ff362e8444: round 9 issues after round 8's drain and L10. Battery dry-run at base
1dd356991a (`round9/checks/`):
- o1.AC1 FAIL as expected: census absent.
- o1.AC2 and o1.AC3 FAIL as expected: census absent.

ISSUED 2026-10-10 ~23:4xZ in round 9's ONE issuance, from `ledger/ROUND_ANALYSIS.round8.md` @d2eb6c471b. Battery re-dry-run at issuance base bf8492f48f: every check of this order FAILS there as a build check must.

<status>complete</status>
<round>9</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
