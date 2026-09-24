# NFRA_MCPORTAL -- surprise channel, INVESTIGATION v1 (site-Z fabric)

**Home:** the project tree's channel. Lane `ANY`; `.tools/surprise-row-gate.py` validates every NEW row
(schema, identity, coordinate, folder == project). **Append-only.**

**Id grammar on this fabric:** a seat's row is `NFRA_MCPORTAL-Z-S<k>`; a worker's row is
`NFRA_MCPORTAL-Z-W<n>-S<k>` with `<n>` its slot; `<k>` restarts at 1 per coordinate. `"project":
"NFRA_MCPORTAL"` and `"fabric": "site-z"` on every new row. The CVO's adjudication rows live in
`adjudications/`, never here.

---

```json
[
  {
    "id": "NFRA_MCPORTAL-Z-W3-S1",
    "project": "NFRA_MCPORTAL",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPORTAL~3",
    "surfaced_at": "2026-09-24T23:55Z",
    "one_line": "_root.sh's mp_writer_entry() (shared by t2.AC1.sh, t2.AC2.sh and t2.AC3.sh) is a SyntaxError inside a redirected python -c one-liner, so all three MP-t-2 checks read an empty source-map lookup and FAIL regardless of whether the cell's registry row, source, tests and Terraform are conforming.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/_root.sh mp_writer_entry(): `print(len(hits)); [print(k); print(v.get('source_dir','')); print(v.get('tf_file','')) for k,v in hits[:1]]` -- a list comprehension cannot contain semicolon-separated statements.",
        "Running that exact string through `python -c` (no redirect) raises `SyntaxError: invalid syntax` at the second `print(...)` inside the brackets; t2.AC1.sh's own invocation of mp_writer_entry() carries `2>/dev/null` inside the function, so the error is swallowed and $e is empty.",
        "The underlying data is conforming: python -c \"import json; d=json.load(open('infra/aws/lambda/ci/lambda-source-map.json',encoding='utf-8'))['functions']; hits=[(k,v) for k,v in d.items() if 'mcportal' in (v.get('source_dir') or '') and 'grant-writer' in k]; print(len(hits))\" prints 1, with source_dir=infra/aws/lambda/mcportal/mcportal-grant-writer-lambda and tf_file=infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf, both real paths in this worktree.",
        "t2.AC1.sh: `name()=mcportal-grant-writer-lambda; source-map entries= key=; source_dir exists=no; tf_file exists=no` / `RESULT: FAIL` / exit=1. t2.AC2.sh: `writer tests absent (/tests/test_grant_writer.py)` / `RESULT: FAIL` / exit=1 (src is empty, so the path is a bare `/tests/...`, even though `.../mcportal-grant-writer-lambda/tests/test_grant_writer.py` exists and its 4 named tests pass 4/4 under plain pytest). t2.AC3.sh: `tf_file absent` / `RESULT: FAIL` / exit=1, even though `infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf` exists and is terraform-fmt-clean. All three measured at CLOUD HEAD 054bad6cc7 + this worker's own commit."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Each of MP-t-2's three literal invocations (`bash .../checks/t2.AC{1,2,3}.sh`) is expected to print `RESULT: PASS` / exit=0 once the builder name resolves, the source-map carries exactly one conforming entry, the tests pass and the Terraform is present and fmt-clean.",
    "world_is": "The shared mp_writer_entry() helper cannot report a non-empty result for ANY conforming entry, ever, because its embedded python fails to parse before it prints anything -- so all three checks FAIL from that one empty lookup regardless of the cell's own state. The defect is in the check, not in this cell's registry row, source directory, tests or Terraform file (all four are present and independently verified correct above and in this worker's proof-of-spec instance).",
    "notes": "Not in this worker's <paths> (org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/** is the issuer's own), so not repaired here -- recorded and the literal AC1 invocation's output kept verbatim in this worker's proof-of-spec instance as FAIL, per the worker rule against repairing a criterion. ARMED because every future re-run of t2.AC1.sh (by MP-t-3, by a re-check, by a fresh worktree) hits the same SyntaxError regardless of what any worker builds."
  }
]
```
