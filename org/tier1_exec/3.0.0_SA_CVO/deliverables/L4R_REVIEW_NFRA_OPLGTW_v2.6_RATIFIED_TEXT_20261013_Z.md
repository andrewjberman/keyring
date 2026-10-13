# L4-R review, NFRA_OPLGTW PRD v2.6, ratified-text half -- SIGN (3.0.0_SA_CVO~Z, 2026-10-13 ~20:4xZ)

**Asked by** `1.0.0_SA_CTO~Z` msgs 33734 and 33737 (both acked).

**Bytes reviewed:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @713305ee56, where the working tree equals the
pin. The diff is `git diff 1825ea3472 713305ee56` read whole: from v2.2, this seat's last signed pin, through v2.6. It
covers:
- the v2.3 addendum (the Bloomberg account mirrors Andrew's principal, plus the Opal-users-only gate);
- the v2.4 addendum (C7 names two mail-bearer holders);
- the v2.5 addendum (C4 adds `copy_site_file_to_s3`);
- the v2.6 addendum, with FWD-20 and FWD-21 in ENDPOINT.

Half hash at review: `4e2c2b77e9f3`.

## Sources read at their pins

- **v2.3 quotes.** `ANDREW_DIRECT_20261009_032xZ_OPAL_GATEWAY_BBG_MIRRORS_OPALGATEWAY.md` carries "opal-gateway-bbg should be an
  exact copy of opal-gateway for now ...". `ANDREW_DIRECT_20261009_033xZ_BBG_CONCIERGE_OPAL_USERS_ONLY_GATE.md:8` carries "it
  should only accept inquiries from opal capital users ... should not even respond at all". Both match.
- **v2.4 and v2.5.** These record widenings this seat already signed as never-widen halves: `commassist` @c348b51df9 and
  `copy_site_file_to_s3` @9b6003cd3b. The C4 text matches the signed half: one prefix, `IfNoneMatch`, 50 MiB, and callers
  already holding `write_files`.
- **FWD-20's quote.** `DIRECTION_SITEZ_20261013.md:51-52` and `:63` ("what backfill or scope out those tools work").
  Matches.
- **FWD-21's widening.** It rests on Andrew's call 8 in
  `ANDREW_DIRECT_20261013_200xZ_NINE_OPEN_CALLS_ANSWERED_FIRMBKTS_DEMQUE_BRIEF_HARVEST.md:5`: "Yes that is available for
  opal users only for now, which will be managed via opalgateway entitlements. There should be no undue holds on that in the
  interim ...".
  - The call it answers was the servable list's open line: does his Bloomberg word also lift the V1 derived-only rule for raw?
  - Servable list v4 @7e0da2dfee records it: all 24 prefixes SERVE to Opal principals, raw included, and a non-Opal
    principal is refused on every prefix.
  - FWD-21's ACCEPT carries this at its width, neither wider nor narrower.

## Verdict: SIGN

- **FWD-20** is a read with a measured or inferred claim on every value. It is read live from the schedule, never typed,
  and nothing rides on it (the moratorium holds).
- **FWD-21** has a real principal's driven call as its positive arm, a non-Opal refusal as its negative arm, and a
  principal census with its denominator.
- **Contract items 1-3** keep C2's owner gate and v2.3's Opal-users-only rule. They type no name (rule 30) and keep one
  grant writer.
- **No seat name** appears in the ENDPOINT section's new text.

## Owed elsewhere: two counterpart PRDs now lag this one

Neither item is grounds against this half. This half is the one that carries Andrew's latest word, and both fixes belong
to the counterparts, which `1.0.0_SA_CTO~Z` owns.

1. **NFRA_MCPINDEX v0.9 is behind call 8.** This seat signed it at ~19:4xZ, before call 8 (~20:0xZ).
   - Its FWD-21 ACCEPT cuts "one catalog row per SERVE prefix in the servable-prefix list v3 @0b2778751a" (11 rows), and
     says "a WITHHOLD prefix gets no data row".
   - Its v0.9 addendum item 1 says "the V1 rule holds: derived layers and article links, never raw publisher text".
   - This PRD's FWD-21 says "NFRA_MCPINDEX catalogs the prefixes", meaning all 24 per v4. Andrew names the two projects
     together for the policy design.
   - **Fix:** an MCPINDEX v0.10 addendum that re-pins FWD-21 to v4 @7e0da2dfee and lifts the V1 line for Opal principals.
     That is an ENDPOINT change, so this seat re-signs it. Until then, MCPINDEX's round 10 would cut 11 rows against
     Andrew's "no undue holds".
2. **NFRA_MCPORTAL has no FWD-21, and its FWD-20 shows no cadence or depth.**
   - Contract item 1 says "Display and control are MC Portal's FWD-20 and FWD-21". The MCPORTAL PRD @cdb5ff66b1 has
     FWD-20 (channels, tools, indexes, entitlements) and no FWD-21.
   - The direction's Z2 calls FWD-21 "a new PRD addendum" not yet written.
   - FWD-20 here ("NFRA_MCPORTAL can display the read") and MCPINDEX FWD-20's depth and freshness therefore have no
     consumer outcome on MC Portal's side.
   - **Fix:** an MCPORTAL addendum that adds FWD-21 (control) and puts cadence, depth and freshness on FWD-20, or on a new
     outcome.

## Carried (not grounds)

3. **"Refused on every prefix", proved on two.** FWD-21's DONE WHEN says a non-Opal principal is refused on every prefix.
   Its PROOF tests `packs/` and `wsj/harvest/`. A `simulate-principal-policy` over all 24 prefix ARNs, for one non-Opal
   principal, closes the quantifier at little cost. The battery can carry it.
4. **The brief half** routes to `2.0.0_SA_COO~ZB` (no live CRO). The v2.6 Sign-off accepts the CRO's alignment reports as
   written, which is PROPORTIONATE SIGN-OFF. That discrepancy is the CTO's to settle.

-- 3.0.0_SA_CVO~Z
