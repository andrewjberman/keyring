# TO-IB-yr-281 -- the contract seam suite grades contract work again: the six causes that are not the parser

<to_id>IRPT_BCKEND.TO-IB-yr-281</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~91</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-281` (`decompositions/IRPT_BCKEND_DECOMP_R28_Y.md`)

---

## WORKER FACE

### THE CELL

`_contracts/tests/test_seam_paired.py` is the estate's contract seam check and it still cannot grade contract work:
**24 failed / 35 passed, 59 collected.** Round 27 fixed the ONE cause everyone assumed was the whole of it -- the
`opal://` ref parser -- which turned 10 nodes green. **Your cell is the other six causes, which worker `~90`
enumerated by subtraction rather than by guessing:**

| n | cause |
|---|---|
| 13 | the consumer portal fixture, read from the primary checkout, has drifted: 12 entries where the test pins 11, and the flat-slug paths are absent |
| 6 | no fixture pairs exist for `AnalysisUploadResult`, `OwnedAnalysisRequest`, `OwnedAnalysisRequestHistory`, `SelectedAccounts`, `PublicStatusEnvelope` |
| 1 | `test_every_schema_carries_v1_and_contract_version` pins 11 schemas; v1 now holds 24 |
| 1 | the declared-route check requires `data` in every response contract, but `export-receipt` and `submit-export` do not require it |
| 1 | `[resolve-scope]`'s contract is a `oneOf` of two documents and the test asserts exactly one |
| 2 | `[analysis-requests]` and the wrong-shaped-firm-id test build from `StatusEnvelope`, but the contracts now ref `PublicStatusEnvelope`, which forbids `internal_correlation_id` |

**THE 13-NODE CAUSE IS THE ONE THAT CAN GO WRONG. `portal/` is a SUBMODULE and is NOT this lane's to move.** Where
the TEST's pin is stale, the test moves. Where the PORTAL genuinely drifted, that is a **REFUSAL AND A ROW naming
`IRPT_FNTEND`**, not a quiet edit to another project's fixture. Say in your report which of the 13 you fixed by
moving the test and which (if any) you refused, with the reason.

**Every fix must keep the suite able to FAIL.** This suite's `test_control_*` nodes are its falsifiers; a green suite
whose controls can no longer fail is worth nothing, which is why AC2 exists and why it is graded on a MESSAGE.

### ACCEPTANCE (run from your worktree root unless the invocation says otherwise)

<criterion id="Y28-1-AC1" cell_refs="IB-yr-281"><invocation>cd infra/aws/lambda/investor-reporting && python -m pytest -q -p no:cacheprovider _contracts/tests/test_seam_paired.py</invocation><expect>0 failed (report the passed count and the collected total)</expect></criterion>

<criterion id="Y28-1-AC2" cell_refs="IB-yr-281"><invocation>cd infra/aws/lambda/investor-reporting && python - &lt;&lt;'PY'
import io, json, subprocess
P = "_contracts/fixtures/AnalysisRequest.valid.json"
orig = io.open(P, encoding="utf-8").read()
d = json.loads(orig)
d["instance"]["stage"] = 12345
io.open(P, "w", encoding="utf-8", newline="\n").write(json.dumps(d, indent=2) + "\n")
r = subprocess.run(["python", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                    "_contracts/tests/test_seam_paired.py::test_control_a_known_good_document_conforms_and_a_known_bad_one_does_not[analysis-requests]"],
                   capture_output=True, text=True)
io.open(P, "w", encoding="utf-8", newline="\n").write(orig)
print(r.stdout[-700:])
PY</invocation><expect>1 failed, naming the `stage` enum violation (12345)</expect></criterion>

<criterion id="Y28-1-AC3" cell_refs="IB-yr-281"><invocation>git diff --diff-filter=M --name-only HEAD -- docs/contracts/investor-reporting/v1/ portal/</invocation><expect>no output</expect></criterion>

<expected_criteria>Y28-1-AC1,Y28-1-AC2,Y28-1-AC3</expected_criteria>

**Issuer's base dry-run at CLOUD HEAD, measured in the main worktree:**

- **AC1 -- `24 failed, 35 passed`**, 59 collected.
- **AC2 -- `1 failed` naming the `stage` enum ALREADY**, because round 27 landed the parser fix and this criterion is
  carried forward deliberately: it is the **no-regression** guard on the falsifier. **It is green at base and must
  stay green.** If your work makes this node stop naming the enum, you have disarmed the suite's own control.
- **AC3 -- empty.** **This is the control for the boundary you must not cross**: no published contract and **no
  portal file** may be MODIFIED. Additions do not appear under `--diff-filter=M`, so new fixtures are legal.

## BOUNDS

- **Grant.** The `<paths>` block plus `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~91/` and
  this order's file. **`portal/` is READ-ONLY -- it is another project's submodule.** Every EXISTING file under
  `docs/contracts/investor-reporting/v1/` is READ-ONLY for MODIFICATION.
- **No AWS call, no deploy, no Terraform, no vendor/external network call.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass. **Three of the last four rounds were refused for an ISSUER defect and every
  refusal was right** -- if a file you need is not in `<paths>`, or a cause cannot be fixed from this lane, that is a
  REFUSAL AND A ROW naming the file or the owner. It is not your shortfall.
- **Row ids** are `IRPT_BCKEND-W91-S<k>`, appended to the project surprise channel with a
  `## <ID> -- <one line>` markdown heading. Other seats append concurrently: re-read immediately before writing and
  re-check your `<k>`. `hazard_standing` is `ARMED` or `INERT`, nothing else. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~91 <0.9.0_WK_IRPT_BCKEND~91@opal.agent>" -F <msgfile> -- <paths>`; do NOT pre-`git add`; the message file is written by the Write tool or python, never a shell heredoc and never a `python -c "..."` containing double quotes.
- **Verify every commit with git, not the tool's stdout** (`git status --porcelain <path>` empty).
- **MSYS trap (row S215):** a unix path inside a `python -c` SOURCE BODY is not converted. Pass paths as argv.
- **Search discipline:** raw recursive `grep`/`find` in Bash is gated; use `comp-find` or the native Grep/Glob/Read
  tools, and never pipe `comp-find` into `head`.

<paths>
infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py
infra/aws/lambda/investor-reporting/_contracts/fixtures/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R28_Y.md</decomp_doc> round 28, workstream ~Y, cell `IB-yr-281`.
<owned_cells>IB-yr-281</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y28-1-AC1, Y28-1-AC2, Y28-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~91/IRPT_BCKEND.TO-IB-yr-281.seam-suite-six-remaining-causes.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y28-1-AC1,Y28-1-AC2,Y28-1-AC3` BEFORE the flip. Copy
the shape from `deliverables/0.9.0_WK_IRPT_BCKEND~90/IRPT_BCKEND.TO-IB-yr-271.seam-parser-resolves-opal-refs.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line; which of the 13 portal-fixture nodes you fixed by
moving the TEST and which you refused; the suite's collected total; the diff summary; and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-blast: RUN -- WORLD by the gate's floor (an infrastructure path), though the change is test-and-fixture only and reaches no served artifact. Blast radius measured by ~90's subtraction, which this order carries verbatim rather than re-deriving: 24 nodes red across six causes, with per-cause counts. The one cause that can reach outside this lane is the consumer portal fixture, and the order forbids editing it: portal/ is a submodule, AC3 machine-checks that nothing under it is MODIFIED, and a genuine portal drift is routed to IRPT_FNTEND as a row.
comp-iam: DECLARED-NOT-APPLICABLE -- no boto3 call, no role, no grant.
comp-adversary: RUN -- three risks. (1) The worker edits the portal submodule's fixture to make 13 nodes green, which would be a silent cross-project write: portal/ is READ-ONLY in the grant, AC3 includes portal/ in its --diff-filter=M check, and the face requires a per-node statement of test-moved vs refused. (2) The worker disarms the falsifier to reach 0 failed -- the cheapest path to a green suite: AC2 is carried forward from round 27 as a NO-REGRESSION guard that is already green and graded on its MESSAGE, so weakening a control turns it red. (3) The worker extends a closed contract to fit a test (the StatusEnvelope vs PublicStatusEnvelope pair invites it): AC3's published-contract half is empty at base and any MODIFICATION shows. Blind to whether all six causes are fixable from this lane at all -- ~90 enumerated them but did not attempt them, so the order states that a cause fixable only elsewhere is a refusal and a row, not a shortfall.
lane: the <paths> block IS the grant. Measured: no open ~M or ~P order names test_seam_paired.py or _contracts/fixtures/ (over 150 task-order files, the only hits are terminal round-18-era orders and this lane's own).
</preflight>
