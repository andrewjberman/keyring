# DSGN_AMGTV1 -- ROUND 22 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-02 ~08:1xZ

**Input:** CVO~Z slug msg 28302, `surprise-channel/adjudications/ADJUDICATION_v20.md` @2345144b54 (3 of 3 terminal; open 0,
ARMED 0). PRD v0.8 is SIGNED (@e491b51258). Round-22 close @863ff402ec. The candidate merged onto remote DEV is portal
`419ef41d`, LOCAL. This seat's review is APPROVED (@20459845ef). **Round 22 is CLOSED.**

## 1. WHAT THE ROUND DELIVERED (on DEV, not PROD)

Read by CVO~Z on the PNGs of walk `20261002T072805Z`:
- the Lusha key and `domains.json` are gone from Exec;
- the Peers field codes are gone;
- the Peers subject row equals the header (BA 196.80 / 187,188).

None of it is on PROD (`b3a1d8a6`) until Andrew's promote word.

## 2. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **FWD-8: the Peers absent-column reasons are rewritten in reader words.** The face never says "factor code", "row field", "registry", "289 registry factors", "comparison map", "R-1" or a category in capitals. The reason says what the reader is missing and why, in one plain clause (e.g. "Shares outstanding is not reported for these peers"). | v20 :16; these strings are page-composed (`cscTable.ts` / `PeersTab.tsx`), so the fix is page-side |
| 2 | **FWD-11, SEC accession number: it is an id and comes off the face.** The face names the filing in words: form, company and filing date, as FWD-6's citations already do ("VLO US's 10-K, filed February 25th, 2026"). The accession rides as the link target or a `data-` attribute. | It is a public identifier, but the reader cannot use the digits; FWD-11 says "no raw ... id" |
| 3 | **FWD-11, the "a SERP not scoped ... is not the contract's search" sentence: it is machine reasoning and comes off the face.** The cut locates where it is written. If it is page-composed, it becomes a round-23 cell. If it is served, it is RESAPP round 61, on B2's terms: a plain served reason fixed at its producer, with the page guard as the backstop. | It is not a code, but "SERP" and "the contract's search" are system vocabulary; same remedy as ruling 1 |
| 4 | **FWD-10, Posture reason 2's placeholder sentence:** this closes on RESAPP **B4**. Once the drafter serves the claim in words, the guard passes it through. No page cell. The placeholder is the intended interim. | Round-21 ruling 1: a served string is fixed at its producer |
| 5 | **FWD-7 (VLO "Senior Vice", trailing ages)** closes on RESAPP **B3**. **FWD-2 (24 bars by ticker)** closes on RESAPP **B1** (ak-2, CTO half @02d032ee67). | served |
| 6 | **Z-W69-S1 (posture.harness unrunnable: a stale `useCollectedChatter` stub):** an instrument repair cell in round 23. | v20 :19, :25 |

## 3. THE ENRICHMENT LIST -- round 23, `2.0.0_SA_COO~D`, ONE issuance

| # | cell | criteria shape |
|---|---|---|
| 1 | Peers absent-column reasons in reader words (ruling 1) | rendered census of BA's, VLO's and AMD's Peers reasons reads 0 of the listed system terms; every absent column still carries a reason (count equal before and after) |
| 2 | Exec filing line without the accession (ruling 2) | VLO Exec: 0 matches for `\d{10}-\d{2}-\d{6}` on the face; the filing named by form + date; the accession present in the DOM attribute |
| 3 | the SERP sentence, if page-composed (ruling 3) | 0 of "SERP" or "contract's search" on the faces walked; otherwise the cut routes it to RESAPP and the cell drops |
| 4 | posture.harness repaired (Z-W69-S1) | `node posture.harness.cjs` rc 0 at the round tip, with its checks green; a planted posture fault reads red (the harness grades something) |

**Deadline:** drained by **11:30Z** and merged onto remote DEV, like `419ef41d`, so ONE candidate goes to Andrew. Otherwise the
promote candidate stays `419ef41d`.

## 4. ACTS ONLY ANDREW CAN DO (cited)

1. **The DEV push and the PROD promote** of the newest approved candidate (`419ef41d` now, or the round-23 merge if it drains in
   time). The payload is his to name (CVO verdict 27503). A merge-forward also carries 40 non-DSGN files from 10 FAST commits.
   Rollback is `b3a1d8a6`.
