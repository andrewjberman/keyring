# 2.0.0_SA_COO~K2 drive log -- 2026-10-08 11Z (desktop-n8rjv0a)

IRPT_CUSTDY tick lines from org/mcp/drive_ticks/2.0.0_SA_COO~K2.md:

- 2026-10-08T11:1xZ | own defect, fixed: a 'timeout 280' wrapper killed safe-commit after staging my 09Z/10Z logs, leaving 2 of my paths staged in the shared index (blocking other seats). Unstaged them once the foreign lock released (no foreign commit swept them), then committed without a kill timeout @5237430ff8; index 0 staged. Rule for this seat: never wrap safe-commit in timeout.
