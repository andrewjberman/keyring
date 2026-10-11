# TO IRPT_DASHBD.TO-DB-b-130 -- APPLY under the signed pair: overwrite exactly two keys so Cottonwood's served method row 3 states the income reason worded for the method; capture first, ledger first

<to_id>IRPT_DASHBD.TO-DB-b-130</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~CB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<placeholders>NONE</placeholders>
<round>69</round>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 5263 ("the applier is 0.7.0_AE_CloudOps~CB2 ... Cut the order to it") on the signed pair: packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~103/NEVER_WIDEN_PACKET_METHOD_ROW3_INCOME_REASON.md` sha256 `6fbce1ff47a174d0f9f019b79a0c6b3693f473fb5ed1cb60622cc6ffcfe0d064`; COO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_METHOD_ROW3_INCOME_REASON_COO_HALF.md` @34cc62f4f7; CTO half `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_METHOD_ROW3_INCOME_REASON_CTO_HALF.md` @34a6a32212

---

## WORKER FACE

You are `0.7.0_AE_CloudOps~CB2`. Run from a tree on `box/dell2` that carries commit `780ba55bde` or later (the producer's reworded
sentence arrived with it): `git merge-base --is-ancestor 780ba55bde HEAD` must exit 0, or STOP. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~CB2/`. Captures and any object body go OUTSIDE the repo, under
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.7.0_AE_CloudOps~CB2/`.

**The act (`DB-b-130`).** ONE overwrite of EXACTLY two keys in bucket `opal-data-cottonwood`:
`irpt/cottonwood/gold/dim_return_method/method_version=3/data.parquet` and `.../method_version=3/manifest.json`. Nothing else is written,
copied or deleted, in this bucket or any other. Read the packet and BOTH halves first, whole; the steps below restate them and the halves
govern where they differ. Verify the packet's sha256 equals the one in this order's header before anything else; if not, STOP.

All AWS calls go through the `.tools/aws` shim (or boto3 exactly as `data/assets/scripts/silver/commonwealth_account_return_daily.py`
builds its client). The same act was performed on these two keys at 10:38Z today; its record is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~98/METHOD_ROW3_APPLY.json` and shows the shape of each step. Do these
in this order; record each in `METHOD_ROW3_REASON_APPLY.json` in your folder:

1. **Ledger first.** Open a change-management entry BEFORE any write (`python .tools/deploy_ledger.py open --help`), slug
   `irpt-dashbd-db-b-130-method-row3-income-reason-20261011`, your serial as author, three legs: the capture (kind `verify`), the overwrite
   of the two keys (kind `activation`), the served read-back (kind `verify`). Commit the opened entry before the write.
   `ledger`: {slug, entry (the repo path of the change_management file), opened_before_write, closed}.
2. **Capture, and it is the rollback.** `head-object` each key: the ETags MUST read `9c774f3770e82ed5e7e6b2a4ebe3e7d3` (data.parquet) and
   `6d5aabdd1e0f3cc9ff2a6c544bd327fd` (manifest.json), sizes 11641 and 2037. `get-object` each body to the folder outside the repo; record
   sha256, size, ETag, VersionId, saved_path. `get-bucket-versioning` read and recorded; it must read `Enabled`.
   `capture`: {keys: [...], etags_as_listed, bucket_versioning}.
   **Branch B:** an ETag or size that differs, a capture that fails, versioning not `Enabled`, or any AccessDenied (on a read or on the put)
   -> the act STOPS, writes NOTHING more, closes the ledger entry as not performed, files a row, and records `branch: "B_STOPPED"`,
   `s3_writes: 0`, `stop_reason`, `row`. A denied put is reported, never retried by another route or another role: the CTO names another
   applier.
3. **Dry run and diff BEFORE the write.** Read the captured `data.parquet` row (pyarrow, one row). Build the new row with the producer's
   own dry run: `emit_method_row(None, firm_scope(entry), thresholds, upload=False, src=entry)` where `entry` is the
   `_commonwealth_delivery` entry of `data/assets/scripts/gold/irpt_reporting/sources.json` and `thresholds` are the stamped manifest's
   (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~79/ard_cottonwood_manifest.json`, `method_row.thresholds` plus
   `threshold_claims` exactly as that mint passed them: read `commonwealth_account_return_daily.py` near line 835 for the shape). Diff
   column by column, `measured_at` excluded: the ONLY difference allowed is `income_basis_reason`, and its new value must equal, exactly:
   `A positions-based method values the account from its positions and cash, so income is inside that value and is not separated from it: the method states no income basis.`
   ANY other difference -> Branch B, nothing written.
4. **The write (Branch A).** ONE call: `emit_method_row(s3, <the same firm scope>, <the same thresholds>, upload=True, src=entry)`. NOT the
   mint's `--apply` (it refuses an existing key), NO other producer function, NO run for any other firm or source. `keys_written`.
5. **Read back the SERVED object.** `head-object` both keys (`head_after`: key, size, ETag, LastModified, VersionId). `get-object`
   `data.parquet` to the outside folder and read its one row: `served_after` {method_version, income_basis, income_basis_claim,
   income_basis_reason}; diff it against the captured row as in step 3 (`diff`: {columns_changed, other_columns_moved}). If the diff is
   wrong AFTER the write, or only one key was written: ROLL BACK now -- restore each key from the version id captured in step 2
   (`copy-object` of that version onto the same key, or `get-object --version-id` then `put-object`), `head-object` to confirm size and
   ETag equal the captured ones -- record `rolled_back: true` with the evidence, file a row, and report it loud. No key and no version is
   ever deleted, in the act or the rollback.
6. **The mint's own verify.** Run the mint's verify of the method row (`commonwealth_account_return_daily.py` near lines 1031-1037: its
   function if it can be called alone on the method row; otherwise exactly its read -- 1 row, `method_version` 3, the five `*_claim`
   threshold columns `absent` -- and say which you did). `mint_verify` contains the literal `method_row=match` only if that is what was read.
7. **Close the ledger entry** with each leg's proof (`deploy_ledger.py close-leg` / `close`), and commit it.

<criterion id="DB69-1-AC1" cell_refs="DB-b-130"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r69/p69_round69.py" . DB69-1-AC1</invocation><expect>DB69-1-AC1 PASS</expect></criterion>
`DB69-1-AC1` -- both keys are captured outside the repo with their hashes, bucket versioning is read, and the ledger entry was opened before the write. Base: FAIL.

<criterion id="DB69-1-AC2" cell_refs="DB-b-130"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r69/p69_round69.py" . DB69-1-AC2</invocation><expect>DB69-1-AC2 PASS</expect></criterion>
`DB69-1-AC2` -- either the two keys are written, only the income reason moved, the served row states the signed sentence, the mint's verify still matches and the ledger is closed; or the act stopped before the write with nothing written, a reason and a row. Base: FAIL.

<expected_criteria>DB69-1-AC1,DB69-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (repo files) and EXACTLY the two S3 keys named above (one overwrite each; a restore of the captured
  version if step 5 requires it). Everything else is read, never edited or written.
- **S3 reads allowed:** `head-object` and `get-object` on those two keys, `get-bucket-versioning` on that bucket, `list-object-versions`
  limited to that prefix. NO read of any `account_return_daily` day key or body, no other prefix, no other bucket.
- **Never:** a delete of any key or version; a Lambda, Terraform or IAM act (no role is widened for this); a run of the gold producer or
  the mint for any firm or source (a 49 Financial method row is not written); a retry of a denied call by another route; a push.
- **Do not leave it half-landed.** Once the write is made you finish steps 5 to 7 in this session, or roll back and report loud.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by
  a route this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-CB2-S<k>` (read the file for the next free `k`), with the real
  current UTC time; append as BYTES, never re-encode the existing content. The method row holds no client data; write no account id and
  no figure anywhere.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~CB2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-130.income-reason-apply.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 71 (round 69), cell `DB-b-130`.
<owned_cells>DB-b-130</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB69-1-AC1,DB69-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~CB2/IRPT_DASHBD.TO-DB-b-130.income-reason-apply.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB69-1-AC1,DB69-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~D2`, under 150 words, citing `METHOD_ROW3_REASON_APPLY.json` and its commit: the branch taken; each criterion's last line; that the ledger is closed; whether anything was rolled back; any row ids; your push state as measured. State plainly anything you could not do.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the blast radius is the signed pair's: exactly two keys, 2 writers and 1 reader counted in the packet, zero readers of an income member.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; the applier's put permission is unread (both halves say so) and a denial is Branch B, nothing written, the CTO naming another applier.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route serves this object to a page; the packet counts its one code reader.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule writes this address (the packet's section 3).
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface reads this object.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; both criteria FAIL at base (no record), and the act's own Branch B is its adversary.
lane: the <paths> block IS the grant, plus exactly the two S3 keys the WORKER FACE names.
</preflight>
