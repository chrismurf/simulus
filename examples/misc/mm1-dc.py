import simulus, random

random.seed(123)

def job():
    r.acquire()
    sim.sleep(random.expovariate(1.1))
    r.release()

def arrival():
    while True:
        sim.sleep(random.expovariate(1))
        sim.process(job)

sim = simulus.simulator()

dc = simulus.DataCollector(
    arrivals='timemarks(all)', 
#    services='timemarks()',
#    reneges='timemarks', 
#    departs='timemarks(all)',
    inter_arrivals='runstats()',
#    queue_times='runstats',
#    renege_times='runstats',
    service_times='runstats',
    system_times='runstats(all)',
    in_systems='timeseries(all)',
#    in_services='timeseries',
    in_queues='timeseries(all)'
)
r = sim.resource(collect=dc)

sim.process(arrival)
sim.run(1000)
dc.report(sim.now)
