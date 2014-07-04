
fn_minus_1 = 1
fn = 2
fn_plus_1 = fn

LIMIT = 4000000

sigma = 0

while fn_plus_1 <= LIMIT:
    if fn_plus_1 % 2 == 0:
        sigma += fn_plus_1
    fn_plus_1 = fn_minus_1 + fn
    fn_minus_1 = fn
    fn = fn_plus_1

print sigma
