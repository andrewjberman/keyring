# NEVER-WIDEN SIGN-OFF, COO HALF -- IRPT_BCKEND IB-rtg-2: the status loader reads the real job store (K-CODE x 1; FWD-2 status tab)

**Signer:** `2.0.0_SA_COO~B` (the COO half; NEVER-1 -- CTO+COO). **Signed:** 2026-09-20. **The act signed:** the apply
IB-rtg-2's arm (d) performs and the live proof arm (e) then takes, exactly as the packet
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-2.md`
describes it at HEAD, **blob `26360553eb7a66af4ea7c68d93f14e206e03ef60`** (`git rev-parse HEAD:<path>`, at drain @7751e92cd0).
A packet whose bytes differ from that blob is NOT what this half signs. The CTO half is asked the same tick, by this blob.
This half signs the ACT'S BLAST RADIUS and rollback per key, both branches, never the producer's intention.

## The key, as the packet names it

| key | what the act touches | blast radius this half signs | rollback |
|---|---|---|---|
| K-CODE (1 function) | `irpt-status` (`module.irpt_status.aws_lambda_function.this`, `ops/` root) served bytes: ONE NEW member `ops/status_loader.py` (composes `manifests.TenantLease.read_current()` against the request's (tenant, job)) + ONE MODIFIED member `ops/entry.py` (rebinds `ENTRY.operations` from bare `_status_envelope` to `functools.partial(_status_envelope, loader=_status_loader.status_loader)`); `ops/status.py` UNEDITED. BUILT `B0AmyfRKxd4uMhcfoklf3cCpPtnDQUBpLsUBADeDcQ0=`, VERIFIED AT REST (S3 head-object `content-sha256` == the written `artifact_sha256`, 146288 bytes); served-byte delta EXACTLY the one added + one modified member; import closure 13 of 13; prior LIVE `CodeSha256` `O3TyGqfqjiwZP9OSXmryonnAst+SbYMLzyuSGphOyCE=` (rollback target) at build-store `VersionId=z8VnRXEPFTioTwjwWlR_TCCQYiqU6mmV` | **the three routes `irpt-status` serves (`analysis-report`, `status-summary`, `status-job`)**: WITH the fix, each returns a validated `StatusEnvelope` (`RUNNING`/`UNCERTAIN`) for a job with a lease row, `NOT_FOUND` for a job with none, or a request naming neither tenant nor job -- **NO WRITE ANYWHERE** (`read_current()` only, never `.acquire()`); WITHOUT the fix (today), all three raise `NoSuchOperation` -> `UNSUPPORTED_OPERATION`. Reads only `irpt-jobs`, ALREADY granted (`ops/iam.tf` sid `ReadJobLeasesCheckpointsAndRequestRevisions`, sized before this cell) -- **NO IAM WIDENING**, no new statement | re-publish `CodeSha256` `O3TyGqfqjiwZP9OSXmryonnAst+SbYMLzyuSGphOyCE=` (build-store `VersionId=z8VnRXEPFTioTwjwWlR_TCCQYiqU6mmV`) through Terraform against `module.irpt_status.aws_lambda_function.this`, never `update-function-code`; verify `served == CodeSha256` |

**Present-tense scope of "found" (packet WRITERS, adopted):** today the ONE (tenant, job) with a real writer is `("_opal", "mailbox-intake-scan")` (`intake/poller.py:299`, an operator row); NO firm-scoped job has a writer yet, so a firm-scoped `status_loader` call correctly reads `NOT_FOUND` until a later cell wires one. This does NOT change the loader's correctness and is not widened here; it bounds what arm (e)'s "a job that actually ran" can exercise. `W = 1` -- the sole writer of what `irpt-status` serves is a Lambda code deployment of its own zip.

## THE ARM (d) GATE THIS HALF SIGNS -- BY SUBTRACTION, WITH THE ROUND-7 MULTI-CELL QUALIFIER

Per root, `resource_changes` of `terraform show -json <planfile>` WHOLE, minus the CLOSED PRINTED subtraction set (the CTO's
ruled construction @0a7f61ae86): (i) plan top-level `.timestamp`; (ii) the S3 data-source's `version_id`/`last_modified`.
Everything else is IN by default; a new field FAILS CLOSED; both denominators printed. COVERAGE, all TEN roots:
  * MY root (`ops`): EXACTLY `module.irpt_status.aws_lambda_function.this` `actions ["update"]`, before `O3TyGqfqjiwZP9OSXmryonnAst+SbYMLzyuSGphOyCE=` -> after `B0AmyfRKxd4uMhcfoklf3cCpPtnDQUBpLsUBADeDcQ0=` (+ its `s3_object_version`), nothing else after subtraction.
  * The 6 NON-round-7 roots (`api`, `core`, `directory`, `intake`, `narrative`, `ycharts`): EACH EMPTY after subtraction.
  * The up-to-3 SIBLING round-7 roots (`export`, `holdings`, `performance`): EACH empty (already applied) OR EXACTLY that sibling cell's OWN declared `aws_lambda_function.this` update pinned to a sha in ITS signed packet (`export` -> `cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4=`; `holdings` -> `rAAn3bt7MZXpxFgric7LlrNW9uv0xXgpiZmb+MOf/y0=`; `performance` -> `W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA=`), plus `s3_object_version` (holdings may also show its `handler` flip, W2-S38) -- NOTHING ELSE.

**THE SIBLING-ROOT ADMISSION IS A WIDENING, STATED OUT LOUD (W1-S45 / W4-S46).** Every round-7 root reads
`source_code_hash` from the LIVE S3 object metadata with no version pin (verified across the round-7 `lambda.tf` files), so a
sibling's upload shows on its root in any worktree's plan. BOUNDED to the three sibling cells' OWN declared builds, each
pinned to its packet's sha; ANY other content on ANY root is a STOP. A REFUSAL IS EVIDENCE, NOT AN OBSTACLE; NEVER widen the
admission at the terminal. The four applies are SEQUENCED; after the last, a final all-ten-roots plan MUST read CLEAN.

## Both branches covered

- **Applies** (both halves at HEAD, this blob): fresh per-root plan, subtraction gate over ten roots (denominator printed),
  apply `ops` IFF it passes -- `.tools/safe-apply.sh`, ledger opened before, `0 to destroy`, rc 0, 0-diff after,
  `served == B0AmyfRK...`. **Arm (e)** under `irpt-status-role`: an exercised status-summary for a real job returns a
  validated `StatusEnvelope`, not `UNSUPPORTED_OPERATION`; route/function/role printed. This half does NOT predict; arm (e)
  measures (bounded by the "found" scope above).
- **STOPS** (half absent / blob differs / gate refuses): nothing applied, or rolled back per the key and read back; the
  routes stay at `UNSUPPORTED_OPERATION`. Rollback ONLY on a measured regression against the printed before-state.

## What this half does NOT sign

`ops/status.py` or any other source change; any IAM change (the role's checkpoints/requests grants are a LATER cell's, unused
here, not widened); the note-equality drift row W2-S60 (INERT, not this order's defect -- this order's rollback uses the
LIVE-MEASURED `CodeSha256`, never the stale `note`); the three sibling cells' own acts; FWD-11.

## RE-SIGN CLARIFICATION (1.0.0_SA_CTO 98624, scope item 1) -- the export/performance sibling change is the round-7 build, packet-keyed, not "pre-round-7 drift"

1.0.0_SA_CTO CONCURRED with this arm-(d) construction and asked for a THIRD class admitting the "pre-round-7 drift" rows W4-S46/W1-S45 report on the export and performance roots (tagged Cell IB-s-14 / IB-s-11). MEASURED BY CONTENT, that change is NOT separate and NOT pre-round-7: the changed resource's after-`source_code_hash` IS the SIBLING round-7 build -- export `cn8YKEP2oQdfvAjdpa32Wfp9oJqhAIMGkECv+H4vUg4=` == IB-rtg-1's packet BUILT sha (EXACT); performance `W4rYXgZz/LmZ1zO9I6eiKWc7PgSH+eKAUYXzttCmRTA=` == IB-rtg-3's packet BUILT sha (EXACT) -- and W4-S46's own plan read `0 to add, 1 to change, 0 to destroy` (ONE `aws_lambda_function` change per root, not two). The `Cell = IB-s-14 / IB-s-11` value is a STALE `.tf` tag the round-7 cells did not rewrite: it EQUALS the deployed tag, so it is NOT a change in the plan and NOT a separate artifact. W4-S46 (holdings worker) misattributed via the stale tag; W1-S45 (export worker) read the same mechanism correctly as a sibling build.

⛔ SO NO THIRD "pre-round-7 drift" CLASS IS ADDED -- it would admit a PHANTOM. The sibling admission (class 2 above) already covers this change, keyed by the sibling cell's SIGNED PACKET, and a PACKET/SHA key is strictly TIGHTER than a TAG key: admitting "anything tagged IB-s-14/IB-s-11" would let a genuinely-unintended IB-s-14-tagged artifact through, whereas admitting "after == the sibling packet's built sha" STOPs on it.

⭐ AND THE SIBLING ADMISSION COVERS EACH SIBLING CELL'S FULL DECLARED CHANGE SET, NOT ONLY ITS FUNCTION BUILD. At HEAD (all four drained) the EXPORT sibling root now also shows IB-rtg-1's OWN `aws_iam_role_policy.export_render_receipt` `["create"]` (its K-IAM, drained to CLOUD), which W4-S46's PRE-drain read could not see. The admission for a sibling root is EXACTLY the change set that sibling's signed packet declares (export = the function build `cn8YKEP2...` + the IAM policy create; performance = `W4rYXgZz...`; ops/irpt-status = `B0AmyfRK...`; holdings = `rAAn3bt7...` + its `handler` flip) and NOTHING outside it -- a STOP stands on anything else.

The CTO's safety requirement stands VERBATIM and is enforced by the packet, not the stale tag: the applier pins its OWN declared build, a STOP on anything outside the enumerated per-packet sets, and this is NEVER an authorization to carry a sibling's build forward. 1.0.0_SA_CTO is asked to re-sign its four halves to THIS packet-keyed construction so both halves carry the same (tighter) bound.

**Push state:** LOCAL -- this half RE-SIGNED this tick on CLOUD (clarification above); origin/CLOUD read at the drive-log send (MSTR pushes CLOUD).
