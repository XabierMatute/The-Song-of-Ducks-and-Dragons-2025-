input = """
619
608|608
592|1184
582|582
576|2304
573|573
568|2272
567|567
563|1689
562|562
551|1102
545|545
527|1054
513|513
511|2044
508|508
490|1470
479|479
467|1868
459|459
458|458
445|445
432|864
428|428
421|842
420|420
415|1660
402|402
383|766
375|375
374|1496
369|369
356|356
353|353
341|1023
338|338
324|324
307|307
302|604
294|294
293|1172
283|283
282|282
263|263
253|506
234|234
225|225
209|209
191|573
171
"""

first_gear = int(input.strip().split("\n")[0])
gears = list(input.strip().split("\n")[1:-1])
print(gears)
gears = [[int(gear.split("|")[0]), int(gear.split("|")[1])] for gear in gears]
print(gears)
last_gear = int(input.strip().split("\n")[-1])
factor = 1
previous_gear = first_gear
print("hola", previous_gear)
for gear in gears:
    print("gear", gear)
    factor *= previous_gear / gear[0]
    print("factor", factor)
    previous_gear = gear[1]
    print(previous_gear)


print(previous_gear)

factor *= previous_gear / last_gear
print(factor)
print(100 * factor)