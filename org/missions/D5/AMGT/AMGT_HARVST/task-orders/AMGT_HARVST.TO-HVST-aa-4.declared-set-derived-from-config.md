# AMGT_HARVST task order -- `HVST-aa-4` -- ROUND 28 chain 4: THE DECLARED PUBLISHER SET IS DERIVED -- `ENABLED_PUBLISHERS` minus universe-wide refusals read from the run records -- never typed (FWD-7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aa-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~79</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- amgt-resapp-chatter-axis reads CHATTER_AXIS_SOURCE=legacy; this cell changes the gold branch's code only and deploys nothing.
comp-iam: RUN at L5 -- in-memory runs over fixtures and read-only gold reads. NO PUT, NO env change, NO deploy.
comp-adversary: RUN at L5 -- the adversary is a set that follows per-name observation (sa in because it covered one name) or that keeps a publisher refused universe-wide. AC1 plants both.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO ENV CHANGE, NO DEPLOY, NO S3 WRITE.**
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~79/scripts/`; outputs named `aa4_*`.
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~79/AMGT_HARVST.TO-HVST-aa-4.declared-set-derived-from-config.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-aa-4.declared-set-derived-from-config`.

<paths>
lib/research/metrics/chatter_axis.py
lib/research/metrics/tests/test_aa4_declared_set_derived.py
lib/research/metrics/tests/test_q4_rank_declared_set.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~79/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULING (`ROUND_ANALYSIS.round27.md` ruling 1; PRD v0.5 `C-HV-RANK-DECLARED-SET`)

- **The declared set** is every publisher in `ENABLED_PUBLISHERS` (`lib/research/harvest/publication_gold.py` ~:375), minus any
  publisher whose collection REFUSED for the whole universe in the window. A refusal is read from the persisted run records
  (`publication_gold._iter_run_records`).
- A per-name trial neither adds a publisher nor keeps one out. For example, sa covering one name adds nothing: sa is in the
  set if and only if it is enabled and was not refused universe-wide.
- **Today the code types it:** `chatter_axis.py` ~:450 `DEFAULT_DECLARED_PUBLISHERS = ("bbg", "wsj")`. Replace that with the
  derivation.
- The printed population names the set and the publishers removed, with their reason.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aa-4"><invocation>python -m pytest lib/research/metrics/tests/test_aa4_declared_set_derived.py -rA --tb=line</invocation><expect>passed</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-aa-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~79/scripts/aa4_ac2_declared_set_today.py</invocation><expect>DECLARED SET:</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-aa-4"><invocation>python -m pytest lib/research/metrics/tests/ -rA --tb=line</invocation><expect>passed</expect></criterion>
</proof_of_spec>

**What each criterion must prove or print:**
- **AC1:**
  - (a) a planted run record with an ft universe-wide refusal takes ft out of the set;
  - (b) sa enabled and not refused is in the set;
  - (c) a per-name coverage of a non-enabled code does not add it;
  - (d) no typed tuple remains: a mutant restoring the typed default fails.
- **AC2:** over the real persisted run records and `ENABLED_PUBLISHERS`, print `DECLARED SET: [...]`, the removed publishers
  with their reasons, and the in-memory gold branch's POPULATION under it (no write).
- **AC3:** the base is commit `699fb78c93`, pinned. Print the base and after pass counts. No test that passed at the base
  fails.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** `ROUND_ANALYSIS.round27.md` s.4 item 4. Eligibility stays 0 either way; adding a publisher only tightens it.

**AMENDMENT 1 (issuer, 2026-09-30 ~10:2xZ) -- PRD v0.6 (@`803ea38a9e`, msg 27079): the exit rule is "refused OR ran no job", and an EMPTY set HOLDs.**
- **AC1 gains two plants:**
  - (e) an enabled publisher with NO job in the window leaves the set;
  - (f) an empty derived set HOLDs with `empty_reason` `NO_DECLARED_PUBLISHER`.
- The worker in flight receives this amendment as a continuation of its order before its drain.
- **Gate limb:** `to-pipeline-gate` grades a modified order's `<placeholders>` only (NONE).

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>28</round>
<slot>~79</slot>
<fabric>site-z</fabric>
