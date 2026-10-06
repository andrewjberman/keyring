# AMGT_HARVST task order -- `HVST-av-1` -- ROUND 49 (round-48 analysis ruling 1; CTO @6d005e5261): FT AND WSJ LINKS FROM THE ADDRESS THE STORED RECORD ALREADY CARRIES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-av-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~98</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code, plants on planted rows, and ONE read-only census over stored silver (S3 GET/LIST only). NO publisher host (ft.com, wsj.com or any other) is contacted: Andrew's FT hold stands. NO S3 write, no gold build, no collector run, and never touch any `.runtime` directory.
comp-adversary: RUN at L5 -- the adversary is a guessed or constructed link, a link on a foreign host (a syndication or redirect address), a list-valued og:url mishandled, a change to any other publisher's link, or a census that fetches.
</preflight>

## 0. THE CELL

`lib/research/harvest/publication_gold.py`, `article_url(article_row)` (around line 281):
- For `ft` and `wsj` it returns only the top-level `url` (`_clean_link`), else None.
- Stored silver for both publishers, measured at the cut (read-only, no publisher contact):
  - **ft:** 185 articles.
    - 171 carry `html_meta["og:url"]` of the form `https://www.ft.com/content/<uuid>` and no top-level `url`.
    - The other 14 are normalised records that carry the top-level `url` and no `html_meta`.
  - **wsj:** 463 articles.
    - 448 carry `html_meta["og:url"]` and `articleData.sourceUrl`.
    - The other 15 carry the top-level `url`.
- So the stored records already hold the publisher's own canonical address: nothing is constructed.
- `html_meta` values may be a string or a list; `articleData` may be a dict or a JSON string. Read both forms.

## 1. THE BUILD (LOCAL)

1. `article_url` for `ft` and `wsj` reads, in order:
   - the top-level `url`;
   - else `html_meta["og:url"]` (its first non-blank value if a list);
   - else, for wsj only, `articleData["sourceUrl"]`.
   A value is accepted ONLY when it starts `https://www.ft.com/` (ft) or `https://www.wsj.com/` (wsj); anything else is None. It is
   never constructed or guessed, and no host is fetched. Update the docstring (name `HVST-av-1`). Every other publisher's branch is
   unchanged.
2. **Plants** in `lib/research/harvest/test_av1_stored_canonical_url.py` (planted rows, no network):
   - (i) an ft row with only `html_meta["og:url"]` returns it, and the list form returns its first value;
   - (ii) a wsj row with only `articleData.sourceUrl` (dict, and JSON-string form) returns it;
   - (iii) a top-level `url` still wins;
   - (iv) an og:url on a foreign host returns None;
   - (v) bbg, barrons and sa rows return exactly what they returned before (pin current outputs);
   - (vi) a mutant that skips the host check makes (iv) fail.
3. **The census:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~98/av-1.link_census.py`.
   - It reads `store.silver_latest` for ft and wsj (S3 reads only) and prints per publisher:
     - `articles <n>; with link <m>`, by source (top-level url / og:url / sourceUrl / none);
     - for wsj, `og:url == sourceUrl on <a> of <b>` where both are present;
     - the count of values refused for a foreign host.
   - Write its output beside it as `av-1.link_census.out`.
4. The research harvest suite stays green: `python -m pytest lib/research/harvest -q`. Report the count.

Worktree: given in your spawn prompt (sparse cone, cut from CLOUD at the issuance commit).

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/test_av1_stored_canonical_url.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~98/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-av-1"><invocation>python -m pytest lib/research/harvest/test_av1_stored_canonical_url.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-av-1"><invocation>python -m pytest lib/research/harvest -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
</proof_of_spec>

- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~98/AMGT_HARVST.TO-HVST-av-1.stored-canonical-url.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-av-1.stored-canonical-url`. Pin every artifact row to the commit that carries it.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Round-48 analysis @6d005e5261, ruling 1; decomposition section 62.
- `article_url` was written by AMGT_RESAPP (au-3 @69c017d520, aw-5 @9d2b7b3d7c); `2.0.0_SA_COO~Z` is told at the issuance.
- av-2 (gold rebuild #7 under a new pair) follows the merge.

<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<status>issued</status>
<round>49</round>
<slot>~98</slot>
<fabric>site-z</fabric>
