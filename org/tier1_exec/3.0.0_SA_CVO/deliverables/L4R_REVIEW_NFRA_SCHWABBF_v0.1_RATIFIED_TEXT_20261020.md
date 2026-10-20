# L4-R review -- NFRA_SCHWABBF PRD v0.1 @ebad019c12, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (laptop), 2026-10-20 ~13:3xZ. Delivered by 1.0.0_SA_CTO msgs 109888 and 109889 (both acked). Half hash
`93998f28b0b1`. **Graded:** ENDPOINT and CONTRACTS of `org/missions/D8/NFRA/NFRA_SCHWABBF/prd/NFRA_SCHWABBF_PRD.md` at ebad019c12 (first
version; no prior to diff).

## Verdict: SIGN

## ENDPOINT against its ratified pin

- **Source:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_SCHWABBF_20261020.md`. Its code block is unchanged between
  649d6624aa (what Andrew was shown) and 2fc743fa91 (after his word): `git diff --ignore-cr-at-eol` shows only the added CONFIRMED section.
- **Andrew's word:** `ANDREW_DIRECT_20261020_130xZ_..._210_MASTERS_OUT.md`, "1.) Yes as written." The record states FWD-7's qualified wait is
  accepted.
- **The PRD block against the source block** (newline-normalised text compare):
  - FWD-1 to FWD-6 are verbatim, except the six `SOURCE` lines, which are dropped. Those are annotations, which this section must not carry.
  - FWD-7's DONE WHEN changes "needs Andrew's word that the wait is accepted" to "ACCEPTED by Andrew 2026-10-20". That records the word the
    source asked for, and rule 27 L2 requires a qualified wait to carry its reason and Andrew's word on the outcome. The dropped parenthetical
    ("today they are absent from its list and a download returns nothing") is a measurement; it now lives in C-SCOPE ("absent from the
    213-master list, download HTTP 204").
- **Operative constraints all present:** FWD-3 "it sends nothing"; FWD-5 "read once at the change and not kept running afterwards"; FWD-4
  "no second form beside it"; FWD-7 "nothing new had to be built". No seat name sits inside the block.

## CONTRACTS, spot-checked against the repo at HEAD

| claim | read | result |
|---|---|---|
| C-NAMES: `address()` returns `s3://opal-data-assets/schwab/<m>/bronze/acc/date=2023-10-17` and silver `.../silver/dim_balance/...` for all three masters | `lib/opal_naming.py address()` run for 08242234, 08335338, 08403355 | all six paths as stated; 08403355 resolves |
| C-KEYFORM: today's key function is `monolith_bronze_key()` at `_monolith_bronze.py:48` | `sed -n 44,52p` | line 48, grammar `schwab/{master}/bronze/{feed}/{YYYYMMDD}/{master}.CRS{YYYYMMDD}.{FEED}.zip` |
| C-MOVE: 21,782 objects = 7,960 + 7,758 + 6,064 | arithmetic | holds |
| C-ONBOARD: three hard-coded master lists | `sdd-daily-pull.ps1:31` ValidateSet; `monolith-daily-schedule.tf:34` `local.si2_daily`; IAM enumeration in `iam.tf` and `monolith-iam.tf` | all three exist; a FOURTH exists (carried item 1) |

## Carried, not grounds

1. **C-ONBOARD misses a fourth master list, and following it as written breaks rule 30.** `monolith-daily-schedule.tf:49-51` holds
   `si2_daily_builder_named = toset(["08403355"])`. The rule's name is builder output only for masters in that set; any other master gets
   the typed `"canonical-schwab-si2-${each.key}-daily-pull"` (:66). A fifth master added by "one map entry" alone gets a hand-typed name
   for a NEW resource, which rule 30 forbids. The proof line ("a dry plan that adds a fourth map entry and changes only that master's
   schedule and IAM statement") would pass on exactly that outcome. Suggested fix for the onboarding cell: invert the set to name the two
   LEGACY masters (08335338, 08242234), so every master not in it is builder-named by default; the proof then also checks the new rule's
   name is `name()` output.
2. **A ratified counterpart PRD carries the grammar this project retires, and CONTRACTS does not name the supersession.**
   `docs/architecture/OPAL_ASSETS_CONSOLIDATION_PRD.md` (RATIFIED) :36 records `{master}/bronze/{type}/{YYYYMMDD}/` as Andrew's verbatim
   grammar of 2026-07-13, and :477 sets the opal-data-assets target in that form; `docs/architecture/OPAL_ASSETS_PRD.md:494` does the same.
   Andrew's later words (2026-10-19 "canonical LGIC_NAMING path form"; 2026-10-20 call 2 "Yes") supersede them, so the substance agrees
   with Andrew. Two consequences for the cut:
   - C-KEYFORM or C-MOVE should name the superseded lines and their records, so a reader of either PRD is not sent to the old grammar.
   - C-READERS' proof ("zero old-form hits outside the move script and this PRD") cannot pass while those PRD lines stand. Scope the
     census to code, deployed copies, IAM and contracts, with documents listed separately; or have each PRD's owner add a superseded-by line.
3. **Decision 1 (move first, then backfill) is safe only while Schwab's floor holds.** The two reads (2026-10-19 21:21Z, 2026-10-20 08:50Z)
   both returned 2023-10-17 across an Eastern roll, so the window does not appear to roll daily. The endpoint source itself names the risk
   ("the oldest 0824 days are lost one per business day until pulled"). The backfill cell should re-read the floor at its cut. If the floor
   has moved, the order of cells 3 and 4 is a call for the CTO, not a silent loss.
4. **Minor:** the ENDPOINT section opens with a line of history ("CONFIRMED by Andrew ... The source, verbatim from step 2, is ..."), and
   2fc743fa91 converted the endpoint source to CRLF (100 lines). Neither changes text; a byte-level citation of the source should use the
   newline-normalised form.

-- 3.0.0_SA_CVO
