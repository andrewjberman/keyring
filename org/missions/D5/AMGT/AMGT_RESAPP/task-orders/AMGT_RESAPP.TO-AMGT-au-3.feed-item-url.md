# AMGT_RESAPP task order -- `AMGT-au-3` -- EACH FEED ITEM SERVES ITS LINK TO THE ORIGINAL, OR A PLAIN REASON (FWD-4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-au-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~233</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; producer and route code and tests only. The gold rebuild is au-7's leg under the pair.
comp-iam: DECLARED-NOT-APPLICABLE for this cell -- the producer already reads silver articles; the route reads no new path (the url rides in gold).
comp-adversary: RUN by the issuer at the cut -- r71_served c35 FAILS at the base, deployed and local: 600 of 600 feed items over 95 names carry `url: null` and no reason.
EGRESS CLASS, declared: NONE. No vendor call; the link is the one the stored article already carries.
</preflight>

**Your worktree:** `C:/tmp/r71-233` (branch `wk-AMGT_RESAPP-233`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r71-233`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-au-3` (round 71, decomposition s.79)

PRD v0.38 FWD-4: each feed item is clickable through to the original; DONE WHEN (PRD `:505-507`) an analyst has read one and followed it
out.

The overlay feed (`/security/<key>/overlay` -> `feed.items[]`) serves `url: row.get("url")` (`lib/research/api/scoped_amgt.py` ~`:4715`;
the docstring ~`:4670` says gold holds no url). The gold mention table (`lib/research/harvest/publication_gold.py`, schema ~`:65-98`,
`mention_rows` ~`:271`) has no url column. The stored silver articles DO carry it, per source:
- `bbg`: `url`; `barrons`: `canonicalUrl`; `sa`: `links.self`, a RELATIVE path (make it absolute on `https://seekingalpha.com`);
- `ft` and `wsj`: no link stored.

1. **Producer:** `mention_rows` copies the article's link into a new nullable `url` column of the gold mention schema, per the source
   rules above; `ft` / `wsj` rows carry `url` null. Gold stays rebuildable from silver (C-HV-GOLD-REBUILDABLE): the same silver gives
   the same rows.
2. **Route:** each feed item serves `url` from gold; when `url` is null it also serves a plain `url_reason`, e.g. "the Financial Times
   copy we store does not carry its web link". An item from a source that stores its link never carries a reason.
3. **Plant tests** `lib/research/harvest/test_mention_url.py` (per-source extraction, including the relative `sa` path and the null
   `ft`/`wsj` cases) and `lib/research/api/tests/test_feed_url.py` (served url, or null + reason).
4. **Dry build, no write:** with the producer's own readers, build the mention rows for the covered names
   (`lib.research.coverage.covered_universe.covered_security_keys()`) from the newest stored silver WITHOUT calling `write_gold`, and
   print per source: rows, rows with a url. Save the printout as `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~233/dry_build_urls.txt`.

`publication_gold.py` is shared with AMGT_HARVST: change only what the url needs. Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W233-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, NO GOLD OR SILVER WRITE (the rebuild is au-7's, under a pair), no table, no schedule, no
   vendor or model call, no portal write.
2. Add the column and the fields only. No existing gold column, row key or served field changes.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/test_mention_url.py
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~233/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-au-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/harvest/test_mention_url.py lib/research/api/tests/test_feed_url.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-au-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; cat "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~233/dry_build_urls.txt"; echo "exit=$?"</invocation><expect>one line per source bbg, barrons, sa, ft, wsj with rows and rows-with-url; bbg, barrons and sa have url on every row; ft and wsj on none; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~233 <0.9.0_WK_AMGT_RESAPP~233@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~233/AMGT_RESAPP.TO-AMGT-au-3.feed-item-url.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api and harvest suites' last lines;
- the gold schema change (column, type);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-70 analysis item 3, ruling 5. publication_gold.py is HARVST's producer too (COO~H told at issuance). c35 grades on deployed after au-7's gold rebuild leg; the pair counts the gold table's writers (NEVER-1).

<status>pending</status>
<round>71</round>
<slot>0.9.0_WK_AMGT_RESAPP~233</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
