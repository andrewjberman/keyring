# TO IRPT_DASHBD.TO-DB-c-11 -- the SHARED ZIP's REGISTRY PIN: why the Cottonwood function refused `registry lookup('z09')`, the minimal re-pin proven by a differential of the producer's own firm derivation, and the UNSIGNED ADDENDUM PACKET for the second zip upload; a read and a packet; nothing is uploaded, planned, applied or invoked

<to_id>IRPT_DASHBD.TO-DB-c-11</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~406</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>118</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the STOP of `IRPT_DASHBD.TO-DB-c-9` by `0.7.0_AE_CloudOps~DB2` (msg 8042; its record `deliverables/0.7.0_AE_CloudOps~DB2/COTTONWOOD_APPLY_RECORD.json` and ledger `org/critical_paths/change_management/irpt-dashbd-cottonwood-holdings-performance-20261015*`), decomposition section 5 | **Rows:** IRPT_DASHBD-D2-W406-S<k> | **Decomp cell:** `DB-c-11` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 5) | **outcome_ref:** FWD-2, FWD-11 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-406`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~406/`. Never push. No client data is read or written. A raw `aws s3`/`aws s3api` call in a shell call is denied by the repo's rail; do every S3 read from a short Python script (boto3, your own identity; a GET of the zip by version id, LIST and HEAD only) kept in your private folder `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~406/` and not committed.

**Why.** The applier stopped at the first catch-up invoke: the Cottonwood function refused `registry lookup('z09') failed: KeyError`. The shared zip `investor-reporting/irpt-holdings-performance-lambda.zip` (bucket `opal-313476888478-lambda-artifacts`, current S3 version `vrBQAr57i.p3TMhjdSld3c_E5HMqX8iy`) is built from `infra/aws/lambda/ci/lambda-source-map.json`, function `irpt-holdings-performance-lambda`, whose `staged_from` pins seven registry members (`infra/logic/registry/{systems,scopes,tiers,exemptions,remediations,resources,reporting_policies}.json`) to old commits. The issuer measured: the pinned `scopes.json` (commit `14b52ca13a`, 15,565 bytes, sha256 `a4e0637257b6...`) has 11 scope rows and no `z09`; HEAD's has 14 rows including `z09`. The producer derives the Cottonwood firm from the registry (`holdings_performance.py` `firm_scope()`). The issuer extracted the live zip and ran the producer's `firm_scope()` for the three declared channels (`schwab_08335338`, `orion`, `blackdiamond_z09`): `z09` refused, the other two `49financial` and `inflection`; replacing ONLY `scopes.json` with HEAD's blob, `z09` resolved to `cottonwood` and the other two did not change. This cell re-proves that as a committed record and writes the addendum packet the CTO's half and the issuer's half sign before any second upload.

**The cell (`DB-c-11`).**
1. **The zip and the pins.** Read the zip by the version id above (a GET; `zipfile` in memory). For EACH of the seven registry members record `name`, `pin` and `pinned_sha256` (from the source map), `in_zip_sha256` (the member inside the zip, which must equal the pinned blob's sha256 from `git show <pin>:<repo_path>`), `head_sha256` (the blob at `HEAD`) and `differs_from_head`. Record `zip` {`bucket`, `key`, `version_id`, `members` (the count)}.
2. **`scopes.json`.** From the git blobs (pinned and `HEAD`) record `scopes_diff` {`added`, `removed`, `changed`}: sorted lists of scope KEYS (the `key` of each row; names only), by comparing each row's JSON. `z09` must be in `added`.
3. **The differential.** Extract the zip twice into scratch outside the repo (`live` and `fixed`). In `fixed` replace the member(s) of your minimal set (step 4) with the blob at the new pin. In EACH tree run, in a fresh `python -I` process with the tree as the root on `sys.path` (and `data/assets/scripts/gold/irpt_holdings_performance` and `data/assets/scripts/lib`), the producer's own `holdings_performance.firm_scope(src)` for each of the three channel entries of `data/assets/scripts/gold/irpt_holdings_performance/sources.json` (read inside that tree), and record the result per channel (the firm token, or the text `REFUSED: ...`). Record `channels` {`in_zip_tree`, `with_repinned_members`} each a map from the three channel keys to the result. The live tree must refuse `blackdiamond_z09`; the fixed tree must resolve it to `cottonwood`; `schwab_08335338` and `orion` must be identical in both. Do not run the producer's `main`; do not touch AWS beyond the zip GET.
4. **The minimal re-pin.** `minimal_repin` is the smallest set of the seven members whose replacement makes the fixed tree resolve `z09` with the other two channels unchanged: try `scopes.json` alone first; add another member only if the derivation still fails (state which in `words`). Each entry is {`member`, `new_pin` (a 40-hex commit that is an ancestor of `HEAD` and holds the blob; the issuer's candidate is the latest commit touching `scopes.json`: `git log -1 --format=%H -- infra/logic/registry/scopes.json`), `new_sha256` (of the blob at that pin)}. Set `unchanged_for_other_channels` true only if the 49 Financial and Inflection results are identical. State in `words` whether the added rows (names only) could change those two channels' derivation (the producer's `firm_scope()` refuses a monolith that carries two scopes; read why it does not here).
5. **The addendum packet** `NEVER_WIDEN_ADDENDUM_DB-c-11_R118.md` (5,000 characters or more), UNSIGNED, with these `## ` headings in this order: `## Change set` (the source-map edit: for each re-pinned member the `pin` and `sha256` fields change, nothing else; the new pins and hashes; the statement that no Terraform file changes); `## Build and member diff` (build with `infra/aws/lambda/ci/build-and-upload.sh` from the commit that carries the edit, compare to the live zip version above; the member diff must be EXACTLY the re-pinned members, each equal to the blob at its new pin; any other difference is a STOP before upload; the new zip's version becomes the artifact the three functions read); `## Plan` (a targeted or full plan must read 0 to add, 3 to change (the three functions `module.irpt_holdings_performance.aws_lambda_function.this`, `module.irpt_holdings_performance_inf...` and `module.irpt_holdings_performance_cot...`), 0 to destroy; anything else a STOP); `## Resume at the catch-up` (after the apply: the open ledger `irpt-dashbd-cottonwood-holdings-performance-20261015` is continued; the 12-date catch-up, the after-read, the 1.1+1.2 reader check, the planted listing test and the ENABLE exactly as steps 6 to 8 of `IRPT_DASHBD.TO-DB-c-9`; the catch-up dates and keys are the first packet's, re-derived by the builders to the as-of date at that time); `## Both branches` (success: three functions on the new zip, the 49 Financial and Inflection derivations unchanged by the differential, the catch-up proceeds; failure of the upload or the apply: what is live; failure midway in the catch-up: as the first packet); `## Rollback` (the previous zip is S3 version `vrBQAr57i.p3TMhjdSld3c_E5HMqX8iy`: the rollback is restoring that version as the current object by a copy over the same key (a write, not a delete) and a plan that reads 0/3/0 back; no delete); `## Questions for the CTO's half` (at least: that this is a second upload not covered by the first pair; whether re-pinning `scopes.json` to HEAD's blob is the intended pin or a pin at a named commit; whether the other six members stay pinned; the 49 Financial and Inflection next scheduled fires on the new zip; Andrew's word for any delete); `## Not in this packet` (what you did not establish). The packet states it is UNSIGNED and carries no signature, and names the live zip version `vrBQAr57i...`, each re-pinned member and its new pin, the Cottonwood function `irpt-cot-holdings-performance-lambda` and the catch-up.
6. **Record** `SCOPES_PIN_READ_R118.json` in your folder with exactly: `claim` ("measured"); `zip`; `registry_members` (the seven); `scopes_diff`; `channels`; `minimal_repin`; `unchanged_for_other_channels`; `words`; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `aws_writes` 0}; `pushed` false; `deployed` false. Names, counts, hashes, commits and words only.

<criterion id="DBC118-1-AC1" cell_refs="DB-c-11"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r118/p118_bcw.py" . DBC118-1-AC1</invocation><expect>DBC118-1-AC1 PASS</expect></criterion>
`DBC118-1-AC1` -- the record is complete; the seven registry members' pinned, in-zip and HEAD hashes equal the checker's recount (the in-zip member is the pinned blob); `scopes_diff` equals the recomputed row-key diff and `z09` is added; each `minimal_repin` entry's `new_sha256` equals the blob at its new pin and the member differs from HEAD; the checker extracts the live zip, re-runs the producer's own `firm_scope()` in the live tree and in the re-pinned tree in fresh processes and finds the recorded results: `blackdiamond_z09` refused then `cottonwood`, `schwab_08335338` and `orion` identical; no write is recorded. Base: FAIL (no record).

<criterion id="DBC118-2-AC1" cell_refs="DB-c-11"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r118/p118_bcw.py" . DBC118-2-AC1</invocation><expect>DBC118-2-AC1 PASS</expect></criterion>
`DBC118-2-AC1` -- the packet exists, is 5,000 characters or more, holds the eight headings in order, states it is unsigned and claims no signature, names each re-pinned member with the first ten characters of its new pin, the live zip version it starts from, the Cottonwood function and the catch-up. Base: FAIL (no packet).

<expected_criteria>DBC118-1-AC1, DBC118-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the source map, every Terraform file, the checkers and every contract: the edit is TEXT in the packet.
- **Reads and writes.** Reads: repo files; `git show`; ONE GET of the shared zip by the version id above (and the zip's version listing if you need it). Writes: the record and the packet in your folder and scratch in your private folder. No upload, no AWS write, no Terraform command, no invoke, no deploy, no push, no vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If `scopes.json` alone does not make `z09` resolve, say so and give the smallest set that does; if no set does, file a BLOCKING row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W406-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~406/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-11.shared-zip-registry-pin-read-and-addendum-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 5, cell `DB-c-11`.
<owned_cells>DB-c-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC118-1-AC1, DBC118-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~406/IRPT_DASHBD.TO-DB-c-11.shared-zip-registry-pin-read-and-addendum-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC118-1-AC1 DBC118-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the two criteria's last lines; the minimal re-pin (member, new pin, new sha256); the added scope keys; the per-channel results in both trees; the packet's length; row ids. No client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read record and a packet; nothing is wired, changed, uploaded or deleted. The later act's blast (one zip upload, a code update on three functions, then the catch-up) is bounded in the addendum for the CTO's half.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: one GET of the shared zip by version id under the existing read grant; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed; the Cottonwood schedule stays DISABLED.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; both criteria FAIL at base (no record, no packet) and DBC118-1-AC1 re-runs the producer's own derivation in extracted trees (its two arms were exercised by the issuer: live refused z09, scopes-only fixed resolved it).
</preflight>
