pool = None

def pmap(njobs=1):
  global pool

  if njobs > 1:
    try:
      import multiprocess
    except:
      raise Exception('Parallel processing requires the pathos multiprocess library.')
    if not pool:
      pool = multiprocess.Pool(njobs)
    return pool.map
  else:
    return map
