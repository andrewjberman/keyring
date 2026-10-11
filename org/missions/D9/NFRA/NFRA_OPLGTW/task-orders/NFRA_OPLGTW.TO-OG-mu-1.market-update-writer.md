# NFRA_OPLGTW task order -- `OG-mu-1` -- the `.pptx` market_update writer made writable: one naming rule, one grant (E1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-mu-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-mu-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~55</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- Phase A builds and asks; no deploy, no plan apply, no release.
comp-iam: RUN-BY-ISSUER -- ONE new PutObject statement on opal-gateway-role for the market_update prefix of opal-data-transcripts; the KMS leg is live (row W49-S1, disarmed by Z-S76). Written here, UNAPPLIED; the apply is a later applier order under a signed pair.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-32 analysis @3566a85699 rows W49-S3 (RULED: one content-addressed rule) and W49-S4 (registry row first, then the grant), E1.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-mu-1` (decomposition addendum R3-T.42, E1). PHASE A only: build, test, ask.

`G` = `infra/aws/ec2/opal-gateway/`. `G/app/integrations/advi_billing/site_to_s3.py` copies ONE SharePoint item to S3,
selected from a table of two admitted pairs: `.xlsx` -> fee_statement, and `.pptx` -> market_update (built in OG-ab-2,
NOT released).

1. **One naming rule (row W49-S3).** The intake writer, `data/transcripts/scripts/updates/intake.py:57`, names a deck
   `address("sharepoint","transcripts","bronze","market_update","date=<placed date>","deck_<sha256[:16]><suffix>")`.
   Make the `.pptx` pair produce its key the SAME way: same partition, same `deck_<sha16>.pptx` name. Use the builder
   (`lib/opal_naming.address`), never a typed string. The placed date is the UTC date of the put. The sanitized original
   file name goes in the object's `Metadata` (key `original-name`), never in the key. The `.xlsx` pair is unchanged.
   The conditional put (`IfNoneMatch="*"`) stays: a second put of the same bytes on the same date is REFUSED as
   existing, not overwritten.
2. **Tests**, offline, in `G/tests/test_og_mu1.py`:
   - `test_ogmu1_ac01`: the `.pptx` key equals intake's form for the same bytes and date;
   - `test_ogmu1_ac02`: the same bytes on the same date from the tool and from intake's function give ONE key;
   - `test_ogmu1_ac03`: the original name is in Metadata and not in the key.
3. **The grant (row W49-S4, route (a)).** In `infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf` (or a
   sibling `.tf` in that root):
   - add a REQUIRED variable `market_update_s3_root` (no default), validated to end in `/bronze/market_update/`;
   - add ONE `s3:PutObject` statement whose resource derives from that variable;
   - hand-type no bucket or prefix literal (the commit-time naming gate refuses one).

   The plan will be fed `-var market_update_s3_root=<address() output>`, from the same `address()` call the deploy
   uses. Do NOT plan against AWS and do NOT apply.
4. **The never-widen ask**, `W/NEVER_WIDEN_ASK_OG-mu-1.md`, for TWO halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`). It
   carries:
   - the diff by file;
   - the one statement;
   - both branches of a call (refused writes nothing; admitted writes one new key);
   - writers N printed;
   - the order of acts (the grant, then a gateway release that carries this code);
   - rollback per act;
   - the residual: one deck placed on two different dates lands under two keys.
5. Run AC1 and AC2, commit, REPORT, STOP.
6. **(A1)** `tests/test_og_ab2_pairs.py::test_ogab2_ac02` asserts the OLD `.pptx` key form
   (`date=<arg>/<sanitized name>.pptx`), which step 1's ruling replaces (row Z-W55-S1). Re-pin ONLY that assertion to the
   content-addressed form: `date=<UTC put date>/deck_<sha16>.pptx`, the original name in `Metadata`. Change nothing
   else in that file; its other two tests stay as they are.

## 2. BOUNDS

- Code, tests, the one `.tf` file and the ask. No AWS write, no plan against AWS, no deploy, no release.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/advi_billing/
infra/aws/ec2/opal-gateway/tests/test_og_mu1.py
infra/aws/ec2/opal-gateway/tests/test_og_ab2_pairs.py
infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf
infra/aws/terraform/opal-gateway/variables.tf
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W55-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-mu-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/mu1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*test_advi_site_to_s3\.py: pytest rc=0.*test_og_ab2_pairs\.py: pytest rc=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-mu-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/mu1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)PutObject statements on the var: 1 \(want 1\); hand-typed market_update ARNs: 0 \(want 0\).*terraform validate: Success.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: one content-addressed rule for both writers, and E2 unchanged. `AC2`: one grant, builder-fed, validated.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-mu-1.market-update-writer.proof_of_spec.json` and validate it with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`. Phase A leaves the order
`pending`: the grant's apply and the release are later orders. Report once.
`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~55/`.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 34, E1. Row W49-S2 was answered by the CTO @6a81b7276e: `address()` builds market_update without refusal, so no
  registry row is owed.
- Pre-cut: mu1.AC1 base FAIL as expected (test file absent); mu1.AC2 base FAIL as expected (no variable; validate
  Success).
- A1 (issuer, 2026-10-11 ~17:0xZ, on row Z-W55-S1): the issuer's defect. The cut left `tests/test_og_ab2_pairs.py` out of
  `<paths>`, yet E1's ruling replaces the key form its `test_ogab2_ac02` pins, so AC1 could not pass. The file is added
  with step 6 (re-pin that one assertion). Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>34</round>
<slot>~55</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
