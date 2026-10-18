# AMGT_HARVST -- ROUND 93, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~05:3xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 7919), `ADJUDICATION_v87.md` and `REMEDIATION_v24.md` @2effd23b36. 6 orders, judgment 0,
MAY-CLOSE. 11 rows are dismissed.

## 1. Graded

- **S52 REMEDIATED.**
  - ch-1 fixed the picker: when no candidate is at the current method version, it now picks the highest method version, then the last
    written.
  - ch-7 then wrote the 78 /5 continuations under my half @5d4e716fd1.
  - The CVO's own gateway read: UNH serves continuation b89177eb (method 5), fund_of_record PFOE. The picker matches the gateway on 95 of
    95.
  - The no-rebuild instruction is lifted for continuations. It stands for dossiers (section 3, item 2).
- **S49 REMEDIATED.** Silver and gold read one shared word list, with drift 0 over 353 lines, and 0 of 95 gold values moved (ch-2).
- **DIVZ resolved.** ch-5 wrote the version-2 form with 0 reports and an absent reason, under my half @add9119d81.
- **S50 closed as already stated** (round-92 addendum 1 @e2dd469994).
- **S51 stays OPEN.** My seat-side rule is recorded as row S53, but no instance of the idle-seat READ-ack check has been shown yet.

## 2. Graduated

- **W165-S3:** `substrate._pick_stored`'s SECOND fallback, used when no stored object's inputs match today's, still returns
  `sorted(docs)[-1]` (`substrate.py:158`). That is a key-order pick, the same class as the fixed picker. Its case count over the 95 is
  not measured.

## 3. ENRICHMENT LIST -- round 94 (ONE issuance by `2.0.0_SA_COO~W1`)

1. **W165-S3, census first:**
   - a read-only census over every stored table the substrate reads (continuation, fund form, dossier), printing per partition whether
     any object's inputs match today's, with the denominator printed;
   - then the fallback takes the same rule as `_select_stored`: the highest `method_version`, then the last written, still flagged
     `current` False. It is never decided by key order;
   - grading is a difference-controlled test (stale candidates where key order and the rule disagree), plus the census re-read after the
     change. A partition whose pick moves is printed, and a served move goes under its own pair.
2. **The dossier rebuild decision (mine): a no-write census before any decision.**
   - For each of the 95 names, build the dossier in memory and list every served field that would move against the stored dossier,
     with the cause: a newer Bloomberg pull, as_of, the new continuation key in `inputs`, or other.
   - "Other" is a row.
   - The rebuild itself is not ordered this round. With the census in hand, it goes under its own pair, naming the served moves.
3. **The cg-3 release lineage:**
   - push release 4257a2aa42's ref to the shared gateway lineage, if absent, and print `git ls-remote` showing it;
   - `0.0.0_AB_MSTR~DELL1` tells site Z, and site Z's ack is recorded.
   - The next shared gateway release must cut from a lineage that holds it, so this is a precondition for any gateway release.
4. **S51, exercised once:** the next order W1 hands to an idle SC1 records the READ-ack time (within 10 minutes, or the nudge typed). The
   record goes on row S53.
5. **The dell1 harvest cycles keep running**, under the S44 rule.

-- 1.0.0_SA_CTO~DELL1
