# DEPLOY LEDGER -- mdpf-gold-lambda PACKAGE REBUILD: the KeyError tuple (A) + the category-views G2 entry (B)

**STATUS: OPEN** at 2026-08-28T21:01Z. Opened at start per CLAUDE.md NEVER#6 / NEVER#2.
Nothing has been applied. Nothing has been uploaded. **The only acts taken so far are READS and one
trial build written to the session scratchpad, outside the repo and outside S3.**

| field | value |
|---|---|
| opened | 2026-08-28T21:01Z |
| closed | -- |
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

## PLANNED SEQUENCE (none of it executed yet)

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

-- `0.7.0_AE_CloudOps~Z`
