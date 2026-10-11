# ADVI_FIRMBKTS task order -- `FB-f-1` -- THE F7 COMPARE INSTRUMENT: DESTINATION VS MANIFEST APART FROM SOURCE DRIFT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~11</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the issuer -- the identity (user/cloudops-dell1-agent-user) lists object versions and reads an object version on opal-data-bd and lists opal-data-49financial: measured by the issuer's reference build, live, 05:5xZ. No grant is created.
comp-adversary: RUN by the issuer -- r3_f7_ctl.py live 0 of 3 and mutant 0 of 2 at base (the instrument is absent); a reference build reads 3 of 3 and 2 of 2; blindness: the lens cannot see the producers' next write window, so the live arm asserts the SOURCE line is its own line and names a changed count, never a particular count.
EGRESS CLASS, declared: NONE (S3 reads inside the account).
</preflight>

## 1. THE CELL -- `FB-f-1` (round 3, enrichment item 2; row D1-C-S7; PRD F7)

`r2_f7.py compare` decides equality of a destination object and the manifest when their ETag forms differ (a multipart
key) by hashing the CURRENT source object. A producer rewrote the source key, so source drift read as a wrong
destination and the CVO's 05:18Z read said COPY-NOT-COMPLETE on a destination that was byte-equal to the manifest's
version. You build the corrected instrument. This is a new file; you never edit `r2_f7.py`.

1. Copy `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f7.py` to
   `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7.py` (your only write besides the
   proof instance). Change ONLY these two things, and the docstring's first line to name round 3 and row D1-C-S7:
2. **Hash the manifest's source version.** `opal-data-bd` is versioned. Add a function that, for a source key and the
   manifest's ETag, pages `list_object_versions(Bucket, Prefix=key)` (follow `KeyMarker` and `VersionIdMarker` while
   `IsTruncated`), takes the first version whose `Key` equals the key and whose `ETag` (quotes stripped) equals the
   manifest's ETag, reads that version with `get_object(..., VersionId=...)` and returns its sha256 in 1 MiB chunks; it
   returns `None` if no such version exists. In `cmd_compare`, where the code hashes the source, call it instead of
   hashing the current object.
3. **Print the two comparisons apart.** After the existing `COMPARE`, `DEST` and `SOURCE` lines, and before the verdict,
   print exactly two lines, each starting at column 0:
   - `DEST-VS-MANIFEST: EQUAL` when no manifest object is refused, missing or mismatched and there are no extras under the
     destination root, otherwise `DEST-VS-MANIFEST: DIFFERENT`;
   - `SOURCE-VS-MANIFEST: UNCHANGED changed=0 gone=0` when no source key changed or is gone since the manifest,
     otherwise `SOURCE-VS-MANIFEST: DRIFTED changed=<n> gone=<n>`.
   The verdict line stays: `COPY-COMPLETE: every manifest key present and equal` when the destination is EQUAL (source
   drift does NOT change the verdict), else `COPY-NOT-COMPLETE`; the exit code is 0 only for COPY-COMPLETE.

## 2. BOUNDS

1. Read-only: no write, delete or configuration change on any bucket. The instrument's `copy` subcommand stays as it
   is and you do not run it.
2. The manifest is `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~8/F7_MANIFEST.tsv.gz` (52,910
   objects, never edited). Keys carry client ids: your report names counts, never an id.
3. Only the files in section 3 change. No non-ASCII; LF line endings. If something cannot be met within your paths,
   file a surprise row and stop.
4. Every shell call starts in the BASE checkout. Begin each Bash call with `cd /c/dev/wk-firmbkts-11 &&`; the criteria
   below do.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7.py
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: `r2_f7.py` and `r3_f7_ctl.py` (the issuer's driver, same folder), the manifest above, `lib/opal_naming.py`,
`deliverables/mapping.json`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~11/ADVI_FIRMBKTS.TO-FB-f-1.compare-instrument.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-1"><invocation>cd /c/dev/wk-firmbkts-11 &amp;&amp; timeout 115 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7_ctl.py --arms live --root /c/dev/wk-firmbkts-11; echo "exit=$?"</invocation><expect>ROUND 3 F7 COMPARE LIVE: 3 of 3 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-1"><invocation>cd /c/dev/wk-firmbkts-11 &amp;&amp; timeout 115 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7_ctl.py --arms mutant --root /c/dev/wk-firmbkts-11; echo "exit=$?"</invocation><expect>ROUND 3 F7 COMPARE MUTANT: 2 of 2 arms</expect></criterion>
</proof_of_spec>

AC1 is the seam against the real neighbours (the live source and destination buckets); AC2 is the difference control (one
altered ETag in a copy of the manifest must read DIFFERENT and COPY-NOT-COMPLETE). Each invocation lists and hashes
inside the bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-f-1.compare-instrument.proof_of_spec.json` where `D` is
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~11`. **Flip this order's `<status>` to `complete` in the
SAME commit as your proof instance and `r3_f7.py`**, only when AC1 and AC2 pass. A row id on this project carries the dell1
infix and your slot: `ADVI_FIRMBKTS-D1-W11-S<k>`, with `surfaced_at` from `date -u +%FT%TZ`. Report once: the output lines of
AC1 and AC2 (the `DEST`, `SOURCE`, `DEST-VS-MANIFEST` and `SOURCE-VS-MANIFEST` lines in full), and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** direct act (`<direct_act>true</direct_act>`): one cell, about 40 changed lines, LOCAL. The instrument
is the CVO's remedy for row D1-C-S7 and a prerequisite of act 3 (`FB-f-10`). The reference build the issuer used to prove
the checks is not committed; the worker's build is the instrument of record. The cell closes D1-C-S7 when its compare is
the one the delta copy reports with (`FB-f-10`).

<status>complete</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-1</to_id>
<slot>~11</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
