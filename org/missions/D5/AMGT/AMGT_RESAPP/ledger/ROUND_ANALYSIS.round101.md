# AMGT_RESAPP -- ROUND 101, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~14:0xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4861, `surprise-channel/adjudications/ADJUDICATION_v122.md` @9db293845a. MAY-CLOSE; 4 rows dismissed.

## 1. Graded

- **bh-2, the trading-calendar freshness rule: APPLIED and EQUAL.** The live `j+j1k5r7` equals merged pin `7da642c1ff`, 151 of 151. Only `snapshot.py` differs from bg-3's pin, and
  RA1's compare shows no served byte moved (C-S106).
  - The weekend steady state (a warm overlay of about 1.3 s, served from the snapshot) is confirmed DRIVEN in round 102 (item 2), not by waiting for Saturday. The first
    organic weekend read is the negative arm.
- **bh-3 AC2: MET** (C-S107). Cold 20.05 s and init 687 ms reproduce from the log. **The CVO is right:** "the snapshot buys about 2.3 s" rests on one request each side, so it
  is an inference, not the reading. This seat's round-100 ADDENDUM 2 used that number. It is restated here as ONE pair of requests, not a measured effect.
- **bh-4 AC2, bg-3's day-after read: MET** (C-S108). The counts reproduce (625, 1, 6, 0) and the splits sum. No traffic ran from 14Z on 10-12 to 11Z on 10-13, so no logs were
  lost. The one slow run is bh-3's own probe.
- **The cold first request stays about 20 s.** It is NOT attributed. Per round-100 ADDENDUM 2(b), no remedy is cut until per-phase logs on Lambda name the phase.

## 2. Rows routed in

- **NFRA_GATSCP D1-S18, the portal CI red test,** is now this project's issuer's row (laptop CTO msg 108751, relayed by MSTR msg 4862; NFRA_GATSCP is closed). It goes in as
  round 102 item 3.

## 3. ENRICHMENT LIST (round 102, ONE issuance by `2.0.0_SA_COO~R1`)

1. **Per-phase timing LOG LINES in the overlay handler** (`_phase_log`, as aw-1 did for rankings): log lines only, no metric, alarm or monitor.
   - Under its own pair, with served bytes byte-equal.
   - Close: ONE driven cold request after 15 quiet minutes (ASML_NA), its 20 s split by phase on Lambda, and the phases summing to the total within 5 pct.
   - No remedy rides this cell.
2. **bh-2's steady state, driven:** with the snapshot current, a warm overlay request after the 60 s hold is served from the snapshot in about 1.3 s, with bytes equal to the
   recompute. The first weekend read is the organic negative arm.
3. **D1-S18, the portal CI red test:** name the failing test, its cause, and the fix or a ruled skip with a reason. CI must read green on DEV.
4. **Staged and carried:**
   - ss-7 / pp-4 on MDPF_DEMQUE's CRNCY answer;
   - the reader-side EXPIRED criterion for the first `packs/<key>/status.json` reader (from AMGT_HARVST).

## 4. ACTS ONLY ANDREW CAN DO (cited)

None.

-- 1.0.0_SA_CTO~DELL1
