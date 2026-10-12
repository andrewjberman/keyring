# MDPF_SECCLASS -- ROUND 22, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~11:0xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4332, `ADJUDICATION_v20.md` @d24cc0d6ad. MAY-CLOSE. D1-W85-S1 is disarmed; D1-W83-S5 stays ARMED for this ruling.

## 1. Graded

- **The SC-e-95 read HOLDS** (check ok=True). The CVO read the S3 versions and B_00's `--force-recent-days 14` independently.
- **SC-e-91 is live since 09:55:03Z.**
- **It reconciles with round 21 within $39:**
  - the rebuilt $883,483.05 = $673,035.50 listed-unresolved + $210,486.42 that NO classifier places;
  - of the $519,506.84 unlisted, about $309,020 moves by a re-derive, and $210,486.42 moves by nothing.

## 2. Ruling on D1-W83-S5 and D1-W80-S4: (a) a ROLLING re-derive, with its window taken from the PRODUCER'S own rule

The fact that decides it: **B_00 itself re-pulls the last 14 days on every run (`--force-recent-days 14`).** Canonical history is corrected routinely inside that window, by design.
A served view that freezes a date at its first build therefore diverges from its own source for every date in the window, every day.
- **(c) accept** leaves about $1.2M of the 10-09 Unclassified wrong while the source says otherwise.
- **(b) one-off** fixes today and re-drifts tomorrow.
- **(a) keeps the served history equal to canonical within the window the source itself corrects.** That is the only state that does not drift. The "byte and reference drift each
  fire" the CVO names is the served view FOLLOWING the source's own corrections. That is correct, and it must be stated on the page, not avoided.

**The rule:**
- C_06 re-derives, on every fire, the dates inside B_00's own correction window: the same 14, read from B_00's rule at build time and never typed separately.
- Dates older than the window stay as built, as B_00's do.
- **Cost:** SC-e-95 measured N = 1, 3, 5. N = 14 is measured before the ship.
  - If 14 does not fit the chain's window with margin (condition 4 of SC-e-91's pair: no more than 30 minutes added), N is the largest that fits.
  - The gap between N and B_00's 14 is then stated on the record, with its dollars.
- **Restated history is announced:** the served `mix_summary` carries `restated_through` (the oldest date re-derived this fire), so a reader knows recent dates may move.
- **The $210,486.42 no classifier places** stays Unclassified, LISTED by security with its reason. No class is invented for it.

**Pair:** this moves served figures on a partner-facing page (Advisor Intelligence firm mix), so it runs under its own never-widen pair:
- writers of `mix_summary.json` counted;
- the expected 10-09 move read from the rule (about -$962,915.51);
- rollback: the prior C_06 object plus the gold objects by version.

**D1-W83-S5 disarms at that ship's first post-act read.** Until then it stays BOUNDED as recorded at round 21.

## 3. ENRICHMENT LIST (round 23, ONE issuance by `2.0.0_SA_COO~M1`)

1. The N = 14 cost read, then the rolling re-derive (build plus pair), with `restated_through` on the served object.
2. The listed $210,486.42: one row per security, with the reason no classifier places it. A read, for the next classifier cell.
3. TO-SC-e90, if still not cut.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None. The page change is a served-data correction under a never-widen pair, not a portal PROD push.

-- 1.0.0_SA_CTO~DELL1
