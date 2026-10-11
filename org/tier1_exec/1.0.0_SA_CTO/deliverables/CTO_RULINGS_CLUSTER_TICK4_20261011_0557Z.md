# CTO rulings -- cluster-lead tick 4 (2026-10-11 05:57Z)

Read: `python .tools/open-calls.py list --all --cloud` at 05:57:54Z: 4 of 4 boxes, 10 OPEN (fork 1, act 9), 78 closed.
keep-driving scan=off empty_tick=off on all four. sitez 0dd7 closed. New: dell1 fe9b.

## dell1-20261011T053810Z-fe9b -- MDPF_CANON X2: the combined all-firms figure carries single-firm lines (fork A/B)

**Not ruled here: SENT TO ANDREW with the recommendation.** The project's own text reserves X2 to him (CN-c-1: "it does NOT
propose a fix, that is Andrew's call"; X2 OWED -> GRANTED is his acknowledgement), and the change is to what the Model
Portfolios page serves in its global view.

Measured in the round-3 basis (`X2_GLOBAL_BASIS.md` @945e1add0c, as-of 2026-10-08, read by this seat from box/dell1):
- Headline sums (`opal_aggregate_aua`, `model_aua`): held at 3 firms. Unchanged under either option.
- `by_model`: 41 entries across the three served files; 21 are held at exactly ONE firm, and in 14 of those the global
  value equals that firm's value (e.g. the two Inflection 50/50 blends at 160 and 23 accounts; nine Cottonwood models at
  1-13 accounts, Opal Muni Sleeve among them). Min firms per entry: 0 (some entries no firm holds at the as-of).
- Two series (`non_model_aua`, `inflection_non_model_aua`): one firm each.

Options as filed by `2.0.0_SA_COO~D1`:
- (A) fold every `by_model` entry held at fewer than 2 firms into one "other models" line and keep the two one-firm series
  out of global. Headline sums unchanged. A served change under never-widen sign-off, every global leaf read before and
  after. The project's REC.
- (B) keep them and rewrite FWD-3 to state what the global view reveals. Changes the ENDPOINT; re-signs the ratified half.

CTO recommendation: **(A)**, because the global view is the one any login can open and a one-firm line equal to that
firm's value is that firm's book shown to the others. Rollback is the publisher's previous output (dated files).

## dell2 XB-20261011T055236Z-0989 item 4 -- a new attribute key on `infra/logic/registry/scopes.json` (shared-infra CRM selector)

**Ruling: YES, one new VIEW field on the firm row, under these terms.** (Owner of the LGIC canon registry schema: this seat.)

Measured: `s3-lgic-firm-buckets.tf:65` reads `scopes.json` only (not `systems.json`); `systems.json` rows carry no firm link
and no per-system host field (54 rows; keys `key, class, long, owner_*`); `scopes.json` already has a VIEW family
(`tenant`, `monolith_scopes`, `pipeline_trees`, `_about.view_fields`). The fact "this firm's bucket hosts the restricted
Commonwealth CRM prefix" is a relationship of the scope, so a view field on the scope row is the right home and the TF
already reads that file. The `masters` proxy stood in for a fact the registry did not carry; dell2's ruling 1-3 stand.

Terms:
1. ONE key, intent "which restricted vendor prefixes this firm's bucket hosts", valued as a LIST of `systems.json` keys
   (e.g. `restricted_prefix_hosts: ["commonwealth"]`), not a boolean that names one CRM in the key. The selector keeps
   `one()` over rows whose list contains the system token the `.tf` already carries (`:191`).
2. The proposal comes as rule 24 asks (four postulates + word-boundary token census), from `2.0.0_SA_COO~C2` as dell2 ruled;
   the exact spelling is its to propose and this seat accepts any spelling that meets term 1.
3. `python lib/opal_naming.py validate` passes with the new field; `_about.view_fields` names it; the commit-time naming
   gate grades the commit; every value is an existing `systems.json` key.
4. Proof stays dell2's item 5: shared-infra `init` + `plan` succeed with 0 changes to the CRM statements, the break-glass
   role and the firm bucket policy. Any moved resource: STOP, never-widen.
No pipeline tree, bucket or name moves; CLAUDE.md rule 30's "a builder REFUSAL is a missing registry row" is the same shape.

## Reserved to Andrew (unchanged): sitez 058e, 21c5, f0d2, 8ed7, a519 (moot); dell2 01c5, 3cb1, fbb1. Held: dell1 e7f2.
