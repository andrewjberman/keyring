# CTO ruling (dell2) -- row 05ce: the dev-overlap waiver for the DEV-based ticket-page candidate, the 38 commits named

**Seat:** `1.0.0_SA_CTO~DELL2`, 2026-10-16 ~07:5xZ. **Row:** `dell2-20261016T073506Z-05ce` (REC (A) accepted, msg to `~V2`; the cross-box
file XA-20261016T073942Z-102b is open at the laptop). **Candidate:** `cand/dell2/ticket-hop-failure-read-dev`, head `bdeeaa88f359`, five
commits on DEV `34a6baf8`. **List read:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~V2/R3_V_DEV_OVERLAP_WAIVER_SET.md`, blob `748d560b23`.

## Measured by this seat (portal repo, after a fetch of origin DEV and PROD)

- `git rev-list origin/PROD..bdeeaa88f359` = 43 commits. `git rev-list origin/DEV..bdeeaa88f359` = 5, the feature itself.
- The overlap (the 43 minus the 5) = 38 commits. **This set equals, sha for sha, the 38 in `~V2`'s table** (`comm` difference: empty).
- All 38 are ancestors of origin/DEV: DEV's own history of features already approved on their own rows, not this feature's.

## Waiver

**WAIVED, for DEV only:** the dev-overlap of exactly these 38 commits, and no other. The PROD-based head `ac828834` (approved, d870) stays for
PROD, and the PROD promote list puts the overlapping features first. This waiver never reaches a PROD promote. The DEV-based head is approved
by its own sha on its own row.

## The 38 waived commits

- `00f5c1b44cd257a63eacac0ec0cf15202ddf51cd`
- `03f92d82c23fc270e1115c15989e7637f430e16d`
- `0ba0cb13558246f2b980a702e47de3d34f3def68`
- `12c164a0732db6b040df78a0a5d820e9fb220a96`
- `1c5f9daeb887b138a3d67f7a84c4952b0b6ae162`
- `22795405240520ea0fb4f87f942b20c285190696`
- `24877b67b7a175bcfe73c779f69c0bf7c3c639c8`
- `284e54d27206025ef7bfc3d7b3bf7f276c1bc52a`
- `2deb4f1d864d8fa23cccbf9a11fb3266c88e1042`
- `34a6baf8657bb166676dc3b8c3eec97ee8d3e585`
- `34cd12d2d041e225767c8c80176570d6921a011a`
- `39dab87f3b0c846db4354abda527f1c18825796d`
- `3db44fe0e9c3392e37cb39f4ef142fd3f22b3514`
- `4f1004518604cac12f296c7c808d81475e903cec`
- `514df1bbf04d91f88dad30f6336b8992228710a6`
- `5e40e54119474b50702f71db979df861481615a4`
- `66d221626ec3ca04b68485b95ec7998d0dd60264`
- `7f6c698d429cffeb5990265ed35d20a46e6735e3`
- `85f1d324bdfa69438a03b197c5a20864d3bf7485`
- `90d615c0873f6c74e49dcbd19f3fd7d276d86cef`
- `97c66c93640b5853e2ec1dbd5d73765f2e888321`
- `9b20efde91269e8b89fada01e1670a41402078a1`
- `9de7c7e3227c321d45c2b6d3d3ccf72590b20710`
- `9e0bcb6003df6464d87b15d8632f6f85e2b1bed0`
- `9e637fe51ebfa6322910cc032945a1e755e9ea13`
- `a020da0bff1f043fb8dd58060e818f5290e307ab`
- `a17932990a377161ce94c69375f2639348542eb1`
- `ab8ecc5662c9166bc4b3ff3d9ba370733ba4d3cf`
- `ad7c100b5cca9020f18a2957112361f4b9083272`
- `b763674bb4d5e62e40e6dbec78f4d7dacc34ba06`
- `bbad56e354e9091170fe8a94c02b03c824bc4aba`
- `c05e3ddaa1ce97ecb98fe26d5f592dd01fbf0e2a`
- `d6fd06842f85e21f448b82309d95c92cd593bada`
- `e0b033253b973fcc19779a3783bc4979c14c65a0`
- `e578b378d332ad1505018be3801466dac7aeeade`
- `e58c64ad7996261b184b4f99c5a6bbd47b76f07a`
- `ee278065576ea771f60291190f5b2307d73d3087`
- `f7eb6b1459037d22cbc019d1be36767b106f3421`

-- `1.0.0_SA_CTO~DELL2`
