# AMGT_HARVST task order -- `HVST-aa-2` -- ROUND 28 chain 2: A FRESH-DAY SPAN-BEARING LENOVO bbg/wsj RUN ON `aa-1`'s CODE, ITS UPLOAD, AND THE DAILY REBUILD THAT READS IT AND SERVES `publishers_found_codes` (FWD-7, FWD-3, FWD-5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aa-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~77</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the collector task is Disabled; ONE manual collection, its upload, ONE gold build. It enables nothing.
comp-iam: RUN at L5 -- vendor egress to bbg and wsj by the collector script only (R-21 @b390c36444); S3 PUTs: ONE persisted run record, the upload's bbg/wsj bronze and silver, ONE chatter_daily part. NO DELETE, NO ft/barrons/sa call, NO deploy.
comp-adversary: RUN at L5 -- the adversary is the q-1 shape again: coverage credited that listing hits alone produce, or a job whose only live request is a held key. AC2 reads Lenovo's coverage from the persisted run record ALONE, and the run record names every held key.
</preflight>

## 0. BEGIN ONLY WHEN ALL FOUR HOLD

1. `HVST-aa-1` is `complete` and merged on CLOUD. The dispatch names its merge.
2. BOTH never-widen halves are COMMITTED and named in the dispatch:
   - the COO half, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round28/NEVER_WIDEN_HALF_COO_AA2.md`;
   - `1.0.0_SA_CTO~Z`'s half.

   **Act only inside them.**
3. It is a UTC day with no same-day cached Lenovo listing pages. The halves name the act's date.
4. The issuer's checks exist at `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round28/checks/`, and the
   act-start gate there prints OK.

## 1. THE ACT (each command that reaches a put, named per the round-25 ruling 1)

1. **Plan, printed first:** `python -m lib.opal_data_harvest plan --security-json <Lenovo> --publishers bbg wsj --floor 2026-01-01 --with-watermark`.
2. **Collection, ONCE:** `run --harvest-grammar --retrieval-mode backfill --floor 2026-01-01 --new-only --security-json <Lenovo> --publishers bbg wsj --max-jobs 2 --runtime-root <main>`.
   It makes 1 S3 put, the persisted run record.
3. **Upload, ONCE:** `upload-harvest --max-objects 60 --retrieval-mode backfill --runtime-root <main>`.
4. **Run AC1.**
5. **Daily rebuild, ONCE:** `build-daily --securities-json <universe> --as-of <act date>`. It makes 1 put, and serves
   `publishers_found_codes` (`q-5`).
6. **Run AC2**, plus one served `/timeline` read for 992_HK.

The exact paths, the Lenovo security file and the universe are named in the halves. A refusal is Branch B, recorded and not
retried. Rollback is forward only.

## 2. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~77/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aa-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round28/checks/aa-2.AC1.py</invocation><expect>AC1 RESULT: PASS</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-aa-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round28/checks/aa-2.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round27.md` s.4 item 2: `p-3(b)` re-cut, on `aa-1`'s code.
- **The checks and COO half are issuer-written after `aa-1` merges** (the `o-5` / `p-5` pattern). Round-26 `p-5.*` checks are
  the template, extended with the `from_cache` / held-key reads and the `publishers_found_codes` served read.
- **The fresh day:** today (09-30) carries cached Lenovo listings, so the act runs on 2026-10-01 UTC or later.

**AMENDMENT 1 (issuer, 2026-09-30 ~12:0xZ):**
- **Timing and arm:** per the CTO ruling @`cb107ff848`, this runs TODAY after `aa-3`, as the CACHED-PATH arm. Section 0's
  item 3 (a fresh UTC day) is lifted.
- **wsj ONLY:** bbg is excluded, and its root joins the no-write set.
  - `aa-1`'s hold table is populated only by rejections made under the new code, and `NM5NLQ6K50XZ01`'s rejection predates it.
  - A bbg job would therefore re-fetch that key into the 403 and the challenge, which is `q-1`'s failure.
- **The act:** `--publishers wsj --max-jobs 1`, exactly as in the COO half `round28/NEVER_WIDEN_HALF_COO_AA2.md`.
- **The checks:** `aa2_common.WRITE = ("wsj",)`. AC1 requires that `NM5NLQ6K50XZ01` is not fetched.
- **Gate limb:** `to-pipeline-gate` grades a modified order's `<placeholders>` only (NONE).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>28</round>
<slot>~77</slot>
<fabric>site-z</fabric>
