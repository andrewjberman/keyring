# NFRA_MCPINDEX task order -- `MX-c-36` -- curated plain-language tags for harvest rows h3 (Seeking Alpha, social, wsj): 10 rows that carry derived `inferred` tags today

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round18-RESEARCH.md</decomp_doc>
<owned_cells>MX-c-36</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-36</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~54</issued_to>
<issued_by>2.0.0_SA_COO~MI2</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- one new data file of tags; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-run (the file is absent) and eight planted arms (`plant_ct.py`, 8 of 8) are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-36` (round 18, workstream RESEARCH; row Z-C-S61)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The gateway's data catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` lists tables; each row has `nl_tags`, the plain words a person types to find it (`opal_discover` matches a question against them). The 10 rows below have NO tags from their source, so the emitter fills them with a mechanical fragment of the row's own name and text, marked `nl_tags_basis: inferred`. Those fragments are not words a person would type. You write the real tags.

**What to write.** One new JSON file: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~54/research_group_map_h3.json` -- a group-map file the catalog emitter reads (`--group-map`): `{"rows": {"<entity>": {"nl_tags": ["tag one", "tag two", ...]}}}`. The `rows` object has exactly the 10 entity names below, and each entry has ONLY the key `nl_tags` (no other key). An optional top-level `"_about"` string may say in one sentence what the file is.

The 10 entities (section `harvest_datasets` of the catalog; read each one's `business_meaning`, `example_questions` and current inferred `nl_tags` there, read only):
- `harvest_seeking_alpha_harvest_bronze_article`
- `harvest_seeking_alpha_harvest_bronze_news`
- `harvest_seeking_alpha_harvest_bronze_news_listing`
- `harvest_seeking_alpha_harvest_bronze_report`
- `harvest_seeking_alpha_harvest_bronze_symbol`
- `harvest_seeking_alpha_harvest_silver_quarantine`
- `harvest_seeking_alpha_harvest_state_job_record`
- `harvest_social_v1`
- `harvest_wsj_harvest_bronze_article`
- `harvest_wsj_harvest_bronze_news_listing`

**What a good tag set is, for each row.**
- 4 to 6 distinct tags. Each tag is 2 to 5 words of lowercase ASCII letters and digits joined by single spaces: no hyphen, no other symbol, no capital letter, never a single word.
- Words a person would type or say to ask for this data: the topic in plain language, the question forms, the common synonyms. Draw them from the row's own `business_meaning` and `example_questions`; invent no fact the row does not state.
- NOT a fragment of the table path or the entity name. Bad (this is what the mechanical derivation gives now): `harvest wsj harvest bronze`, `article bronze harvest bucket`. Good, for the same kind of row: `wall street journal articles`, `raw wsj article text`, `saved wsj articles`.
- At least 3 tags per row must differ from the mechanical derivation (the check computes it), no tag repeats inside a row, and at least one tag shares a word of 4 or more letters with the row's own text.
- A row whose text says it is a raw store, a plumbing table or a quarantine says so in plain words in one tag (for example `raw saved articles`, `rejected articles`), so a person looking for finished data is not sent to it.
- Examples of good tags already in the catalog (contract-given, in this form): `news chatter`, `media attention`, `how much press`, `article count by day`, `annual report analysis`, `risk factors`, `fund holdings returns`.

### Steps

0. From the worktree root, `python -c "import yaml"` works (the check needs it).
1. Read the 10 rows. Write the file. Do not change any other file in the repository.
2. Run the criterion in section 4.

## 2. BOUNDS

1. You write ONLY `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~54/research_group_map_h3.json` and the rest of your own deliverables folder. You do not edit the catalog, any row file, the emitter, the generator, the checks or any test. No AWS call. No deploy. No push.
2. The emitter (another issuer's order, `MX-c-21`) reads this file through `--group-map`, replaces the row's tags with yours and drops its `nl_tags_basis`; you do not build that and your file is data only.
3. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
4. The check is `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/checks/ct.h3.sh` (python `ct_check.py`). Read `ct_check.py` for exactly what is graded. Do not edit it.
5. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~54/research_group_map_h3.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~54/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W54-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI2`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 1)

<proof_of_spec>
  <expected_criteria>AC1</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-36" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI2/round18/checks/ct.h3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (slice h3: 10 entities assigned); all seven checks ok: exactly the 10 entities, each with only `nl_tags`, 4 to 6 tags each, each tag 2 to 5 lowercase words, no repeats, at least 3 tags per row that the derivation does not give, a tag grounded in the row's text -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~54/NFRA_MCPINDEX.TO-MX-c-36.curated-tags-h3.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance.
2. APPEND `<status>complete</status>` only if the criterion PASSES (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~54/research_group_map_h3.json`; (ii) the proof instance.
4. Report once, with: the DENOMINATOR line verbatim, the tags you wrote for the first two rows, and your commit shas.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI2).** Round 18, workstream RESEARCH, worker ~54. Source: CTO round-17 analysis (`ledger/ROUND_ANALYSIS.round17.md` @c7e130a7b2) ruling 1: Z-C-S61 closes at 0 inferred on the in-scope rows, each workstream curating its own files, tags marked `curated`. The mechanism is the ASSETS issuer's `MX-c-21` (`--group-map`, `nl_tags` replace the inferred ones and drop `nl_tags_basis`; msg 34584); this slice is data in that map's format, and the ASSETS issuer's one emitter run (`MX-r-15`, about 17:00Z 2026-10-16) is given the four slice files. Slices h1 (11), h2 (11), h3 (10) harvest rows and p1 (the 5 portal rows) are the 37 RESEARCH rows that carry `inferred` today (32 harvest, 5 portal_datasets); the other 7 inferred rows are the ASSETS issuer's own map. The check grades form and grounding (mechanical); whether the words are ones a person would type is read by the issuer on a sample of rows at the drain and by the CTO at the Z-C-S61 close; no judgment criterion is declared, so no round-close waits on an L9 grade. Base dry-run 2026-10-15 at 5858411c5c: `ct.h3` FAIL as expected (the file is absent). Planted arms: `plant_ct.py` 8 of 8.

<status>issued</status>
<round>18</round>
<workstream>RESEARCH</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
