# Inflection membership census repair

Current control: CONTRACT.md v1.4 / COO_M.md / CONTROL.md@c7265d2bef,
consumed from exact CTO inbox20260923T194210Z. Baseline35999d31a4.

Fresh source receipt census in HOLDINGS_SOURCE_CHECK_20260923.json reports14
full Eclipse portfolios with multiple associated accounts while the flattened
simple feed exposes only one per portfolio. The existing build_inf used only
the flattened count to decide whether portfolio value could be attributed to
an account. A coincidental value tie could therefore conceal incomplete membership.

Repair: require a positive integral numeric full.num_of_associated_accounts
matching the observed simple membership census. Missing, boolean, string,
nonintegral, nonpositive or mismatched counts keep custody value UNRESOLVED.
No proportional allocation and no new currency/value assumptions. Confirmed
single-account membership still permits the existing account-level assignment;
this is not evidence of individual-security membership.

Validation: full producer suite188 PASS. Seven adversarial controls retain
$100 custody without a model node despite a perfect portfolio value tie;
an explicit matching singleton is the positive control. The preexisting
managed/excluded regression now provides full's actual count field rather than
relying on absent evidence. No tolerance or production acceptance check weakened.

First unclosed hop remains actual positions -> accepted source-bound snapshot.
The current builder does not consume positions_mv; source-backed currency is
unresolved. CRO received the exact source request while M continues implementation.
No AWS/vendor mutation, publication, deployment or browser PASS is claimed.
