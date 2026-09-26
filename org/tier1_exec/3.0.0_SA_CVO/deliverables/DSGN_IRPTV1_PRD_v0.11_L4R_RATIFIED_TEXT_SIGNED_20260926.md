# L4-R review -- DSGN_IRPTV1 PRD v0.11, ratified-text half (`3.0.0_SA_CVO`)

**PRD:** `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` @`e13fed2413` (v0.11). **Half:** ratified-text,
`half_hash` `c6ba94d5def9`, ENDPOINT hash `fef02972e418`, re-measured with `prd_signoff_lib` at the pin and matching
delivery 101292. **Prior:** SIGNED at v0.10 @`419c52cbc3`.

**Verdict: SIGN.** The ENDPOINT delta is ONE added outcome, FWD-20; FWD-1 to FWD-19 are byte-unchanged from v0.10
(`git diff -U0 54410c6a90 e13fed2413`).

- **FWD-20 matches its ratified pin.** Andrew-direct "recs approved for all", record @`a6700b211e`, section "What it
  binds" item 2, reads: "Each account's YTD shows beside its name where the advisor chooses accounts, loaded
  progressively, with no combined client return."
  - The ACCEPT carries every clause: YTD beside the name in the chooser, figures filling in as they arrive, and still
    no single return for the whole client.
  - It adds "an account that cannot be computed says so in plain words", the same clause FWD-5 (v0.10) and FWD-19
    already carry.
- **The DONE WHEN is an EXERCISED act a seat can take**: a real multi-account client, and the lagging account named
  from the list.
- **Coherence.** FWD-20 and FWD-19 agree: clients only, per-account figures, no client return. FWD-20 and FWD-5 are
  jointly passable. FWD-5 reads each account by switching; FWD-20 adds naming the lagging one from the list.
- **Hygiene.** The ENDPOINT section holds 0 seat serials (regex census), the `@RECORD_PIN` placeholder seen in the
  CTO's uncommitted draft is filled at the committed pin, the ids run FWD-1 to FWD-20 with no gap, and the header
  `endpoint_outcomes` matches.

-- `3.0.0_SA_CVO`, 2026-09-26 ~16:1xZ
