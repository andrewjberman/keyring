# AMGT_RESAPP round 104, workstream AIFILL -- never-widen pair, the AI fill's store, read grant and redeploy (FWD-41) -- the COO half

**Author:** `2.0.0_SA_COO~R2`. **Status: SIGNED at the close of the build cells, before any act below runs.**
owed by `1.0.0_SA_CTO~DELL1` at `ledger/NEVER_WIDEN_ROUND104_AIFILL_STORE_GRANT_REDEPLOY_CTO_HALF.md`, under a heading naming this act.
**Sources:** decomposition `decompositions/AMGT_RESAPP_AIFILL_DECOMP.md` s.5 items 1 and 2; PRD v0.44 FWD-41; the CTO's page approval, msg 5283
(`ledger/CTO_APPROVAL_PORTAL_CAND_AIFILL_BLOCKS_20261014.md`: "the served ai_fill (fa-7) ships under its own pair, with every stored address as builder output").
**Built and merged (all LOCAL, nothing applied):** fa-9 `957b04a764` (the generated constant `AI_FILL_GOLD_PREFIX = 'amgt/harvest/gold/ai_fill/'`), fa-7 `cd31b97501` (the serve: `read_ai_fill`, the
`/thesis` bundle's `ai_fill`), fa-6 `d5de26b4a0` (the store address and the run command), fa-1 to fa-5 (the producer); amendment 2 of the three builders `d68a6796ef`, `b454de8e3a`, `008251080f`.
**Measured at the cut:** 2026-10-14 ~00:05Z to 00:20Z, read-only.

## THE ACT

Four steps in this order, each read back before the next:

1. **IAM (additive).** ADD `amgt/harvest/gold/ai_fill/` to `local.scoped_amgt_pool_prefixes` in `infra/aws/terraform/harvest/scoped-amgt-api.tf`, as the generator's printed value (`_hp.AI_FILL_GOLD_PREFIX`,
   trailing slash mandatory), so it lands on BOTH limbs of `aws_iam_role_policy.scoped_amgt_api_grants` (`s3:GetObject` on `<bucket>/<prefix>*` and the `s3:ListBucket` prefix condition). A targeted `safe-apply` of that one
   resource; a live re-read shows the entry present on both limbs and every other resource and prefix byte-equal.
2. **Store.** The producer writes the documents:
   - (a) ONE name first: `python -m lib.research.aifill.run --key AMD_US_Equity --to-s3 --confirm-write` writes exactly one key; `store.read_document` returns the document EQUAL to the one written; the issuer reads its five
     blocks once (source class, text, citations).
   - (b) Only after (a) reads back: the remaining resolved names, one `run --to-s3 --confirm-write` per name, four at a time, each key written by that name's run only. Population: the 95 resolved names of the V1
     census (`deliverables/0.9.0_WK_AMGT_RESAPP~408/census_sections.json`: 95 resolved, 93 with an exact-key pack, 2 under the slash-safe key, 105 pack prefixes). A document that fails `contract.validate_document` is never written
     (the command refuses).
3. **Redeploy.** `opal-amgt-scoped-api` is redeployed carrying fa-7's `scoped_amgt.py` and the regenerated `_harvest_prefixes.py`, by `0.7.0_AE_CloudOps~RA1`, ONE applier at a time: only after `2.0.0_SA_COO~R1`'s round-104
   apply has settled and read back (the function was last modified 2026-10-14T00:07:07Z by that line of work), from a pin that includes `cd31b97501`, `957b04a764` and `~R1`'s merged blobs; the admission-table tool names the packaged
   members; the drain's pair names each by blob.
4. **Verify (read-only).** The `/thesis` route for `AMD_US_Equity` serves `ai_fill.status == SERVED` with five blocks EQUAL to the stored document; a name with no stored document serves `ABSENT` with `read_completed` true; for
   three names every other key of the `/thesis` body is byte-equal pre and post; the `/overlay` route's body and handler time are unchanged (fa-7 adds no read to any overlay path: check arm `overlay_untouched`, re-read at the apply).

The portal page (`cand/dell1/aifill-blocks` @85d5749f, APPROVED by the CTO) lands AFTER step 4 reads back, as the CTO ruled ("live together with fa-7"); that landing is its own act under the CTO's approval and is not part of this half.

## BLAST RADIUS -- what the act MAY move, and nothing else

- **(B1) New objects:** at most 95 keys, each `amgt/harvest/gold/ai_fill/security_key=<slash-safe key>/ai_fill.json`. The prefix is EMPTY at the cut (`list-objects-v2 --max-keys 5` returned KeyCount 0 at ~00:05Z). A re-run of one name overwrites
  that name's own key (a derived document, the producer's alone).
- **(B2) The adapter's inline policy `opal-amgt-scoped-api-grants`:** pre sha16 `77c69f8359764942` (canonical JSON, sorted keys), 7 statements. The `ReadThePoolPrefixesTheAdapterReads` statement carries 34 resources and gains exactly
  one (`.../amgt/harvest/gold/ai_fill/*`); the `ListOnlyThePoolPrefixes...` condition list gains exactly one prefix; the other five statements are byte-equal; the statement count stays 7. Pre values are re-read at the apply (AC0).
- **(B3) The adapter's code:** CodeSha256 `Wkt48Y6vf4o4Dhyb9gVkfaf9IIJ75ThoI+hiMUoGrS4=`, CodeSize 42,142,989, LastModified 2026-10-14T00:07:07Z at the cut (re-read at the apply: these are `~R1`'s, not final), and one new artifact version.
- **(B4) The served `/thesis` body:** gains the key `ai_fill`, additive; every existing key is byte-equal. The `/overlay` body is unchanged.
- **Box-side vendor use (not an S3 matter, stated):** the producer calls the Anthropic Messages API with web search, about four calls per name (two searches each, about 21,000 input tokens per call), measured at about 13 cents per call
  at the module's rates: an estimate of at most 55 USD for 95 names. Egress is open on this channel; no Bloomberg call.

**NOT moved (asserted):**
- any existing object in `opal-data-harvest` (no key outside `amgt/harvest/gold/ai_fill/` is written);
- the overlay, peers, coverage, versions and ledger routes;
- `opal-amgt-scoped-api-role`'s trust policy and every other statement of its policy;
- the portal repository, DEV and PROD;
- any scheduled task: the disabled site Z tasks `OpalResearch-ExecManagement` and `OpalResearch-FilingsAnalyzer` stay disabled;
- any secret; any other function.

## WRITER CENSUS -- the act's own write set, one call deeper

- **The prefix's writers:** exactly 1 module path, `lib/research/aifill/store.py write_document`, reached only by `run.py --to-s3 --confirm-write`. A grep of `lib/` for the prefix constant `AI_FILL_GOLD_PREFIX` finds the reader
  (`scoped_amgt.py`), the generator and its pin test; no other writer. The dry run (`--to-s3` alone) writes nothing (check arm, `main_dry_run`).
- **The policy's writers this round:** 1, this act's targeted apply. The file `scoped-amgt-api.tf` was last changed 2026-10-08 (`ddc917a52d`).
- **The artifact key's writers:** 2, serialized by the one-applier rule: `~R1`'s round-104 apply, then this act's redeploy.
- **The `run` command's other effects:** none: it reads the two served routes (GET), calls the model, writes a local file and, with both flags, one S3 object per name.

## EXPECTED OUTCOME, both branches

- **Branch A (policy re-read as stated; AMD's stored document reads back EQUAL; the rest of the names written; the redeploy reads back; the `/thesis` verification as stated):** FWD-41's serve and store are live and the
  census (round 105) can be taken from the served route.
- **Branch B (any mismatch, a served key other than `ai_fill` differs, the overlay handler time moves, or an unexpected key appears under the prefix):** ROLLBACK below, in reverse order. No reader is ever left with neither grant
  (the grant is only ever added by this act; the reader added by step 3 is harmless without it: an AccessDenied read answers `ABSENT` with `read_completed` false).

## PER-KEY ROLLBACK

- **Code:** `copy_object` from the AC pre VersionId, then the targeted apply; CodeSha256 must equal the pre value; the code is also reverted by a NEW commit.
- **Policy:** remove the entry, targeted apply, live re-read shows it absent. Additive, so it may also stay.
- **Store objects:** NOT removed by this act: an S3 delete needs a human word. After the code rollback nothing reads them; a wrong document is overwritten by a corrected run.

## NOT COVERED

This half does not cover, and the act may not perform:
- any S3 delete;
- any key outside `amgt/harvest/gold/ai_fill/`;
- any grant other than the one entry named;
- any function other than `opal-amgt-scoped-api`;
- step 2(b) before 2(a) reads back; step 3 before `~R1`'s round-104 apply has read back;
- the portal landing (its own act);
- a schedule change or any use of Bloomberg.

**Signature (COO):** signed `2.0.0_SA_COO~R2`, 2026-10-14, at the close of the build cells (the commit carrying this file is the signature's vintage).

## ADDENDUM 1 (2026-10-14 ~01:3xZ, `2.0.0_SA_COO~R2`) -- the redeploy's pin and its packaged members, named by blob; steps 1 and 2 as run

This addendum changes nothing in the act and fills the one thing step 3 needs and the half left open: the pin and the packaged-member table. `AMGT-ar-3` stops before upload on any member not named here.

**THE PIN: `0447f2df38`** (a `box/dell1` commit; it carries fa-7's merge `cd31b97501` and every cell of the round; `2.0.0_SA_COO~R1`'s `AMGT-bk-2` is complete and its pin `d7a79c766a` is the live function's). The build is cut from a DETACHED worktree at exactly that hash.
`python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_admission_table.py 0447f2df38 --pin d7a79c766a` reads, run by the issuer at the cut: **members whose bytes differ: 8**.

| member | live pin blob | this pin's blob | delta | loaded by the handler |
|---|---|---|---|---|
| `lib/research/api/scoped_amgt.py` | `351f9a1d7a8a` | `1f5de89912e5` | +225 -0 (fa-7's region and its one wiring line; no other line moves) | YES |
| `lib/research/aifill/block_identity_description.py` | ABSENT | `c70fe05a8c78` | +210 | no |
| `lib/research/aifill/block_mgmt_bio.py` | ABSENT | `fef074d4f30e` | +252 | no |
| `lib/research/aifill/block_mgmt_recent.py` | ABSENT | `f1367c7f97e2` | +251 | no |
| `lib/research/aifill/block_mgmt_team_view.py` | ABSENT | `310f807c43e1` | +154 | no |
| `lib/research/aifill/block_thesis_pillars.py` | ABSENT | `2aea75e0c7c7` | +198 | no |
| `lib/research/aifill/run.py` | ABSENT | `c6a8e343ff3a` | +133 | no |
| `lib/research/aifill/store.py` | ABSENT | `011f1a8972ad` | +98 | no |

The signed half named `scoped_amgt.py` and `_harvest_prefixes.py`. **`_harvest_prefixes.py` is NOT in the table: it is byte-equal at the live pin and at this pin** (the generated `AI_FILL_GOLD_PREFIX` landed in `d7a79c766a` already: `git show` of both reads it once), and
the first five `aifill` modules (`__init__`, `contract`, `orchestrate`, `model`, `inputs`) are likewise already live. The seven `aifill` rows are packaged by the build's tree walk and never imported by `scoped_amgt.py`; they add no reader, no grant and no served byte
(the handler loads `scoped_amgt.py` and the generated prefixes only). The build's own content diff against the live package is the authority: any member beyond these eight, or another blob, is a STOP BEFORE UPLOAD and returns to the issuer.

**Steps 1 and 2 as run (for the record; the half's expectations were met):**
1. **Step 1, `AMGT-ar-1`** (RA1, applied 00:38:18Z to 00:39:53Z, ledger `amgt-resapp-r104-ar1-aifill-grant-dell1` closed): 1 changed in place; GetObject resources 34 to 35, ListBucket prefixes 34 to 35; `check_ar1_grant.py` YES 7 of 7 (the issuer re-ran it from its own seat); with the one entry stripped from each limb the policy is byte-equal to the pre-act policy (`77c69f8359764942`); post sha16 `b50b9248dbcc7d02`.
2. **Step 2:** (a) AMD stored first and read back EQUAL (`store.read_document`, validated). (b) The 94 other names: 93 stored by the batch, 1 (`WALMEX*_MM_Equity`, whose `*` is not a legal Windows file name for the command's `--out`) stored by a direct run without `--out`, then 5 names re-drawn after a block hit the token budget or had no citable source, then AMD (stored before the retry rule existed) and COST re-drawn for the same reason. **Read back through the store reader: 95 of 95 present, valid, ASCII, key-matching** (`round104/store_readback_census.json`). Spend, from the documents' recorded token counts at the module's rates: batch 37.53 USD, re-draw 2.95, AMD 0.40, WALMEX 0.56 + 0.80 for the last two re-draws = 42.24 USD for the stored documents; the second live trial run (before the pair's step 2) cost 0.52; the first trial run, the diagnostic probes of single blocks and the draws a retry discarded wrote no document or recorded no tokens and were NOT metered, so the total is not stated beyond '42.24 USD metered plus a few unmetered trial calls'. The 75 USD stop was never reached: every projection was under it (the batch's own final projection basis: 37.53 spent over 94 names). 95 keys written, none outside `amgt/harvest/gold/ai_fill/`; no delete.

**Signature (COO):** signed `2.0.0_SA_COO~R2`, 2026-10-14, at the close of step 2 (the commit carrying this addendum is the signature's vintage). Owed: the CTO's concurrence with this addendum, appended to the CTO half.
