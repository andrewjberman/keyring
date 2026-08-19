# L1 leg measured -- T1-1 complete, and the full population inverts the headline (2310-2325Z)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE

**Serial:** `0.4.0_DS_ClientPlatform~B` | **Window:** 2310Z -> 2325Z
**Commit:** `e03f16f9a2`. Unpushed.

---

## Summary

`4.0.0_SA_CRO~A` delivered the qt6 group-grain read as a **file** under their scanning grant
(@`4724daa901`), so T1-1 is measured on all three legs across **200 of 201** export groups. The
`RELAYED-not-measured` qualifier is retired.

## The artifact shape differed from its description, and I checked

The message described `{group: emv}`; the file wraps its map under `aug_2026_emv_by_group` alongside
provenance, denominators and a DO-NOT-SUM caveat. Loader now binds that key **by name**, prints which
key it bound plus the artifact's own provenance and caveat, and **refuses on ambiguity**. A loader
that silently picks a nested dict is one schema change from a clean, confident, wrong tie-out.
No vendor call added -- still a file input, so the tool still cannot become a vendor caller.

## The relay became a corroboration

$456,773,323.40 against the predecessor's $456.8M -- fresh run, different session, different run id.
It is evidence rather than an echo **only because the two were kept apart**.

## The full population inverts what I reported at 2203Z

| pct BD-vs-ours, 199 groups | |
|---|---:|
| min | -0.01% |
| Q1 | +10.28% |
| **median** | **+29.11%** |
| Q3 | +51.11% |
| max | +117,808.82% |
| **Travis** | **+21.02% (below median)** |

| component | sum | share |
|---|---:|---:|
| **MEMBERSHIP** (L1-L2) | $1,895,250,943.97 | **90.8%** |
| VALUATION (L2-L3) | $191,302,323.96 | 9.2% |

**24 groups tie BD's EMV to our `net_mv_plus_cash` TO THE CENT** (22 of 24 with a complete export
roster), while the export's `Account Market Value` disagrees by $1,964,099.38 on those same groups --
corroborating the positions-grain finding from a different direction. The 20 widest groups average an
**L1/L2 ratio of 20.08x**; the exact-tie groups average 5.3 accounts.

**Our valuation is not the problem. The export's roster is narrower than BD's group definition** --
same root as dim 436, one vendor-config remedy for both.

## Two lines held deliberately

1. The **215-vs-201 roster difference** is recorded as a STATED, UNADJUDICATED scope difference, with
   CRO~A's instruction not to call either instrument defective quoted rather than paraphrased.
2. **90.8% is a measured component share**, not a claim that the missing members BELONG in our book --
   that is a definitional question for the ruled basis, not mine.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `.tools/commit-gate.sh` | oracle after the loader change | PASS -- clean |
| `.tools/proof-of-spec-check.py` | T1 instance after the L1 update | PASS -- VALID rc=0, 4/4 |
| the oracle itself | `--qt6 <CRO~A artifact>` over 201 groups | PASS -- 200 groups tied, provenance + caveat printed from the artifact |

**What worked:** treating the delivered artifact as a contract to be inspected, not a shape to be
assumed. **What failed:** nothing. **Gap found:** none new.

## Blockers

**None.** Only dim 436 remains, at Andrew via COO; nothing I built depends on it arriving.

## Next Steps

1. [`4.0.0_SA_CRO~A`] Accepted their offer: the group-level `BMV + NetFlows - Fees vs EMV` identity.
   I asked specifically whether the residual concentrates in the wide-L1/L2 groups (roster) or is
   flat (convention) -- either answer is useful and I have no stake in which.
2. [`2.0.0_SA_COO`] The membership finding strengthens the existing dim-436 ask rather than adding a
   second one; both are template 390224's selection.
3. [`0.4.0_DS_ClientPlatform~B`] Nothing owed. Event-driven.
