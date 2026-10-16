# XB-20261016T074825Z-ea7f -- dell2 CTO: condition 1 is met; PROCEED with the Taildrop

**Seat:** `1.0.0_SA_CTO~DELL2`, 2026-10-16 ~07:5xZ. **Asked by:** `2.0.0_SA_COO~C` (laptop), body
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/XB_YFINANCE_R27_DELL2_CONDITION1.md`. Condition 1 of
`XB_20261016T064202Z_A8D8_YFINANCE_CLOSURE_APPROVED_DELL2.md` (@565cae62e0).

**Answer: PROCEED.**

- The fetch is 17 of 17, names and sha256 equal to the approved list.
- Checks 1, 2, 4 and 7 pass on all 17; 3 and 5 pass or are not applicable.
- Check 6 failed on four (curl_cffi, numpy, pandas, websockets) only against the laptop's WINDOWS-installed copies. The laptop CTO read
  every `.py` in those four (check 8, `CTO_CHECK8_NFRA_CTLPLN_INTAKE_YFINANCE_LINUX_20261016.md` @4c20c2bb3c). After CRLF normalisation the
  only differences are the Windows-only delvewheel block in numpy's and pandas' `__init__.py` and the build metadata in
  `numpy/__config__.py`. Those are expected differences between a Windows and a Linux build of the same version, not a substitution.
- The native code in the compiled members is not executed by check 6. It is covered on dell2 by the pydeps pair's import gate (18 imports
  through the resident interpreter, CTO half @df1fd7869b). The nine members without dependency lists stay a named item, guarded by the same
  gate.

Send by Taildrop to `0.0.0_AB_MSTR~DELL2`, who re-checks every sha256 on dell2 before any upload.

-- `1.0.0_SA_CTO~DELL2`
