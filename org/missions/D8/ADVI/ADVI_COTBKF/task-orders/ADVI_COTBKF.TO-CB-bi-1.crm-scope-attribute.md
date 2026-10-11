# TO ADVI_COTBKF.TO-CB-bi-1.crm-scope-attribute -- round 61 CB-bi-1: the CRM-scope selector reads an explicit registry attribute, not `masters`

<to_id>ADVI_COTBKF.TO-CB-bi-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~88</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>61</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bi-1` (`decompositions/ADVI_COTBKF_DECOMP.round61.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Read first:** the ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_CROSSBOX_XB-20261011T055236Z-0989_SHARED_INFRA_CRM_SCOPE_SELECTOR_20261011.md` (all of it), and `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` lines 1 to 110 and 180 to 260.

**The defect.** Line 197 of that `.tf` picks the firm whose bucket holds the restricted Commonwealth CRM prefix as "the ONE managed
FIRM row that carries masters", through `one()`. A second managed firm row now carries a true `masters` value (commit 5f962296ae),
so `one()` fails and every plan of the `shared-infra` root fails. `masters` was a proxy for a fact the registry does not carry.

**Your item. You run NO terraform command and make NO AWS call. Your branch is NOT merged by you.**

1. **Find the one row.** From the `.tf`'s own comments and git history (`git log -p -S"lgic_crm_scope" -- infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf`), establish which
   scope row the selector chose BEFORE 5f962296ae. That row, and only that row, holds the CRM prefix. State the evidence.
2. **Propose the attribute under CLAUDE.md rule 24** and write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~88/CRM_SCOPE_ATTRIBUTE_RULE24.json`:
   - `attribute`: the key name. It says the row's bucket holds the restricted Commonwealth CRM prefix. Read the 17 keys the scope
     rows already carry and `infra/logic/registry/scopes.json`'s `_about` block, and follow their naming and value conventions.
   - `shape`: its value type and what an absent key means (absent = the row does not hold it; no row needs editing but the one).
   - `postulates`: exactly four entries, one per postulate (MECE over a declared domain, with the domain printed and the uncovered
     member hunted by subtraction over ALL scope rows; same grain; intent coherence; state coherence), each with file-and-line
     evidence.
   - `token_census`: a list of `{"token": "...", "hits": n, "files": n, "denominator": "..."}` from `comp-find` with a word-boundary
     pattern and `--limit`, for the proposed name AND at least two rejected candidates. Never pipe `comp-find` into `head`, `tail`
     or `grep`: the rail denies it. A name with existing hits in the corpus is a collision you must explain or avoid.
   - `row`: the key of the one row that gets it; `rejected`: the candidates you rejected and why; `strongest_case_against`.
3. **Edit, two files.**
   - `infra/logic/registry/scopes.json`: add the attribute to that ONE row. Change nothing else in the file; keep its formatting byte-for-byte elsewhere.
   - `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` line 197: the comprehension selects the managed row that carries the attribute, still inside `one()`, still through
     `lookup(...)`. Update the comment block above it (lines 188 to 191) to say what it now reads. No firm token is typed.
4. **Do not run terraform.** The plan proof is the next cell's (`CB-bi-2`), run on your worktree by another seat. Leave the worktree
   clean and committed.

### ACCEPTANCE

<criterion id="CB61bi1-AC1" cell_refs="CB-bi-1"><invocation>python -c "import json,re;r=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~88/CRM_SCOPE_ATTRIBUTE_RULE24.json',encoding='utf-8'));a=r['attribute'];s=json.load(open('infra/logic/registry/scopes.json',encoding='utf-8'))['scopes'];m=[x for x in s if x.get('class')=='FIRM' and (x.get('bucket_managed_by','')=='s3-lgic-firm-buckets.tf' or (x.get('bucket_managed_by','')=='' and x.get('bucket_provisioned') is False))];h=[x for x in m if x.get(a)];t=open('infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf',encoding='utf-8').read();l=[y for y in t.splitlines() if re.match(r'\s*lgic_crm_scope\s*=',y)];print('CRM-SCOPE-SELECT managed_firm_rows=%d rows_with_attribute=%d selector_lines=%d reads_attribute=%s reads_masters=%s postulates=%d census_tokens=%d'%(len(m),len(h),len(l),a in l[0],'masters' in l[0],len(r['postulates']),len(r['token_census'])))"</invocation><expect>CRM-SCOPE-SELECT managed_firm_rows=2 rows_with_attribute=1 selector_lines=1 reads_attribute=True reads_masters=False postulates=4</expect></criterion>
`CB61bi1-AC1` -- exactly one of the 2 managed firm rows carries the attribute, the one selector line reads it and no longer reads
`masters`, and the record carries four postulates and its census.

<criterion id="CB61bi1-AC2" cell_refs="CB-bi-1" judgment="true"/>
`CB61bi1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- the row chosen is the row the selector chose before 5f962296ae, on the cited evidence;
- each postulate's evidence resolves at its cited line, and the subtraction ran over every scope row;
- the token census carries denominators and the name collides with nothing.

<expected_criteria>CB61bi1-AC1,CB61bi1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, your deliverables folder and the file of this order.
- **Do NOT touch:** any other `.tf`, any other registry file, `lib/`, any other row of `scopes.json`.
- **No terraform command, no AWS call, no push, no merge.**
- **Gates.** The naming gate grades the `.tf` at commit and the owned-paths gate grades the registry file's lane. If either REFUSES
  your commit, do NOT override it and do not reword to get past it: stop and report the exact refusal text. A refusal of the
  registry path for lane reasons is expected to be possible and is information the issuer needs.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W88-S<k>`, `"fabric": "dell2"`, its `surfaced_at` read from the clock). Do not weaken a check.

**AMENDMENT 1 (issuer, 2026-10-11 ~06:0xZ) -- the schema owner's terms (laptop `1.0.0_SA_CTO`, relayed by `0.0.0_AB_MSTR~DELL2` msg 4232, bus cbed2121).**
The answer to the ruling's item 4 is YES, on terms that bind this cell:
- ONE new VIEW field on the firm's `scopes.json` row, valued as a LIST of `systems.json` keys (for example
  `restricted_prefix_hosts: ["commonwealth"]`), NOT a boolean naming the CRM. The spelling is this cell's to propose under rule 24.
- The selector keeps `one()` over the managed rows whose list contains the system token the `.tf` already carries.
- `_about.view_fields` in `scopes.json` names the field; `lib/opal_naming.py` validate passes. `lib/` is not granted: a validator
  failure that needs a `lib/` edit is the refusal clause.
- The record carries `value_domain`, and a postulate checks every listed value is a `systems.json` key.
- `CB61bi1-AC1` is unchanged. The report adds the validate output line and the `_about.view_fields` diff.
The laptop's rulings file (`CTO_RULINGS_CLUSTER_TICK4_20261011_0557Z.md` @30646c2598, on origin box/laptop) is not on this box yet;
the terms above are the relay's text, not a read of that file.

<paths>
infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf
infra/logic/registry/scopes.json
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round61.md</decomp_doc> (round 61), cell `CB-bi-1`.
<owned_cells>CB-bi-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB61bi1-AC1, CB61bi1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~88/ADVI_COTBKF.TO-CB-bi-1.crm-scope-attribute.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB61bi1-AC1,CB61bi1-AC2` BEFORE the flip. Mechanical: CB61bi1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:**
- the attribute's name, shape and the row that carries it, with the evidence for the row;
- the `CRM-SCOPE-SELECT` line;
- the token census lines with their denominators;
- the exact diff of the two edited files (they are short);
- commits; every gate refusal or warning, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a registry attribute and one selector line; no schedule reads either. The plan of the root that reads both is the next cell.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call in this cell; the bucket policy statements the selector feeds are graded by the plan in CB-bi-2.
comp-adversary: RUN -- the row is fixed by the selector's own history, not by a guess; the check counts managed rows and rows with the attribute from the registry itself and reads the selector line; the name is censused against the corpus; BLIND: other readers of scopes.json that validate its keys against a closed schema (a registry check or a module) are not exercised here, and the laptop CTO owns that schema.
lane: the <paths> block IS the grant (worker RULING 1); infra/logic/registry is the LGIC canon's and its landing waits on the laptop 1.0.0_SA_CTO's acceptance (the ruling's item 4).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ruling @27ba4d3769 (msg 4216); cross-box call XB-20261011T055236Z-0989; cell CB-d-4 (FWD-7); commit 5f962296ae.
