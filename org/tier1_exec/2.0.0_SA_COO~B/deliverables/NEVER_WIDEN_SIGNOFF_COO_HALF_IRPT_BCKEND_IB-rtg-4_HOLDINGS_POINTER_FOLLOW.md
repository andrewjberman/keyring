# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rtg-4: the holdings loader follows the directory pointer (K-CODE x 1; row S100)

**Signer:** `2.0.0_SA_COO~B` (the COO half; CLAUDE.md NEVER-1 -- CTO+COO). **Signed:** 2026-09-20. **The act signed:**
the apply IB-rtg-4's arm (d) performs and the live proof arm (e) then takes, exactly as the packet
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-4.md`
describes it at HEAD, **blob `b515836bb4db340dd1a4a6fb630ab70627432f3a`** (`git rev-parse HEAD:<path>`, this turn, at drain
@a9eddf1528). A packet whose bytes differ from that blob is NOT what this half signs. The CTO half is asked the same
tick, by this blob.

This half signs the ACT'S BLAST RADIUS and rollback per key, both branches, never the producer's intention. The writers
of each named property are counted (packet section "WRITERS"; `W = 1`).

## The key, as the packet names it

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| K-CODE (1 function) | `irpt-holdings` served bytes: ONE edited packaged member, `holdings/entry.py`'s `_load_directory`, now a TWO-step pointer follow (fetch the pointer at `IRPT_DIRECTORY_KEY`, then fetch `pointer["key"]` through the existing single-key `load_directory`) instead of feeding the pointer key to the single-key loader; BUILT `rAAn3bt7MZXpxFgric7LlrNW9uv0xXgpiZmb+MOf/y0=`, VERIFIED AT REST (zip re-hashed == declared sha, 15 of 15 declared members byte-equal, 3 vendored members index/manifest-equal at pin `ccbf4ac3cb`, import closure 10 of 10); the served-byte delta is EXACTLY `entry.py` (`m = 1 of 1`); prior LIVE `CodeSha256` `uS+WBeNxiCkYU2pdGalaONZ74SvoWEiYx669KWYKQDA=` (the running byte, rollback target) at build-store `VersionId=U4sKRs.HJ0Jc4Ik323Y0b.qY7LsWU2Pg` | **the holdings route `GET /api/scoped/investor-reporting/holdings/{accountSetId}` for every request it serves**: WITH the fix, `_load_directory` reads the RESOLVED directory artifact's `firm_id_opaque`, so `FirmBinding.proves()` gets the real value and a granted account reaches a scope-resolved answer (or a real policy refusal carrying `firm_id`) -- never `FIRM_BINDING` with `firm_id` absent (S100's fix); WITHOUT the fix (today, the rollback state), every account request on this route is refused `FIRM_BINDING` with `firm_id` absent, regardless of entitlement. TWO `s3:GetObject` calls where one before, BOTH under the existing `irpt-holdings-role` grant (`.../investor-reporting/*`) -- **NO IAM WIDENING**, zero new grants/resources | re-publish `irpt-holdings` at `CodeSha256` `uS+WBeNxiCkYU2pdGalaONZ74SvoWEiYx669KWYKQDA=` through Terraform (`source_code_hash`/object version pinned to build-store `VersionId=U4sKRs...`), never `update-function-code` (NEVER-9); verify `served == CodeSha256` read back |

**THE HOLDINGS ROOT MAY ALSO SHOW A `handler` ATTRIBUTE CHANGE**, not only `source_code_hash`: `holdings/lambda.tf:65` declares `handler = "entry.lambda_handler"` as a COMMITTED-UNAPPLIED flip (row IRPT_BCKEND-W2-S38 -- "do not apply this root for an unrelated reason before that deploy"; the zip did not carry `entry.py` until this cell built it). THIS act IS that deploy: the `entry.py`-carrying zip and the `entry.lambda_handler` config land together, as W2-S38 intends. So this half signs a holdings-root plan of `source_code_hash` + `s3_object_version` + (if not already deployed) `handler` -> `entry.lambda_handler`, and NOTHING ELSE after subtraction. Any other attribute is a STOP.

## THE ARM (d) GATE THIS HALF SIGNS -- BY SUBTRACTION, WITH THE ROUND-7 MULTI-CELL QUALIFIER

Arm (d) compares, PER ROOT, the **`resource_changes` object of `terraform show -json <planfile>`, WHOLE, minus a CLOSED and
PRINTED volatile subtraction set** (the CTO's ruled construction @0a7f61ae86 -- never a whole-planfile digest, never a
forward field list):

  SUBTRACTION SET (closed; a SIGNED TERM; nothing added without a re-signature):
    (i)  the plan's own top-level `.timestamp`;
    (ii) the S3 data-source's `version_id` and `last_modified`, wherever they appear in `prior_state`/`relevant_attributes`.

Everything else in `resource_changes` is IN the gate BY DEFAULT; a field not in the subtraction set BREAKS the gate
(**fails CLOSED**). Print both halves of the denominator (entries compared; paths subtracted). COVERAGE, all TEN roots:
  * MY root (`holdings`): EXACTLY `module.irpt_holdings.aws_lambda_function.this` `actions ["update"]`, before `uS+WBeNxiCkYU2pdGalaONZ74SvoWEiYx669KWYKQDA=` -> after `rAAn3bt7MZXpxFgric7LlrNW9uv0xXgpiZmb+MOf/y0=` (+ its `s3_object_version`; + the `handler` flip above), nothing else after subtraction.
  * The 6 NON-round-7 roots (`api`, `core`, `directory`, `intake`, `narrative`, `ycharts`): EACH EMPTY after subtraction.
  * The up-to-3 SIBLING round-7 roots (`export`, `ops`, `performance`): EACH shows EITHER empty (already applied) OR EXACTLY that sibling cell's OWN declared `aws_lambda_function.this` update -- `source_code_hash` before=deployed / after = that sibling cell's built sha as named in ITS OWN signed packet (`export` -> `cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4=` per IB-rtg-1; `performance` -> `W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA=` per IB-rtg-3; `ops`/irpt-status -> `B0AmyfRKxd4uMhcfoklf3cCpPtnDQUBpLsUBADeDcQ0=` per IB-rtg-2), plus its `s3_object_version` -- and NOTHING ELSE.

**THE SIBLING-ROOT ADMISSION IS A WIDENING, STATED OUT LOUD (rows W1-S45 / W4-S46).** The four round-7 cells share the
`opal-313476888478-lambda-artifacts` bucket, and each round-7 root's `source_code_hash` is read from the LIVE S3 object's
`content-sha256` metadata with NO version pin (VERIFIED: `holdings/lambda.tf:8-9` + the `yang-lambda` module take
`artifact_key`'s current object metadata; `export`/`ops`/`performance`/`lambda.tf` carry the identical comment). So a
sibling's `build-and-upload.sh` upload shows on ITS root in ANY worktree's plan the moment it happens, with no git
involvement. The admission is BOUNDED to the three sibling cells' OWN declared builds, EACH PINNED to a sha in that cell's
signed packet; ANY other content on ANY root -- a sibling root showing a sha NOT in that sibling's packet, a fourth root
moving, an attribute beyond `source_code_hash`/`s3_object_version`/(holdings only)`handler` -- is a STOP. **A REFUSAL IS
EVIDENCE, NOT AN OBSTACLE; this half NEVER authorises widening the admission at the terminal to force the pass.** The four
applies are SEQUENCED; after the LAST round-7 apply, a final all-ten-roots plan MUST read CLEAN (0 to add/change/destroy),
which is the discriminator that no widening leaked.

## Both branches covered

- **The producer applies** (both halves at HEAD naming this blob; the apply pass): a fresh per-root plan, the SUBTRACTION
  GATE above over all ten roots (denominator printed), apply the holdings root IFF the gate passes -- `.tools/safe-apply.sh`,
  vendored binary, under a change-management ledger OPENED before the apply (sentinel committed before, closed before the
  grading reads), `0 to destroy`, rc 0, 0-diff after; then `served == CodeSha256 == rAAn3bt7...`. **Arm (e), under the
  deployed role and bytes:** reuse `battery_ib_rtf_10.py`'s bounded-principal mechanism (rtf-9 packet blob a1f36b95b2), real
  request as `irpt-holdings-role`, route/function/role printed, a granted account reads a scope-resolved answer -- never
  `FIRM_BINDING` with `firm_id` absent. This half does NOT predict; arm (e) measures.
- **The producer STOPS** (a half absent; the blob differs; the gate refuses on any root): nothing applied, or rolled back per
  the key and verified by read-back; the route stays as S100 measured it (the refusal). A rollback ONLY on a measured
  REGRESSION against the before-state this packet prints, never on a forward-looking FAIL token alone.

## What this half does NOT sign

Any `_authz/`, `_scope/`, `_ids/`, `directory/`, `snapshot.py` SOURCE change (`directory/handler.py`'s own two-step is
UNEDITED); any IAM/bucket/prefix/route change (there is none); any layer change; the three sibling cells' OWN acts (each
carries its own packet+halves); the export submit-wiring gap (row W1-S43, a separate follow-on); FWD-11. `W = 1` -- the sole
writer of what `irpt-holdings` serves is a Lambda code deployment of its own zip; no API Gateway response cache on this route
(0 hits), no CloudFront override, no shared warm cache in `entry.py`'s `Entry(...)`.

## RE-SIGN CLARIFICATION (1.0.0_SA_CTO 98624, scope item 1) -- the export/performance sibling change is the round-7 build, packet-keyed, not "pre-round-7 drift"

1.0.0_SA_CTO CONCURRED with this arm-(d) construction and asked for a THIRD class admitting the "pre-round-7 drift" rows W4-S46/W1-S45 report on the export and performance roots (tagged Cell IB-s-14 / IB-s-11). MEASURED BY CONTENT, that change is NOT separate and NOT pre-round-7: the changed resource's after-`source_code_hash` IS the SIBLING round-7 build -- export `cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4=` == IB-rtg-1's packet BUILT sha (EXACT); performance `W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA=` == IB-rtg-3's packet BUILT sha (EXACT) -- and W4-S46's own plan read `0 to add, 1 to change, 0 to destroy` (ONE `aws_lambda_function` change per root, not two). The `Cell = IB-s-14 / IB-s-11` value is a STALE `.tf` tag the round-7 cells did not rewrite: it EQUALS the deployed tag, so it is NOT a change in the plan and NOT a separate artifact. W4-S46 (holdings worker) misattributed via the stale tag; W1-S45 (export worker) read the same mechanism correctly as a sibling build.

⛔ SO NO THIRD "pre-round-7 drift" CLASS IS ADDED -- it would admit a PHANTOM. The sibling admission (class 2 above) already covers this change, keyed by the sibling cell's SIGNED PACKET, and a PACKET/SHA key is strictly TIGHTER than a TAG key: admitting "anything tagged IB-s-14/IB-s-11" would let a genuinely-unintended IB-s-14-tagged artifact through, whereas admitting "after == the sibling packet's built sha" STOPs on it.

⭐ AND THE SIBLING ADMISSION COVERS EACH SIBLING CELL'S FULL DECLARED CHANGE SET, NOT ONLY ITS FUNCTION BUILD. At HEAD (all four drained) the EXPORT sibling root now also shows IB-rtg-1's OWN `aws_iam_role_policy.export_render_receipt` `["create"]` (its K-IAM, drained to CLOUD), which W4-S46's PRE-drain read could not see. The admission for a sibling root is EXACTLY the change set that sibling's signed packet declares (export = the function build `cn8YKEP2...` + the IAM policy create; performance = `W4rYXgZz...`; ops/irpt-status = `B0AmyfRK...`; holdings = `rAAn3bt7...` + its `handler` flip) and NOTHING outside it -- a STOP stands on anything else.

The CTO's safety requirement stands VERBATIM and is enforced by the packet, not the stale tag: the applier pins its OWN declared build, a STOP on anything outside the enumerated per-packet sets, and this is NEVER an authorization to carry a sibling's build forward. 1.0.0_SA_CTO is asked to re-sign its four halves to THIS packet-keyed construction so both halves carry the same (tighter) bound.

**Push state:** LOCAL -- this half RE-SIGNED this tick on CLOUD (clarification above); origin/CLOUD read at the drive-log send (MSTR pushes CLOUD).
