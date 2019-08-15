import gc
objs = gc.get_objects()
print ('{} objects before'.format(len(objs)))

ref = 'Test ' * 10000000
objs = gc.get_objects()
print ('{} objects after'.format(len(objs)))
for obj in objs[:3]:
    print(repr(obj)[:100])


import tracemalloc
tracemalloc.start(5) # 5 stack frames

t1 = tracemalloc.take_snapshot()
ref = 'Test ' * 10000000
t2 = tracemalloc.take_snapshot()
stats = t2.compare_to(t1, 'lineno')
for stat in stats[:3]:
    print(stat)

stats = t2.compare_to(t1, 'traceback') # to figure out which particular usage of common function is responsible for memory consumption
top = stats[0]
print('\n'.join(top.traceback.format()))

