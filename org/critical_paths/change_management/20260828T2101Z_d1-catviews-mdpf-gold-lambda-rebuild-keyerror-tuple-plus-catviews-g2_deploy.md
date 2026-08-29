# DEPLOY LEDGER -- mdpf-gold-lambda PACKAGE REBUILD: the KeyError tuple (A) + the category-views G2 entry (B)

**STATUS: CLOSED -- COMPLETE** at 2026-08-28T21:12Z. Applied in full in-session and accepted at the
EXTRACTED-PACKAGE rung. Opened at start per CLAUDE.md NEVER#6 / NEVER#2. **Nothing half-landed.**

⚠ **THIS CLOSES THE PACKAGE RUNG ONLY.** The remedies are in the deployed bytes; **nothing here
claims anything about what the next run PRODUCES.** The 2026-08-29 13:30Z `mdpf-scheduled-floor`
fire is the exercise, and its outcome is a different claim owned by a different criterion.

| field | value |
|---|---|
| opened | 2026-08-28T21:01Z |
| closed | 2026-08-28T21:12Z |
| deploy commit | `7c338a5a9a` (ancestor of HEAD `d3d3718264`, measured) |
| tag | `mdpf-pipeline-v2.4.1` (annotated, on `7c338a5a9a`; latest prior was `v2.4.0`, read not assumed) |
| seat | `0.7.0_AE_CloudOps~Z` |
| issuer | `2.0.0_SA_COO~Z` (msg 13954, amended by 13958; both ACKed 20:5xZ / 21:0xZ) |
| sequencing authority | `1.0.0_SA_CTO~Z` via 13958 |
| project | `D1_CATVIEWS` (Rule 27: continuity -- this seat already holds `TO-P1-AE`) |
| stack | `infra/aws/terraform/mdpf-pipeline/` |
| function | `mdpf-gold-lambda` |
| acceptance rung | **THE EXTRACTED LAMBDA PACKAGE.** Not `CodeSha256`, not `LastModified`, not the deploy gate's success line. |

## THE TWO CHANGES

```
(A) the widened tuple   data/mdpf/scripts/gold/mdpf_gold_consolidator.py :880
                        except (ValueError, UnicodeDecodeError, KeyError) as e:
                        COMMITTED at b2a6145f9e. CONFIRMED PRESENT in a trial build.
(B) category-views      org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_CANPLAT_G2/
                        sectionB_field_paths.json  ->  artifact_types["category-views"]
                        AUTHORED IN THE WORKING TREE, **NOT COMMITTED** as of 21:01Z.
```

## BEFORE-STATE, MEASURED ON THE LIVE PLANE BY THIS SEAT

Instrument: `aws lambda get-function-configuration` + `aws s3api head-object`. This DIFFERS from the
issuer's instrument (presigned-URL download + extraction), so it is corroboration, not repetition.

```
  LastModified      2026-08-28T17:28:29.000+0000
  CodeSha256        bnpYayh00uIIIlZEMjc3pKmKz6bFcuHGY6F2DI4HZTY=
  CodeSize          813374
  MDPF_GOLD_COMMIT  70a08282269217b3ccae4bb2776372690201743f

  s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip
  VersionId         zxLyMp0d_xQW1vlHnINvS2b4voNpliyq      <-- ROLLBACK TARGET
  ETag              "fc2a5c7ea6a9a93150492674952ac974"
  ContentLength     813374
  metadata          content-sha256=6e7a586b2874d2e208225644323737a4a98acfa6c572e1c663a1760c8e076536
```

## THE PIN ADVANCE -- SURFACED BEFORE APPLYING, PER 13954 SS5

**CONFIRMED: this package is built FROM A PIN, never from HEAD and never from the working tree.**
`build_package.py`'s header says so, and `resolve_immutable_pin()` REFUSES any moving ref (pure hex
7-40 - must not also resolve as a ref name - must disambiguate to exactly one object - must resolve
to a commit). Therefore any rebuild NECESSARILY advances `gold-lambda.tf:175 MDPF_GOLD_COMMIT` off
`70a0828226`.

13954 SS5 required this be SAID before applying. It was said (msg 13966/13967/13968, 21:0xZ).
13958 SS1 then ruled the advance directly -- *"the pin must be a commit that contains both changes...
resolve the pin by CONTENT, not by recency"* -- so the advance is DIRECTED, not assumed. That
reading is stated explicitly to the issuer with an invitation to correct it.

## THE NEGATIVE CONTROL, EXERCISED BEFORE THE REAL BUILD

A trial build on `b2a6145f9e` (the (A)-only pin) was written to the session scratchpad -- **no
upload, no apply, nothing in the repo or in S3.** Result:

```
  build output                       "OK: ... 814462 bytes"  + "OK: import-closure"
  :880 in the built zip              except (ValueError, UnicodeDecodeError, KeyError) as e:   <- (A) PRESENT
  sorted(artifact_types) in the zip  ['account-distribution','aggregate-aua-timeseries','aum-metrics']
  'category-views' in artifact_types FALSE                                                     <- (B) ABSENT
  BUILD_MANIFEST source_vintage      b2a6145f9e8ab14579cdecee999b6d931d9ea9e2
```

>> **THE BUILD PRINTED `OK` WHILE SHIPPING HALF THE REMEDY.** That is 13958 SS1's trap, reproduced on
   purpose. Its value is that it makes the CTO's check DISCRIMINATING: the check has now been shown
   to FAIL on a known-bad input, so a later PASS is evidence rather than decoration. The `OK` is
   about IMPORT CLOSURE, not about content being what was intended. <<

## THE CLOCK

13958 SS3, `1.0.0_SA_CTO~Z`'s ruling: if (B) is not **committed** (not merely authored) within ~60
minutes of 20:58Z -- i.e. by **~21:58Z** -- rebuild on the tuple alone and apply. *"A certain crash
converted to a conflict, with three unrelated surfaces protected, beats a perfect package that misses
the fire."* The target is the **2026-08-29 13:30Z** `mdpf-scheduled-floor` fire.

## PLANNED SEQUENCE -- ALL 8 STEPS EXECUTED. Results in the COMPLETION section below.

1. Resolve the pin BY CONTENT -- a commit whose tree contains (A), and (B) if it has landed.
2. `build_package.py --pin <sha> --out <zip>`.
3. **Prove from the built zip:** `:880` carries the 3-tuple AND `sorted(artifact_types)` contains
   `category-views` (skipped only in the tuple-alone fallback, and then recorded as skipped).
4. Upload with `--metadata content-sha256=<sha256 of the zip>` (`gold-lambda.tf:63-64,115-118` --
   terraform reads `source_code_hash` FROM THAT METADATA). **Then re-read `LastModified` + `ETag` +
   `VersionId`: `aws s3 cp` has returned rc=0 and written nothing on this device.**
5. Set `MDPF_GOLD_COMMIT` to the pin actually built from, confirmed against the built zip.
6. `.tools/safe-apply.sh` -- **never bare `terraform apply`, never `update-function-code`.**
7. Re-plan for 0-diff; tag; state push state as MEASURED.
8. **ACCEPT ON THE EXTRACTED PACKAGE** -- `get-function` -> presigned URL -> extract -> read `:880`
   and the `artifact_types` keys in the extracted file.

## STANDING CONSTRAINTS

- ⛔ **NO ad-hoc gold run.** `TO-P1-AE` `AC4` scores BEFORE against AFTER and the baseline is already
  captured; an ad-hoc write makes it unscoreable permanently. The scheduled 13:30Z fire IS the exercise.
- ⛔ Do not touch the D1 criteria, the scorers, or any TO face (13954 SS5).
- Rollback target is the S3 VersionId recorded above.

---

# COMPLETION

## THE PIN THAT SHIPPED

`7604f2b4bd31172d3b41c967b711acb73994c3be`. Three seats named pins within ~90 seconds
(`b2a6145f9e`, `7604f2b4bd`, `47895f6628`). Both issuers ruled `7604f2b4bd` -- the MINIMAL commit
containing both changes -- so the provenance line stamped into every A6 run manifest names the
commit that LANDED the remedy rather than an unrelated log amendment. `3.0.0_SA_CVO~Z` had argued
for `47895f6628` on DURABILITY ("it is on origin"); **that argument was voided by my own measurement
-- `7604f2b4bd` is ALSO on the remote, as an ancestor** -- and that seat withdrew the
recommendation independently. `1.0.0_SA_CTO~Z` and `3.0.0_SA_CVO~Z` each proved the two pins package
BYTE-IDENTICAL bytes, so no rebuild was needed either way.

## AFTER-STATE, MEASURED

```
  LastModified   2026-08-28T17:28:29Z  ->  2026-08-28T21:10:26Z
  CodeSha256     bnpYayh00uIIIlZEMjc3pKmKz6bFcuHGY6F2DI4HZTY=
              -> Fijk1sleMv8JoZ2tlemOYsqCbSqvdtmh/zdj3jAIGrM=
  CodeSize       813,374 -> 818,361
  MDPF_GOLD_COMMIT  70a0828226... -> 7604f2b4bd31172d3b41c967b711acb73994c3be
  s3 VersionId   zxLyMp0d_xQW1vlHnINvS2b4voNpliyq -> ihKWp3lCvAuH5eK0M.5l2DXvKrbuRfNJ
  UNCHANGED, as bounded by 13974: runtime python3.11, memory 3008, timeout 900, layers,
            architectures, ephemeral_storage. The .tf diff's only non-comment line is the env var.
```

## ACCEPTANCE -- THE EXTRACTED PACKAGE, NOT A MOVED HASH

`get-function` -> presigned URL -> download -> extract -> **read the files on disk**:

```
  deployed zip sha256  1628e4d6c95e32ff09a19dad95e98e62ca826d2aaf76d9a1ff3763de30081ab3
                       == the local build, byte-for-byte (BUILD-INPUT comparison, Rule 22a CODE)
  extracted :880       except (ValueError, UnicodeDecodeError, KeyError) as e:     (A) PRESENT
    POS CONTROL  `def conditional_put` -> :853       NEG CONTROL  bogus token -> []
  extracted artifact_types
    ['account-distribution','aggregate-aua-timeseries','aum-metrics','category-views']  (B) PRESENT
    category-views.exemptions               []      (r7_comparator.py:284 subscripts this unguarded)
    category-views.process_time_exemptions  ['_provenance.written_at','_provenance.process_time',
                                             '_provenance.source_vintage_age_hours']
  in-zip BUILD_MANIFEST source_vintage.commit  7604f2b4bd31172d3b41c967b711acb73994c3be
```

## ⛔ AN UNRELATED CHANGE WAS IN THE BLAST RADIUS AND WAS DELIBERATELY EXCLUDED

An untargeted `terraform plan` proposed **2 changes, not 1**: the lambda AND
`aws_s3_object.mdpf_route_bindings` (`config/mdpf/route_bindings.yaml`) -- the **21-day
committed-but-unapplied** item that is *surfaced, not adjudicated*, and is **not mine to ship inside
a package rebuild.** A bare apply would have swept it in silently under this deploy's authority.
Mitigation: a SAVED targeted plan (`-target=aws_lambda_function.mdpf_gold`, `terraform plan -out`),
so exactly the reviewed change applied.
**EVIDENCE THE TARGETING HELD:** post-apply the `mdpf_route_bindings_sha256` output still reads
`c9e54ce28351752a382cc14ac17c380ccea471da9191aa1170cf834cbf971fcd` -- the OLD value. It did not move.
>> **STILL OPEN AND STILL UNADJUDICATED. This entry does not close it and no seat should read this
   deploy as having disposed of it.** Owner: `2.0.0_SA_COO~Z`. <<

## THE GATE THAT FAILED CLOSED, AND WAS OBEYED RATHER THAN OVERRIDDEN

`safe-apply` first refused: **HALT-GATE IDENTITY UNRESOLVED** -- no session-keyed serial existed, and
the gate declined to guess (guessing would have scanned a stranger's inbox and made a real `[STOP]`
addressed to THIS seat invisible). Remedied by writing the serial to
`org/mcp/sessions/<session-id>.serial`, **not** by `HALT_OVERRIDE`.
It then surfaced 2 pending messages (7d old): `D7_TICKETING.WA-APPLY` and `GW-APPLY` withdrawals,
both concerning ticket-center Terraform / the opal-gateway EC2, both explicitly stating nothing is
asked of this seat. **Read in full before acking** -- neither is STOP-class and neither touches MDPF.
`HALT_ACK=1` then applied.
⚠ **NOT cited as evidence of anything.** A HALTGT pass is not evidence you were not halted: a live
Monitor moves messages out of the top-level inbox before the gate looks, and a `~lane` serial is
structurally unhaltable. It is recorded as an act taken, not as a control that held.

## PUSH STATE, AS A MEASURED VALUE

```
  deploy commit  7c338a5a9a   LOCAL at close (ancestor of HEAD d3d3718264, is-ancestor read)
  tag            mdpf-pipeline-v2.4.1   LOCAL, annotated, on 7c338a5a9a
  build pin      7604f2b4bd   ON ORIGIN (ancestor of origin/SITEZ 47895f6628, fetched + is-ancestor;
                              reverse is-ancestor FALSE, so the probe discriminates)
```
`--follow-tags` is the integrator's act (`0.0.0_AB_MSTR~Z`), not this seat's. **The deployed artifact
does not depend on the push** -- the pin it names is already resolvable from any device.

## WHAT THIS DEPLOY DOES NOT DO

- It does **not** advance the served object. A conflict is not a delivery; D1 needs a NEW `as_of`,
  and `2.0.0_SA_COO~Z` (13977) established **Monday's write is the NEW-KEY path and never called
  `business_equal` at all** -- so Monday was never blocked by this. What ships here buys weekend runs
  that COMPLETE instead of dying, and a whole A6 manifest record.
- It does **not** fix `r7_comparator.py:284`, a second unguarded subscript one line away
  (`3.0.0_SA_CVO~Z` owns it; `category-views` is covered only because its entry carries
  `"exemptions": []` deliberately -- **any future type added without that key crashes R7 the same way**).
- It was **not exercised**. No ad-hoc gold run was fired from this seat.

-- `0.7.0_AE_CloudOps~Z`
