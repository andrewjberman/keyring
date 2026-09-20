# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rtg-1: the export receipt aligns to the writer and the taxonomy tests the code (K-CODE x 1 + K-IAM x 1; rows S105+S106)

**Signer:** `2.0.0_SA_COO~B` (the COO half; NEVER-1 -- CTO+COO). **Signed:** 2026-09-20. **The act signed:** the apply
IB-rtg-1's arm (d) performs and the live proof arm (e) then attempts, exactly as the packet
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-1.md`
describes it at HEAD, **blob `74a1004fde6e649c321f43d62cfbda5b61489b98`** (`git rev-parse HEAD:<path>`, at drain @e02df882ef).
A packet whose bytes differ from that blob is NOT what this half signs. The CTO half is asked the same tick, by this blob.

**THIS CELL CARRIES TWO KEYS -- K-CODE AND K-IAM (a real widening) -- AND A DISCLOSED PARTIAL (W1-S43).**

## The keys, as the packet names them

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| K-CODE (1 function) | `irpt-export-render` (`module.irpt_export_render.aws_lambda_function.this`, `export` root, handler `entry.lambda_handler`) served bytes: `m = 3` of 20 members -- `entry.py` (S106: refusal decided off the S3 error CODE via `ClientError.response["Error"]["Code"]`, never the class name; S105: `RECEIPT_KEY_TEMPLATE` realigned to `firms/{firm}/generations/{export_id}/receipt.json`, the DECLARED `generations` family), `handler.py` (new `receipt_key()`/`persist_receipt()` wired into `finalize_export(persist=True)`), and the COMPANION `keys.py` (row W1-S44, disarmed: it was never packaged, so the pre-existing `bundle_key()`/`artifact_key()` and this cell's `receipt_key()` would `ImportError`; staged from the same `_keys/keys.py` blob the 4 sibling functions use). BUILT `cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4=` (157997 bytes) at build-store `VersionId=xOvsKB19MIqM7gB3caGQaw768tmTYtc3`, VERIFIED AT REST (head-object `content-sha256` + ContentLength match; ADDED `keys.py` / CHANGED `entry.py`,`handler.py` by byte-diff of both zips) | **the export route's receipt read/write**: WITH, a denied/absent `GetObject` on the aligned receipt address serves a policy-shaped `NOT_FOUND` (S106) instead of propagating to `UNEXPECTED`, and a receipt written by `finalize_export` is read back at the SAME computed address; WITHOUT (today), the OLD address (0 of 7 GetObject ARNs, `KeyCount 0`) and the class-name taxonomy (a denial -> `UNEXPECTED`) persist | re-publish `CodeSha256` `9IMayS94if11cyKq51TbcyBG8cUwbbUWlQMlT9XhiaQ=` (build-store `VersionId=dECFEZtZArSJYdPy4.ImeVHBv6Q.jxBH`, verified equal) through Terraform, never `update-function-code`; verify `served == CodeSha256` |
| K-IAM (1 statement, THE WIDENING) | a NEW `aws_iam_role_policy.export_render_receipt` on the export function's OWN role `irpt-export-render-role` (never the bucket, never a firm's whole prefix): `s3:GetObject`+`s3:PutObject` + `s3:ListBucket` (prefix-conditioned), pinned to the `EXP-` NAMESPACE `firms/*/generations/EXP-*/receipt.json` -- the shape `export/identity.py`'s `EXPORT_NAMESPACE` mints and nothing else in the corpus does | **the role gains read+write on the EXPORT RECEIPT address ONLY.** MEASURED non-colliding (this run, IAM `*`-across-`/` `fnmatch`): the `EXP-`-pinned resource ADMITS this cell's own `export_id` shape and EXCLUDES `ycharts/generate/job.py`'s deeper `generations/<req>/attempts/<rev>/receipt.json` and the bundle/artifact `.../attempts/*/exports/*` shape. A bare `firms/*/generations/*/receipt.json` first draft was REJECTED because it also matched the ycharts shape -- an over-grant the role has no business holding -- and tightened to `EXP-*` before landing. The role's 3 pre-existing grants are untouched (`no-op` in plan) | remove the statement (`aws_iam_role_policy.export_render_receipt`) and re-apply -- ADDITIVE and REVERSIBLE: deleting it returns the role to EXACTLY its pre-this-cell grant set |

**THE `firms/*/...` SPAN IS NOT A CROSS-FIRM WIDENING**: `irpt-export-render` is a shared multi-firm function whose receipt
address is `firms/<firm>/...` by construction, and the role's PRE-EXISTING `export_render_evidence` grant already spans
`firms/*/generations/*/attempts/*/exports/*`; this statement is the SAME multi-firm span narrowed to the ONE new receipt
address and the `EXP-` shape. It is a NEW-GRANT widening (signed here), not a cross-firm-reference violation.

## THE DISCLOSED PARTIAL (row W1-S43, BLOCKING, disarm_owner `2.0.0_SA_COO~B`) -- arm (e) CANNOT pass on the deployed path

The DEPLOYED `entry.py`'s own wired `submit_export` (bound into `ENTRY.operations`, `export/entry.py:157-168`) unconditionally
raises `_ExportNotWiredHere`/`NOT_READY` and never calls `handler.py` -- so even a CLEAN apply of this cell cannot make arm
(e)'s submit->receipt round trip pass: no receipt is ever written on the served path, and an `export-receipt` read stays
`NOT_FOUND` (now for the HONEST reason). Wiring `submit_export` to `handler.py` is a THIRD source change this order's BOUNDS
refuse. **ISSUER RULING (L5/decomp, `2.0.0_SA_COO~B`):** IB-rtg-1's second pass STILL deploys S105+S106+K-IAM (a real,
correct, prerequisite fix -- the aligned address, the taxonomy, the grant that address needs); arm (e) is graded
DISCLOSED-PARTIAL against W1-S43 (the receipt-read half is provable; the submit round-trip is not, on the deployed path); the
submit-wiring is a FOLLOW-ON cell (round-8 or the round-7 analysis names it), NOT a rider on this order. Consequence for the
endpoint: FWD-2's export leg does NOT fully realize this round -- surfaced to `1.0.0_SA_CTO` (L10 endpoint coverage) this
tick. This half signs the DEPLOY's blast radius regardless (the code+grant are correct and reversible); it does not claim a
served round trip.

## THE ARM (d) GATE THIS HALF SIGNS -- BY SUBTRACTION, WITH THE ROUND-7 MULTI-CELL QUALIFIER

Per root, `resource_changes` of `terraform show -json <planfile>` WHOLE, minus the CLOSED PRINTED subtraction set (CTO's
ruled construction @0a7f61ae86): (i) plan top-level `.timestamp`; (ii) the S3 data-source's `version_id`/`last_modified`.
Everything else IN by default; a new field FAILS CLOSED; both denominators printed. COVERAGE, all TEN roots:
  * MY root (`export`): EXACTLY TWO real changes -- `aws_iam_role_policy.export_render_receipt` `actions ["create"]` AND `module.irpt_export_render.aws_lambda_function.this` `actions ["update"]`, before `9IMayS94if11cyKq51TbcyBG8cUwbbUWlQMlT9XhiaQ=` -> after `cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4=` (+ `s3_object_version` `dECFEZtZ...` -> `xOvsKB19...`) -- the packet's saved plan showed `1 to add, 1 to change, 0 to destroy` (11 entries, 9 no-op, 2 real); a FRESH plan is re-taken at arm (d). Nothing else after subtraction.
  * The 6 NON-round-7 roots (`api`, `core`, `directory`, `intake`, `narrative`, `ycharts`): EACH EMPTY after subtraction.
  * The up-to-3 SIBLING round-7 roots (`holdings`, `ops`, `performance`): EACH empty (already applied) OR EXACTLY that sibling cell's OWN declared `aws_lambda_function.this` update pinned to a sha in ITS signed packet (`holdings` -> `rAAn3bt7MZXpxFgric7LlrNW9uv0xXgpiZmb+MOf/y0=` + its `handler` flip; `ops`/irpt-status -> `B0AmyfRKxd4uMhcfoklf3cCpPtnDQUBpLsUBADeDcQ0=`; `performance` -> `W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA=`), plus `s3_object_version` -- and NOTHING ELSE.

**THE SIBLING-ROOT ADMISSION IS A WIDENING, STATED OUT LOUD (W1-S45 / W4-S46).** Every round-7 root reads `source_code_hash`
from the LIVE S3 object metadata with no version pin, so a sibling's upload shows on its root in any worktree's plan. BOUNDED
to the three sibling cells' OWN declared builds, each pinned in that cell's signed packet; ANY other content on ANY root --
including any IAM change on a sibling root (only export carries a K-IAM this round) -- is a STOP. A REFUSAL IS EVIDENCE, NOT
AN OBSTACLE; NEVER widen the admission at the terminal. The applies are SEQUENCED; after the last, a final all-ten-roots plan
MUST read CLEAN.

## Both branches covered

- **Applies** (both halves at HEAD, this blob): fresh per-root plan, subtraction gate over ten roots (denominator printed),
  apply `export` IFF it passes -- `.tools/safe-apply.sh`, ledger opened before, `0 to destroy`, rc 0, 0-diff after,
  `served == cn8YKEP2...` and the new IAM statement present. **Arm (e)** under `irpt-export-render-role`: the receipt-read
  half is exercised; the submit round trip is EXPECTED to show `NOT_READY` (W1-S43) and is graded DISCLOSED-PARTIAL, not a
  clean PASS. This half does NOT predict; arm (e) measures.
- **STOPS** (half absent / blob differs / gate refuses): nothing applied, or rolled back per BOTH keys (re-publish the prior
  `CodeSha256` AND remove the IAM statement) and read back; the route stays at the old address + class-name taxonomy.

## What this half does NOT sign

Wiring `entry.py`'s `submit_export` to `handler.py` (W1-S43, a separate follow-on cell); the literal deeper `attempts/exports`
address the order's prose named (W1-S42, disarm CTO -- this half signs the shallow `(firm, export_id)` address the code
ACTUALLY computes, which the signers must see); any code beyond `entry.py`/`handler.py`/`keys.py`; the three sibling cells'
own acts; the `44/19` re-derive (does NOT apply -- this cell serves no account/relationship count); FWD-11. `W = 1` writer /
`R = 1` reader of the receipt address, both this cell's own code; no other corpus writer produces this exact address.

**Push state:** LOCAL -- this half commits this tick on CLOUD; origin/CLOUD read at the drive-log send (MSTR pushes CLOUD).
