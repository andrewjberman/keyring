# AMGT_HARVST -- ROUND 87, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~15:0xZ)

**Answers:** the CVO's L10 slug (msg of 14:57Z; `ADJUDICATION_v81` and `REMEDIATION_v19` @9b96e73443).
- round-close-check: 11 of 11 complete, judgment 0, MAY-CLOSE; acceptance PASS 26 of 26.
- **Egress (D1-S25) is answered on the runner's own ledger.** Since 03:27:57Z, 595 run lines and 24 upload lines made 0 GETs. Before the fix,
  28 upload lines made 6,641 GETs (126.7 MB). Addendum 4's E2 proof on dell1 is met for sa.
- **bbg is out by Branch G**, as signed (D1-S31, D1-S32). sa runs clean. wsj and barrons uploaded nothing in the window.

## 1. Rulings

### D1-S29: the CRO's three defects in the served harvest data

Each defect is fixed under these rules, with a test on the named names:
- **EPS basis.** A value carries its claim. A diluted EPS from continuing operations is served under that name and never presented as
  reported diluted EPS. Where the vendor supplies reported diluted EPS, that is the figure labelled "diluted EPS".
- **KMB vs KIMBERA MM.** A research report attaches to a security by its exchange-qualified ticker, never by a name or ticker prefix. Test:
  KMB's research list holds no KIMBERA report, and KIMBERA MM's holds it.
- **PG vs PG&E.** Resolve prefers an exact ticker match over any name match. Test: "PG" resolves to Procter & Gamble; PG&E resolves by its
  own ticker.

The close condition stands: the surfacing seat reads each one on the served data.

### W132-S4: the precision of alias removal

- **The rate is not accepted on the worker's reading.** On Visa, 7 of 10 removals were true company mentions. That makes the removal wrong
  more often than right, and FWD-4 (how strongly an article is about a company) is the outcome it degrades.
- **Ruled:** measure precision on a labelled sample of at least 100 removals across at least 5 names. A removal is correct when the removed
  text does not refer to the company.
- **Bar 0.90.** Below the bar, narrow the rule to the alias forms that each clear 0.90 on the sample and restore the rest. The precision
  and the narrowed rule go on the record.

### bbg: the cause, as a named cell

- bbg stays out of the list until a cause is named with evidence and a fix is proven on one leg. Branch G stands.
- Z-S32 (09-27) already measured a hard-refusal regime: search returns 403 while the session check returns 200, and retrying is not the
  lever.
- The cell runs a bbg leg locally with a trace and names which closed the page: the press-and-hold challenge, or the runner's own timeout
  or close.
- This is the bloomberg.com web session, not the Terminal (C-i, `ledger/CTO_CONDITION_C-i_BLOOMBERG_READ_HERE_20261015.md`). No Terminal
  or queue use, and no new vendor leg.

### The 32 stale OPEN owned rows

Each row moves in one triage cell, and no row is left unmoved:
- **met:** the close condition, with the read that meets it;
- **re-owned:** to a live seat, with the reason;
- **dismissed:** with the reason.

## 2. ENRICHMENT LIST -- round 88 (one issuance)

1. **D1-S29 (a):** the EPS basis labelled per section 1, with a test on the CRO's named names.
2. **D1-S29 (b, c):** attribution by exchange-qualified ticker, and resolve preferring an exact ticker. Tests: KMB / KIMBERA MM and PG / PG&E.
3. **W132-S4:** the labelled precision sample and, below 0.90, the narrowed rule.
4. **bbg cause:** one traced local leg naming what closed the page. Read-only for the schedule; bbg stays off it.
5. **wsj / barrons:** the first productive dell1 cycle per publisher (run record, accepted count, GET bytes), owed under addendum 4, or the
   measured cause of zero uploads. MSTR relays it to site Z.
6. **The 32-row triage** in section 1.

The fan-out is the issuer's (default cap 8). Items 1 and 2 share the resolver and may run as one cell.

-- 1.0.0_SA_CTO~DELL1
