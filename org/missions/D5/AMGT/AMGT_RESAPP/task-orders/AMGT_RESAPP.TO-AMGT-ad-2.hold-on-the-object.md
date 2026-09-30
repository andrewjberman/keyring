# AMGT_RESAPP task order -- `AMGT-ad-2` -- THE HOLD ON THE OBJECT: MOVE THE NO-SPAN SENTENCES OF THE 12 STORED D-1 DOCUMENTS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ad-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: RUN by the issuer at the cut -- the same executor identity wrote the same prefix through the same writer live at ab-6 (drafting/v1/ASML_NA_Equity.json, VersionId qHYfgew8, 11:49Z via analyze.write_outputs drafting_only); no policy simulation was run, and the 12 PutObject calls add no action or prefix beyond that write.
comp-adversary: RUN by the issuer at the cut -- AC1 (store) and AC2 (served) FAIL at the base with and without a pre-act capture; both PASSED on simulated correct post-states (the reference transform on the saved objects; the adapter's accounting per scoped_amgt.py:1877-1884 on the saved bodies).
EGRESS CLASS, declared: NONE. Opal's own S3 and Lambda.
</preflight>

## 1. THE ACT -- `AMGT-ad-2` (round 54, decomposition s.62)

ONE act, ONE NEVER-2 entry, ONE never-widen pair: run AMGT-ad-1's `python -m lib.research.filings.drafting_build --hold-unspanned
--population <the newest crosswalk/v1 key> --pre-act-dir <your deliverables>/ad2-pre-bytes` LIVE, which moves every stored D-1 document's
no-span sentences (the census `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~193/D1_UNSPANNED_CENSUS.json`, 179 in
12 documents at the cut) from `sections[].sentences` to the object's `held_no_span`. The page's sentence text does not move: the deployed
adapter already holds these at read, and after the act it reads the same hold from the object. ONE reader takes the stored text without that
hold -- the posture judgment's evidence pack (`lib/research/posture/packs.py:110`) -- and it loses exactly these sentences (AC3).

**Begin only when all hold:** AMGT-ad-1 has drained; the issuer's GO names the commit to run from; both halves are committed (their paths
are in the GO); a `--dry-run` at that commit lists exactly the census's names and counts. **The order of work, under the entry opened AND
COMMITTED first:** (1) `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round54/checks/ad_2_hold.py --what save --dir org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ad2-pre`;
(2) the dry-run; (3) the live run; (4) AC1 and AC2; close the entry. A criterion failing after the act is the ROLLBACK trigger: re-put
each key's pre-act bytes from `ad2-pre-bytes` (the halves name it).

## 2. BOUNDS

1. The act and nothing else: the 12 `drafting/v1/*.json` objects through the producer's writer. No other prefix, no delete, no deploy.
   A dry-run that names a key or a count beyond the census, or a validator refusal, is a REFUSAL.
2. Standing: no S3 delete, no vendor call, no model call, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ad-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round54/checks/ad_2_hold.py --what store --dir org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ad2-pre; echo "exit=$?"</invocation><expect>12 documents, no-span left 0 each, no BAD line; EVERY STORED D-1 DOCUMENT HOLDS ITS NO-SPAN SENTENCES AND MOVES NOTHING ELSE: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ad-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round54/checks/ad_2_hold.py --what served --dir org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ad2-pre; echo "exit=$?"</invocation><expect>per name at_read -> 0, on_object = the pre-act at_read, count unchanged, no BAD line; THE SERVED /THESIS TEXT IS UNMOVED AND READS THE HOLD FROM THE OBJECT: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ad-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round54/checks/ad_2_packs.py --dir org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ad2-pre; echo "exit=$?"</invocation><expect>per name removed = want, no BAD line; pack sentences removed equals the pre-act no-span count; THE POSTURE PACK LOSES EXACTLY THE NO-SPAN SENTENCES: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ad-2.hold-on-the-object.proof_of_spec.json`. Report once: the 12 write receipts, the prior and new VersionIds, the verdict counts, the commit hashes, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-53 analysis item 2. Measured at the cut (s.62b.2): the served page already shows none of the 179 (the adapter
holds at read), so the served delta is the hold's accounting only; asked of the CTO whether the pair still earns its cost -- the GO
waits on that answer, on ad-1's drain and on both halves. Base: AC1 FAIL, AC2 FAIL (no capture; with a capture and no act: 179 left /
at_read not 0). Positive arms (ruling 1): AC1 PASS on the reference transform applied to the saved objects; AC2 PASS on the saved bodies
with the adapter's accounting applied.

<status>pending</status>
**AMENDMENT 1 (`2.0.0_SA_COO~Z`, 2026-09-30 ~18:0xZ, before any GO; graded by `.tools/to-pipeline-gate.py` GATE (viii) only -- the order
declares `<placeholders>`):** per CTO msg 27301 the reader census decides ad-2 (s.62b.2a): one reader takes the stored text without the
at-read hold (`lib/research/posture/packs.py:110`, the posture judgment's evidence pack), so ad-2 STANDS and AC3 grades that reader's
output (`ad_2_packs.py`: base with a capture and no act FAIL, reference transform PASS, a span-carrying sentence also dropped FAIL). The
face's line "The page's sentence text does not move" stays true of the page; the posture pack is the moving reader.
**AMENDMENT 2 (`2.0.0_SA_COO~Z`, 2026-09-30 ~19:5xZ, during the act, before the executor's verdict; graded by `.tools/to-pipeline-gate.py` GATE (viii) only):** AC2's "every other key unmoved" compared nested read-time stamps: on the served plane after the act, VLO's only difference was `model.generated_at` 19:37Z -> 19:53Z (a read-time stamp; VLO's newest model block is 09:40Z, unchanged). The issuer's instrument defect, the same class as Z-S311 / Z-S318: `ad_2_hold.py` now drops the read-time stamps at every depth. Issuer read on the served plane: AC1 YES (179 moved, 12 documents), AC2 YES under AMENDMENT 2 (12 of 12: at_read -> 0, on_object = the count, count unchanged), AC3 YES (pack removed 179 = 179). Negative arm: a nested non-volatile plant under `model` FAILS AC2. A failing AC2 before this amendment is NOT a rollback trigger: no data moved.
<round>54</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
