# ANDREW-DIRECT — GO on the bd↔cot key-prefix gate candidate

**Channel:** Andrew-direct at the 1.0.0_SA_CTO terminal, 2026-08-11 ~0605Z.
**Verbatim:** > "Go ahead with your rec on the open call"
**The open call as put (the only one named at him at that moment):** the bd↔cot gate candidate —
`ds-precommit-check.py` blocks foreign BUCKET names only and is blind to cross-firm reads under
the shared `opal-data-assets/blackdiamond/` vendor prefix; rec = extend the gate's foreign
reference tuples to KEY PREFIXES.

**IMPLEMENTED same window (this commit):** `_CROSS_FIRM_FOREIGN_KEY_PREFIXES` —
`data/cot/` may not reference `blackdiamond/49f/`; `data/black_diamond/` may not reference
`blackdiamond/cottonwood/`. Trailing-slash matching mirrors `_is_real_bucket_ref`'s
no-bare-substring design; docstrings remain skipped. **Exercised pre-commit: 3/3 controls**
(cross-firm mutant BLOCKs in both directions; own-firm clean file PASSes). Scope kept to the
MEASURED collision (the shared blackdiamond prefix); schwab/{08242234,08335338} product-account
prefixes are a FOLLOW-ON candidate, not implemented — they are a product split, not the bd↔cot
firm pair this gate enforces. IAM half (runtime deny below the bucket) remains open on the CTO
roster. Per the gate-acceptance law: accepted on observed behavior going forward, not on this
authoring commit — the first real BLOCK or clean pass on live traffic is the acceptance event.
