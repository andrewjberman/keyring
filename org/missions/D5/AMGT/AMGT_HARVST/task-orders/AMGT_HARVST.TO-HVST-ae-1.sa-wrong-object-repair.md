# AMGT_HARVST task order -- `HVST-ae-1` -- ROUND 32 chain A: THE SEEKING ALPHA WRONG-OBJECT REPAIR -- TAKE THE BODY FROM THE LISTING, RAISE THE PAGE CAP, QUARANTINE THE 38 STORED ROWS WHOSE ARTICLE IS NOT THE LISTED ONE, REBUILD GOLD (FWD-12, the precondition)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ae-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- phase A is LOCAL (repo code and tests; S3 READS only for the census). Phase B writes ONE quarantine object and new gold parts in opal-data-harvest, only under the signed never-widen pair; no delete, no overwrite.
comp-adversary: RUN at L5 -- the adversary is a quarantine that hides genuine rows (a date predicate does exactly that: 4 genuine 2025 Lenovo items) or a fix that stops the request but still stores a non-listing body. AC2 is the issuer's independent classifier; AC1's plants fail on the old behaviour.
</preflight>

## 0. THE CELL (decomposition section 45, cell `HVST-ae-1`; PRD v0.13 FWD-12)

**FWD-12, verbatim:** every stored Seeking Alpha article is the article its listing named. DONE WHEN, EXERCISED: (a)
every sa row since 2026-01-01 whose stored article is not the listed item is quarantined and counted, with the count
printed against the rows checked; (b) the sa path no longer requests `/api/v3/articles/{news_id}` and takes the body from
the listing; (c) the listing page cap is raised past 25; (d) a re-check over every stored sa row reads 0 mismatches.
PRECONDITION: no sa backfill writes until this is DONE.

**The defect (measured at the cut).** `lib/opal_data_harvest/publishers.py`, method `seeking_alpha`, around line 540:
the listing returns NEWS ids, then `self.module.article(self.session, identity)` requests `/api/v3/articles/{news_id}`,
a DIFFERENT id space, and `raw = self.session.captured[-1]` stores THAT response as the bronze capture. Silver is built
from the bronze capture, so the stored article is an unrelated (mostly 2023) article. Every sa job end on a late 502 or
ProxyError in round 31 was on these calls. The listing item already carries the body in `attributes.content` (the
text blocks are built from it today).

**The census at the cut** (issuer oracle `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round32/checks/ae1_common.py`):
85 sa silver article rows in 66 parts under `seeking-alpha/harvest/silver/article/`; **38 WRONG-OBJECT**. The predicate
(use the SAME one; never a date): a row is wrong-object when it was discovered through a symbol news listing
(`discovered_for` non-empty) AND it carries the raw article capture's own `id` AND its `title` is not the title of the
stored listing hit for the same id under `seeking-alpha/harvest/silver/listing_hit/` (no stored hit counts as unequal).
32 have a differing title (all 2023); 6 have no stored hit (2021). Rows without `id` (listing-shaped) and rows without
`discovered_for` (the analysis feed) are never wrong-object.

## 1. PHASE A (LOCAL) -- the code, now

1. **The sa leg takes the body from the listing.** In `seeking_alpha`, remove the `self.module.article(...)` call and the
   `self.session.captured[-1]` read. The bronze capture becomes the LISTING ITEM itself: `raw_bytes` =
   `json.dumps(item, ensure_ascii=True, sort_keys=True).encode("ascii")`, `raw_ext="json"`, `raw_hash` over those bytes,
   `raw_url` = the listing request's URL. Title, publish time and text blocks keep coming from the listing item, as now.
   `_note_fetch` is no longer called for sa (no article request is made).
2. **The sa page cap.** Raise `DEFAULT_MAX_LISTING_PAGES["sa"]` from 25 to **200** (the floor bound 2026-01-01 still ends
   paging; BA lists about 600 items since January at 20 per page). Other publishers' caps are unchanged.
3. **`lib/opal_data_harvest/sa_quarantine.py` (new), two subcommands, run as `python -m lib.opal_data_harvest.sa_quarantine`:**
   - `census` (read-only): applies the predicate above over every sa silver article row; prints `ROWS CHECKED: <n>`,
     `WRONG-OBJECT: <k> of <n>` and one line per wrong row (article key `sa:<article_id>`, `discovered_for`, published
     date, stored title, listed title or `NO-LISTING`). Writes nothing.
   - `quarantine --apply` (phase B only): writes ONE never-overwrite JSON object `{"written_at", "rows_checked",
     "article_keys": [...], "predicate", "silver_parts": [...]}` at an address built by `lib.research.harvest.store`'s
     own builders (`table_prefix("seeking-alpha", "silver", "quarantine")` + a `stamp()`-named object; never a
     hand-typed key), and the same content locally at
     `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/ae1_quarantine.json` with an added
     `"s3_key"`. Without `--apply` it prints what it would write and writes nothing.
4. **The silver read honours the quarantine.** In `lib/research/harvest/publication_gold.py`, the sa silver rows that
   feed `build-mention` and `build-daily` exclude every `article_key` listed in the NEWEST quarantine object (read once
   per build; absent object = exclude nothing). No silver or bronze object is moved, rewritten or deleted: the
   quarantine is reversible by writing a newer quarantine object.
5. **`lib/opal_data_harvest/test_ae1_sa_listing_body.py` (new), the plants** (each fails on the base behaviour): (i) a
   stub sa module whose `article()` raises; one listing page with 2 items yields 2 articles and `article()` is never
   called; (ii) the bronze capture bytes of each yielded article parse to the listing item (same `id`, same `title`);
   (iii) `DEFAULT_MAX_LISTING_PAGES["sa"] > 25`; (iv) the predicate classes the 4 shapes correctly (listing-shaped,
   analysis-feed, differing title, no stored hit) using in-memory rows; (v) the gold silver read drops a quarantined key
   and keeps every other row.
6. **Run the census** and keep its output as `ae1_census_A.out`. Report and STOP at the end of phase A; phase B is
   dispatched to you by the issuer after the never-widen pair is signed.

## 2. PHASE B (WORLD) -- only after the pair is signed and the issuer hands it to you

1. Re-run the census; its count must equal the signed count, else STOP with a row.
2. `quarantine --apply`, ONCE.
3. Rebuild gold from the quarantine-honouring code, ONCE each, as-of the UTC date of the act:
   `python -m lib.research.harvest.publication_gold build-mention --securities-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json --as-of <date>`
   then the same with `build-daily`. Each makes one never-overwrite part.
4. Run AC2 and AC3. Rollback is forward only: a newer quarantine object with an empty list, then a rebuild.

<paths>
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/sa_quarantine.py
lib/opal_data_harvest/test_ae1_sa_listing_body.py
lib/research/harvest/publication_gold.py
lib/opal_data_harvest/test_bronze_capture.py
lib/opal_data_harvest/test_n1_received_bytes_and_run_record.py
lib/opal_data_harvest/test_p2_fetched_and_stored_keys.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

**Reads you may need (no write):** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round32/checks/`
(the oracles), `lib/research/harvest/store.py`, `lib/opal_data_harvest/conftest.py`, the existing tests beside your file.
**Never:** a request to any publisher (phase A needs none; phase B needs none), a delete, an overwrite, an edit to any
other publisher's leg.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ae-1"><invocation>python -m pytest lib/opal_data_harvest/test_ae1_sa_listing_body.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ae-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round32/checks/ae-1.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ae-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round32/checks/ae-1.AC3.py</invocation><expect>AC3 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC1 passes at the end of phase A. AC2 and AC3 FAIL until phase B (38 outside a quarantine; no manifest) -- record
  them as FAIL with `status_reason: phase B pending` at the end of phase A, never as PASS.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-ae-1.sa-wrong-object-repair.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ae-1.sa-wrong-object-repair`.

## AMENDMENT 1 -- 2026-10-01 ~05:5xZ, the issuer, on the phase-A report (rows Z-W90-S1, Z-W90-S2)

1. **Z-W90-S1 ACCEPTED:** the bronze capture is `{"data": item}` (the listing item whole, inside `data`), so
   `silver_from_bronze._extract_sa` reads the listed `id` and `title`. This replaces section 1 item 1's literal
   `json.dumps(item, ...)`; everything else in item 1 stands.
2. **Z-W90-S2 RULED:** a listing item the sa leg accepts for storage COUNTS AS FETCHED -- its body arrived in this job, so
   the run record's `keys_fetched` and the outbox join keep their meaning (the run record is a source of served
   coverage). Restore `self._note_fetch("sa:" + identity)` at the point the item is accepted (after the pre-floor and
   held skips), with NO request made. Section 1 item 1's "`_note_fetch` is no longer called" is withdrawn.
3. **Paths added:** `test_bronze_capture.py`, `test_n1_received_bytes_and_run_record.py`,
   `test_p2_fetched_and_stored_keys.py`. Update ONLY their sa arms so they assert the listing-body behaviour (the sa
   bronze capture parses to `{"data": <the listing item>}`; a planted new sa key is counted fetched and joins an outbox
   row). Other publishers' arms are not touched.
4. **Done when:** AC1 still passes, and `python -m pytest lib/opal_data_harvest/ -q` reads 0 failed (the base was 363
   passed, 1 skipped; your 8 new tests make 371). Re-run AC1, update the instance, commit. Do not flip `<status>`.

## AMENDMENT 2 -- 2026-10-01 ~06:5xZ, the issuer: phase B is a measured DELTA=0 act on served output (no pair)

1. **Measured at signing** (`round32/checks/ae-1.signing.py`, output `round32/ae1_signing.json`; the gold builders' own
   code through a capturing client, 0 puts sent): with the 33 quarantined keys, `build_mention` reproduces the served
   snapshot exactly -- 379 rows, 0 gone, 0 added, 0 changed, digest
   `08f636c18d66ce8888f8d7cfdc761bacf8f047d9a22c3bf65fce9248415c0e6a`. None of the 33 keys was ever in served gold (the
   unrelated articles do not mention the securities). CLAUDE.md NEVER-1: a verified DELTA=0 needs no hold, so phase B
   carries NO never-widen pair.
2. **`build-daily` is DROPPED from phase B.** Its dry build moves 8 rows and adds 191, all from the as-of date advancing and
   round 31's run records (ASML 09-27..09-30 coverage) -- not from the quarantine. That is the daily producer's own
   cadence, not this cell's act.
3. **Phase B, in order (section 2 is replaced):**
   1. `python -m lib.opal_data_harvest.sa_quarantine census` must print `WRONG-OBJECT: 38 of 85`; anything else is a STOP
      with a row.
   2. `python -m lib.opal_data_harvest.sa_quarantine quarantine --apply`, ONCE (one never-overwrite object under
      `seeking-alpha/harvest/silver/quarantine/`, plus the local `~90/ae1_quarantine.json`).
   3. `python -m lib.research.harvest.publication_gold build-mention --securities-json org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json --as-of <the UTC date of the act>`, ONCE.
   4. **DELTA gate:** read the part it wrote; its rows' digest (sha256 over the sorted `json.dumps(row, sort_keys=True,
      default=str)` lines, as `ae-1.signing.py` computes it) must equal the digest above. If it differs, STOP and file a
      BLOCKING row naming both digests; do not run anything else.
   5. Run AC2 and AC3, update the instance, and flip `<status>` to `complete` when both pass.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Analysis `ROUND_ANALYSIS.round31.md` @`309b2da963` section 4 item 1; brief IV.4 (`publishers.py:540`, 32 of 49 checked).
- **Pair (phase B):** the quarantine moves gold (`chatter_daily`, `article_security_mention`, which RESAPP's FWD-32 counts),
  so CTO + COO never-widen halves name the 38 keys, the two gold parts and the rollback, before phase B is handed over.
- The `publishers.py` session-build hookup for ae-2's `TabSession` is the issuer's, at the merge.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>32</round>
<slot>~90</slot>
<fabric>site-z</fabric>
