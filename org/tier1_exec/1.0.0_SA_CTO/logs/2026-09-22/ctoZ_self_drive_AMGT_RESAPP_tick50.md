# /self-drive AMGT_RESAPP -- tick 50 (1.0.0_SA_CTO~Z), 2026-09-22 12:45Z

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_145xZ_SELF_DRIVE_AMGT_RESAPP_POST_REBOOT_REARM.md`.
**state: ARMED.** Cursor: the tick-49 log @`d3ba12c64b`.

## Since tick 49

- **COO msg 24215: five calls, ruled.** Drafting the held B-run orders found two runs that would fail even with
  Andrew's word:
  - B2 would stop mid-loop on the immutable filing_attempt.
  - B4 would refuse on an empty roster and a missing domain.
  Rulings:
  - Round 27 is a SKIP-HELD code cell plus a read-only B4 diagnosis.
  - A silver write with no reader needs no pair.
  - Caps: B2 45, B3 18, B4 50 credits.
- **Round 27 ISSUED** @`40f01c2b08`: rk-105 (filing_attempt SKIP-HELD) and rk-106 (the B4 roster/domain diagnosis).
  Both are pending, with workers running.
  - This seat REJECTED the COO's REC to raise on a CHANGED outcome, and ruled CHANGED-HELD: continue, 0 puts, then a
    non-zero exit at run end. A mid-loop raise writes nothing and blocks every later name.
  - The superseding of a newly RESOLVED name is a served reader change (`scoped_amgt.py:1954-1981`), for a later round
    under a pair: a sibling RESOLVED marker, never a delete.
- **Andrew-direct ~12:2xZ** @`2a192b6e07`: the recs are agreed, but NO backfill runs until he has confirmed (A) a
  security list and (B) a channel inventory with bronze, silver and gold forms and the ingestion cycle for each.
- **Proposal for A and B** @`51431810dc` (`prd/BACKFILL_SCOPE_PROPOSAL_20260922.md`).
  - It was built from a read-only research pass, with this seat's re-checks on different instruments: an S3 recount
    per prefix, the chatter schedule, the daily-pull script, and `universe/v1/2026-09-16`.
  - Findings:
    - Gold parquet does not exist for any channel.
    - Silver is live only for filings.
    - The only running AMGT schedule is the chatter axis.
    - The PRD's daily price leg is not built.
- **Andrew-direct ~12:5xZ** @`5c20841dd1`: a third precondition, the KEYING STRUCTURE. It sets the primary key and
  ordered fallbacks on measured coverage, for a global IEFA universe that is non-US from the start. His direction is
  "Bloomberg's most stable key".
  - This is a DESIGN FORK, routed to `4.0.0_SA_CRO~Z` for research (msg at 12:44Z). The research covers the estate's
    patterns, Bloomberg identifier stability, coverage over IEFA's constituents, and the re-key blast radius.
  - The list proposal is superseded by IEFA, and is re-cut once the key is ruled.
  - The COO was told not to bake any new dependency on the ticker-derived `security_key` into a round-27 fix.

## Open calls in scope

- **This seat: 1, pending research.** The key design is decided the tick the CRO's research lands.
- **At Andrew: 1 combined card, not yet issued.** It confirms the key design, the IEFA list and the channel inventory,
  and it goes to him after the ruling. The PROD look (after the backfill) and keeping the Lusha profile URL are agreed
  by his ~12:2xZ word.

## State

- AMGT_RESAPP: `active` / `EXECUTING`. PRD v0.21 ADMITTED.
- Open orders: rk-105 and rk-106 (round 27, pending), plus rk-49 (held).
- Inbox: 0 unread. Sequence: no flags.
- **COMPLETION TEST: NOT DONE.**

## Compiler Tools

`prd-signoff.py status`, `sequence-check.py`, `aws s3 ls` / `aws s3 cp` (read-only), `get_live_agents`,
`safe-commit.sh`, `send_message`, `Agent` (the read-only inventory research), Monitor (inbox re-arm 46).

-- `1.0.0_SA_CTO~Z`
