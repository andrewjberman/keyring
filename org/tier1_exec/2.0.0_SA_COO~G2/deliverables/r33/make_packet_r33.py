"""Write the release-33 never-widen sign-off packet (COO half signed, CTO half unsigned) from a verified build record.

usage: python -I make_packet_r33.py <R33_BUILD.json> <stage folder> <packet out path>

It refuses unless `ar_g103_checks.py verify` passes on the record and the stage. Every number in the packet is read from the record,
the source map or git at the record's pin; nothing is typed from memory except the attribution table (read by the issuer from
`git log` and printed with its range) and the plan shapes (stated, graded by the applier). ASCII only.
"""
import json
import subprocess
import sys
from pathlib import Path

REC, STAGE, OUT = sys.argv[1:4]
CHECK = "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g103_checks.py"
GEN, STATUS = "irpt-ycharts-generate", "irpt-status"
IR = "infra/aws/lambda/investor-reporting/"
verdict = subprocess.run([sys.executable, "-I", CHECK, "verify", STAGE, REC], capture_output=True, text=True)
if verdict.returncode != 0 or not verdict.stdout.startswith("AR-G103-OK"):
    sys.exit("REFUSED: the build record does not verify: " + (verdict.stdout + verdict.stderr).strip()[:300])
record = json.loads(Path(REC).read_text(encoding="utf-8"))
pin = record["pin"]
smap = json.loads(subprocess.run(["git", "show", "%s:infra/aws/lambda/ci/lambda-source-map.json" % pin], capture_output=True, text=True, check=True).stdout)
gen, st = record["functions"][GEN], record["functions"][STATUS]
gm, sm = smap["functions"][GEN], smap["functions"][STATUS]

# Hunk attribution, read by the issuer from `git log <old pin or baseline>..<pin> -- <path>` (counts and authors only).
ATTRIBUTION = [
    ("portfolio.py", "3 ANLREQ commits: AR-g-68 (twice: the kept symbol files UNRESOLVED; the residual counts it) and AR-g-96 (the decision-tree findings, the not-covered ticker files UNRESOLVED)"),
    ("uploads.py", "3 ANLREQ commits: AR-y-318 (names the failing step of the partner path), AR-g-95 (the door ignores a sent priceDate and derives T-1), AR-g-96 (word tables, PROXY_CODES retired)"),
    ("acceptance.py", "3 commits: AR-g-67 (the accept step stamps ticket_confirmed) and AR-g-85 (it stamps report_variant), both ANLREQ; and ONE FOREIGN commit, IRPT_BCKEND IB-pr-478 `06557b6618` (the packager reads commentary_ref from the accepted record), which rides in with the file and is for the pair to sign"),
    ("submission_service.py", "1 ANLREQ commit: AR-g-67 (the confirm port and the stamp)"),
    ("generate_installed.py", "1 ANLREQ commit: AR-g-67 (the live ticket-confirm port from IRPT_TICKETS_TABLE)"),
    ("ticket_confirmation.py", "NEW member: AR-g-67 (one consistent GetItem on the ticket table; true only for a dashboard-form ticket the accepted principal filed)"),
    ("normalized_input.py", "native member, 1 ANLREQ commit since the live build: AR-g-68 (an UNRESOLVED row is carried through)"),
    ("prospect_submission.py", "native member, 1 ANLREQ commit since the live build: AR-g-67 (the stamp is carried on the accepted record)"),
]
STATUS_ATTR = "status.py: 1 ANLREQ commit since the release-31 build: AR-g-96 (the correction words; the table that the upload door's copy is locked equal to)"


members_gen = "\n".join("| `%s` | `%s` | %s |" % (m, gen["member_sha256"][m][:12], text) for m, text in ATTRIBUTION)
text = """# Never-widen sign-off packet -- r33: the irpt-ycharts-generate leg (the decision-tree findings, the derived price date, the accept stamps, the ticket confirm) and the irpt-status words, at pin %(pin10)s

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~G2`, 2026-10-16. **Applier:** a CloudOps seat named by the CTO.
**Authority:** CTO msg 8658 (r33 = this leg: the code, the staged row for `ticket_confirmation.py`, `IRPT_TICKETS_TABLE`, GetItem on that one table only, both priceDate branches), msg 8693 and 8723 (r33 also carries the v0.19 decision tree and retires NAME_PROXY), PRD v0.16 to v0.19; the CVO's single-executor rule (@32f2f026ae). **Ledger:** `irpt-ycg-r33-20261016` (generate and its role policy: ONE artifact group) and `irpt-status-r33-20261016` (separate). **Scope:** two Lambda code releases and one inline IAM policy. No route, queue, table, secret, schema or resident host moves. No vendor call.

## 1. What ships

Pin `%(pin)s` (the merge of `AR-g-102`). Built by `r33_build.py` over the repository's own builder in `BUILD_ONLY` mode, twice each, byte-identical; the issuer's verifier `ar_g103_checks.py` re-derived every number below from the zips and the git objects, and the same two CodeSha256 values were produced by the issuer's own earlier build of this pin (a second build is identical).

| function | zip sha256 | CodeSha256 | bytes | members | changed or added vs the build it replaces |
|---|---|---|---|---|---|
| `irpt-ycharts-generate` | `%(gen_zip)s` | `%(gen_code)s` | %(gen_bytes)d | %(gen_members)d | %(gen_delta)d |
| `irpt-status` | `%(st_zip)s` | `%(st_code)s` | %(st_bytes)d | %(st_members)d | %(st_delta)d |

**The delta, member by member** (`irpt-ycharts-generate`: baseline = its last deployed commit `%(gen_base10)s`; the issuer's `release-census.py irpt-ycharts-generate --pin <pin>` against the LIVE zip printed `changed_members=8` before the build record existed):

| member | sha256 (12) | attribution since the live build |
|---|---|---|
%(members_gen)s

`irpt-status` (baseline = the release-31 map commit `af51e37a29`, the commit the live package was built from): exactly **one** member differs, `status.py` (`%(st_status)s`). %(status_attr)s.

**Terraform, declared in `infra/aws/terraform/investor-reporting/ycharts/generate.tf` (merged):** (a) the function's environment gains ONE variable, `IRPT_TICKETS_TABLE = "opal-tickets"`; (b) ONE new inline policy `irpt-ycharts-generate-ticket-read-policy` on `irpt-ycharts-generate-role`: Allow `dynamodb:GetItem` on `arn:aws:dynamodb:us-east-1:<account>:table/opal-tickets` and nothing else (no index, no Query, no write, no wildcard). The table has no customer-managed key (`ticket-center/main.tf`), so no kms statement. The name is the naming builder's output.

**The other 26 stale staged rows of the generate function are NOT re-pinned** (other lanes' merged work): they stay at their old pins, so they are not in the delta.

## 2. Blast radius, by branch (read from the code at the pin)

| what | BEFORE (live) | AFTER (r33) |
|---|---|---|
| an upload whose payload carries `priceDate` (any value, a malformed one included) | stored in the options, used as the pricing date, a malformed one refused | **accepted, the value dropped**, one journal line `IRPT_UPLOAD price_date_ignored=1` (never the value); the price date is the T-1 derived by the server |
| an upload with no `priceDate` | the server derives T-1 | the same |
| a ticker the provider does not know (TICKER_NOT_FOUND) | finding with REPLACE_FILE and NAME_PROXY, words ask for a proxy | finding with REPLACE_FILE, REPLACE_TICKER, FILE_UNRESOLVED (ACCEPT_SUGGESTION first when the gate has one); words without proxy talk |
| a real security the provider will not price (TICKER_DATA_NOT_ENTITLED) | ERROR asking for a proxy; nothing files | **files UNRESOLVED** with a NOTICE "Row N: SYM is not covered by our price data. Opal Staff will manage the replacement."; no filer choice |
| a retry class (check failed, not checked) | ERROR naming a proxy | ERROR asking for a retry; no proxy action |
| a stand-in correction for a not-covered ticker | accepted | refused as CORRECTIONS_INVALID |
| the accept step | stamps nothing about a ticket | stamps `ticket_confirmed` (true only when ONE consistent GetItem on `opal-tickets` finds a dashboard-form ticket whose requester is the accepted principal; every other case and every exception is false) and `report_variant` |
| the Lambda role | no access to `opal-tickets` | `dynamodb:GetItem` on that one table |
| the status envelope's correction words | the old words | the new words (the table the upload door's copy is locked equal to) |

**Who gains: no principal class and no route.** The accept step reads one table it could not read; it writes nothing there. A flag false is the safe value (the producer allow list is unchanged).
**Writers counted.** `IRPT_TICKETS_TABLE`: one writer (Terraform, this pair). The role's inline policies: this pair adds one; the others are not touched.

## 3. Apply protocol, in this order

0. Both halves at HEAD naming this file's blob. Open the ledgers; read every live worktree's `.open_deploys/` and print the denominator (another open entry naming either function, the generate role, or the key is a STOP).
1. **R0, the before-reads.** For each function: CodeSha256 equals the map's recorded `deployed_code_sha256` (`irpt-ycharts-generate` `%(gen_live)s`; `irpt-status` `%(st_live)s`) and the key's latest S3 version, downloaded, hashes to it (record the VersionId: it is the rollback source). The credential-less refusal envelope (status, body sha256) of each. The generate function's environment (names and values) and the role's inline policy list and aggregate size; the simulate-principal-policy battery of section 4 (before).
2. **U, build and upload.** In a throwaway worktree detached at the pin, `BUILD_ONLY=1` for each function: the printed CodeSha256 must equal the table above (any other: ABORT, nothing uploaded); then the same build without `BUILD_ONLY` (one new object version per key); read each object back (sha256 equals the zip's).
3. **C, the scoped plans.** `irpt-status` (root `ops`, `-target=module.irpt_status.aws_lambda_function.this`): `Plan: 0 to add, 1 to change, 0 to destroy`, attributes `last_modified`, `s3_object_version`, `source_code_hash` only. `irpt-ycharts-generate` (root `ycharts`, `-target=module.irpt_ycharts_generate.aws_lambda_function.this -target=aws_iam_role_policy.generate_ticket_read`): `Plan: 1 to add, 1 to change, 0 to destroy`; the add is the policy; the change is the function with `environment` (gaining exactly `IRPT_TICKETS_TABLE`), `last_modified`, `s3_object_version`, `source_code_hash` and nothing else. Anything else: STOP, nothing applied.
4. **A, apply** with `safe-apply` on each saved plan, `irpt-status` first (an independent artifact), then `irpt-ycharts-generate`; never `aws lambda update-function-code`.
5. **V, the after-reads.** `irpt-status`: G1 CodeSha256 equals the table; G2 the live zip against the previous version differs in exactly `status.py`; G3 the refusal envelope equals R0's. `irpt-ycharts-generate`: G1 CodeSha256 equals the table; G2 against the previous version exactly the 8 members of section 1 differ (member-by-member sha256; print the denominator %(gen_members)d); G3 the refusal envelope equals R0's; G4 the environment is R0's plus exactly `IRPT_TICKETS_TABLE=opal-tickets` (handler, timeout, memory, layers, role equal); G5 the new inline policy document equals section 1's statement, and the simulate battery (below) differs from R0's in exactly the first row; G6 the role's aggregate inline size, before and after, under the service limit; G7 `release-census.py` against the live zip prints `changed_members=0` for each function.
6. **Map record and close** in the applier's worktree (the artifact_* and last_deployed_* of both entries); close the ledgers.

**The simulate battery** (principal = the generate role; before and after): `dynamodb:GetItem` on `table/opal-tickets` (before: implicit deny; after: allowed), `dynamodb:Query`, `dynamodb:Scan`, `dynamodb:PutItem`, `dynamodb:UpdateItem`, `dynamodb:DeleteItem`, `dynamodb:BatchGetItem` on that table (all denied before and after), `dynamodb:GetItem` on `table/opal-tickets/index/status-index` (denied), and `dynamodb:GetItem` on `table/irpt-requests`, `table/opal-users-v2`, `s3:GetObject` on the intake store prefix (unchanged, whatever they read before).

**The sitting is a separate order** (the parked release-29 partner-advisor arms D2/D4 re-run on this release, `AR-y-318` rides here; plus the two priceDate arms: a synthetic internal viewer's upload that sends `priceDate` is accepted and the journal shows `IRPT_UPLOAD price_date_ignored=1` once; one that sends none shows no such line). It is `2.0.0_SA_COO~Y2`'s order to cut, under this pair.

## 4. Rollback, per key

- **`irpt-status` code:** copy the previous S3 VersionId (recorded at R0) onto the key, the scoped plan, `safe-apply`, read `%(st_live)s` back.
- **`irpt-ycharts-generate` code:** the same, read `%(gen_live)s` back.
- **The environment variable and the policy:** revert the two additions in `generate.tf` (the file at the baseline commit), the scoped plan (`1 to destroy`, `1 to change`), `safe-apply`, read the environment and the inline policy list equal to R0's.
- Nothing else moves, so nothing else is rolled back. A failed V on one function does not roll back the other unless the CTO orders it.

## 5. Not claimed

- That the live zips equal the build commits (the applier's `release-census.py` step G7 and R0 prove it; `irpt-status`'s baseline is the release-31 map commit because the map's own `last_deployed_commit` for it is not the build commit).
- That the NOT_ENTITLED branch or the tree has run live: they need the resident's resolve and a real provider read (FWD-1 run 3).
- That the resident has the swap or the new door bytes: the resident gets them in r34.
- That `ticket_confirmed` is true for any real ticket: the table read is proven by the policy battery, and its first live use is a filed ticket.

## COO half -- 2.0.0_SA_COO~G2

SIGNED, 2026-10-16, on this packet's bytes at the commit that carries it. The write set: two Lambda code objects (two S3 object versions) and their function configurations, one environment variable, one inline policy of one statement. The blast radius is section 2; the rollback is section 4.

## CTO half -- 1.0.0_SA_CTO

(not signed)
""" % {
    "pin": pin, "pin10": pin[:10], "gen_zip": gen["zip_sha256"], "gen_code": gen["code_sha256"], "gen_bytes": gen["bytes"], "gen_members": gen["members"],
    "gen_delta": len(gen["delta_vs_deployed_commit"]), "st_zip": st["zip_sha256"], "st_code": st["code_sha256"], "st_bytes": st["bytes"],
    "st_members": st["members"], "st_delta": len(st["delta_vs_deployed_commit"]), "gen_base10": gen["deployed_commit"][:10],
    "members_gen": members_gen, "st_status": st["member_sha256"]["status.py"][:12], "status_attr": STATUS_ATTR,
    "gen_live": gm.get("deployed_code_sha256"), "st_live": sm.get("deployed_code_sha256")}
Path(OUT).write_text(text, encoding="utf-8", newline="\n")
print("wrote %s bytes=%d" % (OUT, len(text.encode("utf-8"))))
