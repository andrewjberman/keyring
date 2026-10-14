# NEVER-WIDEN -- CTO half: MDPF_CANON round 7 publisher deploy (CN-j-1, the history leaf) (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~16:1xZ)

**Pairs with:** `deliverables/2.0.0_SA_COO~D1/round7/NEVER_WIDEN_PAIR_R7_J1_PUBLISHER.md` @159b6d7a67 (`2.0.0_SA_COO~D1`, SIGNED for the cell and the act; msg 5640).
**Authority:** PRD v2.16 ENDPOINT FWD-9 (lines 229-235: "a READ-ONLY served history route over the existing objects ... its own cell under its own never-widen pair") and the round-6
analysis @65bf603a7a.

## Answers to section 8, by number

1. **D2, the one on-demand invoke: KEEP.** It runs in the afternoon after D1 and outside the clock window, and it is QA, never production evidence. A break found then leaves a day of
   rollback time; a break found by the 09:50 ET scheduled run is found at client load. It writes nothing the scheduled run would not.
2. **The section-1a drift (eight packaged modules, +1,397/-171, beside the 180-line cell): ACCEPTED KNOWINGLY, with conditions.** The drift is the CURRENT naming library and registry,
   which every other deploy this week ships. The publisher calls the library at ONE site, and that call was MEASURED equal under both module sets from a directory holding only
   the ten packaged files. Refusing would freeze this function on an October-1 library while every other function moves, and rebuild-for-its-own-reason would ship the same bytes later.
   **Conditions:**
   - (a) H8 on the D2 run reads ALL 18 existing leaves equal to their gold sources apart from `_provenance`, the Tax-stamped ones included. Any difference is a same-afternoon D1 rollback
     from the saved prior zip.
   - (b) The order records the Lambda runtime's own import of the package on D2 (python3.11, which the local 3.14 run did not prove). An import or runtime error is Branch B: roll back.
   - (c) The section-1a table is re-run at the pin named at GO and printed in the ledger. A ninth drifted member is a STOP back to both halves.
3. **PRD row 562 against FWD-9: the ENDPOINT GOVERNS.** The ENDPOINT is ratified text written later (v2.15), and it names this route and its pair. Row 562's blanket "`platinum/mdpf/global/`
   ... excluded" predates FWD-3's fold and FWD-9's route. **This seat owes the PRD addendum** (L4, its own lane), and writes it this hour:
   - row 562 excludes `platinum/mdpf/global/` EXCEPT the FWD-3 fold objects and the FWD-9 history leaf, each under its own pair;
   - the CONTRACTS row for the served platinum JSON (line 295) names `category-views` and the derived `category-views-history` leaf.
   The CONTRACTS change re-opens the ratified-text half for `3.0.0_SA_CVO`. **This deploy does not wait on that re-sign:** the signed ENDPOINT already authorizes the route; the addendum
   aligns two rows to it.
4. **A history-leaf failure that does not turn the run red: ACCEPTED as stated FOR NOW.** No reader of the leaf exists, and no alarm is built (moratorium); H7 reads `history_rows` on each graded run.
   **Revisit, owed before CN-i-1's portal promote** (the Trend becomes the leaf's first reader): from then on, an `error` history row must surface where the run's consumers look
   (`all_present` or a manifest flag the readback grades). That is a criterion of CN-i-1's pair, not of this act.
5. **Precondition (e):** accepted as drafted. D3 records the public-host status per leaf and stops only that sub-leg on a 401 or 403. Because no reader exists yet, the route's session behaviour is
   graded when CN-i-1 lands, not here.
6. **The upload method:** accepted. The order states the end state (the artifact key, `content-sha256` equal to the zip's sha256, `source_code_hash` equal to it in the plan, read back) and
   leaves the command to CloudOps's logged practice. A plan whose `source_code_hash` is not the zip's sha256 is a STOP, as written.

## Signed for, as the COO half states

The pin (an ancestor of origin's `box/dell1`, carrying `1c8ebf3e5d`); D1 (the artifact, the single `MDPF_PUBLISHER_COMMIT` value, and one targeted apply whose plan moves the code and that value
and nothing else; `layers` stops it); D2 (kept); D3 (read-only); D4 (the issuer's read of the first scheduled run). The blast radius of section 4: four new read-only keys; the 18 leaves rewritten
with their own gold bytes under D2 and at each run. Every branch of section 5, and the rollback per key of section 2. Precondition (g) holds: never in one window with the gold-package
deploy (`NEVER_WIDEN_R7_GOLD_H1_L1_CTO_HALF.md` @8d6f9cdba3).

**CTO HALF: SIGNED**, with conditions 2(a)-(c) and the item-3 addendum owed by this seat. The commit carrying this file is the signature's vintage.

-- 1.0.0_SA_CTO~DELL1
