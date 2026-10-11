# TO IRPT_DASHBD.TO-DB-b-123 -- APPLY under the signed pair: overwrite exactly two keys so Cottonwood's served method row 3 states income ABSENT; capture first, ledger first

<to_id>IRPT_DASHBD.TO-DB-b-123</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~98</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>67</round>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 4723 ("cut the apply cell, ledger first") on the signed pair: CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_METHOD_ROW3_INCOME_CTO_HALF.md` @59da96c840, COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_METHOD_ROW3_INCOME_COO_HALF.md` @2995b0bff4, both on the packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~97/NEVER_WIDEN_PACKET_METHOD_ROW3_INCOME.md` sha256 `ba3a7fb2fb8e87510886863787ca2915293f0a021666c4cf05192eab2d37c66b` | **Decomp cell:** `DB-b-123` (decomposition section 69) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-122 (drained @d8747d6d39).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-98` (branch `wk-irpt-dashbd-67-98`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~98/`. Captures and any object body go OUTSIDE the repo, under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~98/`.

**The act (`DB-b-123`).** ONE overwrite of EXACTLY two keys in bucket `opal-data-cottonwood`:
`irpt/cottonwood/gold/dim_return_method/method_version=3/data.parquet` and `.../method_version=3/manifest.json`. Nothing else is written,
copied or deleted, in this bucket or any other. Read the packet and BOTH halves first, whole; the conditions below restate them and the halves
govern where they differ. Verify the packet's sha256 equals the one in this order's header before anything else; if not, STOP.

All AWS calls go through the `.tools/aws` shim (or boto3 exactly as `data/assets/scripts/silver/commonwealth_account_return_daily.py`
builds its client: read how it does). Do these in this order; record each in `METHOD_ROW3_APPLY.json`:

1. **Ledger first.** Open a change-management entry BEFORE any write: `python .tools/deploy_ledger.py open --help`, then `open` with a slug
   like `irpt-dashbd-db-b-123-method-row3-income-20261011`, your serial as author, and three legs: the capture (kind `verify`), the overwrite of
   the two keys (kind `activation`), the served read-back (kind `verify`). Commit the opened entry in your worktree before the write.
   `ledger`: {slug, entry (the repo path of the change_management file), opened_before_write, closed}.
2. **Capture, and it is the rollback.** `head-object` each of the two keys: the ETags MUST read `7b70c246337d26fbba60eac594c21f0f`
   (data.parquet) and `5951829e6839cf07e4ef3ce1afdca914` (manifest.json), sizes 10421 and 1831. `get-object` each body to the folder outside
   the repo; record sha256, size, ETag, saved_path. `get-bucket-versioning` read and recorded (`Enabled`, `Suspended`, or `NOT_VERSIONED` for an
   empty answer); if versioned, also record each key's current VersionId. `capture`: {keys: [...], etags_as_listed, bucket_versioning}.
   **Branch B:** an ETag or size that differs, a capture that fails, or any AccessDenied -> the act STOPS, writes NOTHING, closes the ledger
   entry as not performed (the tool's `hold` or `close` with that statement), files a row, and reports `branch: "B_STOPPED"`, `s3_writes: 0`,
   `stop_reason`, `row`.
3. **Dry run and diff BEFORE the write.** Read the captured `data.parquet` row (pyarrow, one row). Build the new row with the producer's own
   dry run: `emit_method_row(None, firm_scope(entry), thresholds, upload=False, src=entry)` where `entry` is the `_commonwealth_delivery`
   entry of `data/assets/scripts/gold/irpt_reporting/sources.json` and `thresholds` are the stamped manifest's
   (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json`, `method_row.thresholds` plus
   `threshold_claims` exactly as that mint passed them: read `commonwealth_account_return_daily.py` near line 835 for the exact shape). Diff
   column by column, `measured_at` excluded: the ONLY differences allowed are `income_basis` (`cash_when_received` -> null) and the two new
   columns `income_basis_claim`, `income_basis_reason`. ANY other difference -> Branch B, nothing written.
4. **The write (Branch A).** ONE call: `emit_method_row(s3, <the same firm scope>, <the same thresholds>, upload=True, src=entry)`. NOT the
   mint's `--apply` (it refuses an existing key) and NO other producer function, NO run for any other firm or source. `keys_written`.
5. **Read back the SERVED object.** `head-object` both keys (`head_after`: key, size, ETag, LastModified, VersionId if any). `get-object`
   `data.parquet` to the outside folder and read its one row: `served_after` {method_version, income_basis, income_basis_claim,
   income_basis_reason}; diff it against the captured row as in step 3 (`diff`: {columns_changed, other_columns_moved}). If the diff is wrong
   AFTER the write: ROLL BACK now -- `put-object` each captured body back to its key, `head-object` to confirm size and re-read sha256 -- record
   `rolled_back: true` with the evidence, file a row, and report it loud. No key is ever deleted, in the act or the rollback.
6. **The mint's own verify.** Run the mint's verify of the method row (`commonwealth_account_return_daily.py` near lines 981-989: use its
   function if it can be called alone on the method row; otherwise perform exactly its read -- 1 row, `method_version` 3, the five `*_claim`
   columns `absent` -- and say which you did). `mint_verify` must contain the literal `method_row=match` only if that is what was read.
7. **Close the ledger entry** with each leg's proof (`deploy_ledger.py close-leg` / `close`), and commit it.

<criterion id="DB67-1-AC1" cell_refs="DB-b-123"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r67/p67_round67.py" . DB67-1-AC1</invocation><expect>DB67-1-AC1 PASS</expect></criterion>
`DB67-1-AC1` -- both keys are captured outside the repo with their hashes, bucket versioning is read, and the ledger entry was opened before the write. Base: FAIL.

<criterion id="DB67-1-AC2" cell_refs="DB-b-123"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r67/p67_round67.py" . DB67-1-AC2</invocation><expect>DB67-1-AC2 PASS</expect></criterion>
`DB67-1-AC2` -- either the two keys are written, only the three income members moved, the served row states income absent, the mint's verify still matches and the ledger is closed; or the act stopped before the write with nothing written, a reason and a row. Base: FAIL.

<expected_criteria>DB67-1-AC1,DB67-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (repo files) and EXACTLY the two S3 keys named above (one overwrite each; a rollback put of the captured
  bytes if step 5 requires it). Everything else is read, never edited or written.
- **S3 reads allowed:** `head-object` and `get-object` on those two keys, `get-bucket-versioning` on that bucket, `list-object-versions`
  limited to that prefix if the bucket is versioned. NO read of any `account_return_daily` day key or body, no other prefix, no other bucket.
- **Never:** a delete of any key or version; a Lambda, Terraform or IAM act; a run of the gold producer or the mint for any firm or source
  (CTO half condition 5: this pair covers the two Cottonwood keys and nothing else; a 49 Financial method row is not written); a retry of a
  denied call by another route; a push.
- **Do not leave it half-landed.** Once the write is made you finish steps 5 to 7 in this session, or roll back and report loud.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W98-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content. The method row holds no client data; write no account id and no figure anywhere.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~98/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-123.method-row3-income-apply.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 69 (round 67), cell `DB-b-123`.
<owned_cells>DB-b-123</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB67-1-AC1,DB67-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~98/IRPT_DASHBD.TO-DB-b-123.method-row3-income-apply.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB67-1-AC1,DB67-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the branch taken; each criterion's last line; the ledger slug, when it was opened and that it is closed; the capture (each key's ETag, size, sha256, where saved; bucket versioning); the pre-write diff; the write's return; the head of both keys after; the served row's three income members as read back; the mint's verify line and how it was produced; whether anything was rolled back; and any row ids. State plainly anything you could not do.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the blast radius is the signed pair's: exactly two keys, 2 writers and 1 reader counted in the packet, zero readers of an income member.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; the put permission is unread (both halves say so) and a denial is Branch B, nothing written.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route serves this object to a page; the packet counts its one code reader.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule writes this address (the packet's section 3: the scheduled producer emits for declared sources only).
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface reads this object.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; both criteria FAIL at base (no record), and the act's own Branch B is its adversary.
lane: the <paths> block IS the grant, plus exactly the two S3 keys the WORKER FACE names.
</preflight>
