"""Write the release-35 Lambda-leg never-widen packet (irpt-status: the failure code and words; COO half signed, CTO half unsigned) from a verified build record.

usage: python -I make_packet_r35l.py <R35L_BUILD.json> <stage folder> <expected CodeSha256> <packet out path>

It refuses unless `ar_g115_checks.py verify` passes on the record and the stage with the same expected CodeSha256. Every number is read from the
record; the attribution (counts and authors from `git log`) and the stated plan shape are written by the issuer. ASCII only. Runs from the repository root.
"""
import json
import subprocess
import sys
from pathlib import Path

REC, STAGE, WANT, OUT = sys.argv[1:5]
CHECK = "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g115_checks.py"
verdict = subprocess.run([sys.executable, "-I", CHECK, "verify", STAGE, REC, WANT], capture_output=True, text=True)
if verdict.returncode != 0 or not verdict.stdout.startswith("AR-G115-OK"):
    sys.exit("REFUSED: the build record does not verify: " + (verdict.stdout + verdict.stderr).strip()[:300])
record = json.loads(Path(REC).read_text(encoding="utf-8"))
pin = record["pin"]
item = record["functions"]["irpt-status"]
ATTR = {
    "status.py": "1 ANLREQ commit since the r33 build: AR-g-111 (the literal words table `FAILURE_STEP_WORDS` / `FAILURE_WORDS` and `failure_words`)",
    "owned_status.py": "native member, 1 ANLREQ commit since the r33 build: AR-g-111 (the reader returns the failure code as the reason and one NONE action holding the words)",
    "durable_job.py": "2 ANLREQ commits since its staged pin: AR-g-109 and its amendment (`HOP_FAILURE_CODES`, `get_state` carrying `hop_failure`, and the two writers, which the status Lambda never calls)",
}
rows = "\n".join("| `%s` | `%s` | %s |" % (m, item["member_sha256"][m][:12], ATTR[m]) for m in item["delta_vs_deployed_commit"])
text = """# Never-widen sign-off packet -- r35 Lambda leg: irpt-status returns the closed failure code and its words (C-HOP-FAILURE), at pin %(pin10)s

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~G2`, 2026-10-16. **Applier:** a CloudOps seat named by the CTO.
**Authority:** PRD v0.20/v0.21 contract C-HOP-FAILURE (clauses 1 and 2), CTO msgs 8907 and 8971; the CVO's single-executor rule (@32f2f026ae). **Ledger:** `irpt-status-r35l-20261016`.
**Scope:** ONE Lambda code release (`irpt-status`). No IAM, route, queue, table, secret, schema or resident host moves. No vendor call.

## 1. What ships

Pin `%(pin)s` (the r35L tooling commit; it carries `AR-g-111`, `AR-g-113`, `AR-g-109`). Built by `r35l_build.py` over the repository's own builder in `BUILD_ONLY` mode, twice,
byte-identical; the issuer's verifier `ar_g115_checks.py` re-derived every number below from the zip and the git objects, and the CodeSha256 equals the issuer's own earlier build of the same pin.

| function | zip sha256 | CodeSha256 | bytes | members | changed vs the live build (r33, pin `%(base10)s`) |
|---|---|---|---|---|---|
| `irpt-status` | `%(zip)s` | `%(code)s` | %(bytes)d | %(members)d | %(delta)d |

| member | sha256 (12) | attribution |
|---|---|---|
%(rows)s

The live package is the r33 build (CodeSha256 `OOez8YSmE22btOqx28/fJdK9sxGNDGAumU5pMJ++6Ss=`, AQ2 msg 8976). The other %(unchanged)d members are identical to it.

## 2. Blast radius, by branch (read from the code at the pin)

| what the status route answers for | BEFORE (r33) | AFTER (r35L) |
|---|---|---|
| a request whose job row has no `hop_failure` and is not FAILED or ATTENTION | the envelope as today | the SAME envelope (no new action, same reason, same state and dates) |
| a request whose job row carries `hop_failure` = {hop, code, at} with a known hop | the usual state and reason; the failure unseen | the usual state and dates; `public_reason_code` = the code when the words table knows it (else the usual reason), plus ONE extra safe NONE action whose description is fixed words naming the step and what happens next |
| a hop_failure with an unknown hop | -- | ignored (the answer is the usual one) |
| a FAILED or ATTENTION job | state and reason as today, no actions | the same state and reason, plus ONE NONE action with the generate step's words (a stored detail code is used only when the table knows it: `DELIVERIES_EXHAUSTED`) |
| the `at` timestamp, any detail text, any row value | never echoed | never echoed (only the fixed strings of the literal table travel) |
| the envelope schema | StatusEnvelope | unchanged (`public_reason_code` and the NONE action already exist) |

**Who gains: no principal class and no route.** The answer carries fixed strings only. **Writers counted.** `hop_failure` has three writers (the resident ready-signal send and packager, the commentary draft store [another seat's]); none of them is this Lambda: `durable_job.py` carries the writer functions, but the status handler never calls them (the issuer test and the reachability of `owned_status.py`). The status role's grant on the jobs table is NOT changed here `[declared in source, the live role policy not read: the apply order's R0 prints it]`.

## 3. Apply protocol, in this order

0. Both halves at HEAD naming this file's blob. Open the ledger; read every live worktree's `.open_deploys/` and print the denominator (another open entry naming `irpt-status`, its role or its key is a STOP).
1. **R0, the before-reads.** `get-function irpt-status` CodeSha256 equals `OOez8YSmE22btOqx28/fJdK9sxGNDGAumU5pMJ++6Ss=`; the key's latest S3 version, downloaded and hashed, equals it (record the VersionId: the rollback source); the credential-less refusal envelope (status, body sha256); one retained READY report read as the synthetic internal viewer WITHOUT a ticket id (status, body sha256).
2. **U, build and upload.** In a throwaway worktree detached at the pin, `BUILD_ONLY=1`: the printed CodeSha256 must equal the table (any other: ABORT, nothing uploaded); then the same build without `BUILD_ONLY` (one new object version); read it back (sha256 equals the zip's). `MSYS_NO_PATHCONV` unset; a private TMPDIR.
3. **C, the scoped plan.** Root `infra/aws/terraform/investor-reporting/ops`, `-target=module.irpt_status.aws_lambda_function.this`: `Plan: 0 to add, 1 to change, 0 to destroy`, attributes `last_modified`, `s3_object_version`, `source_code_hash` only. Anything else: STOP, nothing applied.
4. **A, apply** with `safe-apply` on the saved plan; never `aws lambda update-function-code`.
5. **V, the after-reads.** G1 CodeSha256 equals the table; G2 the live object against the previous version differs in exactly the %(delta)d members above (member by member, denominator %(members)d); G3 the refusal envelope equals R0's; G4 the READY report read of R0 returns the same status and the same body (no hop_failure on that job, so no NONE action); G5 `release-census.py` against the live zip prints `changed_members=0`.
6. **Map record and close** in the applier's worktree (the `artifact_*` and `last_deployed_*` of the `irpt-status` entry); close the ledger.

## 4. Rollback, per key

Copy the previous S3 VersionId (recorded at R0) onto the key, the scoped plan, `safe-apply`, read `OOez8YSmE22btOqx28/fJdK9sxGNDGAumU5pMJ++6Ss=` back. Nothing else moves, so nothing else is rolled back.

## 5. Not claimed

- That any real job row carries `hop_failure` (the writers are in the resident release and the commentary draft store, not here), or that the ticket page reads the new fields (`~V2`'s cell).
- That the live zip equals the r33 build commit (R0 and G5 prove it).
- That the status role cannot write the jobs table (the code never calls the writers; the live policy is not read here).

## COO half -- 2.0.0_SA_COO~G2

SIGNED, 2026-10-16, on this packet's bytes at the commit that carries it. The write set: one Lambda code object (one S3 object version) and its function configuration. The blast radius is section 2; the rollback is section 4.

## CTO half -- 1.0.0_SA_CTO

(not signed)
""" % {"pin": pin, "pin10": pin[:10], "base10": item["deployed_commit"][:10], "zip": item["zip_sha256"], "code": item["code_sha256"], "bytes": item["bytes"],
       "members": item["members"], "delta": len(item["delta_vs_deployed_commit"]), "rows": rows, "unchanged": item["members"] - len(item["delta_vs_deployed_commit"])}
if any(ord(c) > 127 for c in text):
    sys.exit("REFUSED: non-ASCII in the packet")
Path(OUT).write_text(text, encoding="ascii", newline="\n")
print("wrote %s bytes=%d" % (OUT, len(text)))
