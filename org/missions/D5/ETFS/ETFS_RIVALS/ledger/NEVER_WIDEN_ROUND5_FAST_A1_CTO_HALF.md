# ETFS_RIVALS round 5 + amendment A1 (FAST) -- never-widen pair, CTO half (the etfs-rivalfunds deploy)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~07:3xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round5/NEVER_WIDEN_HALF_COO_FAST_A1.md` @4df699fa92 (table filled; msgs 28259, 28260).
Under Andrew's 04:59Z FAST word for ETFS_RIVALS. A FAST lease never lowers the `<risk>` class: this act is WORLD.

## What I read

1. **The COO half end to end,** at @6bd16e078e and again at @4df699fa92:
   - the plan is 0/7/0: 5 Lambda `source_code_hash` changes in place, and 2 role policies that only ADD;
   - the page delta over the same served inputs: 13 fund blocks equal, 198/198 trades, 0 scripts, 1.6 MB against a 2 MiB cap;
   - the blast radius K1-K7 with a rollback per key, writers counted per key, and both branches (applied before 10:45Z, or
     after the 09:00 ET sweep).
2. **The G1/G5/G6 table,** filled from `served_delta_r5.py` at the pin 7aa0186d45 (06:54Z-07:26Z):
   - **G1: 0 differences** on 13 of 13 funds.
   - **G5/G6:** every difference traces to a round-5 cell by its own replayed row:
     - h-5 REFUSED windows: INEQ 6, TXUE 1, TSEL 1, ETFT 2, WCMG 1;
     - h-4 ID-CHANGE pairing: IDVZ, PFOE.
     - 15 changed dates, none of them the newest window.
   - **The PCLG and WCMG +1 windows** are attributed to round 4's t-5. d-5 deployed it with no G5 replay, so the served objects
     predate it. This is INFERRED, with no control replay at the deployed pin. Two things keep it from being a precondition:
     **the act replays no history**, so these served objects do not move under this act; and the next runs build only new
     windows.
3. **The rule the act changes acts on new windows only.** From the 2026-10-01 report window on, an implausible window is
   REFUSED with its reason and infers no trades (h-5), and an exit + entry pair stays two trades unless an identifier relation
   pairs them (h-4). Both are ratified round-5 rules. The table bounds what they would do across the whole history; the act
   applies them forward only.

## Blast radius and rollback

As K1-K7 in the COO half, unchanged, and nothing wider.
- The five stage Lambdas' code and the two additive role policies roll back by re-applying from a tree at 25f4ac5418 in the
  same window.
- The new gold tables (K3), the hypotheses objects (K4) and the republished pages (K5, K7) are additive revisions. The prior
  `index.html` and `manifest.json` are kept under `revisions/<ts>/`.
- **Unmoved:** G0, G2-G4, bronze, silver, the gateway, the schedules and every other stack. No historical G1/G5/G6 object is
  rewritten.

## Conditions

1. The act-start gates in the COO half (1-5) hold at the act. A plan other than 0/7/0, a live base that differs from the
   recorded CodeSha256, or an in-flight invocation is a STOP.
2. **The PCLG/WCMG attribution stays INFERRED** in every record of this act, until a control replay at the deployed pin reads
   it. It is not re-stated as measured.
3. **The post-act read compares the fields the act moves.** For the 2026-10-02 page, that is the headline's current-fund count
   and the three A1 components present. For the first new G5/G6 window, any REFUSED window prints its reason. HTTP status is
   never the grade.
4. **NEVER-2:** the ledger entry `etfs-rivalfunds-fast-a1` is opened before the apply and closed after the read, or rolled
   back and closed RED.

**CTO HALF: SIGNED** for the plan 0/7/0 at CLOUD 7aa0186d45, the K1-K7 blast radius, and both branches as written.
