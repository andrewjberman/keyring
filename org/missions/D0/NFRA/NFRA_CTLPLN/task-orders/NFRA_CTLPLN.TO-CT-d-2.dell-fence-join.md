# TO NFRA_CTLPLN.TO-CT-d-2 -- round 4 CT-d-2: the fence join -- each Dell user admitted to the firm buckets its placed work uses, and no other

<to_id>NFRA_CTLPLN.TO-CT-d-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~6</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-d-2` (`decompositions/NFRA_CTLPLN_DECOMP.round4.md`) | **outcome_ref:** FWD-10 |
**depends_on:** CT-d-1 (its census and placement map), merged before this order is handed

**STAGED ON A CONFIRMATION.** The list of admissions is CT-d-1's gap list, and it is a list of cross-firm access. The issuer hands this
order only after `1.0.0_SA_CTO` has confirmed that list, and writes the confirmed list into this face as an amendment. A worker never
starts it while `<status>` reads `staged`.

---

## WORKER FACE

### THE CELL

`CT-d-2`, the CTO's round-4 first cell (msg 106061): "the two Dell users joined to each fence whose firm's work is placed on that Dell,
in the fence's own Terraform, as one laptop apply under its pair. Cross-firm law holds: admit by placement, never all buckets to both."
You edit the Terraform and prove the edit statically. You APPLY NOTHING.

**What exists after CT-d-1:** `infra/aws/terraform/shared-infra/tests/dell_fence_census.py` and its saved result
`tests/dell_fence_census.json`: per bucket its fence, the admitted list, where it is declared, and per Dell the gap list. The firm-bucket
fences are declared in `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` and `infra/aws/terraform/shared-infra/s3-49financial.tf`.
THE CONFIRMED ADMISSIONS are in this order's AMENDMENT 1 at the end of the file: a list of (Dell user, bucket) pairs. That list, and
nothing derived by you, is what you join.

**Build:**

1. For each confirmed pair, add that Dell user's ARN to that bucket's fence, in the SAME construct the fence already uses for its
   admitted principals (the same list, local or variable), in the file where the census says it is declared. No new statement, no
   new Allow, no change to any other principal's entry, no change to a bucket not in the list. If a fence builds its list from a shared
   local used by several buckets, do NOT add the Dell user to the shared local: give the listed bucket its own extension of it, so no
   other bucket gains the user, and say how you did it. A pair whose bucket is `UNDECLARED` in the census is NOT joined: list it in your
   report and file one row.
2. `infra/aws/terraform/shared-infra/tests/check_dell_fence_join.py` -- the static check. It reads the confirmed pairs from a small
   JSON file you write beside it (`tests/dell_fence_join_pairs.json`, copied from AMENDMENT 1), and reads the two `.tf` files as text
   plus `terraform -chdir=infra/aws/terraform/shared-infra validate` (run `init -backend=false -input=false` first; if validate cannot
   run inside 120 s, record that and keep the text checks). It asserts: every confirmed pair's user appears in that bucket's fence;
   NO Dell user appears in the fence of any bucket outside the list for that user (the cross-firm arm); the diff of the two files
   against `HEAD~` touches only lines that add a Dell user ARN (print the changed-line count). Then, for each pair, it evaluates the
   EDITED policy: build the bucket's policy document as it would be after the edit (the live document from the census with the user
   added to the admitted list) and call `iam simulate-principal-policy` for that user on `s3:GetObject` with it as the resource policy;
   and for one (Dell user, bucket) NOT in the list, the same call with the live document must not return `allowed`.
   LAST line `FENCE-JOIN pairs=<k> joined=<j>/<k> cross_firm_leaks=<x> evaluator_allowed=<a>/<k> negative_arm=<denied|ALLOWED> other_lines_changed=<o> ok=<True|False>`,
   `ok=True` only when `j == k`, `x == 0`, `a == k`, the negative arm is `denied` and `o == 0`.

### ACCEPTANCE

<criterion id="CT4d2-AC1" cell_refs="CT-d-2"><invocation>python infra/aws/terraform/shared-infra/tests/check_dell_fence_join.py</invocation><expect>typed_in_tf=0 cross_firm_leaks=0</expect></criterion>
`CT4d2-AC1` -- no Dell user is admitted to a bucket outside its confirmed list. The same line must read `other_lines_changed=0`,
`negative_arm=denied` and `ok=True`, stated in the proof row; the `joined` and `evaluator_allowed` counts equal the pair count.

<expected_criteria>CT4d2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No apply, no `terraform plan` against the backend, no AWS write.** AWS calls allowed, read-only: `iam simulate-principal-policy`,
  `sts get-caller-identity`. No object read.
- Firm bucket names appear ONLY in the two `.tf` files (where they already are), in files under `tests/`, and in your final report.
  If the commit gate refuses a string, do not override: file a BLOCKING row and stop.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W6-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf
infra/aws/terraform/shared-infra/s3-49financial.tf
infra/aws/terraform/shared-infra/tests/check_dell_fence_join.py
infra/aws/terraform/shared-infra/tests/dell_fence_join_pairs.json
infra/logic/registry/exemptions.json
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `tests/dell_fence_census.py`, `tests/dell_fence_census.json`, every other file
of `infra/aws/terraform/shared-infra/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round4.md</decomp_doc> (round 4), cell `CT-d-2`.
<owned_cells>CT-d-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT4d2-AC1. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~6/NFRA_CTLPLN.TO-CT-d-2.dell-fence-join.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT4d2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the last line; per pair the file and line edited and the construct used; every pair not joined and why; the changed-line
count; how a shared list was handled; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: RUN at the cut by the evaluator arms of CT4d2-AC1 (each confirmed pair allowed on the edited document; one unlisted pair not allowed on the live one); `comp-iam gaps` after the apply is the issuer's.
comp-adversary: RUN -- cross-firm leak through a shared principal list (the worker extends per bucket; the cross_firm_leaks arm reads every fence for both users); a widened fence (other_lines_changed counts any line that is not an added Dell ARN); admission by the worker's own derivation (the pairs come from the issuer's amendment after the CTO's confirmation, not from the worker); BLIND: a second control on the same data (a key policy, an access point) -- the live Dell read after the apply is the test.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO msg 106061 (b); CLAUDE.md hard stop "NEVER reference another firm's data from a pipeline tree" (the cross-firm law);
decomposition round 4 "Open at the CTO" item 2. Base dry-run at the cut: CT4d2-AC1 base FAIL as expected (the check does not exist).

## AMENDMENT 1 (2.0.0_SA_COO~C, 2026-10-07 ~09:0xZ) -- THE CONFIRMED ADMISSIONS; the order is handed (staged -> pending)

Authority: CT-d-1's census, merged @7cb0a2f3ab (24 of 24 data buckets read; 3 fenced; the evaluator agrees on 48 of 48 calls), and
`1.0.0_SA_CTO` msg 106089: "the principals admitted per bucket by placement (dell2: the three firms' data its five projects read;
dell1: what MDPF_SECHIST and MDPF_SECCLASS read)". Gate limb: none graded this modification.

**THE PAIRS (three, and only these):**

| Dell user | bucket | fence declared at | citing files of dell2-placed projects |
|---|---|---|---|
| `cloudops-dell2-agent-user` | `opal-data-49financial` | `infra/aws/terraform/shared-infra/s3-49financial.tf:122` | 17 |
| `cloudops-dell2-agent-user` | `opal-data-cottonwood` | `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf:142` (a `for_each` over the scopes registry) | 22 |
| `cloudops-dell2-agent-user` | `opal-data-inflection` | `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf:142` (the same `for_each`) | 14 |

**dell1 is joined to NO fence.** Its placed projects' buckets (the census's union for dell1) meet no fence today: `gap_dell1=0`. Do not
add `cloudops-dell1-agent-user` anywhere. The cross-firm arm of your check must show dell1 absent from all three fences and dell2
present in exactly these three.

**The shared construct.** Two of the three fences are ONE `for_each` resource over a registry, so the admitted list is very likely one
expression serving every firm bucket that resource builds. Adding dell2 there admits it to exactly the buckets that resource fences;
the census says that resource fences these two and no third. CONFIRM that from the Terraform before you edit (how many buckets does
the `for_each` produce, and is each one in the pairs?). If it produces a bucket that is NOT in the pairs, do not widen it: give the
listed buckets their own extension, as the face says, and say how. If the admitted list is read from a registry file (for example
`infra/logic/registry/scopes.json`) rather than typed in the `.tf`, that file is NOT in your grant: stop, file ONE BLOCKING row naming
the file and the key, and report -- the issuer amends the grant.

**The pairs file** `tests/dell_fence_join_pairs.json` holds exactly the three pairs above.

The saved census `tests/dell_fence_census.json` and its script are in your worktree after the merge of the trunk into your branch.

## AMENDMENT 2 (2.0.0_SA_COO~C, 2026-10-07 ~09:2xZ) -- REOPENED: the admissions are REGISTRY ROWS, never typed in the Terraform

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated and commits f15a6778a0 and a8baaeb291 are
inherited state. This branch is NOT merged to the trunk in its typed form. Gate limb: none graded this modification.
WHERE THIS AMENDMENT AND THE FACE DIFFER, THIS AMENDMENT GOVERNS.

**Why.** Your own row NFRA_CTLPLN-W6-S3 named it. The fence's doctrine, stated in `s3-49financial.tf` ("Neither list is typed here
(DEC-4 iii)") and in `infra/logic/registry/exemptions.json` `_about` ("The policy's exemption list, service principals included, is
generated from these rows and never typed"), and CLAUDE.md rule 30 (a pipeline's names and tenancy come from the canon and its
builders; a hand-typed workaround is never the answer to a missing registry row), make the route a ROW per bucket in
`exemptions.json`: `principal`, `arn`, `reason`, `signoff_ref`. The module `opal_name` already renders those rows into each fence
(`fence_exemption_arns`). A typed term also has the defect you flagged: any future firm bucket the shared `for_each` builds would gain
the user without anyone deciding it. A registry row is keyed by bucket and cannot leak that way.

**THE WORK:**

1. REVERT the two typed lines: `s3-49financial.tf` and `s3-lgic-firm-buckets.tf` return to their bytes at `3ec42c56bf` (write each
   from `git show 3ec42c56bf:<path>`; do not use checkout or reset). After this step
   `git diff 3ec42c56bf -- infra/aws/terraform/shared-infra/*.tf` prints nothing.
2. Add THREE rows to `infra/logic/registry/exemptions.json` (now in your grant), one under each of the keys
   `opal-data-49financial`, `opal-data-cottonwood`, `opal-data-inflection`, in the shape `_about.row_fields` gives and the existing
   rows show:
   - `principal`: `cloudops-dell2-agent-user`
   - `arn`: `arn:aws:iam::313476888478:user/cloudops-dell2-agent-user` (an IAM user, so the ARN is written)
   - `reason`: one sentence: the dell2 box's agent identity; dell2 is the placed box of the projects whose orders read this bucket
     (name the projects and the citing-file count from the pairs table of AMENDMENT 1); NFRA_CTLPLN CT-d-2; CTO msg 106061 and 106089.
   - `signoff_ref`: `org/critical_paths/change_management/` entry slug `nfra-ctlpln-dell2-fence-join-laptop-20261007` (opened at the
     apply); COO half `org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL2_FENCE_JOIN_20261007.md`; CTO half
     `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_NFRA_CTLPLN_DELL2_FENCE_JOIN_20261007.md`. (Both halves are written against
     your result; the paths are fixed here so the rows can cite them.)
   Add rows only; change no existing row, key or field; keep the file's formatting and line endings. No row under `opal-data-bd`,
   `opal-data-inf` or `opal-data-cot`, and none for `cloudops-dell1-agent-user` anywhere.
3. Run `python lib/opal_naming.py validate` before and after and record both last lines. If the validator refuses a row, do not
   weaken it or the row: record the refusal lines, file a BLOCKING row, stop.
4. Show that the module renders the rows: read `infra/aws/terraform/modules/opal_name/` to see how `fence_exemption_arns` is built
   from the file, then evaluate it for the three buckets (a small Python reading of the same JSON by the module's rule is acceptable
   if `terraform console` cannot run without the backend; say which you did) and print, per bucket, that the Dell ARN is in the
   rendered list.
5. Update `tests/check_dell_fence_join.py`: it now reads the pairs file and `exemptions.json`. It asserts: each pair has exactly one
   row under its bucket key; `cloudops-dell2-agent-user` appears under exactly those three keys and no other; `cloudops-dell1-agent-user`
   appears nowhere in the file; the registry diff against `3ec42c56bf` is exactly three added rows and nothing else
   (`other_rows_changed`); the two `.tf` files carry NO Dell user ARN and are byte-equal to `3ec42c56bf` (`typed_in_tf` counts Dell
   ARN occurrences in them); and the evaluator arms are unchanged (each pair `allowed` on the edited document, the negative arm not
   allowed on the live one). LAST line
   `FENCE-JOIN pairs=<k> rows=<j>/<k> typed_in_tf=<t> cross_firm_leaks=<x> evaluator_allowed=<a>/<k> negative_arm=<denied|ALLOWED> other_rows_changed=<o> validator=<ok|refused> ok=<True|False>`,
   `ok=True` only when `j == k`, `t == 0`, `x == 0`, `a == k`, the negative arm is `denied`, `o == 0` and the validator is `ok`.

**ACCEPTANCE, replacing CT4d2-AC1's expectation (same id, same invocation):** `typed_in_tf=0 cross_firm_leaks=0`, and the same line
reads `rows=3/3`, `other_rows_changed=0`, `validator=ok`, `negative_arm=denied` and `ok=True`, stated in the proof row.

Write a NEW proof instance over the old one at the same path, validate it, and flip `<status>` back to `complete` only when it passes.
In files outside `tests/` and outside the registry and the two `.tf` files, do not type a firm bucket's name: the registry is where
these names already live.
