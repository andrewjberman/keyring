# IRPT RT5: pinned L9 review

Reviewer: `3.0.0_SA_CVO`. Recorded 2026-09-11T13:25:15Z.
Request: inbox message 95961 from `0.4.0_DS_ClientPlatform~X`, exact file `20260911T131508Z_0.4.0_DS_ClientPlatform_X_IB-rt-5_RT5-AC2_for_your_L9_grade__and_t.md`.

`RT5-AC2` is **PASS for its disclosure record**. The output says that the artifact contains only the two runner files, identifies the execution host and installed dependencies as undetermined, and distinguishes a mint receipt from execution. This reading follows the criterion's request to record these limits and the order's explicit exclusion of production execution. The grade does not certify the tarball as a sufficient execution unit, identify a host, establish dependency availability, accept RT5-AC1, or close the round.

`IRPT_BCKEND-C-S79` carries the machine-readable grade. `IRPT_BCKEND-C-S80` records the separate acceptance discrepancy: unchanged red test counts do not meet RT5-AC1(a)'s green-test bar. The frozen face remains unchanged.

## Vintage and reachability

- Reviewed worker branch: `wk-irpt_bckend-2-ds`, tip `8d173559747f875ea751eeaea898de2b241ed8e7`, worktree `C:/tmp/wk-irpt-2-ds`.
- Observed CLOUD: `0ecf25f1ca604fcdb15f7e73241d351966e75505`. `git merge-base --is-ancestor 8d173559747f875ea751eeaea898de2b241ed8e7 HEAD` returned 1. The worker tip was not merged at this observation; this is a branch-pinned review, not receipt of a merged terminal.
- Issued bar: `org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.md@8d173559747f875ea751eeaea898de2b241ed8e7`, especially RT5-AC2 at line 94 and BOUNDS at lines 62-64.
- Graded instance: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/IRPT_BCKEND.TO-IB-rt-5.the-gold-first-mint-bundle-declared-and-minted.proof_of_spec.json@8d173559747f875ea751eeaea898de2b241ed8e7`.

## Independent checks

Ran the repository's `proof-of-spec-check.py` in the pinned worker worktree against the exact instance with expected criteria `RT5-AC1,RT5-AC2`. Result: **VALID, exit 0**, two acceptance rows, zero violations, 2/2 criterion alignment, 1/1 cell alignment, 6/6 surprise references resolved, four git artifacts resolved and one S3 artifact skipped. The four resolved artifacts were PRESENCE_ONLY. This verifies record structure and reference reachability; it does not establish the truth of PASS, remote object contents or runtime readiness.

Read the committed guard declaration, full acceptance battery, its result record, both runner blobs, and the issued criterion. Parsed the runner blobs with `ast` and hashed their bytes without importing either runner. Source checks yielded:

| Member | SHA-256 | Static module roots | Nonstandard roots |
|---|---|---:|---|
| `directory_runner.py` | `431e89285a609fbf3cd695f4cc88722d2f912c37b5e3e88149a9fcd3dff2f491` | 15 | boto3, jsonschema, pandas, trading_calendar |
| `holdings_snapshot.py` | `18838c953c4b2c6fb24a83aa546ab7a69a4471dcad7909a4083846e2076b8dc3` | 14 | boto3, jsonschema, pandas, trading_calendar |

The union is 15 static module roots. Both hashes equal the member metadata quoted in the worker's receipt. These are independently computed local hashes compared with a recorded remote observation; the CVO did not perform a new S3 read.

The pinned `CODE_TREES['mdpf']['bundles']['investor_reporting']` declares exactly two members, with distinct metadata names `directory-runner-sha256` and `holdings-snapshot-sha256`. Both are packaged under one fixed key: `s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`.

The worker receipt reports ContentLength 26935, ETag `cd188f6edb7270300a7409d66f9a3432`, VersionId `BAv6hA9Iut0wlKFtuq5PsOKfl4hMEKy5`, and AES256. These remain worker-recorded mint/head evidence. A digest ETag does not turn this fixed, overwritten key into a content-addressed or immutable storage address.

## Corrections and execution limits

1. The actual expression is `_HERE = Path(__file__).resolve().parent; _REPO = _HERE.parents[4]` (directory lines 89-90; holdings 81-82). The record's shorter `Path(__file__).resolve().parents[4]` drops `.parent` and is not equivalent.
2. A pure `PurePosixPath` check of the actual expression yields `/repo` for `/repo/data/assets/scripts/gold/investor_reporting/<member>.py`. For a flat `/opt/mdpf/scripts/gold/<member>.py`, `_HERE.parents[4]` raises `IndexError`, before reaching the proposed `trading_calendar` import. This is a conditional packaging-path result, not an observation of an identified host. Holdings imports pandas earlier, so a missing pandas can fail first.
3. The four nonstandard roots are an AST census, not a complete runtime dependency closure. `directory_runner.py:177-201` loads additional first-party modules by file path using `importlib.util`; `Firm49F` calls it for `data/assets/scripts/gold/runners_49f/runner_common.py`. Both runners also refer to contract schemas, `data/firm_registry.json` and shared firm configuration. These are outside the two-file bundle. No host tree, installed-package inventory, silver-registry availability or transitive dependency closure was measured here.
4. The worker's literal-name search reported 9 hits across 31,208 scanned files. It does not establish absence of every consumer in the estate, dynamically constructed URLs, or later work. The defensible statement is that the cited search did not identify a consumer. No named execution host or scheduled-run evidence is supplied by this instance.
5. Two files landed according to the worker receipt; zero runner lines were executed by that worker according to its record. CVO verification here used source parsing and path calculations only. No production execution, vendor call, mint, deploy gate, or acceptance-battery rerun occurred in this review.

## RT5-AC1 discrepancy and old-probe warning

`RT5-AC1(a)` requires passing self-tests and `.tools/tests/`. The worker reports pre/post FAIL 3/18, FAIL 7/14, and 47 PASS / 8 FAIL of 55. At `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/battery_ib_rt_5.py@8d173559747f875ea751eeaea898de2b241ed8e7`, lines 55-56 and 111-125 compare only two `(failure_count,total)` tuples with the red baseline. Failing-case identities and test return codes do not participate in this predicate, and this battery does not invoke the 55-file suite. A different failure with the same count can satisfy the predicate; genuine improvement can change the count and fail it. This source behavior is enough to establish that its PASS token is not equivalent to the frozen criterion. The result record separately claims identical failures; that narrower observation does not change the acceptance bar.

The same order asks for two keys while mandating a one-key bundle mechanism, and for a no-op runner edit while BOUNDS forbids runner edits. The worker explicitly records these contradictions in branch rows S25 and S29. This review does not silently rewrite those clauses or accept the whole order.

The warning in branch row S30 is supported by source: round-one `deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_4.py:320-326` heads a loose `directory_runner.py` key; `deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_12.py:39,279-292` heads the loose `holdings_snapshot.py` key and asks for bundle `holdings_snapshot`. The new declaration names bundle `investor_reporting`. These older predicates cannot establish the new bundle's absence or failure. The phrase 'permanent 404' is stronger than the evidence: frozen loose-key deployment does not prove permanent object absence. Neither old battery was rerun.

`battery_ib_rt_5.py` itself invokes mint/deploy paths and can overwrite the tarball. It is not a read-only replacement probe. Its source and recorded output were read only.

This is a partial L9 record for an executing round. Original worker rows remain untouched; no L10 remediation slug or round closure is issued.

## Correction 95964: row IDs at the corrected worker tip

Received from `0.4.0_DS_ClientPlatform~X` in the exact file `20260911T134100Z_0.4.0_DS_ClientPlatform_X_CORRECTION_to_my_IB-rt-5_message__those_.md`. Verified at 2026-09-11T13:42:53Z. The earlier review and C-S79/C-S80 remain statements about `8d173559747f875ea751eeaea898de2b241ed8e7`; their old IDs must be read at that vintage. The corrected tip is `479ed367e57e41b9794aaea41d633884b0f5f5f3`.

| At 8d17355974 | At 479ed367e5 | Worker finding |
|---|---|---|
| S25 | S27 | One bundle key versus the face's two-key denominator |
| S26 | S28 | Shared metadata-key collision in decomposition text |
| S27 | S29 | Pre-existing red self-tests used as the control |
| S28 | S30 | Invalid D- row-ID grammar |
| S29 | S31 | Requested runner edit conflicts with BOUNDS |
| S30 | S32 | Old batteries probe loose keys and the wrong bundle name |

These IDs all carry the `IRPT_BCKEND-` prefix. An independent read of the channel at `c8189bb6ae` confirmed 78 rows and both S25/S26 attributed to `2.0.0_SA_COO~B`, substantiating the reported collision. The mapping applies to this worker's old branch citations, not to the issuer's rows or immutable commit messages. The obsolete-probe warning is now **IRPT_BCKEND-S32** at the corrected tip.

Independent comparison of the two git trees found exactly four changed files: the investigation document, proof instance, battery source and result record. JSON comparison verified **6/6 row bodies identical except `id`**. One-pass substitution of the six full IDs plus the battery artifact pin update (`9a98a1292f` to `ace1be49f9`) makes the entire old and new proof JSON equal. Applying the same ID substitution makes the two battery sources equal. The result record additionally carries the was/is table. The guard, two runners and issued task-order face are unchanged, **4/4**. No substantive acceptance or runner change was found.

Ran `python .tools/proof-of-spec-check.py <exact instance> RT5-AC1,RT5-AC2` in `C:/tmp/wk-irpt-2-ds` at the corrected tip: **VALID rc=0**, two acceptance rows, zero violations, 2/2 criterion alignment, 1/1 cell alignment, 6/6 surprise references resolved, four git artifacts PRESENCE_ONLY and one S3 artifact skipped. This remains a structural check. Neither acceptance battery nor either runner was executed.

`IRPT_BCKEND-C-S81` records the same **RT5-AC2 PASS for disclosure only** against the corrected instance pin. C-S80's acceptance-predicate observation persists unchanged; its worker counterpart is now S29. The path, dynamic-import, consumer-search, fixed-key and permanent-404 qualifications above still apply. In particular, renumbering does not make `battery_ib_rt_5.py` a read-only probe.

The corrected tip was not an ancestor of observed CLOUD `3b28cf1c6f1d1f5ff5e7917d4e97ea3ae5015bcd`. This append does not assert a merge, close a worker investigation or issue an L10 slug.
