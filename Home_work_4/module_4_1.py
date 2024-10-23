from fake_math import divide as div_f
from true_math import divide as div_t

res_1 = div_f(69, 3)
res_2 = div_f(3, 0)
res_3 = div_t(49, 7)
res_4 = div_t(15, 0)

print(res_1)
print(res_2)
print(res_3)
print(res_4)