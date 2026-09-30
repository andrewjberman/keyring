# AMGT_RESAPP task order -- `AMGT-zz-5` -- LEAD-LIST ROWS CARRY A NAME AND "PLACES MOVED SINCE THE LAST RUN"

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-zz-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~184</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change and no new read surface: the crosswalk and ranking reads this order extends already run in scoped_amgt.py on the deployed function. A read the function does not already make is a row, not a grant.
comp-adversary: RUN by the issuer at the cut -- AC1/AC2 read the four live axes in process; base: 16 of 66 named, no name_source, no places_moved.
EGRESS CLASS, declared: NONE. Opal's own AWS, read-only.
</preflight>

## 1. THE CELL -- `AMGT-zz-5` (round 51, decomposition s.59)

The lead panel serves four ranked lists through `lib/research/api/scoped_amgt.py` `read_rankings(movement, subject, as_of_date=None,
limit=None)` (`:644`) -- TRENDING|BREAKOUT x CHATTER|PRICE, 66 rows at the cut. Rows pass through in the producer's order. Two
things the page wants are missing (the page lists `places_moved` as an unserved column):

1. **Name.** 16 of 66 rows carry a `name` today. When a row has no name from its ranked source, take it from the served identity
   crosswalk (the adapter already imports `crosswalk`, `:115`; a registration-built record carries it at
   `record["identity"]["name"]`), matched on the row's security key -- never a guessed or fuzzy match, and never the ticker as a name.
   Every named row carries `name_source` (the ranked source's own label for a name that came with the row, `"crosswalk"` for the
   fallback). A row the crosswalk does not name stays unnamed.
2. **Places moved.** Each row carries `places_moved`: the row's rank in the previous COMPLETE generation of the SAME axis (the latest
   served generation dated before this one; the pointer walk `_find_latest_served_pointer` / `read_generation_pointer` /
   `read_generation_rows` already exist) minus its rank now, positive = moved up. When there is no previous generation, or the security
   was not ranked in it, `places_moved` is `null` and `places_moved_reason` says which. One prior read per axis per call, not per row.

Nothing else moves: no rank, score, order, row count or existing field changes. Add tests (stubbed reads) for each branch.

## 2. BOUNDS

1. `scoped_amgt.py` and the api tests only. No route added or changed (payload fields only). Standing: no install, no push, no
   promote, no deploy, no vendor call. REFUSE, do not rescue.
2. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~184/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-zz-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_5_rows.py --what names; echo "exit=$?"</invocation><expect>rows with a name N of R, N &gt; 16, each with name_source; LEAD-LIST ROWS CARRY MORE NAMES, EACH WITH ITS SOURCE: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-zz-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_5_rows.py --what moved; echo "exit=$?"</invocation><expect>every row carries places_moved (int, or null with a reason), at least one int; LEAD-LIST ROWS CARRY PLACES MOVED: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-zz-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/api-suite.sh; echo "exit=$?"</invocation><expect>pytest reports N passed and 0 failed (plus your new tests) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~184/AMGT_RESAPP.TO-AMGT-zz-5.lead-list-names-and-places-moved.proof_of_spec.json`. Report once: named N of R by source, places_moved int/null counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-50 analysis ruling 5, cell 5 (DSGN FWD-2/3). Base: AC1 FAIL (16 of 66, no name_source); AC2 FAIL (no
places_moved); AC3 PASS (the api suite). Served in zz-8.

<status>pending</status>
**ISSUER CLOSE (`2.0.0_SA_COO~Z`, 2026-09-30 ~04:4xZ):** AC1 PASS (18 of 66 named: etf-classifications 16, crosswalk 2; 0 by ticker), AC2 PASS (66 of 66 carry places_moved, 66 int). AC3 FAILED in the worker's run on the REGISTRY_HASH stamp only (row Z-W184-S1); the issuer synced CLOUD (carrying zz-4's restamp) into the branch at bde4f0dc02 and re-ran AC3: 351 passed, 0 failed. Resolving row Z-S310. The prior-generation walk measured within noise of CLOUD per axis.
<status>complete</status>
<round>51</round>
<slot>~184</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
