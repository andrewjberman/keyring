# L4-R review -- NFRA_SCHWABBF PRD v0.2 @6c3ded061f, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (laptop), 2026-10-20 ~14:4xZ. Delivered by 1.0.0_SA_CTO msgs 109893 and 109894 (both acked). Half hash
`7449c7f1e75c`. **Graded:** the whole diff ebad019c12 -> 6c3ded061f (v0.1 was signed by this seat at 389e038b1b). One ENDPOINT change,
FWD-8 appended (FWD-1 to FWD-7 byte-unchanged), plus a paragraph under the block; one CONTRACTS row added, C-ALONGSIDE; OPEN AT ANDREW,
CELL CANDIDATES and the change log extended.

## Verdict: REFUSE

**Reason (one line):** FWD-8 is not ratified text: Andrew has not confirmed its DONE WHEN, and the PRD itself lists "Confirm FWD-8" under
OPEN AT ANDREW.

- **What Andrew said** (`ANDREW_DIRECT_20261020_134xZ_ALONGSIDE_SCHWAB_CREDENTIALS_AND_ALONGSIDE_PULLER.md`): "an alongside-specific schwab
  ec2 daily puller. this is how we can backfill the schwab accounts for Cottonwood"; "it should be exact same setup and logic as already
  exists with the 49 schwab box"; "I will need to RDP into the EC2 box". That is the order for the box. The DONE WHEN and ACCEPT lines of
  FWD-8 are the CTO's projection of it, and he has not seen them.
- **No confirmation exists:** the CTO's deliverables and the NFRA_SCHWABBF tree carry no record after 13:5xZ, and `open-calls` holds no
  row for FWD-8. The three NFRA_SCHWABBF rows (b333, 3c35, 3cd2) are CLOSED and cover FWD-1 to FWD-7 only.
- **The same ground as this seat's ADVI_COTBOOKS refusals of v0.1 and v0.2** (2026-10-17: endpoint unconfirmed). FWD-1 to FWD-7 still
  stand as ratified; this refusal is about FWD-8 alone.
- **What clears it:** one open call to Andrew with FWD-8's three lines as written, and his word recorded. A bump that changes only the
  record line re-opens nothing else; this seat signs on the confirmed text.
- **What the refusal does NOT block:** round 1's six orders were issued under v0.1 (5f1ad506a4), and LIMB 6 grades only a newly added
  order. The Alongside workstream's new orders wait, which is where FWD-8's confirmation belongs.

## For the re-sign (read now so the next pass is one step)

1. **FWD-7 and FWD-8 can put two writers on one Cottonwood prefix.** FWD-7 still names "a Cottonwood account group" opened to Opal's
   existing login; FWD-8 lands the same four masters through the Alongside box. Both write `address('schwab', <m>, 'bronze', ...)`. If
   Schwab later entitles the 49F login to a master the Alongside box already pulls, C-ONBOARD adds it to the 49F map and two boxes write
   the same keys. The record says FWD-7's premise "is superseded for Cottonwood"; the PRD keeps FWD-7 naming Cottonwood. Either FWD-7
   drops the word Cottonwood, or a contract names ONE writer per master (C-ALONGSIDE's list excludes the four from the 49F map).
2. **FWD-8's reach is unmeasured, and the outcome does not say what follows if it fails.** C-ALONGSIDE says the Alongside login's
   entitlement list is unread until the session exists, and "a master it does not see is named". FWD-8's DONE WHEN assumes all four. If
   one is absent, the outcome is unreachable by working. Andrew may want that branch stated on the outcome when he confirms it (a named
   master that the login does not see is reported, and it is his call to Cottonwood).
3. **"Exact copy" carries the v0.1 carried item 1.** The 49F root's `si2_daily_builder_named` set
   (`monolith-daily-schedule.tf`:49-51) types rule names for masters outside it. In a copy labelled Alongside, every rule is new, so
   every name must be builder output from the first apply (rule 30); a verbatim copy of that ternary would type them.
4. **Minor:** the paragraph under the ENDPOINT block ("FWD-8 was ADDED at v0.2 on Andrew-direct ...") is history inside the section; it
   belongs in the change log.

-- 3.0.0_SA_CVO
