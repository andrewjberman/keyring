# CTO WAIVER (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~01:4xZ) -- dev-overlap on `cand/dell1/mdpf-canon-global-trend-variant1-rf-dev`

**Branch:** `cand/dell1/mdpf-canon-global-trend-variant1-rf-dev` @`85f1d324bdfa69438a03b197c5a20864d3bf7485`. It is origin/DEV `e578b378d3` plus ONE commit
whose six product files are blob-equal to the approved candidate `15f7610285` (row `dell1-20261015T013256Z-f411`, approved by Andrew on
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261015_01xxZ_COO_D1_TREND_LOOKS_GOOD_CUSTOM_ROLLFORWARD_THEN_PROD.md`).
It exists only to converge DEV after portal-merge-forward refused the PROD-based candidate on a conflict with the declined Trend already in DEV
(ruling: CTO msg 5977).

**Why the waiver is safe (read by me at ~01:4xZ):** `git rev-list --count origin/PROD..origin/DEV` = **22**, and origin/DEV is still `e578b378`. The 22
shas below are exactly that set. Each is an ancestor of origin/DEV and was merged into DEV on its own approval. Merging this branch into DEV
re-adds none of them, because they are already there; it adds only the one resolution commit. The waiver covers these 22 shas and no other. A
change of DEV's tip before the merge-forward voids it.

## The 22 shas waived

- e578b378d332ad1505018be3801466dac7aeeade
- bbad56e354e9091170fe8a94c02b03c824bc4aba
- 90d615c0873f6c74e49dcbd19f3fd7d276d86cef
- 66d221626ec3ca04b68485b95ec7998d0dd60264
- b763674bb4d5e62e40e6dbec78f4d7dacc34ba06
- 9de7c7e3227c321d45c2b6d3d3ccf72590b20710
- 3db44fe0e9c3392e37cb39f4ef142fd3f22b3514
- 00f5c1b44cd257a63eacac0ec0cf15202ddf51cd
- 9e637fe51ebfa6322910cc032945a1e755e9ea13
- 1c5f9daeb887b138a3d67f7a84c4952b0b6ae162
- 7f6c698d429cffeb5990265ed35d20a46e6735e3
- 6f4e5f671f098ac157a6fa1fcabea10bcf80ad47
- 34cd12d2d041e225767c8c80176570d6921a011a
- 4f1004518604cac12f296c7c808d81475e903cec
- 406345bce120cdec5d9b7a0cef00bd7b80b680e9
- 97c66c93640b5853e2ec1dbd5d73765f2e888321
- 22795405240520ea0fb4f87f942b20c285190696
- 2deb4f1d864d8fa23cccbf9a11fb3266c88e1042
- ab8ecc5662c9166bc4b3ff3d9ba370733ba4d3cf
- 514df1bbf04d91f88dad30f6336b8992228710a6
- 5e40e54119474b50702f71db979df861481615a4
- 24877b67b7a175bcfe73c779f69c0bf7c3c639c8

-- 1.0.0_SA_CTO~DELL1
