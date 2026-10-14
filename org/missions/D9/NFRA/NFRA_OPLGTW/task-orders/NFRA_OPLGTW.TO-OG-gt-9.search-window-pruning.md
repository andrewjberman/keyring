# NFRA_OPLGTW task order -- `OG-gt-9` -- harvest_search_articles reads only what the asked window needs, so it answers inside the 60 s ALB timeout

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-9</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-9</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~88</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; nothing is deployed here.
comp-iam: RUN-BY-ISSUER at the cut: the code's AWS calls are s3:GetObject and s3:ListBucket on opal-data-harvest, read through OG-hv-2's grant; this cell adds no AWS call kind and changes no IAM. Live probes use the box's own credentials, read only.
comp-adversary: DECLARED-NOT-APPLICABLE -- CTO ruling (msg 34205): article search must ship usable; CVO condition on the 60 s ALB idle timeout (halves of OG-ap-18).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gt-9` (decomposition addendum R3-T.53, workstream G1-FIX, FWD-22)

All paths relative to the repo root; the gateway is `infra/aws/ec2/opal-gateway` (`GW`). The module is `GW/app/harvest_press.py`, tool `harvest_search_articles`
(around lines 239-345 on your HEAD).

**The defect, measured by the issuer on the real bucket (ASML, read only).** With no window and `limit=5` the tool takes 43-47 s; the denominator reads
`silver_parts_read: 849`. With the 7 days ending at the newest article it takes about 16 s. The ALB in front of the gateway cuts a call at 60 s, so a
slower call shows the user a 504. The earlier CTO reading was that the gold `article_sentiment` join scans one ~110 MB partition; the numbers above say the
silver join may cost as much. **Profile first, then fix what dominates**, within this one module.

**What to build.**

1. **Profile the two calls** (no window / 7-day window) on the real bucket with the box's credentials: seconds and bytes spent in (a) listing and reading the
   mention-row part(s), (b) the gold `article_sentiment` read, (c) the silver join. Put the three numbers per call in your report.
2. **Prune the sentiment read by partition date.** A sentiment row cannot predate the fetch of its article: read only `article_sentiment` partitions dated on or after the
   earliest `fetched_at` UTC day among the page's rows. **Measure that premise on the real bucket before relying on it:** for the page's article keys, count
   sentiment rows found in partitions dated BEFORE the key's `fetched_at` day (violations; want 0 for the sample) and print the count. If violations are non-zero, widen the cut
   by the measured slack and say so in the envelope's `absent_reason`/notes, never silently.
3. **Reduce whatever else dominates the profile** by reading less, not by caching across calls (no module-level cache, no store write): read only the silver partitions of the
   page's own articles (the page is already limited before the join), and read the mention-row part only once. Keep the answer's content identical for the same inputs.
4. **State the pruning in the denominator**: add `sentiment_partitions_read` and `sentiment_partitions_total` (integers) to the existing `denominator` dict, keeping every
   existing key and the envelope fields (`as_of`, `source_keys`, `denominator`, `absent_reason`).
5. **Tests `GW/tests/test_og_gt9.py`**, offline (a recording fake client, no network), named exactly: `test_oggt9_ac01` (partitions dated before the cut are not read: the fake client's read log proves it),
   `test_oggt9_ac02` (difference control: a synthetic dataset in which every sentiment row is scored on or after its fetch gives the SAME articles and sentiment fields pruned and unpruned; a decoy row in a partition older than the cut is never returned),
   `test_oggt9_ac03` (the denominator carries `sentiment_partitions_read` of `sentiment_partitions_total`).

## 2. BOUNDS

- Code and tests only. No release, no deploy, no IAM or Terraform, no bucket write, no module-level cache.
- Edit only `harvest_press.py` and the new test file. The 50 KB projection, the 64 MiB read cap, the admission (`admit_typed` first) and every other tool in the module are unchanged.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name, a full email address or an article's text body into a report, a row or a log; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/harvest_press.py
infra/aws/ec2/opal-gateway/tests/test_og_gt9.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~88/`. Rows: id `NFRA_OPLGTW-Z-W88-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-9"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt9.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-9"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt9.AC2.sh; echo "exit=$?"</invocation><expect>(?s)search ASML: no window [1-5] article\(s\) in \d+\.\d s \(want . 40\); 7d ending at the newest .* in \d+\.\d s \(want . 40\); denominator names partitions read True; envelope whole True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the offline pruning, difference-control and denominator tests pass. `AC2`: on the real bucket both calls answer under 40 s and the denominator names the partitions.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-9.search-window-pruning.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once.
Your report carries the profile numbers, the premise's violation count, and the before and after seconds of both calls.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G1-FIX (addendum R3-T.53). CTO msg 34205 (Friday work, ships usable); CVO condition 60 s ALB. Base probe (issuer, ASML): no window 43.3 s, windowed 16.6 s, `silver_parts_read` 849.
- Pre-cut: gt9.AC1 base FAIL (file absent), gt9.AC2 base FAIL (43.3 s, no partitions in the denominator).
- Gateway app files are in lane CLOUD_OPS_OR_ETL: a worker order grants them.

<status>pending</status>
<round>37</round>
<workstream>G1-FIX</workstream>
<slot>~88</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
