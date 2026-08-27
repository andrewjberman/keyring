# BLOCKER BRIEF — $51.8M of 49F insurance assets cannot be attributed to any advisor

**For:** DAILY_SPRINT 2026-08-27 · **Author:** 3.0.0_SA_CVO on Andrew's word at the CVO terminal
(~22:3xZ: *"write a brief about this, it's a blocker that we need to bring up in the daily-sprint
today"*) · **Class:** vendor-config blocker — resolved by a 49F conversation, not by any build.

---

## The one-paragraph version

49 Financial's insurance book — **$51,807,815.31 across 102 valued accounts (of 106; 4 carry null
valuations under separate investigation)** — cannot be attributed to any advisor from the Black
Diamond data, because **no advisor-attribution key is populated in 49F's BD instance**. The
Advisor Intelligence views that group clients under their advisor (the advisor Book view, the
Books-tab rollups) will render all insurance as an "unassigned" class until 49F populates one.
The capture machinery on our side is **built, deployed, and idle** — the moment 49F assigns the
data in BD, it flows with **zero additional build**. The unblock is one question to Mike.

## What was measured (not inferred — every claim carries its denominator)

Full key enumeration of both landed vendor payloads (71 keys on the relationship object, 51 on
the account object), then occupancy on every advisor-shaped candidate:

| candidate key | measured occupancy | verdict |
|---|---|---|
| `financialTeam[]` / `teams[]` | **affirmatively EMPTY** — key present, zero entries, 77/77 relationships (probe mutant-controlled, four states → four verdicts) | BD's designed advisor link; nobody has assigned teams |
| `accounts[].repCodes` | **2 of 106** accounts (one code, `PKS001305`) | the classic custodial advisor key; effectively unused |
| `contacts[].team` | populated with the catch-all **"All Firm Users"** | non-discriminating |
| `users[]` (relationship-level) | 1 on the lone specimen — a **@miradorllc.com** FirmUser (Mirador = the outsourced reporting administrator) | almost certainly the admin, not the advisor; cohort-wide read would need 77 vendor calls (egress word) |
| everything else (`portfolios`, `segmentation`, `userDefined`, `outsideIdentifiers`) | ids-only or empty | no advisor content |

**The asset number, twice-derived:** vendor bronze across both pages (denominator 106) and the
emitted gold table `insurance_nav_current` (date=2026-08-25) agree **to the cent** at
$51,807,815.31. Composition: 3 zero-balance, 1 negative (−$309,502.70), largest single account
$3.70M, 4 null-valuation (2 Allianz, 2 Vanguard — cause unattributed, open item).

## What it blocks / what it does NOT

- **BLOCKED:** per-advisor insurance attribution — the advisor Book view and Books rollups carry
  insurance only as "unassigned"; no per-advisor insurance totals are derivable from vendor data.
- **NOT blocked:** the ADVI v1 client cards, the D2 serve gate, the TWR remediation campaign, and
  the insurance NAV data itself (landing daily, honestly stamped `NOT-DERIVABLE-UPSTREAM` on the
  advisor axis). Nothing on the D2 critical path waits on this.

## The sprint item (the ask, ready to say)

> **To Mike / 49F:** How do you attribute clients to advisors — Black Diamond teams (currently
> unassigned on all 77 insurance relationships) or rep codes (currently on 2 of 106 accounts)?
> Whichever is yours, populate it in BD and the data flows to us automatically. If you track
> client→advisor somewhere else entirely, tell us where and we'll source it.

**On each possible answer:** teams assigned in BD → zero build, the deployed capture ingests on
its next run · rep codes populated → one small reader addition · an external list → a sourcing
decision comes back to Andrew.

## Evidence chain (for the record)

Probe + mutant control @113354aa60 · pre-registered empty-semantics ruling (COO 76312 + face rider
@34edfe3e53) · gold-contract stamp @f4836ad706/@36e59823f4 · key census + asset sum measured at
the CVO seat 2026-08-27 ~22:2xZ (bronze 2026-08-25 both pages; gold date=2026-08-25) · channel
record `org/surprise_channel/ADVI_INSURE/INVESTIGATION_v1.md`.

— 3.0.0_SA_CVO
