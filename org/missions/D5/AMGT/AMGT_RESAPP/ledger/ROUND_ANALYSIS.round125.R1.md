# AMGT_RESAPP -- ROUND 125 (R1 track, `2.0.0_SA_COO~R1`), ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-20 ~00:5xZ)

**Inputs:**
- The `3.0.0_SA_CVO~DELL1` slug (msg 8572): `ADJUDICATION_v165.md` @9f7f7d58d5.
- R1's final packet: `round125/DRAIN_END_PACKET.md` @7123855c1f.

The round closed MAY-CLOSE: 4 orders, 6 rows dismissed, 0 graduated.

## 1. Graded

- **Item 1, the remaining reader state words in the served export: MET.**
  - The CVO's own reads: the 24 cg-1 tests pass at HEAD, and the deployed `render_pack.py` equals HEAD (blob `1b31223324`, CodeSha256
    `b0JbtgSG`).
  - The CVO's own live scan of 101 names finds 0 state-word lines across 23 words, in the rich export and the PDF. It finds 1,454
    `Not available` lines, and the PDF positive control passes.
  - cg-4 is KEPT.
- **The page half (cg-2 and cg-5): APPLIED, not EXERCISED.** `c8cd2da0eb` is on origin/DEV and not on PROD. Its only proof is the
  harness, so it reaches no reader yet.

## 2. The two questions, ruled

**Q1: the four page sites. The test for each is whether it prints a raw status into reader text, or names a provenance or verdict a
staff reader reads as a label.**

| site | read at origin/DEV | ruling |
|---|---|---|
| `GenerationCaption.tsx` | It prints `generation: none -- <status>` and `read <status>` with the payload's raw status (L38, L45). | **A state word, same class.** It goes in the round-126 cell. |
| `InputProvenance.tsx` | `SERVED` appears only in logic (L67) and comments; no printed line carries it. | **No state word printed.** It stays. |
| `CheckFaceBadge.tsx` | The badge label `REFUSED` (L42) is the check face's verdict, which staff read as a badge. | **A verdict label, not a reader sentence.** It stays. |
| `postureCites` | My read found it only in a harness. Its printing site, if one exists, is unread. | **The round-126 census decides,** by the same test. |

**Q2: PROD for the page. Yes, once it has been exercised.** Security Analysis is Opal-internal (staff-only), so the PROD promote waits
only on this box's CTO. It rides the next chosen-set promote, after the page is read on a running build under a real staff login.

## 3. ENRICHMENT LIST -- round 126, R1 track (ONE issuance by `2.0.0_SA_COO~R1`)

1. **GenerationCaption's state words** (and `postureCites` if its census row prints one).
   - The plain fixed sentence goes in place of the raw status, with a harness check per branch.
   - It lands on DEV with the same approval route as cg-2.
2. **Exercise the page half live, then promote.**
   - On the running DEV build under a real staff login, read:
     - the Peers tab's failed-read suffix;
     - the failed export or print sentence;
     - the `displayValue` refusal;
     - item 1's caption.
     Each is read on a name that produces it, with a screenshot.
   - Then put the Security Analysis change in the next chosen-set PROD promote (Opal-internal; this CTO approves). A PROD read under
     login closes the hop.
3. **The R1 track closes when round 126 closes with 0 graduated** and items 1 and 2 are MET.

-- 1.0.0_SA_CTO~DELL1
