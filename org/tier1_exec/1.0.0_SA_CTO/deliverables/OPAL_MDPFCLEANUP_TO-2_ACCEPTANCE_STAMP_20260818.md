# OPAL_MDPFCLEANUP.TO-2 -- CTO ACCEPTANCE STAMP (the K3 gate opens)

**Stamped:** 2026-08-18 ~1315Z by `1.0.0_SA_CTO` (arch gate + apply-GO holder, TO-2 `<status>` line)
**Proof under review:** `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/OPAL_MDPFCLEANUP/proof_TO-2.json` rev1 @809b948ef4 (AE, 2026-08-14 18:20Z), COO re-validation 2026-08-18 130021Z (@62bd311d16 wrap-order re-date).
**Verdict:** **ACCEPT.** The K3 second-unattended-sample question (my open call from 08-14) is answered: not one but THREE unattended canonical cycles landed on the floor slot, and the value tie holds across producers at equal value_date.

## What I read myself (not the proof's word)

Object-version census on `s3://opal-data-assets/blackdiamond/cottonwood/gold/dim_model_portfolio/date={D}/data.parquet` (`list-object-versions`, 08-14..08-18) and CloudWatch log-stream census on `/aws/lambda/mdpf-daily-trigger` (the K3 chain's entry) + `/aws/lambda/mdpf-gold-lambda` (the canonical floor):

| day | canonical floor (mdpf-gold-lambda) | K3 legacy chain (mdpf-daily-trigger -> EC2 runner) |
|---|---|---|
| 08-14 | 13:30:39Z write (arrow 20.0.0, value_date 08-13) | trigger 07:24:56Z -> 07:27:53Z write (arrow 21.0.0, value_date 08-12) |
| 08-15 Sat | 13:30:39Z write | trigger 12:40:17Z -> 12:42:46Z write (arrow 21.0.0, value_date 08-14) |
| 08-16 Sun | 13:30:40Z write | trigger 12:40:40Z -> **NO write** |
| 08-17 Mon | 13:30:39Z write | trigger 12:40:09Z + 12:41:21Z -> **NO write** |
| 08-18 Tue | (13:30Z slot not yet reached at stamp time) | trigger 12:44:42Z -> 12:47:32Z write (arrow 21.0.0, 8416B, value_date 08-17) |

**Producer discriminator, exercised both ways on KNOWN 08-14 versions:** legacy EC2 write `Fr46Rdlb...` = `parquet-cpp-arrow 21.0.0`; canonical Lambda write `7uGduxkx...` = `parquet-cpp-arrow 20.0.0`. Every 12:4xZ write since is arrow 21.0.0 = the K3 chain; every 13:30Z write is arrow 20.0.0 = the canonical floor.

**Value tie (my read):** 08-15 12:42Z legacy (value_date 08-14) `dollar_value` sum 144,039,829.45 == 08-17 13:30Z canonical (value_date 08-14) sum 144,039,829.45. Same 10x12 frame, same columns. The 08-14 delta AE attributed (08-12 vs 08-13 marks) is the vintage roll, self-attributed by `value_date`; nothing unexplained.

## COO's timing observation -- RESOLVED, it is the thing K3 kills

Today's 12:47:32Z write (43 min before the floor, 2 bytes smaller) is the **K3 legacy chain**: `mdpf-daily-trigger` fired 12:44:42Z (log stream `2026/08/18/[$LATEST]a52d6543...`), the write is arrow 21.0.0, and mdpf-gold-lambda has NO 08-18 stream yet. Since 08-15 the INF completion marker lands ~12:40Z instead of ~07:24Z, so the legacy write now precedes the floor by ~45 min and the floor overwrites it. Two observations, neither chased (K3 removes the producer): (a) the legacy chain fired 4/4 days but wrote 2/4 -- silent non-delivery on 08-16/17; (b) each day the key carries the legacy toolchain's bytes for ~45 min before the canonical overwrite. Both are the two-homes class the PRD names as the argument for the kill.

## Acceptance criteria (TO-2 `<expected_criteria>`)

| criterion | verdict |
|---|---|
| dim-wired-into-canonical-scheduled-path-no-new-build | PASS -- consolidator production branch `bdmp.main(["--date", adate, "--upload"])` @84c1fc08fd:712, executing bytes pinned at GATE-GO #4; nothing built |
| no-shadow-no-comparator | PASS -- zero new paths, zero applies, reads only |
| full-cycle-exercised-dim-written-by-canonical-path | PASS -- 08-15/16/17 unattended floor writes (3 cycles beyond the 08-14 one) |
| values-tie-against-prior-producer-run-and-read | PASS -- my own versioned-GET comparison above |
| zero-diff-apply-tagged | N/A by construction -- verification TO, no TF change |

## Consequence

**K3 GATE OPEN.** COO may GO AE on the K3 rows of TO-3 (the `mdpf-daily-*` chain: refresh-trigger rule, trigger Lambda, runner EC2, DLQ, alarms, dispatch.sh) -- I gate per-apply exactly as wave-1 (expected-rows-bounded plan, sha-identity, consumers-first sweep with last-invocation history). EC2 stop/terminate remains Andrew-reserved per the PRD ops note; the apply that touches the runner instance names that reservation explicitly.
