# AMGT_RESAPP -- ROUND 53 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~16:4xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27272, *"L10 slug AMGT_RESAPP round 53 @d4fe6127ee"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v63.md` (read to EOF, 6,899 B). Issuer packet: `round53/DRAIN_END_PACKET.md` @`9a1199bbac`.

**Round 53 is CLOSED:** 4 of 4 terminal; `Z-S318` and `Z-W191-S1` GRADUATED; `Z-S319` carried ARMED with an interim limb; 0 judgment
criteria. **The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **ac-3, the slash-key window: landed and SOUND.**
  - 40 of 40 raw-slash objects were copied to their encoded keys; the raw objects are kept.
  - The build `/QP4upEV...` is live (15:22:01Z).
  - `/timeline` serves `publishers_found_codes` (273 of 273).
  - **The CVO's own read of AC3's post-failure re-scope:**
    - the amended check moves 0 of 6 bodies;
    - its negative arm (the rewrite disabled) moves 6 of 6;
    - all 12 rewrites are `*_read` path strings (10 `object_key`, 2 `management_read.reason`), none of them data.
  - **BP/_LN and NG/_LN read the same data at the encoded keys.**
- **ac-4:** `filings/v1` now reads through `slash_safe_key` (the last raw-path reader).
- **ac-1:** FWD-30's grader reads the displayed figure. At close, 95 of 96 names are value-equal. The one NOT_OK is TSM
  `CURR_ENTP_VAL`, whose upstream is AMGT_CORPUS `Z-S69`.
- **ac-2:** STOP. It is the verbatim gate working as designed (`Z-S316`, this seat's 13:49Z ruling).

## 2. RULINGS

1. **"Show the positive arm before the cut" is ADOPTED as DISCIPLINE, not as a new gate.** The CVO counts three instances in this span
   of a check whose comparand embedded the thing the act moves: `Z-S311`, FWD-30's plants, and ac-3 AC3.
   - Where a check compares a before and after that the act is DESIGNED to change in part, the COO half shows, at the cut, the check
     PASSING on a simulated correct post-state as well as FAILING at base.
   - This binds COO halves and this seat's halves, by reading.
   - A mechanical limb in `to-pipeline-gate` is NOT built. CLAUDE.md's "do not manufacture friction" means proposing is legal and
     implementing a new gate needs Andrew's ask.
2. **`Z-S319`'s interim limb is ADOPTED:** the COO half of every RESAPP build pair carries "head-object `content-sha256` equals the local
   sha" as an act-start limb until round 54's repair lands. Served output is unaffected (Lambda deploys the object VERSION). It stays
   ARMED because a corrupted hash can make a later apply read 0-diff on changed code.
3. **FWD-30's last NOT_OK is upstream:** TSM `CURR_ENTP_VAL` waits on AMGT_CORPUS round 25 (`Z-S69`, the denomination census and a
   paired re-derive). The grader re-runs after that lands; no RESAPP cell chases it.

## 3. FWD GRADES

- **REALIZED:** FWD-9, 13, 24, 25, 26 hold. FWD-21..29 are RE-HOMED to DSGN.
- **FWD-30:** value-equal on 95 of 96 names (TSM is the upstream exception). The person-act clause (Adam's forward) is unmeasured.
- **FWD-18 (the driver chart):** ASML's chart is SERVED from the filing branch. It is graded REALIZED at the next FWD sweep, read on
  the page.
- The other outcomes are as round 52.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~Z` cuts for round 54 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **Census of non-verbatim served D-1 sentences**, per name | LOCAL read | It counts sentences served with `quoted_spans []` or `quote_method none-found`. That count is the input to cell 2's pair. |
| 2 | **The compliance act:** remove the non-verbatim sentences from the served D-1 documents | WORLD, pair | It follows cell 1. The expected diff is only the sentences cell 1 names; span-carrying sentences are byte-equal. The predecessor-code diff is required. |
| 3 | **The `Z-S319` repair:** the three build scripts (`build-and-upload-scoped-amgt.sh:742`, `-print-deps-layer.sh:79`, `build-and-upload.sh:29`) take chatter-axis's fixed shape (no path conversion, plus a refusing read-back) | LOCAL | The AC plants a mangled sha, and the build refuses. |
| 4 | **The FWD-30 re-run**, after AMGT_CORPUS round 25's re-derive | LOCAL read | 96 of 96 is the target, with TSM's currency fixed upstream. |

**Fan-out:** 1 and 3 are independent. 2 follows 1. 4 follows the external CORPUS act.

## 5. ACTS ONLY ANDREW CAN DO (cited)

- The portal PROD promotion [CLAUDE.md Portal].
- Adam's forward of the export (FWD-30's ACCEPT) [PRD FWD-30].

## Compiler Tools

- The CVO's v63: the live CodeSha256, the re-run of `ac_3_served.py` with and without the rewrite, and its walk of every `*_read`
  subtree.
- The packet's section 6.

This seat ran no new instrument.
