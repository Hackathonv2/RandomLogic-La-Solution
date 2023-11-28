



from fractions import Fraction
upper = []
n_upper = int(lines[0])
for i in range(n_upper):
    x, y = map(int, lines[i+1].split())
    upper.append((x,y))
    

lower = []
n_lower = int(lines[n_upper+1])
for i in range(n_lower):
    x, y = map(int, lines[i+n_upper+2].split())
    lower.append((x,y))

double_tot_area = 0
for (x1, y1), (x2, y2) in zip(upper, upper[1:]):
    double_tot_area += (x2 - x1) * (y2 + y1)
for (x1, y1), (x2, y2) in zip(lower, lower[1:]):
    double_tot_area += (x2 - x1) * abs(y2 + y1)

assert upper[0] == lower[0] and upper[-1] == lower[-1]


x_interpol = set()
for x,y in upper:
    x_interpol.add(x)
for x,y in lower:
    x_interpol.add(x)

interpol = []
upper_i = lower_i = 0
for x in sorted(x_interpol):
    while x > upper[upper_i+1][0]:
        upper_i += 1
    x1, y1 = upper[upper_i]
    x2, y2 = upper[upper_i+1]
    y_upper = Fraction((x-x1)*(y2-y1), x2-x1) + y1
    
    while x > lower[lower_i+1][0]:
        lower_i += 1
    x1, y1 = lower[lower_i]
    x2, y2 = lower[lower_i+1]
    y_lower = Fraction((x-x1)*(y2-y1), x2-x1) + y1

    interpol.append((x, y_upper, y_lower))

for target_area in (Fraction(double_tot_area, 6), Fraction(double_tot_area, 3)):
    area_so_far = Fraction(0)
    for (x1, yu1, yl1), (x2, yu2, yl2) in zip(interpol, interpol[1:]):
        seg_area = Fraction((x2 - x1) * (yu1 + yu2 - yl1 - yl2), 2)
        if area_so_far + seg_area < target_area:
            area_so_far += seg_area
        else:
            lo = x1
            hi = x2
            while hi-lo > 1e-12:
                x = Fraction(lo + hi, 2)
                y_upper = Fraction((x-x1)*(yu2-yu1), x2-x1) + yu1
                y_lower = Fraction((x-x1)*(yl2-yl1), x2-x1) + yl1
                new_area = Fraction((x - x1) * (yu1 + y_upper - yl1 - y_lower), 2)
                
                if area_so_far + new_area > target_area:
                    hi = x
                else:
                    lo = x
            print(f'{float(lo):.11f}')
            break


