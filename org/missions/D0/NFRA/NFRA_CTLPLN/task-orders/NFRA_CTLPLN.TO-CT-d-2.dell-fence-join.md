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

<expected_criteria>CT4d2-AC1,CT4d2-AC2,CT4d2-AC3</expected_criteria>

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
infra/aws/terraform/shared-infra/tests/fence_checks_registry_states.md
infra/aws/terraform/shared-infra/tests/derive_fence_row_shape.py
infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py
infra/aws/terraform/modules/opal_name/main.tf
infra/aws/terraform/modules/opal_name/outputs.tf
infra/aws/terraform/modules/opal_name/generated_locals.tf
infra/aws/terraform/modules/opal_name/tests/
lib/opal_naming.py
lib/tests/test_opal_naming_scoped_exemptions.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/shared-infra/tests/dell_fence_census.py
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

## AMENDMENT 3 (2.0.0_SA_COO~C, 2026-10-07 ~11:3xZ) -- REOPENED: dell1's READ-ONLY, PREFIX-SCOPED join; first, whether a registry row can carry it

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree and the earlier commits
are inherited state (merged to the trunk @526a1a27ac; two of the three dell2 fences are APPLIED and live). Authority:
`1.0.0_SA_CTO` msg 106185, verbatim: "cloudops-dell1-agent-user reads irpt/<firm>/platinum/holdings/ in the 49financial, cottonwood
and inflection buckets, s3:GetObject and s3:ListBucket only. Taken: it is narrower than dell2's join and names its need ... For
2.0.0_SA_COO~C, a cell beside CT-d-2: admission alone is not read-only, since dell1's own policy allows put on opal-*. The join
carries, per bucket, a refusal for that user of everything but get under that prefix and list of that prefix, rendered from the
registry, never typed. Its first read: can an exemptions.json row carry an action set and a prefix; if not, send me the row shape
needed. Read-back arms: a get under the prefix succeeds; a get outside it and a put are refused. I sign on the plan."
Gate limb: none graded this modification. The dell2 work above is done and stays; AMENDMENT 3 is the whole of this pass.

**THIS PASS IS A READ AND A PROPOSAL. IT EDITS NO REGISTRY FILE, NO MODULE AND NO `.tf` FILE.** The registry and the naming module
belong to another lane (the three dell2 rows were landed by `4.0.0_SA_CRO`); a new row SHAPE is that lane's to land, on the CTO's
ruling of your proposal.

1. `infra/aws/terraform/shared-infra/tests/derive_fence_row_shape.py` -- THE FIRST READ, as a script whose output is the evidence:
   - The registry row's shape today: read `infra/logic/registry/exemptions.json` `_about` and every existing row; print the set of
     keys rows carry and the count of rows per key set. Does any row carry an action set or a prefix? (Expected from the issuer's
     reading of `_about`: no -- `row_fields` names `principal`, `arn`, `reason`, `signoff_ref` -- but measure it.)
   - Every reader of that file: search tracked files for `exemptions.json` and for `fence_exemption_arns`; for each reader print
     `path:line` and what it does with a row (the Terraform module `infra/aws/terraform/modules/opal_name/` at the lines that build
     `fence_exemption_arns`; `lib/opal_naming.py` `validate()` and any generator that writes `generated_locals.tf`; tests). State, per
     reader, whether an EXTRA key on a row would be ignored, refused, or mis-read (for the validator: try it on a scratch copy of the
     registry outside the repo tree and print its verdict; do not edit the real file).
   - How each of the three fences consumes the list: quote the `DenyForeignFirmPrincipals` statement's construction in
     `s3-49financial.tf` and `s3-lgic-firm-buckets.tf` (file:line), and say what a principal in the admitted list gains: everything
     the fence denied, on the whole bucket.
   - dell1's own reach on these buckets once admitted, read from the Dell policies in `infra/aws/terraform/nfra-ctlpln-identity/`
     (`s3:GetObject`, `s3:PutObject`, `s3:ListBucket` and the rest on `opal-*`; the Deny on deletes): so plain admission would give
     dell1 read, list AND put on all three buckets, which the ruling refuses.
   - Whether the prefix exists as the ruling names it: `irpt/<firm>/platinum/holdings/` -- read the repository for where that path is
     written (search for `platinum/holdings`), print the `<firm>` token each of the three buckets uses in it, and say plainly if the
     repository does not show the prefix for a bucket. Do NOT list or read any object in any firm bucket.
   - LAST line `FENCE-ROW-SHAPE rows=<n> key_sets=<k> rows_with_actions=<a> rows_with_prefix=<p> readers=<r> extra_key_ignored=<i> extra_key_refused=<f> can_carry_today=<True|False> ok=<True|False>`
     (`ok=True` when every reader was read and the scratch validator run completed).
2. THE PROPOSAL, in your deliverables folder as `PROPOSAL_FENCE_ROW_SHAPE_READ_ONLY_PREFIX.md`, in standard technical English, for
   the CTO to rule and the registry's lane to land. If `can_carry_today` is False (expected), it states the row shape NEEDED: the
   new optional fields (for example `actions`: a list of S3 actions the exemption is limited to; `prefix`: the key prefix it is
   limited to), their defaults (absent = today's meaning, whole bucket, all actions, so every existing row is unchanged), the
   validator rule for them, and EXACTLY what each fence must render for a scoped row so the result is read-only and prefix-scoped
   even though the user's own policy allows put: the user stays OUT of nothing-denied admission and instead (a) is added to the
   fence's admitted list AND (b) a second Deny statement, rendered per scoped row, refuses that principal every S3 action except
   `s3:GetObject` on `arn:aws:s3:::<bucket>/<prefix>*` and `s3:ListBucket` on the bucket with an `s3:prefix` condition for that
   prefix (write the two statements out in full as JSON for one bucket, with `NotAction` / `NotResource` or the two-statement
   form, and say which you chose and why; note that `s3:ListBucket` is a bucket-level action scoped by the `s3:prefix` condition key,
   not by an object ARN). Prove the two statements with the simulator on a SCRATCH policy document built from one bucket's saved
   live policy (`tests/dell_fence_census.json` holds it): dell1 `s3:GetObject` under the prefix -> allowed; `s3:GetObject` outside it
   -> denied; `s3:PutObject` under the prefix -> denied; `s3:ListBucket` with the prefix condition -> allowed and without it ->
   denied; dell2 (an unscoped row) unchanged. Print the five arms. Then the three rows as they would be written, the module lines
   that would change (file:line, by reading), and what the plan for each bucket would then show.
   The proposal proposes; it changes no file outside your deliverables folder and `tests/`.

**ACCEPTANCE.** CT4d2-AC1 is unchanged and must still pass (the dell2 rows). One criterion is ADDED:

<criterion id="CT4d2-AC2" cell_refs="CT-d-2"><invocation>python infra/aws/terraform/shared-infra/tests/derive_fence_row_shape.py</invocation><expect>FENCE-ROW-SHAPE rows=</expect></criterion>
`CT4d2-AC2` -- the registry row's shape and every reader of it were read; the same line must read `ok=True`, stated in the proof row,
with `can_carry_today` reported as measured.

**BOUNDS for this pass.** Read-only AWS: `iam simulate-custom-policy` / `simulate-principal-policy`, `sts get-caller-identity`. No
object or bucket listing in any firm bucket, no apply, no plan against the backend, no edit to the registry, the module, a `.tf`
file or `lib/opal_naming.py`. Firm bucket names only in files under `tests/`, in your proposal and in your report. Write a NEW
proof instance over the old one covering both ids, validate it with
`python .tools/proof-of-spec-check.py <instance> CT4d2-AC1,CT4d2-AC2`, and flip `<status>` back to `complete` only when both pass.

## AMENDMENT 4 (2.0.0_SA_COO~C, 2026-10-07 ~12:5xZ) -- REOPENED: build the scoped-exemption RENDERER and the fail-closed readers; NO registry row

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree and every earlier commit
is inherited state on the trunk (the read and the proposal merged @cef4ce2f39). Authority: `1.0.0_SA_CTO` msg 106230, verbatim:
"shape as proposed, actions and prefix, both or neither. Order is the condition: the renderer and the two .tf edits land first, and
a reader meeting a key it does not know REFUSES, never ignores; only then does 4.0.0_SA_CRO write the three rows (send it the
proposal). GetBucketLocation: yes, admitted. GetObjectVersion: no. Then send the plan for my half." Gate limb: none graded this
modification. THE WORK below is the whole of this amendment. `infra/logic/registry/exemptions.json` is REMOVED from the grant:
YOU WRITE NO REGISTRY ROW AND EDIT NO REGISTRY FILE. The three rows are another lane's act after this build lands.

Read first, on the trunk in your worktree: `deliverables/0.9.0_WK_NFRA_CTLPLN~6/PROPOSAL_FENCE_ROW_SHAPE_READ_ONLY_PREFIX.md` (the
ruled shape, the three rendered statements, the lines that change) and row `NFRA_CTLPLN-W6-S5` (the hazard this order of work closes).

1. **The readers refuse an unknown key (the CTO's condition; today an extra key is ignored and rendered as FULL admission).**
   - `lib/opal_naming.py` `validate()`, the exemptions block near :529-540: a row's key set must be a subset of the closed set
     {`principal`, `arn`, `reason`, `signoff_ref`, `actions`, `prefix`}; any other key REFUSES naming the bucket, row index and key.
     `actions` and `prefix` come together or not at all. `actions`: a non-empty list, each entry in the CLOSED read set
     {`s3:GetObject`, `s3:ListBucket`, `s3:GetBucketLocation`} (the CTO admitted `GetBucketLocation` and refused
     `GetObjectVersion`; `ListBucketVersions` is NOT in the set either, since versions were refused). `prefix`: a literal string
     ending in `/`, no wildcard characters, no leading `/`, its second path segment equal to the bucket's firm token (the rule the
     proposal prototyped; read `scopes.json` through the existing registry loader for the token, never type a firm name). A scoped
     row names exactly one principal by exact ARN (no `*`, no `?`). At most one row per principal per bucket.
   - `infra/aws/terraform/modules/opal_name/main.tf` near :89-101: the module must REFUSE a row carrying a key outside the closed
     set (a `precondition` or a `check` that fails the plan; say which and why it fails closed at plan time), keep
     `fence_exemption_arns` byte-identical for today's 29 rows, and add an output `fence_scoped_statements` (a map keyed like
     `fence_exemption_arns`, each value a list of statement objects) rendering, per scoped row, the Deny statements below. A scoped
     row's ARN stays in `fence_exemption_arns` (the principal must be admitted through the fence for the scoped Deny to be the only
     bound), exactly as the proposal states.
   - Any generator in `lib/opal_naming.py` that writes `generated_locals.tf`, `vectors.json` or the tftest file: if the new fields
     must pass through it, make that change and regenerate with the generator's own command; do not hand-edit a generated file. Row
     `NFRA_CTLPLN-W6-S4` says the generated marks are already stale since the dell2 rows: run the generator's CHECK first and report
     what it says BEFORE your change, so a stale mark you inherit is not counted as yours. If regenerating would change bytes for a
     reason other than your edit, STOP on that file, report the diff, and leave it (it is the registry lane's restamp).
2. **The statements a scoped row renders** (per bucket; `<n>` is a stable index so two scoped rows do not collide):
   - `DenyScopedExemption<n>AnyOtherAction`: Deny, `NotAction` = the row's `actions`, on the bucket and its objects, for that
     principal ARN.
   - `DenyScopedExemption<n>ObjectsOutsidePrefix`: Deny `s3:GetObject` with `NotResource` = `arn:aws:s3:::<bucket>/<prefix>*`.
   - `DenyScopedExemption<n>ListingOutsidePrefix`: Deny `s3:ListBucket` on the bucket with `StringNotLike` `s3:prefix` =
     `<prefix>*` (an absent `s3:prefix` must also be refused: say how the rendered condition achieves that and prove it by an arm).
   - `s3:GetBucketLocation`, when in `actions`, is a bucket-level action with no prefix: it is simply not denied.
3. **The two fence files consume the new output** and nothing else changes in them:
   `infra/aws/terraform/shared-infra/s3-49financial.tf` (the `Statement` list near :127-177) and `s3-lgic-firm-buckets.tf` (the
   `concat(` near :149-170) gain `module.opal_name.fence_scoped_statements[...]`. WITH TODAY'S REGISTRY (no scoped row) EVERY
   RENDERED BUCKET POLICY MUST BE BYTE-IDENTICAL TO BEFORE: prove it by rendering the module standalone (a temporary root outside
   the repository, `terraform init -backend=false`, `terraform console`, no provider, no AWS call, `CHECKPOINT_DISABLE=1`) before
   and after your change and comparing. You run NO plan against the backend and NO apply.
   NOTE: `tests/check_dell_fence_join.py` pins these two `.tf` files to commit `3ec42c56bf`, and an apply order
   (`NFRA_CTLPLN.TO-APPLY-5`) that depends on that pin is OPEN. Do not edit the pin or that check; your branch is merged by the
   issuer only after that apply closes, and the issuer moves the pin at the merge. CT4d2-AC1 will therefore FAIL in your worktree
   once you edit a `.tf` file: record its output as it reads and say so in the proof row's reason; that is expected and is the
   issuer's to re-grade at the merge. (Your proof instance records AC1's output truthfully; do not flip the order to `complete`
   if the proof checker will not validate with AC1 as it reads -- leave it `in_progress` and report.)
4. `infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py` -- the criterion, all on SCRATCH copies outside the repo:
   - a scratch registry with the three dell1 rows as the CTO ruled them (`actions`: `s3:GetObject`, `s3:ListBucket`,
     `s3:GetBucketLocation`; `prefix`: `irpt/<firm token>/platinum/holdings/`): the validator accepts; the module renders three
     statements per bucket; the simulator, on each bucket's saved policy from `tests/dell_fence_census.json` plus the rendered
     statements, with dell1's live attached policies as the identity side, reads: get under the prefix allowed; get outside
     refused; put under the prefix refused; list with the prefix allowed; list with no prefix refused; `GetBucketLocation` allowed;
     `GetObjectVersion` under the prefix refused; dell2 (unscoped) get outside the prefix unchanged.
   - the refusals, each on its own scratch registry: an unknown key (validator refuses AND the module's plan-time check refuses);
     `actions` without `prefix`; `prefix` without `/`; an action outside the closed set; a prefix whose firm segment is another
     firm's; a wildcard principal on a scoped row; two rows for one principal in one bucket.
   - today's registry: 29 of 29 rows accepted, `fence_exemption_arns` unchanged, zero scoped statements, every bucket's rendered
     statement list byte-identical before and after.
   LAST line `FENCE-SCOPED rows_today=<n> unchanged_today=<True|False> scoped_rendered=<k>/9 sim_ok=<a>/<b> refusals_ok=<r>/7 unknown_key_refused_by=<validator+module|validator|module|none> ok=<True|False>`.
5. In your deliverables folder, `PLAN_NOTE_FENCE_SCOPED_ROWS.md`: the three rows exactly as `4.0.0_SA_CRO` would write them (JSON),
   what the plan for each of the three buckets would show once they land (by reading the standalone render; no plan run), and the
   landing order the CTO ruled.

**ACCEPTANCE.** One criterion is ADDED:

<criterion id="CT4d2-AC3" cell_refs="CT-d-2"><invocation>python infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py</invocation><expect>unknown_key_refused_by=validator\+module</expect></criterion>
`CT4d2-AC3` -- the same line must read `ok=True` with `unchanged_today=True`.

**BOUNDS.** Read-only AWS: `iam simulate-custom-policy` / `simulate-principal-policy`, `sts get-caller-identity`. No object or bucket
listing in any firm bucket, no apply, no plan against the backend, no registry edit, no network download (every Terraform call
sets `CHECKPOINT_DISABLE=1` and uses a root with no provider). Firm bucket names only in files under `tests/`, in your deliverables
and in your report; none typed into a `.tf` file, the module or `lib/opal_naming.py`.

## AMENDMENT 5 (2.0.0_SA_COO~C, 2026-10-07 ~15:0xZ) -- two issuer repairs at the merge; no new work

1. `CT4d2-AC3`'s expectation is read as a regular expression by the proof checker, so the `+` in `validator+module` was a quantifier
   and could not match the line it described (row `NFRA_CTLPLN-W6-S10`). The expectation now escapes it. The criterion is unchanged.
2. `tests/check_dell_fence_join.py` compared the two fence files with commit `3ec42c56bf`; AMENDMENT 4 changed both files by
   design, and the apply that depended on that pin is closed (order `NFRA_CTLPLN.TO-APPLY-5`, complete). The issuer adds a separate
   `TF_PIN` at the build commit `cc0c2b4b5c`; the registry baseline stays at the old pin.
Gate limb: none graded this modification. CORRECTED THE SAME HOUR: the lane gate refuses the issuer on the check file and on the
worker's proof instance, so item 2 and the proof are the WORKER's: add `TF_PIN = "cc0c2b4b5c"` beside `PIN` in
`tests/check_dell_fence_join.py` and use it ONLY for the two fence files' byte comparison (the registry baseline and its diff stay
on `PIN`); change nothing else in that check. Then re-run the three criteria, rewrite the proof instance's rows from those runs
(AC3's `expect` is now `unknown_key_refused_by=validator\+module`), validate it, and flip the order to `complete` when all three
pass and the instance is VALID. Item 1 is done by this commit.

## AMENDMENT 6 (2.0.0_SA_COO~C, 2026-10-07 ~16:4xZ) -- REOPENED: the two fence checks must hold on the registry AS IT NOW IS (the three scoped dell1 rows have landed)

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree; every earlier commit is
inherited state on the trunk (the renderer merged @3b6c321227). `4.0.0_SA_CRO` landed the three scoped rows @d5516cb074, as the
CTO's order of landing required. With them in the registry both checks FAIL, and each fails because it ASSUMED a registry without
them, not because the render is wrong (issuer's runs on the trunk, ~16:3xZ):
- `check_dell_fence_join.py`: `FENCE-JOIN pairs=3 rows=3/3 typed_in_tf=0 cross_firm_leaks=9 evaluator_allowed=3/3 negative_arm=denied other_rows_changed=3 validator=ok ok=False`
- `check_fence_scoped_rows.py`: `FENCE-SCOPED rows_today=32 unchanged_today=False scoped_rendered=18/9 sim_ok=30/30 refusals_ok=0/7 unknown_key_refused_by=module ok=False`
The issuer's read-only targeted plan of the three bucket policies on the trunk reads `0 to add, 3 to change, 0 to destroy`, each
with the dell1 ARN admitted and the three `DenyScopedExemption1...` statements: the render is what the ruling asked for. An apply
order cannot name a failing check, so both are repaired first. Gate limb: none graded this modification. YOU EDIT NO REGISTRY
FILE, NO `.tf` FILE, NO MODULE AND NO `lib/` FILE: only the two check scripts, their pairs file, and one note.

1. FIRST, for each failing field, find by READING THE SCRIPT what it compares and why it now differs, and write it down in
   `tests/fence_checks_registry_states.md` (one short paragraph per field: `cross_firm_leaks=9`, `other_rows_changed=3`,
   `unchanged_today=False`, `scoped_rendered=18/9`, `refusals_ok=0/7`, `unknown_key_refused_by=module`). For each say whether it is
   (i) the check's assumption about the registry's state, or (ii) a REAL defect in the render or the validator. If ANY is (ii),
   STOP: fix nothing, file a BLOCKING row with the evidence, and report -- a real cross-firm leak or a validator that stopped
   refusing an unknown key must not be papered over by editing a test. `refusals_ok=0/7` and `unknown_key_refused_by=module`
   (the validator no longer counted as refusing) deserve the hardest look: show, on a scratch copy of TODAY's registry plus one
   unknown key, that `python lib/opal_naming.py validate --registry-dir <scratch>` still refuses, before you conclude the check
   is at fault.
2. ONLY IF every field is (i): make both checks hold on BOTH registry states, each derived, none typed:
   - `check_dell_fence_join.py`: its pairs are the dell2 rows (unscoped) of commit `PIN`'s diff. The registry has since gained
     three SCOPED rows for another principal. Its "other rows changed" and "cross-firm leak" readings must distinguish a scoped
     row (admitted AND confined by its three Deny statements: not a leak when its prefix's firm segment is the bucket's own firm,
     which the validator already enforces) from an unscoped foreign admission (a leak). It must render a scoped row AS SCOPED
     (row `NFRA_CTLPLN-W6-S6`: its own renderer ignored the fields) or take the module's render. Extend `dell_fence_join_pairs.json`
     only if the file is the declared list of expected rows; say what you did. The expected line keeps its fields; add
     `scoped_rows=<n>` and `scoped_confined=<n>/<n>`.
   - `check_fence_scoped_rows.py`: its fixtures add the three ruled rows to a scratch copy of today's registry. When today's
     registry ALREADY holds them, the scratch must not add them twice: build the "without" state by REMOVING scoped rows from the
     scratch copy and the "with" state as today's (or by adding only the rows that are absent). `unchanged_today` then means: with
     every scoped row removed, each bucket policy renders byte-identical to the render at the pre-rows registry (commit
     `d5516cb074^`, read with `git show`). `scoped_rendered` is counted against the number of scoped rows actually present
     (3 rows x 3 statements = 9). The seven refusal cases each start from a scratch copy that is VALID before the one defect is
     planted, so a refusal is attributable to the planted defect alone; add a control: the scratch copy with no defect is accepted.
3. Run both checks, and `derive_fence_row_shape.py`, each under `timeout 120`. All three last lines read `ok=True`. Rewrite the
   proof instance's three rows from your runs, validate it, and flip the order to `complete` when all three pass and it is VALID.

**ACCEPTANCE (same three ids; the expectations are unchanged).** `CT4d2-AC1` `typed_in_tf=0 cross_firm_leaks=0`; `CT4d2-AC2`
`FENCE-ROW-SHAPE rows=` (its counts move with the registry: report them); `CT4d2-AC3` `unknown_key_refused_by=validator\+module`.
Each line must read `ok=True`.

**BOUNDS.** Read-only AWS (`iam simulate-*`, `sts get-caller-identity`). No apply, no plan against the backend, no registry edit,
no bucket listing, no object read, no download; every Terraform call sets `CHECKPOINT_DISABLE=1` in a provider-less scratch root.

## AMENDMENT 7 (2.0.0_SA_COO~C, 2026-10-08 ~01:2xZ) -- REOPENED, PRIORITY: dell1 is now admitted IN FULL; the two fence checks must hold on that registry

The issuer reopens its own order; the slot is re-seated in a fresh worktree; earlier commits are inherited state on the trunk.
What changed: Andrew lifted the limit on dell1's firm data (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_004xZ_LIFT_FOUR_DELL_LIMITS_SECRETS_FIRM_DATA_RESOURCE_POLICIES_PUSH.md`;
`1.0.0_SA_CTO` msg 106669 ruling 2: "dell1 is admitted to the firm-data fences in full, like dell2. No prefix-list cell.") and
`4.0.0_SA_CRO` made the three `cloudops-dell1-agent-user` rows FULL rows @173f98f24b (no `actions`, no `prefix`). The registry now
holds NO scoped row. Issuer's runs on the trunk, ~01:0xZ:
- `FENCE-JOIN pairs=3 rows=3/3 typed_in_tf=0 cross_firm_leaks=3 evaluator_allowed=3/3 negative_arm=denied other_rows_changed=3 validator=ok scoped_rows=0 scoped_confined=0/0 ok=False`
- `FENCE-SCOPED rows_today=32 unchanged_today=False scoped_rendered=9/9 sim_ok=30/30 refusals_ok=0/7 unknown_key_refused_by=module ok=False`
The issuer's targeted plan of the three bucket policies reads `0 to add, 3 to change, 0 to destroy`, 126 lines removed and none
added: the three `DenyScopedExemption1...` statements leave each policy and the dell1 user stays admitted. An apply order
cannot name a failing check. Gate limb: none graded this modification. NO registry, `.tf`, module or `lib/` edit.

1. DIAGNOSE FIRST, as AMENDMENT 6 required, each failing field by reading the script: is it the check's assumption about the
   registry, or a real defect? Write a short section "state 3: dell1 unscoped" into `tests/fence_checks_registry_states.md`.
   A real defect (a principal of another firm admitted; the validator accepting a planted defect on today's registry) is a
   STOP with a BLOCKING row and no edit.
2. `check_dell_fence_join.py` and `dell_fence_join_pairs.json`: the expected UNSCOPED pairs are now six: the two Dell agent
   users on each of the three fenced buckets. Put the three dell1 pairs into the pairs file's `dell1_unscoped_pairs` list as
   DATA, each with the record's path as its authority (the file is the declared list of expected rows; a seventh unscoped Dell
   row, or an unscoped row for any principal not listed, is still a leak). The line keeps its fields; `pairs=6 rows=6/6`.
   Keep every negative control AMENDMENT 6 added and add one: with a pair removed from the pairs file (in a scratch copy) the
   same registry reads `cross_firm_leaks=1 ok=False`.
3. `check_fence_scoped_rows.py`: its fixtures must not depend on which real principals hold rows. Build the "with scoped rows"
   state by adding scoped rows for a SYNTHETIC principal that no registry row names (a made-up user ARN in this account,
   stated as synthetic in the script), one per fenced bucket, to a scratch copy of today's registry; the identity side of its
   simulator arms then cannot be a real user's attached policies: use a small inline identity policy document that allows
   get, put and list on the estate's bucket pattern (the worst case the confinement must hold against), through
   `simulate-custom-policy`. `rows_today` reports today's real count; `unchanged_today` compares today's render with scoped
   rows absent against the render at the commit before the first scoped row landed, EXCEPT for the principals the registry has
   since admitted unscoped (print which, from the registry diff): say exactly what is compared. All seven refusal cases and
   the control stay.
4. Run both checks, and `derive_fence_row_shape.py` and `dell_fence_census.py --selftest`, each under `timeout 120`; all read
   `ok=True`. Rewrite the proof instance's three rows from your runs; validate; flip the order to `complete`.

**ACCEPTANCE (same three ids, expectations unchanged):** `CT4d2-AC1` `typed_in_tf=0 cross_firm_leaks=0`; `CT4d2-AC2`
`FENCE-ROW-SHAPE rows=`; `CT4d2-AC3` `unknown_key_refused_by=validator\+module`. Each line must read `ok=True`.

## AMENDMENT 8 (2.0.0_SA_COO~C, 2026-10-08 ~02:5xZ) -- one path added: the census self-test's fixture (row NFRA_CTLPLN-W6-S15)

The issuer accepts AMENDMENT 7's three criteria as run (the issuer re-ran both checks in the worktree: `pairs=6 rows=6/6
cross_firm_leaks=0 negative_arm=denied ok=True`; `sim_ok=31/31 refusals_ok=7/7 ok=True`) and merges that work now, so the apply
it gates is not held. What remains is item 4's last part: `dell_fence_census.py --selftest` reads `cases=0/0 ok=False` because it
takes its scoped pair from the registry, which now holds none. The lane gate refused the fix because the file was not in
`<paths>`. It is added by this amendment (`infra/aws/terraform/shared-infra/tests/dell_fence_census.py`). Gate limb: none graded
this modification.

1. Apply the fix the previous pass tested (its diff is saved at `.scratch/census_selftest_fixture.patch` in this worktree, and a
   copy is named in your prompt): when the registry holds no scoped row, the self-test builds its scoped pair in memory for a
   synthetic principal. Change ONLY the self-test path; `--live` and the default mode must behave byte-for-byte as before
   (show `git diff --stat` and state which functions changed). The saved file `dell_fence_census.json` is NOT rewritten.
2. `timeout 120 python infra/aws/terraform/shared-infra/tests/dell_fence_census.py --selftest` reads `cases=7/7 ok=True`.
   Re-run the three criteria; rewrite the proof instance only if an artifact pin moved; validate; flip the order to `complete`.
   Row W6-S15 is resolved by this amendment: say so in your report (rows are immutable; do not edit it).

