# 2.0.0_SA_COO~M -- 2026-09-24 0400-0615Z: display + CUSTODY_UNITS fills, P pin merged, X10 ACTIVE row, labelled COT candidate + GO request

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

Seat `2.0.0_SA_COO~M` (Claude successor to the Codex M seat). Loop `/loop 20m` cron fcf016cf driving Andrew's goal
(Holdings end to end with a SNAPSHOT model overlay for every 49 Financial and Inflection client; structurally correct
Cottonwood pipeline). Window: since `irpt_m_publications_and_cot_recut_0118-0400Z.md` @55c9eccdfc.

## What happened (conclusion first)

1. **Labelled Cottonwood re-cut candidate dec293d6 PREPARED and GO REQUESTED** (CTO 100330, cc P 100331). 841 accepted
   accounts, 16,749 nodes, reconcile exact, both schema copies validate. 16,740 of 16,749 nodes carry `display`; the 9
   without are ACCOUNT nodes absent from the landed directory (842 entries), unassigned, 12.625% of custody value --
   the member is omitted, never blank. CUSTODY_UNITS on 13,656 of 14,426 securities: every OBSERVED one (3,127) and
   10,529 of 11,299 ASSIGNED component rows; the 770 without are components the account holds no custody position for.
   One source_revision on every units fact, equal to the fact_holdings receipt sha256. Zero price facts. Anna's subtree
   75 of 75 labelled. Publisher check (zero writes): preconditions PASS, CAS over index version .VLcr1BCE (etag ffa30e5b),
   prior 2d067b4d retained. Execution waits on the CTO's GO word; P's step-3 holdings repackage readback (CodeSha
   kZygK57y.. 06:00:10Z, P 100327) and the DEV rebuild (7975c3bb) are in hand.
2. **P's schema pin b3e3bcb044 merged** into codex/irpt-m-completion @550789f51d (merge, never a rebase). One conflict,
   `infra/aws/lambda/investor-reporting/_scope/maintained_sources.py` (P's lane): resolved to P's side byte-for-byte
   (cmp against the pin's blob). Two untracked P-owned paths verified byte-identical to P's blobs and removed before the
   merge. After the merge `display_admitted()` and `custody_units_admitted()` both True.
3. **X10 registry row ACTIVE** @7262571e4c (CTO batch 27 / 100299 M act): state PENDING_ENFORCEMENT -> ACTIVE,
   enforcement_ref null -> 0a101a666816dd5e2302992547129ca42637b923; nothing else typed; computed policy_sha256
   e0046398e239... `lib/tests/test_irpt_destination.py` re-encoded to the ACTIVE state (63 passed). Pin sent to P and
   the CTO (100319/100320). P staged the row by pin for the adapter rebuild (100327).
4. **Producer fills** (earlier in the window, on the M branch): node `display` fill @699bf9ed1b (labels from the
   directory's masked discriminator, the strategy name, the model name, the residual sleeve wording, the custody
   symbol + description; contract-gated) and CUSTODY_UNITS valuation fact @947d2a21a5 (quantity from fact_holdings.Units,
   source_revision = the custody receipt sha; price refused per CTO 100208). Test arms follow the merged contract
   @9cdb81368e. Producer suite 240 passed / 4 failed (pre-existing currency-state arms).
5. **Portal UI stopped at the labels pin e5dd8487** (codex/irpt-m-ui-labels on DEV 7975c3bb) per CTO CALL 1(c): the
   L2-by-model_name rows and the Client sleeve are DSGN_IRPTV1 cells C3/C4 (COO~D's). The CTO's L6 trigger for
   DSGN_IRPTV1 is (a) the served COT snapshot carrying `display` on Anna's leaves -- this seat's republish on the GO --
   and (b) e5dd8487 an ancestor of DEV HEAD (P's next candidate, MSTR's push).

## Commits (author 2.0.0_SA_COO~M; ALL LOCAL -- worktree branch codex/irpt-m-completion, pushed by nobody)

699bf9ed1b display fill · 947d2a21a5 CUSTODY_UNITS · 550789f51d merge P b3e3bcb044 · 7262571e4c X10 ACTIVE row ·
9cdb81368e display test arms · 92a75a0bc5 labelled candidate census + STATUS.md. Portal: e5dd8487 (codex/irpt-m-ui-labels).
Shared tree (CLOUD): this log only. Push state of CLOUD: LOCAL @3a02c2dadd vs origin/CLOUD 14b01608e7 (ls-remote read ~06:0xZ).

## Compiler Tools

| Tool | Where | Result | Note |
|---|---|---|---|
| `.tools/commit-gate.sh` | test_irpt_destination.py, test_holdings_display.py | PASS | py_compile + ds-precommit + ruff clean |
| `.tools/safe-commit.sh` | 4 commits this window (M worktree) | PASS | surprise-row gate + missions-tree-check on the merge: 0 violations |
| naming gate (LGIC_ENFORCE) | via safe-commit | PASS | no new hand-kept firm tokens (keys derived from silver_prefix) |
| pytest producer suite | data/assets/scripts/gold/investor_reporting/tests | PARTIAL | 240 passed / 4 failed, the pre-existing currency-state arms |
| pytest lib/tests/test_irpt_destination.py | ACTIVE row | PASS | 63 passed |
| jsonschema (both contract copies) | prepared bytes dec293d6 | PASS | 24,185,053 B body validates against docs/ and lambda copies (sha 976e93dedf73) |
| publish_cot_live.py check | prepared bytes | PASS | preconditions PASS, zero writes |

What worked: preparing exact bytes + receipts before asking for the GO; the census over the prepared bytes caught my own
first census's three instrument errors (wrong directory bucket read as "0 entries" -> every account "absent"; an
observed/component predicate that matched everything; a missing account id) before any number left this seat.
What failed: nothing at the tools. Gap found: `_directory_account_labels` swallows the NoSuchKey on a wrong bucket and
returns {} -- a caller cannot tell "no directory landed" from "wrong bucket"; the build reads the right bucket via the
receipts so the served numbers are sound, but a census that calls it directly must assert non-empty (mine now does).

## Blockers

None. The republish is GATED on the CTO's GO word (an explicit gate, CTO 100173), not blocked.

## Current State (zero-context handoff)

- M worktree `C:/Users/AndrewBerman/Desktop/ajb_irpt_m`, branch codex/irpt-m-completion @92a75a0bc5, clean of tracked changes.
- Prepared labelled candidate: `.runtime/holdings-journey-20260923/prepared_cot/` (candidate_summary.json,
  source_receipts.json, the platinum body + gold parquet under opal-data-cottonwood/...). Prior candidate archived at
  `prepared_cot_2d067b4d/`. Publisher `.runtime/holdings-journey-20260923/publish_cot_live.py <GO> publish` (constants
  re-pinned: EXPECTED_REV dec293d6, EXPECTED_ETAG ffa30e5b, EXPECTED_INDEX_VERSION .VLcr1BCE, PRIOR_REV 2d067b4d).
- Live COT index: opal-data-cottonwood investor-reporting/holdings/index.json version .VLcr1BCEMXLODKeFWA00C31rlgnUBAr,
  row 2026-09-22 -> 2d067b4d (served now). 49F index -> 7c0e7ce3, INF index -> 1ebc7696 (unchanged this window).
- Deliverables (M branch): IRPT_MVP_M/COT_LABELLED_CANDIDATE_CENSUS_20260924.json, STATUS.md (current block prepended).
- Deployed irpt-holdings: CodeSha kZygK57y.. (P, 06:00:10Z) with the display + CUSTODY_UNITS schema copy.

## Next Steps

1. On `GO <ref>` from [1.0.0_SA_CTO]: run publish_cot_live.py <ref> publish; read back index version/etag + served
   envelope; write COT_LABELLED_PUBLICATION_RECEIPT_20260924.json; overwrite STATUS.md; tell the CTO, [2.0.0_SA_COO~P] and
   [2.0.0_SA_COO~D] (its L6 condition (a)).
2. Prepare 49F/INF labelled candidates (display from facts, units) with zero writes; request a second GO (CAS over each
   firm's existing index -- the first-publication IfNoneMatch script needs the CAS variant).
3. Rebuild the model overlay artifacts on the labelled revisions; /verify at goal completion.
