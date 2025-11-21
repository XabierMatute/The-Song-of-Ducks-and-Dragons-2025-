input = """
993
973
961
953
927
902
892
888
872
855
852
833
831
827
826
815
793
780
776
754
732
714
699
681
680
658
634
633
615
598
569
563
551
539
536
523
507
485
468
445
425
420
411
407
380
374
353
346
317
289
289
"""

gears = list(map(int, input.strip().split("\n")))
print(gears)
factor = 1
previous_gear = gears[0]
for gear in gears[1:]:
    factor *= previous_gear / gear
    previous_gear = gear

print(factor)
print(10000000000000 / factor)