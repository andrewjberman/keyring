# TO IRPT_BCKEND.TO-IB-rth-6 -- CREATE opal-data-inflectionwealth + opal-data-cottonwoodcapital, WITH THE THREE-IDENTITY EXEMPTION SHIPPED AT FIRST APPLY: `opal-data-inflection`/`opal-data-cottonwood` were built with a per-firm Deny fence and an EMPTY exemption list, so the fence denied every identity the estate holds, including the operator identity that would need to fix it -- the deploy ledger has sat RED since 2026-09-18 for exactly this reason (`org/critical_paths/.open_deploys/irpt-bckend-ib-rte-3-lgic-firm-buckets.json`). Andrew's own ruling: build replacement buckets rather than keep fighting the lockout, and do not repeat the mistake.

<to_id>IRPT_BCKEND.TO-IB-rth-6</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~6</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B 2026-09-21 (round 8, mid-round addition v0.10, s.R8.7). Andrew-direct @fb8c7a574c, msg 99090. Registry edits first (read-only against live state until the packet), then the Terraform apply is a never-widen act: packet + CTO+COO halves BEFORE it, ledger opened before, safe-apply.sh only.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 8 (mid-round addition) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` (no addendum) | **Andrew-direct:** `../../../../tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_1623Z_CREATE_INFLECTIONWEALTH_COTTONWOODCAPITAL_BUCKETS.md` @fb8c7a574c | **Decomp cell:** `IB-rth-6` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.10, s.R8.7) | **outcome_ref:** FWD-11 (the bucket program) | **row:** none yet -- IB-rte-3's own ledger sentinel is the standing evidence, cited not re-filed

---

## IDENTITY AND WORKTREE
- **Serial:** `0.9.0_WK_IRPT_BCKEND~6`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~6;`.
- **Worktree:** the issuer creates `/c/tmp/wk-irpt-8-6` on branch `wk-irpt_bckend-8-6`, cut from CLOUD HEAD, `.tools/terraform.exe` provisioned; the issuer passes the absolute path at spawn. First act: `cd` there, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`; write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before any apply. Repo root = the worktree.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~6 <0.9.0_WK_IRPT_BCKEND~6@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/checkout--/clean. Capture safe-commit output to a file; never `| tail`; never with `$( )`. Verify by `git log`.
- Python `py -3.12`; AWS via `.tools/aws`; a recursive grep/find is rail-DENIED -- use Read/Grep, a gated read in its own call.

## THE CELL

- **(a) MEASURE FIRST, printed with denominators.** Independently re-confirm before touching anything (do not trust this face's own restatement): `infra/logic/registry/exemptions.json`'s `opal-data-inflection` and `opal-data-cottonwood` rows each carry exactly 3 exemption entries (`Andrew_Berman`, `Andrew_Berman_Console`, `Opal_Terminal`) -- read them, do not assume the count. `infra/logic/registry/scopes.json`'s `inflection`/`cottonwood` entries: current `bucket`, `bucket_provisioned`, `bucket_managed_by` values. The deploy ledger sentinel naming IB-rte-3's original apply is still present under `org/critical_paths/.open_deploys/`. Locate the Terraform root that manages these buckets: `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` -- read it in full, including how it currently derives bucket names and how the Deny-fence policy and exemption list are wired in, BEFORE writing anything.

- **(b) THE NAMING -- Rule 30, no hand-typed address.** Run `lib/opal_naming.py address()` (the exact invocation this project's other cells use for a new S3 address) to derive the two new bucket names from the firm registry entries once you update `scopes.json`'s `bucket` field. **The result MUST be exactly `opal-data-inflectionwealth` and `opal-data-cottonwoodcapital` (Andrew's own names, verbatim).** If the tool derives anything else, STOP -- do not override the tool's output by hand, and do not silently accept a different name; file a row with the discrepancy and carry it to the COO. A builder refusal here is a missing registry row to add, never a hand-typed workaround (CLAUDE.md Rule 30).

- **(c) THE REGISTRY EDITS, in this order:**
  1. `scopes.json`: update the `inflection`/`cottonwood` entries' `bucket` field to the two new names; set `bucket_provisioned: false` (true only after the apply in arm (e) succeeds and is proven). Do NOT touch `key`/`short`/`aliases` on either firm -- those are referenced estate-wide and this is a bucket swap, not a firm rename. Correct the stale "opal-data-inflection does not exist yet" alias note while you are in this file (search for it -- do not assume its exact location or wording).
  2. `exemptions.json`: copy the SAME three exemption rows (principal, arn, reason -- adapt the reason text to name the NEW bucket, keep the substance) into two new entries keyed by the new bucket names. This is the single most important step in this cell: these rows MUST exist before the Terraform apply that creates the bucket policy, never added as a later patch -- that sequencing is the entire root cause of the original lockout.
  3. Mark the OLD `opal-data-inflection`/`opal-data-cottonwood` bucket entries abandoned in `scopes.json` (a status/note field, whatever this registry's own convention is for a superseded entry -- read a precedent if one exists rather than inventing a shape). **NO delete of the old buckets or their objects** -- that is confirmation-gated and nothing in this cell asks for it.

- **(d) THE PACKET.** This is infrastructure creation + a policy that will govern real client data buckets going forward -- same discipline as every served-property change in this project. Measure and disclose: exactly what `s3-lgic-firm-buckets.tf`'s plan shows for the two new bucket resources (bucket creation, the Deny-fence policy WITH the 3-identity exemption baked in, versioning/encryption matching the existing pattern -- read what `opal-data-49financial` or another already-working LGIC bucket has and match it); the blast radius (nothing touches the OLD buckets' objects or policies -- confirm the plan shows zero changes there); rollback (destroy the two new empty buckets if something is wrong before anything is written to them -- state this plainly, an empty bucket destroy is far lower-stakes than anything else in this project and say so). Both never-widen halves (CTO + COO) must SIGN at HEAD naming this packet's blob before any apply. If you cannot get both halves this pass, that is an honest STOP: commit the packet, leave the order open, report exactly what's owed.

- **(e) APPLY, under a change-management ledger OPENED BEFORE the apply, sentinel committed immediately:** fresh plan, confirm it shows ONLY the two new bucket resources and their policies (a subtraction-gate discipline matching this project's own standard, even though the "before" state here is simply absent) -- anything else in the plan is a STOP. `.tools/safe-apply.sh` only, never bare `terraform apply`. Post-apply: `bucket_provisioned: true` in `scopes.json`, close the ledger.

- **(f) PROVE, under an identity that would have been denied before:** as `Andrew_Berman` (or whichever of the three exempted identities you can exercise), `head-bucket` + `get-bucket-policy` + a scoped `put-object`/`delete-object` round trip on BOTH new buckets -- must all succeed where the SAME calls against the old buckets 403. Print the contrast (old bucket call -> AccessDenied, verbatim wire error; new bucket same call -> success) as the discriminating proof this fix actually worked, not just that a bucket exists.

## DELIVERABLE
The registry edits (scopes.json, exemptions.json) with the naming-tool's own output as evidence; the never-widen packet + both signed halves; the Terraform apply's plan/apply logs and the change-management ledger; the identity-exercise proof contrasting old vs new bucket access.

## BOUNDS
- NO delete of the old buckets, their objects, or their bucket policies. NO change to any OTHER firm's bucket entry in scopes.json or exemptions.json. NO rename of the `inflection`/`cottonwood` firm keys, short codes, or aliases.
- NO hand-typed bucket name anywhere -- the naming tool's output is authoritative; a mismatch against Andrew's named buckets is a STOP, not a silent acceptance of either value.
- The exemption rows MUST be present in the Terraform apply's FIRST run against the new buckets -- if you find yourself about to apply before they're in place, STOP.
- The forward-looking-criterion bar; R-40 (content hash per run/artifact read AT the event); S56 vintage pins `path:line @ <commit-ish>`; the LEDGER opened before any apply.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W6-S<k>` continuing above the highest at your HEAD (append INSIDE the first fence's array, PREVAILING EOL, UTF-8 explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); then keep working.

<expected_criteria>R81-AC1, R81-AC2</expected_criteria>
<criterion id="R81-AC1" cell_refs="IB-rth-6"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~6/battery_ib_rth_6.py</invocation><expect>IBR81-NEW-BUCKETS-EXEMPT-IDENTITIES-SUCCEED-OLD-BUCKETS-STILL-DENY</expect></criterion>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rth-6.create-inflectionwealth-cottonwoodcapital-buckets.md
infra/logic/registry/
infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.10, cell `IB-rth-6` (s.R8.7).
<owned_cells>IB-rth-6</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE at the cut -- the exemption-identity grant IS the subject of this cell's own registry edit and packet, never assumed at the cut.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed -- especially anything outside `infra/logic/registry/` and the one named Terraform file -- is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R81-AC1 (both new buckets exist, both carry the 3-identity exemption from first apply, an exempted identity succeeds head-bucket/get-bucket-policy/a scoped object round-trip on both, the SAME calls against the old buckets still 403 exactly as before -- no regression, no accidental widening), R81-AC2 (judgment, the CVO's at L9 -- whether the registry edits correctly preserve every other firm's entry and whether the old-bucket abandonment note is accurate). Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~6/IRPT_BCKEND.TO-IB-rth-6.create-inflectionwealth-cottonwoodcapital-buckets.proof_of_spec.json` per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hash per produced/served artifact pinned to its commit; the judgment row under `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Validate `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>`; rc 0 AND R81-AC1 PASS-by-output, then flip `<status>` complete. A STOP (naming mismatch, halves absent, plan shows anything beyond the two new resources) leaves the order open with the BLOCKING row + the carry, and is the final report on it.
</proof_of_spec>
</output>
