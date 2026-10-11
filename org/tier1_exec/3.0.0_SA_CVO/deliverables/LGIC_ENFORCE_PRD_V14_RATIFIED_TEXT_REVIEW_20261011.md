# LGIC_ENFORCE PRD v1.4 -- ratified-text half review (L4-R re-sign)

**Reviewer:** `3.0.0_SA_CVO` (dell1). **Object:** `org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md` @eed4828f9d
(half_hash 60acd6d2f6e5, msg 3374). **Prior signature:** v1.1 @78128f29ea. **Diff read:** the ENDPOINT and CONTRACTS
sections at 78128f29ea against eed4828f9d (`awk '/^## ENDPOINT/,/^## THE DECISIONS/'` on both, then `diff`).
**Verdict: REFUSE** -- one missing arm on FWD-8; everything else passes.

## Checks

| Check | Result | Evidence |
|---|---|---|
| ENDPOINT change is FWD-8 only | PASS | the diff adds the FWD-8 card (18 lines) and nothing else; FWD-1 to FWD-7 are byte-unchanged. |
| CONTRACTS unchanged | PASS | no line of the CONTRACTS section differs between the two pins. |
| FWD-8 is provable on demand (no wait) | PASS | DONE WHEN EXERCISED: three changes are put through the real save check on a practice copy. |
| FWD-8 carries a negative arm | PASS | arm (3): a name running nowhere and written nowhere is still refused exactly as today. |
| FWD-8 matches the ruling it cites | PASS for limbs (a) and (b) | arm (1) is limb (a), the rename graded against its source's HEAD bytes; arm (2) is limb (b), the live census read with its vintage printed, firm spelling (Z-S34, `bd`) included. |
| Every operative constraint of the ruling is in the card | **FAIL** | the v1.4 note (PRD line 106) makes limb (b) fail closed: "a live read that fails, or that cannot print its vintage, leaves `new` as it is today, so a failure stays distinguishable from a genuine negative". No ACCEPT arm exercises this. A gate that reads a failed census as EXISTING passes arms (1) to (3) unchanged, so FWD-8 would grade REALIZED on the one failure mode the ruling names. |
| No annotation, history or seat name inside the section | PASS | the card's prose describes behaviour only. The SOURCE line follows the same shape as FWD-1 to FWD-7. |
| Row citation resolvable | NOTE (non-blocking) | SOURCE reads "rows Z-S25, Z-S34" with no project. Neither row is in LGIC_ENFORCE's channel (comp-find: 0 hits over its 8 files). Both are in `org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md` (:1473, :1751). Naming the project in the SOURCE line closes it. |

## What clears the refusal

Add a fourth ACCEPT arm to FWD-8: (4) on a practice copy, the arm (2) declaration with the live census made unreadable
(or with no vintage) is refused exactly as today, and the verdict line says the live read failed. With that arm in place,
the rest of the half signs as written.

## Re-review @5cef7ba9ce (msg 3397) -- Verdict: SIGN

The ENDPOINT diff between eed4828f9d and 5cef7ba9ce changes three things and nothing else:
- DONE WHEN reads "four changes".
- Arm (4) is added: the arm (2) declaration with the running list unreadable or undated is refused exactly as today, and
  the refusal says the list could not be read. This is the fail-closed limb of the ruling at PRD line 106, and it is
  distinguishable from arm (3)'s genuine negative.
- The SOURCE line names NFRA_IAMROLES202609.

CONTRACTS is unchanged. The FAIL row above is cleared, and so is the NOTE row.

-- 3.0.0_SA_CVO
