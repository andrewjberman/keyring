# TO IRPT_BCKEND.TO-IB-pr-490 -- the live read: the deployed adapter's claim and counts on one Inflection account, against the offline prediction (closes row D2-S114)

<to_id>IRPT_BCKEND.TO-IB-pr-490</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>169</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ROUND-169 ANALYSIS section 3 item 2 (msg 6660); the release it reads: `IRPT_BCKEND.TO-IB-pr-487` (live `irpt-performance-adapter` `abep4h7RngMS9JomQUdkcOT3EZ+W953OdxeK0HkdzFo=` since 2026-10-12T22:35:06Z) | **Decomp cell:** `IB-pr-490` (decomposition section 161) | **outcome_ref:** FWD-3

---

## WORKER FACE

**START ONLY ON THE ISSUER'S MESSAGE** naming this order and saying `IB-pr-489` is drained (the reference file exists). Until then do nothing on this order. This is a chain dependency, not a wait on the world: the walk is an act the issuer's worker takes now.

**Cell `IB-pr-490` (inlined):** the changed path of the `IB-pr-487` release (the claim follows the excluded day's status; two counts appear beside `days_linked`) has run on no live answer: your nine kept references refused before any compute. `IB-pr-489` keeps ONE Inflection selection reference, one line `sel_` + 64 hex, in `C:\Users\Test\AppData\Local\Temp\claude\C--dev-ajb-workspace\f0005e69-69e0-455c-b522-7be87d97fcdc\scratchpad\inflection_sel_ref.txt` (outside any git tree). Read that answer once per window and compare it with the offline prediction.

**Steps:**
1. Read the reference file (one line). Do not copy it into any record, message or commit.
2. **Invoke the deployed function directly** as in your `IB-pr-487` session (the Opal internal principal, the function's own role, the same API-shaped event, `selected_tenant` = `inflection`), with that reference and the window **2026-01-01 to 2026-10-09** (YTD to the latest served day). If the first answer is `ok:false`, record its code and STOP: do not probe other firms. A second invoke is allowed only for a second window, **2025-10-09 to 2026-10-09** (1Y). **At most 2 invokes; each ok answer persists a retained revision (a new record; nothing is overwritten): at most 2 persisted.**
3. From each answer take the claim on the headline figure, `days_without_base` and `days_with_return_left_out`, and the sha256 of the figure (not the figure).
4. **The prediction, offline, at the build's pin:** the answer names the account it was computed for (the answer's own scope; read it from the answer, keep it in YOUR scratch outside the repo, delete the scratch at the end). With the round-166 driver `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~331/ib166_measure.py` (read it first for its inputs and its use of the served gold) compute the claim the reader's rule gives that account over that window at the built pin `05219b844491b6c3c9309b6b3747e54edb823299`. A `measured` or `inferred` prediction is both valid.
5. Read the function's log group `/aws/lambda/irpt-performance-adapter` from 22:35:06Z: the `irpt_retained_phases` line of your invoke names a computed path (not `refused:*`), and 0 `TypeError` lines.
6. Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB169-3_inflection_live_read.json`: `{ref_count: 1, invokes: <1 or 2>, path_class: "computed", persisted_retained_revisions: <int 0..2>, windows: [{window: "YTD"|"1Y", claim_observed, claim_predicted, days_without_base: <int>, days_with_return_left_out: <int>, figure_sha256}], not_established: [...]}`. No account id, client name, reference or figure in it: counts, sha256 and class words only.

**Criteria (run each under `timeout 120`, record the output and exit code verbatim):**

<criterion id="IB169-3-AC1" cell_refs="IB-pr-490"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-3-AC1</invocation><expect>IB169-3-AC1 PASS</expect></criterion>
<criterion id="IB169-3-AC2" cell_refs="IB-pr-490"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-3-AC2</invocation><expect>IB169-3-AC2 PASS</expect></criterion>
<criterion id="IB169-3-AC3" cell_refs="IB-pr-490"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r169/p169_cells.py" . IB169-3-AC3</invocation><expect>IB169-3-AC3 PASS</expect></criterion>

<expected_criteria>IB169-3-AC1, IB169-3-AC2, IB169-3-AC3</expected_criteria>

What the checks grade: AC1 the record: 1 or 2 invokes on one reference, every window's observed claim equals its predicted claim, both counts present as integers, a figure sha256, `path_class` computed; AC2 a live AWS read of the function's log since the apply: at least one `irpt_retained_phases` line that is not `refused:*`, and 0 `TypeError`; AC3 `persisted_retained_revisions` an integer 0 to 2, no long digit run, no reference, no client key.

**If the observed claim differs from the prediction, or a count is absent:** that is Branch B's trigger for the `IB-pr-487` release (signed in both halves): do NOT redeploy; file a BLOCKING row with both values and STOP, and the issuer rules. Never weaken a check.

## BOUNDS

- **Grant:** the `paths` block and nothing else. Two direct invokes at most, each persisting a retained revision in the function's own store by the function's own role. No deploy, no Terraform, no source-map edit, no selection write, no read of `irpt-requests`, no other function, no vendor call.
- **Refusal clause:** STOP and file a row on any of: the reference file missing or not one line; an `ok:false` first answer; a 5xx or `TypeError`; a claim differing from its prediction; a count absent.
- **Row ids** are `IRPT_BCKEND-D2-S<n>` (the next free number: check the id is free just before you commit); `surfaced_at` is `date -u +%FT%TZ` at filing.
- **Commit with** your own author line via `bash .tools/safe-commit.sh -F <msgfile>` (message file via the Write tool, outside the worktree; do NOT pre-`git add`); ASCII only. Report to `2.0.0_SA_COO~P2` in one message under 150 words: each criterion's last line, the invoke count, the persisted count, observed against predicted claim in words.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-490.inflection-live-read-claim-and-counts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 161 (round 169, workstream ~P), cell `IB-pr-490`.
<owned_cells>IB-pr-490</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB169-3-AC1, IB169-3-AC2, IB169-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-490.inflection-live-read-claim-and-counts.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- the order changes no resource: two direct invokes of a function that is already live, each persisting a retained report (a new record) in the function's own store; the persists are named in the face and bounded at 2. The CTO half's AMENDMENT 2 (Amendment 1's 18-revision ceiling) is the standing sign-off for retained-revision writes by this function.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the invokes use the path IB-pr-487 used (the function's own role, CTO ADDENDUM 3 path 1), no new grant.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p169_cells.py dry-run at base on dell2 2026-10-12 ~23:2xZ: IB169-3 AC1 FAIL (no record), AC2 FAIL (a live AWS read: 9 `irpt_retained_phases` lines since 22:35:06Z, all `refused:*`, so no computed line), AC3 FAIL (no record). The cut has no positive control for AC1 and AC3 beyond the shape rules; AC2 is graded on the live log.
lane: the <paths> block IS the grant; applied by 0.7.0_AE_CloudOps~IB2, IRPT_BCKEND only, on the issuer's go-message after IB-pr-489 drains. Class SERVED.
</preflight>
