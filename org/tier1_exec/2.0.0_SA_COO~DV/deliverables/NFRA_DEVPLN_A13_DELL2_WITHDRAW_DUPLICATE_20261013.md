# NFRA_DEVPLN act A13 -- withdraw dell2's duplicate approval row (for 1.0.0_SA_CTO~DELL2's seat)

Issuer: `2.0.0_SA_COO~DV`, 2026-10-13. Ground: relay from `0.0.0_AB_MSTR` (bus 4ac17c50, CTO~DELL2 msg 7302): dell2 registered `cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal` twice, `dell2-20261013T221352Z-cffa` (keep) and `dell2-20261013T221411Z-3635` (the duplicate), and an approval row could end only as approved or declined. Cell `DP-e-1` (merged `8d1e6fe12f`) adds the third ending, `withdrawn`, which is not a decision on the feature.

## Precondition (on dell2)

`python .tools/open-calls.py close --help` must name `withdrawn` in its `--decision` choices. If it does not, stop: dell2's checkout predates `8d1e6fe12f`; its box-sync brings it (the tool is on origin/box/laptop and CLOUD). Do not close the duplicate `declined`.

## The command (run on dell2, from the workspace root)

```
python .tools/open-calls.py close --id dell2-20261013T221411Z-3635 --ruled-by cto --ruling <a ruling file the CTO~DELL2 lane writes: "3635 is a duplicate registration of the same branch as cffa; withdrawn, NOT a decision on the feature"> --decision withdrawn
```

It prints `CLOSED id=dell2-20261013T221411Z-3635 ... decision=withdrawn`. A withdraw ends only an OPEN row; it is refused on a closed one.

## Read-back (from any box, including the laptop)

`python .tools/open-calls.py approval-status --branch cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal` then reads `row=dell2-20261013T221352Z-cffa state=OPEN` (the newest NON-withdrawn row). Andrew then rules the one remaining row, `cffa`, on the open-calls list. Report the read-back line to `2.0.0_SA_COO~DV`.

Until the withdraw is run, leave both rows OPEN and do not register again; the route reads the newest row, `3635`.
