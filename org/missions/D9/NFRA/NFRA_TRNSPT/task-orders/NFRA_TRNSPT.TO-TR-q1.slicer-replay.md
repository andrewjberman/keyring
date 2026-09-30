# TO NFRA_TRNSPT.TO-TR-q1 -- the slicer as a tested Python function over gold, run over a replay of past Generate compositions

<to_id>NFRA_TRNSPT.TO-TR-q1</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~4</issued_to>
<issued_by>2.0.0_SA_COO~T</issued_by>
<issued_date>2026-09-30</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `TR-q-1` (`decompositions/NFRA_TRNSPT_DECOMP.md`) |
**outcome_ref:** FWD-10 | **depends_on:** TR-k-1 (drained; the gold contract and `gold.py` on your branch)

---

## WORKER FACE

### THE CELL

`TR-q-1`, communications item 5 (PRD section 3): "The slicer as a tested Python function against gold, run over a REPLAY of past
Generate compositions (no live trigger)." C-SLICE (binding): "All Python, no AI. `yc_variant` equal to the request's variant,
ranked by overlap of models with the request's models, then account type, then recency; near-duplicates removed by
`paragraph_hashes`; about ten candidates. Across firms (Andrew: "across all firms, its not their content, its manav's response").
With no candidate the slicer falls back to the nearest variant and the draft says so in its provenance; with none at all a draft is
still produced and says it has no precedent." C-KIMI: input limited to abstract fields (variant, model names, account type, themes,
holdings as category weights; no client identity, no account ids) -- so the slicer's OUTPUT carries only those. No Kimi call this
round.

**The request side (read):** IRPT's Generate request carries `variant` (0 = Overview, 1 = Comparison, 2-5 = Multi), `comparison_keys`,
`client_id`, holdings and `holdings_fingerprint`, `settings` (v3 section 7); READY writes `REPORT#<report_id>#<revision>` items into
DynamoDB `irpt-requests` (`infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py`, `report_index.py`). Map IRPT variant
to `yc_variant`: Overview -> 1, Comparison -> 2, Multi -> 3.

**Build:**
1. `data/transcripts/scripts/outlook/slicer.py`: `slice(request, gold_rows, k=10) -> {"candidates": [{"record_id","score","why":
   {...}}], "variant_used", "fallback_variant": bool, "no_precedent": bool, "provenance": {...}}` where `request = {"yc_variant",
   "comparison_keys": [...], "account_type", "holdings_category_weights": {...} | null}`. Ranking: exact variant first (else the
   nearest variant, flagged), then model overlap (Jaccard over `models_referenced` vs `comparison_keys`), then account type match,
   then recency (`sent_at`); near-duplicate removal by `paragraph_hashes` overlap above 0.6; at most `k`. Output rows carry only
   `record_id`, the abstract fields and the score; never `recipient_firm`, never text (the drafter reads text by `record_id` later).
2. `data/transcripts/scripts/outlook/replay.py`: `--requests <json>` (a list of abstract requests), `--gold <parquet path or
   s3 address>`, `--out <json>` writes per-request results and prints `SLICER-REPLAY client_identifiers=0 requests=<n>
   with_candidates=<k> fallback=<f> no_precedent=<j>`; `client_identifiers` counts any key named `client_id`, `account`,
   `email`, `name`, `recipient_firm` or any 8-digit token in the output (must be 0). Extract the replay set with `--extract-irpt`:
   a READ-ONLY `boto3` scan of `irpt-requests` for `REPORT#`/request items, projecting ONLY `variant`, `comparison_keys`, an
   account-type field if one exists, and holdings as CATEGORY weights (never tickers with quantities, never `client_id`), written
   to `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~4/R1_REPLAY_REQUESTS.json` with a count and the scan's
   denominator. If the scan is refused or the table has no such items, write the file from the fixture requests in your test and
   file a surprise row; never fabricate a real-looking request.
3. Tests `data/transcripts/scripts/tests/test_slicer.py`: synthetic gold rows (inline, invented) covering: exact-variant preference,
   model-overlap ranking, account-type tie-break, recency, near-duplicate removal, the `k` cap, fallback to the nearest variant
   flagged, no-precedent flagged with an empty candidate list, cross-firm rows admitted, and an output with zero identifiers.

### ACCEPTANCE

<criterion id="TR1-q1-AC1" cell_refs="TR-q-1"><invocation>python -m pytest data/transcripts/scripts/tests/test_slicer.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`TR1-q1-AC1` -- C-SLICE's ranking, dedup, cap, fallback, no-precedent, cross-firm, abstract-only output.

<criterion id="TR1-q1-AC2" cell_refs="TR-q-1"><invocation>python data/transcripts/scripts/outlook/replay.py --requests org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~4/R1_REPLAY_REQUESTS.json --gold data/transcripts/scripts/tests/fixtures/outlook_gold_synthetic.parquet --out org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~4/R1_SLICER_REPLAY.json</invocation><expect>SLICER-REPLAY client_identifiers=0</expect></criterion>
`TR1-q1-AC2` -- the replay over the extracted requests against a synthetic gold parquet (written by your test setup to the fixture
path): every request answered, zero client identifiers in the output. The issuer re-runs it over the REAL gold at the drain.

<expected_criteria>TR1-q1-AC1,TR1-q1-AC2</expected_criteria>

Dry-run at the base 2026-09-30 14:0xZ: AC1 "no tests ran", AC2 "No such file" -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL.** The DynamoDB scan is READ-ONLY and projects abstract fields only; no S3 write; no model call; no live trigger.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `NFRA_TRNSPT-W4-S<k>`), and do not weaken the test to pass.

<paths>
data/transcripts/scripts/outlook/slicer.py
data/transcripts/scripts/outlook/replay.py
data/transcripts/scripts/tests/test_slicer.py
data/transcripts/scripts/tests/fixtures/outlook_gold_synthetic.parquet
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP.md</decomp_doc> (round 1), cell `TR-q-1`.
<owned_cells>TR-q-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR1-q1-AC1, TR1-q1-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~4/NFRA_TRNSPT.TO-TR-q1.slicer-replay.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR1-q1-AC1,TR1-q1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the ranking function, the replay set's count and denominator (or the fixture fallback and its row), the SLICER-REPLAY line, the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; the READY hook (S18) is IRPT_BCKEND's, round 2.
comp-iam: RUN -- the scan of irpt-requests runs under Andrew's IAM user, read-only; the commentary Lambda's principal is round 2.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; the volume finding (6 to 18 real commentary emails) means many requests will read no_precedent, which is the designed answer, not a defect.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 C-SLICE, C-KIMI (input bound), S16, section 3 communications item 5; decomposition round 1 cell TR-q-1.
