# cot gold-runner code-review -- Fix Log

Running log of fixes applied from the per-agent reports in this folder (workflow `wf_61db2e92-8e9`).
**One entry per fix, citing the originating report + the commit.** Reviewed top-to-bottom
(chain order), one report at a time.

Legend -- **Verify:** the adversarial-verify verdict (confirmed/plausible) when a critical/high
finding was auto-verified; "ground-truthed" for mediums/lows (no verify agent ran -- validate
against SOURCE before fixing). DISCIPLINE: safe guards (dtype coerce, unguarded-read guard,
fail-loud on systematic/newest failure, observability WARNs) are applied autonomously; a fix
that changes a SERVED tax/AUA/NNA number via cross-script data lineage is a DESIGN ITEM
(flag to the owning exec), NOT an autonomous patch.

---

## FIXES

<!-- ## FIX-001 -- <script>: <one-line> (report N, finding K, <severity>)
- **File:** `<path>` -- `<function>`
- **Defect:** <mechanism -> served/chain impact>
- **Fix:** <what changed>
- **Commit:** `<hash>` -->

---

## DESIGN ITEMS (flagged -- need a cross-script/owner decision, NOT a safe autonomous patch)

---

## Reports reviewed but NO fix applied
(reviewer verdict clean, or a finding refuted / not-actionable on ground-truth)
