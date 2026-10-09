# MDPF_STRATID PRD v0.1 -- ratified-text half review (L4-R)

**Reviewer:** `3.0.0_SA_CVO` (dell1). **Object:** `org/missions/D8/MDPF/MDPF_STRATID/prd/MDPF_STRATID_PRD.md` @c17e5e6300, half_hash
`6ab65484cc74` (msgs 1138, 1139). **Pins read:** ratified endpoint
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_STRATEGY_IDENTIFICATION_INTO_GLOBAL_20261008.md` and Andrew's record
`ANDREW_DIRECT_20261008_201xZ_LIQUID_ALTS_TO_ALTERNATIVES_ETF_STRATEGY_SLEEVES_ENDPOINT_CONFIRMED.md`, both @8e4b5037b4.
**Verdict: SIGN.** Two wording findings, neither touching the ENDPOINT bytes.

## Checks

| Check | Result | Evidence |
|---|---|---|
| ENDPOINT verbatim vs the ratified pin | PASS | A line diff of the FWD block, PRD against the endpoint file, gives one hunk: FWD-5's SOURCE line is shortened (the amendment history is dropped). Every DONE WHEN and ACCEPT line of FWD-1..7 is byte-identical. |
| Ratification covers this text | PASS | Record line "3. Confirm as written"; ruling 3: "DONE WHEN lines are ratified as written, with FWD-5 as amended by answer 2". The FWD-5 ACCEPT carries answer 2: ticker or full name, SmartX, Rebalancer and Eclipse, SMA group under the ETF Strategies drill-down. |
| Operative constraints present | PASS | Cottonwood SMA additive -> C-BASIS. Tax and Muni under ALT -> C-SMA-RULES. Ticker or full name, whole sleeve, not direct holdings -> C-SLEEVE (record ruling 2: "NOT about counting direct holdings"). One list -> C-ONE-LIST. |
| No annotation inside the outcome text | PASS | Annotation sits only in SOURCE lines and the "Ratified by" line outside the fenced block; no seat serial inside the FWD block. |
| No FWD is a wait | PASS | FWD-4, FWD-5 and FWD-6 are "shown on purpose". FWD-1, FWD-2, FWD-3 and FWD-7 read one scheduled run, which is the acceptance fire, not an organic wait. |
| STARTING STATE citations | PASS | Bytes printed at every cited line: `wsb_49f_smartx_model_aua.py:62,194`; `rebalancer_schemas.py:218-226`; `dim_mdpf_aggregate_aua_timeseries.py:82,158-159`; `mdpf_category_registry.py:343,375`; `mdpf_gold_consolidator.py:1648`; `build_cottonwood_mdpf_slice.py:354-357`; the test file exists. Each line says what the PRD says it says. |
| CONTRACTS vs counterparts | PASS with F2 | C-GLOBAL-PAIR routes Global's served output through laptop `1.0.0_SA_CTO` as MDPF_GLOBAL owner (msg 107101). C-LAYERS forbids a shadow path or comparator. |

## Findings (wording; for `1.0.0_SA_CTO~DELL1`, to land at L5 or the next bump)

- **F1. C-BASIS against FWD-5.** C-BASIS says a `(member, firm)` pair with no declared basis "does not count at Global and is listed".
  FWD-5's ACCEPT says a sleeve found in any of the three surfaces "shows in the SMA group under the ETF Strategies drill-down", and
  adding the fund to the list "is the only step". An Eclipse (Inflection) sleeve, or a new fund at any firm, has no declared basis today,
  so under C-BASIS it lands on the unidentified list, not in the SMA group. The two read consistently only if "found" in FWD-5 means
  identified, not counted. The decomposition should either declare a basis for every `(member, firm)` the three surfaces can produce, or
  state that FWD-5 grades identification and FWD-4/C-UNIDENTIFIED cover the basis step. Otherwise the L9 grade of FWD-5 is ambiguous.
- **F2. C-GLOBAL-PAIR names "this seat's half".** NEVER-1's pair is CTO + COO. The contract names the laptop CTO plus "this seat",
  which read inside a CTO-authored PRD is a second CTO half and no COO half. Name the COO half (the MDPF_STRATID COO lane, unseated today).

-- 3.0.0_SA_CVO
