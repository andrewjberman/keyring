# Approval row dell2-20261013T221352Z-cffa is a DUPLICATE of dell2-20261013T221411Z-3635 (2026-10-13 ~23:0xZ)

Both register `cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal` (D2 filed it twice; msg 7301). `approval-status` reads the newest row, so **3635 is the live row** and cffa closes as a duplicate. No decision on the feature is made by this close; Andrew's decision is taken on 3635. On the laptop CTO's word (msg 108975, relayed as 7331).

-- 1.0.0_SA_CTO~DELL2

**Close mechanics (laptop CTO msg 108976, relayed as 7333):** closed with `--decision declined` because `close` requires a decision on an approval row; the ruling is "duplicate of 3635". `approval-status` reads only the newest row (3635), so this decline does not touch the feature.
